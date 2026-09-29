#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ยกป้ายไทยของโป๊กเกอร์ (ชิป / เดิมพัน / คอล / เรส / โฟลด์ / โครงสร้าง / ยก) กลับเข้ากรอบ

## อาการ (ภาพเจ้าของ 29 ก.ย. 2026 · 1080p)

ป้ายไทยทุกตัวบนโต๊ะโป๊กเกอร์ตกลงไปใต้กรอบของมัน:
* แผงผู้เล่น: "ชิป" / "เดิมพัน" / "เดิมพันรวม" ไปนอนใต้แถบตัวเลข
* แถบแอ็กชันใต้แผง NPC (และแถบกลางจอตอนยากามิเล่น): "คอล" / "เรส" / "โฟลด์" หลุดใต้แถบ
* ปุ่มคำสั่งซ้ายล่าง: "เรส" / "คอล" / "โฟลด์" ไปอยู่ที่ขอบล่างปุ่ม
* กล่องซ้าย: "โครงสร้าง" ทับ "5 / 10" · "ยก" ทับเลข 1 2 3 4

## สาเหตุ (`ui.judge.en.par/en/scene/poker_judge.bin`)

กลไกเดียวกับแบนเนอร์แข่งโดรน (`patch_drone_lap_banner.py`): ข้อความไทยไม่ได้วาดตรงกลางกล่องแบบที่
อังกฤษวาด แต่ถูกวางต่ำลงมา · โมเดลของสคริปต์โดรน (ขอบบนเซลล์ = pos.y + pivot.y + 0.78 x ฟอนต์)
ใช้กับจอนี้ไม่ได้ (คำนวณแล้วคลาดจากภาพ 7-18 px) จึงไม่ใช้โมเดล แต่วัดระยะที่ตกจากภาพตรง ๆ แล้วเลื่อน
pos.y ขึ้นเท่านั้น — การเลื่อน pos.y คือการเลื่อนทั้ง element ในพิกัดของ parent จึงไม่ต้องรู้ว่าเอนจิ้นวาง
ข้อความยังไง (หน่วย UI อ้างอิง 1600x900 · จอ 1080p = x1.2 · ตรวจแล้วจาก slash ของกล่อง structure:
pos.y 56 → คาด y 557.5 บนจอ วัดได้ 557.5)

วัดจุดกลางแถวพยัญชนะ (ไม่นับสระบน/วรรณยุกต์) เทียบกับจุดกลางของกรอบ:
* แผงผู้เล่น (ตาราง 2 ชุด: NPC กว้าง 412 · ยากามิ 432) — กลางแถบตัวเลข 147/187 · พยัญชนะ 170/209.5
  (NPC) และ 931.5/968.5 · 952/992 (ยากามิ) → ตก ~22.4 px = 19 หน่วย
* แถบแอ็กชัน — กลางแถบ 271.5 · "คอล"/"เรส" 312 → ตก 40.5 px = 34 หน่วย
* ปุ่มคำสั่ง — กลางปุ่ม 772/848.5/925 · พยัญชนะ 808/885.5/961.5 → ตก ~36.7 px = 30.5 หน่วย
* structure / round (ฟอนต์ 24 สเกล 0.7) — จุดที่อังกฤษวาด 516/619 · พยัญชนะ 544.5/646.5 → ตก ~28 px
  = 23 หน่วย · "โครงสร้าง" ยกแค่ 22 เพราะไม้โทบน ร ชนขอบบนกล่อง

แก้ระดับไบต์ในที่ (ห้ามผ่าน reARMP — กติกาเหล็กข้อ 12) · แก้เฉพาะ col11 (pos.y) · ไบต์อื่นต้องเหมือน
ต้นฉบับทุกไบต์ · ⏳ รอเจ้าของดูบนจอ

ใช้:
  python scripts/patch_poker_labels.py            # ตรวจ/รายงานอย่างเดียว
  python scripts/patch_poker_labels.py --write    # เขียน build/ui/ui.judge.en/en/scene/poker_judge.bin
อ่าน extracted/ui_en/en/scene/poker_judge.bin (ไม่แตะ) · deploy ด้วย deploy_spoil.py (คัดลอกทั้ง build/ui/ui.judge.en)
"""
import argparse
import io
import os
import struct
import sys

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_line_spacing import COL_KIND, KIND_TEXT, OUT_DIR, SRC_DIR, find_tables  # noqa: E402

NAME = "poker_judge.bin"
SRC = SRC_DIR / NAME
OUT = OUT_DIR / NAME

COL_POS_Y = 11

# (ป้าย, {ชื่อแถว: pos.y เดิม}, ระยะที่ยกขึ้น (หน่วย UI), จำนวนตารางที่ต้องเจอ)
TARGETS = [
    ("แผงผู้เล่น ชิป/เดิมพัน/เดิมพันรวม",
     {"chip_text": -2.0, "bet_text": -2.0, "total_bet_text": 31.0}, 19.0, 2),
    ("แถบแอ็กชัน เดิมพัน/บลายด์/เช็ก/คอล/เรส/โฟลด์",
     {"bet": -6.0, "bigblind": -6.0, "littleblind": -6.0, "check": -6.0,
      "call": -6.0, "raise": -6.0, "fold": -6.0}, 34.0, 1),
    ("ปุ่มคำสั่ง (ตัวหนังสือ + เงา)",
     {"bet_text": 0.0, "bet_shadow": 1.0, "call_text": 0.0, "call_shadow": 1.0,
      "fold_text": 0.0, "fold_shadow": 1.0, "raise_text": 0.0, "raise_shadow": 1.0,
      "check_text": 0.0, "check_shadow": 1.0}, 30.5, 1),
    ("โครงสร้าง", {"structure": 21.0}, 22.0, 1),
    ("ยก", {"round": 19.0}, 23.0, 1),
]


def pos_y(data, offs, r):
    return struct.unpack_from("<f", data, offs[COL_POS_Y] + 4 * r)[0]


def main():
    ap = argparse.ArgumentParser(description="ยกป้ายไทยของโป๊กเกอร์เข้ากรอบ")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    assert SRC.exists(), "ยังไม่ได้แตก ui.judge.en.par → tools/ParTool.exe extract <par> extracted/ui_en"

    orig = io.open(SRC, "rb").read()
    tables = find_tables(orig)
    data = bytearray(orig)                            # สร้างจากต้นฉบับทุกครั้ง — ไม่มีสคริปต์อื่นแตะไฟล์นี้
    touched = set()
    for label, rows, lift, want in TARGETS:
        hits = []
        for hdr, _n, offs, names in tables:
            idx = {nm: r for r, nm in enumerate(names) if nm in rows and orig[offs[COL_KIND] + r] == KIND_TEXT}
            if len(idx) == len(rows) and all(pos_y(orig, offs, idx[nm]) == rows[nm] for nm in rows):
                hits.append((hdr, offs, idx))
        if len(hits) != want:
            sys.exit("!! %s: เจอตาราง %d ชุด (ต้องการ %d) — โครงไฟล์อาจเปลี่ยน ห้ามเขียน" % (label, len(hits), want))
        for hdr, offs, idx in hits:
            for nm, r in sorted(idx.items(), key=lambda kv: kv[1]):
                off = offs[COL_POS_Y] + 4 * r
                struct.pack_into("<f", data, off, rows[nm] - lift)
                touched.update(range(off, off + 4))
                print("  @%06x %-44s %-14s pos.y %g → %g" % (hdr, label, nm, rows[nm], rows[nm] - lift))

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
