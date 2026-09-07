#!/usr/bin/env python3
"""เตรียมแฟ้มงานรอบสอง: ฉากคัตซีน (`auth.bin`) ที่ยังมีแถว conf=low / gender=unknown ใน translations/cinema_speakers/

รอบ 19 ทีมระบุผู้พูดครบ 102 ฉากแล้ว แต่ 255 แถวใน 52 ฉากยังเป็น low/unknown → `make_dialogue_gender` นับเป็นไม่รู้เพศ
และคำแปลของแถวพวกนั้นต้องกลางเพศ — รอบนี้ให้ทีมอ่านฉากซ้ำโดยเห็น "ทุกแถว" ของฉาก (แถวที่ตัดสินแล้วช่วยเป็นบริบท)
แล้วตัดสินเฉพาะแถวที่ยังค้าง — ใช้ story_chNN.md + characters_gender.md ที่ make_cinema_work.py สร้างไว้เป็นบริบทเนื้อเรื่อง

เอาต์พุต: build/gender/cinema_low_C1.md, C2.md … (แฟ้มงาน) — agent เขียนผลเป็น build/gender/cinema_low_C1.json …
→ lead รวมด้วย scripts/merge_cinema_low.py (เขียนเฉพาะแถวที่เดิม low/unknown และผลใหม่ conf high/med)

ใช้:  python scripts/make_cinema_low_work.py
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
from make_blind_chunks import load, nested_tables, rows_in_order, CINEMA

OUT = paths.BUILD / "gender"
PARTS = 2


def main():
    master = load(paths.MASTER_TH)
    auth = load(paths.DB_EN / "en" / "auth.bin.json")
    scenes = OrderedDict()
    for k, v in auth.items():
        if not k.isdigit():
            continue
        for name, sub in v.items():
            f = CINEMA / (name + ".json")
            if not f.exists() or not isinstance(sub, dict):
                continue
            table = nested_tables(sub)
            if table is None:
                continue
            cs = load(f)
            pending = {rk for rk, r in cs.get("rows", {}).items() if r.get("conf") == "low" or r.get("gender") == "unknown"}
            if not pending:
                continue
            rows = []
            for rk, rn, row in rows_in_order(table, sort_by_time=True):
                a, b = row.get("4"), row.get("5")
                if not (isinstance(a, str) and a.strip()) and not (isinstance(b, str) and b.strip()):
                    continue
                cur = cs["rows"].get(rk, {})
                rows.append((rk, a or "", b or "", master.get(a or "", ""), master.get(b or "", ""), cur, rk in pending))
            scenes[name] = rows
    # แบ่งเป็นส่วนเท่า ๆ กันตามจำนวนแถวค้าง
    order = sorted(scenes.items(), key=lambda kv: kv[0])
    parts = [[] for _ in range(PARTS)]
    loads = [0] * PARTS
    for name, rows in order:
        i = loads.index(min(loads))
        parts[i].append((name, rows))
        loads[i] += sum(1 for r in rows if r[6])
    OUT.mkdir(parents=True, exist_ok=True)
    esc = lambda s: s.replace("\n", "\\n")
    for pi, part in enumerate(parts, 1):
        md = [f"# แฟ้มงานคัตซีนรอบสอง — ส่วน C{pi} ({len(part)} ฉาก · แถวค้าง {sum(1 for _, rows in part for r in rows if r[6])})", "",
              "> สร้างด้วย `scripts/make_cinema_low_work.py` — ห้ามแก้ไฟล์นี้ · แถวที่มี **← ต้องตัดสิน** คือแถวที่ยัง conf=low/unknown",
              "> แถวอื่นตัดสินไว้แล้วรอบ 19 (ใช้เป็นบริบท ไม่ต้องส่งซ้ำ เว้นแต่พบว่าผิดชัดเจน ให้ส่งพร้อมเหตุผล)",
              "> คอลัมน์ A = ซับชุดแรก (คอลัมน์ 4) · B = ซับชุดสอง (คอลัมน์ 5) ของบรรทัดเดียวกัน · TH = คำแปลปัจจุบัน",
              "> บริบทเนื้อเรื่องรายบท: `build/gender/story_chNN.md` (NN = เลขบทจากชื่อฉาก aNN) · ทะเบียนเพศตัวละคร: `build/gender/characters_gender.md`", ""]
        for name, rows in part:
            ch = re.match(r"a(\d\d)", name)
            md.append(f"## ฉาก `{name}` (บท {int(ch.group(1)) if ch else '?'} · แถว {len(rows)} · ค้าง {sum(1 for r in rows if r[6])})")
            md.append("")
            for rk, a, b, tha, thb, cur, pend in rows:
                mark = " **← ต้องตัดสิน**" if pend else ""
                who = f"{cur.get('speaker', '?')} / {cur.get('gender', '?')} / {cur.get('conf', '?')}"
                md.append(f"- r{rk} [{who}]{mark}")
                if a:
                    md.append(f"  - A: {esc(a)}  ⇒ {esc(tha)}")
                if b and b != a:
                    md.append(f"  - B: {esc(b)}  ⇒ {esc(thb)}")
            md.append("")
        md += ["## รูปแบบผลลัพธ์ (เขียนไฟล์ `build/gender/cinema_low_C%d.json`)" % pi, "",
               "```json", '{"a01_010": {"7": {"speaker": "Saori", "gender": "female", "conf": "high", "why": "หลักฐานสั้น ๆ อ้างแถว/EN"}}}', "```",
               "- ส่งเฉพาะแถว **← ต้องตัดสิน** (และแถวเดิมที่พบว่าผิดชัดเจน) · conf: high = หลักฐานตรง (ชื่อ/he-she/บทบาท) · med = อนุมานจากลำดับบทสนทนา · low = เดา (จะไม่ถูกใช้)",
               "- ผู้พูดหลายคนพร้อมกัน/ฝูงชน/เสียงบรรยาย → speaker \"Narration\" หรือ \"Crowd\" gender \"neutral\"", ""]
        (OUT / f"cinema_low_C{pi}.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
        print(f"C{pi}: {len(part)} ฉาก · แถวค้าง {loads[pi - 1]} · cinema_low_C{pi}.md")
    print(f"ฉากที่มีแถวค้าง {len(scenes)} · แถวค้างรวม {sum(loads)}")


if __name__ == "__main__":
    main()
