#!/usr/bin/env python3
"""แทรกช่องว่างที่ "ขอบคำ" ในข้อความไทยยาว เพื่อให้เอนจิ้นตัดบรรทัดได้

ปัญหา (K3 เจอ 30 ก.ค. 2026 หน้าประวัติตัวละคร · Judgment เจอ 5 ก.ย. 2026 หน้า CASE FILE — ผู้เล่นรายงาน "ตัวหนังสือตกกรอบ"):
  เอนจิ้น Dragon Engine ตัดบรรทัดที่ **ช่องว่าง** เท่านั้น · ภาษาไทยไม่มีช่องว่างระหว่างคำ
  → ทั้งประโยคนับเป็น "คำเดียว" ยาวเกินกล่อง → K3 เรียงเป็นแนวตั้ง · Judgment **ตัดทิ้งที่ขอบขวา**
  (CASE FILE: "…ตระกูลโทโจแห่งคาม|" ช่วงไทยติดกัน ~90 ตัว ขณะกล่องรับได้ ~75)
  (ในภาพ: สองบรรทัดแรกที่ผู้แปลใส่ช่องว่างไว้เรียงปกติ ส่วนที่ไม่มีช่องว่างพังทั้งท่อน)
  v1.2 ก็มีปัญหานี้ 4,363 รายการ = ปัญหาเก่าที่ไม่มีใครแก้ ไม่ใช่ของใหม่

วิธีแก้: ตัดคำไทยด้วย pythainlp (newmm) แล้วแทรกช่องว่าง **ที่ขอบคำเท่านั้น**
ให้ทุกช่วงอักษรไทยติดกันไม่เกิน MAX_RUN ตัว → เอนจิ้นมีจุดตัดบรรทัดให้ใช้
- **ไม่แทรกกลางคำ** (ตัดคำผิด = อ่านไม่รู้เรื่อง) · ไม่แตะแท็ก/`${...}`/`\\n` (เป็น ASCII อยู่นอกช่วงไทย)
- จำนวน `\\n` และแท็กไม่เปลี่ยน → ผ่าน QC ข้อ N/T/S/X เหมือนเดิม

MAX_RUN มาจากการวัดกล่องแคบสุดที่เจอ (หน้าประวัติตัวละคร ~45 ตัวอักษรไทย/บรรทัด)
ตั้ง 32 เผื่อไว้ เพราะฟอนต์เป็น proportional ความกว้างต่อตัวไม่เท่ากัน

ใช้:
  python scripts/fix_thai_wrap.py --check          # ดูตัวอย่างผลลัพธ์ ไม่เขียนไฟล์
  python scripts/fix_thai_wrap.py                  # แก้ที่ translations/done/ ต้นทาง
  python scripts/fix_thai_wrap.py --max-run 28     # เข้มขึ้น (กล่องแคบกว่า)
แล้วต่อด้วย remerge_stale.py --write + build_text.py + gen_font_bin.py + deploy_spoil.py
"""
import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths as PP
from pythainlp.corpus.common import thai_words
from pythainlp.tokenize import Tokenizer
from pythainlp.util import dict_trie

THAI_RUN = re.compile(r"[฀-๿]+")
# วัดจากกล่องแคบสุดที่เจอในเกม (หน้าประวัติตัวละคร): บรรทัด "อดีตหัวหน้าตระกูลชิงากิ
# หลังตระกูลโทโจล่มสลาย" = 44 ตัวอักษร พอดีบรรทัด → ช่วงที่ **ยาวเกิน 44** คือตัวที่พัง
# ตั้ง 44 เพื่อ **ไม่ไปแตะบทพูด/ซับที่กล่องกว้างพออยู่แล้ว** (เกณฑ์ 32 เคยแก้เกิน 9,326 จุด)
MAX_RUN = 60
TARGET = 30          # เวลาต้องแทรก ให้แต่ละช่วงสั้นกว่าเพดานไว้เผื่อ ำ ที่แตกเป็น 2 ตัวตอน encode และตัวนำ U+0165

_TK = None


