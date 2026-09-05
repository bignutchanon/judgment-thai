#!/usr/bin/env python3
"""ฝัง glyph ไทย (Sarabun) ลงฟอนต์ SDF หลักของ K3: system_main_en_all_sdf.bin + .dds
port จาก K2R (D:\\Projects\\yakuza-kiwami-2-mod) 14 ส.ค. 2026 — ใช้ได้เพราะวัดแล้ว
(scripts/measure_sdf_params.py) ว่า atlas K3 มีพารามิเตอร์เท่า K2R ทุกตัว
(em_per_px/slope/pad/format) ต่างแค่จำนวน glyph 366 vs 362
แนวทาง = glyph-remapping ทับ donor slot Cyrillic (เหมือนที่ pirate ship จริง) แต่ generate SDF เอง:

- atlas เป็น DDS **uncompressed 8-bit luminance** 2048x1024 ไม่มี mip
  (ไม่ใช่ BC4 อย่างที่คาดจาก pirate — ตรวจ header แล้ว: pfFlags=LUMINANCE, bitcount=8)
  ค่า pixel = SDF: 128 + d*SLOPE (d = ระยะจากขอบ ink หน่วย atlas px, บวก=ใน ink)
- พื้นที่ใต้ glyph เดิมของ atlas ว่างทั้งแถบ -> วาดไทยลงโซนว่าง
  แล้ว "repoint" UV ของ donor slot มาหา (จำนวน glyph คงเดิม — replace-mode ปลอดภัย
  ตามคำเตือน tail ใน font_tool.py; รูป Cyrillic เดิมยังอยู่ในที่เดิมแต่ไม่ถูกอ้างถึง)
- metrics arrayB = [bearingX(xMin), yBottom, xMax, yTop, advance] (หน่วย em=1000)
  วัดจาก glyph เดิม: ink วาดที่สเกล EM_PER_PX=12.51 em/px, กรอบ UV = ink bbox + pad ~10.5px
  (สเปกเต็ม + ที่มาของค่าคงที่: docs/font_k2r_slotmap.md)
- มาร์ก (สระบน/ล่าง + วรรณยุกต์): advance=0, bearingX บวกจัดกึ่งกลาง/ตำแหน่ง native
  เหนือพยัญชนะที่ "ตามหลัง" (thai_encode reorder มาร์กมาก่อนฐาน)

ใช้:  python scripts/inject_thai_sdf.py
อ่าน  extracted/font/system_main_en_all_sdf.{bin,dds} (ต้นฉบับ — ไม่แตะ)
เขียน build/font/system_main_en_all_sdf.{bin,dds} + build/font/preview_thai.png
"""
import io
import os
import struct
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import distance_transform_edt

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from font_tool import Font, cp_pack, cp_unpack
from thai_encode import THAI_CHARS, ENCODE, DECODE, encode

# ---- ค่าคงที่จากการวัดฟอนต์เดิม (docs/font_k2r_slotmap.md) ----
ATLAS_W, ATLAS_H = 2048, 1024
EM_PER_PX = 12.51      # em ต่อ atlas px (วัด ink สูง 358 glyph, สม่ำเสมอมาก p10-p90 = 12.50-12.57)
SLOPE     = 12.40      # ระดับ SDF ต่อ px (วัดจาก ■ ○ H: 12.27-12.43)
PAD_PX    = 10.5       # ขอบ SDF รอบ ink ในกรอบ UV (วัด median 10.1-11.5 px)
SS        = 8          # supersample ตอน render/EDT (ความละเอียดระยะ ~1/16 atlas px)

# ---- สเกล/ตำแหน่งอักษรไทย (อิง envelope ที่ pirate ship แล้วเห็นจริงในเกม) ----
THAI_SCALE  = 0.90     # game-em ต่อ Sarabun-unit (em 1000): ก สูง 590*0.9=531em
                       # (~77% ของ cap 687 — ใกล้สัดส่วน Thai:Latin ของ Sarabun เอง;
                       #  ใหญ่กว่าม็อด AI v1.3 ~10% แต่ยอด/ฐาน stack ยังอยู่ใน envelope
                       #  ที่พิสูจน์ในเกมแล้ว: ink สูงสุด ~1010em ต่ำสุด ~-307em)
