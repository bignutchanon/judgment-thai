#!/usr/bin/env python3
"""สร้าง title_root.bin ฉบับสปอย/ทดสอบ A-B สำหรับ Judgment

แก้ชื่อเมนูหน้าไตเติล (แถว judge_* = เมนูที่เกมใช้จริง) เป็นไทย 2 แบบสลับกัน:
  - real  = ไทยแท้ (codepoint U+0E01..) — ต้องมี record real-cp ในฟอนต์ (inject_thai_judge.py)
  - donor = encode เป็น Cyrillic/Samaritan ตาม slotmap Y6 — เส้นทางที่พิสูจน์แล้วในภาคอื่น
ภาพหน้าจอเดียวจากผู้ใช้ตอบได้ทั้ง: เกมยอมรับ record ที่เพิ่มไหม / mark ลอยวางถูกไหม /
ระยะห่างตัวอักษร (half/full-width) เป็นแบบไหน

ใช้:  python scripts/make_spoil_title.py
อ่าน  extracted/db_en/en/title_root.bin (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/title_root.bin + build/text/SPOIL_MAP.md
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
from y6_slotmap import ENCODE

SRC = paths.EXTRACTED / "db_en" / "en" / "title_root.bin"
STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / "_work"


def donor_encode(s):
    out = []
    for c in s:
        if c in ENCODE:
            out.append(chr(ENCODE[c]))
        elif "฀" <= c <= "๿":
            raise SystemExit(f"ตัวอักษรไทยไม่มีใน slotmap: {c!r} (U+{ord(c):04X})")
        else:
            out.append(c)
    return "".join(out)


# (row_key, field, ข้อความไทย, mode)
EDITS = [
    ("judge_new_game", "name", "เริ่มเกมใหม่", "real"),
    ("judge_new_game", "explanation", "เริ่มเกมจากจุดเริ่มต้น", "real"),
    ("judge_load", "name", "เล่นต่อ", "donor"),
    ("judge_load", "explanation", "เล่นต่อจากเซฟที่บันทึกไว้", "donor"),
    ("judge_option", "name", "ตั้งค่า", "real"),
    ("judge_movie", "name", "ดูฉากย้อนหลัง", "donor"),
    ("judge_premium_adventure", "name", "พรีเมียมแอดเวนเจอร์", "real"),
    ("profile_change", "name", "เปลี่ยนโปรไฟล์", "donor"),
    ("judge_photo_gallery", "name", "แกลเลอรีภาพ", "real"),
    ("quit_game", "name", "ออกจากเกม", "real"),   # ไม่มี mark ลอย = ตัวควบคุม
]


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    STAGE.mkdir(parents=True, exist_ok=True)
    work_bin = WORK / "title_root.bin"
    shutil.copy2(SRC, work_bin)

    # export -> json (reARMP เขียน <ชื่อไฟล์>.json ลง cwd ของ process)
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

    report = ["# SPOIL_MAP — title_root.bin (diagnostic v1)\n",
              "| เมนู | ข้อความ | โหมด |", "|---|---|---|"]
    for row_key, field, thai, mode in EDITS:
        ids = by_key.get(row_key)
        assert ids, f"ไม่พบแถว {row_key}"
        assert len(ids) == 1, f"แถว {row_key} ซ้ำ: {ids}"
        row = data[ids[0]][row_key]
        assert field in row, f"{row_key} ไม่มีช่อง {field}"
        row[field] = thai if mode == "real" else donor_encode(thai)
        report.append(f"| {row_key}.{field} | {thai} | {mode} |")

    work_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # rebuild json -> bin (reARMP เขียน <json>.bin คู่กับไฟล์ json)
    r = subprocess.run([sys.executable, str(paths.REARMP), str(work_json)],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP rebuild ล้ม: {r.stderr[-400:]}"
    rebuilt = WORK / "title_root.bin.json.bin"
    assert rebuilt.exists(), "ไม่พบ bin ที่ rebuild (<json>.bin)"

    out_bin = STAGE / "title_root.bin"
    shutil.copy2(rebuilt, out_bin)
    orig_size = SRC.stat().st_size
    print(f"เขียน {out_bin} ({out_bin.stat().st_size} B, ต้นฉบับ {orig_size} B)")

    # ตรวจกลับ: bin ใหม่ต้องมีข้อความที่แก้จริง
    blob = out_bin.read_bytes()
    for row_key, field, thai, mode in EDITS:
        needle = (thai if mode == "real" else donor_encode(thai)).encode("utf-8")
        assert needle in blob, f"ข้อความ {row_key}.{field} ไม่อยู่ใน bin ที่ rebuild"
    print("ตรวจกลับ OK: ข้อความครบทุกแถว")

    (paths.BUILD / "text" / "SPOIL_MAP.md").write_text("\n".join(report) + "\n",
                                                       encoding="utf-8")
    print("เขียน SPOIL_MAP.md")


if __name__ == "__main__":
    main()
