#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตรวจ **คำลงท้ายบอกเพศในบทคัตซีน** (`auth.bin`) ที่ไม่มีข้อมูลผู้พูดในไฟล์เกม

ทำไมต้องมีตัวนี้แยกจาก `check_speaker_gender.py`: ตารางคัตซีน `auth.bin/<ฉาก>/cinema_telop`
**ไม่มีคอลัมน์ผู้พูดเลย** (ตรวจกับไฟล์จริง 22 ส.ค. 2026 — คอลัมน์มีแค่เวลาเริ่ม/จบ + ข้อความ
สองชุดคือชุดซับ JA และชุดพากย์ EN) นักแปลจึงไม่มีทางรู้เพศผู้พูดจากไฟล์ ต้องดูบริบทของฉาก
เท่านั้น → บรรทัดที่มี ค่ะ/คะ/ดิฉัน หรือ ครับ/ผม ในฉากพวกนี้คือจุดเสี่ยงที่ต้องตรวจด้วยตา

รายงานเรียงตามฉากและตามลำดับเวลาในฉาก พร้อมบริบทก่อน/หลัง เพื่อให้ตัดสินได้ว่าใครพูด

ใช้:
  python scripts/audit_cinema_gender.py                 # สรุปทุกฉาก
  python scripts/audit_cinema_gender.py --scene a01_010 # ดูฉากเดียวแบบเต็ม
  python scripts/audit_cinema_gender.py --write         # เขียน docs/cinema_gender_audit.md
"""
import argparse
import io
import json
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                    # noqa: E402

AUTH = paths.DB_EN / "en" / "auth.bin.json"
REPORT = paths.DOCS / "cinema_gender_audit.md"

FEMALE = re.compile(r"ค่ะ|คะ|ดิฉัน|เจ้าค่ะ|จ้ะ")
MALE = re.compile(r"ครับ|ผม(?![ก-๙])|กระผม")
META = {"VERSION", "REVISION", "ROW_COUNT", "COLUMN_COUNT", "TEXT_COUNT", "ROW_VALIDATOR",
        "COLUMN_VALIDATOR", "HAS_ROW_NAMES", "HAS_COLUMN_NAMES", "HAS_ROW_VALIDITY",
        "HAS_COLUMN_VALIDITY", "HAS_UNKNOWN_BITMASK", "HAS_ROW_INDICES", "TABLE_ID",
        "STORAGE_MODE", "columnTypes", "columnValidity", "COLUMN_INDICES"}


def scenes():
    """{ชื่อฉาก: [(ลำดับ, ชุด A/B, EN)]} เรียงตามลำดับเวลาในฉาก"""
    d = json.load(io.open(AUTH, encoding="utf-8"))
    out = {}
    for k, v in d.items():
        if k in META or not isinstance(v, dict):
            continue
        for scene, node in v.items():
            if scene.startswith("reARMP") or not isinstance(node, dict):
                continue
            ct = node.get("cinema_telop")
            if not isinstance(ct, dict):
                continue
            lines = []
            for r in sorted((x for x in ct if x.isdigit()), key=int):
                cell = ct[r].get("")
                if not isinstance(cell, dict):
                    continue
                for col, tag in (("4", "A"), ("5", "B")):
                    t = cell.get(col)
                    if isinstance(t, str) and t.strip():
                        lines.append((int(r), tag, t))
            if lines:
                out[scene] = lines
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scene", default="")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    data = scenes()

    L = ["# ตรวจคำลงท้ายบอกเพศในบทคัตซีน (`auth.bin`)", "",
         "> สร้างด้วย `python scripts/audit_cinema_gender.py --write` — ห้ามแก้ด้วยมือ", "",
         "`cinema_telop` ไม่มีคอลัมน์ผู้พูด → เพศต้องตัดสินจากบริบทฉากเท่านั้น", ""]
    total_f = total_m = 0
    rows_out = []
    for scene, lines in sorted(data.items()):
        f = m = 0
        detail = []
        for idx, tag, en in lines:
            th = master.get(en)
            if not isinstance(th, str):
                continue
            g = "F" if FEMALE.search(th) else ("M" if MALE.search(th) else "")
            if g == "F":
                f += 1
            elif g == "M":
                m += 1
            detail.append((idx, tag, g, en, th))
        total_f += f
        total_m += m
        if f or m:
            rows_out.append((scene, f, m, detail))

    if a.scene:
        for scene, f, m, detail in rows_out:
            if scene != a.scene:
                continue
            print("ฉาก %s · หญิง %d · ชาย %d" % (scene, f, m))
            for idx, tag, g, en, th in detail:
                print("%3d%s%s | %-52s | %s" % (idx, tag, g or " ",
                                                en.replace("\n", " / ")[:52],
                                                th.replace("\n", " / ")[:60]))
        return 0

    print("ฉากที่มีคำลงท้ายบอกเพศ %d ฉาก · หญิง %d บรรทัด · ชาย %d บรรทัด"
          % (len(rows_out), total_f, total_m))
    L += ["| ฉาก | หญิง | ชาย | บรรทัดทั้งฉาก |", "|---|---|---|---|"]
    for scene, f, m, detail in sorted(rows_out, key=lambda r: -r[1]):
        print("  %-14s หญิง %3d · ชาย %3d" % (scene, f, m))
        L.append("| %s | %d | %d | %d |" % (scene, f, m, len(detail)))
    L.append("")
    for scene, f, m, detail in sorted(rows_out, key=lambda r: -r[1]):
        if not f:
            continue
        L += ["## %s (หญิง %d · ชาย %d)" % (scene, f, m), "",
              "| # | ชุด | เพศ | EN | TH |", "|---|---|---|---|---|"]
        for idx, tag, g, en, th in detail:
            L.append("| %d | %s | %s | %s | %s |" % (
                idx, tag, g or "-", en.replace("\n", " / ").replace("|", "\\|"),
                th.replace("\n", " / ").replace("|", "\\|")))
        L.append("")
    if a.write:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        io.open(REPORT, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
        print("เขียน", REPORT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