TONE_SCALE  = 0.70     # ย่อวรรณยุกต์+การันต์ ให้ยอดไม่ทะลุเพดาน (ยอดสุด ~1010em)
LOWER_SCALE = 0.80     # ย่อสระล่าง ุ ู ฺ ให้พ้นหางพยัญชนะ/ขอบล่าง
L_TONE      = 845      # ระดับ "ล่างสุด" ของวรรณยุกต์ (เหนือแนวสระบนซึ่งยอด ~840)
LOWER_TOP   = -60      # ระดับ "บนสุด" ของสระล่าง (ใต้ baseline)

UPPER = set('ัิีึื็ํ')          # สระบน/ไม้ไต่คู้/นิคหิต — ตำแหน่ง native ของ Sarabun
TONE  = set('่้๊๋์')            # วรรณยุกต์ + การันต์ — ยกสูงระดับเดียว (ไม่มี variant)
LOWER = set('ฺุู')              # สระล่าง

FONT_PX = 1000 * THAI_SCALE * SS / EM_PER_PX   # ขนาด font PIL (px ต่อ 1000 Sarabun units)


def render_hi(ttf, ch, scale=1.0):
    """render ตัวอักษรเดี่ยวที่ hi-res -> (mask bool, x0,y0(=ink offset em เทียบ pen), adv em)
    คืน None ถ้าไม่มี ink"""
    F = FONT_PX * scale
    font = ImageFont.truetype(str(ttf), int(round(F)))
    em_per_hipx = EM_PER_PX / SS
    W = int(F * 4); H = int(F * 5)
    ox, oy = int(F * 1.5), int(F * 3.2)          # pen origin (เผื่อ mark ยื่นซ้าย/บนล่าง)
    im = Image.new('L', (W, H), 0)
    ImageDraw.Draw(im).text((ox, oy), ch, font=font, fill=255, anchor='ls')
    bb = im.getbbox()
    if not bb:
        return None
    l, t, r, b = bb
    mask = np.asarray(im.crop(bb), dtype=np.uint8) >= 128
    x0_em = (l - ox) * em_per_hipx               # ขอบซ้าย ink เทียบ pen
    ytop_em = (oy - t) * em_per_hipx             # ขอบบน ink เทียบ baseline (y-up)
    adv_em = font.getlength(ch) * em_per_hipx
    return mask, x0_em, ytop_em, adv_em


