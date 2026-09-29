#!/usr/bin/env python3
"""ตัดบทแปลเนื้อเรื่องหลักทีละบทเป็นชุดงาน "เกลา" (29 ก.ย. 2026 · แผนอยู่ที่ docs/polish_plan.md)

ต่างจากรอบตรวจก่อนหน้า (sweep/blind/register) ตรงที่ทำ **ทีละบทครบทุกแหล่งข้อความของบทนั้น** และเป้าหมายคือ
เขียนภาษาไทยให้ลื่นเป็นธรรมชาติ (ไม่ใช่แค่หาจุดผิด) — ผู้เกลาเห็น EN + TH + ผู้พูด/เพศ + บริบทบท

แหล่งข้อความของบท N (เรียงตามที่ผู้เล่นเจอโดยประมาณ — ภายในฉากเรียงตามลำดับจริง):
  บท 2+ : ทวนเรื่องย่อตอนเปิดบท `auth.bin` p{NN}_00100 (P00_Start / P01_* ไม่มีข้อความ — ฉากเปิดเกมอยู่ใน a01_)
  คัตซีน `auth.bin` a{NN}_* (เรียงตามเวลา · คอลัมน์ 4 และแทร็ก 5)
  ฉากพิเศษ `auth.bin` B{NN}_* / b{NN}_* (มีเฉพาะบท 1 5 9 11)
  เสียงพากย์ `sound_auth.bin` speech_list_judge_main_c{NN} (เรียงตามเลขฉาก+เลขบรรทัด · คอลัมน์ 4 และแทร็ก 6)
  บทพูดเดิน `talk.bin` judge_main_c{NN}
  ตัวเลือกบทสนทนา `talk_select_select.bin` M{NN}_* · เป้าหมายภารกิจ `mission_mission_kind.bin` judge_m_M{NN}_*

คีย์ EN เดียวกันในบทเดียวกันให้อ่านครั้งเดียว (ครั้งแรกที่เจอ) · master_th เป็น EN → ไทย ทั้งเกม จึงติดป้าย
`ใช้ร่วม` ให้คีย์ที่ถูกใช้นอกบทนี้ด้วย (บทอื่น/เควสเสริม/ระบบ) — ผู้เกลาแก้ได้เฉพาะเมื่อคำใหม่ใช้ได้ทุกบริบท

ใช้:  python scripts/make_polish_chunks.py --stats          # ขนาดทุกบท (ไม่เขียนไฟล์)
      python scripts/make_polish_chunks.py --chapter 1      # เขียน translations/review/polish/ch01/
เอาต์พุต: chunk_NN.tsv (id · ฉาก · ผู้พูด · หมายเหตุ · EN · TH — \n เขียนเป็น \n ตัวอักษร) · index.json (id → คีย์ EN)
          meta.json (id → bin/ตาราง/แถว/คอลัมน์/ผู้พูด/ป้าย) · context.md (เรื่องย่อบท + ตัวละครที่พูดในบท)
"""
import argparse
import io
import json
import re
import sys
from collections import Counter, OrderedDict, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import paths
from check_latin_leftovers import TAG_RE, THAI_RE
from check_latin_leftovers import scan as latin_scan

OUT_ROOT = paths.REVIEW / "polish"
CONTEXT = OUT_ROOT / "context"
FACTS = paths.EXTRACTED / "facts"
CINEMA = paths.TRANSLATIONS / "cinema_speakers"
SPEECH = paths.TRANSLATIONS / "speech_speakers"
CHUNK_CHARS = 38_000          # อักษรไทยต่อชิ้น (มี EN ด้วย → เล็กกว่า blind 55k) ≈ 800-900 บรรทัด
MAIN_BINS = ("auth.bin", "sound_auth.bin", "talk.bin", "talk_select_select.bin", "mission_mission_kind.bin")
TEXT_COLS = {"auth.bin": ("4", "5"), "sound_auth.bin": ("4", "6"), "talk.bin": ("3",)}
GENDER_TH = {"male": "ช", "female": "ญ", "neutral": "กลาง", "mixed": "กลาง", "unknown": "?"}


