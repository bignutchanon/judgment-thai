#!/usr/bin/env python3
"""สร้าง title_root.bin ทดสอบ **รอบ 3** — เจาะฟอนต์หน้าไตเติล `meta_ot_cond_book`

รอบ 1 (donor Cyrillic + real-cp บน tbgm_0p_ja) ขึ้นว่างทุกแถว เพราะหน้าไตเติลไม่ได้วาด
ด้วย tbgm_0p_ja — atlas ของไตเติลมีแค่ Latin/Latin-1/Latin-Ext-A (ดู title_slotmap.py)
รอบนี้จึง encode ด้วย donor ในตารางของไตเติลเอง 2 กลุ่ม:

  A = เซลล์ที่มีหมึกอยู่แล้ว (À-Ï, U+00C0+)   B = เซลล์ว่างของ Latin Ext-A (U+0102+)

`quit_game` กับ `judge_photo_gallery` ใช้ **ข้อความเดียวกัน** ("ออกจากเกม" ไม่มีมาร์กเลย)
คนละกลุ่ม → ภาพเดียวเทียบ A กับ B ได้ตรง ๆ ทั้งเรื่อง "ขึ้นไหม" และ "ระยะห่างเท่ากันไหม"

ใช้:  python scripts/make_spoil_title2.py
อ่าน  extracted/db_en/en/title_root.bin (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/title_root.bin + build/text/SPOIL_MAP_v3.md
"""
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from title_slotmap import encode

SRC = paths.EXTRACTED / "db_en" / "en" / "title_root.bin"
STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / "_work_v3"

# (row_key, field, ข้อความไทย, กลุ่ม donor, สิ่งที่แถวนี้ตอบ)
EDITS = [
    ("quit_game", "name", "ออกจากเกม", "A",
     "ไทยขึ้นไตเติลไหม + ระยะห่าง (ไม่มีมาร์ก = อ่านง่ายสุด)"),
    ("judge_photo_gallery", "name", "ออกจากเกม", "B",
     "ข้อความเดียวกับข้างบนแต่ลงเซลล์ว่าง — เติมเซลล์ว่างได้ไหม"),
    ("judge_new_game", "name", "เริ่มเกมใหม่", "A", "มาร์กบนเซลล์มีหมึก — advance 0 หรือแยกตัว"),
    ("judge_option", "name", "ตั้งค่า", "A", "มาร์กซ้อน 2 ชั้น (ั + ้)"),
    ("judge_load", "name", "เล่นต่อ", "B", "มาร์กบนเซลล์ว่าง"),
    # judge_movie / judge_premium_adventure / profile_change = ไม่แตะ (ตัวควบคุม EN)
]


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    STAGE.mkdir(parents=True, exist_ok=True)
    work_bin = WORK / "title_root.bin"
    shutil.copy2(SRC, work_bin)

    r = subprocess.run([sys.executable, str(paths.REARMP), str(work_bin)],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP export ล้ม: {r.stderr[-400:]}"
    work_json = WORK / "title_root.bin.json"
    assert work_json.exists(), "ไม่พบ json ที่ export"

    data = json.loads(work_json.read_text(encoding="utf-8"))
    by_key = {}
    for k, v in data.items():
        if isinstance(v, dict) and len(v) == 1:
            row_key = next(iter(v))
            by_key.setdefault(row_key, []).append(k)

    report = ["# SPOIL_MAP v3 — title_root.bin (เจาะฟอนต์ไตเติล meta_ot_cond_book)\n",
              "ฟอนต์ที่ต้อง deploy คู่กัน: `build/font/meta_ot_cond_book.dds`",
              "(กลุ่ม A = เซลล์มีหมึก U+00C0+ · กลุ่ม B = เซลล์ว่าง U+0102+)\n",
              "| เมนู | ข้อความไทย | กลุ่ม | สตริงที่เขียนลง bin | ตอบคำถาม |",
              "|---|---|---|---|---|"]
    for row_key, field, thai, group, question in EDITS:
        ids = by_key.get(row_key)
        assert ids, f"ไม่พบแถว {row_key}"
        assert len(ids) == 1, f"แถว {row_key} ซ้ำ: {ids}"
        row = data[ids[0]][row_key]
        assert field in row, f"{row_key} ไม่มีช่อง {field}"
        enc = encode(thai, group)
        row[field] = enc
        report.append(f"| {row_key}.{field} | {thai} | {group} | `{enc}` | {question} |")

    work_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    r = subprocess.run([sys.executable, str(paths.REARMP), str(work_json)],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP rebuild ล้ม: {r.stderr[-400:]}"
    rebuilt = WORK / "title_root.bin.json.bin"
    assert rebuilt.exists(), "ไม่พบ bin ที่ rebuild (<json>.bin)"

    out_bin = STAGE / "title_root.bin"
    shutil.copy2(rebuilt, out_bin)
    print(f"เขียน {out_bin} ({out_bin.stat().st_size} B, ต้นฉบับ {SRC.stat().st_size} B)")

    blob = out_bin.read_bytes()
    for row_key, field, thai, group, _q in EDITS:
        needle = encode(thai, group).encode("utf-8")
        assert needle in blob, f"ข้อความ {row_key}.{field} ไม่อยู่ใน bin ที่ rebuild"
    print("ตรวจกลับ OK: ข้อความครบทุกแถว")

    (paths.BUILD / "text" / "SPOIL_MAP_v3.md").write_text("\n".join(report) + "\n",
                                                          encoding="utf-8")
    print("เขียน SPOIL_MAP_v3.md")


if __name__ == "__main__":
    main()
