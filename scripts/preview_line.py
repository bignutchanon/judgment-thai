#!/usr/bin/env python3
"""จำลองการวาดข้อความของเอนจิ้นจาก atlas + `kerning_table` ที่บิลด์ไว้ -> PNG

ทำไมต้องมี: การทดสอบในเกมเป็นหน้าที่ผู้ใช้ (กติกาเหล็กข้อ 2) รอบ feedback จึงช้ามาก
ตัวจำลองนี้ใช้ข้อมูลชุดเดียวกับที่เกมใช้จริง — atlas ที่ `inject_thai_title.py` วาด และค่า
(L, R) ที่ `gen_font_bin.py` เขียน — แล้ววางกลิฟตามสูตรของเอนจิ้น:

    x_ink = pen - K*L + ink_x0        แล้ว     pen += CELL_ADV - K*(L + R)

จึงเห็นช่องไฟจริง สระซ้อนจริง ก่อนส่งให้ผู้ใช้เปิดเกม

ใช้:  python scripts/preview_line.py                 # ประโยคตัวอย่างมาตรฐาน
      python scripts/preview_line.py --file x.txt    # อ่านบรรทัดจากไฟล์ (ห้ามส่งไทยผ่าน CLI)
"""
import io
import os
import struct
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
import font_metrics as FM
from bc4_codec import decode_bc4
from slot_alloc import SlotMap
from title_slotmap import ATLAS_H, ATLAS_W, CELL_H, CELL_W, cell_xy

BUILT_DDS = paths.BUILD / "font" / "meta_ot_cond_book.dds"
OUT_PNG = paths.BUILD / "font" / "preview_line.png"
SCALE = 2

SAMPLES = [
    "ยากามิ ทนายผันตัวเป็นนักสืบ",
    "ที่นี่คือคามุโรโจ เมืองที่ไม่เคยหลับ",
    "ผมจะพิสูจน์ว่าเขาบริสุทธิ์ให้ได้",
    "สำนักงานนักสืบยากามิ · ตระกูลมัตสึกาเนะ",
    "ปื้ด ปุ๊ ฝั่ง ฟื้น ผู้ ญี่ปุ่น น้ำ ทั้ง ๆ",
    "กด [X] เพื่อคุยกับ ไคโตะ (100%)",
]


def load_atlas():
    raw = BUILT_DDS.read_bytes()
    h, w = struct.unpack_from("<II", raw[:128], 12)
    return decode_bc4(raw[128:], w, h)


def draw_line(atlas, sm, text):
    """คืนภาพหนึ่งบรรทัดตามที่เอนจิ้นจะวาด"""
    enc = sm.encode(text)
    W = 32 + sum(int(FM.CELL_ADV) for _ in enc) + CELL_W
    canvas = np.zeros((CELL_H, W), dtype=np.uint8)
    pen = 20.0
    for ch in enc:
        cp = ord(ch)
        spec = sm.cells.get("%04X" % cp)
        if spec is None:                                  # ASCII — ใช้เซลล์เดิมของเกม
            x0, y0 = cell_xy(cp)
            cell = atlas[y0:y0 + CELL_H, x0:x0 + CELL_W]
            x = int(round(pen))
            if 0 <= x <= W - CELL_W:
                np.maximum(canvas[:, x:x + CELL_W], cell, out=canvas[:, x:x + CELL_W])
            pen += 14 if ch != " " else 10                # ประมาณ ไม่ใช่ประเด็นของ preview นี้
            continue
        x0, y0 = cell_xy(cp)
        cell = atlas[y0:y0 + CELL_H, x0:x0 + CELL_W]
        x = int(round(pen - FM.K * spec["L"]))
        if x < 0:
            x = 0
        if x + CELL_W <= W:
            np.maximum(canvas[:, x:x + CELL_W], cell, out=canvas[:, x:x + CELL_W])
        pen += FM.CELL_ADV - FM.K * (spec["L"] + spec["R"])
    xs = np.flatnonzero((canvas > 16).any(axis=0))
    if len(xs):
        canvas = canvas[:, :min(W, int(xs[-1]) + 8)]
    return canvas


def main():
    lines = SAMPLES
    if "--file" in sys.argv:
        p = paths.Path(sys.argv[sys.argv.index("--file") + 1])
        lines = [l.rstrip("\n") for l in io.open(p, encoding="utf-8") if l.strip()]
    assert BUILT_DDS.exists(), f"ยังไม่ได้บิลด์ฟอนต์: {BUILT_DDS}"
    atlas = load_atlas()
    sm = SlotMap.load()
    imgs = [draw_line(atlas, sm, s) for s in lines]
    W = max(i.shape[1] for i in imgs)
    out = np.zeros((CELL_H * len(imgs), W), dtype=np.uint8)
    for i, im in enumerate(imgs):
        out[i * CELL_H:(i + 1) * CELL_H, :im.shape[1]] = im
    img = Image.fromarray(out).resize((W * SCALE, CELL_H * len(imgs) * SCALE), Image.LANCZOS)
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PNG)
    for s, im in zip(lines, imgs):
        n_th = sum(1 for c in s if "฀" <= c <= "๿")
        print("%-46s กว้าง %4d px · %d ตัวไทย · เฉลี่ย %.1f px/ตัว"
              % (s[:44], im.shape[1], n_th, (im.shape[1] - 28) / max(1, n_th)))
    print("เขียน %s" % OUT_PNG)


if __name__ == "__main__":
    main()
