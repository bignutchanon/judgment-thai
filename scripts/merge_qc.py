#!/usr/bin/env python3
"""รวมคำแปลจาก `translations/done/*.done.json` เข้า `master_th.json` พร้อม QC อัตโนมัติ

**นี่คือทางเดียวที่เขียน `master_th.json` ได้** (กติกาเหล็กข้อ 4) — คู่ที่ไม่ผ่านด่านจะไม่ถูกรวม
และถูกส่งกลับให้ผู้แปลแก้ผ่าน `translations/qc_failures.json`

ด่านตรวจต่อคู่ (EN -> TH):
  K  ครบ:        ทุก key ของ batch ต้องมีใน done (ขาด = รายงาน ไม่ทำให้คู่อื่นตก)
  E  ไม่ว่าง
  N  จำนวนขึ้นบรรทัด (\\n) เท่ากับต้นฉบับ — กล่องข้อความในเกมตัดบรรทัดตายตัว
  T  tag/placeholder ครบและเท่ากัน: `<...>`, `${...}`, `%s/%d/%1$s`, `~...~`
  C  อักษร CJK/คานะที่มีใน EN ต้องอยู่ครบใน TH (ชื่อร้าน/ป้ายญี่ปุ่นห้ามหาย)
  X  encode ได้จริงด้วย `SlotMap` — ทุกกลิฟไทยต้องมีเซลล์ในฟอนต์ (ไม่งั้นขึ้น tofu)
  S  ห้ามมีอักษรที่ถูกใช้เป็น donor ของกลิฟไทย (เช่น À Ò ā) ปนในข้อความ — จะกลายเป็นไทยมั่วบนจอ
  P  สรรพนามต้องจับคู่ระดับเดียวกันตาม PRONOUN_MATRIX §0 (ผม/คุณ · ฉัน/แก · กู/มึง)
  L  ยาวเกิน 1.8x ของ EN = เตือน (ไม่ตก)
TH == EN ถือว่า "คงต้นฉบับ" (ระบบ/enum/ชื่อเฉพาะ) — ผ่าน แต่ยังตรวจ S เพราะตัวอักษรชน donor
ก็เพี้ยนบนจอแม้จะคง EN ไว้

ใช้:
  python scripts/merge_qc.py              # ตรวจ + รวมเข้า master_th.json
  python scripts/merge_qc.py --dry-run    # ตรวจอย่างเดียว ไม่เขียน
  python scripts/merge_qc.py --only 003   # เฉพาะ batch ที่ระบุ
"""
import argparse
import io
import json
import os
import re
import sys
from collections import Counter, OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from check_pronoun_pairs import check_text as pronoun_problems

TAG_RE = re.compile(r"<[^<>]*>|%[0-9]*\$?[sdxufi%]|\$\{[^}]*\}|~[^~\s]{0,40}~")
CJK_RE = re.compile(r"[ᄀ-ᇿ぀-ヿ㐀-鿿가-힯ｦ-ﾟ]")
THAI_RE = re.compile(r"[฀-๿]")

DONE = paths.TRANSLATIONS / "done"
# บรรทัดที่ "ผสมระดับสรรพนามโดยตั้งใจ" (เช่น ตัวร้ายใช้ "คุณ" แบบประชด ขณะแทนตัวว่า "กู")
# ใส่ EN key ไว้ที่นี่พร้อมเหตุผล แล้วด่าน P จะข้ามให้ — ต้องมีเหตุผลกำกับเสมอ ห้ามใช้กลบความผิดพลาด
PRONOUN_EXCEPTIONS = paths.TRANSLATIONS / "pronoun_exceptions.json"
REPORT = paths.TRANSLATIONS / "qc_report.md"
FAILURES = paths.TRANSLATIONS / "qc_failures.json"


def load_slotmap():
    """คืน (SlotMap, ชุดตัวอักษร donor) — ถ้ายังไม่มี slotmap ให้ข้ามด่าน X/S พร้อมเตือน"""
    try:
        from slot_alloc import SLOTMAP, SlotMap
        if not SLOTMAP.exists():
            return None, set()
        sm = SlotMap.load(SLOTMAP)
        return sm, {chr(cp) for cp in sm.dec}
    except Exception as e:  # noqa: BLE001 — QC ต้องรันได้แม้ระบบฟอนต์ยังไม่พร้อม
        print("!! โหลด slotmap ไม่ได้ (ข้ามด่าน X/S): %s" % e)
        return None, set()


def load_exceptions():
    if PRONOUN_EXCEPTIONS.exists():
        return json.load(io.open(PRONOUN_EXCEPTIONS, encoding="utf-8"))
    return {}