def tokenizer():
    """newmm + **พจนานุกรมชื่อเฉพาะของโปรเจกต์** — กันตัวแบ่งคำผ่าชื่อทับศัพท์
    (เจอจริง: 'มอร์ติเมอร์' ถูกตัดเป็น 'มอร์ติ เมอร์')"""
    global _TK
    if _TK:
        return _TK
    protected = set()
    for f in ("glossary.md", "characters_main.json", "characters_side.json",
              "PRONOUN_MATRIX.md", "glossary.md"):
        p = PP.PROJECT / "translations" / f
        if p.exists():
            # เก็บทุกคำไทยยาว >=4 ตัวที่ปรากฏในเอกสารชื่อเฉพาะ = ถือเป็นคำเดียวห้ามผ่า
            protected.update(w for w in THAI_RUN.findall(p.read_text(encoding="utf-8"))
                             if 4 <= len(w) <= 30)
    _TK = Tokenizer(custom_dict=dict_trie(set(thai_words()) | protected), engine="newmm")
    print(f"พจนานุกรม: คำไทยมาตรฐาน + ชื่อเฉพาะโปรเจกต์ {len(protected):,} คำ (ห้ามผ่า)")
    return _TK


def split_run(run, max_run):
    """คืน run ที่แทรกช่องว่างที่ขอบคำ ให้ทุกช่วงยาวไม่เกิน max_run"""
    if len(run) <= max_run:
        return run
    words = tokenizer().word_tokenize(run)
    out, cur = [], ""
    for w in words:
        if cur and len(cur) + len(w) > TARGET:
            out.append(cur)
            cur = w
        else:
            cur += w
    if cur:
        out.append(cur)
    return " ".join(out)


def fix(th, max_run):
    if not th or not THAI_RUN.search(th):
        return th
    return THAI_RUN.sub(lambda m: split_run(m.group(0), max_run), th)


def worst(th):
    return max((len(x) for x in THAI_RUN.findall(th)), default=0)


# ---- ประมาณความกว้างกล่องต่อบิน (เพื่อไม่แทรกช่องว่างเกินจำเป็น) ----
# หลักการ: บินที่ **SEGA ตัดบรรทัด EN มาให้เองแล้ว** (บรรทัดสั้นสม่ำเสมอ) แปลว่าบรรทัดที่ยาวสุด
# ที่มันปล่อยไว้ยังพอดีกล่อง → ใช้ p99 ของความยาวบรรทัด EN เป็น "ขอบล่างของความกว้างกล่อง"
#   sound_auth.bin p99=76 · auth.bin p99=66  → กล่องซับกว้างกว่ากล่องบรรยายมาก
# บินที่ p99 สูงลิ่ว (talk.bin 153 · pause_profile 348) = SEGA ปล่อยให้เอนจิ้นตัดเอง
# → วัดจากข้อมูลไม่ได้ ใช้ค่าปลอดภัย MAX_RUN (44 = วัดจากกล่องบรรยายในเกมจริง)
PREBROKEN_MAX = 90     # p99 เกินนี้ = ไม่ใช่บินที่ตัดบรรทัดมาให้ → ใช้ค่าปลอดภัย
FLOOR = 36             # รอบ 20 (5 ก.ย. 2026): กติกาตัดบรรทัดจริงของเอนจิ้น (วัดจากภาพ CASE FILE 7 จุดตัด) =
                       # ช่องว่างถูกใช้ตัดบรรทัดก็ต่อเมื่อ "คำถัดไป" ยาวไม่เกิน ~40 ตัว (นับหลัง encode: ตัวนำ U+0165 +1 · ำ +1)
                       # คำที่ยาวกว่านั้นเอนจิ้นข้ามช่องว่างหน้าคำไปตัดที่ช่องว่างถัดไปแทน → บรรทัดล้นกรอบทั้งที่มีช่องว่าง
                       # (ตระกูลเคียวเรอิจากภูมิภาคคันไซกับตระกูลโทโจแห่ง 46 ตัว ล้น · จากประวัติความขัดแย้งอันวุ่นวายระหว่าง 37 ตัว ตัดได้)
                       # เกณฑ์จึงเป็นเรื่อง "ความยาวคำ" ไม่ใช่ความกว้างกล่อง → ใช้ค่าเดียวทุกบิน (36 ราว + ตัวนำ + ำ < 40)
                       # เดิม 60 (รอบ 19 แตะ 750 ข้อความ · เข้าใจผิดว่าเป็นความกว้างกล่อง) · 36 แตะ ~1,300


