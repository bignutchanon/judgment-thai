#!/usr/bin/env python3
"""Donor slot map สำหรับ **ฟอนต์หน้าไตเติล/เมนู** ของ Judgment: `meta_ot_cond_book.dds`

ฟอนต์ตัวนี้ไม่ใช่ `FONT!` — ไม่มีไฟล์ `.bin` คู่เลย เป็น **bitmap grid ล้วน** ที่ตำแหน่ง
เซลล์คือค่า codepoint ตรง ๆ (ผังเดียวกับ `hd2_hankaku.dds` ของเอนจิ้นยุค Yakuza 0/Kiwami
ที่ชุมชนบันทึกไว้ว่า "ตาราง width/kerning อยู่ใน exe ไม่ใช่ไฟล์ data" — ดู
docs/research_web/jp_th_community_sweep.md)

ผังที่ decode จากไฟล์จริงแล้ว (20 ส.ค. 2026 — ยืนยันด้วยตา ไม่ใช่เดา):
  atlas 512x1536 BC4U · 16 คอลัมน์ · cell 32x64 · 24 แถว = 384 เซลล์
  **ตารางข้าม C1 block**: เซลล์ n = cp เมื่อ n < 0x80 · เซลล์ n = cp - 0x20 เมื่อ cp >= 0xA0
  → ครอบคลุม U+0000-007F แล้วต่อด้วย U+00A0-019F (Latin-1 + Latin Extended-A)
  พิสูจน์: แถว 10 = ÀÁÂÃÄ ÇÈÉÊËÌÍÎÏ (ถ้า cp = 16*row จะต้องเป็น ¡¢£ — ผิด)
  แถว 2 = `space ! " # $ % & ' ( ) * + , - . /` · แถว 3 = `0-9 : ; < = > ?` · แถว 4 = `@A-O`
  แถว 10-13 = ÀÁÂÃÄ ÇÈÉÊËÌÍÎÏ / ÑÒÓÔÕÖ ÙÚÛÜ ß / àáâãä çèéêëìíîï / ñòóôõö ùúûü
  Latin Ext-A มีหมึกจริงแค่ 8 ตัว (Ā ā Ō ō Œ œ Ū ū) ที่เหลือ 152 เซลล์ว่าง
  metrics ของกลิฟ (จากเซลล์ 'A'): ink เริ่ม x≈2, baseline y≈44, cap height ≈25px

**ทำไมหน้าไตเติลรอบ 1 ขึ้นว่างทั้งไทยแท้และ donor Cyrillic**: atlas นี้มีแค่
Latin/Latin-1/Latin-Ext-A ไม่มีทั้งไทยไม่มีทั้ง Cyrillic — คนละแอ่งกับ tbgm_0p_ja

## donor pool

เลือกเฉพาะช่วงที่ค่า Unicode = ค่า index เซลล์แน่นอน:
  - **0xA0-0xFF (Latin-1)** — Unicode กับ CP1252 ตรงกันทุกตัวในช่วงนี้
  - **0x100-0x19F (Latin Ext-A)** — ไม่กำกวม
ตัดทิ้ง: cp < 0x20 (control — 0x09/0x0A คือ tab/newline ห้ามแตะ) และ 0x80-0x9F
(ช่วงที่ CP1252 กับ Unicode ไม่ตรงกัน — ยังไม่รู้ว่า engine map ทางไหน)

## กลุ่มทดสอบ (รอบ 3)

| กลุ่ม | donor | ตอบคำถาม |
|---|---|---|
| A | เซลล์ **ที่มีหมึกอยู่แล้ว** ใน Latin-1 | ไทยขึ้นหน้าไตเติลได้ไหม + ระยะห่างเป็นแบบไหน |
| B | เซลล์ **ว่าง** ใน Latin Ext-A | เติมเซลล์ว่างได้ไหม (ปม "ช่องว่าง = tofu ถาวร" ของ Y6) และเซลล์ว่างมี advance เท่าไร |

ถ้า A ขึ้นแต่ B ว่าง = engine มีตาราง cp ปิดตายใน exe (เหมือน Y6)
ถ้าขึ้นทั้งคู่ = แอ่ง donor ของหน้าไตเติลกว้างมาก (152 ช่องว่างใน Ext-A)
"""
import io
import sys

COLS = 16
CELL_W, CELL_H = 32, 64
ATLAS_W, ATLAS_H = 512, 1536
N_CELLS = 384                  # 24 แถว x 16

INK_X0 = 2                     # ink เริ่มที่ x≈2 (วัดจากเซลล์ 'A','a','i','m')
BASELINE_Y = 44                # baseline ของฟอนต์นี้ในเซลล์ 64px
CAP_H = 25                     # ความสูงตัวพิมพ์ใหญ่