def check_pair(en, th, sm, donor_chars, exceptions=()):
    fails, warns = [], []
    if not isinstance(th, str) or not th.strip():
        return ["E: ว่าง"], warns

    hits = sorted({c for c in th if c in donor_chars})
    if hits:
        fails.append("S: มีอักษรที่ชน donor ฟอนต์ %s (จะขึ้นเป็นตัวไทยมั่วบนจอ)" % " ".join(hits))

    if th == en:
        return fails, warns + ["= EN (คงต้นฉบับ)"]

    if en.count("\n") != th.count("\n"):
        fails.append("N: ขึ้นบรรทัดไม่เท่าต้นฉบับ (EN %d / TH %d)" % (en.count("\n"), th.count("\n")))

    en_tags, th_tags = Counter(TAG_RE.findall(en)), Counter(TAG_RE.findall(th))
    if en_tags != th_tags:
        miss = list((en_tags - th_tags).elements())
        extra = list((th_tags - en_tags).elements())
        fails.append("T: tag ไม่ตรง ขาด %s เกิน %s" % (miss or "-", extra or "-"))

    en_cjk, th_cjk = Counter(CJK_RE.findall(en)), Counter(CJK_RE.findall(th))
    if en_cjk - th_cjk:
        fails.append("C: อักษรญี่ปุ่น/CJK หาย %s" % "".join((en_cjk - th_cjk).elements()))

    if sm is not None and THAI_RE.search(th):
        try:
            sm.encode(th)
        except SystemExit as e:
            fails.append("X: encode ไม่ผ่าน — %s" % str(e).split("\n")[0][:120])

    if en in exceptions:
        warns.append("P: ข้ามด่านสรรพนามตามรายการยกเว้น — %s" % exceptions[en])
    else:
        for pr in pronoun_problems(th):
            fails.append("P: " + pr)

    if len(th) > len(en) * 1.8 + 10:
        warns.append("L: ยาว %d ตัวอักษร (EN %d)" % (len(th), len(en)))
    return fails, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="เลข batch เช่น 003 หรือ TALK_007")
    a = ap.parse_args()

    sm, donor_chars = load_slotmap()
    exceptions = load_exceptions()
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8")) if paths.MASTER_TH.exists() else {}
    master = OrderedDict(master)

    files = sorted(DONE.glob("*.done.json")) if DONE.exists() else []
    if a.only:
        files = [f for f in files if a.only in f.name]
    if not files:
        print("ไม่พบไฟล์ใน translations/done/ (ยังไม่มีคำแปลส่งเข้ามา)")
        return 0

    added = kept = failed = 0
    failures = OrderedDict()
    lines = ["# QC report — JETH", ""]
    for f in files:
        data = json.load(io.open(f, encoding="utf-8"))
        strings = data.get("strings", data)
        batch_id = data.get("batch", f.name)
        src = paths.WORKLIST / ("batch_%s.json" % batch_id) if isinstance(batch_id, str) else None
        expected = None
        if src and src.exists():
            expected = list(json.load(io.open(src, encoding="utf-8"))["strings"].keys())

        b_added = b_fail = b_kept = 0
        for en, th in strings.items():
            fails, warns = check_pair(en, th, sm, donor_chars, exceptions)
            if fails:
                failures.setdefault(f.name, {})[en] = {"th": th, "fails": fails}
                b_fail += 1
                continue
            if th == en:
                b_kept += 1
            master[en] = th
            b_added += 1
        missing = [k for k in (expected or []) if k not in strings]
        added += b_added
        failed += b_fail
        kept += b_kept
        lines.append("- `%s`: ผ่าน %d (คง EN %d) · ตก %d · ขาด %d"
                     % (f.name, b_added, b_kept, b_fail, len(missing)))
        if missing:
            failures.setdefault(f.name, {})["__missing__"] = missing[:50]
        print("%-32s ผ่าน %4d  ตก %3d  ขาด %3d" % (f.name, b_added, b_fail, len(missing)))

    lines += ["", "รวม: ผ่าน %d · คง EN %d · ตก %d · master_th ตอนนี้ %d คู่"
              % (added, kept, failed, len(master))]
    if not a.dry_run:
        io.open(paths.MASTER_TH, "w", encoding="utf-8", newline="\n").write(
            json.dumps(master, ensure_ascii=False, indent=1) + "\n")
        io.open(REPORT, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
        io.open(FAILURES, "w", encoding="utf-8", newline="\n").write(
            json.dumps(failures, ensure_ascii=False, indent=1) + "\n")
    print()
    print("รวม: ผ่าน %d · คง EN %d · ตก %d%s" % (added, kept, failed,
          "" if a.dry_run else " · master_th %d คู่" % len(master)))
    if failures and not a.dry_run:
        print("รายละเอียดที่ตก: translations/qc_failures.json")
    elif failures:
        # โหมด dry-run ไม่เขียนไฟล์ — พิมพ์ตัวที่ตกออกมาเลย ไม่งั้นผู้แปลหาไม่เจอ
        for fname, items in failures.items():
            for en, info in list(items.items())[:20]:
                if en == "__missing__":
                    print("  ขาด %d key" % len(info)); continue
                print("  [%s] %s" % (fname, en.replace(chr(10), " / ")[:70]))
                for f in info["fails"]:
                    print("      - " + f)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
