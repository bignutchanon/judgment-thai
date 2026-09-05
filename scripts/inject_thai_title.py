#!/usr/bin/env python3
"""ฝัง glyph ไทย (Sarabun) ลง **ฟอนต์หน้าไตเติล/เมนู** `meta_ot_cond_book.dds` ของ Judgment

ต่างจาก `inject_thai_judge.py` (ฟอนต์ข้อความหลัก `tbgm_0p_ja` ฟอร์แมต `FONT!`) โดยสิ้นเชิง:
ฟอนต์ไตเติลไม่มีไฟล์ metrics เลย เป็น bitmap grid ล้วน — เขียนกลิฟลงเซลล์ที่ตรงกับ
codepoint แล้วจบ ไม่มี record ให้แก้ ไม่มี UV ไม่มี advance ในไฟล์
(ตาราง width อยู่ใน exe — ดู docs/research_web/jp_th_community_sweep.md)

โหมด:
  (ไม่มี flag)  ชุดรอบ 3 จาก `title_slotmap.CELL_ASSIGN` — ทดสอบว่าเซลล์มีหมึก/เซลล์ว่าง
                ใช้ได้ไหม (ผลแล้ว: ได้ทั้งคู่)
  --probe       ชุดรอบ 4 จาก `title_probe.CELLS` — วัดตาราง width ของ exe ผ่านการเลือก donor
                และเทียบ per-char กับ pre-composed cluster
  --slotmap     **โหมดผลิตจริง** — วาดทุกเซลล์ตาม `translations/slotmap.json`
                (แผนเดียวที่ฝั่งข้อความ `build_text.py` ใช้ encode ด้วย · ห้ามมีสำเนาที่สอง)

ใช้:  python scripts/inject_thai_title.py [--slotmap | --probe | --map <module>]
อ่าน  extracted/font/meta_ot_cond_book.dds (ต้นฉบับ — ไม่แตะ · อ่านใหม่ทุกครั้ง เซลล์ของรอบ
      ก่อนหน้าจึงกลับเป็นของเดิมอัตโนมัติ ไม่มีการสะสมทับ)
เขียน build/font/meta_ot_cond_book.dds + build/font/preview_title.png
"""
import io
import os
import struct
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from bc4_codec import decode_bc4, encode_bc4, encode_bc4_blocks
from title_encode import ppem, render_at
from title_slotmap import ATLAS_H, ATLAS_W, BASELINE_Y, CELL_H, CELL_W, INK_X0, cell_xy

SRC_DDS = paths.EXTRACTED / "font" / "meta_ot_cond_book.dds"
OUT_DDS = paths.BUILD / "font" / "meta_ot_cond_book.dds"
PREVIEW = paths.BUILD / "font" / "preview_title.png"

DDS_HEADER = 128               # BC4U legacy header (ไม่มี DX10 extension)

UPPER_MARKS = set("ัิีึื็ํ")    # สระบน/ไม้ไต่คู้
TONE_MARKS = set("่้๊๋์")       # วรรณยุกต์/การันต์
LOWER_MARKS = set("ฺุู")        # สระล่าง

def kind_of(ch):
    if ch in TONE_MARKS:
        return "tone"
    if ch in UPPER_MARKS:
        return "upper"
    if ch in LOWER_MARKS:
        return "lower"
    return "base"


def draw_cell(spec):
    """วาดกลิฟหนึ่งตัวลงเซลล์ตาม spec จาก slotmap (หนึ่งตัวอักษรหนึ่งเซลล์ ตั้งแต่รอบ 16)

    spec ระบุตำแหน่งวาดมาครบแล้ว — allocator เป็นคนคำนวณ เพราะมันต้องรู้ค่าเดียวกันนี้
    ตอนคำนวณ (L, R) ของ `kerning_table` ด้วย (ห้ามคำนวณซ้ำสองที่ เดี๋ยวหลุดจากกัน)
      * ฐาน  : วางตามเส้นฐานจริงของฟอนต์ ที่ x = ink_x0
      * มาร์ก: วางที่ (ink_x0, ink_y0) ตรง ๆ — การเลื่อนไปทับฐานทำด้วยค่า L ในตาราง ไม่ใช่ที่นี่
    """
    canvas = np.zeros((CELL_H, CELL_W), dtype=np.uint8)
    text = spec["text"] if isinstance(spec, dict) else spec
    if not text:                       # เซลล์ตัวนำ (sentinel) — ต้องว่างเปล่าโดยตั้งใจ
        return canvas
    img, _dx, top, _bot = render_at(text[0], ppem())
    h, w = img.shape
    if isinstance(spec, dict):
        x = spec.get("ink_x0", INK_X0)
        y = BASELINE_Y + top if spec["kind"] == "base" else spec["ink_y0"]
    else:
        x, y = INK_X0, BASELINE_Y + top
    y = max(0, min(CELL_H - 1, int(y)))
    w = min(w, CELL_W - x)
    h = min(h, CELL_H - y)
    if w > 0 and h > 0:
        np.maximum(canvas[y:y + h, x:x + w], img[:h, :w], out=canvas[y:y + h, x:x + w])
    return canvas


def load_slotmap_cells():
    """ผัง cp -> spec จาก translations/slotmap.json (map เดียวกับที่ฝั่งข้อความใช้ encode)"""
    from slot_alloc import SlotMap
    sm = SlotMap.load()
    return {cp: spec for cp, spec in sm.glyph_plan()}