# ---- เซลล์ที่มีหมึกจริงในช่วง U+00A0-00FF (สแกนจาก atlas ต้นฉบับ 20 ส.ค. 2026) ----
INKED_LATIN1 = [
    0xA1, 0xA5, 0xA9, 0xAA, 0xAB, 0xAE, 0xB1, 0xB7, 0xB9, 0xBA, 0xBB, 0xBF,
    0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF,
    0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD9, 0xDA, 0xDB, 0xDC, 0xDF,
    0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF,
    0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF9, 0xFA, 0xFB, 0xFC,
]
assert len(INKED_LATIN1) == 61

INKED_EXTA = [0x100, 0x101, 0x14C, 0x14D, 0x152, 0x153, 0x16A, 0x16B]

# ใช้เฉพาะ "ตัวอักษรมีเครื่องหมาย" (U+00C0 ขึ้นไป) เป็น donor กลุ่ม A — เลี่ยงสัญลักษณ์
# © ® ¥ · » ¿ ที่มีโอกาสโผล่ในข้อความอังกฤษจริงของ UI
POOL_A = [cp for cp in INKED_LATIN1 if cp >= 0xC0]
assert len(POOL_A) == 49

# ---- เซลล์ว่างใน Latin Ext-A (U+0100-019F ที่ไม่มีหมึก) ----
EMPTY_EXTA = [cp for cp in range(0x100, 0x1A0) if cp not in INKED_EXTA]
assert len(EMPTY_EXTA) == 152

# ---- ตัวอักษรไทยที่ใช้ในสตริงทดสอบรอบ 3 ----
# ฐาน (พยัญชนะ/สระที่กินที่แนวนอน) + มาร์ก (สระบน/วรรณยุกต์ ที่ควร advance=0)
TEST_BASES = list("เรมกใหลนตองคาจ")
TEST_MARKS = list("ิ่ั้")
TEST_CHARS = TEST_BASES + TEST_MARKS
assert len(set(TEST_CHARS)) == len(TEST_CHARS), "ตัวอักษรทดสอบซ้ำ"

# กลุ่ม A: เซลล์มีหมึก (Latin-1) — เรียงจาก cp น้อยไปมาก ตัวอักษรเรียงตาม TEST_CHARS
MAP_A = {ch: cp for ch, cp in zip(TEST_CHARS, POOL_A)}
# กลุ่ม B: เซลล์ว่าง (Latin Ext-A)
MAP_B = {ch: cp for ch, cp in zip(TEST_CHARS, EMPTY_EXTA)}

assert len(MAP_A) == len(TEST_CHARS) and len(MAP_B) == len(TEST_CHARS)
assert not (set(MAP_A.values()) & set(MAP_B.values()))

# donor cp -> (ตัวอักษรไทย, กลุ่ม) สำหรับ inject + decode ย้อนกลับตอนอ่านผล
CELL_ASSIGN = {}
for ch, cp in MAP_A.items():
    CELL_ASSIGN[cp] = (ch, "A")
for ch, cp in MAP_B.items():
    CELL_ASSIGN[cp] = (ch, "B")


def cell_index(cp):
    """codepoint -> ลำดับเซลล์ในตาราง (ข้าม C1 block U+0080-009F ที่ไม่มีในตาราง)"""
    if cp < 0x80:
        return cp
    assert cp >= 0xA0, f"cp {cp:#x} อยู่ในช่วง C1 ที่ตารางนี้ข้ามไป"
    # cp เกิน 0x19F = เกินขอบ atlas ต้นฉบับ (ใช้ได้เฉพาะเมื่อขยาย atlas — ดู --height)
    return cp - 0x20


def cell_xy(cp):
    """codepoint -> (x0, y0) มุมซ้ายบนของเซลล์ใน atlas"""
    row, col = divmod(cell_index(cp), COLS)
    return col * CELL_W, row * CELL_H


def encode(text, group):
    """แปลงข้อความไทยเป็นสตริง donor ของกลุ่มที่เลือก (A หรือ B)"""
    table = MAP_A if group == "A" else MAP_B
    out = []
    for ch in text:
        if ch in table:
            out.append(chr(table[ch]))
        elif "฀" <= ch <= "๿":
            raise SystemExit(f"ตัวอักษรไทยไม่อยู่ในชุดทดสอบ: {ch!r} (U+{ord(ch):04X})")
        else:
            out.append(ch)
    return "".join(out)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print(f"ตาราง {COLS} คอลัมน์ · cell {CELL_W}x{CELL_H} · {N_CELLS} เซลล์ = U+0000-007F + U+00A0-019F")
    print(f"donor มีหมึก (Latin-1) {len(INKED_LATIN1)} ช่อง · ว่าง (Ext-A) {len(EMPTY_EXTA)} ช่อง")
    print(f"ตัวอักษรทดสอบ {len(TEST_CHARS)} ตัว: {''.join(TEST_CHARS)}")
    for ch in TEST_CHARS:
        print(f"  {ch}  A -> U+{MAP_A[ch]:04X} {chr(MAP_A[ch])!r}   B -> U+{MAP_B[ch]:04X}")
