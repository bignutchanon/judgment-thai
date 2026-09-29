#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ยกป้ายแบนเนอร์กลางจอของแข่งโดรน (รอบที่สอง / รอบสุดท้าย / ถูกตัดสิทธิ์ / หมดเวลา) กลับเข้าแถบมืด

## อาการ (ภาพเจ้าของ 29 ก.ย. 2026)

แถบมืดกลางจอ (obi) ว่างเปล่า ส่วนข้อความไทยตัวเล็กตกลงไปอยู่ใต้แถบ วัดจากภาพ 1080p:
* "รอบที่สอง"   แถบ y 206-277 (กลาง 241) · หมึก y 279-298 (ขอบบนเซลล์ ~279 · เส้นฐาน ~298)
* "ถูกตัดสิทธิ์" แถบ y 480-598 (กลาง 539) · หมึก y 605-647 (ขอบบนเซลล์ ~606 · เส้นฐาน ~639)

## สาเหตุ (`ui.judge.en.par/en/scene/drone_play.bin`)

element ข้อความของแบนเนอร์ใช้ฟอนต์สไปรต์ (col47 = 0) กล่อง 600-1200 x 60 · pivot กลางกล่อง · ช่องไฟ col81 +4..+6
ไทยไม่มีในฟอนต์สไปรต์ (donor ถูกล้างด้วย `strip_ui_sprite_slots.py`) เลย fallback ไปฟอนต์ปกติ —
กลไกเดียวกับหัวข้อเมนูโดรน (`patch_drone_menu_titles.py` · ยืนยันบนจอ 5 ก.ย.): ไม่จัดกลางกล่อง แต่วางลงล่าง

โมเดลที่ fit กับสองภาพข้างบน (หน่วย UI อ้างอิง 1600x900 · จอ 1080p = x1.2 · ยืนยันจากปุ่ม retire_button
ที่ pos (800, 400) ไปอยู่ที่ y 1020 บนจอ):
* ขนาดฟอนต์ตั้งต้นตอน col47 = 0 ≈ 18.5 (ทั้งสองภาพให้ค่าเดียวกัน)
* ขอบบนเซลล์ atlas = pos.y + pivot.y + 0.78 x ขนาดฟอนต์ (หน่วย local ของ element ก่อนคูณสเกล)
* กลางพยัญชนะไทย = ขอบบนเซลล์ + 32.5/36 x ขนาดฟอนต์ (เส้นฐาน 44 · พยัญชนะสูง ~23 px ของ atlas)
→ จัดกลางแถบเมื่อ pos.y = -(pivot.y + 1.68 x ขนาดฟอนต์)

## วิธีแก้ (แก้ระดับไบต์ในที่ — ห้ามผ่าน reARMP)

ต่อ element: col11 (pos.y) += Y_SHIFT (คงระยะเงาเดิม เช่น text1 ที่ (3, 3)) · col47 0 → ขนาดฟอนต์ ·
col81 (ช่องไฟ) → 0 เพราะช่องไฟดันมาร์ก (สระบน/วรรณยุกต์ advance 0) ให้เยื้องขวาออกจากพยัญชนะ
text1/text2/text3 = เงา / ตัวหลัก / ชั้นเรืองแสง (ชั้นหลังอยู่ใต้ parent สเกล 1.5) ใช้ค่า local เดียวกันจึงซ้อนตรงกัน
⏳ "รอบที่สอง" รอเจ้าของดูบนจอ · อีกสองป้ายคำนวณจากโมเดลเดียวกัน

ใช้:
  python scripts/patch_drone_lap_banner.py            # ตรวจ/รายงานอย่างเดียว
  python scripts/patch_drone_lap_banner.py --write    # เขียน build/ui/ui.judge.en/en/scene/drone_play.bin
