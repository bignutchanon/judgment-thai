#!/usr/bin/env python3
"""แก้คำลงท้าย/สรรพนามไทยของบรรทัดที่ขัดกับเพศของ **คิวเสียงของบรรทัดนั้นเอง**

ใช้คู่กับ `make_line_gender.py` (สร้างตาราง) และ `check_line_gender.py` (ตรวจ)
วิธีถอดเพศจากคิวเสียง: `D:\\Projects\\lost-judgment-thai\\docs\\reference\\CUE_GENDER_METHOD.md`

สคริปต์นี้แก้ **ไฟล์ `translations/done/*.done.json`** (ไม่ใช่ master โดยตรง — กติกาเหล็กข้อ 4)
แล้วให้รัน `python scripts/remerge_stale.py --write` ต่อเพื่อดัน master_th.json ตาม

## กติกาที่ใช้แก้

| เพศจากคิว | ทำอะไร |
|---|---|
| `female` | ครับ -> ค่ะ (นะครับ -> นะคะ · ไหมครับ -> ไหมคะ · ประโยคคำถาม -> คะ) · ผม -> ฉัน |
| `male` | ค่ะ/คะ -> ครับ · ดิฉัน/ฉัน -> ผม |
| `mixed` | **ตัดคำลงท้ายบอกเพศทิ้ง** + ตัดสรรพนามบอกเพศที่ขึ้นต้นประโยค = กลางเพศ |

`mixed` = ข้อความเดียวถูกใช้ซ้ำโดยผู้พูดคนละเพศ (เช่น "Yeah." ที่ทั้งชายและหญิงพูด)
บรรทัดพวกนี้แปลระบุเพศไม่ได้เลย ต้องกลาง

## รายชื่อที่ข้าม (`SKIP_VOICERS`)

คอลัมน์ `sex` ใน `sound_voicer.bin` บางแถวเป็นเพศของ **นักพากย์** ไม่ใช่ของตัวละคร
(เด็กผู้ชายมักให้ผู้หญิงพากย์) จึงข้าม voicer ที่ตรวจแล้วว่าขัดกับตัวละครจริง — ดูรายชื่อข้างล่าง
ก่อนเพิ่มชื่อใหม่เข้าลิสต์ ต้องเทียบกับ `translations/characters_main.json` / `characters_side.json`
หรือบทในเกมก่อนเสมอ **ห้ามข้ามเพราะ "ดูแปลก ๆ" เฉย ๆ**

ใช้:
  python scripts/fix_line_gender.py            # ดูข้อเสนอ ไม่เขียนไฟล์
  python scripts/fix_line_gender.py --write
"""
import argparse
import collections
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from check_line_gender import audit
from check_speaker_gender import RE_PHOM, female_markers, male_markers

FACTS = paths.EXTRACTED / "facts" / "line_gender.json"
TALK_FACTS = paths.EXTRACTED / "facts" / "talk_speaker.json"   # ผู้พูดใน talk.bin (บทเดินเมือง)
DONE = paths.TRANSLATIONS / "done"

# voicer ที่ `sex` ในไฟล์เกมขัดกับเพศของตัวละครจริง (ตรวจทีละตัวแล้ว 29 ส.ค. 2026)
SKIP_VOICERS = {
    "sumire": "โฮสเตสหญิง — ตารางบอก 1 (ชาย) น่าจะเป็นเพศนักพากย์",
    "kjart_woman": "พนักงานหญิงที่ KJ Art — ตารางบอก 1 (ชาย)",
    "alpes_boy": "เด็กเสิร์ฟชายร้าน Alps — ตารางบอก 2 (หญิง) ตามธรรมเนียมให้ผู้หญิงพากย์เด็กชาย",
    # 7 ก.ย. 2026 (blind test): แฟนสาวของเซย่า — คิวชื่อ girl และเนื้อหาเป็นหญิงชัด ("he never showed" · นังตัวร้าย) แต่ตารางบอก 1 (ชาย)
    "seiya_girl1": "แฟนสาวของเซย่า — ตารางบอก 1 (ชาย) ขัดกับคิวชื่อ girl และเนื้อหา",
    "seiya_girl2": "แฟนสาวของเซย่า — ตารางบอก 1 (ชาย) ขัดกับคิวชื่อ girl และเนื้อหา",
    "seiya_girl3": "แฟนสาวของเซย่า — ตารางบอก 1 (ชาย) ขัดกับคิวชื่อ girl และเนื้อหา",
}

