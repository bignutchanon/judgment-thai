#!/usr/bin/env python3
"""ชุดทดสอบ **รอบ 6** ของฟอนต์หน้าไตเติล — ล่า donor advance = 0 รอบสอง (ช่วง control 0x00-0x1F)

ผลรอบ 5: ผู้สมัครทั้ง 5 ตัว (NBSP, soft hyphen, ¨, ´, ¡) **ได้ advance > 0 ทุกตัว** —
วรรณยุกต์แยกออกมาเป็นตัวถัดไปหมด ไม่มีตัวไหนลอยทับ `ก` (NBSP กับ ¡ แคบสุดแต่ก็ยังกินที่)

รอบนี้ล่าในช่วงที่ยังไม่เคยแตะ: **codepoint 0x00-0x1F + 0x7F** ซึ่งมีเซลล์อยู่จริงในตาราง
atlas (แถว 0-1) และส่วนใหญ่ว่างเปล่า — ถ้า engine ให้ width 0 กับอักขระควบคุมเหล่านี้
(ซึ่งเป็นค่าปกติของตาราง width ทั่วไป) ก็จะได้มาร์กลอยโดยไม่ต้อง pre-compose

⚠ ความเสี่ยงที่ยอมรับในรอบทดสอบนี้: อักขระควบคุมอาจถูก engine ตีความเป็นอย่างอื่น
(ตัดบรรทัด/จบสตริง/มาร์กอัป) — ถ้าแถวไหนข้อความหายหรือเพี้ยนทั้งแถว = ตัด codepoint นั้นทิ้ง
เลี่ยง 0x00 (null = จบสตริง), 0x09 (tab), 0x0A/0x0D (ขึ้นบรรทัด) และเซลล์ที่มีหมึกเดิมอยู่แล้ว
(0x02 0x03 0x04 0x09 0x0A 0x0B = กลิฟสัญลักษณ์ของเกม ห้ามทับ)
"""
import io
import sys

CP_BASE = 0xC7          # È — ฐาน `ก` เหมือนรอบ 5 (เทียบข้ามรอบได้)

CAND = [0x01, 0x05, 0x0E, 0x1F, 0x7F]   # เซลล์ว่างในช่วง control ที่ปลอดภัยพอจะลอง

CELLS = {CP_BASE: ("ก", "base")}
for cp in CAND:
    CELLS[cp] = ("่", f"cand U+{cp:04X}")


def _pairs(mark_cp, n=3):
    return (chr(CP_BASE) + chr(mark_cp)) * n


ROWS = [
    ("judge_new_game", "name", _pairs(0x01), "วรรณยุกต์บน donor U+0001"),
    ("judge_load", "name", _pairs(0x05), "วรรณยุกต์บน donor U+0005"),
    ("judge_2p_match_mini_game", "name", _pairs(0x0E), "วรรณยุกต์บน donor U+000E"),
    ("judge_option", "name", _pairs(0x1F), "วรรณยุกต์บน donor U+001F"),
    ("judge_movie", "name", _pairs(0x7F), "วรรณยุกต์บน donor U+007F (DEL)"),
    ("quit_game", "name", chr(CP_BASE) * 3, "ควบคุม: ก 3 ตัวไม่มีวรรณยุกต์ = ระยะฐานล้วน"),
]

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    for cp, (spec, tag) in sorted(CELLS.items()):
        print(f"  U+{cp:04X} <- {spec!r} [{tag}]")
    print()
    for row_key, field, s, q in ROWS:
        print(f"  {row_key}.{field} = {s!r}  ({q})")
