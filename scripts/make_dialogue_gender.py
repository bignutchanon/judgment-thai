#!/usr/bin/env python3
"""รวมหลักฐาน "เพศผู้พูด" ทุกแหล่งเป็นตารางเดียว — `extracted/facts/dialogue_gender.json`
พร้อมตารางสรุปสำหรับคนอ่าน `docs/dialogue_gender_table.md`

ทำไมต้องมี: ก่อนหน้านี้แต่ละแหล่งมีตัวตรวจของตัวเอง (`check_line_gender` = คิวเสียง ·
`check_speaker_gender` = talk.bin) แล้วบรรทัดที่ไม่มีทั้งสองอย่างก็หลุด — นับจริง 5 ก.ย. 2026
บรรทัดที่แปลระบุเพศไว้ 14,100 · ไม่มีหลักฐานเลย 2,362 (คัตซีน 992 · แชท 721 · ...) และอีก 1,771
บรรทัดอยู่กับผู้พูดที่ทะเบียนเป็น unknown ผู้เล่นจึงยังเจอ "ผู้หญิงลงท้ายครับ" หลัง v1.0.1

แหล่งที่รวม (ลำดับไม่สำคัญ — ทุกแหล่งโหวตเท่ากัน ขัดกัน = `mixed` ต้องแปลกลางเพศ):

| แหล่ง | ไฟล์ | ครอบคลุม |
|---|---|---|
| `cue` | `extracted/facts/line_gender.json` (คิวเสียง `sound_auth.bin`) | บทพากย์ทุกบรรทัด |
| `talk` | `extracted/facts/talk_speaker.json` (+`dupes`) | บทเดินเมือง/เควส `talk.bin` |
| `cinema` | `translations/cinema_speakers/<ฉาก>.json` (ทีม subagent อ่านบริบทฉาก) × `auth.bin` | คัตซีน `auth.bin` |
| `chat` | `extracted/facts/chat_sender.json` + เพศของคู่แชท | ข้อความแชท `pause_message.bin` |
| `popup` | `extracted/facts/popup_gender.json` | คำพูดลอยชาวเมือง |
| `pov` | รายชื่อ bin ที่เป็นเสียงในใจ/บันทึกของยากามิล้วน (`YAGAMI_POV_BINS`) | ภารกิจ/เคสไฟล์/ตัวเลือก |
| `speech` | `translations/speech_speakers/<ตาราง>.json` (ทีม register รอบ 22 ระบุผู้พูดจากบริบท) × `sound_auth.bin` | บทพากย์ที่ไฟล์เกมไม่บอกชื่อผู้พูด |
| `mahjong` | `translations/mahjong_npc_gender.json` (ค้นเว็บ รอบ 22) × `minigame_mahjong_string_npc.bin` | บทพูดคู่ต่อสู้มาจอง |

กติกา: `SKIP_VOICERS` ของ `fix_line_gender.py` (เพศนักพากย์ ≠ ตัวละคร) ถูกตัดออกจากแหล่ง `cue` ·
ผล `cinema` ใช้เฉพาะ `conf` high/med (low นับเป็นไม่รู้) · เพศของคู่แชทมาจาก
`gender_evidence.json` → `translations/speaker_gender_overrides.json` ตามลำดับ

ผลลัพธ์ต่อข้อความ EN:
  {"gender": male|female|mixed|unknown|narration, "votes": {...}, "sources": [{"src","gender","who"}]}

ใช้:
  python scripts/make_dialogue_gender.py            # สรุปอย่างเดียว
  python scripts/make_dialogue_gender.py --write    # เขียน facts + docs
"""
import argparse
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
from fix_line_gender import SKIP_VOICERS        # noqa: E402

FACTS = paths.EXTRACTED / "facts"
OUT = FACTS / "dialogue_gender.json"
DOC = paths.DOCS / "dialogue_gender_table.md"
CINEMA_DIR = paths.TRANSLATIONS / "cinema_speakers"
OVERRIDES = paths.TRANSLATIONS / "speaker_gender_overrides.json"
AUTH = paths.DB_EN / "en" / "auth.bin.json"

