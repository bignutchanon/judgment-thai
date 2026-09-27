#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""วาดการ์ดชื่อบท + การ์ดแนะนำตัวละครเป็นภาษาไทย (texture ใน ui.judge.en.par)

## ที่มา (research 27 ก.ย. 2026 — verify กับไฟล์จริงแล้ว)

การ์ด "Chapter 01 / Three Blind Mice" และการ์ด "LAWYER AT THE GENDA LAW OFFICE / ISSEI HOSHINO"
**ไม่ได้วาดด้วยฟอนต์** — ข้อความอบอยู่ในรูป DXT5 ของ `ui.judge.en.par/en/texture/`:

  การ์ดบท (scene `caption_chapter01..13_judge` เล่นทับวิดีโอควัน `chapter_sequence.usm` ใน movie.par)
    caption_chapter_judge_NN.dds      1024x256 · ครึ่งบน = ชื่อบทตัวทึบ · ครึ่งล่าง = ตัวเส้นขอบ (+128 px)
    caption_chapter_judge.dds         256x64   · ป้าย "Chapter" (บท 1-12 ใช้ร่วมกัน · ตัวเลขมาจาก num)
    caption_chapter_numNN_judge.dds   512x64   · ตัวเลข "01" · บท 13 เป็นป้าย "Final Chapter" ทั้งคำ
  ป้ายชื่อศัตรูตอนเริ่มต่อสู้ (scene `caption_judge` · caption.bin คอลัมน์ name_texture_id -> รูป · message = ข้อความ)
    bc_eb_*.dds  800x100  · บรรทัดเดียว ชิดขวา (หมึก EN y 24-75 · ขอบขวา x 777) · 32 ใบ
    bc_sb_*.dds  1000x200 · บรรทัดเดียวกลาง (y 74-125) หรือสองบรรทัด ตำแหน่ง (y 40-62) + ชื่อ (y 114-165) · 25 ใบ
                 · แสดงทั้งใบ (ไม่หั่นชิ้น) · ตัวขาว + แสงเรืองส้ม (255,110,0) อบในรูป:
                   ฟุ้ง = 0.9 x gauss(sigma 3) + 1.2 x gauss(sigma 11) · ขอบเข้ม = 0.3 x gauss(sigma 1) (fit กับ bc_eb_chinpira)
                 · ข้อความสองบรรทัดมาจาก message "ชื่อ, ตำแหน่ง" ของ caption.bin (type 11)
  ป้ายสถานที่/เวลาในคัตซีน (เช่น "Kamurocho Police Station Visitation Room")
    telop_<ฉาก>.dds  1920x120 · บรรทัดเดียว ชิดขวา (หมึก EN y 28-84 · ขอบขวา x ~1798) · 24 ใบ
                     · เงาดำฟุ้งอบในรูป = 2.0 x gauss(sigma 5) ไม่มี offset · ข้อความไม่มีในไฟล์เกม
                       -> `caption_cards.json` หัวข้อ telops
  การ์ดตัวละคร (scene `caption_character_<ชื่อ>`)
    caption_character_<ชื่อ>.dds     800/1000x360 · ชื่อทึบ (y 6-120) · ชื่อเส้นขอบ (+118)
                                      · ตำแหน่งทึบ (y 242-294) · ตำแหน่งเส้นขอบ (+62)
                                      · ตัวทึบมีเงา glow ดำอบในรูป (gaussian sigma 3 · เข้ม x1.5 ชื่อ / x2 ตำแหน่ง)
                                      · สี่เหลี่ยมขาวมุมขวาบนเป็นพิกเซลที่ texlist ใช้วาดเส้น — คัดลอกจากต้นฉบับเสมอ

`texlist/<scene>.bin` (ARMP) เก็บพิกัด UV ที่ scene ตัดไปใช้ — ตัวเส้นขอบถูกหั่นเป็นชิ้นตามตัวอักษร EN
(บท 1 = `T|hree B|lind M|ice`) เพื่อทำแอนิเมชันเผยทีละชิ้น ชิ้นที่ติดกันเป็น "กลุ่ม" และระหว่างกลุ่มมีช่องว่าง
(บท 1: x 405-416 และ 654-665) ที่ scene ไม่วาด → หมึกไทยที่ตกในช่องนี้จะหายไปตอนแอนิเมชัน
สคริปต์จึงตัดคำไทย (pythainlp) แล้ววางแต่ละช่วงให้อยู่ในกลุ่มของตัวเอง ช่องว่างระหว่างช่วงตกตรงช่องของ scene พอดี
แถวของ texlist ที่เป็นเลย์เอาต์ EN: การ์ดบท = แถว 3 · การ์ดตัวละคร = แถว 2 (แถวอื่นเป็นภาษาอื่น) — ตรวจซ้ำทุกครั้ง

ข้อความ: ชื่อบท + ชื่อตัวละครดึงจาก `translations/master_th.json` · ป้ายและตำแหน่งตัวละครอยู่ที่
`translations/caption_cards.json` (ไม่มีในไฟล์ข้อความของเกม) · ฟอนต์ `font/Taviraj-Regular.ttf` (OFL)
ขึ้นรูปไทยด้วย HarfBuzz (Pillow ไม่มี raqm) วาดกลิฟด้วย FreeType ที่ 4x แล้วย่อ · เขียน DXT5 ด้วย Pillow
(header/ขนาดไฟล์ตรงต้นฉบับ)

ใช้:
  python scripts/make_caption_cards.py              # พรีวิวอย่างเดียว -> build/preview/caption_cards/
  python scripts/make_caption_cards.py --write      # + เขียน build/ui/ui.judge.en/en/texture/*.dds
                                                    #   และ scene/caption_chapter01..12_judge.bin (เลื่อนเลขบท)
  python scripts/make_caption_cards.py --allow-cut  # ชื่อตัวละครตัวใหญ่ ยอมให้หมึกตกช่องว่างของชิ้นเส้นขอบ
  python scripts/make_caption_cards.py --chapter-safe  # ชื่อบทหลบช่องว่าง (ตัวเล็ก/เยื้อง/มีช่องกลางคำ)

