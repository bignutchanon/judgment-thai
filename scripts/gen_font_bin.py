#!/usr/bin/env python3
"""สร้าง `en/font.bin` ใหม่ — เขียน advance/ตำแหน่งของทุกเซลล์ไทยลง `kerning_table`

นี่คือชิ้นส่วนที่ทำให้สถาปัตยกรรมรอบ 16 เป็นไปได้: ตารางความกว้างของฟอนต์ไม่ได้อยู่ใน
`Judgment.exe` อย่างที่เคยเชื่อ แต่อยู่ใน

    data/db.judge.en.par → en/font.bin → แถว "meta_ot_cond_book" → คอลัมน์ kerning_table

เป็นตาราง ARMP ซ้อน 332 แถว x 6 คอลัมน์ float = 3 คู่ (L, R) สำหรับขนาดวาด 3 แบบ
(ที่มา สูตร และหลักฐานทั้งหมด: `scripts/font_metrics.py`)

สคริปต์นี้:
  1. อ่าน `extracted/db_en/en/font.bin.json` (ต้นฉบับ — ไม่แตะ)
  2. ทับค่า (L, R) ของทุกเซลล์ที่ `translations/slotmap.json` ยึดไป **ลงครบทั้งสามคู่**
     (เมนูไตเติลใช้คู่ (5,6) · แถบภารกิจใช้คู่ (3,4) — เขียนเท่ากันหมดทุกชั้นจึงระยะเท่ากัน)
  3. แถวของเซลล์ที่เราไม่ได้ยึด **คงค่าเดิมทุกตัว** (ข้อความอังกฤษที่เก็บไว้ต้องไม่ขยับ)
  4. encode กลับด้วย reARMP ลง `build/text/db.judge.en/en/font.bin`

ใช้:  python scripts/gen_font_bin.py            # สร้างไฟล์
      python scripts/gen_font_bin.py --check    # ตรวจอย่างเดียว ไม่เขียน
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import struct

import paths
import font_metrics as FM
from slot_alloc import SlotMap
from patch_text_inplace import (H_PCOL_CONTENT, H_PCOL_TYPES_AUX, H_ROW_COUNT, H_STORAGE_MODE,
                                MAIN_PTR_OFF, _i32)

SRC_BIN = paths.EXTRACTED / "db_en" / "en" / "font.bin"
KERN_COL = 2                       # คอลัมน์ kerning_table ของตารางหลัก (ชนิด 9 = ตารางย่อย)
FLOAT_COLS = (1, 2, 3, 4, 5, 6)    # 3 คู่ (L, R)

SRC_JSON = paths.EXTRACTED / "db_en" / "en" / "font.bin.json"
OUT_BIN = paths.BUILD / "text" / "db.judge.en" / "en" / "font.bin"
FONT_ROWS = ("meta_ot_cond_book", "meta_ot_cond_book_italic")


def patch_kerning(table, rows):
    """ทับค่า (L, R) ลงทั้งสามคู่คอลัมน์ -> จำนวนแถวที่แก้"""
    n = 0
    for idx, (L, R) in sorted(rows.items()):
        key = str(idx)
        assert key in table, (
            f"เซลล์ {idx} เกิน {table['ROW_COUNT']} แถวของ kerning_table — "
            f"donor ตัวนี้เอนจิ้นวาดไม่ได้ (ดู build_pool ใน slot_alloc.py)")
        cell = table[key]
        row = cell[list(cell)[0]]
        for c, v in ((1, L), (2, R), (3, L), (4, R), (5, L), (6, R)):
            row[str(c)] = float(v)
        n += 1
    return n


def rearmp_encode(json_path, work):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    res = subprocess.run([sys.executable, str(paths.REARMP), json_path.name],
                         cwd=str(work), env=env, stdout=subprocess.DEVNULL,
                         stderr=subprocess.PIPE, timeout=600)
    out = work / (json_path.name + ".bin")
    if res.returncode != 0 or not out.exists() or out.stat().st_size == 0:
        raise SystemExit("reARMP ล้มเหลว: " + (res.stderr or b"").decode("utf-8", "replace")[-400:])
    return out


def _row_ptr(buf, tbl, r):
    """storage mode 1 (row-major): พอยน์เตอร์ของแถว r"""
    assert buf[tbl + H_STORAGE_MODE] == 1, "คาดว่า font.bin ทุกตารางเป็น storage mode 1"
    return _i32(buf, _i32(buf, tbl + H_PCOL_CONTENT) + 4 * r)


def _col_shift(buf, tbl, c):
    return _i32(buf, _i32(buf, tbl + H_PCOL_TYPES_AUX) + c * 16 + 4)


def kern_table_offsets(buf, row_names):
    """{ชื่อฟอนต์: ออฟเซ็ต header ของ kerning_table} จากตารางหลัก (ค้นด้วยเลขแถวในต้นฉบับ)"""
    main = _i32(buf, MAIN_PTR_OFF)
    shift = _col_shift(buf, main, KERN_COL)
    out = {}
    for idx, name in row_names.items():
        sub = _i32(buf, _row_ptr(buf, main, idx) + shift)
        assert sub > 0, "แถว %s ไม่มี kerning_table" % name
        out[name] = sub
    return out


def patch_inplace(buf, tables, rows):
    """เขียน (L, R) ลงคอลัมน์ 1-6 ของทุกเซลล์ที่ยึด ในทุกตาราง kerning_table -> (bytes, จำนวนเซลล์ที่แก้)"""
    out = bytearray(buf)
    n = 0
    for name, tbl in tables.items():
        n_rows = _i32(buf, tbl + H_ROW_COUNT)
        shifts = {c: _col_shift(buf, tbl, c) for c in FLOAT_COLS}
        for idx, (L, R) in sorted(rows.items()):
            assert idx < n_rows, ("เซลล์ %d เกิน %d แถวของ kerning_table — donor ตัวนี้เอนจิ้นวาดไม่ได้"
                                  % (idx, n_rows))
            rp = _row_ptr(buf, tbl, idx)
            for c, v in ((1, L), (2, R), (3, L), (4, R), (5, L), (6, R)):
                struct.pack_into("<f", out, rp + shifts[c], float(v))
            n += 1
    return bytes(out), n


def verify_inplace(built, data, rows):
    """decode ไฟล์ที่ patch แล้วเทียบกับ JSON ต้นฉบับทุกเซลล์ — ต่างได้เฉพาะเซลล์ที่ตั้งใจแก้ · ไบต์นอกเซลล์ต้องเท่าเดิม"""
    from patch_text_inplace import _cells, _decode
    src = SRC_BIN.read_bytes()
    assert len(built) == len(src), "ขนาดไฟล์เปลี่ยน (%d != %d)" % (len(built), len(src))
    work = Path(tempfile.mkdtemp(prefix="jeth_fontchk_"))
    try:
        p = work / "font.bin"
        p.write_bytes(built)
        got = _cells(_decode(p, work, "a"))
    finally:
        shutil.rmtree(work, ignore_errors=True)
    ref = _cells(data)
    want = {}
    for r in data:
        if r.isdigit() and list(data[r])[0] in FONT_ROWS:
            name = list(data[r])[0]
            for idx, (L, R) in rows.items():
                for c, v in ((1, L), (2, R), (3, L), (4, R), (5, L), (6, R)):
                    want["/%s/%s/kerning_table/%d//%d" % (r, name, idx, c)] = struct.unpack("<f", struct.pack("<f", v))[0]
    bad = []
    for k in sorted(set(got) | set(ref)):
        a, b = got.get(k), ref.get(k)
        if a == b:
            continue
        if k in want and a == want[k]:
            continue
        bad.append((k, a, b))
    n_changed = sum(1 for k in want if got.get(k) != ref.get(k))
    diff_bytes = sum(1 for i in range(len(src)) if src[i] != built[i])
    print("ตรวจกลับ: เซลล์ %s · เซลล์ที่ตั้งใจแก้ %d (เปลี่ยนจริง %d) · ผิดคาด %d · ไบต์ที่ต่างจากต้นฉบับ %d (สูงสุดที่เป็นไปได้ %d)"
          % ("{:,}".format(len(ref)), len(want), n_changed, len(bad), diff_bytes, 4 * len(want)))
    for k, a, b in bad[:8]:
        print("   ผิดคาด %s: patched=%r orig=%r" % (k, a, b))
    assert not bad, "ตรวจกลับไม่ผ่าน"
    assert diff_bytes <= 4 * len(want), "มีไบต์เปลี่ยนนอกเซลล์ที่ตั้งใจ"


def main():
    check_only = "--check" in sys.argv
    rebuild = "--rebuild" in sys.argv
    assert SRC_JSON.exists(), f"ไม่พบต้นฉบับ {SRC_JSON} — รัน scripts/extract_all_en.py ก่อน"
    sm = SlotMap.load()
    rows = sm.kern_rows()
    data = json.load(io.open(SRC_JSON, encoding="utf-8"))

    touched = 0
    for r in data:
        if not r.isdigit():
            continue
        entry = data[r]
        name = list(entry)[0]
        if name not in FONT_ROWS:
            continue
        touched += patch_kerning(entry[name]["kerning_table"], rows)
        print("แก้แถวฟอนต์ %-26s %d เซลล์" % (name, len(rows)))
    assert touched == len(rows) * len(FONT_ROWS), \
        f"แก้ได้ {touched} ควรได้ {len(rows) * len(FONT_ROWS)} — ชื่อแถวฟอนต์เปลี่ยน?"

    adv = [(v["text"], v["advance"]) for v in sm.cells.values()]
    n_zero = sum(1 for _t, a in adv if a == 0)
    print("advance: มาร์ก 0 px %d เซลล์ · ฐาน %d เซลล์ (%.0f-%.0f px)"
          % (n_zero, len(adv) - n_zero,
             min(a for _t, a in adv if a), max(a for _t, a in adv)))
    lr = [(v["L"], v["R"]) for v in sm.cells.values()]
    assert all(-0.2 <= L <= 2.2 and -0.2 <= R <= 2.2 for L, R in lr), \
        "มีค่า L/R หลุดช่วง 0..2 — ตรวจ INK_X0 / mark_place ใน slot_alloc.py"
    if check_only:
        print("--check: ไม่เขียนไฟล์")
        return

    if not rebuild:
        src = SRC_BIN.read_bytes()
        row_names = {int(r): list(data[r])[0] for r in data if r.isdigit() and list(data[r])[0] in FONT_ROWS}
        tables = kern_table_offsets(src, row_names)
        built, n = patch_inplace(src, tables, rows)
        print("patch ในที่: %s · %d เซลล์" % (" · ".join("%s@0x%X" % (k, v) for k, v in tables.items()), n))
        verify_inplace(built, data, rows)
        OUT_BIN.parent.mkdir(parents=True, exist_ok=True)
        OUT_BIN.write_bytes(built)
        print("เขียน %s (%d B · เลย์เอาต์ต้นฉบับ SEGA)" % (OUT_BIN, OUT_BIN.stat().st_size))
        return

    work = Path(tempfile.mkdtemp(prefix="jeth_font_"))
    try:
        tmp = work / "font.bin.json"
        io.open(tmp, "w", encoding="utf-8", newline="\n").write(
            json.dumps(data, ensure_ascii=False))
        built = rearmp_encode(tmp, work)
        OUT_BIN.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(built, OUT_BIN)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    print("เขียน %s (%d B)" % (OUT_BIN, OUT_BIN.stat().st_size))


if __name__ == "__main__":
    main()
