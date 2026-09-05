#!/usr/bin/env python3
"""ค่าคงที่ path กลางของโปรเจกต์ JETH — Judgment (แปลไทย)
ทุกสคริปต์ import จากที่นี่ — แก้ path ที่เดียว ได้ผลทุกตัว

override ได้ด้วย environment variable:
  JUDGE_GAME = โฟลเดอร์เกม (⏳ เกมยังไม่ติดตั้ง — ตั้ง env นี้เมื่อลงแล้ว)

กติกา:
  - GAME_DATA (runtime/media/data) ห้ามแก้/ลบ/ทับไฟล์เดิมเด็ดขาด — mod วางที่ MODS_DIR เท่านั้น
    ยกเว้นฟอนต์: drop-in ทับ font par โดย backup .orig ก่อนเสมอ (กติกาเหล็กข้อ 5)
  - translations/master_th.json = คำแปลรวม (source of truth)

หมายเหตุ: port มาจาก yakuza-kiwami-3 (k3_paths.py) 14 ส.ค. 2026
ค่าที่ยังไม่ยืนยันกับไฟล์เกมจริงถูกทำเครื่องหมาย ⏳ — ต้อง verify ตอนเกมติดตั้งแล้ว
"""
import os
from pathlib import Path

# ---- โปรเจกต์ ----
PROJECT = Path(__file__).resolve().parent.parent   # D:/Projects/judgment-thai

SCRIPTS      = PROJECT / "scripts"
TOOLS        = PROJECT / "tools"
DOCS         = PROJECT / "docs"
EXTRACTED    = PROJECT / "extracted"
DB_EN        = EXTRACTED / "db_en"                 # ARMP .bin อังกฤษ (ต้นฉบับ อย่าแก้)
TRANSLATIONS = PROJECT / "translations"
BUILD        = PROJECT / "build"
FONT_DIR     = PROJECT / "font"

# ---- คำแปล ----
MASTER_TH = TRANSLATIONS / "master_th.json"        # source of truth
WORKLIST  = TRANSLATIONS / "worklist"
DONE      = TRANSLATIONS / "done"
REVIEW    = TRANSLATIONS / "review"

# ---- เกม (Judgment PC 2022, Dragon Engine — verify แล้ว 14 ส.ค. 2026) ----
GAME      = Path(os.environ.get("JUDGE_GAME",
                 r"E:/SteamLibrary/steamapps/common/Judgment"))
GAME_EXE  = GAME / "runtime/media/Judgment.exe"    # ยืนยันแล้ว
GAME_DATA = GAME / "runtime/media/data"            # !! ห้ามเขียน/ลบไฟล์ในนี้ !!

CODENAME    = "judge"                              # ยืนยันแล้วจากชื่อไฟล์จริง
DB_EN_PAR   = GAME_DATA / "db.judge.en.par"        # ยืนยันแล้ว — db par เดียวในเกม (carrier=EN)
# หมายเหตุ: ไม่มี db.judge.ja.par — ภาษาอื่นน่าจะอยู่ในไฟล์เดียวกันหรือ ui.judge.en.par
UI_EN_PAR   = GAME_DATA / "ui.judge.en.par"        # มีจริง (293MB) — เผื่อ texture text

# ฟอนต์: ไม่ใช่ par! เป็นโฟลเดอร์ loose ในเกมเลย (แบบ Y6-era layout)
FONT_GAME_DIR = GAME_DATA / "font.judge" / "en"    # gothic/symbol/tbgm_0p_ja (.bin+.dds)
# format = FONT! (Y6) — ใช้ y6_font_tool.py เท่านั้น · font_tool.py (K2R) parse ไม่ได้
# drop-in: แทนไฟล์ใน FONT_GAME_DIR ตรงๆ โดย backup .orig ก่อนเสมอ (กติกาเหล็กข้อ 5)

MOD_NAME  = "JudgmentThai"
MODS_ROOT = GAME / "runtime/media/mods"
MODS_DIR  = MODS_ROOT / MOD_NAME
# SRMM/Parless รองรับ Judgment อย่างเป็นทางการ (Steam) — db วาง loose ใน MODS_DIR ได้
# (ยังไม่ได้ติดตั้ง SRMM ในเกม — เช็คก่อน deploy db แบบ loose)

# ---- ฟอนต์ ----
# main text font = tbgm_0p_ja (7,093 glyphs / capacity 9,250 / ว่าง 2,157 slot ·
# donor Cyrillic 66/83 ขาดชุดเดียวกับ Y6 · atlas BC4U 4096x4096)
FONT_BASENAME = "tbgm_0p_ja"
FONT_SRC_BIN  = EXTRACTED / "font" / (FONT_BASENAME + ".bin")
FONT_SRC_DDS  = EXTRACTED / "font" / (FONT_BASENAME + ".dds")
SARABUN_TTF   = FONT_DIR / "Sarabun-Regular.ttf"

# ---- เครื่องมือ ----
REARMP  = TOOLS / "reARMP_fixed.py"
PARTOOL = TOOLS / "ParTool.exe"

if __name__ == "__main__":
    import io, sys
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    names = ["PROJECT", "DB_EN", "MASTER_TH", "WORKLIST", "DONE",
             "GAME", "GAME_EXE", "GAME_DATA", "DB_EN_PAR", "FONT_PAR",
             "MODS_DIR", "SARABUN_TTF", "REARMP", "PARTOOL"]
    print(f"MOD_NAME = {MOD_NAME}")
    for n in names:
        v = globals()[n]
        if v is None:
            print(f"--  {n:14s} (ยังไม่กำหนด — รอ survey)")
            continue
        p = Path(v)
        print(f'{"OK" if p.exists() else "--"}  {n:14s} {p}')
