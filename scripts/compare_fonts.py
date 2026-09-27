#!/usr/bin/env python3
"""เทียบฟอนต์ต้นแบบของกลิฟไทย — รันทุกฟอนต์ผ่านสายผลิตจริงแล้วจำลองการวาดของเอนจิ้น

ทำไมต้องมี (27 ก.ย. 2026): เจ้าของถามว่าลองฟอนต์อื่นนอกจาก Sarabun ได้ไหม · สายผลิตทั้งหมด
(`slot_alloc` คิด advance/ตำแหน่งมาร์ก · `inject_thai_title.draw_cell` วาดเซลล์) ขึ้นกับฟอนต์ต้นแบบ
ตัวเดียวคือ `title_encode.THAI_TTF` — สคริปต์นี้สลับตัวนั้นทีละฟอนต์ แล้วคำนวณการจัดสรรใหม่ในหน่วยความจำ
(ไม่เขียน slotmap.json · ไม่แตะ build/font/*.dds) จึงเห็นผลเหมือนตอนบิลด์จริง รวมถึงช่องไฟและการซ้อนสระ

ผลลัพธ์ (build/font/compare/):
  <กลุ่ม>.png   ภาพเทียบ ขนาดจริงของซับคัตซีนที่ 1080p (ฟอนต์ 36 = 1 px atlas ต่อ 1 px จอ)
                แต่ละฟอนต์: ประโยคเดี่ยว · สองบรรทัดที่ระยะ PITCH · ไทยปนอังกฤษ (อังกฤษ = ฟอนต์เดิมของเกม)
  summary.md    ตัวเลขต่อฟอนต์: ความสูงที่กิน (บน/ล่าง) · ความกว้างเฉลี่ยต่อบรรทัดเทียบ Sarabun ·
                ความหนาเส้นเทียบอังกฤษของเกม

ใช้:  python scripts/compare_fonts.py              # ทุกฟอนต์ใน CANDIDATES
      python scripts/compare_fonts.py --only noto  # เฉพาะชื่อที่มีคำนี้
ฟอนต์อยู่ที่ font/candidates/ (OFL ทุกตัว · ไฟล์ OFL_*.txt อยู่ข้างกัน) — variable font ถูก instance
เป็นไฟล์ static ไว้แล้ว (fontTools.varLib.instancer)
"""
import argparse
import contextlib
import io
import json
import os
import struct
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths                                   # noqa: E402
import font_metrics as FM                      # noqa: E402
import slot_alloc                              # noqa: E402
import title_encode                            # noqa: E402
from bc4_codec import decode_bc4               # noqa: E402
from inject_thai_title import draw_cell        # noqa: E402
from title_slotmap import BASELINE_Y, CELL_H, CELL_W, cell_xy   # noqa: E402

CAND = paths.ROOT / "font" / "candidates" if hasattr(paths, "ROOT") else \
    paths.SARABUN_TTF.parent / "candidates"
OUT_DIR = paths.BUILD / "font" / "compare"
PITCH = 56                    # ระยะบรรทัด (px atlas) หลัง patch_line_spacing.py

GROUPS = {
    "looped": [
        ("Sarabun Regular", paths.SARABUN_TTF),
        ("Sarabun Medium", CAND / "Sarabun-Medium.ttf"),
        ("Noto Sans Thai Looped", CAND / "NotoSansThaiLooped-Regular.ttf"),
        ("Noto Sans Thai Looped SemiCondensed", CAND / "NotoSansThaiLooped-SemiCondensed.ttf"),
        ("Noto Sans Thai Looped Condensed", CAND / "NotoSansThaiLooped-Condensed.ttf"),
        ("Noto Sans Thai Looped Condensed Medium", CAND / "NotoSansThaiLooped-CondensedMedium.ttf"),
        ("IBM Plex Sans Thai Looped", CAND / "IBMPlexSansThaiLooped-Regular.ttf"),
        ("IBM Plex Sans Thai Looped Medium", CAND / "IBMPlexSansThaiLooped-Medium.ttf"),
        ("Niramit", CAND / "Niramit-Regular.ttf"),
        ("K2D", CAND / "K2D-Regular.ttf"),
    ],
    "loopless": [
        ("Noto Sans Thai", CAND / "NotoSansThai-Regular.ttf"),
        ("Noto Sans Thai Condensed", CAND / "NotoSansThai-Condensed.ttf"),
        ("Noto Sans Thai Condensed Medium", CAND / "NotoSansThai-CondensedMedium.ttf"),
        ("IBM Plex Sans Thai", CAND / "IBMPlexSansThai-Regular.ttf"),
        ("Anuphan", CAND / "Anuphan-Regular.ttf"),
        ("Kanit Light", CAND / "Kanit-Light.ttf"),
        ("Kanit", CAND / "Kanit-Regular.ttf"),
        ("Prompt", CAND / "Prompt-Regular.ttf"),
        ("Bai Jamjuree", CAND / "BaiJamjuree-Regular.ttf"),
    ],
    "serif": [
        ("Noto Sans Thai Looped Condensed", paths.FONT_DIR / "NotoSansThaiLooped-Condensed.ttf"),
        ("Taviraj", paths.FONT_DIR / "Taviraj-Regular.ttf"),
    ],
}

