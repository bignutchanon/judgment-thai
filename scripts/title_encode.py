#!/usr/bin/env python3
"""ตัวแบ่งเซลล์ + ตัวจัด donor อัตโนมัติ สำหรับ **ฟอนต์หน้าไตเติล** ของ Judgment

สรุปข้อเท็จจริงที่ทดสอบในเกมจริงมาแล้ว (รอบ 3-7 · ดู HANDOFF.md):
  1. เขียนกลิฟไทยลงเซลล์ของ `meta_ot_cond_book.dds` แล้วขึ้นจอได้ ทั้งเซลล์ที่มีหมึกเดิม
     และเซลล์ว่าง
  2. **advance ผูกกับ codepoint ของ donor** (ตาราง width อยู่ใน exe) ไม่ได้มาจากรูปที่วาด
     → เลือก donor ที่ความกว้างใกล้เคียงกลิฟที่จะวาด = ได้ช่องไฟที่ดูเป็นธรรมชาติ
  3. **ไม่มี codepoint ไหนที่ advance = 0** (ลองมาแล้ว 10 ตัวทั้ง Latin-1 และ control)
     → มาร์กลอยแบบ per-char เป็นไปไม่ได้ ต้องประกอบ ฐาน+สระ+วรรณยุกต์ เป็นกลิฟเดียว
  4. ขยายภาพ atlas ไม่ได้ (engine ยึดตารางเดิม จอเละทั้งเมนู) → **เพดานตายตัว 384 เซลล์**

โมดูลนี้จึงทำสองอย่าง:
  - `segment()` แบ่งข้อความไทยเป็น "เซลล์" แบบเดียวกับ Y6: พยัญชนะฐาน + สระบน/ล่าง ≤1 +
    วรรณยุกต์ ≤1 ประกอบเป็นกลิฟเดียว (ตัวที่ไม่ใช่ไทยผ่านตรง)
  - `build_map()` จัด donor ให้แต่ละเซลล์โดย **จับคู่ตามความกว้าง**: วัดความกว้าง ink ของ
    กลิฟที่จะวาด แล้วจับคู่กับ donor ที่ความกว้าง ink เดิมใกล้ที่สุด (deterministic —
    เรียงทั้งสองฝั่งตามความกว้างแล้วจับคู่ตามลำดับ)

donor pool = ตัวอักษรละตินมีเครื่องหมาย U+00C0-00FC (49 ช่อง) — เลี่ยงสัญลักษณ์ © ® ¥ « » ¿
ที่มีโอกาสโผล่ในข้อความอังกฤษจริงของ UI และเลี่ยงเซลล์ว่างที่ยังไม่รู้ค่า width ที่ exe ให้
"""
import io
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from bc4_codec import decode_bc4
from title_slotmap import ATLAS_H, ATLAS_W, CELL_H, CELL_W, POOL_A, cell_xy

UPPER = set("ัิีึื็ํ")
TONE = set("่้๊๋์")
LOWER = set("ฺุู")
COMBINING = UPPER | TONE | LOWER

SRC_DDS = paths.EXTRACTED / "font" / "meta_ot_cond_book.dds"

BASE_REF = "ก"        # ตัวอ้างอิงตั้งขนาดฟอนต์
BASE_H = 22           # ความสูง ink ของตัวอ้างอิงในเซลล์ 64px (cap height ของฟอนต์เดิม = 25)
THAI_TTF = paths.THAI_TTF      # ฟอนต์ต้นแบบของกลิฟไทย — compare_fonts.py สลับตัวนี้ (ต้องล้าง _PPEM ด้วย)
_PPEM = None


def render_at(ch, ppem):
    """render ตัวอักษรเดี่ยวที่ ppem -> (ภาพ ink, dx, top, bottom) วัดจากเส้นฐาน (ลบ = เหนือฐาน)"""
    font = ImageFont.truetype(str(THAI_TTF), ppem)
    pad = ppem * 2
    im = Image.new("L", (ppem * 4, ppem * 5), 0)
    ox, oy = pad, pad * 2
    ImageDraw.Draw(im).text((ox, oy), ch, font=font, fill=255, anchor="ls")
    bb = im.getbbox()
    assert bb, f"render ว่างเปล่า: {ch!r}"
    return (np.asarray(im.crop(bb), dtype=np.uint8), bb[0] - ox, bb[1] - oy, bb[3] - oy)


def ppem():
    """ขนาดฟอนต์เดียวที่ใช้กับทุกตัวอักษร — ตั้งให้ ink ของ `ก` สูงเท่า BASE_H

    ความสม่ำเสมอของขนาดตัวอักษรมาจากตรงนี้: ห้ามสเกลกลิฟทีละตัวให้สูงเท่ากัน (ตัวที่มีหางบน
    อย่าง ใ ไ โ ป ฝ ฟ จะถูกย่อจนเล็กกว่าเพื่อน) ให้ใช้ ppem เดียวแล้ววางตามเส้นฐานแทน
    """
    global _PPEM
    if _PPEM is None:
        _im, _dx, top, bot = render_at(BASE_REF, 100)
        _PPEM = max(8, round(100 * BASE_H / (bot - top)))
    return _PPEM