def sections(n):
    nn = "%02d" % n
    out = []
    if n > 1:                       # P00_Start / P01_* ไม่มีข้อความ (ฉากเปิดเกมอยู่ใน a01_ แล้ว)
        out.append(("ทวนเรื่องเปิดบท", "auth.bin", r"^[Pp]%s_" % nn))
    out += [
        ("คัตซีน", "auth.bin", r"^a%s_" % nn),
        ("ฉากพิเศษ", "auth.bin", r"^[Bb]%s_" % nn),
        ("พากย์", "sound_auth.bin", r"^speech_list_judge_main_c%s$" % nn),
        ("บทพูดเดิน", "talk.bin", r"^judge_main_c%s" % nn),
        ("ตัวเลือก", "talk_select_select.bin", r"^M%s_" % nn),
        ("เป้าหมายภารกิจ", "mission_mission_kind.bin", r"^judge_m_M%s_" % nn),
    ]
    return out


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def nested_table(sub):
    for val in sub.values():
        if isinstance(val, dict) and "ROW_COUNT" in val:
            return val
    return None


def walk_strings(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if not str(k).startswith("reARMP"):
                walk_strings(v, out)
    elif isinstance(o, list):
        for v in o:
            walk_strings(v, out)
    elif isinstance(o, str):
        out.append(o)


def top_rows(data):
    for k, v in data.items():
        if k.isdigit():
            for name, sub in v.items():
                if isinstance(sub, dict):
                    yield name, sub


def sort_key(bin_name, rk, row):
    if bin_name == "auth.bin":
        return (float(row.get("1") or 0), int(rk))
    if bin_name == "sound_auth.bin":
        try:
            return (int(row.get("1") or 0), int(row.get("2") or 0), int(rk))
        except ValueError:
            return (0, 0, int(rk))
    return (int(rk),)


class Speakers:
    def __init__(self):
        self.speech_map = load(FACTS / "speech_speaker_map.json")
        self.voicer = load(FACTS / "voicer_gender.json")
        self.dialogue = load(FACTS / "dialogue_gender.json")
        self.talk = load(FACTS / "talk_speaker.json")
        self._cache = {}

    def _json(self, p):
        if p not in self._cache:
            self._cache[p] = load(p) if p.exists() else {}
        return self._cache[p]

    def get(self, bin_name, table, rk, en):
        who, g = self._get(bin_name, table, rk, en)
        if who.isalpha() and who.islower():      # รหัสผู้พากย์ (yagami) → ชื่อเดียวกับป้ายอื่น (Yagami)
            who = who.capitalize()
        return who, g

    def _get(self, bin_name, table, rk, en):
        if bin_name == "auth.bin":
            r = self._json(CINEMA / (table + ".json")).get("rows", {}).get(rk, {})
            return (r.get("speaker") or "?"), r.get("gender", "unknown")
        if bin_name == "sound_auth.bin":
            r = self._json(SPEECH / (table + ".json")).get("rows", {}).get(rk)
            if r and r.get("speaker") and r["speaker"] != "?":
                return r["speaker"], r.get("gender", "unknown")
            who = (self.speech_map.get(en, {}).get("speaker_exact") or [None])[0]
            g = self.voicer.get(who) if who else None
            return (who or "?"), (g or self.dialogue.get(en, {}).get("gender", "unknown"))
        if bin_name == "talk.bin":
            info = self.talk.get(en, {})
            return info.get("speaker") or "?", info.get("gender", "unknown")
        if bin_name == "talk_select_select.bin":
            return "Yagami (ตัวเลือก)", "male"
        return "(ข้อความระบบ)", "neutral"


def chapter_of(table):
    """คืนเลขบท (0 = บทนำ) ถ้าตารางนี้เป็นเนื้อเรื่องหลัก ไม่งั้น None"""
    pats = [(r"^[Pp](\d\d)_", None), (r"^a(\d\d)_", None), (r"^[Bb](\d\d)_", None),
            (r"^speech_list_judge_main_c(\d\d)$", None), (r"^judge_main_c(\d\d)", None), (r"^M(\d\d)_", None),
            (r"^judge_m_M(\d\d)_", None)]
    for pat, fn in pats:
        m = re.search(pat, table)
        if m:
            return fn(m) if fn else int(m.group(1))
    return None


def english_flags(th):
    """อังกฤษที่ยังค้างในคำแปล — ทั้งบรรทัด (ยังไม่แปล) หรือคำปน (มีอังกฤษ) · หักคำที่ตั้งใจคง EN ตาม check_latin_leftovers"""
    if not THAI_RE.search(th):
        return ["ยังไม่แปล"] if re.search(r"[A-Za-z]", TAG_RE.sub("", th)) else []
    hits, _where = latin_scan([("", th)])
    return ["มีอังกฤษ: " + ", ".join(sorted(hits))] if hits else []


def collect(master, n, bins, spk, usage):
    lines, seen, dup = [], {}, Counter()
    for section, bin_name, pat in sections(n):
        rx = re.compile(pat)
        for table, sub in top_rows(bins[bin_name]):
            if not rx.search(table):
                continue
            if bin_name in TEXT_COLS:
                tbl = nested_table(sub)
                if tbl is None:
                    continue
                rows = []
                for rk, rv in tbl.items():
                    if rk.isdigit() and rk != "0":
                        for _rn, row in rv.items():
                            rows.append((rk, row))
                rows.sort(key=lambda x: sort_key(bin_name, x[0], x[1]))
                items = []
                for rk, row in rows:
                    primary = None
                    for ci, col in enumerate(TEXT_COLS[bin_name]):
                        en = row.get(col)
                        if ci > 0 and en == primary:
                            continue
                        items.append((rk, col, en, ci > 0))
                        if ci == 0:
                            primary = en
            else:
                strs = []
                walk_strings(sub, strs)
                items = [("-", "-", en, False) for en in strs]
            for rk, col, en, alt in items:
                if not isinstance(en, str) or not en.strip():
                    continue
                th = master.get(en)
                missing = not isinstance(th, str)
                if missing:
                    # ตารางอื่น (ตัวเลือก/ภารกิจ) มี identifier ปน — นับเฉพาะคอลัมน์ข้อความของ 3 bin หลัก
                    # ("I..." มีละตินตัวเดียว — extract_all_en.is_translatable ตัดทิ้งเพราะต้องมี >= 2 ตัว จึงไม่เคยเข้าคิวแปล)
                    if bin_name not in TEXT_COLS or not re.search(r"[A-Za-z]", en):
                        continue
                    th = en
                eng = english_flags(th)
                if th == en and not eng:
                    continue          # สัญลักษณ์/จุดล้วน ("..." "!?") ไม่ต้องเกลา
                if en in seen:
                    dup[en] += 1
                    continue
                who, g = spk.get(bin_name, table, rk, en)
                flags = (["ไม่มีใน master"] if missing else []) + eng
                if alt:
                    flags.append("อีกแทร็ก")
                outside = usage.get(en, set()) - {n}
                if outside:
                    flags.append("ใช้ร่วม")
                if spk.dialogue.get(en, {}).get("gender") == "mixed":
                    flags.append("ต้องกลางเพศ")
                seen[en] = len(lines)
                lines.append({"section": section, "table": table, "bin": bin_name, "row": rk, "col": col,
                              "en": en, "th": th, "speaker": who, "gender": g, "flags": flags,
                              "outside": sorted(str(x) for x in outside)})
    for en, k in dup.items():
        lines[seen[en]]["flags"].append("ซ้ำในบท x%d" % (k + 1))
    return lines


def chunk(lines):
    chunks, cur, size = [], [], 0
    for i, ln in enumerate(lines):
        cur.append(ln)
        size += len(ln["th"])
        scene_end = i + 1 == len(lines) or lines[i + 1]["table"] != ln["table"]
        if (size >= CHUNK_CHARS and scene_end) or size >= CHUNK_CHARS * 1.15:
            chunks.append(cur)
            cur, size = [], 0
    if cur:
        # หางสั้น (เช่นบท 3 ตัดกลางตารางพากย์เหลือ 36 บรรทัด) → รวมกับชิ้นก่อน ไม่ต้องเปลืองทีมอีกชุด
        if chunks and sum(len(ln["th"]) for ln in cur) < CHUNK_CHARS * 0.25:
            chunks[-1].extend(cur)
        else:
            chunks.append(cur)
    return chunks


def build_usage(master, bins):
    """คีย์ EN → เซตของ 'ที่ใช้' (เลขบทของเนื้อเรื่องหลัก หรือชื่อ bin/ตารางอื่น)"""
    usage = defaultdict(set)
    for bin_name, data in bins.items():
        for table, sub in top_rows(data):
            ch = chapter_of(table)
            strs = []
            walk_strings(sub, strs)
            for s in strs:
                if s in master:
                    usage[s].add(ch if ch is not None else "%s/%s" % (bin_name, re.sub(r"\d+", "#", table)))
    for b, strs in load(paths.EXTRACTED / "strings_by_bin.json").items():
        if b in MAIN_BINS:
            continue
        for s in strs:
            if s in master:
                usage[s].add(b)
    return usage


def context_md(n, lines):
    story = CONTEXT / ("story_ch%02d.md" % n)
    out = ["# บริบทบทที่ %d — ชุดงานเกลา" % n, ""]
    if story.exists():
        out += [story.read_text(encoding="utf-8").strip(), ""]
    else:
        out += ["(ยังไม่มีเรื่องย่อของบทนี้ใน translations/review/polish/context/)", ""]
    cast = Counter()
    gender = {}
    for ln in lines:
        if ln["speaker"] not in ("?", "(ข้อความระบบ)"):
            cast[ln["speaker"]] += 1
            gender.setdefault(ln["speaker"], ln["gender"])
    out += ["## ผู้พูดที่ไฟล์เกม/ทีมก่อนหน้าระบุได้ในบทนี้ (จำนวนบรรทัด)", "",
            "| ผู้พูด | เพศ | บรรทัด |", "|---|---|---|"]
    out += ["| %s | %s | %d |" % (w, GENDER_TH.get(gender[w], "?"), c) for w, c in cast.most_common()]
    unknown = sum(1 for ln in lines if ln["speaker"] == "?")
    out += ["", "บรรทัดที่ยังไม่รู้ผู้พูด: %d จาก %d — ระบุจากบริบทแล้วส่งใน speakers_NN.json" % (unknown, len(lines)), ""]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="ตัดบทแปลเนื้อเรื่องหลักทีละบทสำหรับงานเกลา")
    ap.add_argument("--chapter", type=int, choices=range(1, 14))
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    if not a.stats and not a.chapter:
        ap.error("ต้องระบุ --chapter N หรือ --stats")

    master = load(paths.MASTER_TH)
    bins = {b: load(paths.DB_EN / "en" / (b + ".json")) for b in MAIN_BINS}
    spk = Speakers()
    usage = build_usage(master, bins)

    chapters = range(1, 14) if a.stats else [a.chapter]
    tot = Counter()
    for n in chapters:
        lines = collect(master, n, bins, spk, usage)
        chunks = chunk(lines)
        sec = OrderedDict()
        for ln in lines:
            sec[ln["section"]] = sec.get(ln["section"], 0) + 1
        unknown = sum(1 for ln in lines if ln["speaker"] == "?")
        shared = sum(1 for ln in lines if "ใช้ร่วม" in ln["flags"])
        chars = sum(len(ln["th"]) for ln in lines)
        untr = sum(1 for ln in lines if "ยังไม่แปล" in ln["flags"])
        mixed = sum(1 for ln in lines if any(f.startswith("มีอังกฤษ") for f in ln["flags"]))
        print("บท %2d: %5d บรรทัด · อักษรไทย %7d · %d ชิ้น · ไม่รู้ผู้พูด %4d · ใช้ร่วม %3d · ยังไม่แปล %2d · มีอังกฤษปน %2d · %s"
              % (n, len(lines), chars, len(chunks), unknown, shared, untr, mixed,
                 " · ".join("%s %d" % kv for kv in sec.items())))
        tot.update(lines=len(lines), chars=chars, chunks=len(chunks), unknown=unknown, shared=shared, untr=untr, mixed=mixed)
        if a.stats:
            continue

        out = OUT_ROOT / ("ch%02d" % n)
        out.mkdir(parents=True, exist_ok=True)
        for old in out.glob("chunk_*.tsv"):
            old.unlink()
        esc = lambda s: s.replace("\\", "\\\\").replace("\t", " ").replace("\n", "\\n")
        index, meta = OrderedDict(), OrderedDict()
        for ci, ch in enumerate(chunks, 1):
            rows = ["id\tฉาก\tผู้พูด\tหมายเหตุ\tEN\tTH"]
            for j, ln in enumerate(ch, 1):
                sid = "P%02d%02d-%04d" % (n, ci, j)
                index[sid] = ln["en"]
                meta[sid] = {k: ln[k] for k in ("section", "bin", "table", "row", "col", "speaker", "gender", "flags", "outside")}
                label = "%s (%s)" % (ln["speaker"], GENDER_TH.get(ln["gender"], "?"))
                rows.append("\t".join((sid, "%s · %s" % (ln["section"], ln["table"]), label,
                                       " ".join("[%s]" % f for f in ln["flags"]), esc(ln["en"]), esc(ln["th"]))))
            (out / ("chunk_%02d.tsv" % ci)).write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
        (out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
        (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
        (out / "context.md").write_text(context_md(n, lines), encoding="utf-8", newline="\n")
        for ci, ch in enumerate(chunks, 1):
            print("  chunk_%02d: %4d บรรทัด · %6d อักษร · %s" % (
                ci, len(ch), sum(len(x["th"]) for x in ch), ch[0]["table"] + " … " + ch[-1]["table"]))
        print("เขียน", out)
    if a.stats:
        print("รวม: %(lines)d บรรทัด · อักษรไทย %(chars)d · %(chunks)d ชิ้น · ไม่รู้ผู้พูด %(unknown)d · ใช้ร่วม %(shared)d"
              " · ยังไม่แปล %(untr)d · มีอังกฤษปน %(mixed)d" % tot)


if __name__ == "__main__":
    main()
