#!/usr/bin/env python3
"""กวาด "ภาษาอังกฤษที่ยังแปลไม่ครบ" ทั้งเกม (db.judge.en.par) → translations/review/english/report.md

เจ้าของสั่ง 29 ก.ย. 2026: "รวมถึงกวาดส่วนที่เป็นภาษาอังกฤษที่แปลไม่ครบด้วย" + "บางประโยคเจอ I... แทนที่จะเป็น ฉัน หรือ ผม"

สามกอง (ตรวจจากไฟล์เกมจริง ไม่ใช่จาก worklist):
  A. ตกคิวแปล — ข้อความแสดงผลที่ไม่มีใน master_th เลย จึงขึ้นเป็นอังกฤษในเกม
     สาเหตุหลัก: `extract_all_en.is_translatable` ต้องมีอักษรละติน >= 2 ตัว → บรรทัดติดอ่าง "I..." ถูกตัดทิ้งตั้งแต่ extract
     (และ "I-I..." หลุดเพราะมีขีด) · เจอทั้งในคอลัมน์แทร็กที่สองของคัตซีน (auth.bin คอลัมน์ 5) และบทพูดเดิน
  B. มีอังกฤษปน — คำละตินในประโยคไทย หลังหักคำที่ตั้งใจคง EN (`check_latin_leftovers.KEEP_EN` + @handle/#hashtag)
  C. คงอังกฤษทั้งบรรทัด — คู่ใน master ที่ค่าไม่มีอักษรไทย (ตัดข้อความจีน/ไลเซนส์/รหัสออก) → ให้ lead/เจ้าของคัดว่า
     "ตั้งใจคง" (ชื่อเกม/แบรนด์) หรือ "ต้องแปล"
ไม่ครอบคลุม: ตัวหนังสือบนรูป (texture) และข้อความใน exe — ต้องดูจากภาพหน้าจอ (ดู docs/polish_plan.md)

ใช้:  python scripts/find_english_leftovers.py        # เขียน translations/review/english/report.md + items.json
"""
import io
import json
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import paths
from check_latin_leftovers import KEEP_EN
from check_latin_leftovers import scan as latin_scan
from make_worklist import DENY_BINS, KEEP_EN_BINS