# มาร์ก (สระบน/ล่าง/วรรณยุกต์) วาดเล็กกว่าฐานทั้งชุด — 27 ก.ย. 2026 เจ้าของแจ้งว่าข้อความสองบรรทัด
# สระล่างของบรรทัดบนชนสระบน/วรรณยุกต์ของบรรทัดล่าง ("อยู่" เหนือ "นั้น") · ขนาดเต็มทำให้ไทยกินที่
# -44..+11 px รอบเส้นฐาน (อังกฤษ -25..+6) และวรรณยุกต์ที่ซ้อนเหนือสระบน (นี้ ชี้ ครื้น) ล้นขอบบนของเซลล์
# จนถูกดันลงมาแตะสระ · ย่อทั้งคลาสด้วยสัดส่วนเดียว ไม่ใช่ normalize ความสูงรายตัว (กฎของ ppem() ยังอยู่)
MARK_SCALE = 0.89
MARKS = COMBINING | {"๎"}


def glyph_ppem(ch):
    """ppem ที่ใช้วาดตัวอักษรนี้ — ฐานใช้ ppem() · มาร์กใช้ ppem() x MARK_SCALE"""
    P = ppem()
    return max(8, round(P * MARK_SCALE)) if ch in MARKS else P


# เซลล์กว้าง 32 px และกลิฟเริ่มวาดที่ x = 2 (INK_X0) → ink กว้างได้ไม่เกิน 30 px ไม่งั้นขอบขวาถูกตัด
# (28 ก.ย. 2026 เจอกับ Taviraj: ฒ 32 · ณ 31 px) · ตัวที่เกินบีบแนวนอนให้พอดี — บีบได้ไม่เกิน 15%
# ตามกฎรอบ 8-9 · Sarabun/Noto ไม่มีตัวไหนเกิน ผลจึงเหมือนเดิมทุกพิกเซล
MAX_INK_W = 30


# รูป "ไม่มีเชิง" ของฐานเมื่อมีสระล่างตามมา (28 ก.ย. 2026 · เจ้าของทัก กตัญญู ที่ ู ทับเชิง ญ):
# ฟอนต์ไทยสลับ ญ ฐ เป็นกลิฟตัดเชิงผ่าน GSUB (Taviraj: yoYingthai.less / thoThanthai.less) ตอนมี ุ ู ฺ
# ตามหลัง · เราวาดแยกเป็นเซลล์ variant "less" แล้ว SlotMap.encode เลือกเองเมื่อตัวถัดไปเป็นสระล่าง
LESS_BASES = "ญฐ"


def render_less(ch, P):
    """รูปไม่มีเชิงของ ch จาก GSUB ของฟอนต์ (shape ch + ุ แล้วเอากลิฟแรก) -> รูปแบบเดียวกับ render_at

    ฟอนต์ที่ไม่มีกลิฟนี้ → ใช้รูปปกติแล้วตัดหมึกใต้เส้นฐานทิ้ง
    """
    import freetype
    import uharfbuzz as hb
    font = hb.Font(hb.Face(hb.Blob.from_file_path(str(THAI_TTF))))

    def first_gid(s):
        buf = hb.Buffer()
        buf.add_str(s)
        buf.guess_segment_properties()
        hb.shape(font, buf, {})
        return buf.glyph_infos[0].codepoint

    gid = first_gid(ch + "ุ")
    if gid != first_gid(ch):
        ft = freetype.Face(str(THAI_TTF))
        ft.set_pixel_sizes(0, P)
        ft.load_glyph(gid, freetype.FT_LOAD_DEFAULT)
        ft.glyph.render(freetype.FT_RENDER_MODE_NORMAL)
        bm = ft.glyph.bitmap
        img = np.array(bm.buffer, np.uint8).reshape(bm.rows, bm.pitch)[:, :bm.width]
        ys = np.flatnonzero((img > 0).any(axis=1))
        xs = np.flatnonzero((img > 0).any(axis=0))
        return (img[ys[0]:ys[-1] + 1, xs[0]:xs[-1] + 1].copy(), ft.glyph.bitmap_left + int(xs[0]),
                int(ys[0]) - ft.glyph.bitmap_top, int(ys[-1]) + 1 - ft.glyph.bitmap_top)
    img, dx, top, _bot = render_at(ch, P)
    return img[:max(1, -top)].copy(), dx, top, 0


