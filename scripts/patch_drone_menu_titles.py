#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เลื่อนหัวข้อเมนูโดรน (FLIGHT / CUSTOMIZE / RACE RECORD / OPERATION) ให้พ้นคำอธิบาย
หลังจากล้าง donor ในฟอนต์สไปรต์ (`strip_ui_sprite_slots.py`) แล้วหัวข้อ fallback ไปฟอนต์ปกติ

## อาการ (ภาพผู้ใช้ 5 ก.ย. 2026 บ่าย)

หัวข้อทั้ง 4 ขึ้นเป็นไทยได้แล้ว แต่ตกลงมาอยู่ใต้เส้นคั่นและทับกับคำอธิบายของแถวที่เลือก
("ทะยานสู่ท้องฟ้า" ทับ "การบิน")

## สาเหตุ (จาก `ui.judge.en.par/en/scene/pause_drone.bin`)

แต่ละแถวเมนู = ตารางย่อย `top_menu_list_item0..3` (121 คอลัมน์ · column-major) ประกอบด้วย
* `category`  = หัวข้อ · type 3 (text) · pos (-868, -17) · กล่อง 800x80 · pivot (0, 40) = ซ้าย-กลาง
                · col47 (ขนาดฟอนต์) = 0 · col59 = 4 · col81 = 2 → โหมดฟอนต์ภาพ `drone_font`
* `line1`     = เส้นคั่นที่ y = +17
* `text`      = คำอธิบาย (แสดงเฉพาะแถวที่เลือก) · pos (-867, +32) · กล่อง 128x20 · pivot (0, 10) · col47 = 20
กล่องหัวข้อกินพื้นที่ -57..+23 (เหนือเส้น) แต่ตอน fallback เอนจิ้นวางข้อความฟอนต์ปกติที่
**pos.y + pivot.y = +23** (ขอบล่างของกล่อง) แทนที่จะจัดกลางกล่อง ข้อความจึงไปนอนที่ +23..+45 ทับคำอธิบาย
(วัดจากภาพ: ตัวหนังสือเริ่มต่ำกว่าเส้นราว 8 px ในหน่วย UI)

## วิธีแก้

แก้ค่าในตาราง scene ระดับไบต์ (ห้ามผ่าน reARMP — บทเรียน LJ-011/LJ-015 layout เลื่อนเงียบ ๆ):
* col11 (pos.y) -17 → CATEGORY_Y  (เลื่อนขึ้นให้ข้อความ fallback ไปอยู่ตำแหน่งเดิมของหัวข้อสไปรต์)
* col47 (ขนาดฟอนต์) 0 → CATEGORY_FONT_SIZE (ถ้าเอนจิ้นอ่านค่านี้ตอน fallback จะได้หัวข้อใหญ่ขึ้น
  ถ้าไม่อ่านก็ไม่เสียหาย)
ไม่แตะคอลัมน์โหมดฟอนต์ (col59/col81) เพราะยังไม่รู้ว่าโค้ดเกมเลือกฟอนต์ภาพจากคอลัมน์หรือจากชื่อ element

ใช้:
  python scripts/patch_drone_menu_titles.py            # ตรวจ/รายงานอย่างเดียว
  python scripts/patch_drone_menu_titles.py --write    # เขียน build/ui/ui.judge.en/en/scene/pause_drone.bin
