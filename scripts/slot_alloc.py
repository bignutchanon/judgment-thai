#!/usr/bin/env python3
"""Slot allocator — จัดสรรเซลล์ของ `meta_ot_cond_book.dds` ให้ข้อความไทยทั้งเกม

## สถาปัตยกรรมรอบ 16 (22 ส.ค. 2026) — หนึ่งตัวอักษร หนึ่งเซลล์

เดิมโปรเจกต์นี้ต้อง **pre-compose** ฐาน+สระ+วรรณยุกต์ให้เป็นกลิฟเดียวต่อเซลล์ เพราะเชื่อว่า
advance ของทุกเซลล์ถูกล็อกไว้ในตารางใน `Judgment.exe` (แก้ไม่ได้ ไม่มีเซลล์ไหน advance = 0)
ข้อเชื่อนั้น **ผิด** — ตารางอยู่ใน `db.judge.en.par → en/font.bin → kerning_table` ซึ่งเราแก้ได้
(ดูที่มา สูตร และหลักฐานทั้งหมดใน `scripts/font_metrics.py`)

ผลคือระบบง่ายลงมากและได้คุณภาพดีกว่าเดิมทั้งสองด้าน:

  * **มาร์กได้ advance = 0** และเลื่อนซ้ายไปทับฐานได้ → สระ/วรรณยุกต์ซ้อนจริง เลิกแตกคลัสเตอร์
  * **ฐานได้ advance = ความกว้าง ink จริง + side bearing** → ไม่มีเพดาน 36 px อีกต่อไป

สิ่งที่ยังต้องจัดสรร (เพราะเซลล์ยังจำกัด) คือ **variant ของมาร์ก**: ตำแหน่งที่มาร์กต้องเลื่อนซ้าย
ขึ้นกับความกว้างของฐานตัวก่อนหน้า และความสูงขึ้นกับว่าฐานสูงไหม/มีสระบนซ้อนอยู่แล้วไหม
เซลล์เดียวจำค่าได้ค่าเดียว จึงต้องทำหลาย variant แล้วให้ตัว encode เลือกให้ตรงบริบท:

  * `wclass` — ชั้นของฐานตัวก่อนหน้า (ค่าเริ่มต้น 5 ชั้น) · ตั้งแต่ 28 ก.ย. 2026 แบ่งตาม **ตำแหน่งมาร์ก
    ที่ฟอนต์ต้นแบบตั้งไว้** (GPOS ผ่าน HarfBuzz · `mark_anchor.py` · ฐานเก็บชั้นไว้ที่ `mclass`) ไม่ใช่
    ความกว้าง — ฟอนต์ไทยวางสระบน/วรรณยุกต์ชิดขวา การวางกึ่งกลางแบบเดิมทำให้ ่ ลอยกลาง ี (ที่ นี่)
  * `hlevel` — ชั้นความสูง: 0 ปกติ · 1 วรรณยุกต์ที่ต้องซ้อนเหนือสระบนอีกที (เช่น ที่ ปื้ ญี่)

ใช้:
  python scripts/slot_alloc.py                 # รายงานอย่างเดียว (ไม่เขียนไฟล์)
  python scripts/slot_alloc.py --write         # เขียน translations/slotmap.json + รายงาน
  python scripts/slot_alloc.py --wclass 6      # เพิ่มชั้นความกว้างของมาร์ก (ถ้าเซลล์เหลือพอ)
"""
import argparse
import io
import json
import re
import os
import sys
from collections import Counter, OrderedDict

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6 — console Windows = cp1252
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
import font_metrics as FM
from title_slotmap import CELL_H, CELL_W, INKED_EXTA, INKED_LATIN1, cell_xy

SLOTMAP = paths.TRANSLATIONS / "slotmap.json"
WIDTHS_FILE = paths.TRANSLATIONS / "donor_widths.json"   # advance เดิมของ donor (ใช้แค่รายงาน/probe)
UNIQUE_STRINGS = paths.EXTRACTED / "unique_strings.json"  # ผลจาก extract_all_en.py

# ---------------------------------------------------------------- ไทย ----
UPPER = set("ัิีึื็ํ๎")
TONE = set("่้๊๋์")
LOWER = set("ฺุู")
COMBINING = UPPER | TONE | LOWER
THAI_LO, THAI_HI = "฀", "๿"

INK_X0 = 2                # ขอบซ้ายของ ink ในเซลล์ (px) — ทุกกลิฟวาดเริ่มที่นี่เสมอ
N_WCLASS = 5              # ชั้นความกว้างของฐาน ที่มาร์กต้องมี variant ตาม
TONE_BEARERS = "ัิีึืํ"    # สระบนที่วรรณยุกต์ซ้อนทับได้ — ความสูงสูงสุดของชุดนี้ = ที่ที่กันไว้ให้สระบน
                          # ตอนยกวรรณยุกต์ขึ้นชั้น hlevel 1 (เดิมค่าคงที่ 12 px — คิดจากกลิฟจริงตั้งแต่
                          # 27 ก.ย. 2026 เพราะมาร์กถูกย่อด้วย title_encode.MARK_SCALE)
LOWER_GAP = 1             # ระยะจากเส้นฐานถึงสระล่าง (px) — เดิม 2 · ลดเพื่อไม่ให้ ุ ู ชนบรรทัดถัดไป

# หมายเหตุ: **ไม่ยกมาร์กขึ้นเมื่อฐานเป็นตัวสูง** (ป ฝ ฟ) — หางสูงอยู่ขวา ฟอนต์ไทยจึงเลื่อนมาร์ก
# ไปทางซ้ายแทน (ชั้น mclass ของตัวพวกนี้ได้ค่านั้นจาก GPOS อัตโนมัติ) · เคยลองยกขึ้นแล้วมาร์กชนขอบบน
# ของเซลล์จนถูกตัด เพราะเหนือเส้นฐานมีที่แค่ 44 px

