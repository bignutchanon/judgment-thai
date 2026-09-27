#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ปิดการบีบช่องไฟ (tracking ติดลบ) ของป้ายข้อความ UI ที่แสดงภาษาไทย

## อาการ (ภาพเจ้าของ 28 ก.ย. 2026 — หน้า CASE FILE)

แท็บ "ภารกิจ / คดีหลัก / คดีเสริม" ตัวอักษรเบียดซ้อนกัน ขณะที่ข้อความยาวในจอเดียวกันปกติ
วัดจากภาพ: "คดีหลัก" กว้าง 51 px แต่ตามตาราง advance ควรกว้าง 66 px (ฟอนต์ 22) — ไม่ใช่การบีบให้พอดีกล่อง
(กล่องแท็บกว้าง 220 และ EN "Main Case" ยาวกว่าไทย) และกลิฟพยัญชนะเหมือน v1.1.4 ทุกพิกเซล = เป็นมาตั้งแต่แรก

## สาเหตุ

ตาราง scene ของ UI (ตารางย่อย 121 คอลัมน์ · ดู `patch_line_spacing.py`) **col81 (1 ไบต์ มีเครื่องหมาย) =
ช่องไฟระหว่างตัวอักษร** หน่วยเดียวกับขนาดฟอนต์: 254 = -2 · 255 = -1 · ส่วนใหญ่ 0
แท็บ CASE FILE (`pause_todo_judge.bin` / `text` ฟอนต์ 22 กล่อง 220x30) = 254 → หัก 2 px **ทุกตัวอักษร**
ภาษาไทยของเรามีตัวอักษรต่อคำมากกว่าอังกฤษ (สระ/วรรณยุกต์เป็นตัวแยก advance 0 + เซลล์ตัวนำ U+0165)
คดีหลัก = 8 ตัว → หัก ~14-16 px → 66 - 15 ≈ 51 px ตรงกับที่วัดได้ · มาร์กก็ถูกดึงซ้ายไปด้วย เลยซ้อนฐาน

## วิธีแก้

ตั้ง col81 = 0 เฉพาะ element ข้อความที่ค่าติดลบ (250-255) · ข้าม element ที่เป็นตัวเลขล้วน (ชื่อมี num / time /
timer / nom) และ element ฟอนต์ภาพ (ขนาดฟอนต์ 0) เพราะไม่ได้แสดงไทย · แก้ระดับไบต์ในที่ ไบต์อื่นเท่าต้นฉบับ
ถ้าไฟล์นั้นมีใน build/ui อยู่แล้ว (สคริปต์อื่นแก้ไว้ เช่น pause_drone) จะแก้ต่อจากไฟล์นั้น ไม่ทับของเดิม

ใช้:
  python scripts/patch_ui_tracking.py            # รายงานอย่างเดียว
  python scripts/patch_ui_tracking.py --write    # เขียน build/ui/ui.judge.en/en/scene/<ไฟล์>
ต้องรันหลัง strip_ui_sprite_slots / patch_drone_menu_titles / patch_line_spacing (ลำดับในสายบิลด์)
"""
import argparse
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_line_spacing import COL_FONT_SIZE, COL_KIND, KIND_TEXT, OUT_DIR, SRC_DIR, find_tables  # noqa: E402

COL_TRACKING = 81
SKIP_NAME_PARTS = ("num", "time", "nom")          # ตัวเลขล้วน — คงช่องไฟเดิมของเกม
# มินิเกมตีเบสบอล: element `text` ช่องไฟ -5 ใช้แสดงคะแนน/สถิติเป็นตัวเลข (ไม่ใช่ป้ายไทย) — คงค่าเดิม
SKIP_FILES = {"baseball_parts_judge.bin", "batting_batting_judge.bin"}


def tracking_rows(data):
    """element ข้อความที่ col81 ติดลบ -> [(ชื่อ, ขนาดฟอนต์, ค่า col81 แบบมีเครื่องหมาย, offset)]"""
    out = []
    for _hdr, rows, offs, names in find_tables(data):
        if not offs[COL_TRACKING] or not offs[COL_KIND]:
            continue
        for r in range(rows):
            if data[offs[COL_KIND] + r] != KIND_TEXT:
                continue
            off = offs[COL_TRACKING] + r
            v = data[off]
            if v >= 250:
                out.append((names[r], data[offs[COL_FONT_SIZE] + r] if offs[COL_FONT_SIZE] else 0,
                            v - 256, off))
    return out


def main():
    ap = argparse.ArgumentParser(description="ปิด tracking ติดลบของป้ายข้อความไทย")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    assert SRC_DIR.exists(), "ยังไม่ได้แตก ui.judge.en.par → tools/ParTool.exe extract <par> extracted/ui_en"

    n_files = n_rows = 0
    for src in sorted(SRC_DIR.glob("*.bin")):
        if src.name in SKIP_FILES:
            continue
        orig = io.open(src, "rb").read()
        rows = tracking_rows(orig)
        todo = [(n, fs, v, off) for n, fs, v, off in rows
                if fs and not any(p in n.lower() for p in SKIP_NAME_PARTS)]
        if not todo:
            continue
        built = OUT_DIR / src.name
        base = io.open(built, "rb").read() if built.exists() else orig
        assert len(base) == len(orig), "%s ใน build ขนาดไม่เท่าต้นฉบับ" % src.name
        data = bytearray(base)
        for n, fs, v, off in todo:
            assert data[off] in (orig[off], 0), "%s/%s col81 ใน build ถูกแก้เป็นค่าอื่น" % (src.name, n)
            data[off] = 0
            print("  %-34s %-22s ฟอนต์ %2d  ช่องไฟ %+d → 0" % (src.name, n, fs, v))
        diff = {i for i, (x, y) in enumerate(zip(base, data)) if x != y}
        assert diff <= {off for *_x, off in todo}, "มีไบต์นอกช่องที่ตั้งใจแก้เปลี่ยน"
        n_files += 1
        n_rows += len(todo)
        if a.write:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            io.open(built, "wb").write(bytes(data))
    print("รวม %d element ใน %d ไฟล์%s" % (n_rows, n_files, "" if a.write else " (ยังไม่เขียน — ใส่ --write)"))


if __name__ == "__main__":
    main()
