#!/usr/bin/env python3
"""ตัดคำแปลเป็นชิ้นสำหรับ "blind test" — ผู้ตรวจอ่าน **ไทยล้วน** โดยไม่เห็นต้นฉบับ EN (7 ก.ย. 2026)

ที่มา: ผู้เล่นรายงานประโยคที่ "อ่านแล้วแปลก" (รูปประโยคติดโครงอังกฤษ · คำลงท้ายซ้ำ · ช่องว่างผ่าวลี)
ซึ่งการตรวจแบบเทียบคู่ EN/TH (sweep รอบ 21) มองข้ามได้ เพราะผู้ตรวจเห็นต้นฉบับแล้วเข้าใจไปเอง
→ ให้ agent อ่านเฉพาะฝั่งไทยตามลำดับฉาก พร้อมชื่อผู้พูด/เพศ แล้วรายงานจุดที่สะดุดจริง

ขอบเขตรอบแรก (ส่วนที่ผู้เล่นรายงานเข้ามา): บทนำ + บทที่ 1-3 (คัตซีน `auth.bin` · เสียงพากย์
`sound_auth.bin` · บทพูดเดิน `talk.bin/judge_main_c01`) + บท Dice & Cube ทั้งหมด (`talk.bin/judge_minigame_sugoroku*`)

ใช้:  python scripts/make_blind_chunks.py            # เขียน translations/review/blind/chunk_NN.tsv
เอาต์พุต: chunk_NN.tsv (คอลัมน์ id · ฉาก · ผู้พูด · TH — \n ในข้อความเขียนเป็น \n ตัวอักษร)
          index.json (id → คีย์ EN) + meta.json (id → bin/ตาราง/แถว/คอลัมน์/ผู้พูด) สำหรับ blind_report.py
"""
import io
import json
import re
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import paths

OUT = paths.REVIEW / "blind"
CHUNK_CHARS = 55_000          # อักษรไทยต่อชิ้น (ไทยล้วน ≈ 60-80k token เมื่อรวม prompt)
FACTS = paths.EXTRACTED / "facts"
CINEMA = paths.TRANSLATIONS / "cinema_speakers"

# ลำดับการอ่าน = ลำดับเนื้อเรื่อง (ฉากคัตซีนของบทนั้นก่อน แล้วค่อยเสียงพากย์ของบทเดียวกัน)
SCOPE = [
    ("บทนำ", "auth.bin", r"^P0[01]_"),
    ("บท 1 คัตซีน", "auth.bin", r"^a01_"),
    ("บท 1 พากย์", "sound_auth.bin", r"^speech_list_judge_main_c01$"),
    ("บท 1 บทพูดเดิน", "talk.bin", r"^judge_main_c01$"),
    ("บท 2 คัตซีน", "auth.bin", r"^a02_"),
    ("บท 2 พากย์", "sound_auth.bin", r"^speech_list_judge_main_c02$"),
    ("บท 3 คัตซีน", "auth.bin", r"^a03_"),
    ("บท 3 พากย์", "sound_auth.bin", r"^speech_list_judge_main_c03$"),
    ("VR Dice & Cube", "talk.bin", r"^judge_minigame_sugoroku"),
]
TEXT_COLS = {"auth.bin": ("4", "5"), "sound_auth.bin": ("4", "6"), "talk.bin": ("3",)}
GENDER_TH = {"male": "ช", "female": "ญ", "neutral": "กลาง", "unknown": "?"}


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def nested_tables(sub):
    """คืน dict ตารางซ้อนตัวแรกที่มี ROW_COUNT ในแถวของ bin ระดับบน"""
    for val in sub.values():
        if isinstance(val, dict) and "ROW_COUNT" in val:
            return val
    return None


