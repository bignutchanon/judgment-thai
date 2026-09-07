#!/usr/bin/env python3
"""ตัดบทพูดเป็นชิ้นสำหรับทีม "ตรวจสรรพนาม/ระดับภาษาตามตัวตนตัวละคร" (รอบ 22 · 7 ก.ย. 2026)

ต่างจาก make_blind_chunks.py ตรงที่ **ให้ EN ด้วย** และให้ผู้พูด+เพศเท่าที่ไฟล์เกมรู้ — งานของทีมคือ
(1) ระบุผู้พูดของบรรทัดที่ยังเป็น ? (เสียงพากย์ 86% ไม่มีชื่อผู้พูด) จากบริบท
(2) รายงาน/แก้บรรทัดที่สรรพนาม คำลงท้าย ระดับ T1/T2/T3 หรือคำเรียกคู่สนทนา ไม่ตรงกับผู้พูดตาม PRONOUN_MATRIX

ขอบเขตรอบแรกเท่ากับ blind test: บทนำ + บท 1-3 (คัตซีน/พากย์/บทพูดเดิน) + Dice & Cube ทั้งหมด

ใช้:  python scripts/make_register_chunks.py          # เขียน translations/review/register/chunk_NN.tsv
เอาต์พุต: chunk_NN.tsv (id · ฉาก · ผู้พูด · EN · TH — \n เขียนเป็น \n ตัวอักษร) + index.json + meta.json
"""
import io
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from make_blind_chunks import SCOPE, TEXT_COLS, GENDER_TH, load, nested_tables, rows_in_order, FACTS, CINEMA

OUT = paths.REVIEW / "register"
CHUNK_LINES = 1000            # EN+TH ต่อชิ้น ≈ 1,000 บรรทัด (≈ 150-220k token ต่อ agent)


def main():
    master = load(paths.MASTER_TH)
    bins = {b: load(paths.DB_EN / "en" / (b + ".json")) for b in ("auth.bin", "sound_auth.bin", "talk.bin")}
    speech_map = load(FACTS / "speech_speaker_map.json")
    voicer_gender = load(FACTS / "voicer_gender.json")
    dialogue_gender = load(FACTS / "dialogue_gender.json")
    talk_speaker = load(FACTS / "talk_speaker.json")

    def speaker_for(bin_name, scene, rk, en):
        if bin_name == "auth.bin":
            f = CINEMA / (scene + ".json")
            if f.exists():
                r = load(f).get("rows", {}).get(rk, {})
                if r.get("speaker") and r.get("conf") in ("high", "med"):
                    return r["speaker"], r.get("gender", "unknown")
            return "?", dialogue_gender.get(en, {}).get("gender", "unknown")
        if bin_name == "sound_auth.bin":
            info = speech_map.get(en, {})
            who = (info.get("speaker_exact") or [None])[0]
            g = voicer_gender.get(who) if who else None
            if not g:
                g = dialogue_gender.get(en, {}).get("gender", "unknown")
            return (who or "?"), (g or "unknown")
        info = talk_speaker.get(en, {})
        return info.get("speaker") or "?", info.get("gender", "unknown")

    lines, seen = [], set()
    for section, bin_name, pat in SCOPE:
        rx = re.compile(pat)
        for k, v in bins[bin_name].items():
            if not k.isdigit():
                continue
            for name, sub in v.items():
                if not rx.search(name) or not isinstance(sub, dict):
                    continue
                table = nested_tables(sub)
                if table is None:
                    continue
                cols = TEXT_COLS[bin_name]
                for rk, rn, row in rows_in_order(table, sort_by_time=(bin_name == "auth.bin")):
                    primary = None
                    for ci, col in enumerate(cols):
                        en = row.get(col)
                        if not isinstance(en, str) or not en.strip():
                            continue
                        th = master.get(en)
                        if not isinstance(th, str) or th == en or (ci > 0 and en == primary) or (en, name) in seen:
                            continue
                        seen.add((en, name))
                        who, g = speaker_for(bin_name, name, rk, en)
                        label = f"{who} ({GENDER_TH.get(g, '?')})" + (" [อีกแทร็ก]" if ci > 0 else "")
                        if ci == 0:
                            primary = en
                        dgi = dialogue_gender.get(en, {})
                        whos = {w.strip().lower() for s in dgi.get("sources", []) if s.get("src") != "pov" and s.get("who")
                                for w in str(s.get("who")).split(",") if w.strip()}
                        shared = dgi.get("gender") == "mixed" or len(whos) > 1      # คนละคนพูดข้อความเดียวกันจริง ๆ ไม่ใช่แค่หลายแหล่งหลักฐาน
                        lines.append((section, name, label, en, th,
                                      {"bin": bin_name, "table": name, "row": rk, "col": col, "speaker": who,
                                       "gender": g, "alt": ci > 0, "shared": shared}))
    chunks, cur = [], []
    for i, ln in enumerate(lines):
        cur.append(ln)
        scene_end = (i + 1 == len(lines)) or (lines[i + 1][1] != ln[1])
        if (len(cur) >= CHUNK_LINES and scene_end) or len(cur) >= CHUNK_LINES * 1.2:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("chunk_*.tsv"):
        old.unlink()
    esc = lambda s: s.replace("\\", "\\\\").replace("\t", " ").replace("\n", "\\n")
    index, meta = OrderedDict(), OrderedDict()
    for ci, ch in enumerate(chunks, 1):
        rows = ["id\tฉาก\tผู้พูด\tEN\tTH"]
        for j, (section, scene, label, en, th, md) in enumerate(ch, 1):
            sid = f"R{ci:02d}-{j:04d}"
            index[sid] = en
            meta[sid] = dict(md, section=section)
            flag = " [ใช้ร่วมหลายคน]" if md["shared"] else ""
            rows.append(f"{sid}\t{section} · {scene}\t{label}{flag}\t{esc(en)}\t{esc(th)}")
        (OUT / f"chunk_{ci:02d}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
    (OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
    tot = sum(len(c) for c in chunks)
    print(f"ชิ้น {len(chunks)} · บรรทัด {tot:,} · ผู้พูด ? {sum(1 for l in lines if l[5]['speaker'] == '?'):,}")
    for ci, ch in enumerate(chunks, 1):
        secs = OrderedDict()
        for ln in ch:
            secs[ln[0]] = secs.get(ln[0], 0) + 1
        unk = sum(1 for l in ch if l[5]["speaker"] == "?")
        print(f"  chunk_{ci:02d}: {len(ch):5,} บรรทัด · ผู้พูด ? {unk:4d} · " + " · ".join(f"{s} {n}" for s, n in secs.items()))


if __name__ == "__main__":
    main()
