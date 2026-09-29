#!/usr/bin/env python3
"""รวมผลงานเกลาบทเนื้อเรื่องหลัก (translations/review/polish/chNN/) → รายงานให้ lead + เจ้าของตัดสิน

งาน lead หลังทีมเกลาส่งงาน (ชิ้นงานจาก make_polish_chunks.py · บรีฟ polish/POLISH_BRIEF.md · แผน docs/polish_plan.md):
  1. findings_MM[.partN].json → ตรวจโครงทุกจุด + กติกาเดียวกับ apply_sweep_findings.validate + ตรวจเพิ่ม:
     * คำแก้สร้างคำเบิ้ล/คำเวลาที่ห้าม (CHECK_RE ของ fix_doubled_words)
     * คำลงท้าย/สรรพนามขัดเพศผู้พูด (ใช้ผู้พูดที่ทีมระบุ ถ้า conf high/med)
     * บรรทัด [ต้องกลางเพศ] ที่คำแก้มีคำบอกเพศ · บรรทัด [ใช้ร่วม] ที่มีคำแก้ (เตือนให้ lead อ่านว่าใช้ได้ทุกบริบท)
     * คำล็อกที่หายไปจากคำแก้
  2. speakers_MM.json → speakers_all.json · `--write-speakers` เขียน
     translations/speech_speakers/<ตาราง>.json (รวมกับของเดิม ไม่ทับแถวที่มีผู้พูดแล้ว) + build/gender/cinema_low_P<NN>.json
     (ให้ merge_cinema_low.py รวมต่อ)
  3. report.md (สรุป + ทุกจุดเรียงตามฉาก แนบ EN/TH เดิม/คำแก้/คำเตือน) + findings_all.json

ใช้:  python scripts/polish_report.py --chapter 2
      python scripts/polish_report.py --chapter 2 --write-speakers
รายงานอย่างเดียว ไม่แตะ done/master — นำคำแก้ไปใช้ด้วย
      python scripts/apply_sweep_findings.py --dir polish/ch02 [--mid | --mid-ids …] [--reject-ids …] --write
แล้ว remerge_stale.py --write (ดูลำดับเต็มใน docs/polish_plan.md)
"""
import argparse
import io
import json
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from apply_sweep_findings import unesc, validate
from fix_doubled_words import CHECK_RE

SPEECH_DIR = paths.TRANSLATIONS / "speech_speakers"
CATS = OrderedDict([("E", "อังกฤษค้าง/แปลไม่ครบ"), ("M", "ความหมายผิด/หาย"), ("P", "สรรพนาม/ระดับ/เพศ"), ("N", "ไม่เป็นธรรมชาติ"), ("V", "น้ำเสียงตัวละคร"),
                    ("C", "ความต่อเนื่อง/คำล็อก"), ("T", "พิมพ์ผิด/คำเพี้ยน"), ("S", "ช่องว่าง/ตัดบรรทัด"), ("R", "ซ้ำ/เยิ่นเย้อ")])
VALID_G = {"male", "female", "neutral", "unknown"}
MALE_RE = re.compile(r"ครับ|(?<![ก-๛])ผม(?![้่])")
FEMALE_RE = re.compile(r"ค่ะ|คะ(?![ก-๛])|ดิฉัน")
ANY_GENDER_RE = re.compile(r"ครับ|ค่ะ|คะ(?![ก-๛])|ดิฉัน|(?<![ก-๛])ผม(?![้่])|(?<![ก-๛])กู(?![ก-๛])|มึง")
# คำล็อกที่ถ้ามีในคำแปลเดิมแล้วหายไปจากคำแก้ = น่าสงสัย (อาจถูกเกลาทิ้ง)
LOCKED = ("ยากามิ", "ไคโตะ", "ฮิงาชิ", "มัตสึกาเนะ", "เคียวเรอิ", "มาฟุยุ", "คุโรอิวะ", "อาจารย์เก็นดะ", "ไอ้ตัวตุ่น", "ลูกพี่",
          "ถนนพิงก์สตรีท", "พยานที่อยู่", "ย่านแชมเปี้ยน", "Don Quijote")