# bin ที่ข้อความทั้ง bin เป็นเสียงในใจ/บันทึก/ตัวเลือกคำพูดของยากามิ (ตรวจแล้ว 5 ก.ย. 2026:
# ไม่มีบรรทัดใดใช้คำหญิง) — ยกเว้น side_case_side_case_request.bin ที่เป็นข้อความจากลูกความ (ต่างเพศ)
YAGAMI_POV_BINS = {
    "mission_mission_kind.bin", "scene_scenario_explanation.bin", "talk_select_select.bin",
    "item.bin", "evidence_item_to_update.bin", "pause_crowdfunding.bin", "talk_question_text.bin",
}
META = {"ROW_COUNT", "COLUMN_COUNT", "TEXT_COUNT", "ROW_VALIDATOR", "COLUMN_VALIDATOR",
        "HAS_ROW_NAMES", "HAS_COLUMN_NAMES", "HAS_ROW_VALIDITY", "HAS_COLUMN_VALIDITY",
        "HAS_UNKNOWN_BITMASK", "HAS_ROW_INDICES", "TABLE_ID", "STORAGE_MODE",
        "columnValidity", "columnTypes", "COLUMN_INDICES"}


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


class Table:
    def __init__(self):
        self.rows = collections.defaultdict(list)     # EN -> [(src, gender, who)]

    def vote(self, en, src, gender, who=""):
        if not en:
            return
        self.rows[en].append((src, gender, who))

    def finish(self):
        out = {}
        for en, votes in self.rows.items():
            gs = collections.Counter()
            for _, g, _ in votes:
                if g == "mixed":
                    gs["male"] += 1
                    gs["female"] += 1
                elif g in ("male", "female", "narration", "unknown"):
                    gs[g] += 1
            if gs["male"] and gs["female"]:
                g = "mixed"
            elif gs["male"]:
                g = "male"
            elif gs["female"]:
                g = "female"
            elif gs["narration"]:
                g = "narration"
            else:
                g = "unknown"
            out[en] = {"gender": g,
                       "votes": {k: v for k, v in gs.items() if v},
                       "sources": [{"src": s, "gender": gg, "who": w} for s, gg, w in votes]}
        return out


def cue_votes(t):
    for en, info in load(FACTS / "line_gender.json").items():
        voicers = info.get("voicers") or []
        if voicers and all(v in SKIP_VOICERS for v in voicers):
            continue
        t.vote(en, "cue", info.get("gender"), ",".join(voicers)[:40])


def talk_votes(t):
    for en, info in load(FACTS / "talk_speaker.json").items():
        recs = [info] + [d for d in info.get("dupes", []) if isinstance(d, dict)]
        for r in recs:
            g = r.get("gender")
            if g == "neutral":
                g = "mixed"
            if g in ("male", "female", "mixed"):
                t.vote(en, "talk", g, r.get("speaker", ""))


def cinema_rows():
    """{ฉาก: {row_key: (en_a, en_b)}}"""
    a = load(AUTH)
    out = {}
    for v in a.values():
        if not isinstance(v, dict):
            continue
        for name, vv in v.items():
            if not (isinstance(vv, dict) and "cinema_telop" in vv):
                continue
            rows = {}
            for r, row in vv["cinema_telop"].items():
                if r in META:
                    continue
                row = row.get("", row)
                ea, eb = row.get("4"), row.get("5")
                rows[r] = (ea if isinstance(ea, str) else "", eb if isinstance(eb, str) else "")
            out[name] = rows
    return out


def cinema_votes(t):
    scenes = cinema_rows()
    n_scene = n_row = 0
    bad = []
    for p in sorted(CINEMA_DIR.glob("*.json")):
        try:
            d = load(p)
        except Exception as e:     # noqa: BLE001
            bad.append("%s: %s" % (p.name, e))
            continue
        scene = d.get("scene") or p.stem
        rows = scenes.get(scene)
        if rows is None:
            bad.append("%s: ไม่มีฉากนี้ใน auth.bin" % p.name)
            continue
        n_scene += 1
        for r, info in (d.get("rows") or {}).items():
            if r not in rows:
                bad.append("%s: แถว %s ไม่มีในฉาก" % (p.name, r))
                continue
            g = (info.get("gender") or "unknown").lower()
            conf = (info.get("conf") or "low").lower()
            if g in ("male", "female") and conf == "low":
                g = "unknown"
            who = info.get("speaker") or ""
            for en in rows[r]:
                t.vote(en, "cinema", g, who)
            n_row += 1
    return n_scene, n_row, bad


