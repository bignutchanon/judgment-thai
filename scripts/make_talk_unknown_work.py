#!/usr/bin/env python3
"""เตรียมแฟ้มงานให้ทีม subagent พิสูจน์เพศของ **ผู้พูดใน talk.bin ที่ยังเป็น unknown**

ทำไมต้องมี: `check_speaker_gender.py` ข้ามบรรทัดที่ผู้พูดเพศ `unknown` ทั้งหมด — นับจริง 5 ก.ย. 2026
มี 1,771 บรรทัดที่แปลระบุเพศไว้ (ครับ/ค่ะ/ผม/ฉัน) โดยไม่มีใครตรวจ กระจายใน 123 ชื่อผู้พูด
พิสูจน์เพศ "ต่อชื่อ" 123 ครั้งถูกกว่าตรวจ "ต่อบรรทัด" 1,771 ครั้งมาก

แฟ้มงานต่อผู้พูดหนึ่งคน:
  * ชื่อ EN / ชื่อ JA (ชื่อ JA มักมี 男/女 บอกเพศตรง ๆ — ใส่คำใบ้ให้)
  * ตาราง talk.bin ที่ปรากฏ + จำนวนบรรทัดที่แปลระบุเพศไว้
  * คำบรรยายจาก friends.json (ถ้าเป็นเพื่อน) — มี he/she ให้ใช้ได้เลย
  * ตัวอย่างบทพูดของเขาเอง (EN + TH ปัจจุบัน)
  * บรรทัดของ "คนอื่น" ที่อยู่ใกล้ ๆ ในตารางเดียวกันและมีคำบอกเพศ (he/she/sir/ma'am/lady/guy ...)

ผลลัพธ์ที่ agent ต้องส่ง: build/gender/talk_overrides_<part>.json (โครงอยู่ท้ายแฟ้มงาน)
→ lead รวมเป็น translations/speaker_gender_overrides.json แล้วรัน make_talk_speaker.py --write

ใช้:
  python scripts/make_talk_unknown_work.py            # เขียน build/gender/talk_unknown_P1.md .. P3.md
"""
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

DB = paths.DB_EN / "en"
FACTS = paths.EXTRACTED / "facts"
OUT = paths.BUILD / "gender"
PARTS = 3

GENDER_WORD = re.compile(
    r"\b(he|she|his|her|hers|him|himself|herself|sir|ma'am|madam|mr\.?|ms\.?|mrs\.?|miss|lady|ladies|"
    r"gentleman|guy|dude|man|woman|boy|girl|brother|sister|bro|sis|husband|wife|father|mother|dad|mom|"
    r"son|daughter|uncle|aunt|boyfriend|girlfriend|hostess|actress|waitress|old man|old lady|"
    r"young man|young woman|schoolgirl|schoolboy)\b", re.I)

# คำใบ้จากชื่อ JA ภายใน (ป้ายกำกับของทีมพัฒนา)
JA_HINT = [
    ("女", "หญิง (女)"), ("婦", "หญิง (婦)"), ("娘", "หญิง (娘)"), ("嬢", "หญิง (嬢)"), ("妻", "หญิง (妻)"),
    ("母", "หญิง (母)"), ("姉", "หญิง (姉)"), ("妹", "หญิง (妹)"), ("少女", "หญิง (少女)"),
    ("おばさん", "หญิง"), ("おばあ", "หญิง"), ("ママ", "หญิง (ママ)"), ("ホステス", "หญิง (ホステス)"),
    ("男", "ชาย (男)"), ("夫", "ชาย (夫)"), ("父", "ชาย (父)"), ("兄", "ชาย (兄)"), ("弟", "ชาย (弟)"),
    ("少年", "ชาย (少年)"), ("おじさん", "ชาย"), ("おじい", "ชาย"), ("親父", "ชาย (親父)"), ("マスター", "ชาย? (マスター)"),
    ("店長", "? (店長)"), ("店員", "? (店員)"), ("社長", "? (社長)"),
]


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def talk_rows():
    """{ตาราง: [(row_no, speaker_id, text)]} เรียงตามแถว"""
    talk = load(DB / "talk.bin.json")
    out = collections.OrderedDict()
    for k in talk:
        if not k.isdigit():
            continue
        table, val = list(talk[k].items())[0]
        sub = val.get("text") if isinstance(val, dict) else None
        if not isinstance(sub, dict):
            continue
        rows = []
        for kk in sub:
            if not kk.isdigit():
                continue
            row = list(sub[kk].values())[0]
            if isinstance(row, dict) and isinstance(row.get("3"), str) and row["3"].strip():
                rows.append((int(kk), row.get("2", 0), row["3"]))
        rows.sort()
        out.setdefault(table, []).extend(rows)
    return out


