#!/usr/bin/env python3
"""รวมผล blind test (translations/review/blind/findings_*.json) → รายงาน report.md + findings_all.json

blind test = ทีมอ่านคำแปลไทยล้วนโดยไม่เห็น EN (ดู BLIND_BRIEF.md · ชิ้นงานจาก make_blind_chunks.py)
สคริปต์นี้เป็นงาน lead หลังทีมส่งงาน:
  * ตรวจโครง finding ทุกจุด (id มีใน index · หมวด/ระดับถูกต้อง · th_new ผ่านกติกาเดียวกับ apply_sweep_findings.validate)
  * แนบ EN ต้นฉบับ + ผู้พูด + ฉาก ให้ทุกจุด (ทีมไม่เห็น EN — lead ต้องเห็นเพื่อตัดสินว่าเป็นแปลผิดหรือแค่สำนวน)
  * นับอัตราสะดุดต่อ 100 บรรทัด แยกตามชิ้น/บท/หมวด

ใช้:  python scripts/blind_report.py            # เขียน translations/review/blind/report.md + findings_all.json
รายงานอย่างเดียว ไม่แตะ done/master — การนำคำแก้ไปใช้เป็นคำตัดสินของเจ้าของโปรเจกต์
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

BLIND = paths.REVIEW / "blind"
CATS = OrderedDict([("U", "ไม่เข้าใจ/กำกวม"), ("N", "ไม่เป็นธรรมชาติ"), ("T", "พิมพ์ผิด/คำเพี้ยน"),
                    ("P", "สรรพนาม/คำลงท้าย"), ("R", "ซ้ำจนรก"), ("S", "ช่องว่างผ่าคำ"), ("F", "ติดอ่าง/อุทาน")])
# คำในพจนานุกรมที่ newmm ประกบข้ามช่องว่างแล้วลวง (พิสูจน์จากผลจริง 7 ก.ย. 2026 — "ใช่ครับ ผมได้ยิน" ไม่ใช่ "ครับผม")
MECH_FALSE = {"ครับผม", "แล้วแต่", "น่าจะ", "เฮ้อ", "เป็นไรไป", "มายา", "ดีฉัน", "ที่แล้ว", "รู้เรื่อง", "อยากได้", "เห็นภาพ"}


def esc(s):
    return str(s).replace("\n", "\\n").replace("|", "\\|")


def main():
    index = json.loads((BLIND / "index.json").read_text(encoding="utf-8"))
    meta = json.loads((BLIND / "meta.json").read_text(encoding="utf-8"))
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    lines_per_chunk = Counter(sid[:3] for sid in index)          # "B01"
    lines_per_section = Counter(m["section"] for m in meta.values())

    findings, bad = [], []
    files = sorted(p for p in BLIND.glob("findings_*.json") if p.name != "findings_all.json")   # ผลรวมของสคริปต์นี้เอง ห้ามอ่านกลับ
    for fp in files:
        try:
            items = json.loads(fp.read_text(encoding="utf-8-sig"))
        except Exception as e:  # noqa: BLE001 — ไฟล์ agent อาจพัง ต้องรายงานไม่ใช่ล้ม
            bad.append((fp.name, "-", "JSON พัง: %s" % e))
            continue
        if isinstance(items, dict):
            items = items.get("findings", [])
        for it in items:
            if not isinstance(it, dict):
                continue
            sid = str(it.get("id", "")).strip()
            en = index.get(sid)
            if en is None:
                bad.append((fp.name, sid, "id ไม่มีใน index"))
                continue
            cat = str(it.get("cat", "?")).strip()[:1].upper()
            if cat not in CATS:
                bad.append((fp.name, sid, "หมวดไม่รู้จัก %r" % it.get("cat")))
                cat = "N"
            sev = str(it.get("sev", "mid")).strip().lower()
            if sev not in ("high", "mid"):
                sev = "mid"
            old = master.get(en, "")
            new = it.get("th_new")
            new_status = ""
            if isinstance(new, str) and new.strip():
                if "\\n" in new and "\n" not in new:
                    new = unesc(new)
                err = validate(old, new)
                new_status = "ใช้ได้" if err is None else "ใช้ไม่ได้: " + err
            else:
                new = None
            findings.append({"id": sid, "file": fp.name, "cat": cat, "sev": sev, "note": str(it.get("note", "")).strip(),
                             "th_new": new, "th_new_status": new_status, "en": en, "th": old, **meta[sid]})

    # ---- สรุปตัวเลข ----
    by_chunk = Counter(f["id"][:3] for f in findings)
    high_chunk = Counter(f["id"][:3] for f in findings if f["sev"] == "high")
    by_cat = Counter(f["cat"] for f in findings)
    by_sec = Counter(f["section"] for f in findings)
    high_sec = Counter(f["section"] for f in findings if f["sev"] == "high")
    uniq_ids = len({f["id"] for f in findings})

    out = ["# Blind test — รายงานรวม (Judgment ม็อดแปลไทย)", "",
           f"ชิ้นงาน {len(lines_per_chunk)} ชิ้น · บรรทัดที่ให้อ่าน {sum(lines_per_chunk.values()):,} · "
           f"ไฟล์ผลที่ส่ง {len(files)} · finding {len(findings):,} จุด (บรรทัดไม่ซ้ำ {uniq_ids:,}) · "
           f"high {sum(1 for f in findings if f['sev']=='high'):,} · mid {sum(1 for f in findings if f['sev']=='mid'):,} · "
           f"โครงพัง {len(bad)}", "",
           "## อัตราสะดุดต่อ 100 บรรทัด — แยกตามชิ้น", "", "| ชิ้น | บรรทัด | finding | high | ต่อ 100 บรรทัด |", "|---|---|---|---|---|"]
    for c in sorted(lines_per_chunk):
        n = lines_per_chunk[c]
        out.append(f"| {c} | {n:,} | {by_chunk[c]} | {high_chunk[c]} | {100*by_chunk[c]/n:.1f} |")
    out += ["", "## แยกตามบท/ชนิดข้อความ", "", "| ส่วน | บรรทัด | finding | high | ต่อ 100 บรรทัด |", "|---|---|---|---|---|"]
    for s, n in lines_per_section.items():
        out.append(f"| {s} | {n:,} | {by_sec[s]} | {high_sec[s]} | {100*by_sec[s]/n:.1f} |")
    out += ["", "## แยกตามหมวด", "", "| หมวด | ความหมาย | จำนวน | high |", "|---|---|---|---|"]
    for c, name in CATS.items():
        out.append(f"| {c} | {name} | {by_cat[c]} | {sum(1 for f in findings if f['cat']==c and f['sev']=='high')} |")
    ok_new = sum(1 for f in findings if f["th_new_status"] == "ใช้ได้")
    out += ["", f"คำแก้ที่เสนอมา {sum(1 for f in findings if f['th_new'])} จุด · ผ่านกติกา (\\n/tag/run≤36/ความยาว) {ok_new} จุด", ""]
    if bad:
        out += ["## โครง finding ที่ใช้ไม่ได้", ""] + [f"- {a} · {b} · {c}" for a, b, c in bad] + [""]

    # ---- สอบเทียบกับที่ lead อ่านเอง (ช่วงสุ่ม) ----
    calib_files = sorted(BLIND.glob("lead_calibration_*.json"))
    if calib_files:
        out += ["## สอบเทียบ: lead สุ่มอ่านเองแบบ blind แล้วเทียบกับที่ทีมจับได้", "",
                "| ช่วงสุ่ม | บรรทัด | lead จด | ทีมจด (ในช่วงเดียวกัน) | ตรงกัน | ทีมจับได้เฉพาะที่ lead จด |",
                "|---|---|---|---|---|---|"]
        agent_ids = {f["id"] for f in findings}
        calib_rows = []
        for cf in calib_files:
            cd = json.loads(cf.read_text(encoding="utf-8-sig"))
            lead = {str(x["id"]): x for x in cd.get("findings", [])}
            for chunk, a, b in cd.get("sample_ranges", []):
                in_range = lambda sid: sid.startswith(chunk) and a <= int(sid.split("-")[1]) <= b
                lead_in = {k for k in lead if in_range(k)}
                team_in = {k for k in agent_ids if in_range(k)}
                both = lead_in & team_in
                rate = f"{100*len(both)/len(lead_in):.0f}%" if lead_in else "-"
                out.append(f"| {chunk} {a}-{b} | {b-a} | {len(lead_in)} | {len(team_in)} | {len(both)} | {rate} |")
            for k, x in lead.items():
                calib_rows.append((k, x, k in agent_ids))
        out += ["", "| id | หมวด | sev | ทีมจับได้? | TH | EN | เหตุผลของ lead |", "|---|---|---|---|---|---|---|"]
        for k, x, hit in sorted(calib_rows):
            out.append(f"| {k} | {x.get('cat')} | {x.get('sev')} | {'ใช่' if hit else 'ไม่'} | {esc(master.get(index.get(k, ''), ''))} | "
                       f"{esc(index.get(k, ''))} | {esc(x.get('note', ''))} |")
        out.append("")

    # ---- ตรวจเชิงกล: ช่องว่างตกกลางคำในพจนานุกรม (pythainlp newmm) ----
    try:
        from pythainlp import word_tokenize
        from pythainlp.corpus import thai_words
        words = thai_words()
        mech = []
        rx = re.compile(r"([฀-๿]+) ([฀-๿]+)")
        for sid, en in index.items():
            th = master.get(en, "")
            for mt in rx.finditer(th):
                left, right = mt.group(1)[-12:], mt.group(2)[:12]
                joined = left + right
                pos, span = 0, None
                for tok in word_tokenize(joined, engine="newmm", keep_whitespace=False):
                    if pos < len(left) < pos + len(tok):
                        span = tok
                        break
                    pos += len(tok)
                # ตัดผลลวงที่พิสูจน์แล้วรอบ 7 ก.ย.: ช่องว่างหน้า ๆ เป็นแบบแผนถูกต้อง · คำที่บังเอิญประกบเป็นคำใหม่ข้ามประโยค
                if span and span in words and len(span) >= 3 and not span.endswith("ๆ") and span not in MECH_FALSE:
                    mech.append((sid, span, mt.group(1)[-8:] + "␣" + mt.group(2)[:8]))
        out += ["## ตรวจเชิงกล — ช่องว่างตกกลางคำที่มีในพจนานุกรม (pythainlp newmm · เฉพาะบรรทัดในขอบเขต blind test)", "",
                f"ผู้สมัคร {len(mech)} จุดหลังตัดผลลวง (ช่องว่างหน้า ๆ · คำที่บังเอิญประกบข้ามประโยค เช่น ครับ|ผม แล้ว|แต่) — "
                f"ต้องดูด้วยตาทุกจุด · ทีม blind จับได้ {sum(1 for s, _, _ in mech if s in agent_ids)} จุด", "",
                "| id | คำที่ถูกผ่า | บริบท | TH เต็ม |", "|---|---|---|---|"]
        for sid, span, ctx in mech:
            out.append(f"| {sid} | {span} | {esc(ctx)} | {esc(master.get(index[sid], ''))} |")
        out.append("")
    except ImportError:
        out += ["(ไม่มี pythainlp — ข้ามการตรวจเชิงกล)", ""]

    # ---- ตรวจเชิงกล 2: ยากามิพูดออกเสียงด้วย "ฉัน" (กติกาล็อก: ยากามิ = ผม เสมอ · คิดในใจในวงเล็บใช้ ฉัน ได้) ----
    yag = []
    for sid, en in index.items():
        m = meta[sid]
        if str(m.get("speaker", "")).lower() not in ("yagami", "takayuki yagami"):
            continue
        th = master.get(en, "")
        spoken = re.sub(r"\([^)]*\)", "", th)
        if re.search(r"(?<![ก-๙])(ฉัน|ชั้น)(?![ก-๙])", spoken):
            yag.append(sid)
    out += ["## ตรวจเชิงกล 2 — ยากามิ (ผู้พูดระบุชัด) พูดออกเสียงด้วย ฉัน/ชั้น", "",
            f"พบ {len(yag)} บรรทัด (ทีม blind จับได้ {sum(1 for s in yag if s in agent_ids)}) — ตัดบรรทัดที่ผู้พูดเป็น ? ออกแล้ว "
            "จึงเป็นขอบล่างของจำนวนจริง", ""]
    if yag:
        out += ["| id | ฉาก | TH | EN |", "|---|---|---|---|"]
        for sid in yag:
            out.append(f"| {sid} | {meta[sid]['table']} | {esc(master.get(index[sid], ''))} | {esc(index[sid])} |")
    out.append("")

    # ---- ตรวจเชิงกล 3: ผู้พูดคนเดียวกันในฉากคัตซีน/บทพูดเดินเดียวกัน ใช้ทั้ง กู/มึง และ ผม/ครับ/คุณ ----
    T3 = re.compile(r"(?<![ก-๙])(กู|มึง)(?![ก-๙])")
    T1 = re.compile(r"(?<![ก-๙])(ผม|ดิฉัน|ครับ|ค่ะ|คะ)(?![ก-๙])")
    per = defaultdict(lambda: {"t3": [], "t1": []})
    for sid, en in index.items():
        m = meta[sid]
        if m["bin"] == "sound_auth.bin" or m.get("speaker") in ("?", "", None) or m.get("alt"):
            continue
        th = re.sub(r"\([^)]*\)", "", master.get(en, ""))
        key = (m["table"], m["speaker"])
        if T3.search(th):
            per[key]["t3"].append(sid)
        if T1.search(th):
            per[key]["t1"].append(sid)
    mixed = {k: v for k, v in per.items() if v["t3"] and v["t1"]}
    out += ["## ตรวจเชิงกล 3 — ผู้พูดคนเดียวกันในฉากเดียวกันใช้ทั้งระดับหยาบ (กู/มึง) และสุภาพ (ผม/ครับ/ค่ะ)", "",
            f"พบ {len(mixed)} คู่ ฉาก×ผู้พูด (เฉพาะคัตซีน `auth.bin` และบทพูดเดิน `talk.bin` ที่รู้ผู้พูด · ข้ามเสียงพากย์ทั้งบทเพราะกว้างเกิน) — "
            "อาจตั้งใจ (ประชด/อารมณ์แตก) ต้องอ่านบริบท", ""]
    if mixed:
        out += ["| ฉาก | ผู้พูด | บรรทัดหยาบ | บรรทัดสุภาพ |", "|---|---|---|---|"]
        for (table, spk), v in sorted(mixed.items()):
            out.append(f"| {table} | {esc(spk)} | {', '.join(v['t3'][:6])} | {', '.join(v['t1'][:6])} |")
    out.append("")

    # ---- คำตัดสิน lead (lead_verdicts.json — เขียนด้วยมือหลังเห็น EN) ----
    verdict_path = BLIND / "lead_verdicts.json"
    verdicts = {}
    if verdict_path.exists():
        verdicts = {k: v for k, v in json.loads(verdict_path.read_text(encoding="utf-8-sig")).items() if not k.startswith("_")}
        vc = Counter(v.get("verdict", "?") for v in verdicts.values())
        team_v = Counter(verdicts[f["id"]]["verdict"] for f in findings if f["id"] in verdicts)
        out += ["## คำตัดสิน lead", "",
                f"ตัดสินแล้ว {len(verdicts)} จุด (ของทีม {sum(team_v.values())}/{len(findings)} · ที่เหลือมาจากการสอบเทียบ/ตรวจเชิงกลของ lead) — "
                + " · ".join(f"{k} {n}" for k, n in vc.most_common()), "",
                "| id | คำตัดสิน | เหตุผล |", "|---|---|---|"]
        for k, v in sorted(verdicts.items()):
            out.append(f"| {k} | {v.get('verdict')} | {esc(v.get('why', ''))} |")
        out.append("")

    out += ["## รายการทั้งหมด (เรียงตามฉาก — EN แนบให้ lead ตัดสิน ทีมไม่ได้เห็น)", ""]
    grouped = defaultdict(list)
    for f in findings:
        grouped[(f["section"], f["table"])].append(f)
    for (sec, table), items in grouped.items():
        out.append(f"### {sec} · `{table}` — {len(items)} จุด")
        out.append("")
        out.append("| id | ผู้พูด | หมวด | sev | lead | TH ปัจจุบัน | EN | เหตุผลของผู้อ่าน | คำแก้ที่เสนอ |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        for f in sorted(items, key=lambda x: x["id"]):
            spk = f"{f['speaker']} ({f['gender']})" + (" [อีกแทร็ก]" if f.get("alt") else "")
            fix = (esc(f["th_new"]) + (" ⚠" + f["th_new_status"] if f["th_new_status"] != "ใช้ได้" else "")) if f["th_new"] else ""
            lv = verdicts.get(f["id"], {}).get("verdict", "-")
            out.append(f"| {f['id']} | {esc(spk)} | {f['cat']} | {f['sev']} | {lv} | {esc(f['th'])} | {esc(f['en'])} | {esc(f['note'])} | {fix} |")
        out.append("")
    (BLIND / "report.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    (BLIND / "findings_all.json").write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print(f"finding {len(findings):,} จุด · high {sum(1 for f in findings if f['sev']=='high'):,} · โครงพัง {len(bad)} · "
          f"เขียน {BLIND / 'report.md'}")
    for c in sorted(lines_per_chunk):
        print(f"  {c}: {by_chunk[c]:4d} / {lines_per_chunk[c]:5,} บรรทัด = {100*by_chunk[c]/lines_per_chunk[c]:.1f} ต่อ 100")
    print("  หมวด: " + " · ".join(f"{c} {by_cat[c]}" for c in CATS))


if __name__ == "__main__":
    main()
