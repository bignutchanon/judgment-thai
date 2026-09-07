#!/usr/bin/env python3
"""รวมผลทีม "ตรวจสรรพนาม/ระดับภาษาตามตัวตนตัวละคร" (translations/review/register/) — งาน lead หลังทีมส่งงาน

ทำอะไร:
  1. findings_NN[.partN].json → ตรวจโครง (id · หมวด G/L/H/N/V/S · sev · th_new ผ่านกติกาเดียวกับ apply_sweep_findings.validate)
     → report.md (แนบ EN/TH/ผู้พูด/ฉาก) + findings_all.json — ยังไม่เขียนลง done (ใช้ apply_sweep_findings.py --dir register ทีหลัง)
  2. speakers_NN[.partN].json → ตรวจ id · รวมเป็น speakers_all.json · สรุปความครอบคลุม (ผู้พูด ? ที่ระบุได้ high/med/low)
     · บรรทัดพากย์ (sound_auth) → translations/speech_speakers/<ตาราง>.json (แหล่ง `speech` ของ make_dialogue_gender)
     · บรรทัดคัตซีน (auth) ที่เดิมเป็น ? → build/gender/cinema_low_R.json (ให้ merge_cinema_low.py รวม)
     · ข้อความ EN เดียวกันที่ทีมให้ผู้พูดต่างกัน → รายงานเป็นข้อขัดแย้ง (ต้องกลางเพศ)

ใช้:  python scripts/register_report.py            # เขียน report.md + findings_all.json + speakers_all.json
      python scripts/register_report.py --write    # เขียน speech_speakers/*.json + cinema_low_R.json ด้วย
"""
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

REG = paths.REVIEW / "register"
SPEECH_DIR = paths.TRANSLATIONS / "speech_speakers"
CINEMA_R = paths.BUILD / "gender" / "cinema_low_R.json"
CATS = OrderedDict([("G", "เพศผิด"), ("L", "ระดับผิด"), ("H", "คำเรียกไม่ตรง EN"), ("N", "ต้องกลาง"), ("V", "โทนไม่ตรงตัวละคร"), ("S", "ป้ายผู้พูดผิด")])
VALID_G = {"male", "female", "neutral", "unknown"}


def esc(s):
    return str(s).replace("\n", "\\n").replace("|", "\\|")


def load_parts(prefix):
    """findings_01.json + findings_01.part1.json … → [(ชื่อไฟล์, รายการ)]"""
    out = []
    for fp in sorted(REG.glob(prefix + "_*.json")):
        if fp.name.endswith("_all.json"):
            continue
        try:
            items = json.loads(fp.read_text(encoding="utf-8-sig"))
        except Exception as e:  # noqa: BLE001
            out.append((fp.name, e))
            continue
        if isinstance(items, dict):
            items = items.get("findings") or items.get("speakers") or items.get("items") or []
        out.append((fp.name, items))
    return out


