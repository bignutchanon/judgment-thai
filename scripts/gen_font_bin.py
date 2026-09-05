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
import paths
import font_metrics as FM
from slot_alloc import SlotMap

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


def main():
    check_only = "--check" in sys.argv
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
