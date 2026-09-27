#!/usr/bin/env python3
r"""แพ็กไฟล์แจก — ตัวติดตั้งอัตโนมัติที่ใช้วิธีเดียวกับที่ทดสอบผ่านแล้วในเครื่องเรา

**ไม่ใช้วิธีของ MOD2SUB** (วางฟอนต์ไว้ในโฟลเดอร์ mods แล้วหวังว่า Parless จะโหลดให้)
เพราะวิธีนั้นเรายังไม่เคยพิสูจน์เอง และกติกาเหล็กข้อ 5 ของโปรเจกต์ระบุว่าเกมโหลดฟอนต์
ตั้งแต่ก่อน Parless จะ hook ทัน สิ่งที่เรายืนยันบนจอจริงแล้วคือ **ฟอนต์เขียนทับไฟล์เกมตรง ๆ**
(สำรองเป็น .orig ก่อนเสมอ) ส่วนข้อความไปทางโฟลเดอร์ mods

โครงที่แพ็ก:

    JudgmentThai-th-vX/
      install.bat / install.ps1        ติดตั้ง (หาโฟลเดอร์เกมจาก Steam ให้เอง)
      uninstall.bat / uninstall.ps1    ถอน — คืนฟอนต์จาก .orig + ลบโฟลเดอร์ม็อด
      README.txt
      files/
        font/*.dds                     -> data/font.judge/en/ (สำรอง .orig ก่อนทับ)
        JudgmentThai/db.judge.en/...   -> mods/JudgmentThai/
        loader/                        -> runtime/media/ (ใส่ให้เฉพาะที่ยังไม่มี)

ใช้:  python scripts/package_release.py [--version 1.0] [--no-loader]
"""
import argparse
import io
import json
import os
import shutil
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

RELEASE = paths.PROJECT / "release"
PACKAGING = paths.PROJECT / "packaging"
MOD_NAME = "JudgmentThai"
LOADER = ["ShinRyuModManager.exe", "version.dll", "YakuzaParless.asi"]
FONTS = ["meta_ot_cond_book.dds", "meta_ot_cond_book_italic.dds"]
SCRIPTS = ["install.bat", "install.ps1", "uninstall.bat", "uninstall.ps1"]

META = """Name: JudgmentThai
Author: JETH
Version: {ver}
Description: "Judgment ภาษาไทย — แปลจากภาษาอังกฤษของเกม (ข้อความ {n_bin} ไฟล์ + ฟอนต์ไทย)"
"""

README = r"""Judgment — ม็อดแปลไทย (JETH) v{ver}
=====================================

แปลข้อความในเกมเป็นไทย {n_str} ประโยค พร้อมฟอนต์ไทยที่วาดลงฟอนต์ของเกมเอง
รองรับเฉพาะ Judgment เวอร์ชัน Steam (PC) เท่านั้น

สิ่งที่คงเป็นภาษาอังกฤษโดยตั้งใจ: license / EULA / เครดิต / กล่องข้อความของ Windows
(เช่นตอนกด Alt+F4 — ตัวนั้น Windows เป็นคนวาด ไม่ใช่เกม)


ติดตั้ง
--------
ดับเบิลคลิก  install.bat  — ตัวติดตั้งจะหาโฟลเดอร์เกมจาก Steam ให้เอง
(ถ้าหาไม่เจอ จะให้วางพาธของโฟลเดอร์ที่มีไฟล์ Judgment.exe เอง)

จากนั้นเข้าเกมแล้วตั้งภาษาข้อความเป็น English — ม็อดแทนที่ข้อความชุดอังกฤษ

ตัวติดตั้งทำ 3 อย่าง:
 1. สำรองฟอนต์เดิมของเกมเป็นไฟล์ .orig (ครั้งแรกครั้งเดียว) แล้วเขียนทับด้วยฟอนต์ไทย
    ที่ data\font.judge\en\meta_ot_cond_book.dds และ meta_ot_cond_book_italic.dds
 2. ก๊อปข้อความไทยไปที่ mods\{mod}\
 3. ใส่ตัวโหลดม็อด (Shin Ryu Mod Manager / Parless) ให้ถ้ายังไม่มี แล้วสร้างไฟล์ MLO


ถอนการติดตั้ง
--------------
ดับเบิลคลิก  uninstall.bat  — คืนฟอนต์เดิมจากไฟล์ .orig และลบโฟลเดอร์ม็อดออก
ไฟล์ตัวโหลดม็อดไม่ถูกลบ เพราะม็อดตัวอื่นอาจใช้อยู่


ข้อควรทราบ
-----------
* ฟอนต์เขียนทับไฟล์ในเกมจริง เพราะเกมโหลดฟอนต์ตั้งแต่ก่อนตัวโหลดม็อดจะทำงานทัน
  วางไว้ในโฟลเดอร์ mods แล้วไม่ติด — ตัวติดตั้งจึงสำรอง .orig ไว้ให้เสมอ
* ถ้าสั่ง "ตรวจสอบความสมบูรณ์ของไฟล์เกม" ใน Steam ฟอนต์จะถูกเขียนกลับเป็นของเดิม
  ให้รัน install.bat ซ้ำอีกครั้ง
* เกมอัปเดตแล้วให้รัน install.bat ซ้ำ เพื่อสร้างไฟล์ MLO ใหม่
* ยังไม่ผ่านการเล่นจบเกม — เจอข้อความเพี้ยนหรือเกมค้าง ช่วยแจ้งพร้อมภาพหน้าจอ


เครดิต
-------
* ตัวโหลดม็อด: Shin Ryu Mod Manager + YakuzaParless (SutandoTsukai181 และผู้ร่วมพัฒนา)
* ฟอนต์ไทย: {font} (SIL Open Font License)
* ฟอนต์บนป้ายภาพ (การ์ดชื่อบท/ตัวละคร · ป้ายชื่อศัตรู · ป้ายสถานที่): Taviraj (SIL Open Font License)
"""