SINGLE = "ยากามิ ทนายผันตัวเป็นนักสืบ คดีนี้ไม่ธรรมดาแน่นอน"
TWO = ("เขาอยู่ที่นี่ ผมรู้ดีกว่าใคร ปู่ก็รู้", "นั้นแหละที่ปู่ทิ้งไว้ให้ ฟื้นขึ้นมาสิ")
MIXED = "Yagami ยากามิ · Kaito ไคโตะ · 100% OK?"


def load_atlas(p):
    raw = open(p, "rb").read()
    h, w = struct.unpack_from("<II", raw[:128], 12)
    return decode_bc4(raw[128:], w, h)


ORIG = load_atlas(paths.EXTRACTED / "font" / "meta_ot_cond_book.dds")
_FB = json.load(io.open(paths.EXTRACTED / "db_en" / "en" / "font.bin.json", encoding="utf-8"))
_KT = _FB["17"]["meta_ot_cond_book"]["kerning_table"]


def orig_lr(cp):
    r = _KT[str(FM.cell_index(cp))]
    row = r[list(r)[0]]
    return float(row["5"]), float(row["6"])


def memo(fn):
    cache = {}

    def wrap(*a, **k):
        key = (a, tuple(sorted(k.items())))
        if key not in cache:
            cache[key] = fn(*a, **k)
        return cache[key]
    return wrap


# คลังคำแปลโหลดครั้งเดียว (ไม่ขึ้นกับฟอนต์)
slot_alloc.load_corpora = memo(slot_alloc.load_corpora)
slot_alloc.en_used_codepoints = memo(slot_alloc.en_used_codepoints)
slot_alloc.th_used_codepoints = memo(slot_alloc.th_used_codepoints)


def build_font(ttf):
    """สลับฟอนต์ต้นแบบ -> (SlotMap, atlas ที่วาดแล้ว) — ไม่เขียนไฟล์ใด ๆ"""
    title_encode.THAI_TTF = ttf
    title_encode._PPEM = None
    with contextlib.redirect_stdout(io.StringIO()):
        data = slot_alloc.allocate()
    sm = slot_alloc.SlotMap(data)
    atlas = ORIG.copy()
    for k, spec in data["cells"].items():
        x0, y0 = cell_xy(int(k, 16))
        atlas[y0:y0 + CELL_H, x0:x0 + CELL_W] = draw_cell(spec)
    return sm, atlas, data


def engine_line(sm, atlas, text):
    enc = sm.encode(text)
    W = 40 + 40 * len(enc)
    c = np.zeros((CELL_H, W), np.uint8)
    pen = 8.0
    for ch in enc:
        cp = ord(ch)
        spec = sm.cells.get("%04X" % cp)
        if spec is None and not FM.in_table(cp):      # นอกตาราง (— “ ” ฯลฯ ในคลัง) — นับความกว้างคงที่
            pen += FM.K
            continue
        L, R = (spec["L"], spec["R"]) if spec else orig_lr(cp)
        x0, y0 = cell_xy(cp)
        x = max(0, int(round(pen - FM.K * L)))
        if x + CELL_W <= W:
            np.maximum(c[:, x:x + CELL_W], atlas[y0:y0 + CELL_H, x0:x0 + CELL_W],
                       out=c[:, x:x + CELL_W])
        pen += FM.CELL_ADV - FM.K * (L + R)
    return c, pen


def stroke_width(img):
    """ความหนาเส้นเฉลี่ยโดยประมาณ = 2 x พื้นที่หมึก / เส้นรอบรูป (ภาพขาวดำที่ 50%)"""
    b = img > 127
    area = b.sum()
    per = (b[:, 1:] != b[:, :-1]).sum() + (b[1:, :] != b[:-1, :]).sum()
    return 2.0 * area / per if per else 0.0


def cell_img(atlas, cp):
    x0, y0 = cell_xy(cp)
    return atlas[y0:y0 + CELL_H, x0:x0 + CELL_W]


EN_STROKE = np.mean([stroke_width(cell_img(ORIG, ord(c))) for c in "nmuhoadbl"])


def sample_texts(n=3000):
    data = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    out = [v for v in data.values() if isinstance(v, str) and any("฀" <= c <= "๿" for c in v)]
    return out[:n]


def label_img(text, W):
    im = Image.new("L", (W, 30), 0)
    try:
        f = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        f = ImageFont.load_default()
    ImageDraw.Draw(im).text((8, 4), text, font=f, fill=150)
    return np.asarray(im)


