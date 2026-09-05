#!/usr/bin/env python3
"""สร้าง title_root.bin ทดสอบ **รอบ 4** — วัดตาราง width ของ exe ผ่านหน้าไตเติล

คู่กับ `python scripts/inject_thai_title.py --probe` (ต้อง build ฟอนต์ก่อน)
แถวและเหตุผลทั้งหมดนิยามไว้ที่ `scripts/title_probe.py` (ROWS)

ใช้:  python scripts/make_spoil_title4.py [--map <module>]
อ่าน  extracted/db_en/en/title_root.bin (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/title_root.bin + build/text/SPOIL_MAP_v4.md
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

def _load_rows():
    """ROWS มาจากโมดูล probe ที่ระบุด้วย --map (ค่าเริ่มต้น title_probe = รอบ 4)"""
    name = "title_probe"
    if "--map" in sys.argv:
        name = sys.argv[sys.argv.index("--map") + 1]
    return name, __import__(name).ROWS


PROBE_MOD, ROWS = _load_rows()

SRC = paths.EXTRACTED / "db_en" / "en" / "title_root.bin"
STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / ("_work_" + PROBE_MOD)


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

    report = ["# SPOIL_MAP v4 — title_root.bin (วัดตาราง width ผ่านการเลือก donor)\n",
              "ฟอนต์ที่ต้อง deploy คู่กัน: `build/font/meta_ot_cond_book.dds` "
              "(build ด้วย `inject_thai_title.py --probe`)\n",
              "| เมนูเดิมบนจอ | แถว | สตริงที่เขียน | อ่านผลยังไง |",
              "|---|---|---|---|"]
    labels = {"judge_new_game": "NEW GAME", "judge_load": "CONTINUE",
              "judge_2p_match_mini_game": "VS MINIGAMES", "judge_option": "SETTINGS",
              "judge_movie": "REPLAY", "quit_game": "EXIT GAME"}
    for row_key, field, enc, question in ROWS:
        ids = by_key.get(row_key)
        assert ids, f"ไม่พบแถว {row_key}"
        assert len(ids) == 1, f"แถว {row_key} ซ้ำ: {ids}"
        row = data[ids[0]][row_key]
        assert field in row, f"{row_key} ไม่มีช่อง {field}"
        row[field] = enc
        report.append(f"| {labels.get(row_key, row_key)} | `{row_key}.{field}` | "
                      f"`{enc}` | {question} |")

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
    for row_key, field, enc, _q in ROWS:
        assert enc.encode("utf-8") in blob, f"สตริงของ {row_key}.{field} ไม่อยู่ใน bin"
    print("ตรวจกลับ OK: ครบทุกแถว")

    (paths.BUILD / "text" / f"SPOIL_MAP_{PROBE_MOD}.md").write_text("\n".join(report) + "\n",
                                                          encoding="utf-8")
    print(f"เขียน SPOIL_MAP_{PROBE_MOD}.md")


if __name__ == "__main__":
    main()
