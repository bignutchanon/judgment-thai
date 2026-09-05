#!/usr/bin/env python3
"""ตรวจว่าคำแปลไทยใช้สรรพนาม "จับคู่" ถูกระดับตาม PRONOUN_MATRIX §0

ระบบที่ผู้ใช้สั่งไว้ (20 ส.ค. 2026):
  T1 สุภาพ : ผม / ดิฉัน  <->  คุณ            (คำลงท้าย ครับ/ค่ะ)
  T2 กันเอง: ฉัน         <->  แก             (ว่ะ/นะ/เหรอ/สิ)
  T3 หยาบ  : กู          <->  มึง            (โว้ย/เว้ย/ว่ะ)

ผิดคือ "ผสมข้ามระดับในประโยคเดียว" เช่น «ผม...มึง» หรือ «กู...คุณ» — ตัวตรวจนี้จับให้อัตโนมัติ
เพราะพอแปลจริงหลายหมื่นบรรทัดโดยหลายคน การผสมข้ามระดับจะหลุดแน่ถ้าไม่มีตัวจับ

ใช้:
  python scripts/check_pronoun_pairs.py                       # ตรวจ translations/master_th.json (ถ้ามี)
  python scripts/check_pronoun_pairs.py --files translations/characters_main.json translations/PRONOUN_MATRIX.md
  python scripts/check_pronoun_pairs.py --max 50              # จำกัดจำนวนที่พิมพ์
"""
import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

# คำแทนตัวเอง / คำเรียกคู่สนทนา แยกตามระดับ
# คำเดียวอาจอยู่ได้หลายระดับ — "ฉัน" เป็นได้ทั้ง T1 (หญิง โทนกลาง ๆ ตาม §0 แถวแรก) และ T2
# ดังนั้นเก็บเป็น "ชุดระดับที่เป็นไปได้" แล้วตัดสินว่าผิดก็ต่อเมื่อ **ไม่มีระดับไหนใช้ร่วมกันได้เลย**
# (ก่อน 21 ส.ค. 2026 เคยล็อก ฉัน = T2 อย่างเดียว ทำให้ "ฉัน...คุณ" ของตัวละครหญิงตก QC เท็จ
#  ผู้ตรวจ batch_050/051 ต้องไปดัด "ดิฉัน" หรือตัด "คุณ" ทิ้งเพื่อให้ผ่าน — บิดคำแปลเพราะเครื่องมือผิด)
SELF = {"ผม": {"T1"}, "ดิฉัน": {"T1"}, "ฉัน": {"T1", "T2"}, "กู": {"T3"}}
OTHER = {"คุณ": {"T1"}, "แก": {"T2"}, "มึง": {"T3"}}
ENDINGS = {"T1": ["ครับ", "ค่ะ", "คะ"], "T3": ["โว้ย", "เว้ย"]}

# ภาษาไทยไม่เว้นวรรคระหว่างคำ จึงเช็ค "ขอบเขตคำ" ด้วย regex เฉพาะคำ (กันคำที่มีสรรพนามเป็นส่วนหนึ่ง
# เช่น คุณภาพ · ฉันทะ · แกง/แก้/แกล้ง · กูเกิล · เส้นผม) — จับพลาดฝั่งปล่อยผ่านดีกว่าจับผิดคนแปล
WORD_RE = {
    # เพิ่ม 21 ส.ค. 2026: กันคำบรรยายเส้นผม (ผมดำ/ผมยาว/ผมทรง... ในตาราง search_characteristic)
    # โดนจับเป็นสรรพนาม "ผม" — นักแปล batch_127 ต้องเลี่ยงคำจนภาษาแข็ง
    "ผม":   r"(?<!เส้น)(?<!วิก)(?<!ทรง)(?<!ตัด)(?<!สระ)ผม(?!เผ้า|ดำ|ขาว|ทอง|สี|ยาว|สั้น|หยิก|ตรง|ทรง|บลอนด์|ฟู|ซอย|ม้า)",
    "ดิฉัน": r"ดิฉัน",
    "ฉัน":  r"(?<!ดิ)ฉัน(?!ท)",
    # กัน ยากูซ่า · ตระกูล · กูเกิล · กูรู · **กู้** (กู้โลก/กู้ภัย/กู้เงิน — นักแปล batch_071 เจอ "กู้โลก" โดนจับ)
    # เพิ่ม 21 ส.ค. 2026: กัน "จิ" ท้าย (ทากูจิ · คามากูจิ — นามสกุลลงท้าย -guchi ที่ lead ล็อกเป็น กูจิ
    # ทำให้ batch_103 โดนจับว่าผสม ผม/กู ทั้งที่เป็นชื่อคน)
    "กู":   r"(?<!ยา)(?<!ตระ)(?<!สุด)กู(?!เกิล|รู|ซ่า|ล|้|่|จิ)",
    # กัน ขอบคุณ/บุญคุณ/คุณภาพ + คำเรียกญาติที่ขึ้นต้นด้วย "คุณ" (คุณยาย/คุณตา/คุณปู่ ฯลฯ)
    # ซึ่งเป็นคำนามเรียกบุคคลที่สาม ไม่ใช่สรรพนาม T1 — นักแปล batch_052 ต้องดัด "คุณยาย" เป็น
    # "ยายของฉัน" เพื่อหนี QC เท็จ (21 ส.ค. 2026)
    "คุณ":  r"(?<!ขอบ)(?<!บุญ)คุณ(?!ภาพ|สมบัติ|ค่า|ธรรม|ประโยชน์|วุฒิ|งาม|หมอ"
            r"|ยาย|ย่า|ปู่|ตา|น้า|ลุง|ป้า|พ่อ|แม่|นาย)",
    "แก":   r"(?<!รัง)แก(?![งะ้ลนมวำจิีุ๊๋็่]|ร[่็นม])",   # กัน แก๊ง/แกะ/แก้/แกล้ง/แกร่ง/แกรน/โปรแกรม/รังแก (เพิ่ม ร ทั้งชุด 21 ส.ค. 2026)
    "มึง":  r"มึง",
}


