#!/usr/bin/env python3
"""ถอดเพศผู้พูด **รายบรรทัด** จากชื่อคิวเสียงใน `sound_auth.bin`

พอร์ตวิธีมาจาก `D:\\Projects\\lost-judgment-thai\\docs\\reference\\CUE_GENDER_METHOD.md`
(เอกสารกลางของตระกูล Dragon Engine — พิสูจน์กับ Lost Judgment แล้ว 99.98% ของแถวบทพูด)
อ่านเอกสารนั้นก่อนแก้สคริปต์นี้ทุกครั้ง

## ทำไมต้องมี ทั้งที่โปรเจกต์นี้มี `voicer_gender.json` อยู่แล้ว

`voicer_gender.json` บอกเพศ **ต่อ voicer** และ `talk_speaker.json` บอกเพศ **ต่อชื่อผู้พูด**
สองอันนั้นพลาดได้สองแบบ:

  * ชื่อผู้พูดเดียวถูกใช้กับตัวละครหลายคน (บทเดินเมือง/NPC บรรยายลักษณะ) → เสียงข้างมากกลบฝั่งน้อย
  * บทคัตซีนใน `sound_auth.bin` ไม่มีคอลัมน์ชื่อผู้พูดเลย (คอลัมน์ 3 ว่าง) จึงผูกกับทะเบียนชื่อไม่ได้

แต่ **ทุกแถวบทพูดผูกกับคิวเสียงของตัวเอง** และชื่อคิวลงท้ายด้วย id ของ voicer เสมอ
จึงชี้เพศได้ตรง ๆ รายบรรทัด ไม่ต้องผ่านชื่อผู้พูด

## โครงข้อมูลของ Judgment (ต่างจาก Lost Judgment สองจุด — verify แล้ว 29 ส.ค. 2026)

    db.judge.en.par → en/sound_auth.bin
      └── แถวชื่อ speech_list_*        (138 แถว)
            └── table                  (13 คอลัมน์ = แถวบทพูด)
                  คอลัมน์ 1  = เลขคิวสากล
                  คอลัมน์ 4  = บทพูด EN ฉบับเต็ม
                  คอลัมน์ 6  = บทพูด EN อีกรูปของคิวเดียวกัน  (LJ ใช้คอลัมน์ 13)
                  คอลัมน์ 3  = **ว่างทั้งเกม** (LJ ใช้เป็น index ของชื่อผู้พูด)
            └── table.subTable         (แถวคิวเสียง · ชื่อแถว = ชื่อคิว · คอลัมน์ 0 = เลขคิวสากล)

    en/sound_voicer.bin → คอลัมน์ `sex` (1 = ชาย · 2 = หญิง · 0 = ไม่ระบุ)
                          **ไม่มีคอลัมน์ `voice_type`** (LJ มี — ของภาคนี้ไม่มีให้ใช้)

ชื่อคิวมีคำนำหน้าไม่คงที่แต่ id ของ voicer อยู่ท้ายเสมอ จึงตัดคำหน้าทีละท่อนด้วย `_`
จนได้ชื่อที่มีจริงใน `sound_voicer` (`speech_m01_00100_kaito` → `kaito`)

## กติกาผลลัพธ์

  * ทุกคิวของข้อความนั้นเป็นชายล้วน  -> `male`
  * หญิงล้วน                        -> `female`
  * มีทั้งสองฝั่ง                    -> `mixed` = **รู้แน่ว่าใช้ร่วมกันหลายเพศ ต้องแปลกลางเพศ**
    (ต่างจาก "ไม่มีข้อมูล" ซึ่งคือข้อความที่ไม่โผล่ในไฟล์นี้เลย)

ผลลัพธ์: `extracted/facts/line_gender.json`

ใช้:
  python scripts/make_line_gender.py            # ดูสรุปเฉย ๆ
  python scripts/make_line_gender.py --write
"""
import argparse
import collections
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")           # กติกาเหล็กข้อ 6
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

SRC = paths.DB_EN / "en" / "sound_auth.bin.json"
VOICER = paths.DB_EN / "en" / "sound_voicer.bin.json"
OUT = paths.EXTRACTED / "facts" / "line_gender.json"

