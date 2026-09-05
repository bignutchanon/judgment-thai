#!/usr/bin/env python3
"""จับบรรทัดที่คำลงท้าย/สรรพนามไทยขัดกับ **เพศของคิวเสียงของบรรทัดนั้นเอง**

ต่างจาก `check_speaker_gender.py` ตรงหลักฐานที่ใช้:

| สคริปต์ | หลักฐาน | ครอบคลุม | จุดอ่อน |
|---|---|---|---|
| `check_speaker_gender.py` | เพศของ **ชื่อผู้พูด** (`talk_speaker.json`) | บทเดินเมือง `talk.bin` | ชื่อเดียวใช้กับหลายคน = เสียงข้างมากกลบฝั่งน้อย |
| **ตัวนี้** | เพศของ **คิวเสียงรายบรรทัด** (`line_gender.json`) | บทคัตซีน `sound_auth.bin` | บรรทัดที่ไม่มีเสียงพากย์ช่วยไม่ได้ |

วิธีถอดเพศจากคิวเสียงอยู่ใน `D:\\Projects\\lost-judgment-thai\\docs\\reference\\CUE_GENDER_METHOD.md`
สร้างตารางด้วย `python scripts/make_line_gender.py --write` ก่อนใช้สคริปต์นี้

`gender: "mixed"` = ข้อความเดียวถูกใช้ซ้ำโดยผู้พูดคนละเพศ → **ต้องกลางเพศ**
สคริปต์จึงรายงานบรรทัด mixed ที่มีคำบอกเพศแยกอีกกลุ่มหนึ่ง (ไม่ปนกับกลุ่มที่ผิดเพศชัด ๆ)

ใช้:
    python scripts/check_line_gender.py                 # ตรวจ master_th.json
    python scripts/check_line_gender.py --max 60
    python scripts/check_line_gender.py --json out.json # ส่งต่อให้สคริปต์แก้
"""
import argparse
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from check_speaker_gender import female_markers, male_markers

FACTS = paths.EXTRACTED / "facts" / "line_gender.json"


def load_pairs(path):
    data = json.load(io.open(path, encoding="utf-8"))
    return data.get("strings", data)


def audit(pairs, facts):
    """คืน [(ชนิดปัญหา, เพศจากคิว, EN, TH, คิวตัวอย่าง)]"""
    hits = []
    for en, info in facts.items():
        th = pairs.get(en)
        if not th:
            continue
        g = info.get("gender")
        m, f = male_markers(th), female_markers(th)
        if g == "female" and m:
            hits.append(("คิวเสียงหญิงแต่ใช้คำชาย", g, en, th, info))
        elif g == "male" and f:
            hits.append(("คิวเสียงชายแต่ใช้คำหญิง", g, en, th, info))
        elif g == "mixed" and (m or f):
            hits.append(("บรรทัดใช้ร่วมสองเพศแต่แปลระบุเพศ", g, en, th, info))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", nargs="*", default=[str(paths.MASTER_TH)])
    ap.add_argument("--max", type=int, default=30)
    ap.add_argument("--json", help="เขียนผลเป็น JSON ให้สคริปต์แก้อ่านต่อ")
    a = ap.parse_args()

    assert FACTS.exists(), "ยังไม่มี %s — รัน scripts/make_line_gender.py --write ก่อน" % FACTS
    facts = json.load(io.open(FACTS, encoding="utf-8"))

    for path in a.files:
        pairs = load_pairs(path)
        covered = sum(1 for en in facts if en in pairs)
        hits = audit(pairs, facts)
        by_kind = {}
        for h in hits:
            by_kind.setdefault(h[0], []).append(h)
        print("== %s · %s คู่ · มีคิวเสียงชี้เพศ %s คู่ · ขัดกัน %d"
              % (os.path.basename(path), format(len(pairs), ","),
                 format(covered, ","), len(hits)))
        for kind, items in sorted(by_kind.items(), key=lambda kv: -len(kv[1])):
            print("  -- %s: %d" % (kind, len(items)))
            for _, g, en, th, info in items[: a.max]:
                print("     cue %s (%s)" % (info.get("example_cue", ""), g))
                print("     EN:", en.replace("\n", " ")[:88])
                print("     TH:", th.replace("\n", " ")[:88])
            if len(items) > a.max:
                print("     ... อีก %d" % (len(items) - a.max))

        if a.json:
            out = [{"kind": k, "gender": g, "en": en, "th": th,
                    "cue": info.get("example_cue", ""),
                    "voicers": info.get("voicers", []),
                    "votes": info.get("votes", {})}
                   for k, g, en, th, info in hits]
            io.open(a.json, "w", encoding="utf-8", newline="\n").write(
                json.dumps(out, ensure_ascii=False, indent=1) + "\n")
            print("เขียน %s (%d รายการ)" % (a.json, len(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
