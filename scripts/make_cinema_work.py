#!/usr/bin/env python3
"""เตรียมแฟ้มงานให้ทีม subagent ระบุ "ใครพูด" ในบทคัตซีน (`auth.bin/<ฉาก>/cinema_telop`)

ทำไมต้องมี: ตารางคัตซีนไม่มีคอลัมน์ผู้พูดเลย (ตรวจกับไฟล์จริง 22 ส.ค. 2026) และคิวเสียงใน
`sound_auth.bin` ครอบคลุมบรรทัดคัตซีนแค่ 545/4,743 บรรทัด → บรรทัดที่มีคำบอกเพศ 1,025 บรรทัด
ใน 101 ฉากต้องให้คนอ่านบริบทแล้วตัดสินทีละฉาก (รายงานผู้เล่น 27 ส.ค. + 5 ก.ย. 2026:
ตัวละครหญิงในคัตซีนลงท้าย "ครับ")

สคริปต์นี้เขียน:
  build/gender/cinema/G01.md ... G11.md   แฟ้มงานต่อ agent (หลายฉาก · ทุกแถวเรียงตามเวลา
                                          · EN ชุด A/B + TH ปัจจุบัน + คำใบ้จากคิวเสียง/talk.bin)
  build/gender/cinema/_groups.json        ฉากในแต่ละกลุ่ม (ใช้ตรวจว่า agent ส่งครบ)
  build/gender/characters_gender.md       ทะเบียนเพศตัวละครที่พิสูจน์แล้ว (แนบให้ทุก agent)
  build/gender/story_chNN.md              บริบทเนื้อเรื่องรายบท (ตัดจาก docs/story_context_judge.*)

agent ต้องเขียนผลเป็น translations/cinema_speakers/<ฉาก>.json (โครงอยู่ท้ายแฟ้มงานทุกไฟล์)
แล้ว lead รัน `scripts/make_dialogue_gender.py --write` ต่อ

ใช้:
  python scripts/make_cinema_work.py
"""
import collections
import io
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                    # noqa: E402
from check_speaker_gender import female_markers, male_markers   # noqa: E402

AUTH = paths.DB_EN / "en" / "auth.bin.json"
OUT = paths.BUILD / "gender"
CINEMA_OUT = OUT / "cinema"
RESULT_DIR = paths.TRANSLATIONS / "cinema_speakers"

META = {"ROW_COUNT", "COLUMN_COUNT", "TEXT_COUNT", "ROW_VALIDATOR", "COLUMN_VALIDATOR",
        "HAS_ROW_NAMES", "HAS_COLUMN_NAMES", "HAS_ROW_VALIDITY", "HAS_COLUMN_VALIDITY",
        "HAS_UNKNOWN_BITMASK", "HAS_ROW_INDICES", "TABLE_ID", "STORAGE_MODE",
        "columnValidity", "columnTypes", "COLUMN_INDICES"}

