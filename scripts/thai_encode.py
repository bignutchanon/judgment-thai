#!/usr/bin/env python3
"""เข้ารหัสไทย <-> codepoint slot ของ SDF font (system_main_en_all_sdf) — เวอร์ชัน K2R
แนว glyph-remapping เดียวกับที่ pirate ship จริง แต่ slot map ออกแบบใหม่สำหรับ K2R:

- donor = บล็อก Cyrillic ล้วน U+0400..U+0452 (83 slot ติดกัน, K2R มี Cyrillic 136 slot)
  * ไม่แตะ ASCII 0x20-0x7E เลย (ตัวเลข/ชื่ออังกฤษ/tag ในเกมยังแสดงปกติ)
  * ไม่แตะ Latin-1 (é ü ® ฯลฯ ที่โผล่ในข้อความเกมได้) — ต่างจากม็อด AI v1.3 ที่ทับ Latin-1
- ไทย 83 ตัว เรียงตาม codepoint ไทย map ไปยัง donor เรียงตามลำดับ:
    U+0E01..U+0E3A (พยัญชนะ ก-ฮ 44 + ฤ ฦ + ฯ + ะ ั า ำ ิ ี ึ ื ุ ู ฺ)  -> U+0400..U+0439
    U+0E3F ฿                                                        -> U+043A
    U+0E40..U+0E4D (เ แ โ ใ ไ ๅ ๆ ็ ่ ้ ๊ ๋ ์ ํ)                       -> U+043B..U+0448
    U+0E50..U+0E59 (๐-๙)                                             -> U+0449..U+0452
  (สูตร: ดู _SEGMENTS ข้างล่าง — decode กลับได้ด้วยตารางเดียวกัน)

พฤติกรรม encode (เหมือน pirate):
- สระบน/สระล่าง/วรรณยุกต์ (combining marks) ถูก reorder ไป "หน้า" พยัญชนะฐาน
  (glyph มาร์กใน font ตั้ง advance=0 + bearingX บวก -> มาร์กวาดที่ pen ก่อน
   แล้วพยัญชนะ (advance เต็ม) วาดทับตำแหน่งเดียวกัน -> มาร์กลอยบน/ล่างพยัญชนะ)
- ตัวที่ไม่อยู่ใน map (ASCII อังกฤษ/เลข/วรรคตอน) ส่งผ่านตามเดิม

ฟอนต์คู่กัน: build/font/system_main_en_all_sdf.bin สร้างโดย scripts/inject_thai_sdf.py
ตารางเต็ม + ค่า metrics: docs/font_k2r_slotmap.md
"""

# ---- ตาราง slot: (thai_start, thai_end_inclusive) เรียงต่อกันลง donor 0x0400.. ----
_SEGMENTS = [(0x0E01, 0x0E3A), (0x0E3F, 0x0E3F), (0x0E40, 0x0E4D), (0x0E50, 0x0E59)]
DONOR_BASE = 0x0400

THAI_CHARS = []
for _a, _b in _SEGMENTS:
    THAI_CHARS += [chr(c) for c in range(_a, _b + 1)]
assert len(THAI_CHARS) == 83

# donor slot (codepoint Cyrillic) -> ตัวอักษรไทย
DECODE = {DONOR_BASE + i: th for i, th in enumerate(THAI_CHARS)}
# ไทย -> donor slot
ENCODE = {th: cp for cp, th in DECODE.items()}
assert all(not (0x20 <= cp <= 0x7E) for cp in DECODE), 'donor ต้องไม่ใช่ ASCII'

# combining marks ที่ต้อง reorder ไปหน้าพยัญชนะฐาน (advance=0 ใน font):
#   สระบน ั ิ ี ึ ื ็ ํ + วรรณยุกต์ ่ ้ ๊ ๋ + การันต์ ์ + สระล่าง ุ ู ฺ
# (ำ เป็นสระเรียงมี advance ไม่ reorder — พฤติกรรมเดิมของ pirate)
COMBINING = set('ัิีึื็ํ่้๊๋์ฺุู')

def is_cons(c):
    return 0x0E01 <= ord(c) <= 0x0E2E

def encode(s):
    """ไทย (Unicode ปกติ) -> สตริง codepoint slot (มาร์กเรียงก่อนพยัญชนะฐาน)"""
    n = len(s); out = []; i = 0
    while i < n:
        c = s[i]
        if is_cons(c):
            j = i + 1; marks = []
            while j < n and s[j] in COMBINING:
                marks.append(s[j]); j += 1
            if marks:
                for m in marks:                                        # มาร์กก่อน
                    out.append(chr(ENCODE[m]) if m in ENCODE else m)
                out.append(chr(ENCODE[c]) if c in ENCODE else c)       # พยัญชนะหลัง
                i = j; continue
        out.append(chr(ENCODE[c]) if c in ENCODE else c)
        i += 1
    return ''.join(out)

_COMBINING_SLOTS = {chr(ENCODE[m]) for m in COMBINING}

def decode(s):
    """สตริง codepoint slot -> ไทย Unicode ปกติ (undo ทั้ง map และการ reorder มาร์ก)"""
    n = len(s); out = []; i = 0
    while i < n:
        c = s[i]
        if c in _COMBINING_SLOTS:
            j = i; marks = []
            while j < n and s[j] in _COMBINING_SLOTS:
                marks.append(DECODE[ord(s[j])]); j += 1
            if j < n and ord(s[j]) in DECODE and is_cons(DECODE[ord(s[j])]):
                out.append(DECODE[ord(s[j])]); out.extend(marks)       # ฐานก่อน มาร์กตาม
                i = j + 1; continue
            out.extend(marks); i = j; continue                         # มาร์กลอย (ไม่มีฐานตาม)
        out.append(DECODE.get(ord(c), c))
        i += 1
    return ''.join(out)

def coverage(text):
    """คืนรายชื่อตัวอักษรไทยใน text ที่ยังไม่มีใน ENCODE"""
    return sorted({c for c in text if 0x0E00 <= ord(c) <= 0x0E7F and c not in ENCODE})

if __name__ == '__main__':
    import sys, io, json
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    for w in ['เกมใหม่', 'เล่นต่อ', 'ตั้งค่า', 'มินิเกม', 'ซื้อ', 'ที่นี่',
              'สวัสดีครับ ผมชื่อคาซึมะ คิริว', 'น้ำ', 'บทที่ 1: พายุฝน']:
        e = encode(w)
        print(f'{w:32s} -> {" ".join("%04X" % ord(c) for c in e)}  decode_ok={decode(e) == w}')
    if len(sys.argv) > 1:
        m = json.load(io.open(sys.argv[1], encoding='utf-8'))
        allth = ''.join(v for v in m.values() if isinstance(v, str))
        miss = coverage(allth)
        print(f'\nตัวอักษรไทยใน {sys.argv[1]} ที่ยังไม่มีใน map: {len(miss)}')
        print('  ', ' '.join(f'{c}(U+{ord(c):04X})' for c in miss))