def esc(s):
    return str(s).replace("\n", "\\n").replace("|", "\\|")


def load_parts(folder, prefix):
    out = []
    for fp in sorted(folder.glob(prefix + "_*.json")):
        if fp.name.endswith("_all.json"):
            continue
        try:
            items = json.loads(fp.read_text(encoding="utf-8-sig"))
        except Exception as e:  # noqa: BLE001 — ไฟล์ agent อาจพัง ต้องรายงานไม่ใช่ล้ม
            out.append((fp.name, e))
            continue
        if isinstance(items, dict):
            items = items.get("findings") or items.get("speakers") or items.get("items") or []
        out.append((fp.name, items))
    return out


def gender_warnings(new, gender, flags):
    w = []
    if "ต้องกลางเพศ" in flags and ANY_GENDER_RE.search(new):
        w.append("บรรทัดต้องกลางเพศแต่คำแก้มีคำบอกเพศ")
    elif gender == "female" and MALE_RE.search(new):
        w.append("ผู้พูดหญิงแต่คำแก้มี ครับ/ผม")
    elif gender == "male" and FEMALE_RE.search(new):
        w.append("ผู้พูดชายแต่คำแก้มี ค่ะ/คะ/ดิฉัน")
    return w


def read_speakers(folder, meta, index):
    speakers, bad = {}, []
    for fname, items in load_parts(folder, "speakers"):
        if isinstance(items, Exception):
            bad.append((fname, "-", "JSON พัง: %s" % items))
            continue
        for it in items:
            if not isinstance(it, dict):
                continue
            sid = str(it.get("id", "")).strip()
            if sid not in meta:
                bad.append((fname, sid, "id ไม่มีใน index"))
                continue
            g = str(it.get("gender", "unknown")).lower()
            conf = str(it.get("conf", "low")).lower()
            speakers[sid] = {"speaker": str(it.get("speaker", "?")).strip() or "?",
                             "gender": g if g in VALID_G else "unknown",
                             "conf": conf if conf in ("high", "med", "low") else "low",
                             "why": str(it.get("why", "")).strip(), "file": fname}
    by_en = defaultdict(set)
    for sid, s in speakers.items():
        if s["speaker"] != "?" and s["conf"] in ("high", "med"):
            by_en[index[sid]].add((s["speaker"].lower(), s["gender"]))
    conflicts = {en: v for en, v in by_en.items() if len({x[1] for x in v}) > 1}
    return speakers, bad, conflicts


def read_findings(folder, meta, index, master, speakers):
    findings, bad = [], []
    for fname, items in load_parts(folder, "findings"):
        if isinstance(items, Exception):
            bad.append((fname, "-", "JSON พัง: %s" % items))
            continue
        for it in items:
            if not isinstance(it, dict):
                continue
            sid = str(it.get("id", "")).strip()
            en = index.get(sid)
            if en is None:
                bad.append((fname, sid, "id ไม่มีใน index"))
                continue
            cat = str(it.get("cat", "?")).strip()[:1].upper()
            if cat not in CATS:
                bad.append((fname, sid, "หมวดไม่รู้จัก %r" % it.get("cat")))
                cat = "N"
            sev = str(it.get("sev", "mid")).strip().lower()
            m = meta[sid]
            old = master.get(en, "")
            new = it.get("th_new")
            status, warns = "", []
            if isinstance(new, str) and new.strip():
                if "\\n" in new and "\n" not in new:
                    new = unesc(new)
                err = validate(old, new)
                status = "ใช้ได้" if err is None else "ใช้ไม่ได้: " + err
                team = speakers.get(sid)
                gender = team["gender"] if team and team["conf"] in ("high", "med") else m["gender"]
                warns += gender_warnings(new, gender, m["flags"])
                if CHECK_RE.search(new) and not CHECK_RE.search(old):
                    warns.append("คำแก้มีคำเบิ้ล/คำเวลาที่ห้าม")
                warns += ["คำล็อก '%s' หายไป" % w for w in LOCKED if w in old and w not in new]
                if "ใช้ร่วม" in m["flags"]:
                    warns.append("ใช้ร่วมที่อื่น: " + ", ".join(m["outside"][:4]))
                if "ไม่มีใน master" in m["flags"]:
                    # apply_sweep_findings ใส่ได้เฉพาะคีย์ที่มีใน done — คีย์ใหม่ต้องเพิ่มเป็น batch เสริม (แบบ batch_UICAPS)
                    warns.append("คีย์ใหม่: เพิ่มผ่าน batch เสริม ไม่ใช่ apply")
                if re.search(r"[A-Za-z]{2}", new) and "มีอังกฤษ" not in " ".join(m["flags"]) and not re.search(r"[A-Za-z]{2}", old):
                    warns.append("คำแก้มีอังกฤษใหม่")
            else:
                new = None
            findings.append({"id": sid, "file": fname, "cat": cat, "sev": sev if sev in ("high", "mid") else "mid",
                             "note": str(it.get("note", "")).strip(), "th_new": new, "status": status,
                             "warn": warns, "en": en, "th": old, **m})
    return findings, bad