def render_glyph(ch, variant=None):
    """กลิฟที่ใช้ผลิตจริง -> (ภาพ ink, dx, top, bottom) · ขนาด glyph_ppem + บีบถ้ากว้างเกิน MAX_INK_W

    slot_alloc (วัดความกว้าง/ความสูง) และ inject_thai_title (วาดเซลล์) ต้องเรียกตัวนี้ตัวเดียวกัน
    variant = "less" → รูปไม่มีเชิงของ ญ ฐ (ดู LESS_BASES)
    """
    if variant == "less":
        img, dx, top, bot = render_less(ch, glyph_ppem(ch))
    else:
        img, dx, top, bot = render_at(ch, glyph_ppem(ch))
    h, w = img.shape
    if w > MAX_INK_W:
        assert w <= MAX_INK_W / 0.85, f"{ch!r} กว้าง {w} px ต้องบีบเกิน 15% — ลด BASE_H หรือเปลี่ยนฟอนต์"
        img = np.asarray(Image.fromarray(img).resize((MAX_INK_W, h), Image.LANCZOS), dtype=np.uint8)
    return img, dx, top, bot


def natural_width(cell_text):
    """ความกว้าง ink จริงของฐานในเซลล์ (px) ที่ ppem มาตรฐาน"""
    return render_at(cell_text[0], ppem())[0].shape[1]


def segment(text):
    """แบ่งข้อความเป็นลิสต์ของ 'เซลล์' — ฐาน 1 ตัว + มาร์กที่เกาะอยู่ (คืนเป็นสตริงต่อเซลล์)"""
    cells = []
    for ch in text:
        if ch in COMBINING and cells and cells[-1][0] not in COMBINING:
            cells[-1] += ch
        else:
            cells.append(ch)
    return cells


def donor_widths():
    """ความกว้าง ink เดิมของแต่ละ donor ใน atlas ต้นฉบับ (ตัวแทนของ advance ที่ exe จะให้)"""
    raw = SRC_DDS.read_bytes()
    atlas = decode_bc4(raw[128:], ATLAS_W, ATLAS_H)
    out = {}
    for cp in POOL_A:
        x0, y0 = cell_xy(cp)
        cell = atlas[y0:y0 + CELL_H, x0:x0 + CELL_W]
        xs = np.where((cell > 16).any(axis=0))[0]
        out[cp] = int(xs.max() - xs.min() + 1) if len(xs) else 0
    return out


def build_map(strings, glyph_width):
    """strings: ข้อความไทยทั้งหมดที่จะใช้ · glyph_width(cell_text) -> ความกว้าง ink ที่จะวาด

    คืน (CELLS, ENCODE) โดย
      CELLS  = {donor_cp: (ข้อความของเซลล์, ป้ายกำกับ)}  ป้อนให้ inject_thai_title.py
      ENCODE = {ข้อความของเซลล์: donor_cp}                ใช้แปลงข้อความเป็นสตริง donor
    """
    cells = []
    for s in strings:
        for c in segment(s):
            if any("฀" <= ch <= "๿" for ch in c) and c not in cells:
                cells.append(c)

    pool = donor_widths()
    if len(cells) > len(pool):
        raise SystemExit(f"เซลล์ที่ต้องใช้ {len(cells)} เกิน donor pool {len(pool)} ช่อง — "
                         f"ต้องขยาย pool ไปใช้เซลล์ว่างเพิ่ม (ดู title_slotmap.EMPTY_EXTA)")

    # จับคู่แบบ "กว้างสุดก่อน แล้วเลือก donor ที่ความกว้างใกล้ที่สุดที่ยังว่าง"
    # (ดีกว่าเรียงจับคู่ตามลำดับ เพราะตัวกว้างจะได้ donor กว้างจริง ไม่ต้องถูกบีบมาก)
    need = sorted(((glyph_width(c), c) for c in cells), reverse=True)
    avail = dict(pool)
    CELLS, ENCODE = {}, {}
    for want_w, cell_text in need:
        cp = min(avail, key=lambda k: (abs(avail[k] - want_w), -avail[k]))
        w = avail.pop(cp)
        tag = "cluster" if len(cell_text) > 1 else "เดี่ยว"
        # ตัวที่สาม = ความกว้างเป้าหมายของ ink (บีบกลิฟให้พอดี advance ที่ donor จะได้)
        CELLS[cp] = (cell_text, f"{tag} · donor ink {w}px · กลิฟ {want_w}px", w + 1)
        ENCODE[cell_text] = cp
    return CELLS, ENCODE


def encode(text, ENCODE):
    """ข้อความไทย -> สตริง donor (ตัวที่ไม่ใช่ไทยผ่านตรง)"""
    out = []
    for c in segment(text):
        if c in ENCODE:
            out.append(chr(ENCODE[c]))
        elif any("฀" <= ch <= "๿" for ch in c):
            raise SystemExit(f"เซลล์ {c!r} ไม่มีใน map — เพิ่มข้อความต้นทางให้ครบก่อน build_map")
        else:
            out.append(c)
    return "".join(out)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    demo = ["เริ่มเกมใหม่", "เล่นต่อ", "ตั้งค่า"]
    for s in demo:
        print(s, "->", segment(s))
    w = donor_widths()
    print(f"donor pool {len(w)} ช่อง · ink {min(w.values())}-{max(w.values())} px")