def contact_gender_lookup():
    """ชื่อคู่แชท -> เพศ (gender_evidence → overrides)"""
    m = {}
    ev = load(FACTS / "gender_evidence.json")
    for k, v in ev.items():
        if k == "_meta":
            continue
        g = v.get("gender")
        if g in ("male", "female"):
            m[v.get("name_en", "").lower()] = g
            m[k.lower()] = g
            last = v.get("name_en", "").split()[-1:] if v.get("name_en") else []
            if last:
                m.setdefault(last[0].lower(), g)
    # ทะเบียนในโค้ดของ make_talk_speaker (พิสูจน์ไว้ตอนสปรินต์แปล) — ใช้กับชื่อคู่แชทด้วย
    # (Ohata / Amamiya / Jo Masuda อยู่ตรงนี้ ไม่อยู่ใน gender_evidence)
    from make_talk_speaker import ALIASES, OVERRIDES as CODE_OVERRIDES
    vg = load(FACTS / "voicer_gender.json")
    for k, g in CODE_OVERRIDES.items():
        if g in ("male", "female"):
            m.setdefault(k, g)
    for k, voicer in ALIASES.items():
        if vg.get(voicer) in ("male", "female"):
            m.setdefault(k, vg[voicer])
    if OVERRIDES.exists():
        for k, v in load(OVERRIDES).items():
            if k.startswith("_"):
                continue
            g = v.get("gender") if isinstance(v, dict) else v
            if g in ("male", "female"):
                m[k.lower()] = g
                last = k.split()[-1:]
                if last:
                    m.setdefault(last[0].lower(), g)
    return m


def chat_votes(t):
    look = contact_gender_lookup()
    unresolved = collections.Counter()
    for en, info in load(FACTS / "chat_sender.json").items():
        role = info.get("role")
        contact = info.get("contact") or ""
        if role in ("yagami", "choice", "chosen_echo", "narration"):
            t.vote(en, "chat", "male", "Yagami")
        elif role == "contact":
            g = look.get(contact.lower()) or look.get(contact.split()[-1].lower() if contact else "")
            if g:
                t.vote(en, "chat", g, contact)
            else:
                unresolved[contact] += 1
        elif role == "ambiguous":
            t.vote(en, "chat", "mixed", contact)
    return unresolved


def popup_votes(t):
    for en, info in load(FACTS / "popup_gender.json").items():
        g = info.get("gender")
        if g in ("male", "female"):
            t.vote(en, "popup", g, info.get("row", ""))


def pov_votes(t):
    sbb = load(paths.EXTRACTED / "strings_by_bin.json")
    for b in YAGAMI_POV_BINS:
        for en in sbb.get(b, []):
            t.vote(en, "pov", "male", "Yagami")


