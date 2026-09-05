#!/usr/bin/env python3
"""ชุดทดสอบ **รอบ 5** ของฟอนต์หน้าไตเติล — หา donor ที่ได้ advance = 0 (ทีละตัวแปรต่อแถว)

รอบ 4 ยืนยันแล้วว่า **advance มาจาก codepoint ของ donor** (ตาราง width ใน exe) ไม่ใช่จากรูป
ที่เราวาด: `ก` ตัวเดียวกันบน donor แคบ (¡ ¹ Í Ì Ï) เรียงชิดกว่าบน donor กว้าง (Ò Ó Ô Õ Ö)
อย่างเห็นได้ชัด และเซลล์ว่างของ Latin Ext-A ก็ได้ advance ปกติ ไม่ใช่ 0

รอบ 4 ใส่ผู้สมัคร advance-0 ทั้ง 4 ตัวไว้แถวเดียวกัน ทำให้อ่านผลกำกวม รอบนี้จึงแยก
**หนึ่งผู้สมัครต่อหนึ่งแถว** และซ้ำ 3 คู่ต่อแถวเพื่อให้เห็นระยะชัด

รูปแบบทุกแถว: `ก` + `่` สลับกัน 3 คู่ (ฐานเป็น donor เดียวกันหมด = È U+00C7)
อ่านผลได้ 3 แบบ:
  - วรรณยุกต์ลอยทับ `ก` พอดี      -> donor นั้น advance = 0  (เป้าหมาย)
  - วรรณยุกต์แยกออกมาเป็นตัวถัดไป -> advance > 0
  - ไม่เห็นวรรณยุกต์เลย            -> engine ข้าม codepoint นั้นทั้งตัว (เช่นถูกตีความเป็น
                                     whitespace/soft-hyphen แล้วไม่วาด)
"""
import io
import sys

CP_BASE = 0xC7          # È — ฐาน `ก` ของทุกแถว (ตัวควบคุมเดียวกันหมด)

# ผู้สมัคร donor สำหรับวรรณยุกต์ (หนึ่งตัวต่อหนึ่งแถว)
CAND_NBSP = 0xA0        # no-break space — ไม่มีหมึกในฟอนต์เดิม
CAND_SHY = 0xAD         # soft hyphen — ปกติเป็นอักขระ "มองไม่เห็น"
CAND_DIAERESIS = 0xA8   # ¨ — เครื่องหมายเสริมสัทอักษร มักได้ความกว้างแคบ
CAND_ACUTE = 0xB4       # ´ — เช่นเดียวกัน
CAND_INVEXCL = 0xA1     # ¡ — กลิฟจริงที่แคบสุดในตาราง (ink 5 px)

CELLS = {
    CP_BASE: ("ก", "base"),
    CAND_NBSP: ("่", "cand NBSP"),
    CAND_SHY: ("่", "cand soft-hyphen"),
    CAND_DIAERESIS: ("่", "cand ¨"),
    CAND_ACUTE: ("่", "cand ´"),
    CAND_INVEXCL: ("่", "cand ¡"),
}


def _pairs(mark_cp, n=3):
    return (chr(CP_BASE) + chr(mark_cp)) * n


ROWS = [
    ("judge_new_game", "name", _pairs(CAND_NBSP), "วรรณยุกต์บน donor NBSP (U+00A0)"),
    ("judge_load", "name", _pairs(CAND_SHY), "วรรณยุกต์บน donor soft hyphen (U+00AD)"),
    ("judge_2p_match_mini_game", "name", _pairs(CAND_DIAERESIS), "วรรณยุกต์บน donor ¨ (U+00A8)"),
    ("judge_option", "name", _pairs(CAND_ACUTE), "วรรณยุกต์บน donor ´ (U+00B4)"),
    ("judge_movie", "name", _pairs(CAND_INVEXCL), "วรรณยุกต์บน donor ¡ (U+00A1, กลิฟแคบสุด)"),
    ("quit_game", "name", chr(CP_BASE) * 3, "ควบคุม: ก 3 ตัวไม่มีวรรณยุกต์ = ระยะฐานล้วน"),
]

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    for cp, (spec, tag) in sorted(CELLS.items()):
        print(f"  U+{cp:04X} <- {spec!r} [{tag}]")
    print()
    for row_key, field, s, q in ROWS:
        print(f"  {row_key}.{field} = {s!r}  ({q})")
