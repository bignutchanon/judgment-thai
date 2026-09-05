#!/usr/bin/env python3
"""ชุดทดสอบ **รอบ 7** ของฟอนต์หน้าไตเติล — ขยาย atlas เพื่อเปิดเซลล์ใหม่เกิน U+019F

สรุปที่ได้จนถึงรอบ 6:
  - ไทยขึ้นหน้าไตเติลได้ ทั้งเซลล์ที่มีหมึกเดิมและเซลล์ว่าง
  - advance ผูกกับ codepoint ของ donor (ตาราง width ใน exe) — เลือก donor = เลือกระยะ
  - **ไม่มี codepoint ไหนที่ advance = 0** ทดสอบมาแล้ว 10 ตัว: NBSP, soft hyphen, ¨, ´, ¡
    (รอบ 5) และ U+0001, U+0005, U+000E, U+001F, U+007F (รอบ 6) — ทุกตัววาดกลิฟออกมาจริง
    แต่กินที่แนวนอนหมด และกลุ่ม control ได้ระยะเท่ากันทุกตัว = ค่า default ของตาราง
  → มาร์กลอยแบบ per-char เป็นไปไม่ได้บนฟอนต์นี้ ต้องใช้ **pre-composed cluster**

โจทย์ที่เหลือของเส้นทาง cluster คือ **จำนวนช่อง**: ตาราง atlas เดิมจบที่ U+019F = 384 เซลล์
ใช้ได้จริง ~213 ช่อง (มีหมึก 61 + ว่าง 152) หักพยัญชนะ/สระเดี่ยว 68 ตัว เหลือ ~145 ช่อง
สำหรับ cluster — Y6 ทั้งเกมมี 403 cluster ไม่ซ้ำ จึงเสี่ยงไม่พอ

รอบนี้ทดสอบว่า **ขยายภาพ atlas ให้สูงขึ้นแล้ว engine ยอมรับเซลล์แถวใหม่ไหม**
(สคริปต์ inject จะขยายภาพ + แก้ dwHeight/linear size ใน DDS header ให้อัตโนมัติ)
ถ้ายอมรับ = แอ่ง donor โตได้ตามต้องการ ปลดล็อกเส้นทาง cluster ทั้งเส้น

อ่านผล:
  - แถวที่ใช้ cp ใหม่ขึ้น `ก` = **atlas ขยายได้** (แถว LICENSE/CREDITS ต้องยังเป็นอังกฤษปกติ)
  - ขึ้นว่าง = engine จำกัดตารางไว้ใน exe → ต้องอยู่ในโควตา ~213 ช่องเดิม
  - เมนูอังกฤษเพี้ยน/ภาพรวมพัง = engine อ่านความสูงเดิมค้างไว้ → ถอดคืนด้วย --restore ทันที
"""
import io
import sys

CP_BASE = 0xC7          # È — `ก` ในตารางเดิม (ตัวควบคุม)

# cp ใหม่ที่อยู่นอกขอบ atlas ต้นฉบับ (U+01A0 ขึ้นไป = แถวที่ 29 ของตาราง)
NEW_CPS = [0x1A0, 0x1B0, 0x1C0, 0x200, 0x24F]

CELLS = {CP_BASE: ("ก", "base เดิม")}
for cp in NEW_CPS:
    CELLS[cp] = ("ก", f"เซลล์ใหม่ U+{cp:04X}")

ROWS = [
    ("judge_new_game", "name", chr(0x1A0) * 3, "ก x3 บนเซลล์ใหม่ U+01A0"),
    ("judge_load", "name", chr(0x1B0) * 3, "ก x3 บนเซลล์ใหม่ U+01B0"),
    ("judge_2p_match_mini_game", "name", chr(0x1C0) * 3, "ก x3 บนเซลล์ใหม่ U+01C0"),
    ("judge_option", "name", chr(0x200) * 3, "ก x3 บนเซลล์ใหม่ U+0200"),
    ("judge_movie", "name", chr(0x24F) * 3, "ก x3 บนเซลล์ใหม่ U+024F (ไกลสุดที่ทดสอบ)"),
    ("quit_game", "name", chr(CP_BASE) * 3, "ควบคุม: ก 3 ตัวบนเซลล์เดิม È — ต้องขึ้นเหมือนเดิม"),
]

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    for cp, (spec, tag) in sorted(CELLS.items()):
        print(f"  U+{cp:04X} <- {spec!r} [{tag}]")
    print()
    for row_key, field, s, q in ROWS:
        print(f"  {row_key}.{field} = {s!r}  ({q})")