def main():
    ap = argparse.ArgumentParser(description="แพ็กไฟล์แจก")
    ap.add_argument("--version", default="1.0")
    ap.add_argument("--no-zip", action="store_true")
    ap.add_argument("--no-loader", action="store_true",
                    help="ไม่ใส่ไฟล์ตัวโหลดม็อดไปด้วย (ผู้ใช้ต้องติดตั้งเอง)")
    a = ap.parse_args()

    stage_text = paths.BUILD / "text" / "db.judge.en"
    stage_font = paths.BUILD / "font"
    assert stage_text.exists(), "ยังไม่ได้บิลด์ข้อความ — รัน scripts/build_text.py"
    for f in FONTS:
        assert (stage_font / f).exists(), "ยังไม่ได้บิลด์ฟอนต์: %s" % f

    out = RELEASE / ("%s-th-v%s" % (MOD_NAME, a.version))
    if out.exists():
        shutil.rmtree(out)
    files = out / "files"
    mod = files / MOD_NAME
    (files / "font").mkdir(parents=True)
    (files / "loader").mkdir()
    shutil.copytree(stage_text, mod / "db.judge.en")
    # ตารางฟอนต์สไปรต์ UI ที่ล้าง donor (จอโดรน/คาสิโน — scripts/strip_ui_sprite_slots.py --write)
    stage_ui = paths.BUILD / "ui" / "ui.judge.en"
    if stage_ui.exists():
        shutil.copytree(stage_ui, mod / "ui.judge.en")
        print("ใส่ ui.judge.en %d ไฟล์" % sum(1 for _ in (mod / "ui.judge.en").rglob("*.bin")))
    else:
        print("!! ไม่มี build/ui/ui.judge.en — จอโดรนจะยังเพี้ยน (รัน strip_ui_sprite_slots.py --write)")
    for f in FONTS:
        shutil.copy2(stage_font / f, files / "font" / f)
    if not a.no_loader:
        for f in LOADER:
            shutil.copy2(paths.TOOLS / "SRMM-4.8.4" / f, files / "loader" / f)
    for f in SCRIPTS:
        shutil.copy2(PACKAGING / f, out / f)

    n_bin = sum(1 for _ in (mod / "db.judge.en").rglob("*.bin"))
    n_str = len(json.load(io.open(paths.MASTER_TH, encoding="utf-8")))
    io.open(mod / "mod-meta.yaml", "w", encoding="utf-8", newline="\n").write(
        META.format(ver=a.version, n_bin=n_bin))
    io.open(out / "README.txt", "w", encoding="utf-8-sig", newline="\r\n").write(
        README.format(ver=a.version, n_str="{:,}".format(n_str), mod=MOD_NAME,
                      font=paths.THAI_FONT_NAME))

    total = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
    print("แพ็ก %s · %d bin · %.1f MB" % (out, n_bin, total / 1e6))

    if not a.no_zip:
        zpath = RELEASE / ("%s-th-v%s.zip" % (MOD_NAME, a.version))
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for f in sorted(out.rglob("*")):
                if f.is_file():
                    z.write(f, str(f.relative_to(out)).replace("\\", "/"))
        print("เขียน %s (%.1f MB)" % (zpath, zpath.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
