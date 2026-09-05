#!/usr/bin/env python3
"""กวาดหา "อักษรละตินตกค้าง" ในคำแปลไทย — จับชื่อร้าน/สถานที่ที่ลืมทับศัพท์

ทำไมต้องมี: ผู้ตรวจ batch_120 เจอ `To Earth Angel` -> "ไปยัง Earth Angel" ทั้งที่ glossary §10
ล็อก "เอิร์ธแองเจิล" ไว้แล้ว — บั๊กแบบนี้รอดสายตาเพราะ merge_qc ไม่ได้ตรวจเรื่องคำล็อก
สคริปต์นี้ไล่ทุกคำแปล หาคำละตินที่ยังปนอยู่ แล้วหักคำที่ตั้งใจคง EN ออก เหลือไว้ให้คนดู

ใช้:
  python scripts/check_latin_leftovers.py                 # ดูของ master_th.json
  python scripts/check_latin_leftovers.py --done          # ดูของ translations/done/*.done.json
  python scripts/check_latin_leftovers.py --only 120      # เจาะ batch เดียว
"""
import argparse
import collections
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

# คำที่ทีมตัดสินให้ "คง EN" อย่างเป็นทางการ (glossary + คำตัดสิน lead) — ไม่ต้องรายงาน
KEEP_EN = {
    "chatter", "kamurogo", "quickstarter", "smz", "s-one", "mako mods", "esc",
    "ex action", "ex boost", "ex bond", "playstation", "steam", "kamuro of the dead",
    "konban wife", "kj art", "mflp", "staminan", "hug bomb", "toughness", "tauriner",
    "wette kitchen", "vf5", "virtua fighter", "dice & cube", "paradise vr", "edison",
    "quadra", "cab angus", "sega", "sony", "microsoft", "xbox", "windows", "amd", "nvidia",
    "fps", "hdr", "vsync", "hd", "sd", "pc", "ps4", "ps5", "id", "sp", "ex", "vr", "tv",
    "double quickstep", "quickstep strike", "quickstep cancel", "asahi", "justis",
    "puyo puyo", "battle royale", "addc", "ad-9", "stijl", "wife eye", "ufo catcher", "l'amant",

    # audit 21 ส.ค. 2026 (ผู้ตรวจ Latin-leftover ทั้งโปรเจกต์) — กองที่ 1 "คง EN ถูกต้อง"
    # ชื่อเกมอาร์เคด/แบรนด์จริงที่ล็อกใน glossary.md §"ชื่อเกมที่คง EN" + คง EN
    "out run", "fighting vipers", "fantasy zone", "space harrier", "championship motor raid",
    "motor raid", "ufo catcher", "koi-koi", "koi koi", "don quijote", "jungle boy",
    "super monkey ball", "dartslive", "dartslive card", "final showdown", "vf", "vf2", "fs",
    "kitty kat", "d&c", "kj", "kj art", "g.i", "g.i.", "yagami system", "ryu ga gotoku studio",
    # ตัวละครแบรนด์ SEGA ในตัวเกม (Fighting Vipers / Super Monkey Ball) — ชื่อคาแรกเตอร์จริง ไม่แปล
    "bahn", "tokio", "raxel", "sanman", "picky", "grace", "honey", "aiai", "gongon", "meemee",
    # ชื่อคอร์ส/โต๊ะในมินิเกม VR (Dice & Cube / Motor Raid) — คง EN ตามชื่อแบรนด์
    "simple road", "wide way", "northern canyon", "breakthrough cafe", "pipeline",
    "lullaby mahjong", "modern mahjong", "koro-nyan", "sugorokuhacks",
    # ตัวย่อ UI/สถิติ/กราฟิกทั่วเกม — คง EN ตามธรรมเนียมเมนู
    "lv", "hp", "dna", "qr", "gps", "dlc", "mk", "max", "reverse", "ui", "npc", "caution", "ad",
    "challenge course", "home run course",
    "dlss", "xess", "gpu", "xe-hpg", "fov", "anti-aliasing", "screen space ambient occlusion",
    "ai super resolution", "intel xe super sampling", "capture gallery", "options",
    "new game+", "vip", "iq", "ii", "iii", "iv", "ver", "bull",
    # ศัพท์ปาลูกดอก (glossary §"ศัพท์ดาร์ท") — Ton/Three in a Bed/White Horse ล็อกคง EN แล้ว
    "ton", "three in a bed", "white horse",
    # เพลง/สินค้า Haruka Sawamura + มุกเล่นคำที่ lead ยืนยันคง EN
    "so much more", "dreamline", "t-set", "japan dome", "amidst a dream", "nice dice",
    "open beta boyz",
    # เพิ่มเติม 21 ส.ค. 2026 — คำเดี่ยว/วลีคง EN ที่ยืนยันจาก precedent ใน master_th
    "ufo", "un", "deux", "trois", "a-z", "lullaby", "modern", "paradise", "yagami", "xl",
    "j-pop", "new game", "dice and cube", "yagami system", "kotd",
}
TAG_RE = re.compile(r"<[^>]*>|\$\{[^}]*\}|%[sd]|~[^~]*~|\[[a-z]{1,2}\]")
# Chatter (แอป SNS ในเกม) ใช้ @handle / #hashtag ปลอมของ NPC เป็นร้อย ๆ ชื่อ — พวกนี้
# "คง EN ถูกต้อง" เสมอ (ไม่มีใครแปล handle บนโซเชียล) แต่แจกแจงทีละชื่อใน KEEP_EN ไม่ไหว
# (ชื่อใหม่โผล่ทุก batch) จึง mask ทิ้งเชิงโครงสร้างแทน — audit 21 ส.ค. 2026
HANDLE_RE = re.compile(r"[@#][A-Za-z0-9_]+")
LATIN_RE = re.compile(r"[A-Za-z][A-Za-z'&.\- ]{1,30}[A-Za-z]|[A-Za-z]{2,}")
THAI_RE = re.compile(r"[฀-๿]")


