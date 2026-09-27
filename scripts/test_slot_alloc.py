#!/usr/bin/env python3
"""ตรวจ slotmap.json + encode/decode ของ slot allocator (รันหลังแก้ slot_alloc.py ทุกครั้ง)

เช็ค 12 ข้อ:
  1. slotmap โหลดได้ · เซลล์ไม่เกิน pool · ไม่มี donor/variant ซ้ำ · advance กับ (L,R) สมเหตุผล
     · donor ทุกตัวอยู่ในช่วงที่ `kerning_table` มีแถวให้ (<= U+016B ไม่งั้นเอนจิ้นวาดเป็นกล่อง)
  2. ไม่มี donor แตะช่วง ASCII (U+0020-007F) ที่เกมใช้เขียนอังกฤษ
  3. donor ไม่ชนกับ codepoint ที่ข้อความอังกฤษของเกมใช้อยู่จริง (จาก unique_strings.json)
  4. decode(encode(s)) == s สำหรับคลังแปลจริง (fallback แตกมาร์กก็ต้องได้ลำดับตัวอักษรเดิม)
  5. encode ทั้งคลังโดยไม่ throw = ครอบคลุมทุก cluster ที่เคยเจอในเกม RGG
  6. ตัวอักษรฐานไทยครบทุกตัว (พิมพ์คำอะไรก็เรนเดอร์ได้ ไม่มี tofu)
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from slot_alloc import (CORPORA, MANDATORY, SLOTMAP, SlotMap, en_used_codepoints,
                        is_thai, thai_cells)

FAILS = []
N_CHECKS = 12


def check(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  — " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


def main():
    sm = SlotMap.load(SLOTMAP)
    data = sm.data
    cps = [int(k, 16) for k in sm.cells]

    check("1a slotmap โหลดได้ + มีเซลล์", len(sm.cells) > 0, "%d เซลล์" % len(sm.cells))
    check("1b donor ไม่ซ้ำ", len(cps) == len(set(cps)))
    check("1c ไม่เกิน pool", len(cps) <= data["budget"]["pool"],
          "%d/%d" % (len(cps), data["budget"]["pool"]))
    variants = [(v["text"], v["kind"], v.get("wclass"), v.get("hlevel"), v.get("variant"))
                for v in sm.cells.values()]
    check("1d ไม่มี variant ซ้ำ", len(set(variants)) == len(sm.cells),
          "%d variant / %d เซลล์" % (len(set(variants)), len(sm.cells)))
    check("1e มาร์กทุกเซลล์ advance = 0", not [v for v in sm.cells.values()
                                                if v["kind"] != "base" and v["advance"] != 0])
    check("1f ฐานทุกเซลล์ advance = ink + side bearing",
          not [v for v in sm.cells.values() if v["kind"] == "base"
               and v["advance"] != v["ink_w"] + data["policy"]["lsb"] + data["policy"]["rsb"]])
    check("1g L/R อยู่ในช่วงที่เอนจิ้นรับได้",
          not [v for v in sm.cells.values() if not (-0.01 <= v["L"] <= 2.0 and -0.01 <= v["R"] <= 2.0)])
    check("1h donor ทุกตัวมีแถวใน kerning_table (<= U+016B)", max(cps) <= 0x16B,
          "สูงสุด U+%04X" % max(cps))

    check("2  ไม่แตะ ASCII ที่ใช้พิมพ์อังกฤษ",
          not [c for c in cps if 0x20 <= c <= 0x7E],
          "ต่ำสุด U+%04X" % min(cps))

    en_used, have = en_used_codepoints()
    check("3  ไม่ชน codepoint ที่ EN ใช้", have and not (set(cps) & set(en_used)),
          "EN ใช้ %d ตัวในช่วง pool" % len(en_used))

    # ---- 4-5: วิ่งกับคลังแปลจริงทั้งหมด ----
    n_str = n_cell = 0
    bad_roundtrip = []
    for name, path in CORPORA.items():
        p = paths.Path(path)
        if not p.exists():
            continue
        vals = [v for v in json.load(io.open(p, encoding="utf-8")).values()
                if isinstance(v, str) and any(is_thai(c) for c in v)]
        for s in vals:
            enc = sm.encode(s)              # throw = ครอบคลุมไม่ครบ
            if sm.decode(enc) != s:
                bad_roundtrip.append((name, s))
            n_str += 1
            n_cell += len(thai_cells(s))
    check("4  decode(encode(s)) == s", not bad_roundtrip,
          "%d ประโยค / %d เซลล์" % (n_str, n_cell) if not bad_roundtrip
          else repr(bad_roundtrip[:2]))
    check("5  encode ทั้งคลังไม่ throw", n_str > 0, "%d ประโยค" % n_str)

    have = set(sm.base) | {k[0] for k in sm.mark}
    missing = [c for c in MANDATORY if c not in have]
    check("6  ฐาน/มาร์กไทยครบทุกตัว", not missing, "ขาด: " + "".join(missing))

    print()
    print("สรุป: %d ผ่าน / %d ตก" % (N_CHECKS - len(FAILS), len(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
