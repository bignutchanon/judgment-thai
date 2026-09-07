#!/usr/bin/env python3
"""จับบรรทัดที่คำลงท้าย/สรรพนามไทย **ขัดกับเพศของผู้พูดจริงในไฟล์เกม**

ที่มา: ผู้พูดของแต่ละบรรทัดอยู่ใน `extracted/facts/talk_speaker.json` (จาก `talk.bin` โดยตรง)
แต่คำแปลถูกทำทีละ batch นักแปลจึงมีโอกาสให้ผู้หญิงพูด "ครับ" หรือให้ยากามิพูด "ค่ะ" ได้
`merge_qc` ไม่จับ เพราะประโยคถูกไวยากรณ์อยู่แล้ว

ข้ามให้อัตโนมัติ:
  * บรรทัดที่มี `dupes` (หลายคนพูดข้อความเดียวกัน — คำแปลต้องเป็นกลางอยู่แล้ว)
  * เพศ `unknown`
  * คำที่หน้าตาเหมือนสรรพนามแต่ไม่ใช่ (เส้นผม/ทรงผม/โยคะ/นะคะที่อยู่กลางคำ ฯลฯ)

ใช้:
    python scripts/check_speaker_gender.py                       # ตรวจ master_th.json
    python scripts/check_speaker_gender.py --files translations/done/batch_TALK_065.done.json
"""
import argparse
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "translations", "master_th.json")
FACTS = os.path.join(ROOT, "extracted", "facts", "talk_speaker.json")

# ยืมกติกากันคำหลอกมาจาก check_pronoun_pairs.py (เส้นผม/ทรงผม ฯลฯ)
RE_PHOM = re.compile(r"(?<!เส้น)(?<!วิก)(?<!ทรง)(?<!ตัด)(?<!สระ)ผม"
                     r"(?!เผ้า|ดำ|ขาว|ทอง|สี|ยาว|สั้น|หยิก|ตรง|ทรง|บลอนด์|ฟู|ซอย|ม้า|โทน)")
RE_KRAP = re.compile(r"ครับ|คร้าบ")
# กันคำที่ขึ้นต้นด้วย "คะ" แต่ไม่ใช่คำลงท้าย (คะแนน · คะน้า · คะยั้นคะยอ)
# 7 ก.ย. 2026: ตัด (?<![ก-ฮ]) ออก — คำถาม "ไหมคะ/หรือคะ/อะไรคะ" ติดกับคำหน้าเสมอ (blind test เจอชินทานิ "หรือคะ?" หลุด 13 บรรทัด)
# กันคำที่ลงท้าย คะ โดยกำเนิดด้วย lookbehind แทน: โยคะ · ราคะ · (คะแนน/คะน้า/คะยั้น กันด้วย lookahead เดิม)
RE_KHA = re.compile(r"ค่ะ|(?<!โย)(?<!รา)คะ(?![ก-ฮแ])(?!แนน|น้า|ยั้น)|ดิฉัน")


RE_QUOTE = re.compile(r"[\"“”「『][^\"“”」』]*[\"“”」』]")


def outside_quotes(th):
    """ตัดข้อความในเครื่องหมายคำพูดออก — ตัวละครยกคำพูดของคนอื่นมาเล่าได้
    (เคสจริง: มิฮารุเล่าคำสารภาพของผู้ชาย จึงมี ผม/ครับ อยู่ในบรรทัดของผู้หญิงอย่างถูกต้อง)"""
    return RE_QUOTE.sub(" ", th)


def male_markers(th):
    t = outside_quotes(th)
    return bool(RE_KRAP.search(t)) or bool(RE_PHOM.search(t))


def female_markers(th):
    return bool(RE_KHA.search(outside_quotes(th)))


# สรรพนามที่ "ล็อกรายตัวละคร" — ผู้ตรวจ TALK_052/056/066 เจอหลุดซ้ำสามสปรินต์
# `check_pronoun_pairs.py` จับไม่ได้เพราะแต่ละคำถูกไวยากรณ์ในตัวเอง ต้องรู้ว่าใครพูดถึงจะรู้ว่าผิด
# ใช้ขอบเขตคำชุดเดียวกับ check_pronoun_pairs.py (กัน ฉันทะ · แก๊ง/แก้/แกล้ง · กูเกิล/ยากูซ่า ฯลฯ)
RE_CHAN = re.compile(r"(?<!ดิ)ฉัน(?!ท)")
RE_DICHAN = re.compile(r"ดิฉัน")
RE_KU = re.compile(r"(?<!ยา)(?<!ตระ)(?<!สุด)กู(?!เกิล|รู|ซ่า|ล|้|่|จิ)")
RE_KAE = re.compile(r"(?<!รัง)แก(?![งะ้ลนมวำจิีุ๊๋็่]|ร[่็นม])")
RE_MUENG = re.compile(r"มึง")

SELF_LOCK = {
    "yagami": ([RE_CHAN, RE_DICHAN, RE_KU], "ยากามิต้องใช้ \"ผม\" เสมอ"),
}
ADDRESS_LOCK = {
    "yagami": ([RE_KAE, RE_MUENG], "ยากามิห้ามเรียกคู่สนทนาว่า \"แก\"/\"มึง\""),
}


def lock_hits(speaker, th):
    """คืนรายการเหตุผลที่บรรทัดนี้ผิดคำล็อกรายตัวละคร"""
    out = []
    key = (speaker or "").lower()
    t = outside_quotes(th)
    for table in (SELF_LOCK, ADDRESS_LOCK):
        if key in table:
            pats, why = table[key]
            if any(p.search(t) for p in pats):
                out.append(why)
    return out


def load_pairs(path):
    with io.open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("strings", data)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", nargs="*", default=[MASTER])
    ap.add_argument("--max", type=int, default=30)
    a = ap.parse_args()

    with io.open(FACTS, encoding="utf-8") as fh:
        facts = json.load(fh)

    for path in a.files:
        pairs = load_pairs(path)
        hits = []
        for en, info in facts.items():
            th = pairs.get(en)
            if not th or info.get("dupes"):
                continue
            g = info.get("gender")
            for why in lock_hits(info.get("speaker"), th):
                hits.append((why, info.get("speaker"), en, th))
            if g == "female" and male_markers(th):
                hits.append(("ผู้พูดหญิงแต่ใช้คำชาย", info.get("speaker"), en, th))
            elif g == "male" and female_markers(th):
                hits.append(("ผู้พูดชายแต่ใช้คำหญิง", info.get("speaker"), en, th))
        print("== %s · %d คู่ · ขัดเพศผู้พูด %d" % (os.path.basename(path), len(pairs), len(hits)))
        for why, sp, en, th in hits[: a.max]:
            print("  [%s] %s" % (sp, why))
            print("    EN:", en.replace("\n", " ")[:84])
            print("    TH:", th.replace("\n", " ")[:84])
        if len(hits) > a.max:
            print("  ... อีก %d" % (len(hits) - a.max))


if __name__ == "__main__":
    main()