MARKS_PER_CELL = 0        # เลิกใช้ (คงไว้ให้สคริปต์เก่าอ่านค่าได้) — หนึ่งตัวอักษรหนึ่งเซลล์แล้ว

# ---------------------------------------------------------------- sentinel ----
# เซลล์ "ตัวนำ" — กลิฟว่าง advance 0 ที่แทรกไว้หน้าอักษรไทยทุกช่วง
#
# ทำไมต้องมี (พบ 29 ส.ค. 2026 จากภาพเมนูโดรนของผู้ใช้): UI บางจอไม่ได้วาดด้วย
# `meta_ot_cond_book` แต่วาดด้วยฟอนต์ bitmap `yakuza` (`data/font.judge/en/yakuza.dds`
# 256x512 · cell 16x32 · 225 กลิฟ = cp U+0020-U+0100) ซึ่งมีอักษร Latin-1 ครบ
# → เซลล์ donor ของเราในช่วง U+00C0-U+00FF ออกมาเป็น "À È Ú Á" ตัวใหญ่บนจอ
#
# เอนจิ้นมีลูกเล่นช่วย: **พอเจอ codepoint แรกที่ฟอนต์นั้นไม่มี มันจะสลับไปวาดด้วย
# `meta_ot_cond_book` แล้ววาดด้วยฟอนต์นั้นต่อจนจบสตริง** (ยืนยันจากภาพ: ตัวที่อยู่หลัง
# มาร์กตัวแรกออกมาเป็นไทยถูกต้องหมด ทั้งที่เป็น donor ที่ `yakuza` มีกลิฟ)
# → แทรก cp ที่ **ไม่มีในฟอนต์อื่นแต่มีในตารางของ meta** ไว้หน้าช่วงไทย = บังคับสลับฟอนต์
#   ตั้งแต่ตัวแรก ข้อความไทยจึงถูกวาดด้วย atlas ของเราเสมอ ไม่ว่าจอนั้นตั้งฟอนต์อะไรไว้
#
# เลือก U+0165: เกิน 225 กลิฟของ `yakuza` (จึงไม่มีวันชนกับกลิฟจริงของฟอนต์นั้น) ·
# ไม่มีใน `tbgm_0p_ja` (ตรวจแล้ว ไม่มี Latin Ext-A เลย) · ยังอยู่ในตาราง 332 แถวของ
# `kerning_table` (แถว 325) จึงมี advance ให้ตั้งเป็น 0 ได้ · ข้อความอังกฤษของเกมไม่ใช้
SENTINEL_CP = 0x0165


def is_thai(ch):
    return THAI_LO <= ch <= THAI_HI


# สระอำ: แตกเป็น นิคหิต (มาร์ก advance 0 ซ้อนเหนือฐาน) + สระอา (ฐาน) — ข้อเสนอเจ้าของโปรเจกต์ 5 ก.ย. 2026
# เพราะเซลล์ ำ ตัวเดียววาดวงกลมไว้ซ้ายสุดของกลิฟ จึงไปโผล่หลัง advance ของพยัญชนะ = "อ ำ" ห่างกัน
# วรรณยุกต์ที่นำหน้า ำ ในยูนิโค้ด (น้ำ = น ้ ำ) ย้ายไปหลังนิคหิต (น ํ ้ า) ให้ตัว encode ยกวรรณยุกต์
# ขึ้นชั้น hlevel 1 เหนือวงกลมเหมือนกรณี ที่/ปื้
RE_AM_TONE = re.compile("([่-๋])ำ")
RE_AM_BACK = re.compile("ํ([่-๋])?า")


def decompose_am(text):
    return RE_AM_TONE.sub("ํ\\1า", text).replace("ำ", "ํา")


def recompose_am(text):
    return RE_AM_BACK.sub(lambda m: (m.group(1) or "") + "ำ", text)


def kind_of(ch):
    if ch in TONE:
        return "tone"
    if ch in UPPER:
        return "upper"
    if ch in LOWER:
        return "lower"
    return "base"


def segment(text, marks_per_cell=None):
    """แบ่งข้อความเป็นคลัสเตอร์ 'ฐาน + มาร์กที่เกาะอยู่' — ใช้สำหรับรายงาน/สถิติเท่านั้น

    ตั้งแต่รอบ 16 การเรนเดอร์ไม่ได้ใช้คลัสเตอร์แล้ว (หนึ่งตัวอักษรหนึ่งเซลล์)
    """
    cells = []
    for ch in text:
        if ch in COMBINING and cells and is_thai(cells[-1][0]) and cells[-1][0] not in COMBINING:
            cells[-1] += ch
        else:
            cells.append(ch)
    return cells


def clusters(text, max_marks=None):
    return segment(text)


def thai_cells(text, marks_per_cell=None):
    """เฉพาะคลัสเตอร์ที่มีอักษรไทย (ASCII ไม่กินโควตา)"""
    return [c for c in segment(text) if is_thai(c[0])]


# ------------------------------------------------------------ donor pool ----
# ตารางเซลล์ = U+0000-007F (ASCII — เกมใช้เขียนอังกฤษ ห้ามแตะ) ต่อด้วย U+00A0-019F
# แต่ `kerning_table` มีแค่ 332 แถว = cell 0..331 = **ถึง U+016B เท่านั้น**
# เซลล์ที่เกินนั้นไม่มีแถวในตาราง เอนจิ้นจึงวาดเป็นกล่องเปล่า (อาการ tofu ของ Latin Ext-B
# ที่เจอรอบ 13 — สาเหตุจริงคือตรงนี้ ไม่ใช่ atlas)
TIER_ORDER = ["latin1_letter", "exta", "latin1_symbol", "extb", "control"]

