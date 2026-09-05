#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ค้นหา **ตาราง width ของฟอนต์ `meta_ot_cond_book` ใน `Judgment.exe`**

ทำไม: advance ของแต่ละเซลล์ไม่ได้อยู่ในไฟล์ dds/bin เลย (ยืนยันรอบ 4 — เลือก donor = เลือก
ความกว้าง) ตาราง width จึงต้องอยู่ในโค้ด ถ้าหาเจอ เราจะรู้ค่าของ donor 183 ช่องที่วัดจากในเกม
ไม่ได้ทันที (ปมใหญ่ที่ค้างอยู่) — และรู้ด้วยว่า cell ไหน advance กว้างเกินกลิฟจนเห็นเป็นช่องไฟ

วิธี (ไม่แตะไฟล์เกม — เปิดอ่านอย่างเดียว):
  1. วัดความกว้าง ink จริงของเซลล์ ASCII ใน atlas ต้นฉบับ (ตัวที่มีหมึกทุกตัว)
  2. ไล่ทุก offset ในไฟล์ exe แล้วถามว่า "ถ้าตรงนี้คือตาราง width ที่ index ด้วย codepoint
     ค่าที่ได้จะเรียงตามความกว้าง ink ไหม" — กรองหยาบด้วยอสมการที่ต้องจริงเสมอ
     (m > i, W > l, M > .) แล้วค่อยคำนวณ correlation กับผู้รอด
  3. รายงาน offset ที่ correlation สูง พร้อมค่าของช่วง U+00A0-019F (= donor pool ของเรา)

ใช้:
  python scripts/find_width_table.py                    # สแกน u8/u16/f32
  python scripts/find_width_table.py --min-corr 0.9 --top 20
  python scripts/find_width_table.py --dump 0x1234567 --kind u8 --stride 1
