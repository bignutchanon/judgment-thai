#!/usr/bin/env python3
"""กวาดคำที่เจ้าของสั่งเปลี่ยนทั้งเกม — ใช้เฉพาะกฎชุดนี้จาก normalize_terms.RULES

- aniki: เลิกทับศัพท์ "อานิกิ" → "ลูกพี่" (เจ้าของสั่ง 27 ก.ย. 2026) · ติดชื่อ = ลูกพี่ไคโตะ/ลูกพี่ฮิงาชิ
- the Mole: "ไส้ศึก" → "ไอ้ตัวตุ่น" (เจ้าของสั่ง 28 ก.ย. 2026) — ชื่อ JA คือ モグラ (ตัวตุ่น) ยากามิตั้ง
  เพราะคนร้ายมุดหายใต้ดิน ไม่ใช่ความหมาย "สายลับ" ของคำ mole ในภาษาอังกฤษ

ทำไมไม่ใช้ `normalize_terms.py --write` ตรง ๆ: ตอนเขียนสคริปต์นี้ normalize_terms มีกฎเก่าที่ยัง
ค้างเสนอแก้ในไฟล์ done อยู่ ~16 จุด (คนโด/คนจัง/โรค อัลไซเมอร์ ฯลฯ) ซึ่งบางจุดอาจเป็นคำอื่นที่ถูกอยู่แล้ว
(เช่น regex `คนโด(?!ะ)` ชน "คนโดน") — จึงดึงเฉพาะกฎที่มีคำใน TERMS มาใช้
(กฎยังอยู่ใน normalize_terms เพื่อกันคำเก่ากลับมาจาก batch ใหม่) · คำสั่งเปลี่ยนคำครั้งใหม่: เพิ่มกฎท้าย
normalize_terms.RULES + เพิ่มคำเก่าใน TERMS + ปรับ EXPECTED_RULES

อีกส่วน: EN "Kaito-aniki" 6 บรรทัดเดิมแปลเป็น "พี่ไคโตะ" — ปรับเป็น "ลูกพี่ไคโตะ" ให้ตรงกันทั้งเกม
(อิงคีย์ EN เพราะ "พี่ไคโตะ" ในบรรทัดที่ EN ไม่มี aniki ต้องคงไว้)

ใช้:  python scripts/fix_owner_terms.py            # ดูเฉย ๆ
      python scripts/fix_owner_terms.py --write    # แก้ docs/translations (แล้วรัน remerge_stale.py --write ต่อ)
"""
import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
import normalize_terms as nt

TERMS = ("อานิกิ", "ไส้ศึก")   # คำเก่าที่เจ้าของสั่งเลิกใช้
EXPECTED_RULES = 5            # aniki 3 + the Mole 2
RULES = [r for r in nt.RULES if any(t in r[0] for t in TERMS)]
KAITO_RE = re.compile(r"(?<!ลูก)พี่ไคโตะ")


def apply_rules(s):
    n = 0
    for bad, good, _src in RULES:
        if bad.startswith("re:"):
            s, k = re.subn(bad[3:], good, s)
        else:
            k = s.count(bad)
            s = s.replace(bad, good)
        n += k
    return s, n


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    assert len(RULES) == EXPECTED_RULES, "กฎใน normalize_terms.RULES หายหรือเพิ่ม — ตรวจก่อน"

    total = 0
    for p in nt.targets():
        s = io.open(p, encoding="utf-8").read()
        s2, n = apply_rules(s)
        k = 0
        if p.name.endswith(".done.json"):
            d = json.loads(s2)
            for en, th in d["strings"].items():
                if re.search(r"aniki", en, re.I) and KAITO_RE.search(th):
                    d["strings"][en], c = KAITO_RE.subn("ลูกพี่ไคโตะ", th)
                    k += c
            if k:
                s2 = json.dumps(d, ensure_ascii=False, indent=1)
        if not (n or k):
            continue
        total += n + k
        print("%-48s กฎคำ x%d · Kaito-aniki(พี่ไคโตะ) x%d" % (p.relative_to(paths.PROJECT), n, k))
        if a.write:
            io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
    print("รวม %d จุด%s" % (total, " (แก้แล้ว)" if a.write else " (ใส่ --write เพื่อแก้)"))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
