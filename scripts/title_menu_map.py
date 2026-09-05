#!/usr/bin/env python3
"""ผัง **รอบ 8** — เมนูหน้าไตเติลภาษาไทยของจริง ด้วย pre-composed cluster + donor จับคู่ความกว้าง

นี่คือรูปแบบที่จะใช้จริงถ้าผ่าน (ไม่ใช่ probe แล้ว): ข้อความเมนูไทยเต็มรูปแบบ แต่ละเซลล์คือ
ฐาน+สระ+วรรณยุกต์ที่ประกอบเป็นกลิฟเดียว และ donor ถูกเลือกให้ความกว้างใกล้เคียงกลิฟจริง
(เหตุผลทั้งหมด + ผลทดสอบที่เป็นที่มาของวิธีนี้: `scripts/title_encode.py` และ HANDOFF.md)

LICENSE INFORMATION / ADDITIONAL CREDITS คงภาษาอังกฤษตามกติกาเหล็กข้อ 10 — และยังทำหน้าที่
เป็นตัวควบคุมด้วยว่าฟอนต์อังกฤษไม่พังจากการที่เราทับเซลล์ตัวอักษรมีเครื่องหมาย
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from title_encode import build_map, encode, natural_width, segment

# (row_key, field, ข้อความไทย)
MENU = [
    ("judge_new_game", "name", "เริ่มเกมใหม่"),
    ("judge_new_game", "explanation", "เริ่มเล่นตั้งแต่ต้นเรื่อง"),
    ("judge_load", "name", "เล่นต่อ"),
    ("judge_load", "explanation", "เล่นต่อจากไฟล์เซฟ"),
    ("judge_2p_match_mini_game", "name", "มินิเกมสองผู้เล่น"),
    ("judge_option", "name", "ตั้งค่า"),
    ("judge_movie", "name", "ดูฉากย้อนหลัง"),
    ("quit_game", "name", "ออกจากเกม"),
]

# ข้อความนอก title_root ที่ต้องใช้กลิฟชุดเดียวกัน — (ไฟล์ bin, เส้นทางใน json, ข้อความไทย, หมายเหตุ)
# แพตช์ด้วย `scripts/make_extra_tests.py`
EXTRA_TARGETS = [
    ("ui_text.bin", ["1889", "", "text"], "กดปุ่มใดก็ได้",
     "จอโลโก้ก่อนไตเติล — ยืนยันแล้วว่าใช้ฟอนต์ไตเติล"),
    ("msg.bin", ["10", "save_data", "table", "34", "", "1"], "บันทึกเรียบร้อยแล้ว",
     "กล่องยืนยันหลังเซฟ — รอบก่อนเขียนเป็น cp ไทยจริงแล้วขึ้นว่าง รอบนี้ลอง donor ฟอนต์ไตเติล"),
]

EXTRA = {"press_any_button": EXTRA_TARGETS[0][2], "save_completed": EXTRA_TARGETS[1][2]}

STRINGS = [text for _k, _f, text in MENU] + [t[2] for t in EXTRA_TARGETS]


def _glyph_width(cell_text):
    """ความกว้าง ink ของเซลล์ = ความกว้างของฐาน (มาร์กวางกึ่งกลางเหนือฐาน ไม่กินที่เพิ่ม)"""
    return natural_width(cell_text)


CELLS, ENCODE = build_map(STRINGS, _glyph_width)

ROWS = [(k, f, encode(text, ENCODE), text) for k, f, text in MENU]

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print(f"ใช้ {len(CELLS)} เซลล์ จาก donor pool 49 ช่อง")
    for cp, entry in sorted(CELLS.items(), key=lambda kv: kv[1][0]):
        print(f"  {entry[0]:4s} -> U+{cp:04X} {chr(cp)}  [{entry[1]}]")
    print()
    for k, f, enc, text in ROWS:
        print(f"  {k}.{f} = {text}  ->  {enc!r}")