SEX_NAME = {1: "male", 2: "female"}
TEXT_COLS = ("4", "6")        # บทพูด EN สองรูปของคิวเดียวกัน — เก็บแยก ห้ามต่อสตริง


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def first_row(v):
    """แถว ARMP หนึ่งแถว = {ชื่อแถว: {คอลัมน์...}} — คืน (ชื่อแถว, dict คอลัมน์)"""
    if not isinstance(v, dict) or not v:
        return None, None
    k = list(v.keys())[0]
    r = v[k]
    return (k or ""), (r if isinstance(r, dict) else None)


def voicer_table():
    """id ของ voicer (ตัวเล็ก) -> sex  เฉพาะตัวที่ระบุเพศ"""
    out = {}
    for k, v in load(VOICER).items():
        if not k.isdigit():
            continue
        name, row = first_row(v)
        if not row or not name:
            continue
        if row.get("sex") in SEX_NAME:
            out[name.lower()] = row["sex"]
    return out


def iter_speech_tables(node):
    """ทุกแถวที่ชื่อขึ้นต้นด้วย speech_list (ไล่ลงทุกชั้น เผื่อโครงเปลี่ยน)"""
    if not isinstance(node, dict):
        return
    for k, v in node.items():
        if isinstance(k, str) and k.startswith("speech_list") and isinstance(v, dict):
            yield k, v
        else:
            yield from iter_speech_tables(v)


def suffix_voicer(cue, vox):
    """ตัดคำหน้าของชื่อคิวทีละท่อนจนเจอ id ที่มีจริงใน sound_voicer"""
    parts = (cue or "").lower().split("_")
    for i in range(1, len(parts)):
        cand = "_".join(parts[i:])
        if cand in vox:
            return cand
    return None


def build():
    vox = voicer_table()
    data = load(SRC)

    votes = collections.defaultdict(collections.Counter)      # ข้อความ EN -> Counter เพศ
    voicers = collections.defaultdict(collections.Counter)
    cues = {}
    stats = collections.Counter()

    for list_name, node in iter_speech_tables(data):
        tbl = node.get("table")
        if not isinstance(tbl, dict):
            continue
        by_cue = {}
        for k, v in (tbl.get("subTable") or {}).items():
            if not k.isdigit():
                continue
            cue, row = first_row(v)
            if row and row.get("0") is not None:
                by_cue[row["0"]] = cue

        for k, v in tbl.items():
            if not k.isdigit():
                continue
            _, row = first_row(v)
            if not row:
                continue
            texts = [t for t in ((row.get(c) or "").strip() for c in TEXT_COLS)
                     if len(t) >= 2]
            if not texts:
                continue
            stats["lines"] += 1
            cue = by_cue.get(row.get("1"))
            if not cue:
                continue
            stats["cued"] += 1
            vid = suffix_voicer(cue, vox)
            if not vid:
                stats["no_voicer"] += 1
                continue
            stats["sexed"] += 1
            sex = vox[vid]
            for text in texts:
                votes[text][sex] += 1
                voicers[text][vid] += 1
                cues.setdefault(text, cue)

    out = {}
    for text, c in votes.items():
        m, f = c.get(1, 0), c.get(2, 0)
        gender = "mixed" if (m and f) else ("male" if m else "female")
        out[text] = {
            "gender": gender,
            "votes": {"male": m, "female": f},
            "example_cue": cues.get(text, ""),
            "voicers": [v for v, _ in voicers[text].most_common(4)],
        }
    return out, stats


def main():
    ap = argparse.ArgumentParser(description="ตารางเพศผู้พูดรายบรรทัดจากคิวเสียง")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    table, stats = build()
    per = collections.Counter(v["gender"] for v in table.values())
    print("แถวบทพูดที่มีข้อความ %s · จับคิวได้ %s · คิวชี้ voicer ที่ระบุเพศ %s"
          % tuple(format(stats[k], ",") for k in ("lines", "cued", "sexed")))
    print("ข้อความไม่ซ้ำที่ชี้ขาดได้ %s รายการ — ชาย %s · หญิง %s · ปนสองเพศ %s"
          % tuple(format(n, ",") for n in
                  (len(table), per["male"], per["female"], per["mixed"])))
    if not a.write:
        print("(ใส่ --write เพื่อเขียนไฟล์)")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(table, ensure_ascii=False, indent=1) + "\n")
    print("เขียน %s แล้ว" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