TIERS = {
    "latin1_letter": [cp for cp in range(0xC0, 0x100)],
    "exta": [cp for cp in range(0x100, 0x180)],
    "extb": [cp for cp in range(0x180, 0x1A0)],
    "latin1_symbol": [cp for cp in range(0xA0, 0xC0)],
    "control": [cp for cp in range(0x01, 0x20) if cp not in (0x09, 0x0A, 0x0D)] + [0x7F],
}
DEFAULT_TIERS = ["latin1_letter", "exta", "latin1_symbol"]

INKED = set(INKED_LATIN1) | set(INKED_EXTA)   # เซลล์ที่มีหมึกเดิม (ใช้ตอน probe เท่านั้น)


def en_used_codepoints(path=UNIQUE_STRINGS):
    """codepoint ในช่วง pool ที่ **ข้อความอังกฤษของเกมใช้อยู่จริง** -> ห้ามเอาไปเป็น donor"""
    if not path.exists():
        return {}, False
    data = json.load(io.open(path, encoding="utf-8"))
    used = Counter()
    where = {}
    for s, meta in data.items():
        for ch in set(s):
            cp = ord(ch)
            if 0xA0 <= cp <= 0x19F:
                used[cp] += meta["count"]
                where.setdefault(cp, set()).update(meta["bins"])
    return {cp: (n, sorted(where[cp])) for cp, n in used.items()}, True


def th_used_codepoints(names=None):
    """codepoint ในช่วง pool ที่ **คำแปลไทย** ใช้อยู่ (° × ½ é ฯลฯ ที่ปนมากับประโยคไทย)"""
    used = Counter()
    sources = OrderedDict(CORPORA)
    if paths.MASTER_TH.exists():
        sources["jeth"] = str(paths.MASTER_TH)
    for name, path in sources.items():
        if names and name not in names:
            continue
        p = paths.Path(path)
        if not p.exists():
            continue
        for v in json.load(io.open(p, encoding="utf-8")).values():
            if not isinstance(v, str) or not any(is_thai(c) for c in v):
                continue
            for ch in set(v):
                cp = ord(ch)
                if 0xA0 <= cp <= 0x19F:
                    used[cp] += 1
    return dict(used)


def build_pool(tiers=DEFAULT_TIERS, reserved=()):
    """donor cp ที่ใช้ได้ เรียงตามชั้น — ตัดตัวที่เกิน 332 แถวของ kerning_table ออกเสมอ"""
    reserved = set(reserved)
    pool = []
    for t in tiers:
        pool += [cp for cp in TIERS[t] if cp not in reserved and FM.in_table(cp)]
    assert len(pool) == len(set(pool))
    return pool


def tier_of(cp):
    for t in TIER_ORDER:
        if cp in TIERS[t]:
            return t
    return "ascii"


# --------------------------------------------------------------- widths ----
def atlas_ink_widths():
    """ความกว้าง ink เดิมของเซลล์ที่มีหมึกใน atlas ต้นฉบับ (px) — ใช้ตอน probe เท่านั้น"""
    import numpy as np
    from bc4_codec import decode_bc4
    from title_slotmap import ATLAS_H, ATLAS_W
    src = paths.EXTRACTED / "font" / "meta_ot_cond_book.dds"
    atlas = decode_bc4(src.read_bytes()[128:], ATLAS_W, ATLAS_H)
    out = {}
    for cp in sorted(INKED):
        x0, y0 = cell_xy(cp)
        cell = atlas[y0:y0 + CELL_H, x0:x0 + CELL_W]
        xs = np.where((cell > 16).any(axis=0))[0]
        if len(xs):
            out[cp] = int(xs.max() - xs.min() + 1)
    return out


def donor_widths():
    """{cp: (advance_px, source)} — advance **เดิม** ของ donor (ก่อนเราเขียนทับตาราง)

    ตั้งแต่รอบ 16 ค่านี้ไม่ได้ใช้จัดสรรอีกแล้ว (เราตั้ง advance เองได้) เก็บไว้เพื่อรายงาน
    และเพื่อสคริปต์ probe ที่ยังอ้างถึง
    """
    if WIDTHS_FILE.exists():
        data = json.load(io.open(WIDTHS_FILE, encoding="utf-8"))
        prov = set(data.get("provisional_extA_default", [])) | set(data.get("provisional_from_ink", []))
        return {int(k, 16): (int(v), "provisional" if k in prov else "measured")
                for k, v in data.get("widths", {}).items()}
    return {cp: (v + 6, "est_from_ink") for cp, v in atlas_ink_widths().items()}


# --------------------------------------------------------------- ความต้องการ ----
CORPORA = OrderedDict([
    ("k3",     "D:/Projects/yakuza-kiwami-3/translations/master_th.json"),
    ("gaiden", "D:/Projects/yakuza-gaiden/translations/master_th.json"),
    ("y6",     "D:/Projects/yakuza-6-thai/translations/master_th.json"),
])

THAI_CONSONANTS = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
THAI_STANDALONE = "เแโใไาะๅๆฯฤฦ"        # ำ ไม่ต้องมีเซลล์แล้ว (แตกเป็น ํ + า เสมอ)        # สระ/สัญลักษณ์ที่กินที่แนวนอนเหมือนฐาน
THAI_MARKS = "".join(sorted(COMBINING))
MANDATORY = [c for c in THAI_CONSONANTS + THAI_STANDALONE] + list(THAI_MARKS)


