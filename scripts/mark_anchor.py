#!/usr/bin/env python3
"""ตำแหน่งแนวนอนของสระ/วรรณยุกต์ตามที่ผู้ออกแบบฟอนต์ตั้งไว้ — อ่านจาก GPOS (mark/mkmk) ผ่าน HarfBuzz

## ทำไมต้องมี (28 ก.ย. 2026 — เจ้าของแจ้ง "ไม้เอกลอยออกจากสระ อี")

เดิม `slot_alloc` วางมาร์กทุกตัว **กึ่งกลาง ink ของฐาน** (`font_metrics.mark_place`) แต่ฟอนต์ไทยจริง
**ชิดขวา**: สระบนวางเหนือเสาขวาของพยัญชนะ วรรณยุกต์ที่ซ้อนบนสระไปอยู่ปลายขวาของสระ (ที่ นี่ กี้)
ผลคือ ่ ไปอยู่กลาง ี ห่างจากหางสระ ดูเหมือนลอยแยกกัน · ป ฝ ฟ ฬ ก็ต้องหลบหางสูงไปทางซ้ายอีกแบบ

## วิธี

shape "ฐาน + มาร์ก" (และ "ฐาน + สระบน + วรรณยุกต์" สำหรับชั้นซ้อน) ด้วยฟอนต์ต้นแบบตัวจริง
(`title_encode.THAI_TTF`) ที่ ppem เดียวกับที่วาด แล้ววัด

    off = ขอบขวา ink ของมาร์ก - ขอบขวา ink ของฐาน     (px · ลบ = มาร์กจบก่อนขอบขวาฐาน)

ใช้ขอบขวาเพราะฟอนต์ไทยจัดมาร์กชิดขวา และมาร์กของเราถูกย่อด้วย `MARK_SCALE` — ยึดขอบขวาไว้
ตำแหน่งที่ตาเห็นจึงเหมือนต้นฉบับ · ค่านี้ไม่ขึ้นกับความกว้างฐาน (ต่างจากการวางกึ่งกลาง) จึงแบ่งชั้นฐาน
ตาม off ได้ตรงกว่าแบ่งตามความกว้าง — ป ฝ ฟ ฬ แยกเป็นชั้นของตัวเองอัตโนมัติ
"""
import numpy as np
import uharfbuzz as hb
import freetype


class Shaper:
    """ตัววัดตำแหน่งมาร์กของฟอนต์หนึ่งตัวที่ ppem หนึ่งค่า"""

    def __init__(self, ttf, ppem):
        self.ppem = ppem
        face = hb.Face(hb.Blob.from_file_path(str(ttf)))
        self.font = hb.Font(face)
        self.scale = ppem / float(face.upem)
        self.ft = freetype.Face(str(ttf))
        self.ft.set_pixel_sizes(0, ppem)
        self._ink = {}

    def ink_x(self, gid):
        """(ขอบซ้าย, ขอบขวาแบบไม่รวม) ของ ink วัดจากจุดกำเนิดกลิฟ (px) · None = กลิฟว่าง"""
        if gid not in self._ink:
            self.ft.load_glyph(gid, freetype.FT_LOAD_NO_HINTING)
            self.ft.glyph.render(freetype.FT_RENDER_MODE_NORMAL)
            bm = self.ft.glyph.bitmap
            res = None
            if bm.width and bm.rows:
                img = np.array(bm.buffer, np.uint8).reshape(bm.rows, bm.pitch)[:, :bm.width]
                cols = np.flatnonzero((img > 0).any(axis=0))
                if len(cols):
                    left = self.ft.glyph.bitmap_left
                    res = (left + int(cols[0]), left + int(cols[-1]) + 1)
            self._ink[gid] = res
        return self._ink[gid]

    def right_edges(self, text):
        """shape ข้อความ -> ขอบขวา ink (px) ของแต่ละกลิฟตามลำดับ · None ถ้าจำนวนกลิฟไม่เท่าตัวอักษร"""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.font, buf, {})
        infos, poss = buf.glyph_infos, buf.glyph_positions
        if len(infos) != len(text):              # ถูกรวม/แตกกลิฟ — วัดไม่ได้ ให้ผู้เรียกใช้ค่าสำรอง
            return None
        out, pen = [], 0.0
        for info, pos in zip(infos, poss):
            ink = self.ink_x(info.codepoint)
            x = pen + pos.x_offset * self.scale
            out.append(None if ink is None else x + ink[1])
            pen += pos.x_advance * self.scale
        return out

    def mark_off(self, base, marks):
        """off ของมาร์กตัวสุดท้ายใน `marks` ที่ซ้อนบน `base` (px) · None ถ้าวัดไม่ได้"""
        r = self.right_edges(base + marks)
        if not r or r[0] is None or r[-1] is None:
            return None
        return r[-1] - r[0]