อ่าน extracted/ui_en/en/scene/pause_drone.bin (ไม่แตะ) · deploy ด้วย deploy_spoil.py (คัดลอกทั้ง build/ui/ui.judge.en)
"""
import argparse
import io
import os
import struct
import sys

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths                                        # noqa: E402

SRC = paths.EXTRACTED / "ui_en" / "en" / "scene" / "pause_drone.bin"
OUT = paths.BUILD / "ui" / "ui.judge.en" / "en" / "scene" / "pause_drone.bin"

N_COLS = 121                 # คอลัมน์ของตารางย่อย top_menu_list_item*
ROW_COUNTS = (22, 21)        # item0-2 = 22 แถว · item3 = 21 แถว
N_ITEMS = 4

# ค่าเดิมของแถว category ที่ใช้ยืนยันว่าเจอถูกแถว
ORIG = {10: -868.0, 11: -17.0, 38: 800.0, 39: 80.0, 41: 0.0, 42: 40.0}
ORIG_INT = {47: 0, 59: 4, 81: 2}

# ค่าใหม่ (ปรับได้หลังดูภาพผู้ใช้)
CATEGORY_Y = -62.0           # ข้อความ fallback จะเริ่มที่ pos.y + pivot.y = -22 (เหนือเส้น +17 ราว 39 px)
CATEGORY_FONT_SIZE = 30      # col47 — คำอธิบายใช้ 20 · หัวข้อควรใหญ่กว่า


def col_offsets(data, hdr):
    p1c = struct.unpack_from("<i", data, hdr + 0x1C)[0]
    return struct.unpack_from("<%di" % N_COLS, data, p1c)


def find_tables(data):
    """คืน [(header_offset, row_count, offsets)] ของตารางย่อย top_menu_list_item* ที่ยืนยันแถว category ได้"""
    found = []
    for rows in ROW_COUNTS:
        pat = struct.pack("<3i", rows, N_COLS, 0)
        i = -1
        while True:
            i = data.find(pat, i + 1)
            if i < 0:
                break
            p18, p1c = struct.unpack_from("<2i", data, i + 0x18)
            if not (0 < p18 < len(data) and 0 < p1c < len(data)):
                continue
            offs = col_offsets(data, i)
            if any(not (0 < o < len(data)) for o in (offs[10], offs[11], offs[47], offs[81])):
                continue
            cat = category_row(data, offs, rows)
            if cat is not None:
                found.append((i, rows, offs, cat))
    return found


def f32(data, offs, col, row):
    return struct.unpack_from("<f", data, offs[col] + 4 * row)[0]


def u8(data, offs, col, row):
    """คอลัมน์ type 2 ของตาราง scene เก็บ 1 ไบต์ต่อแถว (ยืนยันจาก col47 ของแถวคำอธิบาย = 0x14 = 20)"""
    return data[offs[col] + row]


def category_row(data, offs, rows):
    for r in range(rows):
        try:
            if all(f32(data, offs, c, r) == v for c, v in ORIG.items()) and \
               all(u8(data, offs, c, r) == v for c, v in ORIG_INT.items()):
                return r
        except struct.error:
            return None
    return None


def main():
    ap = argparse.ArgumentParser(description="เลื่อนหัวข้อเมนูโดรนให้พ้นคำอธิบาย")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    assert SRC.exists(), "ยังไม่ได้แตก ui.judge.en.par → tools/ParTool.exe extract <par> extracted/ui_en"

    data = bytearray(io.open(SRC, "rb").read())
    tables = find_tables(data)
    print("ตารางย่อย top_menu_list_item ที่เจอ: %d (ต้องการ %d)" % (len(tables), N_ITEMS))
    if len(tables) != N_ITEMS:
        sys.exit("!! จำนวนตารางไม่ตรง — โครงไฟล์อาจเปลี่ยน ห้ามเขียน")

    touched = set()
    for hdr, rows, offs, cat in tables:
        # แถว text (คำอธิบาย) ต้องอยู่ที่ y=+32 ในตารางเดียวกัน — ยืนยันว่าเป็นเมนูหลักจริง
        desc = [r for r in range(rows) if f32(data, offs, 11, r) == 32.0 and u8(data, offs, 47, r) == 20]
        print("  header @%06x  %d แถว  category=แถว %d  คำอธิบาย=แถว %s" % (hdr, rows, cat, desc))
        if not desc:
            sys.exit("!! ไม่เจอแถวคำอธิบายในตาราง @%x" % hdr)
        y_off = offs[11] + 4 * cat
        sz_off = offs[47] + cat
        struct.pack_into("<f", data, y_off, CATEGORY_Y)
        data[sz_off] = CATEGORY_FONT_SIZE
        touched.update(range(y_off, y_off + 4))
        touched.add(sz_off)

    orig = io.open(SRC, "rb").read()
    diff = {i for i, (x, y) in enumerate(zip(orig, data)) if x != y}
    assert len(orig) == len(data) and diff <= touched, "มีไบต์นอกช่องที่ตั้งใจแก้เปลี่ยน"
    print("ไบต์ที่เปลี่ยน %d (col11 → %.0f · col47 → %d ใน %d แถว category)"
          % (len(diff), CATEGORY_Y, CATEGORY_FONT_SIZE, N_ITEMS))

    if not a.write:
        print("(ยังไม่เขียนไฟล์ — ใส่ --write เพื่อเขียนจริง)")
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    io.open(OUT, "wb").write(bytes(data))
    print("เขียน", OUT)


if __name__ == "__main__":
    main()
