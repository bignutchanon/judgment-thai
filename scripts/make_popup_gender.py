#!/usr/bin/env python3
"""ถอดเพศ/อายุ/บริบทของผู้พูดคำพูดลอยชาวเมือง จากชื่อแถวใน character_npc_popup_text.bin

ที่มา: ชื่อแถวในไฟล์เกมบอกครบ เช่น `kamuro_daytime_man_young_solo_01`
= ย่านคามุโรกลางวัน · **ชาย** · วัยหนุ่ม · พูดคนเดียว
ผู้ตรวจ batch_122 เจอว่ามี 153/250 บรรทัดที่ไฟล์เกมบอกเพศไว้ แต่ทีมไม่ได้ใช้
(นักแปลเลี่ยงสรรพนามทั้งหมดเพราะคิดว่าไม่มีหลักฐาน)

ผลลัพธ์: `extracted/facts/popup_gender.json` = {ข้อความ EN: {row, gender, age, place, time}}

ใช้:
  python scripts/make_popup_gender.py --write
  python scripts/make_popup_gender.py --find "My husband's on a business trip"
"""
import argparse
import collections
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

SRC = paths.PROJECT / "extracted" / "db_en" / "en" / "character_npc_popup_text.bin.json"
OUT = paths.PROJECT / "extracted" / "facts" / "popup_gender.json"

AGE = {"young": "หนุ่มสาว", "middle": "วัยกลางคน", "old": "สูงอายุ", "child": "เด็ก"}


def parse_row(name: str):
    parts = name.split("_")
    gender = "unknown"
    if "man" in parts:
        gender = "male"
    if "woman" in parts:
        gender = "female"
    if "boy" in parts:
        gender = "male"
    if "girl" in parts:
        gender = "female"
    age = next((AGE[p] for p in parts if p in AGE), "")
    time = next((p for p in parts if p in ("daytime", "night", "evening", "morning")), "")
    place = parts[0] if parts else ""
    return {"row": name, "gender": gender, "age": age, "place": place, "time": time}


def build():
    d = json.load(io.open(SRC, encoding="utf-8"))
    out = {}
    for key in d:
        if not key.isdigit():
            continue
        for row_name, row in d[key].items():
            text = row.get("text")
            if not text or not row_name:
                continue
            out[text] = parse_row(row_name)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--find", help="ค้นข้อความ EN ตรง ๆ")
    a = ap.parse_args()
    table = build()

    if a.find:
        meta = table.get(a.find)
        print(json.dumps(meta, ensure_ascii=False) if meta else "ไม่พบข้อความนี้ในตาราง")
        return 0

    c = collections.Counter(v["gender"] for v in table.values())
    print("ทั้งหมด %d บรรทัด · %s" % (len(table), dict(c)))
    if a.write:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        io.open(OUT, "w", encoding="utf-8").write(json.dumps(table, ensure_ascii=False, indent=1))
        print("เขียน %s แล้ว" % OUT)
    else:
        print("ใส่ --write เพื่อเขียนไฟล์")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
