#!/usr/bin/env python3
"""รวมผลคัตซีนรอบสอง (build/gender/cinema_low_C*.json + cinema_low_R.json จากทีม register) เข้า translations/cinema_speakers/<ฉาก>.json

กติกา:
  * เขียนทับเฉพาะแถวที่เดิม conf=low หรือ gender=unknown — แถวที่รอบ 19 ตัดสินไว้แล้ว (high/med) ไม่แตะ
    เว้นแต่ผลใหม่ให้ conf high พร้อม why และใส่ `--override` (lead อ่านเหตุผลก่อน)
  * รับเฉพาะผลใหม่ที่ conf high/med — low ยังคงเป็นเดิม
  * ทุกแถวที่เขียนจะติด source = ชื่อไฟล์ผล เพื่อตามรอยได้

ใช้:  python scripts/merge_cinema_low.py            # รายงานอย่างเดียว
      python scripts/merge_cinema_low.py --write
      python scripts/merge_cinema_low.py --write --override   # ยอมให้ผล high ทับแถวที่ตัดสินแล้ว
ขั้นต่อไป: python scripts/make_dialogue_gender.py --write → fix_dialogue_gender.py
"""
import io
import json
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths

CINEMA = paths.TRANSLATIONS / "cinema_speakers"
SRC = paths.BUILD / "gender"
VALID_G = {"male", "female", "neutral", "unknown"}


def main():
    write = "--write" in sys.argv
    override = "--override" in sys.argv
    stat = Counter()
    rows_out = []
    for fp in sorted(SRC.glob("cinema_low_*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8-sig"))
        except Exception as e:  # noqa: BLE001
            print(f"{fp.name}: JSON พัง — {e}")
            stat["json พัง"] += 1
            continue
        for scene, rows in data.items():
            f = CINEMA / (scene + ".json")
            if not f.exists() or not isinstance(rows, dict):
                stat["ฉากไม่มี"] += 1
                continue
            cs = json.loads(f.read_text(encoding="utf-8"))
            changed = False
            for rk, r in rows.items():
                if not isinstance(r, dict):
                    continue
                cur = cs.setdefault("rows", {}).get(rk)
                g = str(r.get("gender", "unknown")).lower()
                conf = str(r.get("conf", "low")).lower()
                if g not in VALID_G:
                    stat["เพศไม่รู้จัก"] += 1
                    continue
                if cur is None:
                    stat["แถวไม่มีในฉาก"] += 1
                    continue
                pending = cur.get("conf") == "low" or cur.get("gender") == "unknown"
                if not pending and not (override and conf == "high"):
                    stat["ข้าม: ตัดสินแล้ว"] += 1
                    continue
                if conf not in ("high", "med"):
                    stat["ข้าม: conf low"] += 1
                    continue
                rows_out.append((scene, rk, cur.get("speaker"), cur.get("gender"), r.get("speaker"), g, conf, r.get("why", "")))
                cs["rows"][rk] = {"speaker": r.get("speaker", "?"), "gender": g, "conf": conf,
                                  "why": r.get("why", ""), "source": fp.name}
                changed = True
                stat["รับ " + g] += 1
            if changed and write:
                f.write_text(json.dumps(cs, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print(("เขียนแล้ว" if write else "ตัวอย่าง (ยังไม่เขียน)") + " · " + " · ".join(f"{k} {v}" for k, v in stat.most_common()))
    for scene, rk, os_, og, ns, ng, conf, why in rows_out[:40]:
        print(f"  {scene} r{rk}: {os_}/{og} → {ns}/{ng} ({conf}) — {why[:70]}")
    if len(rows_out) > 40:
        print(f"  … อีก {len(rows_out) - 40} แถว")


if __name__ == "__main__":
    main()