def talkers():
    t = load(DB / "talk_talker.bin.json")
    out = {}
    for k in t:
        if not k.isdigit():
            continue
        ja, row = list(t[k].items())[0]
        if isinstance(row, dict):
            out[int(k)] = (row.get("talk_talker") or "", ja or "")
    return out


def ja_hint(ja):
    hits = [h for key, h in JA_HINT if key in ja]
    return " · ".join(dict.fromkeys(hits)) if hits else ""


def cell(s, n=110):
    s = (s or "").replace("|", "¦").replace("\n", " / ").strip()
    return s[:n] + ("…" if len(s) > n else "")


SCHEMA = """
## รูปแบบผลลัพธ์ที่ต้องส่ง

เขียนที่ `build/gender/talk_overrides_%s.json` (ไฟล์เดียว · UTF-8 · ห้ามใส่ข้อความไทย) — **ทุกชื่อในแฟ้มนี้ต้องมี**:

```json
{
 "Yosuke": {"gender": "male", "conf": "high", "why": "judge_side_a01 row 8 'this is my sister, Tsukino' + friends.json 'his'"},
 "Bantam Owner": {"gender": "unknown", "conf": "low", "why": "no gendered reference found in given lines"}
}
```

* `gender` ใช้ได้เฉพาะ `male` · `female` · `unknown` · `neutral`
  (`neutral` = ชื่อนี้ถูกใช้กับหลายคนต่างเพศจริง ๆ เช่น "Staff" — ต้องแปลกลางเพศ)
* `why` เป็นอังกฤษ อ้างตาราง+เลขแถว หรือแหล่งที่ยกมา — **ห้ามตัดสินจากชื่อเฉย ๆ** (ชื่อญี่ปุ่นบอกเพศไม่ได้)
  คำใบ้จาก 男/女 ในชื่อ JA ใช้เป็นหลักฐานได้ (ป้ายกำกับของผู้พัฒนาเกม) แต่ให้ระบุว่าใช้
* ตัวละครที่ "ผู้พูดคนเดียวกันแต่เกมตั้งชื่อผู้พูดต่างกันตามฉาก" ให้ตอบตามตัวจริง
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    master = load(paths.MASTER_TH)
    ts = load(FACTS / "talk_speaker.json")
    tk = talkers()
    rows_by_table = talk_rows()
    friends = load(FACTS / "friends.json")

    # ผู้พูด unknown ที่มีบรรทัดแปลระบุเพศ
    stats = collections.defaultdict(lambda: {"n": 0, "tables": collections.Counter(), "ids": set()})
    for en, info in ts.items():
        th = master.get(en)
        if not th or info.get("gender") != "unknown":
            continue
        if not (male_markers(th) or female_markers(th)):
            continue
        s = stats[info.get("speaker") or "(no name)"]
        s["n"] += 1
        s["tables"][info.get("table")] += 1
        s["ids"].add(info.get("speaker_id"))
    names = sorted(stats, key=lambda k: -stats[k]["n"])
    print("ผู้พูด unknown ที่มีบรรทัดระบุเพศ: %d ชื่อ · %d บรรทัด" % (len(names), sum(s["n"] for s in stats.values())))

    # แบ่งงานเป็น PARTS ส่วน (สลับกันเพื่อให้ปริมาณใกล้เคียง)
    parts = [[] for _ in range(PARTS)]
    for i, n in enumerate(names):
        parts[i % PARTS].append(n)

    for pi, part in enumerate(parts, 1):
        tag = "P%d" % pi
        lines = ["# แฟ้มงานพิสูจน์เพศผู้พูด talk.bin — ส่วน %s (%d ชื่อ)" % (tag, len(part)), "",
                 "> สร้างด้วย `scripts/make_talk_unknown_work.py` — ห้ามแก้ไฟล์นี้",
                 "> แต่ละหัวข้อ = ผู้พูดหนึ่งชื่อ · `บทของเขาเอง` = ตัวอย่างบรรทัดที่เขาพูด (EN) ·",
                 "> `บรรทัดใกล้เคียง` = คนอื่นในตารางเดียวกันภายใน ±3 แถว ที่มีคำบอกเพศ (ตัวหนา) — อาจพูดถึงเขาหรือไม่ก็ได้ ต้องอ่านเอง", ""]
        for name in part:
            s = stats[name]
            ids = sorted(i for i in s["ids"] if isinstance(i, int))
            ja = " / ".join(dict.fromkeys(tk.get(i, ("", ""))[1] for i in ids if tk.get(i)))
            lines += ["## `%s`" % name, "",
                      "* ชื่อ JA ภายใน: `%s`%s" % (ja or "-", ("  → คำใบ้: **%s**" % ja_hint(ja)) if ja_hint(ja) else ""),
                      "* speaker_id: %s · บรรทัดที่แปลระบุเพศไว้: %d · ตาราง: %s" % (
                          ids, s["n"], ", ".join("%s(%d)" % kv for kv in s["tables"].most_common(6)))]
            # friends.json
            low = name.lower()
            fr = [f for f in friends if low and (low in f.get("name", "").lower()
                                                or f.get("name", "").lower().split()[-1:] == [low])]
            for f in fr[:2]:
                lines.append("* friends.json «%s»: %s" % (f.get("name"), cell(f.get("description"), 200)))
            # บทของเขาเอง + บรรทัดใกล้เคียง
            own, near = [], []
            for table in s["tables"]:
                rows = rows_by_table.get(table, [])
                idx = [i for i, (_, sid, _) in enumerate(rows) if sid in s["ids"]]
                for i in idx:
                    rno, _, text = rows[i]
                    # เอาแค่ EN — หลักฐานเพศอยู่ในภาษาอังกฤษ ใส่ TH ด้วยทำให้แฟ้มบวมเป็น 180KB (5 ก.ย. 2026)
                    if len(own) < 8:
                        own.append("%s r%d: %s" % (table, rno, cell(text, 110)))
                    for j in range(max(0, i - 3), min(len(rows), i + 4)):
                        if j == i or rows[j][1] in s["ids"]:
                            continue
                        t2 = rows[j][2]
                        if GENDER_WORD.search(t2) and len(near) < 10:
                            who = tk.get(rows[j][1], ("?", ""))[0] or "?"
                            near.append("%s r%d [%s]: %s" % (table, rows[j][0], who,
                                                            cell(GENDER_WORD.sub(lambda m: "**%s**" % m.group(0), t2), 140)))
            lines.append("* บทของเขาเอง:")
            lines += ["  - " + x for x in own] or ["  - (ไม่พบ)"]
            lines.append("* บรรทัดใกล้เคียงที่มีคำบอกเพศ:")
            lines += ["  - " + x for x in dict.fromkeys(near)] or ["  - (ไม่พบ)"]
            lines.append("")
        lines.append(SCHEMA % tag)
        p = OUT / ("talk_unknown_%s.md" % tag)
        p.write_text("\n".join(lines), encoding="utf-8")
        print("  %s: %d ชื่อ · %d บรรทัดระบุเพศ · %s (%d KB)" % (
            tag, len(part), sum(stats[n]["n"] for n in part), p.name, p.stat().st_size // 1024))
    (OUT / "talk_unknown_names.json").write_text(
        json.dumps({"P%d" % (i + 1): p for i, p in enumerate(parts)}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