def sdf_tile(mask):
    """mask hi-res (bool, ink bbox แนบขอบ) -> tile SDF uint8 ขนาด atlas px (ink + pad รอบด้าน)
    ink วางที่ offset PAD_PX พอดีทุกด้าน"""
    pad = int(round(PAD_PX * SS))
    m = np.pad(mask, pad)
    h, w = m.shape
    # ขยายให้หารด้วย SS ลงตัว (ขยายขอบขวา/ล่าง — นอก ink อยู่แล้ว)
    H2 = -(-h // SS) * SS
    W2 = -(-w // SS) * SS
    m = np.pad(m, ((0, H2 - h), (0, W2 - w)))
    d_in = distance_transform_edt(m)
    d_out = distance_transform_edt(~m)
    d = np.where(m, d_in - 0.5, -(d_out - 0.5))          # ระยะ signed หน่วย hi-res px
    d = d.reshape(H2 // SS, SS, W2 // SS, SS).mean(axis=(1, 3)) / SS   # -> atlas px
    return np.clip(np.rint(127.5 + SLOPE * d), 0, 255).astype(np.uint8)


def main():
    if paths.FONT_BASENAME is None:
        sys.exit("FONT_BASENAME ยังไม่กำหนดใน paths.py — รัน survey_fonts.py กับ font par ของ Judgment จริงก่อน (ห้าม copy slot map จากภาคอื่น)")
    ttf = paths.SARABUN_TTF
    src_bin, src_dds = paths.FONT_SRC_BIN, paths.FONT_SRC_DDS
    out_dir = paths.BUILD / 'font'
    out_dir.mkdir(parents=True, exist_ok=True)

    f = Font(str(src_bin))
    dds = bytearray(open(src_dds, 'rb').read())
    assert struct.unpack_from('<I', dds, 88)[0] == 8, 'atlas ต้องเป็น 8-bit luminance'
    atlas = np.frombuffer(dds, np.uint8, ATLAS_W * ATLAS_H, 128).reshape(ATLAS_H, ATLAS_W).copy()
    slot_index = {cp_unpack(cp): i for i, cp in enumerate(f.cps) if cp_unpack(cp)}

    # ---- โซนว่างใต้ glyph เดิม ----
    y_used = max(int(np.ceil(uv[3] * ATLAS_H)) for uv in f.uv)
    y_start = y_used + 3
    print(f'glyph เดิมใช้ถึง y={y_used} -> เริ่มวาดที่ y={y_start} (เหลือ {ATLAS_H - y_start} แถว)')

    # ---- render ทุกตัว + เก็บ tile ----
    glyphs = {}          # ch -> dict(tile, met)
    natives = {}         # ch -> (x0, ytop, adv, w, h) หน่วย em (สเกลตามชนิดแล้ว)
    for ch in THAI_CHARS:
        scale = TONE_SCALE if ch in TONE else LOWER_SCALE if ch in LOWER else 1.0
        r = render_hi(ttf, ch, scale)
        assert r, f'Sarabun ไม่มี glyph {ch!r} (U+{ord(ch):04X})'
        mask, x0, ytop, adv = r
        em_per_hipx = EM_PER_PX / SS
        w_em = mask.shape[1] * em_per_hipx
        h_em = mask.shape[0] * em_per_hipx
        natives[ch] = (x0, ytop, adv, w_em, h_em)
        glyphs[ch] = {'tile': sdf_tile(mask)}

    # จุดอ้างอิงแนวนอนของมาร์ก: advance กลาง ๆ ของพยัญชนะ (มาร์กวาด "ก่อน" ฐาน ณ pen เดียวกัน
    # -> ตำแหน่ง native ของมาร์ก (ออกแบบให้อยู่หลัง advance ฐาน) = MADV + native_x)
    cons = [c for c in THAI_CHARS if 0x0E01 <= ord(c) <= 0x0E2E and ord(c) not in (0x0E24, 0x0E26)]
    MADV = float(np.median([natives[c][2] for c in cons]))
    print(f'MADV (advance พยัญชนะ median) = {MADV:.0f} em')

    # ---- ตั้ง metrics ----
    for ch in THAI_CHARS:
        x0, ytop, adv, w, h = natives[ch]
        if ch in UPPER:
            # ตำแหน่ง native ของ Sarabun (แนว y แถบ ~610..840em) + เลื่อนไปอยู่เหนือฐานที่ตามมา
            bx, yt, a = MADV + x0, ytop, 0
        elif ch in TONE:
            # ยกขึ้นระดับเดียว (เหนือสระบน) — กึ่งกลาง native, ล่างสุดที่ L_TONE
            cx_native = MADV + (x0 / TONE_SCALE + (x0 / TONE_SCALE + w / TONE_SCALE)) / 2
            # ยอดสุดไม่เกิน 1010em (envelope ที่ pirate พิสูจน์ในเกม ~1011) — ์ ตัวสูงโดนกดลงเล็กน้อย
            bx, yt, a = cx_native - w / 2, min(L_TONE + h, 1010), 0
        elif ch in LOWER:
            cx_native = MADV + (x0 / LOWER_SCALE + (x0 / LOWER_SCALE + w / LOWER_SCALE)) / 2
            bx, yt, a = cx_native - w / 2, LOWER_TOP, 0
        else:
            bx, yt, a = x0, ytop, adv
        met = (int(round(bx)), int(round(yt - h)), int(round(bx + w)),
               int(round(yt)), int(round(a)))
        assert all(-32768 <= v <= 32767 for v in met)
        glyphs[ch]['met'] = met

    # ---- pack ลงโซนว่าง (shelf, เรียงสูง->เตี้ย) ----
    order = sorted(THAI_CHARS, key=lambda c: glyphs[c]['tile'].shape[0], reverse=True)
    px, py, rowh, GAP = 1, y_start, 0, 1
    for ch in order:
        tile = glyphs[ch]['tile']
        th_, tw = tile.shape
        if px + tw + GAP > ATLAS_W:
            px = 1; py += rowh + GAP; rowh = 0
        assert py + th_ < ATLAS_H, f'atlas เต็ม (ถึง {ch!r} y={py})'
        atlas[py:py + th_, px:px + tw] = tile
        glyphs[ch]['uv'] = (px / ATLAS_W, py / ATLAS_H, (px + tw) / ATLAS_W, (py + th_) / ATLAS_H)
        glyphs[ch]['rect'] = (px, py, tw, th_)
        px += tw + GAP; rowh = max(rowh, th_)
    print(f'วาดครบ {len(order)} glyph, ใช้ atlas ถึง y={py + rowh}/{ATLAS_H}')

    # ---- repoint donor slots (replace-mode: จำนวน glyph คงเดิม) ----
    for ch in THAI_CHARS:
        donor = chr(ENCODE[ch])
        i = slot_index[donor]
        assert f.cps[i] == cp_pack(donor)
        f.uv[i] = glyphs[ch]['uv']
        f.met[i] = glyphs[ch]['met']

    # ---- เขียนผลลัพธ์ ----
    out_bin = out_dir / (paths.FONT_BASENAME + '.bin')
    out_dds = out_dir / (paths.FONT_BASENAME + '.dds')
    built = f.build()
    orig = open(src_bin, 'rb').read()
    assert len(built) == len(orig), 'ขนาด bin ต้องเท่าเดิม (replace-mode)'
    open(out_bin, 'wb').write(built)
    dds[128:128 + ATLAS_W * ATLAS_H] = atlas.tobytes()
    open(out_dds, 'wb').write(dds)
    print(f'เขียน {out_bin} ({len(built)} B) และ {out_dds} ({len(dds)} B)')

    # ---- ตรวจกลับ ----
    f2 = Font(str(out_bin))
    assert len(f2.cps) == 366 and f2.cps == f.cps and f2.tail == f.tail  # K3 มี 366 glyph (K2R = 362)
    assert open(out_dds, 'rb').read(128) == open(src_dds, 'rb').read(128), 'DDS header ต้องเท่าเดิม'
    n_diff = sum(1 for a, b in zip(f2.uv, Font(str(src_bin)).uv) if a != b)
    print(f'ตรวจกลับ OK: {len(f2.cps)} glyphs, cp table เท่าเดิม, UV เปลี่ยน {n_diff} slot')

    make_preview(out_bin, out_dds, out_dir / 'preview_thai.png', ttf)


# ================= preview =================
def _alpha(tile):
    return np.clip((tile.astype(np.float32) - 127.5) / SLOPE + 0.5, 0, 1)

def make_preview(bin_path, dds_path, out_png, ttf):
    """grid glyph ไทยทุกตัว (decode จาก DDS ใหม่) + บรรทัดทดสอบ render จำลองด้วย metrics จริง"""
    f = Font(str(bin_path))
    d = open(dds_path, 'rb').read()
    atlas = np.frombuffer(d, np.uint8, ATLAS_W * ATLAS_H, 128).reshape(ATLAS_H, ATLAS_W)
    idx = {cp_unpack(cp): i for i, cp in enumerate(f.cps) if cp_unpack(cp)}
    lab = ImageFont.truetype(str(ttf), 22)

    COLS, CW, CH = 10, 190, 170
    rows = -(-len(THAI_CHARS) // COLS)
    grid = Image.new('L', (COLS * CW, rows * CH + 260), 20)
    dr = ImageDraw.Draw(grid)
    for k, ch in enumerate(THAI_CHARS):
        gx, gy = (k % COLS) * CW, (k // COLS) * CH
        i = idx[chr(ENCODE[ch])]
        u0, v0, u1, v1 = f.uv[i]
        x0, y0 = int(round(u0 * ATLAS_W)), int(round(v0 * ATLAS_H))
        x1, y1 = int(round(u1 * ATLAS_W)), int(round(v1 * ATLAS_H))
        a = (_alpha(atlas[y0:y1, x0:x1]) * 255).astype(np.uint8)
        im = Image.fromarray(a)
        if im.width > CW - 10 or im.height > CH - 34:
            im.thumbnail((CW - 10, CH - 34))
        grid.paste(im, (gx + (CW - im.width) // 2, gy + 4 + (CH - 34 - im.height) // 2))
        dr.text((gx + 8, gy + CH - 28),
                f'{ch}  {ord(ch):04X}→{ENCODE[ch]:04X}', font=lab, fill=255)
        dr.line([(gx, gy + CH - 1), (gx + CW, gy + CH - 1)], fill=60)

    # บรรทัดจำลอง: วาดตาม metrics + advance จริง (พิสูจน์ reorder/advance=0/ตำแหน่งมาร์ก)
    sample = 'สวัสดีครับ ผมชื่อคาซึมะ คิริว น้ำ ที่นี่ ๑๒๓ ฿'
    enc = encode(sample)
    P_EM = PAD_PX * EM_PER_PX
    pen = 0.0; parts = []
    for c in enc:
        if c == ' ':
            pen += 300; continue
        i = idx.get(c)
        if i is None:
            pen += 300; continue
        bx, yb, xmax, yt, adv = f.met[i]
        u0, v0, u1, v1 = f.uv[i]
        x0, y0 = int(round(u0 * ATLAS_W)), int(round(v0 * ATLAS_H))
        x1, y1 = int(round(u1 * ATLAS_W)), int(round(v1 * ATLAS_H))
        tile = _alpha(atlas[y0:y1, x0:x1])
        parts.append((pen + bx - P_EM, yt + P_EM, tile))     # มุมซ้าย-บนของ quad (em)
        pen += adv
    top = max(p[1] for p in parts); bot = min(p[1] - p[2].shape[0] * EM_PER_PX for p in parts)
    lw = int((pen + 200) / EM_PER_PX) + 20
    lh = int((top - bot) / EM_PER_PX) + 20
    line = np.zeros((lh, lw), np.float32)
    for x_em, ytop_em, tile in parts:
        px = int(round(x_em / EM_PER_PX)) + 10
        py = int(round((top - ytop_em) / EM_PER_PX)) + 10
        h, w = tile.shape
        if px < 0: tile = tile[:, -px:]; w = tile.shape[1]; px = 0
        sub = line[py:py + h, px:px + w]
        np.maximum(sub, tile[:sub.shape[0], :sub.shape[1]], out=sub)
    line_img = Image.fromarray((line * 255).astype(np.uint8)).resize((lw * 2, lh * 2), Image.LANCZOS)
    if line_img.width > grid.width - 20:
        line_img.thumbnail((grid.width - 20, 10 ** 6))
    yline = rows * CH + 10
    dr.text((10, yline), 'render จำลองจาก metrics จริง: ' + sample, font=lab, fill=255)
    grid.paste(line_img, (10, yline + 34))
    grid.save(out_png)
    print(f'เขียน {out_png}')


if __name__ == '__main__':
    main()
