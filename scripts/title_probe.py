#!/usr/bin/env python3
"""ชุดทดสอบ **รอบ 4** ของฟอนต์หน้าไตเติล — วัด "ตาราง width ใน exe" โดยไม่ต้อง RE

ผลรอบ 3 (ภาพจากผู้ใช้ 20 ส.ค. 2026) พิสูจน์แล้ว:
  - ไทยขึ้นหน้าไตเติลได้ทั้งกลุ่ม A (เซลล์มีหมึก) และกลุ่ม B (เซลล์ว่าง Latin Ext-A)
    → แอ่ง donor ของฟอนต์ไตเติล = 61 + 152 = 213 ช่อง ไม่มีปม "เซลล์ว่าง = tofu" แบบ Y6
  - ตัวฐานเรียงชิดปกติ (ฟอนต์นี้ proportional จริง ไม่ใช่ fixed-pitch แบบ tbgm_0p_ja)
  - **มาร์กกินที่แนวนอน** ("เริ่ ม", "ตั้ ง") เพราะไปนั่งบน donor Ñ Ò Ó Ô ที่กว้างเต็มตัว

สมมติฐานที่รอบนี้ทดสอบ: ความกว้างมาจาก **codepoint ของ donor** (ตารางใน exe) ไม่ใช่จาก
รูปที่เราวาด → ถ้าจริง การเลือก donor ก็คือการเลือก advance โดยไม่ต้องแตะ exe เลย

วิธี: วาด `ก` ตัวเดียวกันลง donor สามคลาส แล้วดูระยะบนจอ + ทดสอบ donor ที่น่าจะ advance ≈ 0
สำหรับมาร์ก + เทียบ per-char กับ pre-composed cluster ด้วยคำเดียวกัน

ink width ของเซลล์ต้นฉบับ (วัดจาก atlas — ใช้เป็นตัวแทนคร่าว ๆ ของ advance ที่ exe จะให้):
  ¡ 5 · ¹ 8 · Í 8 · Ì 9 · Ï 11    |    Ò Ó Ô Õ Ö 19    |    เซลล์ว่าง = ไม่มีหมึกเลย
"""
import io
import sys

# ---- donor สามคลาสสำหรับวัดระยะ (ทุกช่องวาด `ก` ตัวเดียวกัน) ----
NARROW = [0xA1, 0xB9, 0xCD, 0xCC, 0xCF]        # ¡ ¹ Í Ì Ï  (ink 5-11 px)
WIDE = [0xD2, 0xD3, 0xD4, 0xD5, 0xD6]          # Ò Ó Ô Õ Ö  (ink 19 px)
EMPTY = [0x120, 0x121, 0x122, 0x123, 0x124]    # เซลล์ว่างใน Latin Ext-A

# ---- donor ที่อาจได้ advance ใกล้ 0 (ถ้าตัวใดตัวหนึ่งได้ = มาร์กลอยได้โดยไม่ต้อง pre-compose) ----
ZERO_CANDIDATES = [0xA0, 0xAD, 0xA8, 0xB4]     # NBSP · soft hyphen · ¨ · ´

# ---- เซลล์สำหรับคำทดสอบ "เริ่ม" ----
CP_SARA_E = 0xC0        # เ
CP_RO = 0xC1            # ร
CP_MO = 0xC2            # ม
CP_CLUSTER = 0xC3       # "ริ่" ประกอบเป็นกลิฟเดียว
CP_BASE_KO = 0xC7       # ก (ตัวฐานของแถวทดสอบ zero-width)
CP_MARK_I = 0xEC        # ิ  บน donor แคบ (ì, ink 9)
CP_MARK_TONE = 0xED     # ่  บน donor แคบ (í, ink 8)

# cp -> (สิ่งที่จะวาดลงเซลล์, ป้ายกำกับสำหรับรายงาน)
CELLS = {}
for cp in NARROW:
    CELLS[cp] = ("ก", "narrow")
for cp in WIDE:
    CELLS[cp] = ("ก", "wide")
for cp in EMPTY:
    CELLS[cp] = ("ก", "empty-cell")
for cp in ZERO_CANDIDATES:
    CELLS[cp] = ("่", "zero-cand")
CELLS[CP_SARA_E] = ("เ", "word")
CELLS[CP_RO] = ("ร", "word")
CELLS[CP_MO] = ("ม", "word")
CELLS[CP_CLUSTER] = ("ริ่", "cluster")      # ประกอบ base+สระบน+วรรณยุกต์ ในเซลล์เดียว
CELLS[CP_BASE_KO] = ("ก", "word")
CELLS[CP_MARK_I] = ("ิ", "mark-narrow")
CELLS[CP_MARK_TONE] = ("่", "mark-narrow")

assert len(CELLS) == 5 * 3 + 4 + 7, f"เซลล์ซ้ำกัน — เหลือ {len(CELLS)} ช่อง"


def _s(cps):
    return "".join(chr(c) for c in cps)


# (row_key, field, สตริง donor, สิ่งที่แถวนี้ตอบ)
ROWS = [
    ("judge_new_game", "name", _s(NARROW),
     "ก x5 บน donor แคบ (¡ ¹ Í Ì Ï) — ระยะแคบสุดที่ทำได้"),
    ("judge_load", "name", _s(WIDE),
     "ก x5 บน donor กว้าง (Ò Ó Ô Õ Ö) — ระยะกว้างสุด เทียบกับแถวบน"),
    ("judge_2p_match_mini_game", "name", _s(EMPTY),
     "ก x5 บนเซลล์ว่าง Ext-A — เซลล์ว่างได้ advance เท่าไร"),
    ("judge_option", "name",
     _s([CP_BASE_KO, 0xA0, CP_BASE_KO, 0xAD, CP_BASE_KO, 0xA8, CP_BASE_KO, 0xB4]),
     "ก+่ สลับกัน 4 คู่ ด้วย donor NBSP / soft hyphen / ¨ / ´ — คู่ไหนวรรณยุกต์ลอยทับ ก = advance 0"),
    ("judge_movie", "name", _s([CP_SARA_E, CP_CLUSTER, CP_MO]),
     "เริ่ม แบบ pre-composed (ริ่ = กลิฟเดียว) — เป้าหมายที่อยากได้"),
    ("quit_game", "name", _s([CP_SARA_E, CP_RO, CP_MARK_I, CP_MARK_TONE, CP_MO]),
     "เริ่ม แบบ per-char มาร์กบน donor แคบ — เทียบกับแถวบนโดยตรง"),
]

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print(f"เซลล์ที่จะเขียน {len(CELLS)} ช่อง")
    for cp, (spec, tag) in sorted(CELLS.items()):
        print(f"  U+{cp:04X} <- {spec!r} [{tag}]")
    print()
    for row_key, field, s, q in ROWS:
        print(f"  {row_key}.{field} = {s!r}  ({q})")