OUT = paths.REVIEW / "english"
THAI_RE = re.compile(r"[฀-๿]")
CJK_RE = re.compile(r"[　-ヿ㐀-鿿＀-￯]")
TAG_RE = re.compile(r"<[^>]*>|\$\{[^}]*\}|%[0-9]*\$?[sdxufi%]")
IDENT_RE = re.compile(r"[_\\/]|\.(?:dds|bin|par|png|gmd|txt)\b|^[a-z0-9]+$|^[A-Z0-9]+[0-9][A-Z0-9]*$")
TEST_BINS_RE = re.compile(r"^(db2?_|db_example|db_unittest|test)")
DIALOG_BINS = {"auth.bin", "sound_auth.bin", "talk.bin", "talk_select_select.bin", "pause_message.bin", "msg.bin"}


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def walk(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if not str(k).startswith("reARMP"):
                walk(v, out)
    elif isinstance(o, list):
        for v in o:
            walk(v, out)
    elif isinstance(o, str):
        out.append(o)


def looks_display(s):
    """สตริงนี้น่าจะเป็นข้อความที่ผู้เล่นเห็น (ไม่ใช่ identifier/รหัส)"""
    t = TAG_RE.sub("", s).strip()
    if not re.search(r"[A-Za-z]", t) or CJK_RE.search(t) or THAI_RE.search(t) or IDENT_RE.search(t):
        return False
    if len(t) > 400:
        return False
    return bool(" " in t or "\n" in t or re.search(r"[.!?…,:]$", t) or re.fullmatch(r"[A-Z][a-z]+", t))


def skip_bin(b):
    return b in DENY_BINS or b in KEEP_EN_BINS or TEST_BINS_RE.match(b)


def main():
    master = load(paths.MASTER_TH)
    where = defaultdict(set)           # คีย์ EN → bin ที่ใช้ (จาก strings_by_bin)
    for b, strs in load(paths.EXTRACTED / "strings_by_bin.json").items():
        for s in strs:
            where[s].add(b)

    # A. ตกคิวแปล — เดินทุกสตริงของทุก bin จริง
    missing = defaultdict(Counter)
    for fp in sorted((paths.DB_EN / "en").glob("*.bin.json")):
        b = fp.name[:-5]
        if skip_bin(b):
            continue
        strs = []
        walk(load(fp), strs)
        for s in strs:
            if s not in master and looks_display(s):
                missing[s][b] += 1

    # B. มีอังกฤษปน
    hits, _w = latin_scan([(en, th) for en, th in master.items() if isinstance(th, str)])
    mixed = defaultdict(list)
    for en, th in master.items():
        if not isinstance(th, str) or not THAI_RE.search(th):
            continue
        h, _ = latin_scan([(en, th)])
        for term in h:
            mixed[term].append(en)

    # C. คงอังกฤษทั้งบรรทัด
    kept = defaultdict(list)
    for en, th in master.items():
        if not isinstance(th, str) or THAI_RE.search(th) or CJK_RE.search(th):
            continue
        bins = sorted(b for b in where.get(en, ()) if not skip_bin(b))
        if not bins or not re.search(r"[A-Za-z]", TAG_RE.sub("", th)):
            continue
        low = " ".join(TAG_RE.sub("", th).lower().split())
        intent = "ตั้งใจ (KEEP_EN)" if low.strip(" .!?") in KEEP_EN else ("ข้อความบทพูด" if set(bins) & DIALOG_BINS else "ชื่อ/ป้าย")
        kept[intent].append((en, bins))

    OUT.mkdir(parents=True, exist_ok=True)
    esc = lambda s: str(s).replace("\n", "\\n").replace("|", "\\|")
    out = ["# อังกฤษที่ยังแปลไม่ครบ — ทั้งเกม (db.judge.en.par)", "",
           "สร้างด้วย `python scripts/find_english_leftovers.py` · ไม่ครอบคลุมตัวหนังสือบนรูป/ใน exe", "",
           "| กอง | ความหมาย | จำนวน |", "|---|---|---|",
           "| A | ตกคิวแปล (ไม่มีใน master → ขึ้นอังกฤษในเกม) | %d ข้อความ / %d จุด |" % (len(missing), sum(sum(c.values()) for c in missing.values())),
           "| B | คำอังกฤษปนในประโยคไทย (หลังหักคำที่ตั้งใจคง) | %d คำ / %d บรรทัด |" % (len(mixed), sum(len(v) for v in mixed.values())),
           "| C | คงอังกฤษทั้งบรรทัด | %s |" % " · ".join("%s %d" % (k, len(v)) for k, v in sorted(kept.items())), "",
           "## A. ตกคิวแปล", "", "| EN | bin (จำนวนจุด) |", "|---|---|"]
    out += ["| `%s` | %s |" % (esc(s), ", ".join("%s (%d)" % kv for kv in c.most_common()))
            for s, c in sorted(missing.items(), key=lambda x: -sum(x[1].values()))]
    out += ["", "## B. คำอังกฤษปนในประโยคไทย", "", "| คำ | บรรทัด | ตัวอย่าง EN |", "|---|---|---|"]
    out += ["| %s | %d | `%s` |" % (esc(t), len(v), esc(v[0])[:90]) for t, v in sorted(mixed.items(), key=lambda x: -len(x[1]))]
    for intent in ("ข้อความบทพูด", "ชื่อ/ป้าย", "ตั้งใจ (KEEP_EN)"):
        rows = kept.get(intent, [])
        out += ["", "## C. คงอังกฤษทั้งบรรทัด — %s (%d)" % (intent, len(rows)), "", "| EN (= ค่าที่แสดง) | bin |", "|---|---|"]
        out += ["| `%s` | %s |" % (esc(en)[:90], ", ".join(bins[:4])) for en, bins in sorted(rows, key=lambda x: x[1])]
    (OUT / "report.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    items = {"missing": {s: dict(c) for s, c in missing.items()}, "mixed": mixed,
             "kept": {k: [[en, bins] for en, bins in v] for k, v in kept.items()}}
    (OUT / "items.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print("A ตกคิวแปล %d ข้อความ · B อังกฤษปน %d คำ · C คงอังกฤษ %s → %s" % (
        len(missing), len(mixed), " · ".join("%s %d" % (k, len(v)) for k, v in sorted(kept.items())), OUT / "report.md"))


if __name__ == "__main__":
    main()