def main():
    write = "--write" in sys.argv
    index = json.loads((REG / "index.json").read_text(encoding="utf-8"))
    meta = json.loads((REG / "meta.json").read_text(encoding="utf-8"))
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    lines_per_chunk = Counter(sid[:3] for sid in index)
    unk_per_chunk = Counter(sid[:3] for sid, m in meta.items() if m["speaker"] == "?")

    # ---- findings ----
    findings, bad = [], []
    for fname, items in load_parts("findings"):
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
                cat = "V"
            sev = str(it.get("sev", "mid")).strip().lower()
            sev = sev if sev in ("high", "mid") else "mid"
            old = master.get(en, "")
            new = it.get("th_new")
            status = ""
            if isinstance(new, str) and new.strip():
                if "\\n" in new and "\n" not in new:
                    new = unesc(new)
                err = validate(old, new)
                status = "ใช้ได้" if err is None else "ใช้ไม่ได้: " + err
            else:
                new = None
                if cat in ("G", "L", "H", "N"):
                    status = "ไม่มีคำแก้ (บังคับสำหรับหมวดนี้)"
            findings.append({"id": sid, "file": fname, "cat": cat, "sev": sev, "note": str(it.get("note", "")).strip(),
                             "th_new": new, "th_new_status": status, "en": en, "th": old, **meta[sid]})

    # ---- speakers ----
    speakers, sbad = {}, []
    by_en = defaultdict(set)
    for fname, items in load_parts("speakers"):
        if isinstance(items, Exception):
            sbad.append((fname, "-", "JSON พัง: %s" % items))
            continue
        for it in items:
            if not isinstance(it, dict):
                continue
            sid = str(it.get("id", "")).strip()
            if sid not in meta:
                sbad.append((fname, sid, "id ไม่มีใน index"))
                continue
            g = str(it.get("gender", "unknown")).lower()
            if g not in VALID_G:
                g = "unknown"
            conf = str(it.get("conf", "low")).lower()
            conf = conf if conf in ("high", "med", "low") else "low"
            spk = str(it.get("speaker", "?")).strip() or "?"
            speakers[sid] = {"speaker": spk, "gender": g, "conf": conf, "why": str(it.get("why", "")).strip(), "file": fname}
            if spk != "?" and conf in ("high", "med"):
                by_en[index[sid]].add((spk.lower(), g))
    conflicts = {en: v for en, v in by_en.items() if len({x[1] for x in v}) > 1}
    cov = Counter()
    for sid, m in meta.items():
        if m["speaker"] != "?":
            continue
        s = speakers.get(sid)
        cov["ระบุ " + s["conf"] if s and s["speaker"] != "?" else "ยังไม่รู้"] += 1

    # ---- speech_speakers / cinema_low_R (เฉพาะ --write) ----
    speech_tables = defaultdict(dict)
    cinema_r = defaultdict(dict)
    for sid, s in speakers.items():
        m = meta[sid]
        if s["speaker"] == "?" and s["conf"] == "low":
            continue
        rec = {"speaker": s["speaker"], "gender": s["gender"], "conf": s["conf"], "why": s["why"], "source": "register/" + s["file"]}
        if m["bin"] == "sound_auth.bin":
            speech_tables[m["table"]][m["row"]] = rec
        elif m["bin"] == "auth.bin" and m["speaker"] == "?":
            cinema_r[m["table"]][m["row"]] = rec
    if write:
        SPEECH_DIR.mkdir(parents=True, exist_ok=True)
        for table, rows in speech_tables.items():
            (SPEECH_DIR / (table + ".json")).write_text(json.dumps({"table": table, "rows": rows}, ensure_ascii=False, indent=1),
                                                       encoding="utf-8", newline="\n")
        CINEMA_R.write_text(json.dumps(cinema_r, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    # ---- รายงาน ----
    by_cat = Counter(f["cat"] for f in findings)
    by_chunk = Counter(f["id"][:3] for f in findings)
    ok_new = sum(1 for f in findings if f["th_new_status"] == "ใช้ได้")
    out = ["# ตรวจสรรพนาม/ระดับภาษา — รายงานรวม (รอบ 22)", "",
           f"บรรทัดที่ให้อ่าน {sum(lines_per_chunk.values()):,} · finding {len(findings):,} (high {sum(1 for f in findings if f['sev']=='high')}) · "
           f"คำแก้ที่เสนอ {sum(1 for f in findings if f['th_new'])} · ผ่านกติกา {ok_new} · โครงพัง {len(bad)}", "",
           "## ความครอบคลุมผู้พูด (บรรทัดที่เดิมเป็น ?)", "",
           f"ทั้งหมด {sum(unk_per_chunk.values()):,} บรรทัด — " + " · ".join(f"{k} {v:,}" for k, v in cov.most_common()),
           f"· ตารางพากย์ที่ได้ผู้พูด {len(speech_tables)} ตาราง / {sum(len(r) for r in speech_tables.values()):,} แถว · คัตซีน {sum(len(r) for r in cinema_r.values())} แถว"
           + ("" if write else " (ยังไม่เขียน — ใส่ --write)"), "",
           f"ข้อความ EN เดียวกันที่ทีมให้เพศต่างกัน (ต้องแปลกลางเพศ): {len(conflicts)}", ""]
    for en, v in list(conflicts.items())[:30]:
        out.append(f"- `{esc(en)[:80]}` → " + ", ".join(f"{s}/{g}" for s, g in sorted(v)))
    out += ["", "## finding แยกชิ้น / หมวด", "", "| ชิ้น | บรรทัด | ? เดิม | finding |", "|---|---|---|---|"]
    for c in sorted(lines_per_chunk):
        out.append(f"| {c} | {lines_per_chunk[c]:,} | {unk_per_chunk[c]:,} | {by_chunk[c]} |")
    out += ["", "| หมวด | ความหมาย | จำนวน | high |", "|---|---|---|---|"]
    for c, name in CATS.items():
        out.append(f"| {c} | {name} | {by_cat[c]} | {sum(1 for f in findings if f['cat']==c and f['sev']=='high')} |")
    if bad or sbad:
        out += ["", "## โครงที่ใช้ไม่ได้", ""] + [f"- {a} · {b} · {c}" for a, b, c in bad + sbad]
    out += ["", "## รายการ finding ทั้งหมด (เรียงตามฉาก)", ""]
    grouped = defaultdict(list)
    for f in findings:
        grouped[(f["section"], f["table"])].append(f)
    for (sec, table), items in grouped.items():
        out += [f"### {sec} · `{table}` — {len(items)} จุด", "",
                "| id | ผู้พูด (ไฟล์ → ทีม) | หมวด | sev | TH ปัจจุบัน | EN | เหตุผล | คำแก้ |", "|---|---|---|---|---|---|---|---|"]
        for f in sorted(items, key=lambda x: x["id"]):
            s = speakers.get(f["id"], {})
            spk = f"{f['speaker']} ({f['gender']})" + (f" → {s['speaker']} ({s['gender']}/{s['conf']})" if s else "")
            fix = (esc(f["th_new"]) if f["th_new"] else "") + (" ⚠" + f["th_new_status"] if f["th_new_status"] and f["th_new_status"] != "ใช้ได้" else "")
            out.append(f"| {f['id']} | {esc(spk)} | {f['cat']} | {f['sev']} | {esc(f['th'])} | {esc(f['en'])} | {esc(f['note'])} | {fix} |")
        out.append("")
    (REG / "report.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    (REG / "findings_all.json").write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    (REG / "speakers_all.json").write_text(json.dumps(speakers, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print(f"finding {len(findings)} (high {sum(1 for f in findings if f['sev']=='high')}) · คำแก้ผ่าน {ok_new}/{sum(1 for f in findings if f['th_new'])} · "
          f"โครงพัง {len(bad)+len(sbad)} · ผู้พูด: " + " · ".join(f"{k} {v}" for k, v in cov.most_common())
          + f" · ขัดแย้ง {len(conflicts)} · เขียน {REG / 'report.md'}" + ("" if write else " (speech_speakers ยังไม่เขียน)"))
    print("  หมวด: " + " · ".join(f"{c} {by_cat[c]}" for c in CATS))


if __name__ == "__main__":
    main()