# กลุ่มงาน — แบ่งให้แต่ละกลุ่มไม่เกิน ~570 บรรทัด (สองชุด A/B) เพื่อคุม token ของ agent
GROUPS = {
    "G01": ["a01_010", "a01_020", "a01_025", "a01_030", "a01_035", "a01_040", "a01_050", "a01_060"],
    "G02": ["a01_080", "a01_085", "a01_090", "a01_100", "a01_110", "a01_120",
            "a02_010", "a02_013", "a02_017", "a02_020", "a02_030", "a02_035", "a02_040"],
    "G03": ["a03_010", "a03_015", "a03_020", "a03_030", "a03_040",
            "a04_010", "a04_015", "a04_017", "a04_020", "a04_030", "a04_040"],
    "G04": ["a05_010", "a05_020", "a05_030", "a05_040", "a06_010", "a06_020", "a06_030", "a07_010"],
    "G05": ["a08_010", "a08_020", "a08_023", "a08_025", "a08_030", "a08_040"],
    "G06": ["a09_005", "a09_010", "a09_015", "a09_030", "a09_040", "a09_050", "a09_060",
            "a10_010", "a10_020", "a10_030"],
    "G07": ["a11_005", "a11_010", "a11_020", "a11_030", "a11_040"],
    "G08": ["a12_010", "a12_020", "a12_030", "a12_040", "a12_050", "a12_060", "a12_070"],
    "G09": ["a13_030", "a13_040", "a13_050", "a13_060", "a13_065", "a13_080", "a13_082",
            "a13_090", "a13_110"],
    "G10": ["a13_120", "a13_130", "a13_140", "a13_150", "a13_160", "a13_170", "a13_180",
            "a13_185", "a13_190"],
    "G11": ["b01_010", "b05_010", "b09_010", "b11_020",
            "p02_00100", "p03_00100", "p04_00100", "p05_00100", "p06_00100", "p07_00100",
            "p08_00100", "p09_00100", "p10_00100", "p11_00100", "p12_00100", "p13_00100"],
}


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def scenes():
    """{ชื่อฉาก: [(row_key, en_a, en_b), ...]} เรียงตามเวลาเริ่ม"""
    a = load(AUTH)
    out = {}
    for v in a.values():
        if not isinstance(v, dict):
            continue
        for name, vv in v.items():
            if not (isinstance(vv, dict) and "cinema_telop" in vv):
                continue
            rows = []
            for r, row in vv["cinema_telop"].items():
                if r in META:
                    continue
                row = row.get("", row)
                ea, eb = row.get("4"), row.get("5")
                if not (isinstance(ea, str) and ea.strip()) and not (isinstance(eb, str) and eb.strip()):
                    continue
                rows.append((float(row.get("1") or 0), r, ea if isinstance(ea, str) else "",
                             eb if isinstance(eb, str) else ""))
            rows.sort(key=lambda t: (t[0], int(t[1])))
            out[name] = [(r, ea, eb) for _, r, ea, eb in rows]
    return out


def chapter_of(scene):
    m = re.match(r"a(\d\d)_", scene)
    if m:
        return int(m.group(1))
    return None


def scene_label(scene):
    ch = chapter_of(scene)
    if ch:
        return "บทที่ %d" % ch
    if scene.startswith("b"):
        return "สรุปคดีในศาล/เคสไฟล์ (บรรยาย)"
    if scene.startswith("p"):
        return "บทนำต้นบท (recap 'ความเดิม')"
    return "?"


def hints(master, line_gender, talk_speaker):
    def one(en):
        if not en:
            return ""
        h = []
        lg = line_gender.get(en)
        if lg:
            h.append("cue=%s(%s)" % (lg.get("gender"), ",".join(lg.get("voicers") or [])[:30]))
        ts = talk_speaker.get(en)
        if ts and ts.get("speaker"):
            h.append("talk=%s" % ts["speaker"])
        return " ".join(h)
    return one


def th_mark(th):
    if not th:
        return ""
    m, f = male_markers(th), female_markers(th)
    return "M" if m and not f else "F" if f and not m else "MF" if m and f else ""


def cell(s):
    return (s or "").replace("|", "¦").replace("\n", " / ").strip()


