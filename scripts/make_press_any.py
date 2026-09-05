#!/usr/bin/env python3
"""แก้แถว "Press any button" ใน `ui_text.bin` เป็นไทย ด้วย donor ของ **ฟอนต์ไตเติล**

ทำไมต้องมีสคริปต์แยก: จอโลโก้ก่อนเข้าไตเติลไม่ได้อยู่ใน `title_root.bin` และรอบก่อนหน้า
(รอบ 2) เขียนแถวนี้เป็น **codepoint ไทยจริง** ซึ่งใช้ได้เฉพาะกับฟอนต์ `tbgm_0p_ja` ที่เรา
เพิ่ม record ไทยเข้าไป — ผลคือจอนั้นขึ้นว่างเปล่า แปลว่าจอโลโก้ไม่ได้วาดด้วย tbgm

รอบนี้จึงเขียนแถวเดียวกันด้วย donor ของ `meta_ot_cond_book` (ชุดเดียวกับเมนูไตเติลที่พิสูจน์
แล้วว่าขึ้นจอ) เพื่อตอบว่า **จอโลโก้ใช้ฟอนต์ไตเติลหรือฟอนต์อื่น**:
  - ขึ้นเป็นไทยอ่านออก  -> จอโลโก้ใช้ meta_ot_cond_book เหมือนเมนูไตเติล
  - ยังว่างเปล่า        -> เป็นฟอนต์ตัวที่สาม (น่าจะ `yakuza.dds` ที่ไม่มี .bin — กับดักแบบ Y6 §8)

ใช้:  python scripts/make_press_any.py
อ่าน  extracted/db_en/en/ui_text.bin (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/ui_text.bin
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
from title_menu_map import ENCODE, EXTRA

SRC = paths.EXTRACTED / "db_en" / "en" / "ui_text.bin"
STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / "_work_ui"

ROW_ID = "1889"                 # แถว "Press any button" (ยืนยันด้วย diff กับต้นฉบับ)
ORIG_TEXT = "Press any button"


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    STAGE.mkdir(parents=True, exist_ok=True)
    work_bin = WORK / "ui_text.bin"
    shutil.copy2(SRC, work_bin)

    r = subprocess.run([sys.executable, str(paths.REARMP), work_bin.name],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP export ล้ม: {r.stderr[-400:]}"
    work_json = WORK / "ui_text.bin.json"
    assert work_json.exists(), "ไม่พบ json ที่ export"

    data = json.loads(work_json.read_text(encoding="utf-8"))
    row = data[ROW_ID][""]
    assert row.get("text") == ORIG_TEXT, \
        f"แถว {ROW_ID} ไม่ใช่ {ORIG_TEXT!r} แต่เป็น {row.get('text')!r} — ต้องหาแถวใหม่ก่อน"

    thai = EXTRA["press_any_button"]
    enc = encode(thai, ENCODE)
    row["text"] = enc
    work_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    r = subprocess.run([sys.executable, str(paths.REARMP), work_json.name],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP rebuild ล้ม: {r.stderr[-400:]}"
    rebuilt = WORK / "ui_text.bin.json.bin"
    assert rebuilt.exists(), "ไม่พบ bin ที่ rebuild"

    out = STAGE / "ui_text.bin"
    shutil.copy2(rebuilt, out)
    assert enc.encode("utf-8") in out.read_bytes(), "สตริงที่แก้ไม่อยู่ใน bin ที่ rebuild"
    print(f"เขียน {out} ({out.stat().st_size} B) · แถว {ROW_ID}: {ORIG_TEXT!r} -> {thai} ({enc!r})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
