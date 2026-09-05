"""Apply confirmed speaker-audit fixes to batch_TALK_004 and batch_TALK_005
done files. Each fix is verified against extracted/facts/talk_speaker.json
(speaker=Yagami, gender=male) plus surrounding dialogue context -- see
translations/review/TALK_speaker_audit.md for the full reasoning.
"""
import sys, json, os

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\Projects\judgment-thai"

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ---- TALK_004 ----
p4 = os.path.join(ROOT, "translations/done/batch_TALK_004.done.json")
d4 = load(p4)
s4 = d4["strings"]

fixes4 = {
    "I'm sorry to put it like this, but...":
        ("ขอโทษที่ต้องพูดแบบนี้นะคะ แต่...",
         "ขอโทษที่ต้องพูดแบบนี้นะครับ แต่..."),
    "You barely moved into town, right? I doubt you have the\nbudget to hire a private investigator.":
        ("คุณเพิ่งย้ายเข้ามาในเมืองใช่ไหมคะ ฉันสงสัยว่าคุณคง\nไม่มีงบพอจ้างนักสืบเอกชนหรอก",
         "คุณเพิ่งย้ายเข้ามาในเมืองใช่ไหมครับ ผมสงสัยว่าคุณคง\nไม่มีงบพอจ้างนักสืบเอกชนหรอก"),
    "I'm sorry I let this happen. If only I'd have warned you...":
        ("ขอโทษนะคะที่ปล่อยให้เรื่องแบบนี้เกิดขึ้น ถ้าฉันเตือนคุณไว้ก่อน...",
         "ขอโทษนะครับที่ปล่อยให้เรื่องแบบนี้เกิดขึ้น ถ้าผมเตือนคุณไว้ก่อน..."),
}

for en, (old, new) in fixes4.items():
    assert en in s4, f"MISSING KEY in TALK_004: {en!r}"
    assert s4[en] == old, f"UNEXPECTED CURRENT VALUE in TALK_004 for {en!r}: {s4[en]!r}"
    s4[en] = new

save(p4, d4)
print(f"TALK_004: applied {len(fixes4)} fixes")

# ---- TALK_005 ----
p5 = os.path.join(ROOT, "translations/done/batch_TALK_005.done.json")
d5 = load(p5)
s5 = d5["strings"]

fixes5 = {
    "What do you mean!?":
        ("มึงหมายความว่าอะไร!?", "นายหมายความว่าอะไร!?"),
}

for en, (old, new) in fixes5.items():
    assert en in s5, f"MISSING KEY in TALK_005: {en!r}"
    assert s5[en] == old, f"UNEXPECTED CURRENT VALUE in TALK_005 for {en!r}: {s5[en]!r}"
    s5[en] = new

save(p5, d5)
print(f"TALK_005: applied {len(fixes5)} fixes")