def block(name, sm, atlas, data, texts, base_width):
    single, _ = engine_line(sm, atlas, SINGLE)
    l1, _ = engine_line(sm, atlas, TWO[0])
    l2, _ = engine_line(sm, atlas, TWO[1])
    two = np.zeros((CELL_H + PITCH, max(l1.shape[1], l2.shape[1])), np.uint8)
    np.maximum(two[:CELL_H, :l1.shape[1]], l1, out=two[:CELL_H, :l1.shape[1]])
    np.maximum(two[PITCH:PITCH + CELL_H, :l2.shape[1]], l2, out=two[PITCH:PITCH + CELL_H, :l2.shape[1]])
    mixed, _ = engine_line(sm, atlas, MIXED)

    # ตัวเลข
    tops, bots = [], []
    for k, s in data["cells"].items():
        ys = np.flatnonzero((cell_img(atlas, int(k, 16)) > 40).any(axis=1))
        if len(ys):
            tops.append(int(ys[0]) - BASELINE_Y)
            bots.append(int(ys[-1]) - BASELINE_Y)
    width = sum(engine_line(sm, atlas, t)[1] for t in texts)
    stroke = np.mean([stroke_width(cell_img(atlas, sm.base[c])) for c in "นมอกดบ"])
    stats = {"name": name, "ppem": title_encode.ppem(), "top": min(tops), "bottom": max(bots),
             "width_pct": 100.0 * width / base_width if base_width else 100.0, "width": width,
             "stroke_pct": 100.0 * stroke / EN_STROKE}
    title = "%s  |  top %d  bottom +%d  |  line length %.0f%%  |  stroke %.0f%% of EN" % (
        name, stats["top"], stats["bottom"], stats["width_pct"], stats["stroke_pct"])
    parts = [single, two, mixed]
    W = max(p.shape[1] for p in parts)
    rows = [label_img(title, max(W, 900))]
    W = max(W, 900)
    for p in parts:
        xs = np.flatnonzero((p > 16).any(axis=0))
        p = p[:, :xs[-1] + 8] if len(xs) else p
        rows.append(np.pad(p, ((0, 0), (0, W - p.shape[1]))))
    rows.append(np.full((3, W), 70, np.uint8))
    return rows, stats


def main():
    ap = argparse.ArgumentParser(description="เทียบฟอนต์ต้นแบบของกลิฟไทย")
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    texts = sample_texts()
    base_width = None
    all_stats = []
    for group, fonts in GROUPS.items():
        rows = []
        for name, ttf in fonts:
            if a.only and a.only.lower() not in name.lower() and ttf != paths.SARABUN_TTF:
                continue
            if not os.path.exists(ttf):
                print("!! ไม่พบ", ttf)
                continue
            try:
                sm, atlas, data = build_font(ttf)
            except AssertionError as e:          # render_glyph: กว้างเกินเซลล์แม้บีบ 15%
                print("%-40s ใช้ไม่ได้ — %s" % (name, e))
                continue
            if base_width is None:              # ตัวแรก = Sarabun Regular = ฐานเทียบความยาว
                base_width = sum(engine_line(sm, atlas, t)[1] for t in texts)
            r, st = block(name, sm, atlas, data, texts, base_width)
            rows += r
            all_stats.append(st)
            print("%-40s ppem %2d  top %4d  bottom +%2d  ความยาว %5.1f%%  เส้น %5.1f%%"
                  % (name, st["ppem"], st["top"], st["bottom"], st["width_pct"], st["stroke_pct"]))
        if not rows:
            continue
        W = max(r.shape[1] for r in rows)
        img = np.concatenate([np.pad(r, ((0, 0), (0, W - r.shape[1]))) for r in rows])
        out = OUT_DIR / (group + ".png")
        Image.fromarray(img).save(out)
        print("เขียน", out, img.shape)

    title_encode.THAI_TTF = paths.THAI_TTF
    title_encode._PPEM = None
    with io.open(OUT_DIR / "summary.md", "w", encoding="utf-8") as f:
        f.write("# เทียบฟอนต์ต้นแบบของกลิฟไทย\n\n> สร้างด้วย `python scripts/compare_fonts.py`\n\n")
        f.write("| ฟอนต์ | ppem | บนสุด | ล่างสุด | ความยาวบรรทัด (Sarabun = 100) | เส้น (% ของอังกฤษ) |\n")
        f.write("|---|---|---|---|---|---|\n")
        for st in all_stats:
            f.write("| %s | %d | %d | +%d | %.0f | %.0f |\n" % (
                st["name"], st["ppem"], st["top"], st["bottom"], st["width_pct"], st["stroke_pct"]))
    print("เขียน", OUT_DIR / "summary.md")


if __name__ == "__main__":
    main()
