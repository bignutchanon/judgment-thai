#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เพิ่มระยะห่างบรรทัดของข้อความเนื้อเรื่อง (ซับคัตซีน + กล่องบทสนทนา) ให้ไทยสองบรรทัดไม่ทับกัน

## อาการ (เจ้าของแจ้ง 27 ก.ย. 2026)

ข้อความที่ขึ้นสองบรรทัด สระล่างของบรรทัดบนชนสระบน/วรรณยุกต์ของบรรทัดล่าง
เช่น "อยู่" อยู่เหนือ "นั้น" พอดี → ู ทับ ั้ อ่านยาก

## สาเหตุ

ความสูงของอักษรไทยใน atlas (`inject_thai_title.py`) เทียบกับเส้นฐาน:
* อังกฤษ: ตัวใหญ่ -25 · หางล่าง (g y p) +6 → กินที่ 32 px (ตัวมีหมวก À É สูงสุด -33)
* ไทย   : วรรณยุกต์ซ้อนเหนือสระบน -44 · สระล่าง ุ ู +11 → กินที่ 55 px
ระยะบรรทัดของเกมตั้งไว้สำหรับอังกฤษ — ซับคัตซีน (`telop.bin` ฟอนต์ 36) ห่างกันราว 44 px ของ atlas
(จำลองด้วยค่านี้แล้วได้ภาพชนแบบเดียวกับที่เจ้าของเห็น: ู ของบรรทัดบนตกลงไปทับ ั้ ของบรรทัดล่าง)

## คอลัมน์ที่แก้ (⏳ สมมติฐาน — ต้องให้เจ้าของดูจอยืนยัน)

ตาราง scene ของ UI (`ui.judge.en.par/en/scene/*.bin`) — ตารางย่อย 121 คอลัมน์ หนึ่งแถวต่อหนึ่ง element:
* col2  (1 ไบต์) = ชนิด element · 3 = ข้อความ
* col47 (1 ไบต์) = ขนาดฟอนต์ (ยืนยันแล้วจากเมนูโดรนรอบ 17)
* col82 (type 5) = 16 บนป้ายบรรทัดเดียว · 46-54 บนกล่องหลายบรรทัด (ความหมายยังไม่รู้ · สคริปต์นี้ไม่อ่าน)
* **col84 (1 ไบต์) = 8** บนข้อความเนื้อเรื่อง (`telop` text/text_talk/text_memories ·
  `message_window_judge` text_talk/text_message) และ template ข้อความบางตัว (เมนูไตเติล · ตัวเลือก ·
  popup · snack_telop) · กล่องข้อความหลายบรรทัดอื่น (dialog/tutorial) เป็น 0 — ดูทั้งหมดด้วย `--scan`
  → น่าจะเป็น "ระยะห่างบรรทัดเพิ่ม" (หน่วยเดียวกับขนาดฟอนต์) · เมนูไตเติลที่ col84 = 8 ไม่มีขอบหนา
    ในภาพจริง (`shots/zoom_menu.png`) จึงไม่น่าใช่ความหนาขอบตัวอักษร
  สคริปต์นี้ **บวกเพิ่ม** ให้ระยะบรรทัดกว้างขึ้นตาม TARGETS (px ของ atlas · สเกล atlas = ขนาดฟอนต์ / 36
  · ครึ่ง em = 18 px ตาม `font_metrics.K`) — ใช้ส่วนต่าง จึงไม่ต้องรู้ว่าเอนจิ้นคิดระยะฐานยังไง
  ถ้าผิดจะเห็นทันทีบนจอ — ถอนได้ด้วย `deploy_spoil.py --restore`

แก้ระดับไบต์ในที่ (ห้ามผ่าน reARMP — กติกาเหล็กข้อ 12) · ไบต์อื่นต้องเหมือนต้นฉบับทุกไบต์

ใช้:
  python scripts/patch_line_spacing.py --scan     # ไล่ทุก scene: ข้อความหลายบรรทัด + ค่า col84
  python scripts/patch_line_spacing.py            # ตรวจ/รายงานอย่างเดียว
  python scripts/patch_line_spacing.py --write    # เขียน build/ui/ui.judge.en/en/scene/<ไฟล์>