def box_width_per_bin():
    sbb = json.loads((PP.EXTRACTED / "strings_by_bin.json").read_text(encoding="utf-8"))
    box = {}
    for b, ss in sbb.items():
        lines = sorted(len(l) for s in ss for l in s.split("\n") if l.strip())
        if not lines:
            continue
        p99 = lines[max(0, int(len(lines) * 0.99) - 1)]
        # ⚠ p99 เป็นได้แค่ **ขอบล่าง** ของความกว้างกล่อง ไม่ใช่ค่าจริง —
        # บินที่เนื้อหาสั้นตามธรรมชาติ (ชื่อไอเทม/ป้ายปุ่ม) จะได้ p99 ต่ำ เช่น 38 ทั้งที่กล่องอาจกว้างกว่านั้น
        # ถ้าเอา p99 มาใช้ตรงๆ จะไปแทรกช่องว่างในข้อความที่ไม่มีปัญหา → ต้อง clamp ด้วย FLOOR เสมอ
        # รอบ 20: เพดานเป็นความยาว "คำ" ที่เอนจิ้นยอมตัดหน้ามัน ไม่ขึ้นกับความกว้างกล่อง → FLOOR ทุกบิน
        # (เก็บ p99 ไว้รายงานเฉย ๆ)
        box[b] = FLOOR
    return box, sbb


def threshold_per_string(box, sbb):
    """เกณฑ์ของแต่ละข้อความ = ค่าที่ **แคบสุด** ของบินที่มันโผล่
    (ข้อความเดียวใช้ได้หลายที่ ต้องรอดในกล่องที่แคบสุด)"""
    th = {}
    for b, ss in sbb.items():
        w = box.get(b, FLOOR)
        for s in ss:
            if s not in th or w < th[s]:
                th[s] = w
    return th


def main():
    check = "--check" in sys.argv
    force = int(sys.argv[sys.argv.index("--max-run") + 1]) if "--max-run" in sys.argv else None

    box, sbb = box_width_per_bin()
    limit = threshold_per_string(box, sbb)
    wide = {b: w for b, w in box.items() if w > FLOOR}
    print(f"กล่องกว้างกว่าค่าปลอดภัย {len(wide)} บิน (วัดจากบรรทัดที่ SEGA ตัดไว้เอง): "
          + " · ".join(f"{b.replace('.bin','')}={w}" for b, w in sorted(wide.items(),
                                                                        key=lambda x: -x[1])[:8]))

    files = changed = 0
    samples = []
    hist = {}
    for dp in sorted(PP.DONE.glob("batch_*.done.json")):
        d = json.loads(dp.read_text(encoding="utf-8"))
        strings = d.get("strings", {})
        n = 0
        for en, th in strings.items():
            if not isinstance(th, str):
                continue
            cap = force or limit.get(en, FLOOR)
            if worst(th) <= cap:
                continue
            new = fix(th, cap)
            if new == th:
                continue
            strings[en] = new
            n += 1
            hist[cap] = hist.get(cap, 0) + 1
            if len(samples) < 5:
                samples.append((worst(th), cap, th, new))
        if n:
            files += 1
            changed += n
            if not check:
                dp.write_text(json.dumps(d, ensure_ascii=False, indent=1),
                              encoding="utf-8", newline="\n")

    print(f"แก้ {changed:,} ข้อความ ใน {files} batch"
          + ("  (--check: ไม่ได้เขียนไฟล์)" if check else ""))
    print("แยกตามเกณฑ์ที่ใช้:",
          " · ".join(f"เกณฑ์ {k} ตัว: {v:,}" for k, v in sorted(hist.items())))
    for w, cap, was, now in samples:
        print(f"\n[ช่วงเดิม {w} ตัว · เกณฑ์ {cap}]")
        print(f"  เดิม: {was[:150]}")
        print(f"  ใหม่: {now[:170]}")
    if changed and not check:
        print("\nขั้นถัดไป: python scripts/remerge_stale.py --write → build_text.py → gen_font_bin.py → deploy_spoil.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