ค่าเริ่มต้น (เลือกจากพรีวิว 27 ก.ย. 2026): ชื่อบท = กึ่งกลางขนาดเต็มแบบ EN ไม่หลบช่อง — รอยต่อชิ้นของ EN
ไม่ตรงคำไทย ถ้าหลบทุกช่องข้อความจะเยื้อง/เล็ก/มีรูกลางคำ (ผลกระทบของการไม่หลบ = ตัวเส้นขอบขาดเป็นเส้นบาง ๆ
เฉพาะช่วงแอนิเมชันเผยตัว แล้วตัวทึบทับเต็ม) · ชื่อตัวละคร = หลบช่อง (ตัดตรงวรรคชื่อ-นามสกุลอยู่แล้ว ได้ขนาดเต็มเกือบทุกคน)
deploy: `deploy_spoil.py` คัดลอก build/ui/ui.judge.en ทั้งโฟลเดอร์ -> mods (loose ผ่าน Parless)
⚠ ยังไม่ได้ยืนยันบนจอว่า Parless โหลด .dds loose จาก ui par ได้ (scene .bin จาก par เดียวกันยืนยันแล้ว)
"""
import argparse
import io
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
from itertools import combinations

import freetype
import numpy as np
import uharfbuzz as hb
from PIL import Image, ImageDraw
from scipy import ndimage, optimize

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths                                        # noqa: E402

UI_EN = paths.EXTRACTED / "ui_en" / "en"
SRC_TEX = UI_EN / "texture"
SRC_TL = UI_EN / "texlist"
OUT = paths.BUILD / "ui" / "ui.judge.en" / "en" / "texture"
SRC_SCENE = UI_EN / "scene"
OUT_SCENE = paths.BUILD / "ui" / "ui.judge.en" / "en" / "scene"
PREVIEW = paths.BUILD / "preview" / "caption_cards"
FONT = paths.FONT_DIR / "Taviraj-Regular.ttf"
CARDS = paths.TRANSLATIONS / "caption_cards.json"

SS = 4                 # supersample
OUTLINE_PX = 1.4       # ความหนาเส้นขอบ (EN ~1.5 px)
MARGIN = 3             # ระยะกันหมึกห่างขอบชิ้นเส้นขอบ
EN_ROW = {"chapter": "3", "character": "2"}

# บรรทัด "บทที่ 01" ของการ์ดบท (หน่วย UI 1600x900 · x = 0 คือกึ่งกลางจอ · 1 px ในรูปป้าย ~ 1 หน่วย UI)
# วัดจากภาพหน้าจอ 1080p (UI x1.2) + ค่าใน scene: หมึก "Chapter" x 8..190 ในรูป = UI -122..+60
# ป้าย (caption_chapter_judge.dds) ใช้ร่วมกันทุกบท ส่วนเลขเป็นสไปรต์ num_0 ของ scene แต่ละบท
# "บทที่" สั้นกว่า "Chapter" มาก ถ้าไม่ขยับเลข ทั้งกลุ่มจะเยื้องขวา ~55 หน่วย → เลื่อนเลข (แก้ col10 ของ num_0)
LABEL_TEX_TO_UI = -130      # x ในรูปป้าย -> x UI
NUM_X_EN = 70.0             # scene caption_chapterNN_judge.bin แถว num_0: col10 (x) · col11 = 1 · col38 = 69 (บท 1-12)
NUM_RECT_X0 = 298           # ขอบซ้ายช่องเลขในรูป caption_chapter_numNN_judge.dds (texlist แถว 1 ชิ้น 8 · กว้าง 69)
LABEL_DIGIT_GAP = 14        # ระยะหมึกป้าย -> หมึกเลข ของ EN (หน่วย UI)
SCENE_COLS = 121            # ตาราง node ของ scene UI (เหมือน pause_drone.bin)

# ---------------------------------------------------------------- เรนเดอร์


class Renderer:
    def __init__(self, path):
        self.face = hb.Face(hb.Blob.from_file_path(str(path)))
        self.font = hb.Font(self.face)
        self.upem = self.face.upem
        self.font.scale = (self.upem, self.upem)
        self.ft = freetype.Face(str(path))
        self.cache = {}
        buf = hb.Buffer()
        buf.add_str(" ")
        buf.guess_segment_properties()
        hb.shape(self.font, buf, {})
        self.space_em = buf.glyph_positions[0].x_advance / self.upem

    def seg(self, text, px):
        """คืน dict: mask (4x) · ink ซ้าย/ขวา/บน/ล่าง เทียบ origin/baseline หน่วย px จริง"""
        key = (text, px)
        if key in self.cache:
            return self.cache[key]
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.font, buf, {"kern": True, "liga": True})
        P = px * SS
        self.ft.set_pixel_sizes(0, P)
        sc = P / self.upem
        adv = sum(p.x_advance for p in buf.glyph_positions) * sc
        W, H = int(adv + P * 2), int(P * 3)
        ox, base = int(P * 0.5), int(P * 1.9)
        can = np.zeros((H, W), np.float32)
        x = float(ox)
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            self.ft.load_glyph(info.codepoint, freetype.FT_LOAD_NO_HINTING)
            self.ft.glyph.render(freetype.FT_RENDER_MODE_NORMAL)
            bm = self.ft.glyph.bitmap
            if bm.width and bm.rows:
                a = np.array(bm.buffer, np.uint8).reshape(bm.rows, bm.pitch)[:, : bm.width] / 255.0
                gx = int(round(x + pos.x_offset * sc)) + self.ft.glyph.bitmap_left
                gy = int(round(base - pos.y_offset * sc)) - self.ft.glyph.bitmap_top
                sub = can[gy: gy + bm.rows, gx: gx + bm.width]
                np.maximum(sub, a[: sub.shape[0], : sub.shape[1]], out=sub)
            x += pos.x_advance * sc
        ys, xs = np.nonzero(can > 0.02)
        x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
        mask = can[y0:y1, x0:x1]
        r = dict(mask=mask, w=(x1 - x0) / SS, above=(base - y0) / SS, below=(y1 - base) / SS)
        self.cache[key] = r
        return r


def disk(r):
    yy, xx = np.mgrid[-r: r + 1, -r: r + 1]
    return (xx * xx + yy * yy) <= r * r


def down(a):
    h, w = a.shape[0] // SS, a.shape[1] // SS
    return a[: h * SS, : w * SS].reshape(h, SS, w, SS).mean(axis=(1, 3))


def draw_line(R, W, H, segs, xs, baseline, px):
    """วางช่วงข้อความ (หมึกซ้ายสุดที่ xs[i]) บน baseline → (ทึบ, เส้นขอบ) ขนาดจริง WxH"""
    can = np.zeros((H * SS, W * SS), np.float32)
    for text, x in zip(segs, xs):
        s = R.seg(text, px)
        m = s["mask"]
        tx = int(round(x * SS))
        ty = int(round((baseline - s["above"]) * SS))
        sub = can[ty: ty + m.shape[0], tx: tx + m.shape[1]]
        np.maximum(sub, m[: sub.shape[0], : sub.shape[1]], out=sub)
    line = np.zeros_like(can)
    rows = np.nonzero(can.max(axis=1) > 0)[0]
    if len(rows):
        r = max(1, int(round(OUTLINE_PX * SS)))
        y0, y1 = max(0, rows[0] - r - 1), rows[-1] + r + 2
        er = ndimage.grey_erosion(can[y0:y1], footprint=disk(r))
        line[y0:y1] = np.clip(can[y0:y1] - er, 0, 1)
    return down(can), down(line)


# ---------------------------------------------------------------- จัดวาง


def tokens_of(text, override=None):
    """คืน (tokens, natural_space_after) — จุดตัดได้เฉพาะระหว่าง token"""
    if override:
        parts = override.split("|")
    else:
        from pythainlp.tokenize import word_tokenize
        parts = word_tokenize(text, engine="newmm", keep_whitespace=True)
    toks, spaces = [], []
    for p in parts:
        if p.strip() == "":
            if spaces:
                spaces[-1] = True
            continue
        toks.append(p)
        spaces.append(False)
    assert "".join(t + (" " if s else "") for t, s in zip(toks, spaces)).strip() == text.strip(), \
        f"ตัดคำแล้วประกอบกลับไม่ตรง: {toks}"
    return toks, spaces


def layout(R, text, groups, band, anchor, px_range, override=None, words_only=False, max_dev=60,
           max_gap=0.8, pull=0.3):
    """หา px ใหญ่สุด + จุดตัด + ตำแหน่ง ที่หมึกทุกช่วงอยู่ในกลุ่มชิ้นของตัวเอง
    groups = [(x0,x1)] ช่วงที่ scene วาด · band = (บน, ล่าง) ของหมึก · anchor = ("center"|"left"|"right", x)
    words_only = ตัดได้เฉพาะตรงช่องว่างเดิม (ชื่อคน) · max_dev = ยอมให้เยื้องจากเป้ากี่ px
    max_gap = ช่องที่เว้นเพิ่มได้ (เท่าของ px) · pull = น้ำหนักดึงเข้าเป้า เทียบกับความห่างของช่อง"""
    toks, spaces = tokens_of(text, override)
    cuts_all = [i for i in range(1, len(toks)) if (spaces[i - 1] or not words_only)]
    kind, target = anchor
    best_any = None
    for px in range(px_range[1], px_range[0] - 1, -1):
        whole = R.seg(text, px)
        if whole["above"] + whole["below"] > band[1] - band[0]:
            continue
        sp = R.space_em * px
        best = None
        for s in range(len(groups)):
            for k in range(1, min(len(groups) - s, len(toks)) + 1):
                gs = groups[s: s + k]
                for cuts in combinations(cuts_all, k - 1):
                    b = [0, *cuts, len(toks)]
                    segs, nat = [], []
                    for j in range(k):
                        seg = ""
                        for t in range(b[j], b[j + 1]):
                            seg += toks[t] + (" " if spaces[t] and t < b[j + 1] - 1 else "")
                        segs.append(seg)
                        nat.append(sp if spaces[b[j + 1] - 1] else 0.0)
                    ws = [R.seg(t, px)["w"] for t in segs]
                    lo = [g[0] + MARGIN for g in gs]
                    hi = [g[1] - MARGIN - w for g, w in zip(gs, ws)]
                    if any(h < l for l, h in zip(lo, hi)):
                        continue

                    def cost(x):
                        c = 0.0
                        for j in range(k - 1):
                            c += (x[j + 1] - x[j] - ws[j] - nat[j]) ** 2
                        if kind == "center":
                            c += pull * ((x[0] + x[-1] + ws[-1]) / 2 - target) ** 2
                        elif kind == "left":
                            c += pull * (x[0] - target) ** 2
                        else:
                            c += pull * (x[-1] + ws[-1] - target) ** 2
                        return c
                    x0 = [(l + h) / 2 for l, h in zip(lo, hi)]
                    r = optimize.minimize(cost, x0, bounds=list(zip(lo, hi)), method="L-BFGS-B")
                    xs = list(r.x)
                    gaps = [xs[j + 1] - xs[j] - ws[j] - nat[j] for j in range(k - 1)]
                    cand = (r.fun, px, segs, xs, gaps)
                    if best is None or cand[0] < best[0]:
                        best = cand
        if best is None:
            continue
        if best_any is None:
            best_any = best
        # ยอมรับเมื่อช่องที่ต้องเว้นเพิ่มไม่เกิน max_gap เท่าของขนาดตัวอักษร และตำแหน่งไม่หลุดเป้าเกิน max_dev
        _, _, segs, xs, gaps = best
        ws = [R.seg(t, px)["w"] for t in segs]
        pos = {"center": (xs[0] + xs[-1] + ws[-1]) / 2, "left": xs[0], "right": xs[-1] + ws[-1]}[kind]
        if max(gaps, default=0) <= max_gap * px and abs(pos - target) <= max_dev:
            return best, None
    if best_any is None:
        raise SystemExit(f"จัดวางไม่ได้: {text}")
    return best_any, "ใช้ตัวเลือกที่ดีที่สุดที่หาได้ (ช่องห่าง/เยื้องเกินเกณฑ์)"


def baseline_for(R, segs, px, band, prefer):
    above = max(R.seg(t, px)["above"] for t in segs)
    below = max(R.seg(t, px)["below"] for t in segs)
    return float(np.clip(prefer, band[0] + above, band[1] - below))


# ---------------------------------------------------------------- texlist


def decode_texlist(path, work):
    dst = os.path.join(work, os.path.basename(path))
    shutil.copyfile(path, dst)
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    subprocess.run([sys.executable, str(paths.REARMP), os.path.basename(dst)], cwd=work, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300, check=True)
    doc = json.load(io.open(dst + ".json", encoding="utf-8"))
    rows = {}
    for k, v in doc["0"][""]["1"].items():
        if not k.isdigit() or not v[""].get("1"):
            continue
        rows[k] = [(r[""]["1"], r[""]["2"], r[""]["3"], r[""]["4"]) for kk, r in v[""]["1"].items()
                   if kk.isdigit() and r[""]["reARMP_isValid"] == "1"]
    return rows


def chunk_groups(rows, tex_rgba, v_lo, v_hi, expect_row):
    """หาแถว EN (ชิ้นครอบหมึก EN ครบ) แล้วคืนกลุ่มชิ้นที่ติดกัน + ช่วง y ของแถบเส้นขอบ"""
    H, W = tex_rgba.shape[:2]
    ink = tex_rgba[..., 3] > 40
    best = None
    for k, rects in rows.items():
        ch = [r for r in rects if r[1] >= v_lo - 0.01 and r[3] <= v_hi + 0.01
              and (r[2] - r[0]) < 0.9 and (r[3] - r[1]) > 0.2]
        if not ch:
            continue
        y0, y1 = int(min(r[1] for r in ch) * H), int(max(r[3] for r in ch) * H)
        band = ink[y0:y1].any(0)
        cov = np.zeros(W, bool)
        for r in ch:
            cov[int(r[0] * W): int(np.ceil(r[2] * W))] = True
        score = (band & cov).sum() / max(1, band.sum())
        if best is None or score > best[0] + 1e-9 or (k == expect_row and score >= 0.99):
            best = (score, k, ch, (y0, y1))
        if k == expect_row and score >= 0.99:
            break
    score, k, ch, ys = best
    if k != expect_row or score < 0.99:
        print(f"  ⚠ แถว EN ของ texlist = {k} (คาด {expect_row}) coverage {score:.3f} — ตรวจด้วยตา")
    groups = []
    for a, b in sorted((r[0] * W, r[2] * W) for r in ch):
        if groups and a - groups[-1][1] <= 1.5:
            groups[-1][1] = max(groups[-1][1], b)
        else:
            groups.append([a, b])
    return [tuple(g) for g in groups], ch, ys


def en_ink(tex_rgba, y0, y1, white_only=False):
    a = tex_rgba[y0:y1, :, 3] > 40
    if white_only:
        a &= tex_rgba[y0:y1, :, :3].mean(-1) > 215
    ys, xs = np.nonzero(a)
    return xs.min(), xs.max() + 1, ys.min() + y0, ys.max() + 1 + y0


# ---------------------------------------------------------------- ประกอบรูป


def to_rgba(white, shadow=None):
    white = np.clip(white, 0, 1)
    if shadow is None:
        alpha, rgb = white, np.ones_like(white)
    else:
        alpha = white + np.clip(shadow, 0, 1) * (1 - white)
        rgb = np.where(alpha > 1e-4, white / np.maximum(alpha, 1e-4), 0)
    out = np.zeros(white.shape + (4,), np.uint8)
    out[..., :3] = np.clip(rgb * 255 + 0.5, 0, 255).astype(np.uint8)[..., None]
    out[..., 3] = np.clip(alpha * 255 + 0.5, 0, 255).astype(np.uint8)
    return out


def shift_rows(a, dy):
    out = np.zeros_like(a)
    if dy >= 0:
        out[dy:] = a[: a.shape[0] - dy]
    else:
        out[:dy] = a[-dy:]
    return out


def ink_outside(a, allowed_x, y_band, name):
    """เตือนเมื่อมีหมึกนอกกลุ่มชิ้น (ในแถบเส้นขอบ)"""
    H, W = a.shape
    ok = np.zeros(W, bool)
    for x0, x1 in allowed_x:
        ok[int(np.ceil(x0)): int(x1)] = True
    bad = a[y_band[0]: y_band[1], ~ok].max(initial=0)
    if bad > 0.05:
        print(f"  ⚠ {name}: หมึกตกช่องว่างของชิ้นเส้นขอบ (alpha {bad:.2f})")


def make_chapter(R, n, title, groups, tex, override, allow_cut):
    """ค่าเริ่มต้นหลบช่องว่างของชิ้นเส้นขอบ (ยอมเยื้องจากกึ่งกลางได้ถึง 100 px) · allow_cut = กึ่งกลางตัวใหญ่"""
    H, W = 256, 1024
    ex0, ex1, _, _ = en_ink(tex, 0, 128)
    g_use = [(groups[0][0], groups[-1][1])] if allow_cut else groups
    (cost, px, segs, xs, gaps), warn = layout(
        R, title, g_use, band=(6, 121), anchor=("center", (ex0 + ex1) / 2), px_range=(40, 84),
        override=None if allow_cut else override, max_dev=30 if allow_cut else 100)
    base = baseline_for(R, segs, px, (6, 121), prefer=92)
    solid, line = draw_line(R, W, H, segs, xs, base, px)
    white = solid.copy()
    white = np.maximum(white, shift_rows(line, 128))
    if not allow_cut:
        ink_outside(shift_rows(line, 128), groups, (128, 256), f"บท {n}")
    info = f"px {px} · ช่วง {' | '.join(segs)} · เว้นเพิ่ม {', '.join(f'{g:.0f}' for g in gaps) or '-'}"
    return to_rgba(white), info, warn


def make_label(R, text, tex, box, anchor, band, prefer, keep_from_x):
    H, W = tex.shape[:2]
    (cost, px, segs, xs, gaps), warn = layout(R, text, [box], band=band, anchor=anchor,
                                               px_range=(24, 56))
    base = baseline_for(R, segs, px, band, prefer)
    solid, _ = draw_line(R, W, H, segs, xs, base, px)
    out = to_rgba(solid)
    out[:, keep_from_x:] = tex[:, keep_from_x:]      # พิกเซลอรรถประโยชน์ของต้นฉบับ
    cols = np.nonzero(solid[:, :keep_from_x].max(axis=0) > 0.05)[0]
    return out, f"px {px}", warn, (int(cols.min()), int(cols.max()) + 1)


def digits_ink(num_rgba):
    """ช่วง x ของหมึกเลขบทในช่องเลข (ชิ้น 8 ของ texlist)"""
    a = num_rgba[:, NUM_RECT_X0: NUM_RECT_X0 + 70, 3] > 30
    xs = np.nonzero(a.any(axis=0))[0]
    return NUM_RECT_X0 + int(xs.min()), NUM_RECT_X0 + int(xs.max()) + 1


def patch_num_x(orig, data, new_x):
    """แก้ x (col10) ของแถว num_0 ในตาราง node ของ scene การ์ดบท — แก้ไบต์ในที่ 4 ไบต์
    วิธีเดียวกับ patch_drone_menu_titles.py (ตารางย่อย column-major · header = rows, cols, text_count ·
    +0x1C = ตัวชี้ไปอาร์เรย์ offset ของแต่ละคอลัมน์ · float 4 ไบต์ต่อแถว) · ยืนยันแถวด้วยค่าเดิม 3 คอลัมน์
    ในไฟล์ต้นฉบับ (`orig`) แล้วแก้บน `data` = ไฟล์ใน build ถ้ามี (สคริปต์ patch_* ตัวอื่นอาจแก้ scene
    เดียวกันไว้ก่อน เช่น patch_ui_tracking.py) — ต่อยอด ไม่ทับงานของสคริปต์อื่น"""
    base = bytes(data)
    data = bytearray(orig)
    hits = []
    i = -1
    while True:
        i = data.find(struct.pack("<2i", SCENE_COLS, 0), i + 1)
        if i < 0:
            break
        hdr = i - 4
        rows = struct.unpack_from("<i", data, hdr)[0]
        if not 0 < rows < 1000:
            continue
        try:
            p1c = struct.unpack_from("<i", data, hdr + 0x1C)[0]
            offs = struct.unpack_from("<%di" % SCENE_COLS, data, p1c)
        except struct.error:
            continue
        if any(not (0 < offs[c] < len(data) - 4 * rows) for c in (10, 11, 38)):
            continue
        for r in range(rows):
            def f(c):
                return struct.unpack_from("<f", data, offs[c] + 4 * r)[0]
            if f(10) == NUM_X_EN and f(11) == 1.0 and f(38) == 69.0:
                hits.append(offs[10] + 4 * r)
    if len(hits) != 1:
        raise SystemExit(f"หาแถว num_0 ใน scene ไม่ได้ (เจอ {len(hits)} แถว) — โครงไฟล์อาจเปลี่ยน ห้ามเขียน")
    assert len(base) == len(orig), "scene ใน build ขนาดไม่เท่าต้นฉบับ — มีคนสร้างไฟล์ใหม่แทนการแก้ในที่"
    out = bytearray(base)
    struct.pack_into("<f", out, hits[0], new_x)
    diff = [k for k, (a, b) in enumerate(zip(base, out)) if a != b]
    assert all(hits[0] <= k < hits[0] + 4 for k in diff)
    return bytes(out)


def chapter_card_preview(title, label, num, num_x, final=False):
    """ประกอบการ์ดบทตามเลย์เอาต์บนจอ (หน่วยพิกเซลของรูปชื่อบท 1024 กว้าง · กึ่งกลางจอ = x 508.8)"""
    def cx(u):
        return 508.8 + u * 1.2 / 1.195
    c = Image.new("RGBA", (1024, 214), (27, 23, 20, 255))
    top = 78
    if final:
        xs = np.nonzero(num[:, :470, 3].max(axis=0) > 30)[0]
        c.alpha_composite(Image.fromarray(num[:, :470]), (int(round(cx(0) - (xs.min() + xs.max()) / 2)), top - 70))
    else:
        c.alpha_composite(Image.fromarray(label[:, :240]), (int(round(cx(LABEL_TEX_TO_UI))), top - 70))
        c.alpha_composite(Image.fromarray(num[:, NUM_RECT_X0: NUM_RECT_X0 + 70]), (int(round(cx(num_x))), top - 70))
    arr = np.array(c)
    arr[top - 17: top - 16, :, :3] = (236, 227, 211)
    c = Image.fromarray(arr)
    c.alpha_composite(Image.fromarray(title[:128]), (0, top))
    d = ImageDraw.Draw(c)
    d.line([(509, 0), (509, 8)], fill=(201, 168, 108, 255))          # ขีดกึ่งกลางจอ (อ้างอิง)
    d.line([(509, 205), (509, 213)], fill=(201, 168, 108, 255))
    return c


def make_character(R, key, name, role, groups, tex, allow_cut):
    H, W = tex.shape[:2]
    nx0, _, _, _ = en_ink(tex, 0, 124, white_only=True)
    rx0, _, _, _ = en_ink(tex, 242, 300, white_only=True)
    g_use = [(groups[0][0], groups[-1][1])] if allow_cut else groups
    (c1, npx, nsegs, nxs, ngaps), w1 = layout(
        R, name, g_use, band=(10, 112), anchor=("left", nx0), px_range=(34, 80), words_only=True,
        max_dev=70, max_gap=1.6, pull=1.0)
    nbase = baseline_for(R, nsegs, npx, (10, 112), prefer=88)
    nsolid, nline = draw_line(R, W, H, nsegs, nxs, nbase, npx)
    # ชื่อไทยสั้นกว่า EN จึงอาจเลื่อนขวาเพื่อไม่ให้ช่องระหว่างชื่อ-นามสกุลโหว่ → ขอบซ้ายตำแหน่งตามชื่อ
    # (สองบรรทัดเป็นสไปรต์คนละตัวแต่ใช้จุดตั้งต้น x เดียวกัน: EN ชื่อ x 20 / ตำแหน่ง x 15 ในรูป)
    role_left = rx0 + max(0.0, nxs[0] - nx0)
    (c2, rpx, rsegs, rxs, _), w2 = layout(
        R, role, [(0, W - 10)], band=(246, 291), anchor=("left", role_left), px_range=(20, 44),
        words_only=True, override=role)
    rbase = baseline_for(R, rsegs, rpx, (246, 291), prefer=280)
    rsolid, rline = draw_line(R, W, H, rsegs, rxs, rbase, rpx)
    shadow = np.clip(ndimage.gaussian_filter(nsolid, 3) * 1.5, 0, 1)
    shadow[122:] = 0
    rs = np.clip(ndimage.gaussian_filter(rsolid, 3) * 2.0, 0, 1)
    rs[:238] = 0
    rs[300:] = 0
    shadow = np.maximum(shadow, rs)
    nl, rl = shift_rows(nline, 118), shift_rows(rline, 62)
    if not allow_cut:
        ink_outside(nl, groups, (124, 238), key)
    white = np.clip(nsolid + rsolid + nl + rl, 0, 1)
    out = to_rgba(white, shadow)
    out[0:20, W - 24:] = tex[0:20, W - 24:]           # สี่เหลี่ยมขาวมุมขวาบน
    info = f"ชื่อ px {npx} ({' | '.join(nsegs)}) · ตำแหน่ง px {rpx}"
    return out, info, w1 or w2


GLOW_RGB = np.array([255.0, 110.0, 0.0])


def glow_rgba(white):
    """ตัวขาว + ขอบเข้มบาง ๆ + แสงเรืองส้ม (โมเดลที่ fit กับรูปต้นฉบับ) · จางขอบรูป 8 px กันเส้นตัด"""
    ag = np.clip(0.9 * ndimage.gaussian_filter(white, 3) + 1.2 * ndimage.gaussian_filter(white, 11), 0, 1)
    ad = np.clip(0.3 * ndimage.gaussian_filter(white, 1), 0, 1)
    H, W = white.shape
    fy = np.clip(np.minimum(np.arange(H), H - 1 - np.arange(H)) / 8.0, 0, 1)[:, None]
    fx = np.clip(np.minimum(np.arange(W), W - 1 - np.arange(W)) / 8.0, 0, 1)[None, :]
    under = (ad + (1 - ad) * ag) * fy * fx
    A = white + (1 - white) * under
    C = white[..., None] * 255 + ((1 - white) * (1 - ad) * ag * fy * fx)[..., None] * GLOW_RGB
    rgb = C / np.maximum(A, 1e-4)[..., None]
    out = np.zeros((H, W, 4), np.uint8)
    out[..., :3] = np.clip(rgb + 0.5, 0, 255).astype(np.uint8)
    out[..., 3] = np.clip(A * 255 + 0.5, 0, 255).astype(np.uint8)
    return out


def en_lines(tex):
    """ช่วง y ของบรรทัดตัวขาวใน EN (ใช้แยกแบบบรรทัดเดียว/สองบรรทัด)"""
    g = (tex[..., :3].min(-1) > 225) & (tex[..., 3] > 230)
    rows = g.any(1)
    runs, s0 = [], None
    for i, x in enumerate(rows):
        if x and s0 is None:
            s0 = i
        if not x and s0 is not None:
            runs.append((s0, i - 1))
            s0 = None
    return [r for r in runs if r[1] - r[0] > 4]


def make_battle(R, text, tex):
    """ป้ายชื่อศัตรู: 800x100 ชิดขวา · 1000x200 กลาง (สองบรรทัดถ้า EN มีสองบรรทัด: ตำแหน่ง + ชื่อ)"""
    H, W = tex.shape[:2]
    white = np.zeros((H, W), np.float32)
    infos, warn_all = [], None

    def put(t, band, anchor, pxr, prefer):
        nonlocal white, warn_all
        (c, px, segs, xs, _), warn = layout(R, t, [(20, W - 20)], band=band, anchor=anchor,
                                            px_range=pxr, words_only=True, override=t)
        base = baseline_for(R, segs, px, band, prefer)
        solid, _ = draw_line(R, W, H, segs, xs, base, px)
        white = np.maximum(white, solid)
        infos.append(f"px {px}")
        warn_all = warn_all or warn

    if W == 800:
        put(text, (16, 86), ("right", 777), (30, 64), 70)
    elif len(en_lines(tex)) >= 2 and ", " in text:
        name, title = text.split(", ", 1)
        put(title, (26, 78), ("center", 500), (18, 32), 66)
        put(name, (98, 182), ("center", 500), (34, 70), 160)
    else:
        put(text, (52, 150), ("center", 500), (34, 70), 126)
    return glow_rgba(white), " · ".join(infos), warn_all


def make_telop(R, text, tex):
    """ป้ายสถานที่: ชิดขวาที่ x 1798 · เงาดำ gauss sigma 5 x2 (fit กับ telop_m01_02400) · จางขอบรูป 8 px"""
    H, W = tex.shape[:2]
    (c, px, segs, xs, _), warn = layout(R, text, [(20, W - 20)], band=(12, 106), anchor=("right", 1798),
                                        px_range=(30, 72), words_only=True, override=text)
    base = baseline_for(R, segs, px, (12, 106), 84)
    white, _ = draw_line(R, W, H, segs, xs, base, px)
    sh = np.clip(2.0 * ndimage.gaussian_filter(white, 5), 0, 1)
    fy = np.clip(np.minimum(np.arange(H), H - 1 - np.arange(H)) / 8.0, 0, 1)[:, None]
    fx = np.clip(np.minimum(np.arange(W), W - 1 - np.arange(W)) / 8.0, 0, 1)[None, :]
    return to_rgba(white, sh * fy * fx), f"px {px}", warn


# ---------------------------------------------------------------- พรีวิว


def panel(rgba, bg, label, rects=None):
    im = Image.fromarray(rgba, "RGBA")
    b = Image.new("RGBA", im.size, bg)
    b.alpha_composite(im)
    d = ImageDraw.Draw(b)
    if rects:
        for (x0, y0, x1, y1) in rects:
            d.rectangle([x0, y0, x1, y1], outline=(255, 70, 70, 255))
    d.text((4, 2), label, fill=(255, 200, 0, 255))
    return b


def sheet(pairs, path, scale):
    w = max(max(a.width, b.width) for a, b in pairs)
    h = sum(a.height + b.height + 12 for a, b in pairs)
    out = Image.new("RGBA", (w, h), (70, 70, 70, 255))
    y = 0
    for a, b in pairs:
        out.paste(a, (0, y))
        out.paste(b, (0, y + a.height + 2))
        y += a.height + b.height + 12
    out = out.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    out.convert("RGB").save(path)


def save_dds(rgba, path):
    Image.fromarray(rgba, "RGBA").save(path, pixel_format="DXT5")


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="เขียน .dds ลง build/ui/ui.judge.en/en/texture")
    ap.add_argument("--allow-cut", action="store_true",
                    help="ชื่อตัวละครตัวใหญ่ ไม่หลบช่องว่างของชิ้นเส้นขอบ (ต้องดูแอนิเมชันในเกม)")
    ap.add_argument("--chapter-safe", action="store_true",
                    help="ชื่อบทหลบช่องว่างของชิ้นเส้นขอบ (ค่าเริ่มต้น = กึ่งกลางขนาดเต็มแบบ EN)")
    ap.add_argument("--only", help="ทำเฉพาะ key นี้ เช่น chapter01 / hoshino / bc_eb_chinpira / battle / telop")
    args = ap.parse_args()

    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    cards = json.load(io.open(CARDS, encoding="utf-8"))

    def th(en):
        v = master.get(en)
        v = v.get("th", v) if isinstance(v, dict) else v
        if not v:
            raise SystemExit(f"ไม่มีคำแปลใน master: {en!r}")
        return v

    R = Renderer(FONT)
    PREVIEW.mkdir(parents=True, exist_ok=True)
    if args.write:
        OUT.mkdir(parents=True, exist_ok=True)
    work = tempfile.mkdtemp(prefix="jeth_caption_")
    outputs, warns, scenes, card_pairs = [], [], [], []
    nums = {n: np.array(Image.open(SRC_TEX / f"caption_chapter_num{n:02d}_judge.dds").convert("RGBA"))
            for n in range(1, 14)}
    ch_pairs, char_pairs = [], []
    tc = json.load(io.open(paths.DB_EN / "en" / "title_movie_chapter.bin.json", encoding="utf-8"))

    def emit(fname, rgba):
        outputs.append((fname, rgba))

    # ---- การ์ดบท
    for n in range(1, 14):
        key = f"chapter{n:02d}"
        if args.only and args.only != key:
            continue
        en_full = list(tc[str(n)].values())[0]["name"]
        title = th(en_full).split(":", 1)[1].strip()
        tname = f"caption_chapter_judge_{n:02d}.dds"
        tex = np.array(Image.open(SRC_TEX / tname).convert("RGBA"))
        rows = decode_texlist(SRC_TL / f"caption_chapter{n:02d}_judge.bin", work)
        groups, ch, ys = chunk_groups(rows, tex, 0.5, 1.0, EN_ROW["chapter"])
        rgba, info, warn = make_chapter(R, n, title, groups, tex,
                                        cards.get("chapter_breaks", {}).get(str(n)),
                                        allow_cut=not args.chapter_safe)
        print(f"{key}: {title} · {info}" + (f" · ⚠ {warn}" if warn else ""))
        if warn:
            warns.append(f"{key}: {warn}")
        emit(tname, rgba)
        rects = [(r[0] * 1024, r[1] * 256, r[2] * 1024, r[3] * 256) for r in ch]
        ch_pairs.append((panel(tex, (38, 28, 22, 255), f"{key} EN"),
                         panel(rgba, (38, 28, 22, 255), f"{key} TH", rects)))

    if not args.only or args.only == "labels":
        tex = np.array(Image.open(SRC_TEX / "caption_chapter_judge.dds").convert("RGBA"))
        label_en = tex
        # จัด "บทที่ 01" ทั้งกลุ่มให้อยู่กึ่งกลาง: วางป้ายตามความกว้างเลขเฉลี่ย แล้วให้เลขของแต่ละบท
        # ตามหลังป้ายด้วยระยะเท่า EN (แก้ x ของ num_0 ใน scene บท 1-12)
        dig = {n: digits_ink(a) for n, a in nums.items() if n <= 12}
        wd = float(np.mean([b - a for a, b in dig.values()]))
        _, _, _, (l0, l1) = make_label(R, cards["chapter_label"], tex, (6, 225), ("left", 60),
                                       band=(2, 47), prefer=46, keep_from_x=240)
        start_ui = -((l1 - l0) + LABEL_DIGIT_GAP + wd) / 2
        rgba, info, warn, (l0, l1) = make_label(
            R, cards["chapter_label"], tex, (6, 225), ("left", start_ui - LABEL_TEX_TO_UI),
            band=(2, 47), prefer=46, keep_from_x=240)
        label_th = rgba
        label_end = l1 + LABEL_TEX_TO_UI
        num_x = {n: float(round(label_end + LABEL_DIGIT_GAP - (dig[n][0] - NUM_RECT_X0), 1)) for n in dig}
        mids = [((l0 + LABEL_TEX_TO_UI) + (num_x[n] + dig[n][1] - NUM_RECT_X0)) / 2 for n in dig]
        print(f"ป้ายบท: {cards['chapter_label']} · {info} · หมึกป้าย x {l0}-{l1} ในรูป · "
              f"เลข num_0 x {NUM_X_EN:.0f} -> {min(num_x.values())}..{max(num_x.values())} · "
              f"กึ่งกลางกลุ่ม {min(mids):+.1f}..{max(mids):+.1f} หน่วย UI จากกลางจอ")
        emit("caption_chapter_judge.dds", rgba)
        for n in num_x:
            sname = f"caption_chapter{n:02d}_judge.bin"
            src_b = io.open(SRC_SCENE / sname, "rb").read()
            built = OUT_SCENE / sname
            base_b = io.open(built, "rb").read() if built.exists() else src_b
            scenes.append((sname, patch_num_x(src_b, base_b, num_x[n])))
        ch_pairs.append((panel(tex, (38, 28, 22, 255), "label EN"),
                         panel(rgba, (38, 28, 22, 255), "label TH")))
        tex = np.array(Image.open(SRC_TEX / "caption_chapter_num13_judge.dds").convert("RGBA"))
        ex0, ex1, _, _ = en_ink(tex[:, :470], 0, 64)
        rgba, info, warn, _ = make_label(R, cards["final_chapter_label"], tex, (3, 468),
                                      ("center", (ex0 + ex1) / 2), band=(2, 46), prefer=44,
                                      keep_from_x=470)
        print(f"ป้ายบทสุดท้าย: {cards['final_chapter_label']} · {info}")
        emit("caption_chapter_num13_judge.dds", rgba)
        num13_th = rgba
        # การ์ดเต็มใบตามเลย์เอาต์บนจอ EN เทียบ TH — ดูว่า "บทที่ 01" อยู่กึ่งกลาง
        th_titles = {f: a for f, a in outputs}
        for n in range(1, 14):
            f = f"caption_chapter_judge_{n:02d}.dds"
            if f not in th_titles:
                continue
            en_t = np.array(Image.open(SRC_TEX / f).convert("RGBA"))
            fin = n == 13
            card_pairs.append((
                panel(np.array(chapter_card_preview(en_t, label_en, nums[n], NUM_X_EN, fin)), (0, 0, 0, 0), f"ch{n:02d} EN"),
                panel(np.array(chapter_card_preview(th_titles[f], label_th, num13_th if fin else nums[n],
                                                    num_x.get(n, 0.0), fin)), (0, 0, 0, 0), f"ch{n:02d} TH")))
        ch_pairs.append((panel(tex, (38, 28, 22, 255), "num13 EN"),
                         panel(rgba, (38, 28, 22, 255), "num13 TH")))

    # ---- ป้ายชื่อศัตรูตอนเริ่มต่อสู้ (bc_*.dds)
    cap = json.load(io.open(paths.DB_EN / "en" / "caption.bin.json", encoding="utf-8"))
    cap_msg = {}
    for k, v in cap.items():
        if k.isdigit():
            n = list(v.keys())[0]
            cap_msg.setdefault(n, v[n].get("message"))
    over = {k: v for k, v in cards.get("battle_overrides", {}).items() if not k.startswith("_")}
    bc_pairs = []
    for f in sorted(SRC_TEX.glob("bc_*.dds")):
        key = f.stem
        if args.only and args.only not in (key, "battle"):
            continue
        if key in over:
            text = over[key]["th"]
        else:
            text = th(cap_msg.get(key) or "")
        tex = np.array(Image.open(f).convert("RGBA"))
        rgba, info, warn = make_battle(R, text, tex)
        print(f"{key}: {text} · {info}" + (f" · ⚠ {warn}" if warn else ""))
        if warn:
            warns.append(f"{key}: {warn}")
        emit(f.name, rgba)
        bc_pairs.append((panel(tex, (58, 60, 68, 255), f"{key} EN"), panel(rgba, (58, 60, 68, 255), f"{key} TH")))

    # ---- ป้ายสถานที่/เวลาในคัตซีน (telop_*.dds)
    tl_pairs = []
    for key, t in cards.get("telops", {}).items():
        if key.startswith("_") or (args.only and args.only not in (key, "telop")):
            continue
        tex = np.array(Image.open(SRC_TEX / f"{key}.dds").convert("RGBA"))
        rgba, info, warn = make_telop(R, t["th"], tex)
        print(f"{key}: {t['th']} · {info}" + (f" · ⚠ {warn}" if warn else ""))
        if warn:
            warns.append(f"{key}: {warn}")
        emit(f"{key}.dds", rgba)
        crop = (slice(None), slice(560, 1920))
        tl_pairs.append((panel(np.ascontiguousarray(tex[crop]), (80, 92, 100, 255), f"{key} EN"),
                         panel(np.ascontiguousarray(rgba[crop]), (80, 92, 100, 255), f"{key} TH")))

    # ---- การ์ดตัวละคร
    for key, c in cards["characters"].items():
        if args.only and args.only != key:
            continue
        name = th(c["name"])
        role = cards["roles"][c["role"]]
        tname = f"caption_character_{key}.dds"
        tex = np.array(Image.open(SRC_TEX / tname).convert("RGBA"))
        rows = decode_texlist(SRC_TL / f"caption_character_{key}.bin", work)
        groups, ch, ys = chunk_groups(rows, tex, 0.3444, 0.6611, EN_ROW["character"])
        rgba, info, warn = make_character(R, key, name, role, groups, tex, args.allow_cut)
        print(f"{key}: {name} / {role} · {info}" + (f" · ⚠ {warn}" if warn else ""))
        if warn:
            warns.append(f"{key}: {warn}")
        emit(tname, rgba)
        H, W = tex.shape[:2]
        rects = [(r[0] * W, r[1] * H, r[2] * W, r[3] * H) for r in ch]
        char_pairs.append((panel(tex, (120, 100, 85, 255), f"{key} EN"),
                           panel(rgba, (120, 100, 85, 255), f"{key} TH", rects)))

    shutil.rmtree(work, ignore_errors=True)
    suffix = "_allowcut" if args.allow_cut else ""
    if card_pairs:
        sheet(card_pairs, PREVIEW / "chapter_cards.png", 0.6)
    for i in range(0, len(tl_pairs), 12):
        sheet(tl_pairs[i: i + 12], PREVIEW / f"telop_{i // 12 + 1}.png", 0.6)
    for i in range(0, len(bc_pairs), 10):
        sheet(bc_pairs[i: i + 10], PREVIEW / f"battle_{i // 10 + 1}.png", 0.7)
    if ch_pairs:
        sheet(ch_pairs, PREVIEW / ("chapters_safe.png" if args.chapter_safe else "chapters.png"), 0.6)
    if char_pairs:
        for i in range(0, len(char_pairs), 8):
            sheet(char_pairs[i: i + 8], PREVIEW / f"characters{suffix}_{i // 8 + 1}.png", 0.75)
    for fname, rgba in outputs:
        Image.fromarray(rgba, "RGBA").save(PREVIEW / (fname[:-4] + suffix + ".png"))
        if args.write:
            save_dds(rgba, OUT / fname)
            src = SRC_TEX / fname
            assert (OUT / fname).stat().st_size == src.stat().st_size, f"ขนาด dds ไม่ตรงต้นฉบับ: {fname}"
    if args.write and scenes:
        OUT_SCENE.mkdir(parents=True, exist_ok=True)
        for sname, blob in scenes:
            io.open(OUT_SCENE / sname, "wb").write(blob)
        print(f"เขียน scene {len(scenes)} ไฟล์ (num_0 x) -> {OUT_SCENE}")
    print(f"\nพรีวิว: {PREVIEW}")
    if args.write:
        print(f"เขียน {len(outputs)} ไฟล์ -> {OUT}")
    if warns:
        print("\n⚠ ต้องดูด้วยตา:\n  " + "\n  ".join(warns))


if __name__ == "__main__":
    main()