def rows_in_order(table, sort_by_time=False):
    out = []
    for rk, rv in table.items():
        if not rk.isdigit() or rk == "0":
            continue
        for rn, row in rv.items():
            out.append((rk, rn, row))
    if sort_by_time:
        out.sort(key=lambda x: (float(x[2].get("1") or 0), int(x[0])))
    return out


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
                if r.get("speaker"):
                    return r["speaker"], r.get("gender", "unknown")
            return "?", "unknown"
        if bin_name == "sound_auth.bin":
            info = speech_map.get(en, {})
            who = (info.get("speaker_exact") or [None])[0]
            g = voicer_gender.get(who) if who else None
            if not g:
                g = dialogue_gender.get(en, {}).get("gender", "unknown")
            return (who or "?"), (g or "unknown")
        info = talk_speaker.get(en, {})
        return info.get("speaker") or "?", info.get("gender", "unknown")

    lines = []   # (section, scene, speaker_label, en, th, meta)
    seen = set()
    for section, bin_name, pat in SCOPE:
        data = bins[bin_name]
        rx = re.compile(pat)
        for k, v in data.items():
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
                        if not isinstance(th, str) or th == en:
                            continue
                        if ci > 0 and en == primary:
                            continue          # แทร็กที่สองซ้ำแทร็กแรก — ไม่ต้องอ่านซ้ำ
                        key = (en, name)
                        if key in seen:
                            continue          # บรรทัดเดิมซ้ำในฉากเดียวกัน (คีย์ master เดียวกัน) อ่านครั้งเดียวพอ
                        seen.add(key)
                        who, g = speaker_for(bin_name, name, rk, en)
                        label = f"{who} ({GENDER_TH.get(g, '?')})"
                        if ci > 0:
                            label += " [อีกแทร็ก]"
                        else:
                            primary = en
                        lines.append((section, name, label, en, th,
                                      {"bin": bin_name, "table": name, "row": rk, "col": col,
                                       "speaker": who, "gender": g, "alt": ci > 0}))
    # ตัดชิ้น — พยายามตัดที่ขอบฉาก
    chunks, cur, size = [], [], 0
    for i, ln in enumerate(lines):
        n = len(ln[4])
        scene_end = (i + 1 == len(lines)) or (lines[i + 1][1] != ln[1])
        cur.append(ln)
        size += n
        if (size >= CHUNK_CHARS and scene_end) or size >= CHUNK_CHARS * 1.15:
            chunks.append(cur)
            cur, size = [], 0
    if cur:
        chunks.append(cur)

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("chunk_*.tsv"):
        old.unlink()
    esc = lambda s: s.replace("\\", "\\\\").replace("\t", " ").replace("\n", "\\n")
    index, meta = OrderedDict(), OrderedDict()
    for ci, ch in enumerate(chunks, 1):
        rows = ["id\tฉาก\tผู้พูด\tTH"]
        for j, (section, scene, label, en, th, md) in enumerate(ch, 1):
            sid = f"B{ci:02d}-{j:04d}"
            index[sid] = en
            meta[sid] = dict(md, section=section)
            rows.append(f"{sid}\t{section} · {scene}\t{label}\t{esc(th)}")
        (OUT / f"chunk_{ci:02d}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
    (OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
    tot = sum(len(c) for c in chunks)
    print(f"ชิ้น {len(chunks)} · บรรทัด {tot:,} · อักษรไทย {sum(len(l[4]) for l in lines):,}")
    for ci, ch in enumerate(chunks, 1):
        secs = OrderedDict()
        for ln in ch:
            secs[ln[0]] = secs.get(ln[0], 0) + 1
        print(f"  chunk_{ci:02d}: {len(ch):5,} บรรทัด · {sum(len(l[4]) for l in ch):6,} อักษร · "
              + " · ".join(f"{s} {n}" for s, n in secs.items()))
    unknown = sum(1 for l in lines if l[5]["speaker"] == "?")
    print(f"ไม่รู้ผู้พูด {unknown:,}/{tot:,} บรรทัด")


if __name__ == "__main__":
    main()
