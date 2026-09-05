#!/usr/bin/env python3
"""แก้คำลงท้าย/สรรพนามไทยให้ตรงกับ **เพศผู้พูดจากหลักฐานทุกแหล่ง** (`dialogue_gender.json`)

ต่อยอดจาก `fix_line_gender.py` (ซึ่งใช้แค่คิวเสียง) — ตัวนี้อ่านตารางรวมที่
`make_dialogue_gender.py --write` สร้างไว้ (คิวเสียง + talk.bin + คัตซีน + แชท + คำพูดลอย + บันทึกยากามิ)
กติกาแก้เหมือนเดิมทุกข้อ (นำเข้าจาก fix_line_gender):

| เพศจากหลักฐาน | ทำอะไร |
|---|---|
| `female` แต่คำแปลใช้คำชาย | ครับ -> ค่ะ · ผม -> ฉัน |
| `male` แต่คำแปลใช้คำหญิง | ค่ะ/คะ -> ครับ · ดิฉัน/ฉัน -> ผม |
| `mixed` (ข้อความเดียวใช้กับผู้พูดต่างเพศ) | ตัดคำบอกเพศทิ้ง = กลางเพศ |
| `unknown` / `narration` | ไม่แตะ |

เขียนลง `translations/done/*.done.json` (กติกาเหล็กข้อ 4) แล้วต้องรัน `remerge_stale.py --write` ต่อ
บรรทัดที่ตัดคำลงท้ายแล้วเหลือว่างจะถูกข้ามและรายงานให้แก้มือ

ใช้:
  python scripts/fix_dialogue_gender.py            # ดูข้อเสนอ ไม่เขียน
  python scripts/fix_dialogue_gender.py --write
  python scripts/fix_dialogue_gender.py --json build/gender/fix_proposal.json
"""
import argparse
import collections
import io
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                    # noqa: E402
from check_speaker_gender import female_markers, male_markers   # noqa: E402
from fix_line_gender import apply_to_done, to_female, to_male, to_neutral   # noqa: E402

FACTS = paths.EXTRACTED / "facts" / "dialogue_gender.json"
# บรรทัดที่ lead ตัดสินให้คงไว้แม้หลักฐานอัตโนมัติจะค้าน (เช่น ธง ambiguous ของแชทที่เป็น artifact)
EXCEPTIONS = paths.TRANSLATIONS / "gender_exceptions.json"


def propose(master, facts):
    """คืน ({en: th ใหม่}, [(en, เหตุผลที่ข้าม)], Counter ชนิด)"""
    fixes, skipped, kinds = {}, [], collections.Counter()
    exc = json.load(io.open(EXCEPTIONS, encoding="utf-8")) if EXCEPTIONS.exists() else {}
    for en, info in facts.items():
        th = master.get(en)
        if not th or en in exc:
            continue
        g = info.get("gender")
        m, f = male_markers(th), female_markers(th)
        if g == "male" and f:
            new, kind = to_male(th), "หญิง->ชาย"
        elif g == "female" and m:
            new, kind = to_female(th), "ชาย->หญิง"
        elif g == "mixed" and (m or f):
            new, kind = to_neutral(th, en), "->กลาง"
        else:
            continue
        if not new:
            skipped.append((en, "ตัดคำลงท้ายแล้วเหลือว่าง — ต้องแก้มือ"))
            continue
        if new != th:
            fixes[en] = new
            kinds[kind] += 1
    return fixes, skipped, kinds


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--json", help="เขียนข้อเสนอเป็น JSON (en -> {old, new, gender, who})")
    ap.add_argument("--max", type=int, default=40, help="จำนวนตัวอย่างที่พิมพ์")
    a = ap.parse_args()
    assert FACTS.exists(), "ยังไม่มี %s — รัน scripts/make_dialogue_gender.py --write ก่อน" % FACTS
    facts = json.load(io.open(FACTS, encoding="utf-8"))
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))

    fixes, skipped, kinds = propose(master, facts)
    for i, (en, new) in enumerate(fixes.items()):
        if i >= a.max:
            print("... อีก %d" % (len(fixes) - a.max))
            break
        who = ",".join(dict.fromkeys(s.get("who", "") for s in facts[en]["sources"]))[:40]
        print("[%s %s] EN : %s" % (facts[en]["gender"], who, en.replace("\n", " | ")[:80]))
        print("        OLD: %s" % master[en].replace("\n", " | ")[:80])
        print("        NEW: %s" % new.replace("\n", " | ")[:80])
    print("\nแก้ %d บรรทัด (%s) · ข้าม %d" % (
        len(fixes), " · ".join("%s %d" % kv for kv in kinds.most_common()), len(skipped)))
    for en, why in skipped[:20]:
        print("  ข้าม %s — %s" % (en.replace("\n", " ")[:60], why))

    if a.json:
        out = {en: {"old": master[en], "new": new, "gender": facts[en]["gender"],
                    "sources": facts[en]["sources"]} for en, new in fixes.items()}
        Path(a.json).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("เขียน %s" % a.json)
    if not a.write:
        print("\n(ใส่ --write เพื่อเขียนลง translations/done/ แล้วรัน remerge_stale.py --write ต่อ)")
        return 0
    touched = apply_to_done(fixes)
    print("\nแก้ไฟล์ done %d ไฟล์ รวม %d บรรทัด" % (len(touched), sum(touched.values())))
    print("ขั้นต่อไป: python scripts/remerge_stale.py --write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