def write_speakers(n, speakers, meta):
    speech, cinema = defaultdict(dict), defaultdict(dict)
    for sid, s in speakers.items():
        if s["speaker"] == "?" or s["conf"] == "low":
            continue
        m = meta[sid]
        rec = {"speaker": s["speaker"], "gender": s["gender"], "conf": s["conf"], "why": s["why"],
               "source": "polish/ch%02d/%s" % (n, s["file"])}
        if m["bin"] == "sound_auth.bin":
            speech[m["table"]][m["row"]] = rec
        elif m["bin"] == "auth.bin" and m["speaker"] == "?":
            cinema[m["table"]][m["row"]] = rec
    added = 0
    SPEECH_DIR.mkdir(parents=True, exist_ok=True)
    for table, rows in speech.items():
        fp = SPEECH_DIR / (table + ".json")
        cur = json.loads(fp.read_text(encoding="utf-8")) if fp.exists() else {"table": table, "rows": {}}
        for rk, rec in rows.items():
            old = cur["rows"].get(rk)
            if not old or old.get("speaker") in (None, "", "?"):
                cur["rows"][rk] = rec
                added += 1
        fp.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    cin = paths.BUILD / "gender" / ("cinema_low_P%02d.json" % n)
    cin.parent.mkdir(parents=True, exist_ok=True)
    cin.write_text(json.dumps(cinema, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    return added, sum(len(r) for r in cinema.values())


def main():
    ap = argparse.ArgumentParser(description="รวมผลงานเกลาบทเนื้อเรื่องหลัก")
    ap.add_argument("--chapter", type=int, required=True, choices=range(1, 14))
    ap.add_argument("--write-speakers", action="store_true")
    a = ap.parse_args()
    folder = paths.REVIEW / "polish" / ("ch%02d" % a.chapter)
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))

    speakers, sbad, conflicts = read_speakers(folder, meta, index)
    findings, bad = read_findings(folder, meta, index, master, speakers)
    lines_per_chunk = Counter(sid[:5] for sid in index)
    unknown = [sid for sid, m in meta.items() if m["speaker"] == "?"]
    cov = Counter()
    for sid in unknown:
        s = speakers.get(sid)
        cov["ระบุ " + s["conf"] if s and s["speaker"] != "?" else "ยังไม่รู้"] += 1
    if a.write_speakers:
        added, cin = write_speakers(a.chapter, speakers, meta)
        print("เขียนผู้พูด: speech_speakers +%d แถว · cinema_low_P%02d %d แถว" % (added, a.chapter, cin))

    with_fix = [f for f in findings if f["th_new"]]
    ok = [f for f in with_fix if f["status"] == "ใช้ได้"]
    by_cat, by_chunk = Counter(f["cat"] for f in findings), Counter(f["id"][:5] for f in findings)
    out = ["# เกลาบทที่ %d — รายงานรวม" % a.chapter, "",
           "บรรทัดในบท %s · finding %d (high %d · mid %d) · มีคำแก้ %d · ผ่านกติกา %d · มีคำเตือน %d · โครงพัง %d"
           % ("{:,}".format(len(index)), len(findings), sum(f["sev"] == "high" for f in findings),
              sum(f["sev"] == "mid" for f in findings), len(with_fix), len(ok), sum(bool(f["warn"]) for f in ok),
              len(bad) + len(sbad)), "",
           "ผู้พูดที่เดิมเป็น ? : %d บรรทัด — %s · EN เดียวกันแต่ทีมให้เพศต่างกัน %d" % (
               len(unknown), " · ".join("%s %d" % kv for kv in cov.most_common()) or "-", len(conflicts)), "",
           "| ชิ้น | บรรทัด | finding | ต่อ 100 บรรทัด |", "|---|---|---|---|"]
    for c in sorted(lines_per_chunk):
        out.append("| %s | %d | %d | %.1f |" % (c, lines_per_chunk[c], by_chunk[c], 100.0 * by_chunk[c] / lines_per_chunk[c]))
    out += ["", "| หมวด | ความหมาย | จำนวน | high |", "|---|---|---|---|"]
    out += ["| %s | %s | %d | %d |" % (c, nm, by_cat[c], sum(f["cat"] == c and f["sev"] == "high" for f in findings))
            for c, nm in CATS.items()]
    # apply_sweep_findings ไม่รู้คำเตือนของสคริปต์นี้ → ตัด id ที่มีคำเตือนออกไว้ก่อน (lead อ่านแล้วค่อยเอากลับด้วย --mid-ids)
    warned = sorted(f["id"] for f in ok if f["warn"])
    out += ["", "คำสั่ง apply ตั้งต้น (รับ high ที่ไม่มีคำเตือน · mid ต้องเลือกเองด้วย `--mid-ids` · เติม id ที่เจ้าของไม่รับใน `--reject-ids`):", "",
            "```", "python scripts/apply_sweep_findings.py --dir polish/ch%02d%s --write" % (
                a.chapter, (" --reject-ids " + ",".join(warned)) if warned else ""), "```"]
    if bad or sbad:
        out += ["", "## โครงที่ใช้ไม่ได้", ""] + ["- %s · %s · %s" % x for x in bad + sbad]
    if conflicts:
        out += ["", "## EN เดียวกันที่ทีมให้เพศต่างกัน (ต้องแปลกลางเพศ)", ""]
        out += ["- `%s` → %s" % (esc(en)[:80], ", ".join("%s/%s" % x for x in sorted(v))) for en, v in conflicts.items()]
    out += ["", "## ทุกจุด (เรียงตามฉาก)", ""]
    grouped = defaultdict(list)
    for f in findings:
        grouped[(f["section"], f["table"])].append(f)
    for (sec, table), items in grouped.items():
        out += ["### %s · `%s` — %d จุด" % (sec, table, len(items)), "",
                "| id | ผู้พูด | หมวด | sev | EN | TH เดิม | เกลาเป็น | เหตุผล | ⚠ |", "|---|---|---|---|---|---|---|---|---|"]
        for f in sorted(items, key=lambda x: x["id"]):
            s = speakers.get(f["id"])
            who = "%s (%s)" % (f["speaker"], f["gender"]) + (" → %s (%s/%s)" % (s["speaker"], s["gender"], s["conf"]) if s else "")
            warn = "; ".join(([f["status"]] if f["status"] and f["status"] != "ใช้ได้" else []) + f["warn"])
            out.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                f["id"], esc(who), f["cat"], f["sev"], esc(f["en"]), esc(f["th"]), esc(f["th_new"] or "—"), esc(f["note"]), esc(warn)))
        out.append("")
    (folder / "report.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    (folder / "findings_all.json").write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    (folder / "speakers_all.json").write_text(json.dumps(speakers, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print("บท %d: finding %d (high %d) · คำแก้ผ่าน %d/%d · มีคำเตือน %d · โครงพัง %d · ผู้พูด: %s · เขียน %s" % (
        a.chapter, len(findings), sum(f["sev"] == "high" for f in findings), len(ok), len(with_fix),
        sum(bool(f["warn"]) for f in ok), len(bad) + len(sbad), " · ".join("%s %d" % kv for kv in cov.most_common()) or "-",
        folder / "report.md"))
    print("  หมวด: " + " · ".join("%s %d" % (c, by_cat[c]) for c in CATS))


if __name__ == "__main__":
    main()
