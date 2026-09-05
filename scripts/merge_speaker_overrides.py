#!/usr/bin/env python3
"""รวมผลพิสูจน์เพศผู้พูดจากทีม (`build/gender/talk_overrides_P*.json`) เข้าทะเบียนถาวร
`translations/speaker_gender_overrides.json` (รูปแบบเดียวกับ K3) แล้วรายงานสรุป

กติกา:
  * ทะเบียนเดิมชนะ ถ้าคีย์ซ้ำและมี `locked: true` (คนตัดสินไว้แล้ว) — ที่เหลือใช้ผลใหม่ทับ
  * `conf: low` ไม่รับเข้า (คงเป็น unknown ต่อ) — ต้องมีหลักฐานจริงเท่านั้น
  * ทุกแถวต้องมี why

ขั้นต่อไปหลังรวม: python scripts/make_talk_speaker.py --write → make_dialogue_gender.py --write

ใช้:
  python scripts/merge_speaker_overrides.py            # ดูสรุป
  python scripts/merge_speaker_overrides.py --write
"""
import argparse
import collections
import io
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                    # noqa: E402

SRC = sorted((paths.BUILD / "gender").glob("talk_overrides_P*.json"))
DST = paths.TRANSLATIONS / "speaker_gender_overrides.json"
NOTE = ("ทะเบียนเพศผู้พูดใน talk.bin ที่คนตัดสิน — ชนะข้อมูลในไฟล์เกม (ใช้โดย scripts/make_talk_speaker.py) · "
        "ค่าที่ใช้ได้: male / female / neutral (ชื่อเดียวใช้กับหลายคนต่างเพศ ต้องแปลกลาง) / unknown · "
        "ทุกแถวต้องมี why + แหล่งหลักฐาน · แถวที่ใส่ locked: true จะไม่ถูกผลทีมทับ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    dst = json.load(io.open(DST, encoding="utf-8")) if DST.exists() else {}
    dst.setdefault("_note", NOTE)
    stats = collections.Counter()
    for p in SRC:
        for name, v in json.load(io.open(p, encoding="utf-8")).items():
            g, conf, why = v.get("gender"), v.get("conf", "low"), v.get("why", "")
            if g not in ("male", "female", "neutral", "unknown"):
                stats["ค่าผิด"] += 1
                continue
            if conf == "low" and g != "unknown":
                stats["ทิ้ง (conf low)"] += 1
                g = "unknown"
            old = dst.get(name)
            if isinstance(old, dict) and old.get("locked"):
                stats["คงของเดิม (locked)"] += 1
                continue
            dst[name] = {"gender": g, "conf": conf, "why": why, "source": p.name}
            stats[g] += 1
    print("ไฟล์ต้นทาง %d · %s" % (len(SRC), " · ".join("%s %d" % kv for kv in stats.most_common())))
    if a.write:
        DST.write_text(json.dumps(dst, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("เขียน %s (%d ชื่อ)" % (DST, len(dst) - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
