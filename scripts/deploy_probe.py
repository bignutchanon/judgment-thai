#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สลับเกมระหว่าง **บิลด์เล่นจริง** กับ **บิลด์ probe หวี (วัดความกว้าง donor)** ด้วยคำสั่งเดียว

  python scripts/deploy_probe.py            # ลง probe หวี -> ผู้ใช้เปิดเกมถึงหน้าไตเติล แคปภาพ
  python scripts/deploy_probe.py --play     # กลับไปบิลด์ไทยเล่นจริง (ฟอนต์ + ข้อความทั้งเกม)

ทำไมต้องสลับ: ฟอนต์มีไฟล์เดียว (`meta_ot_cond_book.dds`) เซลล์ที่ probe ใช้เป็นเซลล์เดียวกับ
ที่ข้อความไทยใช้ จึงอยู่ในเกมพร้อมกันไม่ได้ · ขั้นตอน probe ใช้เวลาแค่เปิดเกมถึงหน้าไตเติล
"""
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = Path(__file__).resolve().parent
SHOT = HERE.parent / "shots" / "comb.png"


def run(*args):
    print(">", " ".join(str(a) for a in args))
    r = subprocess.run([sys.executable, str(HERE / args[0])] + [str(a) for a in args[1:]])
    if r.returncode != 0:
        sys.exit("!! ล้มเหลว: %s" % args[0])


def main():
    play = "--play" in sys.argv
    if play:
        run("inject_thai_title.py", "--slotmap")
        run("build_text.py", "--workers", "8", "--clean")
        run("deploy_spoil.py")
        print("\nลงบิลด์ไทยเล่นจริงแล้ว")
        return 0

    run("inject_thai_title.py", "--map", "title_comb")
    run("make_spoil_title4.py", "--map", "title_comb")
    run("deploy_spoil.py")
    SHOT.parent.mkdir(parents=True, exist_ok=True)
    print("""
ลง probe หวีแล้ว — ขั้นตอนของผู้ใช้:
  1. เปิดเกมให้ถึง **หน้าเมนูไตเติล** (เมนู 8 บรรทัดจะกลายเป็นแถวขีดตั้ง)
  2. กด PrintScreen แล้วเซฟภาพเป็น PNG ที่  %s
  3. ปิดเกม แล้วบอกกลับมา — ผมจะรัน
        python scripts/measure_comb.py shots/comb.png
        python scripts/deploy_probe.py --play
     เพื่อวัดความกว้าง 151 donor แล้วบิลด์ไทยตัวจริงกลับลงไป
""" % SHOT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