อ่าน extracted/ui_en/en/scene/drone_play.bin (ไม่แตะ) · deploy ด้วย deploy_spoil.py (คัดลอกทั้ง build/ui/ui.judge.en)
"""
import argparse
import io
import os
import struct
import sys

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_line_spacing import COL_FONT_SIZE, COL_KIND, KIND_TEXT, OUT_DIR, SRC_DIR, find_tables  # noqa: E402

NAME = "drone_play.bin"
SRC = SRC_DIR / NAME
OUT = OUT_DIR / NAME

COL_SCALE_X, COL_POS_X, COL_POS_Y, COL_TRACKING = 7, 10, 11, 81
COL_BOX_W, COL_BOX_H, COL_PIVOT_X, COL_PIVOT_Y = 38, 39, 41, 42
PIVOT_Y = 30.0                                     # ทุกแบนเนอร์ใช้กล่องสูง 60 pivot กลาง


def centered_y(font_size):
    return -(PIVOT_Y + 1.68 * font_size)


# ป้าย: (คำอธิบาย, {ชื่อแถว: (pos เดิม x, y)}, สเกล, กล่องกว้าง, ช่องไฟเดิม, ขนาดฟอนต์ใหม่)
# ข้อความ: ui_text.bin 685-686 (Final / Second Lap) · 704-706 (Disqualified x3) · 676-678 (Time up x3)
TARGETS = [
    ("lap_info_text (รอบที่สอง/รอบสุดท้าย)", {"second": (0.0, 0.0), "final": (0.0, 0.0)}, 0.7, 1200.0, 4, 30),
    ("retire (ถูกตัดสิทธิ์)", {"text1": (3.0, 3.0), "text2": (0.0, 0.0), "text3": (0.0, 0.0)}, 1.2, 600.0, 6, 36),
    ("count_down_time_limit (หมดเวลา)", {"text1": (3.0, 3.0), "text2": (0.0, 0.0), "text3": (0.0, 0.0)},
     1.4, 600.0, 5, 36),
]
NEW_TRACKING = 0


def f32(data, offs, col, row):
    return struct.unpack_from("<f", data, offs[col] + 4 * row)[0]


def row_matches(data, offs, r, pos, scale, box_w, tracking):
    return (data[offs[COL_KIND] + r] == KIND_TEXT and data[offs[COL_FONT_SIZE] + r] == 0
            and data[offs[COL_TRACKING] + r] == tracking
            and abs(f32(data, offs, COL_SCALE_X, r) - scale) < 1e-6
            and (f32(data, offs, COL_POS_X, r), f32(data, offs, COL_POS_Y, r)) == pos
            and f32(data, offs, COL_BOX_W, r) == box_w and f32(data, offs, COL_BOX_H, r) == 60.0
            and f32(data, offs, COL_PIVOT_X, r) == box_w / 2 and f32(data, offs, COL_PIVOT_Y, r) == PIVOT_Y)


def main():
    ap = argparse.ArgumentParser(description="ยกป้ายแบนเนอร์แข่งโดรนเข้าแถบ")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    assert SRC.exists(), "ยังไม่ได้แตก ui.judge.en.par → tools/ParTool.exe extract <par> extracted/ui_en"

    orig = io.open(SRC, "rb").read()
    tables = find_tables(orig)
    data = bytearray(orig)                            # สร้างจากต้นฉบับทุกครั้ง — ไม่มีสคริปต์อื่นแตะไฟล์นี้
    touched = set()
    for label, rows, scale, box_w, tracking, font in TARGETS:
        hits = []
        for hdr, _n, offs, names in tables:
            idx = {nm: r for r, nm in enumerate(names) if nm in rows}
            if len(idx) == len(rows) and all(row_matches(orig, offs, idx[nm], rows[nm], scale, box_w, tracking)
                                              for nm in rows):
                hits.append((hdr, offs, idx))
        if len(hits) != 1:
            sys.exit("!! %s: เจอตาราง %d ชุด (ต้องการ 1) — โครงไฟล์อาจเปลี่ยน ห้ามเขียน" % (label, len(hits)))
        hdr, offs, idx = hits[0]
        shift = centered_y(font)
        for nm, r in sorted(idx.items(), key=lambda kv: kv[1]):
            y_off, sz_off, tr_off = offs[COL_POS_Y] + 4 * r, offs[COL_FONT_SIZE] + r, offs[COL_TRACKING] + r
            y = rows[nm][1] + shift
            struct.pack_into("<f", data, y_off, y)
            data[sz_off] = font
            data[tr_off] = NEW_TRACKING
            touched.update(range(y_off, y_off + 4))
            touched.update((sz_off, tr_off))
            print("  @%06x %-36s %-6s pos.y %g → %.1f · ฟอนต์ 0 → %d · ช่องไฟ +%d → %d"
                  % (hdr, label, nm, rows[nm][1], y, font, tracking, NEW_TRACKING))

    diff = {i for i, (x, y) in enumerate(zip(orig, data)) if x != y}
    assert len(orig) == len(data) and diff <= touched, "มีไบต์นอกช่องที่ตั้งใจแก้เปลี่ยน"
    print("ไบต์ที่เปลี่ยน %d" % len(diff))

    if not a.write:
        print("(ยังไม่เขียนไฟล์ — ใส่ --write เพื่อเขียนจริง)")
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    io.open(OUT, "wb").write(bytes(data))
    print("เขียน", OUT)


if __name__ == "__main__":
    main()
