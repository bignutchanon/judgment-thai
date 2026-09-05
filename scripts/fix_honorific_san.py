#!/usr/bin/env python3
"""กวาดคำเรียกที่ EN มี honorific `-san` แต่ไทยใช้ "คุณ+ชื่อ" แทน

กฎทีม: ถ้า EN เขียน honorific ไว้ (`-san`/`-kun`/`-chan`/`-sensei`) ต้องทับศัพท์ต่อท้ายชื่อ
(`Yagami-san` -> ยากามิซัง) · "คุณ+ชื่อ" ใช้เฉพาะตอน EN **ไม่มี** honorific

ทำไมต้องมีสคริปต์: กฎนี้เดิมอยู่แต่ใน characters_main.json นักแปลมองข้ามบ่อย
(ผู้ตรวจ TALK_017 เจอพลาด 7/7 จุดใน batch เดียว · master มีตกค้าง 30 จุดจาก 547)

สคริปต์นี้แก้เฉพาะกรณีที่ปลอดภัย: EN มี `<ชื่อ>-san` และไทยมี "คุณ<ชื่อ>" โดยที่ไทย
ยังไม่มีรูป "<ชื่อ>ซัง" อยู่แล้วในบรรทัดเดียวกัน (กันเคสที่บรรทัดนั้นมีทั้งสองแบบปนกันจริง ๆ)

ใช้:  python scripts/fix_honorific_san.py            # ดูเฉย ๆ
      python scripts/fix_honorific_san.py --write    # แก้ไฟล์ done (แล้วรัน remerge_stale.py ต่อ)
"""
import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

# ชื่อ EN -> (รูปไทยแบบ "คุณ+ชื่อ", รูปไทยแบบ "ชื่อ+ซัง")
NAMES = {
    "Yagami": ("คุณยากามิ", "ยากามิซัง"),
    "Kaito": ("คุณไคโตะ", "ไคโตะซัง"),
    "Sugiura": ("คุณซุกิอุระ", "ซุกิอุระซัง"),
    "Hoshino": ("คุณโฮชิโนะ", "โฮชิโนะซัง"),
    "Saori": ("คุณซาโอริ", "ซาโอริซัง"),
    "Higashi": ("คุณฮิงาชิ", "ฮิงาชิซัง"),
    "Meguro": ("คุณเมกุโระ", "เมกุโระซัง"),
    "Kawada": ("คุณคาวาดะ", "คาวาดะซัง"),
    "Uozumi": ("คุณอุโอซึมิ", "อุโอซึมิซัง"),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    total = 0
    for p in sorted((paths.TRANSLATIONS / "done").glob("*.done.json")):
        d = json.load(io.open(p, encoding="utf-8"))
        hits = 0
        for en, th in d["strings"].items():
            for name, (khun, san) in NAMES.items():
                if ("%s-san" % name) in en and khun in th and san not in th:
                    d["strings"][en] = th.replace(khun, san)
                    th = d["strings"][en]
                    hits += 1
        if hits:
            total += hits
            print("%-34s %d จุด" % (p.name, hits))
            if a.write:
                io.open(p, "w", encoding="utf-8").write(
                    json.dumps(d, ensure_ascii=False, indent=1))
    print("รวม %d จุด%s" % (total, " (แก้แล้ว)" if a.write else " (ใส่ --write เพื่อแก้)"))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