def write_characters_sheet():
    main = load(paths.TRANSLATIONS / "characters_main.json")
    ev = load(paths.EXTRACTED / "facts" / "gender_evidence.json")
    lines = ["# ทะเบียนเพศตัวละคร (พิสูจน์จากไฟล์เกมแล้ว) — ใช้อ้างอิงตอนระบุผู้พูด", "",
             "> สร้างด้วย `scripts/make_cinema_work.py` จาก `translations/characters_main.json` +",
             "> `extracted/facts/gender_evidence.json` — ห้ามแก้ด้วยมือ · ชื่อ = ชื่อ EN ในเกม", "",
             "## ตัวละครหลัก", "", "| ชื่อ EN | เพศ | บทบาท |", "|---|---|---|"]
    TH = {"male": "ชาย", "female": "หญิง", "unknown": "ไม่ยืนยัน", "mixed": "หลายคน"}
    for k, v in main.items():
        role = (v.get("role") or "").replace("\n", " ")
        role = role[:140] + ("…" if len(role) > 140 else "")
        lines.append("| %s | %s | %s |" % (v.get("name_en", k), TH.get(v.get("gender"), "?"), role))
    lines += ["", "## ตัวละครรอง/เพื่อน/NPC ที่พิสูจน์แล้ว", "", "| ชื่อ EN | เพศ | หลักฐาน (ย่อ) |", "|---|---|---|"]
    seen = {v.get("name_en", "").lower() for v in main.values()}
    for k, v in ev.items():
        if k == "_meta" or v.get("name_en", "").lower() in seen:
            continue
        # ตัด notes ทิ้ง — ทะเบียนเต็ม 73KB กิน token ของ agent เกินจำเป็น เอาแค่ชื่อ+เพศ+หลักฐานสั้น
        ev1 = (v.get("evidence") or [{}])[0]
        quote = (ev1.get("quote") or "").replace("\n", " ")
        lines.append("| %s | %s | %s |" % (v.get("name_en", k), TH.get(v.get("gender"), "?"), quote[:60]))
    lines += ["", "กติกา: ชื่อที่ไม่อยู่ในตารางนี้ = ยังไม่ยืนยันเพศ ให้ใส่ `unknown` เว้นแต่บทในฉากบอกเพศชัด",
              "(he/she · sir/ma'am · Mr./Ms. · บทบาทแม่/ลูกสาว/โฮสเตส ฯลฯ) และต้องอ้างบรรทัดที่เป็นหลักฐาน"]
    (OUT / "characters_gender.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_story_chapters():
    """ตัด docs/story_context_judge.part{1,2}.md เป็นรายบท"""
    text = ""
    for p in (paths.DOCS / "story_context_judge.part1.md", paths.DOCS / "story_context_judge.part2.md"):
        if p.exists():
            text += p.read_text(encoding="utf-8") + "\n"
    parts = re.split(r"(?m)^(?=### บทที่ )", text)
    n = 0
    for part in parts:
        m = re.match(r"### บทที่ (\d+)", part)
        if not m:
            continue
        ch = int(m.group(1))
        body = re.split(r"(?m)^## ", part)[0]      # ตัดทิ้งเมื่อเจอหัวข้อระดับ ## ถัดไป
        (OUT / ("story_ch%02d.md" % ch)).write_text(body.strip() + "\n", encoding="utf-8")
        n += 1
    return n


SCHEMA = """
## รูปแบบผลลัพธ์ที่ต้องส่ง (หนึ่งไฟล์ต่อฉาก)

เขียนที่ `translations/cinema_speakers/<ฉาก>.json` (UTF-8 · ห้ามใส่ข้อความไทย) เช่น:

```json
{
 "scene": "a01_010",
 "rows": {
  "1":  {"speaker": "Saori", "gender": "female", "conf": "high", "why": "row 12 'Genda Law, Saori speaking'"},
  "6":  {"speaker": "Genda", "gender": "male", "conf": "high", "why": "named in row 5"},
  "17": {"speaker": "Narration", "gender": "narration", "conf": "high", "why": "on-screen caption"},
  "24": {"speaker": "Unknown employee", "gender": "unknown", "conf": "low", "why": "no cue"}
 }
}
```

* คีย์ของ `rows` = เลข `#` ในตารางข้างบน (ต้องมี **ทุกแถว** ของฉาก ห้ามข้าม)
* `gender` ใช้ได้เฉพาะ `male` · `female` · `unknown` · `narration` (ป้าย/บรรยาย/ข้อความบนจอ)
* `speaker` = ชื่อ EN ตามทะเบียน `characters_gender.md` ถ้าเป็นคนในทะเบียน · NPC ไม่มีชื่อให้บรรยายสั้น ๆ
  เป็นอังกฤษ เช่น `Female clerk` · `Thug A`
* `conf` = `high` (บทระบุชัด/ชื่อถูกเรียกในฉาก) · `med` (อนุมานจากลำดับสนทนา) · `low` (เดา)
* `why` สั้น ๆ เป็นอังกฤษ อ้างเลขแถวที่เป็นหลักฐาน — ห้ามเดาเพศจากชื่อเฉย ๆ (ดูกติกาในทะเบียน)
* แถวที่เป็นสองคนพูดสลับกันในบรรทัดเดียว หรือระบุไม่ได้จริง ๆ → `unknown`
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CINEMA_OUT.mkdir(parents=True, exist_ok=True)
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    master = load(paths.MASTER_TH)
    lg = load(paths.EXTRACTED / "facts" / "line_gender.json")
    ts = load(paths.EXTRACTED / "facts" / "talk_speaker.json")
    hint = hints(master, lg, ts)
    sc = scenes()

    grouped = {s for g in GROUPS.values() for s in g}
    missing = sorted(set(sc) - grouped)
    assert not missing, "ฉากที่ยังไม่อยู่ในกลุ่มใด: %s" % missing

    write_characters_sheet()
    nch = write_story_chapters()
    stats = collections.OrderedDict()
    for gid, names in GROUPS.items():
        lines = ["# แฟ้มงานระบุผู้พูดคัตซีน — กลุ่ม %s" % gid, "",
                 "> สร้างด้วย `scripts/make_cinema_work.py` — ห้ามแก้ไฟล์นี้ · ทุกแถวเรียงตามเวลาในฉาก",
                 "> คอลัมน์: `#` เลขแถว (ใช้เป็นคีย์ตอนส่งผล) · `EN-A`/`EN-B` = ข้อความสองรูปของบรรทัดเดียวกัน",
                 "> (ชุด A = ซับ, ชุด B = บทพากย์ — ผู้พูดคนเดียวกันเสมอ) · `TH` = คำแปลปัจจุบันของชุด A ·",
                 "> `ปัจจุบัน` = คำลงท้ายที่แปลไว้ (M=ครับ/ผม · F=ค่ะ/ฉัน) · `คำใบ้` = หลักฐานจากไฟล์เกม",
                 "> (cue=เพศจากคิวเสียง · talk=ชื่อผู้พูดของประโยคเดียวกันในบทเดินเมือง — เชื่อได้สูง)", ""]
        total = 0
        for name in names:
            rows = sc[name]
            total += len(rows)
            lines += ["## ฉาก `%s` — %s · %d แถว" % (name, scene_label(name), len(rows)), "",
                      "| # | EN-A | EN-B | TH (ชุด A) | ปัจจุบัน | คำใบ้ |", "|---|---|---|---|---|---|"]
            for r, ea, eb in rows:
                th = master.get(ea) or master.get(eb) or ""
                lines.append("| %s | %s | %s | %s | %s | %s |" % (
                    r, cell(ea), cell(eb), cell(th)[:120], th_mark(th),
                    " ".join(x for x in (hint(ea), hint(eb)) if x)))
            lines.append("")
        lines.append(SCHEMA)
        (CINEMA_OUT / (gid + ".md")).write_text("\n".join(lines), encoding="utf-8")
        stats[gid] = {"scenes": names, "lines": total,
                      "chapters": sorted({chapter_of(s) for s in names if chapter_of(s)})}
        print("%s  %2d ฉาก  %4d แถว  บท %s" % (gid, len(names), total, stats[gid]["chapters"]))
    (CINEMA_OUT / "_groups.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1) + "\n",
                                             encoding="utf-8")
    print("ฉาก %d · แถวรวม %d · story รายบท %d ไฟล์ · %s" % (
        len(sc), sum(v["lines"] for v in stats.values()), nch, OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