def load_map(mod_name):
    """โหลดผัง cp -> (สิ่งที่วาด, ป้ายกำกับ) จากโมดูลที่ระบุ
    - title_slotmap : ชุดรอบ 3 (CELL_ASSIGN, ค่าเป็น (ตัวอักษร, กลุ่ม))
    - title_probe*  : ชุด probe (CELLS, ค่าเป็น (สิ่งที่วาด, ป้ายกำกับ))"""
    mod = __import__(mod_name)
    if hasattr(mod, "CELLS"):
        return dict(mod.CELLS)
    return {cp: (ch, f"กลุ่ม {group}") for cp, (ch, group) in mod.CELL_ASSIGN.items()}


def main():
    mod_name = "title_slotmap"
    if "--probe" in sys.argv:
        mod_name = "title_probe"
    if "--map" in sys.argv:
        mod_name = sys.argv[sys.argv.index("--map") + 1]
    if "--slotmap" in sys.argv:
        mod_name = "slotmap.json"
        cell_map = load_slotmap_cells()
    else:
        cell_map = load_map(mod_name)
    assert SRC_DDS.exists(), f"ไม่พบต้นฉบับ {SRC_DDS} — คัดลอกจาก {paths.FONT_GAME_DIR} ก่อน"
    OUT_DDS.parent.mkdir(parents=True, exist_ok=True)

    raw = SRC_DDS.read_bytes()
    header, payload = bytearray(raw[:DDS_HEADER]), raw[DDS_HEADER:]
    atlas = decode_bc4(payload, ATLAS_W, ATLAS_H).copy()

    # ---- ขยาย atlas ถ้าเซลล์ที่ขอไปเกินขอบล่างของภาพเดิม ----
    need_rows = max(cell_xy(cp)[1] for cp in cell_map) // CELL_H + 1
    need_h = need_rows * CELL_H
    if need_h > ATLAS_H:
        pad = np.zeros((need_h - ATLAS_H, ATLAS_W), dtype=atlas.dtype)
        atlas = np.vstack([atlas, pad])
        payload = payload + encode_bc4(np.zeros((need_h - ATLAS_H, ATLAS_W), dtype=np.uint8))
        struct.pack_into("<I", header, 12, need_h)                      # dwHeight
        struct.pack_into("<I", header, 20, (ATLAS_W // 4) * (need_h // 4) * 8)  # linear size
        print(f"ขยาย atlas: {ATLAS_H} -> {need_h} px ({need_rows} แถว = cp ถึง "
              f"U+{need_rows * 16 + 0x20 - 1:04X})")
    atlas_h = atlas.shape[0]

    changed_blocks = set()
    for cp, entry in sorted(cell_map.items()):
        spec = entry if isinstance(entry, dict) else entry[0]
        x0, y0 = cell_xy(cp)
        atlas[y0:y0 + CELL_H, x0:x0 + CELL_W] = draw_cell(spec)            # ล้าง + วาดใหม่
        for by in range(y0 // 4, (y0 + CELL_H) // 4):
            for bx in range(x0 // 4, (x0 + CELL_W) // 4):
                changed_blocks.add((by, bx))

    new_payload = encode_bc4_blocks(payload, ATLAS_W, atlas, changed_blocks)
    assert len(new_payload) == len(payload), "ขนาด payload เปลี่ยน — ผิดแน่"
    OUT_DDS.write_bytes(bytes(header) + new_payload)

    # ตรวจกลับ: เซลล์ที่แก้ต้องมีหมึก (ยกเว้นเซลล์ตัวนำที่ต้องว่าง) · เซลล์อื่น bit-identical
    check = decode_bc4(OUT_DDS.read_bytes()[DDS_HEADER:], ATLAS_W, atlas_h)
    for cp, entry in cell_map.items():
        want_ink = (entry["text"] if isinstance(entry, dict) else entry[0]) != ""
        x0, y0 = cell_xy(cp)
        has_ink = (check[y0:y0 + CELL_H, x0:x0 + CELL_W] > 16).sum() > 0
        assert has_ink == want_ink, (
            f"เซลล์ U+{cp:04X} " + ("ว่างหลัง encode" if want_ink
                                    else "มีหมึกทั้งที่ต้องเป็นเซลล์ว่าง"))
    untouched = np.ones((atlas_h, ATLAS_W), dtype=bool)
    for cp in cell_map:
        x0, y0 = cell_xy(cp)
        untouched[y0:y0 + CELL_H, x0:x0 + CELL_W] = False
    orig = decode_bc4(payload, ATLAS_W, atlas_h)
    assert np.array_equal(orig[untouched], check[untouched]), "เซลล์ที่ไม่ได้แก้เปลี่ยนไป"

    print(f"เขียน {OUT_DDS} ({OUT_DDS.stat().st_size} B) · ผัง {mod_name} · "
          f"แก้ {len(cell_map)} เซลล์ ({len(changed_blocks)} BC4 block)")
    by_tag = {}
    for cp, entry in sorted(cell_map.items()):
        tag = entry["kind"] if isinstance(entry, dict) else entry[1]
        text = entry["text"] if isinstance(entry, dict) else entry[0]
        by_tag.setdefault(tag, []).append(f"{text}=U+{cp:04X}")
    for tag, items in by_tag.items():
        print(f"  {tag}: " + " ".join(items))

    # preview: ตัดเฉพาะแถวที่แตะ มาต่อกันให้ตรวจด้วยตา
    touched_rows = sorted({cell_xy(cp)[1] // CELL_H for cp in cell_map})
    prev = Image.new("L", (ATLAS_W, CELL_H * len(touched_rows)), 0)
    for i, r in enumerate(touched_rows):
        prev.paste(Image.fromarray(check[r * CELL_H:(r + 1) * CELL_H, :]), (0, i * CELL_H))
    prev.resize((ATLAS_W * 2, CELL_H * len(touched_rows) * 2), Image.NEAREST).save(PREVIEW)
    print(f"เขียน {PREVIEW} (แถว {touched_rows})")


if __name__ == "__main__":
    main()
