#!/usr/bin/env python3
"""ฝัง glyph ไทย (Sarabun) ลงฟอนต์หลักของ Judgment: font.judge/en/tbgm_0p_ja.{bin,dds}

Judgment ใช้ container `FONT!` แบบ Y6 เป๊ะ (ยืนยัน 14 ส.ค. 2026: round-trip 3/3,
UV order (v0,u0,v1,u1), field0 = advance หน่วย 1/256px, cell 40x40 — Y6 คือ 39x39)

แนวทาง (ต่างจาก Y6 ที่เขียนทับ donor cell):
1. วาด glyph ไทย 83 ตัวลง **โซนว่างของ atlas** (y>=FREE_Y0 — ไม่มี glyph ใดอ้างถึง
   ยืนยันแล้ว: used extent y<=3107)
2. ชี้ record 2 ชุดไปที่ cell ใหม่ชุดเดียวกัน:
   a. donor remap: record Cyrillic/Samaritan 83 ตัว (slotmap เดียวกับ Y6) — แก้ uv+advance
   b. real-cp: **เพิ่ม record ใหม่ 83 ตัว cp = ไทยจริง (U+0E01..)** ลงช่อง zero-padding
      (declared_count 7093 -> 7176, ขนาดไฟล์เท่าเดิม) — ถ้าเกมยอมรับ = เลิกใช้ donor ได้เลย
   ผลเทสต์ในเกมภาพเดียวตอบทั้งสองแนว (ข้อความ encode donor กับข้อความไทยแท้ วางคนละบรรทัด)

ใช้:  python scripts/inject_thai_judge.py
อ่าน  extracted/font/tbgm_0p_ja.{bin,dds} (ต้นฉบับ — ไม่แตะ)
เขียน build/font/tbgm_0p_ja.{bin,dds} + build/font/preview_thai.png
"""
import io
import os
import sys
from bisect import bisect_left

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from y6_font_tool import Y6Font
from font_tool import cp_pack, cp_unpack
from bc4_codec import decode_bc4, encode_bc4_blocks
from y6_slotmap import THAI_CHARS, ENCODE, UPPER, TONE, LOWER, COMBINING

ATLAS_W = ATLAS_H = 4096
CELL = 40
BASELINE_ROW = 34          # สัดส่วนเดียวกับ Y6 (33/39 ≈ 85%) — ตรวจกับ preview ก่อนใช้จริง
FREE_Y0 = 3120             # โซนว่าง (ใช้จริงสุดที่ y=3107, ปัด align 16) — วาง cell ใหม่จากตรงนี้
FREE_COLS = ATLAS_W // CELL

RENDER_PX = 300
SS = 4
CANVAS_PX = RENDER_PX * SS
BASE_SCALE = 21.0 / 177.0  # ก สูง ~21px ใน cell 40 (Y6: 20px ใน cell 39)

TONE_BAND = (0, 7)
UPPER_BAND = (8, 18)
LOWER_BAND = (34, 40)

TTF = str(paths.SARABUN_TTF)


def render_mask(ch):
    font = ImageFont.truetype(TTF, RENDER_PX * SS)
    W, H = CANVAS_PX * 4, CANVAS_PX * 5
    ox, oy = int(CANVAS_PX * 1.5), int(CANVAS_PX * 3.2)
    im = Image.new('L', (W, H), 0)
    ImageDraw.Draw(im).text((ox, oy), ch, font=font, fill=255, anchor='ls')
    bb = im.getbbox()
    if not bb:
        return None
    l, t, r, b = bb
    mask = np.asarray(im.crop(bb), dtype=np.uint8)
    return mask, (l - ox) / SS, (oy - t) / SS, (oy - b) / SS, font.getlength(ch) / SS


def rasterize_to_box(mask, tw, th):
    return np.asarray(Image.fromarray(mask).resize((max(1, tw), max(1, th)), Image.LANCZOS),
                      dtype=np.uint8)


def paste_clip(canvas, tile, row0, col0):
    th, tw = tile.shape
    sr0, sc0 = max(0, -row0), max(0, -col0)
    dr0, dc0 = max(0, row0), max(0, col0)
    dr1, dc1 = min(CELL, row0 + th), min(CELL, col0 + tw)
    if dr1 <= dr0 or dc1 <= dc0:
        return
    sub = tile[sr0:sr0 + (dr1 - dr0), sc0:sc0 + (dc1 - dc0)]
    np.maximum(canvas[dr0:dr1, dc0:dc1], sub, out=canvas[dr0:dr1, dc0:dc1])