"""
import argparse
import io
import json
import sys
from pathlib import Path

import numpy as np

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                            # noqa: E402
from bc4_codec import decode_bc4                        # noqa: E402
from title_slotmap import ATLAS_H, ATLAS_W, CELL_H, CELL_W, cell_xy   # noqa: E402

SRC_DDS = paths.EXTRACTED / "font" / "meta_ot_cond_book.dds"
OUT = paths.BUILD / "text" / "width_table_candidates.json"

# ตัวอักษรที่ความกว้างต่างกันชัดเจน — ใช้กรองหยาบก่อนคำนวณ correlation
PROBE_PAIRS = [("m", "i"), ("W", "l"), ("M", "."), ("w", "j"), ("O", "I"), ("A", "'")]


def ascii_ink_widths():
    """{cp: ความกว้าง ink px} ของเซลล์ ASCII ที่มีหมึกใน atlas ต้นฉบับ"""
    atlas = decode_bc4(SRC_DDS.read_bytes()[128:], ATLAS_W, ATLAS_H)
    out = {}
    for cp in range(0x21, 0x7F):
        x0, y0 = cell_xy(cp)
        cell = atlas[y0:y0 + CELL_H, x0:x0 + CELL_W]
        xs = np.where((cell > 16).any(axis=0))[0]
        if len(xs):
            out[cp] = int(xs.max() - xs.min() + 1)
    return out


def as_values(data, kind, stride, cp, n):
    """ค่าของ codepoint `cp` สำหรับทุก offset เริ่มต้น 0..n-1 (เวกเตอร์เดียว ไม่วนลูป)"""
    off = cp * stride
    if kind == "u8":
        return data[off:off + n].astype(np.float32)
    if kind == "u16":
        v = data[off:off + n + 1]
        return (v[:n].astype(np.float32) + v[1:n + 1].astype(np.float32) * 256.0)
    if kind == "f32":
        raw = np.frombuffer(data.tobytes(), dtype=np.uint8)   # ใช้ view เดิม
        # อ่าน f32 ที่ offset ไม่ align ด้วยการประกอบ 4 ไบต์
        b0 = raw[off:off + n].astype(np.uint32)
        b1 = raw[off + 1:off + 1 + n].astype(np.uint32) << 8
        b2 = raw[off + 2:off + 2 + n].astype(np.uint32) << 16
        b3 = raw[off + 3:off + 3 + n].astype(np.uint32) << 24
        return (b0 | b1 | b2 | b3).view(np.float32)
    raise ValueError(kind)


def scan(data, widths, kind, stride, min_corr, top, lo=1.0, hi=64.0):
    """คืน [(offset, corr, ค่าที่อ่านได้)] ที่ค่าในไฟล์เรียงตามความกว้าง ink ของ ASCII

    กรองสองชั้นเพื่อให้สแกน exe 400 MB ไหว:
      ชั้นแรก  อสมการที่ต้องจริงเสมอ (m>i, W>l ...) + ค่าต้องอยู่ในพิสัยที่เป็นไปได้
      ชั้นสอง  correlation กับความกว้าง ink ของ ASCII ทั้ง 94 ตัว
    """
    cps = sorted(widths)
    max_cp = max(cps)
    n = len(data) - (max_cp + 2) * stride - 8
    if n <= 0:
        return []

    keep = np.ones(n, dtype=bool)
    for a, b in PROBE_PAIRS:
        keep &= as_values(data, kind, stride, ord(a), n) > as_values(data, kind, stride, ord(b), n)
        if not keep.any():
            return []
    for ch in "imWlM.oX":                       # ค่าต้องอยู่ในพิสัยความกว้างที่เป็นไปได้
        v = as_values(data, kind, stride, ord(ch), n)
        keep &= np.isfinite(v) & (v >= lo) & (v <= hi)
        if not keep.any():
            return []
    cand = np.flatnonzero(keep)
    if len(cand) == 0:
        return []

    ink = np.array([widths[c] for c in cps], dtype=np.float64)
    ink_c = ink - ink.mean()
    ink_n = np.sqrt((ink_c ** 2).sum())

    out = []
    CH = 200000                                  # ทำเป็นก้อน กันหน่วยความจำบวม
    for i0 in range(0, len(cand), CH):
        blk = cand[i0:i0 + CH]
        cols = []
        for c in cps:
            v = as_values(data, kind, stride, c, n)
            cols.append(v[blk])
        vals = np.stack(cols, axis=1).astype(np.float64)
        ok = np.isfinite(vals).all(axis=1) & (vals.std(axis=1) > 0)
        vals, blk = vals[ok], blk[ok]
        if not len(blk):
            continue
        vc = vals - vals.mean(axis=1, keepdims=True)
        corr = (vc * ink_c).sum(axis=1) / (np.sqrt((vc ** 2).sum(axis=1)) * ink_n)
        hit = np.flatnonzero(corr >= min_corr)
        for h in hit:
            out.append((int(blk[h]), float(corr[h]), vals[h]))
    out.sort(key=lambda r: -r[1])
    return out[:top]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--exe", default=str(paths.GAME_EXE))
    ap.add_argument("--min-corr", type=float, default=0.85)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--kinds", default="u8,u16,f32")
    ap.add_argument("--strides", default="1,2,4,8,16")
    a = ap.parse_args()

    widths = ascii_ink_widths()
    print("ความกว้าง ink ของ ASCII ที่วัดได้ %d ตัว (เช่น i=%d m=%d W=%d)"
          % (len(widths), widths[ord("i")], widths[ord("m")], widths[ord("W")]))

    exe = Path(a.exe)
    assert exe.exists(), "ไม่พบ %s" % exe
    data = np.fromfile(exe, dtype=np.uint8)
    print("อ่าน %s (%.1f MB)" % (exe.name, len(data) / 1e6))

    found = {}
    for kind in [k.strip() for k in a.kinds.split(",") if k.strip()]:
        for stride in [int(s) for s in a.strides.split(",")]:
            if kind == "u8" and stride > 4:
                continue
            if kind == "u16" and stride < 2:
                continue
            if kind == "f32" and stride < 4:
                continue
            lo = 0.0005 if kind == "f32" else 1.0   # f32 อาจเก็บเป็นสัดส่วนของ em (0..1)
            res = scan(data, widths, kind, stride, a.min_corr, a.top, lo=lo)
            print("%-4s stride %-2d : ผู้สมัคร %d" % (kind, stride, len(res)))
            for off, corr, vals in res[:5]:
                print("   0x%08X corr %.4f  ตัวอย่าง i=%.3f m=%.3f W=%.3f"
                      % (off, corr, vals[ord("i") - 0x21], vals[ord("m") - 0x21],
                         vals[ord("W") - 0x21]))
            if res:
                found["%s/%d" % (kind, stride)] = [
                    {"offset": off, "corr": corr} for off, corr, _ in res]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(found, ensure_ascii=False, indent=1) + "\n")
    print("เขียน", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