# ประโยคสั้นที่ตัดคำลงท้ายแล้วเหลือว่าง — ต้องมีคำกลางเพศแทน
NEUTRAL_FALLBACK = {"Yeah.": "ใช่", "Yes.": "ใช่", "Sure.": "ได้เลย", "Okay.": "ได้"}

RE_KHA_Q = re.compile(r"(?<![ก-ฮ])(?<!รา)คะ(?![ก-ฮแ])(?!แนน|น้า|ยั้น)")
RE_CHAN = re.compile(r"(?<!ดิ)ฉัน(?!ท)")
RE_LEAD_PRONOUN = re.compile(r"^([\s.…]*)(ผม|ดิฉัน|ฉัน)\s*")


def to_female(t):
    t = (t.replace("นะครับ", "นะคะ").replace("ไหมครับ", "ไหมคะ")
          .replace("เหรอครับ", "เหรอคะ").replace("หรือครับ", "หรือคะ")
          .replace("ครับ?", "คะ?").replace("คร้าบ", "ค่ะ").replace("ครับ", "ค่ะ"))
    return RE_PHOM.sub("ฉัน", t)


def to_male(t):
    t = (t.replace("นะคะ", "นะครับ").replace("ไหมคะ", "ไหมครับ")
          .replace("เหรอคะ", "เหรอครับ").replace("หรือคะ", "หรือครับ")
          .replace("ค่ะ", "ครับ"))
    t = RE_KHA_Q.sub("ครับ", t)
    t = t.replace("ดิฉัน", "ผม")
    return RE_CHAN.sub("ผม", t)


def to_neutral(t, en=""):
    t = t.replace("นะครับ", "นะ").replace("นะคะ", "นะ")
    # "ไหมคะ/เหรอคะ/หรือคะ" — RE_KHA_Q ไม่จับเพราะมีพยัญชนะนำหน้า (เจอตอนกวาดแชท 5 ก.ย. 2026)
    t = t.replace("ไหมคะ", "ไหม").replace("เหรอคะ", "เหรอ").replace("หรือคะ", "หรือ")
    t = re.sub(r"ครับ|คร้าบ|ค่ะ", "", t)
    t = RE_KHA_Q.sub("", t)
    t = RE_LEAD_PRONOUN.sub(r"\1", t)          # "ผมขอตัวไปก่อนนะ" -> "ขอตัวไปก่อนนะ"
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"[ \t]+([?!.,])", r"\1", t)
    t = "\n".join(line.strip() for line in t.split("\n")).strip()
    return t or NEUTRAL_FALLBACK.get(en, "")


def talk_gender():
    """ข้อความ EN -> เพศผู้พูดใน `talk.bin` (หลักฐานคนละชุดกับคิวเสียง)"""
    if not TALK_FACTS.exists():
        return {}
    out = {}
    for en, info in json.load(io.open(TALK_FACTS, encoding="utf-8")).items():
        g = info.get("gender")
        if g in ("male", "female"):
            out[en] = g
    return out