def build_glyph(ch):
    rendered = render_mask(ch)
    assert rendered is not None, f'Sarabun ไม่มี glyph สำหรับ {ch!r}'
    mask, x0, ytop, ybot, adv = rendered
    canvas = np.zeros((CELL, CELL), dtype=np.uint8)
    h_rp = ytop - ybot
    w_rp = mask.shape[1] / SS
    if ch in TONE or ch in UPPER or ch in LOWER:
        band = TONE_BAND if ch in TONE else UPPER_BAND if ch in UPPER else LOWER_BAND
        scale = (band[1] - band[0]) / max(h_rp, 1e-6)
        tw, th = int(round(w_rp * scale)), int(round(h_rp * scale))
        tile = rasterize_to_box(mask, tw, th)
        col0 = (CELL - tile.shape[1]) // 2
        row0 = band[0] if ch in LOWER else band[1] - tile.shape[0]
        paste_clip(canvas, tile, row0, col0)
        return canvas, 0.0
    tw, th = int(round(w_rp * BASE_SCALE)), int(round(h_rp * BASE_SCALE))
    tile = rasterize_to_box(mask, tw, th)
    paste_clip(canvas, tile, BASELINE_ROW - int(round(ytop * BASE_SCALE)),
               int(round(x0 * BASE_SCALE)))
    return canvas, adv * BASE_SCALE


