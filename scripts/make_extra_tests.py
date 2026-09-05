#!/usr/bin/env python3
"""แพตช์ข้อความทดสอบนอก `title_root.bin` ด้วย donor ของ **ฟอนต์ไตเติล** (`meta_ot_cond_book`)

รายการเป้าหมายอยู่ที่ `title_menu_map.EXTRA_TARGETS` (ไฟล์ bin + เส้นทางใน json + ข้อความไทย)
ใช้ตอบคำถามว่า "จอไหนวาดด้วยฟอนต์ไหน" โดยเขียนข้อความเดียวกันด้วย donor ที่พิสูจน์แล้วว่า
ขึ้นบนฟอนต์ไตเติล:
  - ขึ้นเป็นไทยอ่านออก -> จอนั้นใช้ `meta_ot_cond_book`
  - ยังว่างเปล่า      -> จอนั้นใช้ฟอนต์อื่น (tbgm_0p_ja หรือ bitmap ที่ไม่มี .bin)

ใช้:  python scripts/make_extra_tests.py
อ่าน  extracted/db_en/en/<bin> (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/<bin>
"""
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from title_encode import encode
from title_menu_map import ENCODE, EXTRA_TARGETS
from y6_slotmap import ENCODE as TBGM_ENCODE

# เป้าหมายคู่เทียบที่เขียนด้วย donor ของ **ฟอนต์ข้อความหลัก** (`tbgm_0p_ja`, Cyrillic/Samaritan)
# วางไว้จอเดียวกับเป้าหมายด้านบนเพื่อให้ภาพเดียวตอบได้ว่าจอนั้นวาดด้วยฟอนต์ไหน
TBGM_TARGETS = [
    ("msg.bin", ["10", "save_data", "table", "35", "", "1"], "โหลดเรียบร้อยแล้ว",
     "กล่องยืนยันหลังโหลด — เขียนด้วย donor ของ tbgm_0p_ja (คู่เทียบของแถวเซฟ)"),
]


def tbgm_encode(text):
    out = []
    for ch in text:
        if ch in TBGM_ENCODE:
            out.append(chr(TBGM_ENCODE[ch]))
        elif "฀" <= ch <= "๿":
            raise SystemExit(f"ไทยไม่มีใน slotmap ของ tbgm: {ch!r}")
        else:
            out.append(ch)
    return "".join(out)

STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / "_work_extra"


def _rearmp(work_dir, name):
    r = subprocess.run([sys.executable, str(paths.REARMP), name],
                       cwd=str(work_dir), capture_output=True)
    assert r.returncode == 0, f"reARMP ล้มที่ {name}: {r.stderr[-400:]}"


def patch(bin_name, targets):
    """targets: list of (path, ข้อความไทย, หมายเหตุ, encoder) ที่อยู่ในไฟล์ bin เดียวกัน"""
    work = WORK / bin_name
    work.mkdir(parents=True, exist_ok=True)
    src = paths.EXTRACTED / "db_en" / "en" / bin_name
    shutil.copy2(src, work / bin_name)
    _rearmp(work, bin_name)

    jf = work / (bin_name + ".json")
    data = json.loads(jf.read_text(encoding="utf-8"))
    done = []
    for path, thai, note, enc_fn in targets:
        node = data
        for key in path[:-1]:
            node = node[key]
        before = node[path[-1]]
        enc = enc_fn(thai)
        node[path[-1]] = enc
        done.append((path, before, thai, enc, note))

    jf.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    _rearmp(work, jf.name)
    rebuilt = work / (bin_name + ".json.bin")
    assert rebuilt.exists(), f"ไม่พบ bin ที่ rebuild ของ {bin_name}"

    STAGE.mkdir(parents=True, exist_ok=True)
    out = STAGE / bin_name
    shutil.copy2(rebuilt, out)
    blob = out.read_bytes()
    for _p, _b, _t, enc, _n in done:
        assert enc.encode("utf-8") in blob, f"สตริงที่แก้ไม่อยู่ใน {bin_name}"
    print(f"เขียน {out} ({out.stat().st_size} B)")
    for path, before, thai, enc, note in done:
        print(f"  {'/'.join(path)}: {before!r} -> {thai} ({enc!r})")
        print(f"    {note}")


def main():
    by_bin = {}
    for bin_name, path, thai, note in EXTRA_TARGETS:
        by_bin.setdefault(bin_name, []).append(
            (path, thai, note, lambda t: encode(t, ENCODE)))
    for bin_name, path, thai, note in TBGM_TARGETS:
        by_bin.setdefault(bin_name, []).append((path, thai, note, tbgm_encode))
    for bin_name, targets in by_bin.items():
        patch(bin_name, targets)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