def find_word(text, word):
    """หาคำสรรพนามแบบมีขอบเขต — คืนตำแหน่งที่พบจริง"""
    pat = WORD_RE.get(word, re.escape(word))
    return [m.start() for m in re.finditer(pat, text)]


def tiers_in(text):
    """คืน (คำแทนตัวที่พบ, คำเรียกอีกฝ่ายที่พบ, ระดับที่พบจากคำลงท้าย)"""
    self_w = [w for w in SELF if find_word(text, w)]
    other_w = [w for w in OTHER if find_word(text, w)]
    end_t = {t for t, ws in ENDINGS.items() if any(w in text for w in ws)}
    return self_w, other_w, end_t


def possible_tiers(words, table):
    """ระดับที่ยัง "เป็นไปได้พร้อมกัน" ของคำที่พบ — ว่างเปล่า = ขัดกันเอง"""
    out = None
    for w in words:
        out = set(table[w]) if out is None else out & table[w]
    return out if out is not None else set()


# ข้อความ "อธิบายกฎ" ในไฟล์เอกสาร/ไฟล์ตัวละคร จงใจเอ่ยหลายระดับพร้อมกัน (เช่น "แก้จาก 'ผม / ฉัน' เดิม")
# เวลาสแกนไฟล์พวกนั้นให้ข้ามด้วย --docs · บทแปลจริงใน master_th.json ไม่มีเครื่องหมายพวกนี้
NOTE_MARKERS = ["T1", "T2", "T3", "⏳", "§", "แก้จาก", "PRONOUN", "จับคู่", "ระดับ", "ตาม EN",
                "ยืนยันกับ EN", "คู่กับ", "แล้วแต่บริบท", "ตามความเป็นทางการ", "ห้ามผสม",
                "ห้ามข้าม", "ห้ามขยับ", "สลับตามบริบท", "เหตุผล:"]


def is_note(text):
    return any(m in text for m in NOTE_MARKERS)


def check_text(text):
    """คืนรายการปัญหาของข้อความหนึ่งชิ้น"""
    problems = []
    self_w, other_w, end_t = tiers_in(text)
    self_t, other_t = possible_tiers(self_w, SELF), possible_tiers(other_w, OTHER)
    if self_w and other_w and not (self_t & other_t):
        problems.append("ผสมข้ามระดับ: แทนตัว %s + เรียกอีกฝ่าย %s"
                        % ("/".join(self_w), "/".join(other_w)))
    all_t = possible_tiers(self_w + other_w, dict(SELF, **OTHER))
    if all_t == {"T3"} and "T1" in end_t:
        problems.append("T3 (กู/มึง) คู่กับคำลงท้ายสุภาพ ครับ/ค่ะ")
    if len(self_w) > 1:
        problems.append("คำแทนตัวหลายคำในบรรทัดเดียว: %s" % "/".join(self_w))
    if len(other_w) > 1:
        problems.append("คำเรียกอีกฝ่ายหลายคำในบรรทัดเดียว: %s" % "/".join(other_w))
    return problems


def walk_json(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_json(v, "%s/%s" % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_json(v, "%s[%d]" % (path, i))
    elif isinstance(obj, str):
        yield path, obj


def units(p):
    """แตกไฟล์เป็นชิ้นข้อความที่ควรตรวจทีละชิ้น"""
    if p.suffix == ".json":
        data = json.load(io.open(p, encoding="utf-8"))
        yield from walk_json(data)
    else:
        for i, line in enumerate(io.open(p, encoding="utf-8"), 1):
            yield "บรรทัด %d" % i, line.rstrip("\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--files", nargs="*", help="ไฟล์ที่จะตรวจ (ว่าง = translations/master_th.json)")
    ap.add_argument("--max", type=int, default=100)
    ap.add_argument("--docs", action="store_true",
                    help="โหมดสแกนไฟล์เอกสาร/ไฟล์ตัวละคร — ข้ามข้อความที่เป็นคำอธิบายกฎ")
    a = ap.parse_args()

    files = [paths.PROJECT / f for f in (a.files or [])] or [paths.MASTER_TH]
    files = [f for f in files if f.exists()]
    if not files:
        print("ไม่พบไฟล์ที่จะตรวจ (ยังไม่มี translations/master_th.json — ปกติสำหรับตอนนี้)")
        return 0

    total = shown = 0
    for p in files:
        for where, text in units(p):
            if a.docs and is_note(text):
                continue
            probs = check_text(text)
            if not probs:
                continue
            total += 1
            if shown < a.max:
                shown += 1
                print("%s  %s" % (p.relative_to(paths.PROJECT), where))
                for pr in probs:
                    print("    - " + pr)
                print("    " + text.strip()[:160])
    print()
    print("พบปัญหา %d จุด%s" % (total, "" if total <= a.max else " (แสดง %d จุดแรก)" % a.max))
    return 1 if total else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