def scan(pairs):
    hits = collections.Counter()
    where = collections.defaultdict(list)
    for k, v in pairs:
        if not THAI_RE.search(v):      # คำแปลที่คง EN ทั้งค่า = ตั้งใจ ไม่ใช่ตกค้าง
            continue
        clean = TAG_RE.sub(" ", v)
        clean = HANDLE_RE.sub(" ", clean)   # mask @handle / #hashtag ของ Chatter ก่อนสแกน
        for m in LATIN_RE.findall(clean):
            term = m.strip(" .-'&")
            if len(term) < 2:
                continue
            low = " ".join(term.lower().split())  # ยุบช่องว่างซ้ำจาก tag ที่ถูกตัดออก (เช่น <font_kind=...>and</font_kind>)
            if low in KEEP_EN:
                continue
            # เดิมใช้ `w in low` กับทุกคำ ทำให้คำสั้นอย่าง id/ex/sp/pc กลืนคำอื่นทั้งกอง
            # (เช่น "Rapid" มี "id" · "Extra" มี "ex") — ตอนนี้เทียบเป็นคำ ๆ แทน
            if any(w in low.split() for w in KEEP_EN):
                continue
            if any(len(w) >= 4 and (low.startswith(w) or w in low) for w in KEEP_EN):
                continue
            hits[term] += 1
            if len(where[term]) < 3:
                where[term].append(k[:60])
    return hits, where


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--done", action="store_true", help="ตรวจไฟล์ done แทน master_th")
    ap.add_argument("--only", help="เจาะ batch เดียว (ใช้กับ --done โดยอัตโนมัติ)")
    a = ap.parse_args()

    pairs = []
    if a.only or a.done:
        pat = "batch_%s.done.json" % a.only if a.only else "*.done.json"
        for p in sorted((paths.TRANSLATIONS / "done").glob(pat)):
            d = json.load(io.open(p, encoding="utf-8"))
            pairs += list(d["strings"].items())
    else:
        pairs = list(json.load(io.open(paths.MASTER_TH, encoding="utf-8")).items())

    hits, where = scan(pairs)
    print("ตรวจ %s คู่ · พบคำละตินตกค้าง %d แบบ" % (format(len(pairs), ","), len(hits)))
    for term, n in hits.most_common(60):
        print("  %-34s x%-4d  เช่น: %s" % (term, n, where[term][0]))
    if len(hits) > 60:
        print("  ... อีก %d แบบ" % (len(hits) - 60))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
