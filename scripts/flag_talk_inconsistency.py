"""For each (batch, speaker) with >=2 lines, check if the Thai translation
mixes male-coded (ครับ/ผม-as-self) and female-coded (ค่ะ/คะ/ดิฉัน) register
within the same speaker in the same batch, without an established mid-scene
switch. This catches misattributed dialogue turns that a plain gender-field
conflict check would miss (e.g. speaker's gender itself is 'unknown' but
their own lines contradict each other).
"""
import sys, json, os, re
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\Projects\judgment-thai"
speak = json.load(open(os.path.join(ROOT, "extracted/facts/talk_speaker.json"), encoding="utf-8"))

for n in range(1, 6):
    tag = f"TALK_{n:03d}"
    wl = json.load(open(os.path.join(ROOT, f"translations/worklist/batch_{tag}.json"), encoding="utf-8"))
    done = json.load(open(os.path.join(ROOT, f"translations/done/batch_{tag}.done.json"), encoding="utf-8"))
    order = list(wl["strings"].keys())
    strings = done["strings"]

    by_speaker = defaultdict(list)
    for en in order:
        info = speak.get(en)
        if not info:
            continue
        speaker = info.get("speaker", "")
        if not speaker or speaker == "Yagami":
            continue
        th = strings.get(en, "")
        if not th:
            continue
        has_krap = "ครับ" in th
        has_phom = bool(re.search(r"(?<![ก-๙])ผม(?![ก-๙])", th))
        has_ka = bool(re.search(r"(ค่ะ|คะ)", th))
        has_dichan = "ดิฉัน" in th
        male_sig = has_krap or has_phom
        female_sig = has_ka or has_dichan
        if male_sig or female_sig:
            by_speaker[(info.get("table",""), speaker)].append((en, th, male_sig, female_sig))

    for (table, speaker), lines in by_speaker.items():
        has_male = any(m for _,_,m,f in lines)
        has_female = any(f for _,_,m,f in lines)
        if has_male and has_female and len(lines) >= 2:
            print(f"[{tag}] table={table} speaker={speaker} -- MIXED REGISTER ({len(lines)} gendered lines)")
            for en, th, m, f in lines:
                tag2 = "M" if m and not f else ("F" if f and not m else "MF")
                print(f"   [{tag2}] EN: {en[:70]}")
                print(f"        TH: {th[:90]}")
            print()