def load_corpora(names=None, self_weight=3):
    """คืน (Counter ของตัวอักษรไทยรายตัว, Counter ของคู่ (ฐาน,มาร์ก), สถิติต่อคลัง)"""
    chars = Counter()
    pairs = Counter()          # (ความกว้างฐาน, มาร์ก) -> ความถี่ ใช้ตั้งชั้นความกว้าง
    stats = OrderedDict()
    sources = OrderedDict(CORPORA)
    if paths.MASTER_TH.exists():
        sources["jeth"] = str(paths.MASTER_TH)
    for name, path in sources.items():
        if names and name not in names:
            continue
        p = paths.Path(path)
        if not p.exists():
            stats[name] = {"strings": 0, "note": "ไม่พบไฟล์"}
            continue
        data = json.load(io.open(p, encoding="utf-8"))
        vals = [v for v in data.values() if isinstance(v, str) and any(is_thai(c) for c in v)]
        w = self_weight if name == "jeth" else 1
        n = 0
        for v in vals:
            base = None
            for ch in decompose_am(v):
                if not is_thai(ch):
                    base = None
                    continue
                chars[ch] += w
                n += 1
                if ch in COMBINING:
                    if base:
                        pairs[(base, ch)] += w
                else:
                    base = ch
        stats[name] = {"strings": len(vals), "char_occurrences": n, "weight": w}
    return chars, pairs, stats


# ------------------------------------------------------------- จัดสรร ----
def glyph_metrics(chars):
    """{ch: (ink_w, top, bottom)} จาก Sarabun ที่ ppem ของตัวนั้น (top/bottom วัดจากเส้นฐาน)

    ต้องใช้ `render_glyph` ตัวเดียวกับ `inject_thai_title.draw_cell` — มาร์กวาดเล็กกว่าฐาน + บีบตัวที่กว้างเกินเซลล์
    """
    from title_encode import render_glyph
    out = {}
    for ch in chars:
        img, _dx, top, bot = render_glyph(ch)
        out[ch] = (int(img.shape[1]), int(top), int(bot))
    return out


def width_classes(base_widths, weights, n=N_WCLASS):
    """แบ่งฐานเป็น n ชั้นตามความกว้าง ink -> (ขอบเขต, ความกว้างตัวแทนของแต่ละชั้น)

    ใช้ k-means 1 มิติถ่วงน้ำหนักด้วยความถี่ (Lloyd จนนิ่ง) — เป้าหมายคือลดค่า
    |ความกว้างฐานจริง - ตัวแทนของชั้น| เฉลี่ย เพราะค่านั้นคือระยะที่มาร์กจะเยื้องจากกึ่งกลางฐาน
    การแบ่งด้วยควอนไทล์ล้วนทำให้ชั้นบนกวาดตั้งแต่ 19 ถึง 28 px (เยื้องได้ถึง 4 px)
    """
    pts = sorted({w for w in base_widths.values()})
    wt = {w: 0 for w in pts}
    for ch, w in base_widths.items():
        wt[w] += max(1, weights.get(ch, 0))
    if len(pts) <= n:
        reps = [float(w) for w in pts] + [float(pts[-1])] * (n - len(pts))
    else:
        lo, hi = pts[0], pts[-1]
        reps = [lo + (hi - lo) * (i + 0.5) / n for i in range(n)]
        for _ in range(60):
            groups = [[] for _ in range(n)]
            for w in pts:
                groups[min(range(n), key=lambda i: abs(w - reps[i]))].append(w)
            new = []
            for i, g in enumerate(groups):
                tw = sum(wt[w] for w in g)
                new.append(sum(w * wt[w] for w in g) / float(tw) if tw else reps[i])
            if all(abs(a - b) < 1e-6 for a, b in zip(new, reps)):
                break
            reps = new
    reps = sorted(reps)
    edges = [int((reps[i] + reps[i + 1]) / 2.0) for i in range(n - 1)] + [pts[-1]]
    return edges, [round(r, 1) for r in reps]


def class_of(ink_w, edges):
    for i, e in enumerate(edges):
        if ink_w <= e:
            return i
    return len(edges) - 1


def anchor_classes(bases, chars, pairs, metrics, n=N_WCLASS):
    """ชั้นฐานตามตำแหน่งมาร์กที่ฟอนต์ต้นแบบตั้งไว้ + ตำแหน่งวางของทุก variant (ดู mark_anchor.py)

    คืน (mclass {ฐาน: ชั้น}, place {(มาร์ก, ชั้น, hlevel): px จากปากกา}, edges, reps)
    · key ของฐาน = off ของ ิ (ขอบขวาสระ - ขอบขวาฐาน) · ฐานที่วัดไม่ได้ (เช่น เ า ที่ HarfBuzz
      ใส่วงกลมประ) ได้ค่ากลางของทั้งหมด · place = off - ความกว้างมาร์กของเรา - RSB (ยึดขอบขวา)
    """
    import title_encode as T
    from mark_anchor import Shaper
    sh = Shaper(T.THAI_TTF, T.ppem())
    bearers = [v for v in TONE_BEARERS if v in metrics]
    off = {}
    for b in bases:
        for m in COMBINING:
            if m not in metrics:
                continue
            off[(b, m, 0)] = sh.mark_off(b, m)
            if kind_of(m) == "tone":
                vals = [(sh.mark_off(b, v + m), max(1, chars.get(v, 0))) for v in bearers]
                vals = [(o, w) for o, w in vals if o is not None]
                off[(b, m, 1)] = (sum(o * w for o, w in vals) / sum(w for _, w in vals)) if vals else None
    # แบ่งชั้นเฉพาะตัวที่มีมาร์กเกาะจริง (พยัญชนะ + ฤ ฦ) ถ่วงด้วยความถี่คู่ (ฐาน, มาร์ก) — สระหน้า/หลัง
    # อย่าง เ า ๆ ไม่มีมาร์กเกาะ ถ้านับรวมจะดึงชั้นไปเปล่า ๆ (ได้ชั้นกลางของพยัญชนะแทน)
    bearers_of_marks = [b for b in bases if b in THAI_CONSONANTS + "ฤฦ" and off.get((b, "ิ", 0)) is not None]
    keys = {b: int(round(off[(b, "ิ", 0)])) for b in bearers_of_marks}
    wt = {b: sum(w for (bb, _m), w in pairs.items() if bb == b) for b in keys}
    edges, reps = width_classes(keys, wt, n)
    # เลือกชั้นจากตัวแทนที่ใกล้สุด — edges ของ width_classes ปัดด้วย int() (ปัดเข้าหาศูนย์) ใช้กับค่าติดลบ
    # แล้วชั้นติดกันถูกรวม (Sarabun: ชั้น -4 กับ 0 ว่าง ฐานปกติทั้งหมดไปกองชั้นเดียว)
    mclass = {b: min(range(n), key=lambda i, k=k: abs(k - reps[i])) for b, k in keys.items()}
    common = max(set(mclass.values()), key=lambda c: sum(wt[b] for b in mclass if mclass[b] == c))
    for b in bases:
        mclass.setdefault(b, common)

    place = {}
    for m in COMBINING:
        if m not in metrics:
            continue
        mw = metrics[m][0]
        for c in range(n):
            for lvl in (0, 1):
                vals = [(off.get((b, m, lvl)), pairs.get((b, m), 0) + 1)
                        for b in bases if mclass[b] == c]
                vals = [(o, w) for o, w in vals if o is not None]
                if vals:
                    o = sum(o * w for o, w in vals) / float(sum(w for _, w in vals))
                    place[(m, c, lvl)] = round(o - mw - FM.RSB, 2)
    return mclass, place, edges, reps


