#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ผัง **probe หวี (comb)** — วัด advance ของ donor ทั้งชุดในภาพเดียว

ปัญหา: advance ของแต่ละ donor อยู่ในตาราง width ใน `Judgment.exe` อ่านตรงไม่ได้ (สแกนแล้วไม่เจอ)
และเดาไม่ได้ เพราะ advance ไม่ผูกกับความกว้าง ink แบบเชิงเส้น (M ink 22 -> advance 28 แต่
¡ ink 4 -> advance 18) — **เดาผิดแล้วตัวอักษรวาดทับกันจนหายไปเลย** (เห็นจริงบนจอรอบ 14: ก ง า หาย)

วิธีหวี: วาด **ขีดตั้งบาง ๆ ตัวเดียวกัน** ลงในทุกเซลล์ที่ต้องวัด แล้วเรียงเป็นแถวยาวในเมนู
หน้าไตเติล — ระยะระหว่างขีดที่ i กับ i+1 บนจอ = advance ของ donor ตัวที่ i พอดี
(ทุกเซลล์วาด ink ที่ x = INK_X0 เท่ากันหมด ค่าคงที่นี้จึงหักล้างกันเอง)
แถวแรกเป็นแถวเทียบมาตราส่วน: ตัว `M` ของเกมเอง (เซลล์ ASCII ไม่ถูกแตะ) ซึ่งรู้ ink จริงจาก atlas

บทเรียนรอบแรก (22 ส.ค. 2026): **แถวที่เคอร์เซอร์เมนูเลือกอยู่ถูกแถบไฮไลต์กลืนจนวัดไม่ได้**
(เสียไป 26 ตัว) → รอบนี้เว้นแถวที่ 2 (แถวที่เกมเลือกไว้ตอนเปิดเมนู) ไม่ใส่ข้อมูล

โหมด (ตัวแปรสภาพแวดล้อม `COMB_MODE`):
  provisional (ค่าเริ่มต้น) = เฉพาะ donor ที่ค่ายังเป็น "ค่าเดา" ใน translations/donor_widths.json
  all                       = donor ทั้ง pool (ใช้ตอนอยากวัดซ้ำทั้งชุด)

คู่กับ:
  python scripts/deploy_probe.py           # build ฟอนต์หวี + title_root แล้ว deploy ลงเกม
  -> ผู้ใช้เปิดเกมถึงหน้าไตเติล แคปหน้าจอเป็น PNG
  python scripts/measure_comb.py <ภาพ>     # อ่านค่า -> translations/donor_widths.json
  python scripts/deploy_probe.py --play    # กลับไปบิลด์ไทยเล่นจริง
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths                                        # noqa: E402
from slot_alloc import DEFAULT_TIERS, WIDTHS_FILE, build_pool, en_used_codepoints, \
    th_used_codepoints                              # noqa: E402

BAR = "l"              # กลิฟที่ใช้เป็นซี่หวี — เส้นตั้งบาง ink แคบ วัดตำแหน่งง่าย
CAL_ROW = "MMMMMMMM"   # แถวเทียบมาตราส่วน (เซลล์ ASCII ของเกม ไม่ถูกทับ)

# แถวข้อความที่หน้าไตเติลแสดงจริง เรียงบนลงล่าง — ใช้เฉพาะช่อง `name`
# (explanation โชว์แค่ของแถวที่เลือกอยู่แถวเดียว)
TITLE_ROWS = [
    ("judge_new_game", "name"),               # แถวเทียบมาตราส่วน
    ("judge_load", "name"),                   # **เว้นว่าง** — แถบไฮไลต์เริ่มต้นทับแถวนี้
    ("judge_2p_match_mini_game", "name"),
    ("judge_option", "name"),
    ("judge_movie", "name"),
    ("judge_license", "name"),
    ("staffroll", "name"),
    ("quit_game", "name"),
]
DATA_ROWS = TITLE_ROWS[2:]                    # 6 แถวที่ใส่ซี่หวีได้


def target_donors():
    """donor ที่ต้องวัดรอบนี้ (เรียงตาม codepoint)"""
    en_used, _ = en_used_codepoints()
    reserved = set(en_used) | set(th_used_codepoints())
    pool = build_pool(DEFAULT_TIERS, reserved)
    if os.environ.get("COMB_MODE", "provisional") == "all" or not WIDTHS_FILE.exists():
        return pool
    data = json.load(io.open(WIDTHS_FILE, encoding="utf-8"))
    prov = set(data.get("provisional_extA_default", [])) | \
        set(data.get("provisional_from_ink", []))
    todo = [cp for cp in pool if "%04X" % cp in prov]
    return todo or pool


TARGETS = target_donors()
PER_ROW = -(-len(TARGETS) // len(DATA_ROWS)) if TARGETS else 1
CHUNKS = [TARGETS[i:i + PER_ROW] for i in range(0, len(TARGETS), PER_ROW)]

CELLS = {cp: (BAR, "comb") for cp in TARGETS}

ROWS = [(TITLE_ROWS[0][0], TITLE_ROWS[0][1], CAL_ROW, "แถวเทียบมาตราส่วน (M ของเกมเอง)")]
for i, chunk in enumerate(CHUNKS):
    key, field = DATA_ROWS[i]
    # ปิดท้ายแถวด้วย M ของเกมเอง เพื่อให้ซี่สุดท้ายมีระยะถัดไปให้วัดด้วย
    ROWS.append((key, field, "".join(chr(cp) for cp in chunk) + "M",
                 "ซี่หวี %d ตัว: U+%04X..U+%04X" % (len(chunk), chunk[0], chunk[-1])))

LAYOUT = {"calibration": CAL_ROW, "rows": [list(c) for c in CHUNKS]}


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print("donor ที่ต้องวัดรอบนี้ %d ตัว · แถวละ %d · ใช้ %d แถว (+1 แถวเทียบมาตราส่วน)"
          % (len(TARGETS), PER_ROW, len(CHUNKS)))
    for key, field, s, note in ROWS:
        print("  %-28s %-12s %2d เซลล์  %s" % (key, field, len(s), note))
