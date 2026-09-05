"""Heuristic scan: flag lines in TALK_001..005 where the Thai translation's
gendered pronoun/ending contradicts the confirmed speaker's gender from
talk_speaker.json, or where Yagami (must always be T1 "phom") uses forbidden
T3 tokens. Output candidates only, for manual review (saves reading all 1250
lines by hand).
"""
import sys, json, os, re

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\Projects\judgment-thai"
speak = json.load(open(os.path.join(ROOT, "extracted/facts/talk_speaker.json"), encoding="utf-8"))

FEMALE_MARKERS = ["ดิฉัน", "ค่ะ", "คะ", "นะคะ", "เจ้าค่ะ"]
MALE_MARKERS = ["ครับ", "กระผม", "ผม"]  # "ผม" alone is weak (could be hair/body) -- handled carefully
T3_TOKENS = ["กู", "มึง", "เว้ย", "โว้ย"]

def has_word(text, word):
    return word in text

results = []

for n in range(1, 6):
    tag = f"TALK_{n:03d}"
    wl = json.load(open(os.path.join(ROOT, f"translations/worklist/batch_{tag}.json"), encoding="utf-8"))
    done = json.load(open(os.path.join(ROOT, f"translations/done/batch_{tag}.done.json"), encoding="utf-8"))
    order = list(wl["strings"].keys())
    strings = done["strings"]

    for en in order:
        info = speak.get(en)
        if not info:
            continue
        speaker = info.get("speaker", "")
        gender = info.get("gender", "unknown")
        table = info.get("table", "")
        th = strings.get(en, "")
        if not th:
            continue

        flags = []

        # Yagami must never use T3
        if speaker == "Yagami":
            for tok in T3_TOKENS:
                if has_word(th, tok):
                    flags.append(f"YAGAMI_T3:{tok}")

        has_krap = "ครับ" in th
        has_phom = bool(re.search(r"(?<![ก-๙])ผม(?![ก-๙])", th))
        has_ka = bool(re.search(r"(ค่ะ|คะ)", th))
        has_dichan = "ดิฉัน" in th
        gendered_any = has_krap or has_phom or has_ka or has_dichan

        # Female speaker but male-only markers present
        if gender == "female":
            if has_krap:
                flags.append("FEMALE_SPEAKER_HAS_KRAP")
            if has_phom:
                flags.append("FEMALE_SPEAKER_HAS_PHOM")
        if gender == "male":
            if has_dichan:
                flags.append("MALE_SPEAKER_HAS_DICHAN")
            if has_ka:
                flags.append("MALE_SPEAKER_HAS_KA")
        if gender == "unknown" and speaker not in ("", None):
            if gendered_any:
                flags.append("UNKNOWN_GENDER_LEAK")

        if flags:
            results.append({
                "batch": tag, "table": table, "speaker": speaker,
                "gender": gender, "en": en, "th": th, "flags": flags,
            })

print(f"total flagged: {len(results)}\n")
for r in results:
    print(f"[{r['batch']}] table={r['table']} speaker={r['speaker']} gender={r['gender']} flags={r['flags']}")
    print(f"  EN: {r['en']}")
    print(f"  TH: {r['th']}")
    print()