def mark_levels(ch, freq):
    """จำนวนชั้นความสูงที่มาร์กตัวนี้ต้องมี — มีแค่วรรณยุกต์ที่ต้องมีสองชั้น"""
    if freq <= 0:
        return 1
    return 2 if kind_of(ch) == "tone" else 1     # ปกติ · ซ้อนเหนือสระบนอีกที


def mark_wclasses(ch, freq, n=N_WCLASS):
    return n if freq > 0 else 1


def plan_cells(chars, metrics, edges, reps, n_wclass=N_WCLASS, less_metrics=None):
    """ลำดับ 'สิ่งที่ต้องมีเซลล์' ตามความสำคัญ -> ลิสต์ของ spec dict (ยังไม่ผูก donor)

    less_metrics = {ฐาน: (ink_w, top, bottom)} ของรูปไม่มีเชิง (ญ ฐ — title_encode.LESS_BASES)
    ได้เซลล์ต่อจากฐานทันที (2 เซลล์) เพื่อให้ encode ใช้ตอนมีสระล่างตามหลัง
    """
    bases = [c for c in dict.fromkeys(MANDATORY + sorted(chars, key=lambda c: -chars[c]))
             if c not in COMBINING and c in metrics]
    marks = [c for c in dict.fromkeys(sorted(COMBINING, key=lambda c: -chars.get(c, 0)))
             if c in metrics]

    specs = []
    for ch in bases:
        w, top, bot = metrics[ch]
        specs.append({"text": ch, "kind": "base", "ink_w": w, "top": top, "bottom": bot,
                      "freq": chars.get(ch, 0)})
    for ch, (w, top, bot) in sorted((less_metrics or {}).items()):
        specs.append({"text": ch, "kind": "base", "variant": "less", "ink_w": w, "top": top,
                      "bottom": bot, "freq": 0})
    # มาร์ก: variant ที่พบบ่อยที่สุดมาก่อน (ชั้นความกว้างกลาง + ความสูงปกติ)
    for order in range(max(n_wclass * 3, 1)):
        for ch in marks:
            f = chars.get(ch, 0)
            nw, nl = mark_wclasses(ch, f, n_wclass), mark_levels(ch, f)
            for lvl in range(nl):
                for wc in range(nw):
                    if lvl * n_wclass + wc != order:
                        continue
                    w, top, bot = metrics[ch]
                    specs.append({"text": ch, "kind": kind_of(ch), "ink_w": w,
                                  "top": top, "bottom": bot, "freq": f,
                                  "wclass": wc, "hlevel": lvl,
                                  "base_w": reps[wc] if wc < len(reps) else reps[-1]})
    return specs


def cell_geometry(spec, metrics, refs):
    """เติมค่าเรขาคณิตของเซลล์: ตำแหน่งวาด (ink_x0, ink_y0) · advance · (L, R)"""
    from title_slotmap import BASELINE_Y
    ink_w = spec["ink_w"]
    if spec["kind"] == "base":
        adv = FM.base_advance(ink_w)
        place = FM.LSB
        y0 = BASELINE_Y + spec["top"]           # top เป็นค่าลบ = เหนือเส้นฐาน
    else:
        adv = 0.0
        place = refs.get("mark_place", {}).get((spec["text"], spec["wclass"], spec["hlevel"]))
        if place is None:                       # วัดจากฟอนต์ไม่ได้ — ถอยไปวางกึ่งกลางแบบเดิม
            place = FM.mark_place(spec["base_w"], ink_w)
        h = spec["bottom"] - spec["top"]
        if spec["kind"] == "lower":
            y0 = BASELINE_Y + refs["lower_gap"]
        else:
            lift = refs["upper_stack"] + refs["gap"] if spec["hlevel"] >= 1 else 0
            y0 = BASELINE_Y + refs["normal_top"] - refs["gap"] - lift - h
        y0 = max(0, min(CELL_H - h, int(round(y0))))
    L, R = FM.lr_for(adv, INK_X0, place)
    spec.update({"advance": round(float(adv), 2), "place": round(float(place), 2),
                 "ink_x0": INK_X0, "ink_y0": int(y0),
                 "L": round(L, 4), "R": round(R, 4)})
    return spec


