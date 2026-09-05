#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""อ่านภาพหน้าไตเติลของ probe หวี -> `translations/donor_widths.json` (รวมกับค่าที่วัดไว้เดิม)

คู่กับ `scripts/title_comb.py` (อ่านวิธีทั้งหมดที่หัวไฟล์นั้น) — สรุป: ทุกเซลล์ที่ต้องวัดถูกวาด
เป็นขีดตั้งเหมือนกันหมด เรียงเป็นแถวในเมนูไตเติล ระยะระหว่างขีดสองอันติดกัน = advance ของ
donor ตัวซ้าย (หน่วย px จอ) หารด้วย scale = advance ในหน่วย atlas

ใช้:
  python scripts/measure_comb.py shots/comb2.png
  python scripts/measure_comb.py shots/comb2.png --dry-run   # วัดอย่างเดียว ไม่เขียนไฟล์
  python scripts/measure_comb.py shots/comb2.png --bands     # โชว์ทุกบรรทัดที่เจอ (ตอนภาพไม่เข้าผัง)
"""
import argparse
import io
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                    # noqa: E402
import title_comb                               # noqa: E402
from find_width_table import ascii_ink_widths   # noqa: E402

OUT = paths.TRANSLATIONS / "donor_widths.json"


def mask_of(img, thresh=230, grey_tol=25):
    """เฉพาะพิกเซล 'ขาว' ของตัวหนังสือ — ฉากหลังหน้าไตเติลเป็นควันเหลือง/แดงจึงถูกตัดทิ้ง"""
    a = np.asarray(img.convert("RGB"), dtype=np.int16)
    lo, hi = a.min(axis=2), a.max(axis=2)
    return (lo >= thresh) & ((hi - lo) <= grey_tol)


def bands(mask, min_h=5, min_row_px=4):
    """ช่วงแถว (y0, y1, จำนวนพิกเซล) ที่มีหมึก — หนึ่งช่วง = หนึ่งบรรทัดข้อความ"""
    rows = mask.sum(axis=1)
    out, y, n = [], 0, len(rows)
    while y < n:
        if rows[y] > min_row_px:
            y0 = y
            while y < n and rows[y] > min_row_px:
                y += 1
            if y - y0 >= min_h:
                out.append((y0, y, int(mask[y0:y].sum())))
        else:
            y += 1
    return out


def segments(mask, y0, y1, gap=2):
    """ช่วงคอลัมน์ที่มีหมึกในบรรทัดนี้ -> [(x0, x1)]"""
    cols = mask[y0:y1].sum(axis=0)
    xs = np.flatnonzero(cols > 0)
    if not len(xs):
        return []
    out = [[int(xs[0]), int(xs[0])]]
    for x in xs[1:]:
        if x - out[-1][1] <= gap:
            out[-1][1] = int(x)
        else:
            out.append([int(x), int(x)])
    return [tuple(v) for v in out]


def rows_of(mask, expect, dark=None):
    """จับคู่บรรทัดในภาพกับจำนวนซี่ที่คาดไว้ (เรียงบนลงล่าง)

    แถวที่เคอร์เซอร์เมนูเลือกอยู่จะกลายเป็น **ตัวมืดบนแถบขาว** -> ถ้าเจอแถบทึบ ให้กลับขั้ว
    ไปหาช่วงพิกเซลมืดในแถบนั้นแทน (รอบ 14 เสียข้อมูลไปทั้งแถวเพราะไม่ได้ทำแบบนี้)
    """
    cand = []
    for y0, y1, npx in bands(mask):
        h = y1 - y0
        if npx > 150 * h:                  # แถบไฮไลต์ (พื้นขาวทึบ) -> อ่านตัวมืดข้างใน
            if dark is None:
                continue
            # แถบไฮไลต์มีสามเหลี่ยมตกแต่งหัวท้าย -> เก็บเฉพาะ "ซี่" (กว้าง <= 7 px)
            # แล้วต่อท้ายด้วยช่วงถัดไปที่กว้างพอเป็นตัว M ปิดแถว
            allsegs = segments(dark, y0, y1)
            bars = [g for g in allsegs if g[1] - g[0] + 1 <= 7]
            segs = list(bars)
            if bars:
                for g in allsegs:
                    if g[0] > bars[-1][0] and 8 <= g[1] - g[0] + 1 <= 25:
                        segs.append(g)
                        break
            if len(segs) >= 3:
                cand.append((y0, y1, segs))
            continue
        segs = segments(mask, y0, y1)
        if len(segs) >= 3:
            cand.append((y0, y1, segs))
    out, i = [], 0
    for want in expect:
        hit = None
        while i < len(cand):
            y0, y1, segs = cand[i]
            i += 1
            if abs(len(segs) - want) <= 1:
                hit = (y0, y1, segs)
                break
        out.append(hit)
    return out, cand


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("image")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--bands", action="store_true", help="โชว์ทุกบรรทัดที่เจอในภาพ")
    ap.add_argument("--thresh", type=int, default=230)
    ap.add_argument("--x0", type=int, default=1000,
                    help="ตัดเฉพาะฝั่งขวาที่เป็นเมนู (ภาพตัวละครฝั่งซ้ายมีขาวปนจนบรรทัดติดกัน)")
    ap.add_argument("--x1", type=int, default=0, help="ขอบขวา (0 = สุดภาพ)")
    a = ap.parse_args()

    img = Image.open(a.image)
    full = mask_of(img, a.thresh)
    x1 = a.x1 or full.shape[1]
    mask = np.zeros_like(full)
    mask[:, a.x0:x1] = full[:, a.x0:x1]
    print("ภาพ %dx%d · พิกเซลขาว %d" % (img.width, img.height, int(mask.sum())))

    cal, chunks = title_comb.CAL_ROW, title_comb.CHUNKS
    expect = [len(cal)] + [len(c) + 1 for c in chunks]
    a_rgb = np.asarray(img.convert("RGB"), dtype=np.int16)
    dark = np.zeros_like(mask)
    dark[:, a.x0:x1] = (a_rgb[:, a.x0:x1].max(axis=2) <= 90)
    rows, cand = rows_of(mask, expect, dark)

    if a.bands:
        for y0, y1, segs in cand:
            print("  y=%4d..%4d  %3d ช่วง  x=%d..%d" % (y0, y1, len(segs), segs[0][0], segs[-1][1]))
    for want, got in zip(expect, rows):
        print("  คาด %2d ซี่ -> %s" % (want, "ไม่พบบรรทัด" if got is None
                                       else "y=%d..%d เจอ %d" % (got[0], got[1], len(got[2]))))
    if rows[0] is None:
        sys.exit("!! ไม่พบแถวเทียบมาตราส่วน (M x%d) — ลองปรับ --thresh หรือดู --bands" % len(cal))

    ink = ascii_ink_widths()
    m_w = float(np.median([s[1] - s[0] + 1 for s in rows[0][2]]))
    scale = m_w / ink[ord("M")]
    m_adv = float(np.median(np.diff([s[0] for s in rows[0][2]])))
    print("scale = %.4f px จอ/px atlas · advance ของ M = %.1f px จอ = %.2f px atlas"
          % (scale, m_adv, m_adv / scale))

    fresh, misses = {}, []
    for chunk, row in zip(chunks, rows[1:]):
        if row is None:
            misses += chunk
            continue
        lefts = [s[0] for s in row[2]]
        for i, cp in enumerate(chunk):
            if i + 1 >= len(lefts):
                misses.append(cp)
                continue
            fresh["%04X" % cp] = round((lefts[i + 1] - lefts[i]) / scale, 1)
    print("วัดใหม่ได้ %d donor%s" % (len(fresh),
          "" if not misses else " · ยังขาด %d (%s)" % (len(misses),
          " ".join("U+%04X" % c for c in misses[:12]))))
    if fresh:
        vals = sorted(fresh.values())
        print("   ค่าที่ได้: %.1f - %.1f (กลาง %.1f)" % (vals[0], vals[-1], float(np.median(vals))))

    if a.dry_run or not fresh:
        return 0

    # ---- รวมกับไฟล์เดิม: ค่าที่วัดใหม่ทับค่าเดา และเลื่อนสถานะเป็น measured ----
    old = json.load(io.open(OUT, encoding="utf-8")) if OUT.exists() else {}
    raw = dict(old.get("raw", {}))
    raw.update(fresh)
    prov_ext = [k for k in old.get("provisional_extA_default", []) if k not in fresh]
    prov_ink = [k for k in old.get("provisional_from_ink", []) if k not in fresh]
    measured = sorted(k for k in raw if k not in prov_ext and k not in prov_ink)
    payload = {
        "note": "advance จริงต่อ codepoint (หน่วย px ของ atlas) — วัดจาก probe หวี",
        "source_image": str(a.image),
        "scale_screen_per_atlas": round(scale, 4),
        "measured": measured,
        "provisional_extA_default": prov_ext,
        "provisional_from_ink": prov_ink,
        "widths": {k: int(round(v)) for k, v in sorted(raw.items())},
        "raw": {k: v for k, v in sorted(raw.items())},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    print("เขียน %s · วัดจริงแล้ว %d · ยังเป็นค่าเดา %d"
          % (OUT, len(measured), len(prov_ext) + len(prov_ink)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