def write_doc(table, master, stats):
    sbb = load(paths.EXTRACTED / "strings_by_bin.json")
    en2bin = {}
    for b, lst in sbb.items():
        for s in lst:
            en2bin.setdefault(s, b)
    by_src = collections.Counter()
    by_g = collections.Counter()
    covered = 0
    marked = 0
    conflict = []
    per_bin = collections.defaultdict(collections.Counter)
    for en, th in master.items():
        info = table.get(en)
        has_mark = bool(male_markers(th) or female_markers(th))
        marked += has_mark
        if not info:
            if has_mark:
                per_bin[en2bin.get(en, "?")]["ไม่มีหลักฐาน"] += 1
            continue
        covered += 1
        by_g[info["gender"]] += 1
        for s in {x["src"] for x in info["sources"]}:
            by_src[s] += 1
        if has_mark:
            b = en2bin.get(en, "?")
            g = info["gender"]
            m, f = male_markers(th), female_markers(th)
            if (g == "male" and f) or (g == "female" and m) or (g == "mixed" and (m or f)):
                per_bin[b]["ขัดกัน"] += 1
                conflict.append((b, g, en, th))
            else:
                per_bin[b]["ตรง"] += 1
    lines = ["# ตารางเพศผู้พูดทั้งเกม — Judgment", "",
             "> สร้างด้วย `python scripts/make_dialogue_gender.py --write` — ห้ามแก้ด้วยมือ ·",
             "> ข้อมูลเต็มอยู่ `extracted/facts/dialogue_gender.json` (ข้อความ EN → เพศ + แหล่งหลักฐาน)", "",
             "| ตัวชี้วัด | ค่า |", "|---|---|",
             "| ข้อความ EN ที่รู้เพศผู้พูด (ทุกแหล่ง) | %s |" % format(len(table), ","),
             "| ในจำนวนนี้อยู่ใน master_th | %s |" % format(covered, ","),
             "| master_th ที่แปลระบุเพศไว้ (ครับ/ค่ะ/ผม/ฉัน) | %s |" % format(marked, ","),
             "| บรรทัดที่คำแปลขัดกับหลักฐาน (ต้องแก้) | **%s** |" % format(len(conflict), ","),
             "| ฉากคัตซีนที่ทีมระบุผู้พูดแล้ว | %d / 102 (%s แถว) |" % (stats["cinema_scenes"], format(stats["cinema_rows"], ",")),
             "", "## แยกตามเพศ (ข้อความในเกมที่รู้ผู้พูด)", "", "| เพศ | จำนวน |", "|---|---|"]
    TH = {"male": "ชาย", "female": "หญิง", "mixed": "ใช้ร่วมสองเพศ (ต้องกลาง)", "narration": "บรรยาย/ป้าย", "unknown": "ไม่ยืนยัน"}
    for g in ("male", "female", "mixed", "narration", "unknown"):
        lines.append("| %s | %s |" % (TH[g], format(by_g[g], ",")))
    lines += ["", "## แยกตามแหล่งหลักฐาน", "", "| แหล่ง | ข้อความ |", "|---|---|"]
    for s, n in by_src.most_common():
        lines.append("| %s | %s |" % (s, format(n, ",")))
    lines += ["", "## บรรทัดที่แปลระบุเพศไว้ แยกตาม bin", "",
              "| bin | ตรง | ขัดกัน | ไม่มีหลักฐาน |", "|---|---|---|---|"]
    for b, c in sorted(per_bin.items(), key=lambda kv: -sum(kv[1].values())):
        lines.append("| %s | %d | %d | %d |" % (b, c["ตรง"], c["ขัดกัน"], c["ไม่มีหลักฐาน"]))
    if stats.get("chat_unresolved"):
        lines += ["", "## คู่แชทที่ยังไม่รู้เพศ (ข้อความจากเขายังไม่ได้ตรวจ)", ""]
        lines += ["* %s — %d ข้อความ" % kv for kv in stats["chat_unresolved"].most_common()]
    if stats.get("cinema_bad"):
        lines += ["", "## ไฟล์ผลคัตซีนที่มีปัญหา", ""] + ["* " + x for x in stats["cinema_bad"]]
    lines += ["", "## บรรทัดที่ขัดกัน (%d) — แก้ด้วย `python scripts/fix_dialogue_gender.py --write`" % len(conflict), "",
              "| bin | เพศจริง | EN | TH ปัจจุบัน |", "|---|---|---|---|"]
    for b, g, en, th in conflict[:400]:
        lines.append("| %s | %s | %s | %s |" % (b, g, en.replace("|", "¦").replace("\n", " / ")[:80],
                                                th.replace("|", "¦").replace("\n", " / ")[:80]))
    if len(conflict) > 400:
        lines.append("| … | | อีก %d บรรทัด | |" % (len(conflict) - 400))
    DOC.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(conflict)