# กลิฟว่าง advance 0 (L = R = 1.0 -> 36 - 18 x 2 = 0) — ดูเหตุผลที่ SENTINEL_CP ข้างบน
SENTINEL_SPEC = {"text": "", "kind": "sentinel", "ink_w": 0, "top": 0, "bottom": 0,
                 "freq": 0, "advance": 0.0, "place": 0.0, "ink_x0": 0, "ink_y0": 0,
                 "L": 1.0, "R": 1.0,
                 "note": "ตัวนำบังคับสลับฟอนต์ — วาดเป็นเซลล์ว่าง ห้ามใส่หมึก"}


def allocate(tiers=DEFAULT_TIERS, corpora=None, self_weight=3, keep_en_safe=True,
             n_wclass=N_WCLASS):
    """คำนวณการจัดสรรทั้งหมด -> dict พร้อมเขียนเป็น slotmap.json"""
    from title_slotmap import BASELINE_Y  # noqa: F401  (ยืนยันว่าโมดูลโหลดได้ก่อนเรนเดอร์)

    chars, pairs, corpus_stats = load_corpora(corpora, self_weight)
    en_used, have_extract = en_used_codepoints()
    th_used = th_used_codepoints(corpora)
    reserved = sorted(set(en_used) | set(th_used)) if (keep_en_safe and have_extract) else []
    pool = [cp for cp in build_pool(tiers, reserved) if cp != SENTINEL_CP]

    need = set(MANDATORY) | {c for c in chars if is_thai(c)}
    metrics = glyph_metrics(sorted(need))

    base_w = {c: metrics[c][0] for c in metrics if c not in COMBINING}
    edges, reps = width_classes(base_w, chars, n_wclass)

    tops = sorted(metrics[c][1] for c in base_w)
    normal_top = tops[len(tops) // 2]                  # ค่ากลางของ ink บนสุด (ค่าลบ)
    upper_stack = max(metrics[c][2] - metrics[c][1] for c in TONE_BEARERS if c in metrics)
    refs = {"normal_top": int(normal_top), "upper_stack": int(upper_stack),
            "gap": 1, "lower_gap": LOWER_GAP}

    thai_bases = [c for c in base_w if is_thai(c)]
    mclass, mplace, medges, mreps = anchor_classes(thai_bases, chars, pairs, metrics, n_wclass)
    refs["mark_place"] = mplace

    from title_encode import LESS_BASES, render_glyph
    less_metrics = {}
    for ch in LESS_BASES:
        img, _dx, top, bot = render_glyph(ch, "less")
        less_metrics[ch] = (int(img.shape[1]), int(top), int(bot))

    specs = plan_cells(chars, metrics, edges, reps, n_wclass, less_metrics)
    for spec in specs:
        if spec["kind"] == "base" and spec["text"] in mclass:
            spec["mclass"] = mclass[spec["text"]]
    used, spilled = [], []
    for spec in specs:
        if len(used) >= len(pool):
            spilled.append(spec)
            continue
        spec = cell_geometry(spec, metrics, refs)
        spec["cp"] = pool[len(used)]
        used.append(spec)

    used.append(dict(SENTINEL_SPEC, cp=SENTINEL_CP))

    cells = OrderedDict()
    for spec in sorted(used, key=lambda s: s["cp"]):
        cp = spec.pop("cp")
        spec["tier"] = tier_of(cp)
        cells["%04X" % cp] = spec

    refs = {k: v for k, v in refs.items() if k != "mark_place"}
    return {
        "font": "meta_ot_cond_book",
        "note": "ไฟล์นี้สร้างด้วย scripts/slot_alloc.py — ห้ามแก้ด้วยมือ",
        "policy": {
            "model": "per-char (kerning_table)",
            "kern_unit_px": FM.K,
            "cell_advance_px": FM.CELL_ADV,
            "lsb": FM.LSB, "rsb": FM.RSB,
            "ink_x0": INK_X0,
            "n_wclass": n_wclass,
            "wclass_edges": edges,
            "wclass_rep": reps,
            "mark_model": "font-anchor",   # มาร์กวางตาม GPOS ของฟอนต์ต้นแบบ (mark_anchor.py) · ชั้น = mclass ของฐาน
            "mclass_edges": medges,
            "mclass_rep": mreps,
            "refs": refs,
            "tiers": list(tiers),
            "keep_en_safe": bool(keep_en_safe and have_extract),
        },
        "budget": {
            "grid_cells": 384,
            "kern_rows": FM.KERN_ROWS,
            "pool": len(pool),
            "reserved_by_en": len(reserved),
            "used": len(cells),
            "free": len(pool) - len(cells),
            "demand_cells": len(specs),
            "spilled": len(spilled),
        },
        "reserved": {"%04X" % cp: {
            "char": chr(cp),
            "en_count": en_used[cp][0] if cp in en_used else 0,
            "th_count": th_used.get(cp, 0),
            "bins": en_used[cp][1][:8] if cp in en_used else [],
        } for cp in reserved},
        "corpora": corpus_stats,
        "spill_top": [{"text": s["text"], "kind": s["kind"],
                       "wclass": s.get("wclass"), "hlevel": s.get("hlevel")}
                      for s in spilled[:40]],
        "cells": cells,
    }


# --------------------------------------------------------------- ใช้งาน ----
class SlotMap:
    """อ่าน slotmap.json แล้วใช้ encode/decode — ฝั่งฟอนต์และฝั่งข้อความใช้ตัวเดียวกัน"""

    def __init__(self, data):
        self.data = data
        self.cells = data["cells"]
        pol = data["policy"]
        self.n_wclass = pol.get("n_wclass", 1)
        self.edges = pol.get("wclass_edges", [])
        self.base = {}          # ch -> cp
        self.mark = {}          # (ch, wclass, hlevel) -> cp
        self.width = {}         # ch -> ink_w (ของฐาน)
        self.mclass = {}        # ch -> ชั้นมาร์กของฐาน (mark_model = font-anchor)
        self.base_less = {}     # ch -> cp ของรูปไม่มีเชิง (ญ ฐ) ใช้เมื่อตัวถัดไปเป็นสระล่าง
        self.dec = {}
        self.sentinel = None
        for k, v in self.cells.items():
            cp = int(k, 16)
            self.dec[cp] = v["text"]
            if v["kind"] == "sentinel":
                self.sentinel = cp
            elif v["kind"] == "base" and v.get("variant") == "less":
                self.base_less[v["text"]] = cp
            elif v["kind"] == "base":
                self.base[v["text"]] = cp
                self.width[v["text"]] = v["ink_w"]
                if "mclass" in v:
                    self.mclass[v["text"]] = v["mclass"]
            else:
                self.mark[(v["text"], v.get("wclass", 0), v.get("hlevel", 0))] = cp
        self.marks_per_cell = 0
        self.max_unit_len = 1

    @classmethod
    def load(cls, path=SLOTMAP):
        return cls(json.load(io.open(path, encoding="utf-8")))

    def wclass_of(self, ch):
        if ch in self.mclass:
            return self.mclass[ch]
        w = self.width.get(ch)
        if w is None:
            return self.n_wclass // 2
        return class_of(w, self.edges)

    def _mark_cp(self, ch, wc, lvl):
        """หา variant ที่ใกล้ที่สุดที่มีจริง (ถอยชั้นความสูงก่อน แล้วค่อยถอยชั้นความกว้าง)"""
        for l2 in range(lvl, -1, -1):
            for w2 in ([wc] + [w for w in range(self.n_wclass) if w != wc]):
                cp = self.mark.get((ch, w2, l2))
                if cp is not None:
                    return cp
        return None

    def encode(self, text, strict=True):
        """ข้อความไทย -> สตริง donor (ตัวที่ไม่ใช่ไทยผ่านตรง) — หนึ่งตัวอักษรหนึ่ง codepoint

        ทุกช่วงที่เป็นอักษรไทยจะถูกนำหน้าด้วยเซลล์ตัวนำ (`SENTINEL_CP` — กลิฟว่าง advance 0)
        เพื่อบังคับให้เอนจิ้นสลับไปวาดด้วย `meta_ot_cond_book` ตั้งแต่ตัวแรกของช่วงนั้น
        มิฉะนั้นจอที่ตั้งฟอนต์เป็น `yakuza` จะวาด donor ของเราเป็นอักษร Latin-1 ตัวใหญ่
        (เหตุผลเต็มอยู่ที่ SENTINEL_CP ข้างบน)
        """
        out = []
        wc, has_upper = self.n_wclass // 2, False
        in_run = False

        def lead():
            """เปิดช่วงไทยด้วยตัวนำ (ครั้งเดียวต่อช่วง)"""
            if not in_run and self.sentinel is not None:
                out.append(chr(self.sentinel))

        src = decompose_am(text)
        for i, ch in enumerate(src):
            if not is_thai(ch):
                if ord(ch) in self.dec:
                    raise SystemExit(
                        f"ข้อความมี {ch!r} (U+{ord(ch):04X}) ซึ่งถูกใช้เป็น donor ของ "
                        f"{self.dec[ord(ch)]!r} — ในเกมจะกลายเป็นตัวอักษรไทย "
                        f"ให้แทนด้วยตัวอื่นในขั้นตอน QC ก่อน")
                out.append(ch)
                wc, has_upper, in_run = self.n_wclass // 2, False, False
                continue
            if ch in COMBINING:
                k = kind_of(ch)
                lvl = 1 if (k == "tone" and has_upper) else 0
                cp = self._mark_cp(ch, wc, lvl)
                if cp is None:
                    if strict:
                        raise SystemExit(f"มาร์ก {ch!r} ไม่มีเซลล์ใน slotmap — รัน slot_alloc.py ใหม่")
                    out.append("?")
                    continue
                lead()
                out.append(chr(cp))
                in_run = True
                if k == "upper":
                    has_upper = True
                continue
            cp = self.base.get(ch)
            if ch in self.base_less and i + 1 < len(src) and src[i + 1] in LOWER:
                cp = self.base_less[ch]             # ญ ฐ + สระล่าง → รูปไม่มีเชิง (กตัญญู)
            if cp is None:
                if strict:
                    raise SystemExit(f"ตัวอักษร {ch!r} ไม่มีเซลล์ใน slotmap — รัน slot_alloc.py ใหม่")
                out.append("?")
                continue
            lead()
            out.append(chr(cp))
            in_run = True
            wc, has_upper = self.wclass_of(ch), False
        return "".join(out)

    def decode(self, s):
        return recompose_am("".join(self.dec.get(ord(ch), ch) for ch in s))

    def glyph_plan(self):
        """[(cp, spec dict)] ให้ inject_thai_title.py วาด — spec บอกตำแหน่งวาดครบแล้ว"""
        return [(int(k, 16), v) for k, v in sorted(self.cells.items())]

    def kern_rows(self):
        """{cell_index: (L, R)} ให้ gen_font_bin.py เขียนลง kerning_table"""
        return {FM.cell_index(int(k, 16)): (v["L"], v["R"]) for k, v in self.cells.items()}


# --------------------------------------------------------------- รายงาน ----
REPORT = paths.DOCS / "slot_alloc.md"


def write_report(res, path=REPORT):
    b, pol = res["budget"], res["policy"]
    cells = res["cells"]
    n_base = sum(1 for v in cells.values() if v["kind"] == "base")
    n_mark = len(cells) - n_base
    L = []
    L.append("# Slot allocation — `meta_ot_cond_book`")
    L.append("")
    L.append("> สร้างอัตโนมัติด้วย `python scripts/slot_alloc.py --write` — ห้ามแก้ด้วยมือ")
    L.append("")
    L.append("ตั้งแต่รอบ 16 การจัดสรรคุมทั้ง **รูปกลิฟ** และ **advance** พร้อมกัน เพราะตาราง")
    L.append("`kerning_table` ใน `db.judge.en.par → en/font.bin` แก้ได้ (ดู `scripts/font_metrics.py`)")
    L.append("")
    L.append("## งบประมาณเซลล์")
    L.append("")
    L.append("| รายการ | ค่า |")
    L.append("|---|---|")
    L.append("| เซลล์ทั้งตาราง atlas | %d |" % b["grid_cells"])
    L.append("| แถวใน kerning_table (เพดานจริง) | %d = ถึง U+016B |" % b["kern_rows"])
    L.append("| donor pool ที่เปิดใช้ (%s) | %d |" % (", ".join(pol["tiers"]), b["pool"]))
    L.append("| หักคืนเพราะข้อความอังกฤษ/ไทยใช้อยู่ | %d |" % b["reserved_by_en"])
    L.append("| ต้องการทั้งหมด | %d |" % b["demand_cells"])
    L.append("| **จัดสรรแล้ว** | **%d** (ฐาน %d · มาร์ก %d) |" % (b["used"], n_base, n_mark))
    L.append("| เหลือว่าง | %d |" % b["free"])
    L.append("| ตกขอบ | %d |" % b["spilled"])
    L.append("")
    L.append("## นโยบายเรขาคณิต")
    L.append("")
    L.append("| รายการ | ค่า |")
    L.append("|---|---|")
    L.append("| หน่วยตาราง | %.1f px ต่อ 1.0 (เซลล์เต็ม = 2.0 = %.0f px) |"
             % (pol["kern_unit_px"], pol["cell_advance_px"]))
    L.append("| side bearing ฐาน | ซ้าย %d px · ขวา %d px |" % (pol["lsb"], pol["rsb"]))
    L.append("| ชั้นความกว้างของฐาน (variant ของมาร์ก) | %d ชั้น · ขอบ %s · ตัวแทน %s |"
             % (pol["n_wclass"], pol["wclass_edges"], pol["wclass_rep"]))
    L.append("")
    L.append("## ตัวอย่าง advance ที่ตั้งให้ (ฐานที่พบบ่อยสุด 15 ตัว)")
    L.append("")
    L.append("| ตัว | ink | advance | L | R |")
    L.append("|---|---|---|---|---|")
    top = sorted((v for v in cells.values() if v["kind"] == "base"),
                 key=lambda v: -v["freq"])[:15]
    for v in top:
        L.append("| %s | %d | %.0f | %.4f | %.4f |"
                 % (v["text"], v["ink_w"], v["advance"], v["L"], v["R"]))
    L.append("")
    L.append("## คลังที่ใช้คำนวณความถี่")
    L.append("")
    L.append("| คลัง | ประโยคไทย | ตัวอักษรไทย | น้ำหนัก |")
    L.append("|---|---|---|---|")
    for name, st in res["corpora"].items():
        L.append("| %s | %s | %s | %s |" % (
            name, "{:,}".format(st.get("strings", 0)),
            "{:,}".format(st.get("char_occurrences", 0)), st.get("weight", "-")))
    L.append("")
    if res["spill_top"]:
        L.append("## variant ที่ตกขอบ (เซลล์ไม่พอ)")
        L.append("")
        for s in res["spill_top"]:
            L.append("- `%s` %s wclass=%s hlevel=%s" % (s["text"], s["kind"], s["wclass"], s["hlevel"]))
        L.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    return path


def main():
    ap = argparse.ArgumentParser(description="จัดสรรเซลล์ฟอนต์ให้ข้อความไทย")
    ap.add_argument("--write", action="store_true", help="เขียน translations/slotmap.json")
    ap.add_argument("--tiers", default=",".join(DEFAULT_TIERS))
    ap.add_argument("--corpora", default="")
    ap.add_argument("--self-weight", type=int, default=3)
    ap.add_argument("--wclass", type=int, default=N_WCLASS)
    a = ap.parse_args()

    res = allocate(tiers=a.tiers.split(","),
                   corpora=a.corpora.split(",") if a.corpora else None,
                   self_weight=a.self_weight, n_wclass=a.wclass)
    b = res["budget"]
    n_base = sum(1 for v in res["cells"].values() if v["kind"] == "base")
    print("pool %d · ใช้ %d (ฐาน %d · มาร์ก %d) · เหลือ %d · ตกขอบ %d"
          % (b["pool"], b["used"], n_base, b["used"] - n_base, b["free"], b["spilled"]))
    print("ชั้นความกว้าง %d: ขอบ %s ตัวแทน %s"
          % (res["policy"]["n_wclass"], res["policy"]["wclass_edges"], res["policy"]["wclass_rep"]))
    if a.write:
        SLOTMAP.parent.mkdir(parents=True, exist_ok=True)
        io.open(SLOTMAP, "w", encoding="utf-8", newline="\n").write(
            json.dumps(res, ensure_ascii=False, indent=1) + "\n")
        print("เขียน %s" % SLOTMAP)
        print("เขียน %s" % write_report(res))


if __name__ == "__main__":
    main()
