#!/usr/bin/env python3
"""เข้ารหัสไทย <-> donor codepoint ของฟอนต์ Y6 (j/gothic.bin, j/mincho.bin) — เวอร์ชัน 2:
PRE-COMPOSED CLUSTER GLYPH (เปลี่ยนจาก v1 ที่ใช้เทคนิค "มาร์ก advance=0 ซ้อนทับพยัญชนะ" แบบ
K2R/pirate เพราะ **พิสูจน์แล้วจาก in-game PoC ว่าเอนจิน Y6 เลย์เอาต์ทุก glyph แบบ full-width
เสมอ ไม่สนใจ advance=0 เลย** — สระ/วรรณยุกต์ที่ควรลอยซ้อนพยัญชนะเลยกลายเป็นตัวอักษรแยกเต็ม
ความกว้างวางเรียงข้าง ๆ กันแทน (พิสูจน์เพิ่มจาก subtitle ญี่ปุ่นในภาพเดียวกันที่ก็เต็มความกว้าง
เท่ากันหมดเช่นกัน — ไม่ใช่บั๊กเฉพาะจุด)

v2 = ประกอบ "cluster" (พยัญชนะ + สระ/วรรณยุกต์ที่ประกบ) เป็น **glyph เดียวเสร็จสรรพ** ก่อน
inject (คนละ donor cp ต่อ 1 cluster) วิธีนี้ไม่ต้องพึ่ง advance=0 อีกต่อไป เพราะไม่มีการซ้อน
glyph ตอน runtime เลย — ทุกอย่างวาดเสร็จเป็นภาพเดียวตั้งแต่ตอน build ฟอนต์

โครงสร้าง cell (นิยามเดียวกับที่ scripts/gen_cluster_slotmap.py ใช้ segment corpus):
  cell = พยัญชนะ (U+0E01-0E2E) + สระบน/ล่างไม่เกิน 1 ตัว (ั ิ ี ึ ื ็ ํ / ฺ ุ ู) +
         วรรณยุกต์/การันต์ไม่เกิน 1 ตัว (่ ้ ๊ ๋ ์)
  ตัวที่ไม่เข้าเกณฑ์ข้างต้น (พยัญชนะเดี่ยวไม่มีมาร์ก, สระเดี่ยว/เลขไทย/ฯลฯ, หรือมาร์กลอยไม่มี
  พยัญชนะนำ) -> ผ่าน **ตาราง 83 ตัวเดิม** (scripts/y6_slotmap.py, ไม่เปลี่ยน — ยังใช้ได้เพราะ
  ตัวเหล่านี้มี advance เดี่ยวปกติอยู่แล้ว ไม่เคยต้องพึ่ง advance=0)
  cluster ที่มีมาร์ก -> ตาราง scripts/y6_slotmap_clusters.py (generated, 2,990 cluster ครอบคลุม
  พยัญชนะ 46 x mark-combo 65 แบบทั้งหมดที่เป็นไปได้ตามหลักภาษาไทย)

encode()/decode() คง signature เดิมทุกประการ (ตัวอื่นในโปรเจกต์ apply_thai.py/
build_ja_carrier.py import แค่สองฟังก์ชันนี้ ไม่ต้องแก้)
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from y6_slotmap import ENCODE as BARE_ENCODE, DECODE as BARE_DECODE  # ตาราง 83 ตัวเดิม (ไม่แก้)
from y6_slotmap_clusters import CLUSTER_MAP, DONOR_TO_CLUSTER          # ตาราง cluster (generated)

UPPER = set('ัิีึื็ํ')
LOWER = set('ฺุู')
TONE = set('่้๊๋์')
COMBINING = UPPER | LOWER | TONE
assert len(COMBINING) == 15


def is_cons(c):
    return 0x0E01 <= ord(c) <= 0x0E2E


def _segment(s):
    """ไทย (Unicode ปกติ) -> list ของ 'unit': ('cluster', base, vmark, tmark) หรือ ('bare', ch)
    เดินตรรกะเดียวกับ gen_cluster_slotmap.py เป๊ะ (ต้องตรงกันเสมอ ไม่งั้น cluster หลุด)"""
    n = len(s); out = []; i = 0
    while i < n:
        c = s[i]
        if is_cons(c):
            j = i + 1
            vmark = tmark = None
            extra = []
            while j < n and s[j] in COMBINING:
                m = s[j]
                if m in TONE:
                    if tmark is None:
                        tmark = m
                    else:
                        extra.append(m)
                else:
                    if vmark is None:
                        vmark = m
                    else:
                        extra.append(m)
                j += 1
            if extra:
                raise ValueError(
                    f"cluster ผิดปกติ (มาร์กเกิน 1 ตัวต่อหมวดในตัวเดียวกัน): "
                    f"{s[i:j]!r} ที่ตำแหน่ง {i} ในข้อความ {s!r} — เกินขอบเขตที่ gen_cluster_slotmap "
                    f"รองรับ (พยัญชนะ + สระ 1 ตัว + วรรณยุกต์ 1 ตัว เท่านั้น) ต้องแก้คำแปลหรือขยาย schema")
            # 'ำ' (U+0E33) = นิคหิต + สระอา · ต้องแตกออก ไม่งั้นวงกลมไปอยู่เหนือ 'า'
            # แทนที่จะอยู่เหนือพยัญชนะตัวหน้า (ผู้ใช้เห็นจากจอจริง 28 ก.ค.)
            # -> cluster(พยัญชนะ + ํ [+ วรรณยุกต์]) แล้วตามด้วย bare 'า'
            sara_am = False
            if j < n and s[j] == 'ำ':
                if vmark is not None:
                    raise ValueError(
                        f"'ำ' ตามหลังสระบนอื่น ({vmark!r}) ที่ตำแหน่ง {j} ในข้อความ {s!r} "
                        f"— รูปนี้ไม่รองรับ ต้องแก้คำแปล")
                vmark = 'ํ'
                sara_am = True
                j += 1
            if vmark is None and tmark is None:
                out.append(('bare', c))
            else:
                out.append(('cluster', c, vmark, tmark))
            if sara_am:
                out.append(('bare', 'า'))
            i = j
        else:
            out.append(('bare', c))
            i += 1
    return out


def encode(s):
    """ไทย (Unicode ปกติ) -> สตริง donor-slot: cluster (พยัญชนะ+มาร์ก) -> 1 ตัวอักษร cluster
    donor, ตัวเดี่ยว -> ตาราง 83 เดิม, อื่นๆ (ASCII/เลขอารบิก/ฯลฯ) ผ่านตรงตามเดิม
    raise ValueError พร้อมข้อความชัดเจนถ้าเจอ cluster ที่ไม่มีใน CLUSTER_MAP (ให้ QC จับได้)"""
    out = []
    for unit in _segment(s):
        if unit[0] == 'cluster':
            _, base, vmark, tmark = unit
            key = (base, vmark, tmark)
            donor = CLUSTER_MAP.get(key)
            if donor is None:
                label = base + (vmark or '') + (tmark or '')
                raise ValueError(
                    f"ไม่มี cluster donor สำหรับ {label!r} (base={base!r} vmark={vmark!r} "
                    f"tmark={tmark!r}) ในข้อความ {s!r} — ต้อง regenerate "
                    f"scripts/y6_slotmap_clusters.py (รัน gen_cluster_slotmap.py) หรือแจ้ง lead "
                    f"ว่า pool ไม่พอ")
            out.append(chr(donor))
        else:
            _, ch = unit
            out.append(chr(BARE_ENCODE[ch]) if ch in BARE_ENCODE else ch)
    return ''.join(out)


def decode(s):
    """สตริง donor-slot -> ไทย Unicode ปกติ (undo ทั้ง cluster และตาราง 83 เดิม)"""
    out = []
    for c in s:
        cp = ord(c)
        if cp in DONOR_TO_CLUSTER:
            base, vmark, tmark = DONOR_TO_CLUSTER[cp]
            out.append(base)
            if vmark:
                out.append(vmark)
            if tmark:
                out.append(tmark)
        else:
            out.append(BARE_DECODE.get(cp, c))
    # ประกอบ 'ำ' กลับ: <พยัญชนะ> ํ [วรรณยุกต์] า  ->  <พยัญชนะ> [วรรณยุกต์] ำ
    t = ''.join(out)
    res = []
    i = 0
    while i < len(t):
        if t[i] == 'ํ':
            k = i + 1
            tone = ''
            if k < len(t) and t[k] in TONE:
                tone = t[k]
                k += 1
            if k < len(t) and t[k] == 'า':
                res.append(tone + 'ำ')
                i = k + 1
                continue
        res.append(t[i])
        i += 1
    return ''.join(res)


def coverage(text):
    """คืนรายชื่อ 'หน่วย' ไทยใน text ที่ยังไม่มีทาง encode ได้ (cluster ไม่อยู่ใน CLUSTER_MAP,
    หรือตัวเดี่ยวไม่อยู่ในตาราง 83) — สตริงรูปแบบ base+vmark+tmark ต่อ 1 รายการที่ขาด"""
    missing = set()
    try:
        units = _segment(text)
    except ValueError as exc:
        missing.add(f'<segment-error: {exc}>')
        return sorted(missing)
    for unit in units:
        if unit[0] == 'cluster':
            _, base, vmark, tmark = unit
            if (base, vmark, tmark) not in CLUSTER_MAP:
                missing.add(base + (vmark or '') + (tmark or ''))
        else:
            _, ch = unit
            if 0x0E00 <= ord(ch) <= 0x0E7F and ch not in BARE_ENCODE:
                missing.add(ch)
    return sorted(missing)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    import json
    for w in ['เกมใหม่', 'เล่นต่อ', 'ตั้งค่า', 'มินิเกม', 'ซื้อ', 'ที่นี่',
              'สวัสดีครับ ผมชื่อคาซึมะ คิริว', 'น้ำ', 'บทที่ 1: พายุฝน',
              'โอโนมิจิ จังหวัดฮิโรชิม่า', 'กฎแห่งสายเลือด', 'ปั้น เที่ยง']:
        e = encode(w)
        print(f'{w:32s} -> {" ".join("%04X" % ord(c) for c in e)}  decode_ok={decode(e) == w}')
    if len(sys.argv) > 1:
        m = json.load(io.open(sys.argv[1], encoding='utf-8'))
        allth = ''.join(v for v in m.values() if isinstance(v, str))
        miss = coverage(allth)
        print(f'\nหน่วยไทยใน {sys.argv[1]} ที่ยังไม่มีใน map: {len(miss)}')
        print('  ', ' '.join(f'{c!r}' for c in miss))