SPEECH_DIR = paths.TRANSLATIONS / "speech_speakers"          # รอบ 22: ทีม register ระบุผู้พูดของบทพากย์ที่ไฟล์เกมไม่บอกชื่อ
MAHJONG = paths.TRANSLATIONS / "mahjong_npc_gender.json"     # รอบ 22: เพศคู่ต่อสู้มาจอง (ค้นเว็บ) × minigame_mahjong_string_npc.bin


def speech_votes(t):
    """แหล่ง `speech`: translations/speech_speakers/<ตาราง>.json = {"table","rows":{แถว:{speaker,gender,conf}}} × sound_auth.bin
    (แถวใน sound_auth เป็นเลขลำดับ JSON เหมือนที่ make_register_chunks ใช้ · ใช้เฉพาะ conf high/med)"""
    if not SPEECH_DIR.exists():
        return 0
    sa = load(paths.DB_EN / "en" / "sound_auth.bin.json")
    tables = {}
    for v in sa.values():
        if not isinstance(v, dict):
            continue
        for name, sub in v.items():
            tb = sub.get("table") if isinstance(sub, dict) else None
            if isinstance(tb, dict) and tb.get("ROW_COUNT"):
                tables[name] = tb
    n = 0
    for p in sorted(SPEECH_DIR.glob("*.json")):
        d = load(p)
        tb = tables.get(d.get("table") or p.stem)
        if not tb:
            continue
        for rk, info in (d.get("rows") or {}).items():
            row = tb.get(rk)
            if not isinstance(row, dict):
                continue
            row = row.get("", row)
            g = (info.get("gender") or "unknown").lower()
            if (info.get("conf") or "low").lower() not in ("high", "med"):
                g = "unknown"
            for col in ("4", "6"):
                en = row.get(col)
                if isinstance(en, str) and en.strip():
                    t.vote(en, "speech", g, info.get("speaker") or "")
                    n += 1
    return n


def mahjong_votes(t):
    """แหล่ง `mahjong`: translations/mahjong_npc_gender.json {row_name: {gender, conf}} × ทุกคอลัมน์ข้อความของแถวนั้น"""
    if not MAHJONG.exists():
        return 0
    genders = load(MAHJONG)
    bin_ = load(paths.DB_EN / "en" / "minigame_mahjong_string_npc.bin.json")
    n = 0
    for k, v in bin_.items():
        if not k.isdigit() or not isinstance(v, dict):
            continue
        for rn, row in v.items():
            info = genders.get(rn)
            if not isinstance(info, dict):
                continue
            g = (info.get("gender") or "unknown").lower()
            if (info.get("conf") or "low").lower() not in ("high", "med"):
                g = "unknown"
            for c, val in row.items():
                if c != "text" and isinstance(val, str) and val.strip():
                    t.vote(val, "mahjong", g, info.get("name") or rn)
                    n += 1
    return n


def build():
    t = Table()
    cue_votes(t)
    talk_votes(t)
    n_scene, n_row, bad = cinema_votes(t)
    unresolved = chat_votes(t)
    popup_votes(t)
    pov_votes(t)
    n_speech = speech_votes(t)
    n_mj = mahjong_votes(t)
    return t.finish(), {"cinema_scenes": n_scene, "cinema_rows": n_row, "cinema_bad": bad,
                        "chat_unresolved": unresolved, "speech_rows": n_speech, "mahjong_rows": n_mj}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    table, stats = build()
    master = load(paths.MASTER_TH)
    print("ข้อความที่รู้เพศ %s · คัตซีน %d ฉาก %s แถว · คู่แชทไม่รู้เพศ %d · ไฟล์คัตซีนมีปัญหา %d" % (
        format(len(table), ","), stats["cinema_scenes"], format(stats["cinema_rows"], ","),
        len(stats["chat_unresolved"]), len(stats["cinema_bad"])))
    for b in stats["cinema_bad"][:10]:
        print("  !", b)
    if not a.write:
        return 0
    OUT.write_text(json.dumps(table, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n = write_doc(table, master, stats)
    print("เขียน %s · %s · ขัดกัน %d บรรทัด" % (OUT.name, DOC, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