def main():
    src_bin, src_dds = str(paths.FONT_SRC_BIN), str(paths.FONT_SRC_DDS)
    out_dir = paths.BUILD / 'font'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_bin, out_dds = str(out_dir / 'tbgm_0p_ja.bin'), str(out_dir / 'tbgm_0p_ja.dds')

    font = Y6Font(src_bin)
    dds = bytearray(open(src_dds, 'rb').read())
    payload = dds[128:]
    assert len(payload) == ATLAS_W * ATLAS_H // 2, 'BC4U payload size ไม่ตรง'
    atlas = decode_bc4(bytes(payload), ATLAS_W, ATLAS_H).copy()
    print(f'โหลด tbgm_0p_ja: declared={font.declared_count} capacity={font.capacity()}')

    # กันโซนว่างชนของจริง
    for cp, fl, (v0, u0, v1, u1), met in font.used_records():
        assert int(round(v1 * ATLAS_H)) <= FREE_Y0, f'มี glyph ล้ำโซนว่าง: cp={cp:#x}'

    idx_by_cp = {cp: i for i, (cp, fl, uv, met) in enumerate(font.records[:font.declared_count])}

    # ---- วาด glyph ไทยลงโซนว่าง + เตรียม uv/advance ----
    changed_blocks = set()
    glyph_info = {}          # ch -> (uv, field0, tile)
    for k, ch in enumerate(THAI_CHARS):
        tile, adv_px = build_glyph(ch)
        r, c = divmod(k, FREE_COLS)
        x0, y0 = c * CELL, FREE_Y0 + r * CELL
        x1, y1 = x0 + CELL, y0 + CELL
        assert y1 <= ATLAS_H, 'โซนว่างไม่พอ'
        atlas[y0:y1, x0:x1] = tile
        for by in range(y0 // 4, -(-y1 // 4)):
            for bx in range(x0 // 4, -(-x1 // 4)):
                changed_blocks.add((by, bx))
        uv = (y0 / ATLAS_H, x0 / ATLAS_W, y1 / ATLAS_H, x1 / ATLAS_W)   # (v0,u0,v1,u1)
        field0 = 0 if ch in COMBINING else int(round(adv_px * 256))
        glyph_info[ch] = (uv, field0, tile)

    # ---- a) donor remap (แก้ record เดิม — จำนวน record ไม่เปลี่ยน) ----
    for ch in THAI_CHARS:
        donor_packed = cp_pack(chr(ENCODE[ch]))
        i = idx_by_cp.get(donor_packed)
        assert i is not None, f'donor U+{ENCODE[ch]:04X} ไม่มีในฟอนต์'
        cp0, flag0, uv_old, met_old = font.records[i]
        uv, field0, _ = glyph_info[ch]
        font.records[i] = [cp0, flag0, uv, (field0, met_old[1], met_old[2], met_old[3])]

    # ---- b) real-cp: เพิ่ม record ใหม่ 83 ตัวลงช่อง zero-padding ----
    used = font.records[:font.declared_count]
    tail = font.records[font.declared_count:]
    assert all(cp == 0 for cp, *_ in tail), 'tail ต้องเป็น zero record ล้วน'
    assert len(tail) >= len(THAI_CHARS), 'ช่องว่างไม่พอสำหรับ real-cp'
    for ch in THAI_CHARS:
        uv, field0, _ = glyph_info[ch]
        packed = cp_pack(ch)
        donor_i = idx_by_cp[cp_pack(chr(ENCODE[ch]))]
        met_ref = font.records[donor_i][3]
        cps_sorted = [r[0] for r in used]
        j = bisect_left(cps_sorted, packed)
        assert j == len(used) or used[j][0] != packed, f'{ch!r} มีในฟอนต์อยู่แล้ว'
        used.insert(j, [packed, 0, uv, (field0, met_ref[1], met_ref[2], met_ref[3])])
    font.records = used + tail[:len(tail) - len(THAI_CHARS)]
    font.declared_count += len(THAI_CHARS)
    import struct
    struct.pack_into('<I', font.header, 0x10, font.declared_count)

    # ---- เขียนไฟล์ ----
    built = font.build()
    orig = open(src_bin, 'rb').read()
    assert len(built) == len(orig), f'ขนาด .bin ต้องเท่าเดิม: {len(built)} vs {len(orig)}'
    open(out_bin, 'wb').write(built)
    new_payload = encode_bc4_blocks(bytes(payload), ATLAS_W, atlas, changed_blocks)
    assert len(new_payload) == len(payload)
    dds[128:] = new_payload
    open(out_dds, 'wb').write(bytes(dds))
    print(f'เขียน {out_bin} + {out_dds} (บล็อก BC4 แก้ {len(changed_blocks)})')

    # ---- ตรวจกลับ ----
    f2 = Y6Font(out_bin)
    assert f2.declared_count == 7093 + 83
    cps = [r[0] for r in f2.used_records()]
    assert cps == sorted(cps), 'cp table ต้อง sort ascending'
    for ch in THAI_CHARS:
        assert cp_pack(ch) in cps, f'real-cp {ch!r} หายไป'
    print(f'ตรวจกลับ OK: declared={f2.declared_count}, sorted, real-cp ครบ 83')

    make_preview(f2, out_dds, str(out_dir / 'preview_thai.png'))


def donor_encode(s):
    """encode ไทย -> donor ตรงจาก slotmap (ไม่ใช้ระบบ cluster ของ Y6)"""
    return ''.join(chr(ENCODE[c]) if c in ENCODE else c for c in s)


def make_preview(font, dds_path, out_png):
    d = open(dds_path, 'rb').read()
    atlas = decode_bc4(d[128:], ATLAS_W, ATLAS_H)
    idx = {}
    for cp, fl, uv, met in font.used_records():
        ch = cp_unpack(cp)
        if ch:
            idx[ch] = (uv, met)

    lab = ImageFont.truetype(TTF, 18)
    samples = [
        ('real-cp ไทยแท้', 'จัดจ์เมนต์ ภาษาไทย ทดสอบฟอนต์', lambda s: s),
        ('donor encode', 'จัดจ์เมนต์ ภาษาไทย ทดสอบฟอนต์', donor_encode),
        ('real-cp', 'ยางามิ ทนายผันตัวเป็นนักสืบ', lambda s: s),
        ('real-cp', 'เริ่มเกมใหม่ เล่นต่อ ตั้งค่า ออกจากเกม', lambda s: s),
    ]
    img = Image.new('L', (1400, 120 * len(samples) + 20), 20)
    dr = ImageDraw.Draw(img)
    y = 10
    for label, text, enc_fn in samples:
        enc = enc_fn(text)
        pen = 0.0
        line = np.zeros((CELL + 12, 1360), dtype=np.uint8)
        for c in enc:
            if c == ' ':
                pen += 10
                continue
            rec = idx.get(c)
            if rec is None:
                pen += 10
                continue
            (v0, u0, v1, u1), met = rec
            x0, y0 = int(round(u0 * ATLAS_W)), int(round(v0 * ATLAS_H))
            tile = atlas[y0:y0 + CELL, x0:x0 + CELL]
            px = int(round(pen))
            if px + CELL <= line.shape[1]:
                np.maximum(line[:CELL, px:px + CELL], tile, out=line[:CELL, px:px + CELL])
            pen += met[0] / 256.0
        li = Image.fromarray(line).resize((line.shape[1] * 2, line.shape[0] * 2), Image.LANCZOS)
        li = li.crop((0, 0, 1380, li.height))
        dr.text((10, y), f'{label}: {text}', font=lab, fill=180)
        img.paste(li.resize((1380, li.height // 2)), (10, y + 24))
        y += 120
    img.save(out_png)
    print(f'เขียน {out_png}')


if __name__ == '__main__':
    main()