def propose(pairs, facts):
    """คืน ({en: th ใหม่}, [รายการที่ข้าม])"""
    fixes, skipped = {}, []
    talk = talk_gender()
    for kind, gender, en, th, info in audit(pairs, facts):
        voicers = info.get("voicers") or []
        skip = [v for v in voicers if v in SKIP_VOICERS]
        if skip:
            skipped.append((en, skip[0], SKIP_VOICERS[skip[0]]))
            continue
        # ข้อความเดียวกันถูกใช้ใน talk.bin โดยผู้พูดคนละเพศ = ใช้ร่วมกันจริง -> ต้องกลางเพศ
        # (เคสจริง: "Good luck." คิวเป็นมาฟุยุ (หญิง) แต่ยากามิพูดประโยคเดียวกันใน talk.bin)
        if gender in ("male", "female") and talk.get(en) not in (None, gender):
            gender = "mixed"
        new = (to_female(th) if gender == "female"
               else to_male(th) if gender == "male"
               else to_neutral(th, en))
        if not new:
            skipped.append((en, "-", "ตัดคำลงท้ายแล้วเหลือว่าง — ต้องแก้มือ"))
            continue
        if new != th:
            fixes[en] = new

    # รอบสอง: ข้อความที่ **สองแหล่งหลักฐานไม่ตรงกัน** (คิวเสียงว่าเพศหนึ่ง · talk.bin ว่าอีกเพศ)
    # แปลว่าเกมเอาบรรทัดเดียวไปใช้กับผู้พูดคนละเพศจริง ๆ ต้องกลางเพศ แม้ตอนนี้จะยังไม่ขัดกับ
    # แหล่งใดแหล่งหนึ่ง (เคสจริง: "Good luck." — คิวเป็นมาฟุยุ (หญิง) แต่ยากามิพูดใน talk.bin)
    for en, info in facts.items():
        th = pairs.get(en)
        if not th or en in fixes:
            continue
        g = info.get("gender")
        if g not in ("male", "female") or talk.get(en) in (None, g):
            continue
        if not (male_markers(th) or female_markers(th)):
            continue
        if any(v in SKIP_VOICERS for v in (info.get("voicers") or [])):
            continue
        new = to_neutral(th, en)
        if new and new != th:
            fixes[en] = new
    return fixes, skipped


def apply_to_done(fixes):
    """เขียนคำแปลใหม่ลงทุกไฟล์ done ที่มีคีย์นั้น -> Counter ชื่อไฟล์ที่แก้"""
    touched = collections.Counter()
    for path in sorted(glob.glob(str(DONE / "*.done.json"))):
        data = json.load(io.open(path, encoding="utf-8"))
        strings = data.get("strings", data)
        n = 0
        for en, new in fixes.items():
            if en in strings and strings[en] != new:
                strings[en] = new
                n += 1
        if n:
            io.open(path, "w", encoding="utf-8", newline="\n").write(
                json.dumps(data, ensure_ascii=False, indent=1) + "\n")
            touched[os.path.basename(path)] = n
    return touched


def main():
    ap = argparse.ArgumentParser(description="แก้เพศคำลงท้าย/สรรพนามตามคิวเสียงรายบรรทัด")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    assert FACTS.exists(), "ยังไม่มี %s — รัน scripts/make_line_gender.py --write ก่อน" % FACTS
    facts = json.load(io.open(FACTS, encoding="utf-8"))
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))

    fixes, skipped = propose(master, facts)
    for en, new in fixes.items():
        print("EN :", en.replace("\n", " | ")[:96])
        print("OLD:", master[en].replace("\n", " | ")[:96])
        print("NEW:", new.replace("\n", " | ")[:96])
    print("\nแก้ %d บรรทัด · ข้าม %d" % (len(fixes), len(skipped)))
    for en, who, why in skipped:
        print("  ข้าม [%s] %s — %s" % (who, en.replace("\n", " ")[:60], why))

    if not a.write:
        print("\n(ใส่ --write เพื่อเขียนลง translations/done/ แล้วรัน remerge_stale.py --write ต่อ)")
        return 0
    touched = apply_to_done(fixes)
    print("\nแก้ไฟล์ done %d ไฟล์:" % len(touched))
    for name, n in touched.most_common():
        print("  %s: %d บรรทัด" % (name, n))
    print("ขั้นต่อไป: python scripts/remerge_stale.py --write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