อ่าน extracted/ui_en/en/scene/ (ไม่แตะ) · deploy ด้วย deploy_spoil.py (คัดลอกทั้ง build/ui/ui.judge.en)
"""
import argparse
import io
import os
import struct
import sys

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths                                        # noqa: E402

SRC_DIR = paths.EXTRACTED / "ui_en" / "en" / "scene"
OUT_DIR = paths.BUILD / "ui" / "ui.judge.en" / "en" / "scene"

N_COLS = 121
COL_KIND, COL_FONT_SIZE, COL_LINE_GAP = 2, 47, 84
KIND_TEXT = 3
ATLAS_EM = 36.0              # font_metrics: ครึ่ง em = 18 px ของ atlas

# ระยะบรรทัดที่เพิ่ม (px ของ atlas) · ไทยกินที่ -43..+11 รอบเส้นฐาน อังกฤษ -25..+6
# 27 ก.ย. +12 ทั้งหมด → 28 ก.ย. เจ้าของดูในเกม (เปิดเกม 00:36 หลัง deploy 23:40) ยังซ้อน อ่านยาก
# → ข้อความเนื้อเรื่อง +24 · กล่องหลายบรรทัดอื่น (popup/ทิป/สอนเล่น — เดิมไม่ได้แตะ) +12
STORY_ADD = 24.0
BOX_ADD = 12.0

# ไฟล์ -> [(ชื่อ element, ขนาดฟอนต์ที่ต้องตรง หรือ None, col84 เดิมที่ต้องเจอ, px atlas ที่เพิ่ม)]
# ชื่อซ้ำในไฟล์เดียว (tutorial มี text 3 แถว) จึงต้องระบุขนาดฟอนต์ด้วย · ทุกรายการต้องเจออย่างน้อย 1 แถว
TARGETS = {
    "telop.bin": [("text", 36, 8, STORY_ADD), ("text_talk", 36, 8, STORY_ADD),
                  ("text_memories", 36, 8, STORY_ADD)],
    "message_window_judge.bin": [("text_talk", 30, 8, STORY_ADD), ("text_message", 30, 8, STORY_ADD)],
    "snack_telop.bin": [("text1", 30, 8, BOX_ADD)],
    "question_text.bin": [("text", 28, 8, BOX_ADD)],
    "popup_window_judge.bin": [("message_text", 20, 8, BOX_ADD)],
    "popup_window_new_judge.bin": [("message_text", 20, 8, BOX_ADD)],
    "common_dialog_message_judge.bin": [("text", 22, 0, BOX_ADD)],
    "common_dialog_message_large_judge.bin": [("text", 22, 0, BOX_ADD)],
    "common_window_dialog_judge.bin": [("text1", 22, 0, BOX_ADD)],
    "common_dialog_tutorial_judge.bin": [("text_detail", 20, 0, BOX_ADD)],
    "info_dialog_judge.bin": [("text", 22, 0, BOX_ADD)],
    "tips_judge.bin": [("text", 22, 0, BOX_ADD)],
    "tutorial_judge.bin": [("text", 24, 0, BOX_ADD)],
}


def i32(data, off):
    return struct.unpack_from("<i", data, off)[0]


def cstr(data, off):
    end = data.index(b"\0", off)
    return data[off:end].decode("utf-8", "replace")


def find_tables(data):
    """[(header_offset, row_count, col_offsets, row_names)] ของตารางย่อย 121 คอลัมน์แบบ column-major"""
    out = []
    pat = struct.pack("<i", N_COLS)
    i = -1
    n = len(data)
    while True:
        i = data.find(pat, i + 1)
        if i < 0:
            break
        hdr = i - 4
        if hdr < 0 or hdr % 4:
            continue
        rows = i32(data, hdr)
        if not 0 < rows < 4096:
            continue
        p_names, p_content = i32(data, hdr + 0x10), i32(data, hdr + 0x1C)
        if not (0 < p_names < n and 0 < p_content + 4 * N_COLS <= n) or data[hdr + 0x23] != 0:
            continue
        offs = struct.unpack_from("<%di" % N_COLS, data, p_content)
        if any(not (0 <= o < n) for o in (offs[COL_KIND], offs[COL_FONT_SIZE], offs[COL_LINE_GAP])):
            continue
        try:
            names = [cstr(data, i32(data, p_names + 4 * r)) for r in range(rows)]
        except (ValueError, struct.error):
            continue
        out.append((hdr, rows, offs, names))
    return out


def text_rows(data):
    """ทุกแถวที่เป็น element ข้อความ -> (ชื่อ, ขนาดฟอนต์, col84, offset ของไบต์ col84)"""
    for hdr, rows, offs, names in find_tables(data):
        for r in range(rows):
            if offs[COL_KIND] == 0 or data[offs[COL_KIND] + r] != KIND_TEXT:
                continue
            gap_off = offs[COL_LINE_GAP] + r if offs[COL_LINE_GAP] else None
            yield (names[r], data[offs[COL_FONT_SIZE] + r] if offs[COL_FONT_SIZE] else 0,
                   data[gap_off] if gap_off is not None else 0, gap_off)


def new_gap(font_size, old, add_px):
    """col84 ใหม่ = เดิม + add_px (px ของ atlas) แปลงเป็นหน่วย UI ของ element นี้"""
    return old + int(round(add_px * font_size / ATLAS_EM))


def scan():
    print("element ข้อความที่ col84 ≠ 0 ในทุก scene:")
    for p in sorted(SRC_DIR.glob("*.bin")):
        data = io.open(p, "rb").read()
        for name, fs, gap, _off in text_rows(data):
            if gap:
                print("  %-44s %-24s ฟอนต์ %2d  col84 %d" % (p.name, name, fs, gap))


def main():
    ap = argparse.ArgumentParser(description="เพิ่มระยะห่างบรรทัดของข้อความเนื้อเรื่อง")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--scan", action="store_true")
    a = ap.parse_args()
    assert SRC_DIR.exists(), "ยังไม่ได้แตก ui.judge.en.par → tools/ParTool.exe extract <par> extracted/ui_en"
    if a.scan:
        scan()
        return

    for fname, want in TARGETS.items():
        src = SRC_DIR / fname
        orig = io.open(src, "rb").read()
        data = bytearray(orig)
        rows = list(text_rows(orig))
        touched = set()
        for name, want_fs, want_gap, add_px in want:
            hits = [(fs, gap, off) for n, fs, gap, off in rows
                    if n == name and (want_fs is None or fs == want_fs)]
            if not hits:
                sys.exit("!! %s ไม่เจอ element %s (ฟอนต์ %s) — ห้ามเขียน" % (fname, name, want_fs))
            for fs, gap, off in hits:
                if gap != want_gap or off is None:
                    sys.exit("!! %s/%s col84 = %d (คาด %d) — โครงไฟล์ไม่ตรง ห้ามเขียน"
                             % (fname, name, gap, want_gap))
                g = new_gap(fs, gap, add_px)
                assert 0 <= g <= 255
                data[off] = g
                touched.add(off)
                print("  %-38s %-14s ฟอนต์ %2d  col84 %d → %d  (ระยะบรรทัด +%.1f px atlas)"
                      % (fname, name, fs, gap, g, (g - gap) * ATLAS_EM / fs))

        diff = {i for i, (x, y) in enumerate(zip(orig, data)) if x != y}
        assert len(orig) == len(data) and diff <= touched, "มีไบต์นอกช่องที่ตั้งใจแก้เปลี่ยน"
        if a.write:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            io.open(OUT_DIR / fname, "wb").write(bytes(data))
            print("  เขียน %s (ไบต์ที่เปลี่ยน %d)" % (OUT_DIR / fname, len(diff)))
    if not a.write:
        print("(ยังไม่เขียนไฟล์ — ใส่ --write เพื่อเขียนจริง)")


if __name__ == "__main__":
    main()
