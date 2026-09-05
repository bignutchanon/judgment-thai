"""กวาดชื่อเฉพาะที่ "ล็อกเป็นไทยแล้ว" แต่ยังถูกอ้างเป็นภาษาอังกฤษในบรรทัดไทย (และกลับกัน)

ที่มา: ตารางชื่อ (ไอเทม/ร้าน/คอร์ส) กับประโยคที่อ้างถึงชื่อนั้นอยู่คนละ bin และมักคนละ batch
นักแปลคนที่ทำประโยคจึงไม่รู้ว่าอีก batch แปลชื่อเป็นไทยไปแล้ว ผู้เล่นเห็นสองภาษาในหน้าจอเดียวกัน
(คลาสเดียวกับบั๊กชื่อช่อง Dice & Cube ที่เจอในสปรินต์สาม)

ทุกคู่ในตารางมีที่มาจาก `translations/glossary.md` หรือคำที่ ship แล้วในโปรเจกต์พี่น้อง

ใช้:
    python scripts/fix_locked_name_quotes.py            # ดูอย่างเดียว
    python scripts/fix_locked_name_quotes.py --write    # แก้ translations/done/*.done.json
หลังแก้ต้อง `python scripts/merge_qc.py --only <batch>` ทุก batch ที่ถูกแตะ
"""
import argparse
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONE_GLOB = os.path.join(ROOT, "translations", "done", "*.done.json")
THAI = re.compile(r"[฀-๿]")

# ชื่ออังกฤษที่โผล่ในบรรทัดไทย -> รูปไทยที่ล็อกไว้ (เรียงยาวก่อนสั้นตอนใช้งาน)
IN_SENTENCE = [
    ("Lullaby Mahjong", "ลัลลาบายมาจอง", "glossary §11 บรรทัด 440/445 ล็อกชื่อร้านมาจองให้ทับศัพท์ทั้งหมด"),
    ("Modern Mahjong", "โมเดิร์นมาจอง", "เหมือนข้อบน"),
    ("Hug Bomb Explosion Omega", "ระเบิดกอด เอ็กซ์โพลชันโอเมกา", "ชื่อไอเทมในตาราง item ที่แปลไทยแล้ว"),
    ("Hug Bomb Spark Alpha", "ระเบิดกอด สปาร์คอัลฟา", "ชื่อไอเทมในตาราง item ที่แปลไทยแล้ว"),
    ("Hug Bomb Spark Beta", "ระเบิดกอด สปาร์คเบตา", "ชื่อไอเทมในตาราง item ที่แปลไทยแล้ว"),
    ("Hug Bomb", "ระเบิดกอด", "ชื่อไอเทมในตาราง item ที่แปลไทยแล้ว"),
    ("Staminan X", "สตามินัน X", "รูปที่ ship แล้วทั้ง K3 และ Gaiden"),
    ("Amidst a Dream", "ท่ามกลางความฝัน", "ชื่อแผ่นเสียงในตารางไอเทมแปลไทยแล้ว"),
    ("Home Run Course", "คอร์สโฮมรัน", "ชื่อคอร์สแบตติ้งเซ็นเตอร์ในตารางแปลไทยแล้ว"),
    ("Challenge Course", "คอร์สท้าทาย", "เหมือนข้อบน"),
    ("Koro-nyan", "โคโระเนียง", "ชื่อมาสคอต Dice & Cube ที่ล็อกไว้ใน glossary"),
]

# คีย์ที่ "ตัวชื่อเอง" ต้องคงอังกฤษตามคำล็อก แต่มี batch แปลเป็นไทยไว้
KEEP_EN_KEYS = {
    "Wette Kitchen": "glossary บรรทัด 429/453/463 ล็อก Wette Kitchen ให้คง EN ทั้งในตารางและในประโยค",
    "Don Quijote": "glossary บรรทัด 40 (K3 wave10) ล็อกให้คง EN — ห้ามทับศัพท์ 'ดอนกิโฮเต้'",
}

# คีย์ที่ตัวชื่อเองต้องเป็นรูปไทยตามคำล็อก แต่ batch แปลเป็นรูปอื่น
FIX_KEYS = {
    "Lullaby Mahjong": ("ลัลลาบายมาจอง", "glossary §11 — ชื่อร้านมาจองทับศัพท์ ไม่แปลความหมาย"),
    "Modern Mahjong": ("โมเดิร์นมาจอง", "glossary §11 — ชื่อร้านมาจองทับศัพท์ ไม่แปลความหมาย"),
}


def main(write=False):
    pats = [(en, th, re.compile(r"(?<![A-Za-z])" + re.escape(en) + r"(?![A-Za-z])"))
            for en, th, _src in IN_SENTENCE]
    touched, total = {}, 0
    for path in sorted(glob.glob(DONE_GLOB)):
        with io.open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        strings = data.get("strings", {})
        changed = 0
        for key, val in list(strings.items()):
            new = val
            if key.strip() in KEEP_EN_KEYS and THAI.search(val):
                new = key.strip()
            elif key.strip() in FIX_KEYS and val != FIX_KEYS[key.strip()][0]:
                new = FIX_KEYS[key.strip()][0]
            elif THAI.search(val):
                for en, th, pat in pats:
                    if key.strip() == en:
                        continue
                    new = pat.sub(th, new)
            if new != val:
                total += 1
                changed += 1
                print("--", os.path.basename(path))
                print("   EN :", key.replace("\n", " ")[:90])
                print("   เดิม:", val.replace("\n", " ")[:90])
                print("   ใหม่:", new.replace("\n", " ")[:90])
                strings[key] = new
        if changed:
            touched[os.path.basename(path)] = changed
            if write:
                with io.open(path, "w", encoding="utf-8") as fh:
                    json.dump(data, fh, ensure_ascii=False, indent=1)
    print()
    print("รวม %d จุด ใน %d batch%s" % (total, len(touched), "" if write else " (ยังไม่แก้ — ใส่ --write)"))
    for b, n in sorted(touched.items()):
        print("   %-32s %d" % (b, n))
    if write and touched:
        ids = sorted(b.replace("batch_", "").replace(".done.json", "") for b in touched)
        print()
        print("ต้อง merge ใหม่:", " ".join(ids))
    return total


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    main(write=ap.parse_args().write)
