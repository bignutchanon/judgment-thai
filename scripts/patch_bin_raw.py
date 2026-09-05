#!/usr/bin/env python3
"""แทนที่ข้อความใน ARMP bin ระดับไบต์ โดยไม่ต้องผ่าน reARMP

ใช้กับ bin ที่ **reARMP export ไม่ผ่าน** (7 ไฟล์ในโปรเจกต์นี้ — ตัวที่มีข้อความจริงคือ
`ui_layer_text.bin`: MISSION · TIPS · ป้ายโต๊ะรูเล็ต) จึงแก้ด้วย `patch_bin_strings.py` ไม่ได้

หลักการ (ยืนยันกับไฟล์จริง 21 ส.ค. 2026):
  * ข้อความเก็บเป็นบล็อกสตริงลงท้าย NUL
  * มีตาราง pointer u32 little-endian ชี้ตำแหน่งสตริงแต่ละตัว
    (ตรวจแล้ว: MISSION @0xcc0 ถูกชี้จาก 0x11c0 · TIPS @0xcc8 จาก 0x11c4 · Even Odd @0x10c4 จาก 0x1230)
  * ไม่มีฟิลด์ "ขนาดไฟล์" ในเฮดเดอร์ (สแกนแล้วไม่พบ u32 ที่เท่ากับขนาดไฟล์)
    → **เติมสตริงใหม่ท้ายไฟล์แล้วชี้ pointer มาที่ตำแหน่งใหม่ได้** ไม่ต้องแก้ความยาวเดิม
    (คำแปลไทยยาวกว่าคำอังกฤษเสมอ เพราะ 1 เซลล์ = 2 ไบต์ UTF-8 จึงเขียนทับที่เดิมไม่ได้)

⚠ ยังไม่ผ่านการทดสอบบนจอจริง — ผู้ใช้ต้องเปิดเกมยืนยันก่อนถือว่าใช้ได้

ใช้:
    python scripts/patch_bin_raw.py --list ui_layer_text.bin     # ดูสตริง + pointer
    python scripts/patch_bin_raw.py                              # สร้าง build จาก EDITS
"""
import argparse
import io
import re
import struct
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402
from slot_alloc import SlotMap  # noqa: E402

STAGE = paths.BUILD / "text" / "db.judge.en" / "en"

# bin -> [(ข้อความ EN เดิมเป๊ะ, คำแปลไทย)]
EDITS = {
    "ui_layer_text.bin": [
        ("MISSION", "ภารกิจ"),
        ("TIPS", "เคล็ดลับ"),
        ("Even Odd", "คู่ คี่"),
    ],
}


def find_string(data, text):
    """คืนตำแหน่งของสตริง (ต้องลงท้าย NUL) — ต้องเจอตัวเดียวเท่านั้น"""
    needle = text.encode("utf-8") + b"\x00"
    hits = [m.start() for m in re.finditer(re.escape(needle), data)]
    if len(hits) != 1:
        raise SystemExit(f"หา {text!r} เจอ {len(hits)} จุด (ต้องเจอ 1 จุด) — ตรวจก่อนแก้")
    return hits[0]


def find_pointers(data, offset):
    """ตำแหน่งทุกจุดในไฟล์ที่เก็บค่า u32 = offset"""
    want = struct.pack("<I", offset)
    return [m.start() for m in re.finditer(re.escape(want), data) if m.start() % 4 == 0]


def list_strings(bin_name):
    data = (paths.EXTRACTED / "db_en" / "en" / bin_name).read_bytes()
    print(f"{bin_name} · {len(data)} ไบต์")
    for m in re.finditer(rb"[\x20-\x7e]{3,}\x00", data):
        s = m.group(0)[:-1].decode("ascii")
        off = m.start()
        ptrs = find_pointers(data, off)
        print("  %-24s @%-8s pointer: %s" % (s[:24], hex(off), [hex(p) for p in ptrs] or "ไม่พบ"))


def patch(bin_name, edits, slotmap):
    src = paths.EXTRACTED / "db_en" / "en" / bin_name
    data = bytearray(src.read_bytes())
    print(f"== {bin_name} ({len(data)} ไบต์)")
    for en, th in edits:
        off = find_string(bytes(data), en)
        ptrs = find_pointers(bytes(data), off)
        if not ptrs:
            raise SystemExit(f"ไม่พบ pointer ที่ชี้ {en!r} (@{hex(off)}) — ยังแก้ไฟล์นี้ไม่ได้")
        enc = slotmap.encode(th).encode("utf-8")
        while len(data) % 4:
            data.append(0)
        new_off = len(data)
        data += enc + b"\x00"
        for p in ptrs:
            struct.pack_into("<I", data, p, new_off)
        print("   %-10s -> %s  (%d เซลล์ / %d ไบต์) ย้ายจาก %s ไป %s · แก้ pointer %d จุด"
              % (en, th, len(slotmap.encode(th)), len(enc), hex(off), hex(new_off), len(ptrs)))
    STAGE.mkdir(parents=True, exist_ok=True)
    out = STAGE / bin_name
    out.write_bytes(bytes(data))
    # ตรวจซ้ำ: pointer ใหม่ต้องอ่านกลับได้เป็นข้อความเดิม
    blob = out.read_bytes()
    for en, th in edits:
        enc = slotmap.encode(th).encode("utf-8")
        assert enc + b"\x00" in blob, f"เขียน {th} ไม่สำเร็จ"
    print(f"   -> {out} ({out.stat().st_size} ไบต์)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", metavar="BIN", help="แสดงสตริง + pointer ของ bin แล้วจบ")
    a = ap.parse_args()
    if a.list:
        list_strings(a.list)
        return
    slotmap = SlotMap.load()
    for bin_name, edits in EDITS.items():
        patch(bin_name, edits, slotmap)
    print("เสร็จ — ยังไม่ deploy · ผู้ใช้ต้องเปิดเกมยืนยันว่าไม่แครชและข้อความขึ้นถูก")


if __name__ == "__main__":
    main()
