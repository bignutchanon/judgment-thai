#!/usr/bin/env python3
"""ตรวจว่าไฟล์ใน `build/text/db.judge.en/en/` ยัง "เหมือนต้นฉบับ SEGA" จริง — พอร์ตจาก Gaiden 15 ก.ย. 2026

ตัวเขียนไฟล์แบบ patch ในที่ (`patch_text_inplace.py`) ต้องแตะแค่สองอย่าง:
  1) ตัวเลขใน **text offset table** ของแต่ละตาราง (ชี้ไปสตริงไทยที่ต่อไว้ท้ายไฟล์)
  2) ไบต์ที่ **ต่อท้ายไฟล์เดิม** (pool ใหม่)
ทุกไบต์อื่นในช่วงความยาวไฟล์ต้นฉบับต้องเท่าเดิมเป๊ะ — ถ้าไม่เท่าแปลว่าไฟล์ถูกประกอบใหม่ (reARMP rebuild)
หรือ patch พลาด ซึ่งเป็นเคสที่ Y8/Gaiden พิสูจน์แล้วว่าทำเกมค้าง/เด้งที่จอสอนปุ่มของมินิเกม

ข้อยกเว้นที่รู้อยู่แล้ว (รายงานแยก ไม่นับตก): `font.bin` — patch ในที่เหมือนกันแต่แก้ **เซลล์ float** ใน kerning_table
ไม่ใช่ text offset table จึงตรวจด้วยตัวนี้ไม่ได้ · `gen_font_bin.py` ตรวจกลับเองทุกครั้ง (ขนาดเท่าเดิม ·
decode เทียบต้นฉบับทุกเซลล์ · นับไบต์ที่ต่าง ≤ 4 x เซลล์ที่ตั้งใจแก้)

ใช้:
  python scripts/check_inplace_bins.py                # ตรวจทุกไฟล์ใน build/text
  python scripts/check_inplace_bins.py --only a.bin   # เฉพาะบางไฟล์
  python scripts/check_inplace_bins.py --dir <โฟลเดอร์>  # ตรวจโฟลเดอร์อื่น เช่น release/.../en
  python scripts/check_inplace_bins.py --selftest     # ทดสอบตัวตรวจเอง
"""
import argparse
import io
import struct
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")   # กติกาเหล็กข้อ 6
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402
from patch_text_inplace import H_PTEXT, H_TEXT_COUNT, MAIN_PTR_OFF, _i32, walk_tables  # noqa: E402

BUILD_TEXT = paths.BUILD / "text" / "db.judge.en" / "en"
ORIG_DIR = paths.DB_EN / "en"
KNOWN_REBUILT = {"font.bin"}


def offset_table_ranges(src: bytes) -> list:
    """ช่วงไบต์ของ text offset table ทุกตารางในไฟล์ (ช่วงเดียวที่อนุญาตให้ต่างจากต้นฉบับ)"""
    ranges = []
    for t in walk_tables(src, _i32(src, MAIN_PTR_OFF), set()):
        n = _i32(src, t + H_TEXT_COUNT)
        p = _i32(src, t + H_PTEXT)
        if n > 0 and 0 < p < len(src):
            ranges.append((p, p + 4 * n))
    return ranges


def check_one(orig_p: Path, built_p: Path) -> list:
    """คืนรายการข้อความปัญหา (ว่าง = ผ่าน)"""
    src = orig_p.read_bytes()
    out = built_p.read_bytes()
    bad = []
    if len(out) < len(src):
        return ["ไฟล์สั้นกว่าต้นฉบับ (%s < %s) = ถูกประกอบใหม่ ไม่ใช่ patch ในที่"
                % ("{:,}".format(len(out)), "{:,}".format(len(src)))]

    allowed = offset_table_ranges(src)
    head = out[:len(src)]
    if head != src:
        outside, first = 0, None
        for i in range(len(src)):
            if head[i] != src[i] and not any(a <= i < b for a, b in allowed):
                outside += 1
                if first is None:
                    first = i
        if outside:
            bad.append("ไบต์ต่างจากต้นฉบับนอก text offset table %s ไบต์ (ตำแหน่งแรก 0x%X) = ไม่ใช่ patch ในที่"
                       % ("{:,}".format(outside), first))

    # ทุกออฟเซ็ตต้องชี้เข้าไฟล์ และสตริงต้องปิดท้ายด้วย NUL
    n_new = 0
    for a, b in allowed:
        for p in range(a, b, 4):
            off = struct.unpack_from("<i", out, p)[0]
            if off < 0 or off >= len(out):
                bad.append("text offset ที่ 0x%X ชี้นอกไฟล์ (%d)" % (p, off))
                continue
            if off and out.find(b"\x00", off) < 0:
                bad.append("สตริงที่ 0x%X ไม่มี NUL ปิดท้าย" % off)
            if off >= len(src):
                n_new += 1
    if len(out) > len(src) and n_new == 0:
        bad.append("มี pool ต่อท้ายแต่ไม่มีออฟเซ็ตไหนชี้ถึง (patch ไม่ได้ผล?)")
    return bad


def selftest() -> int:
    """ตัวตรวจต้องผ่านไฟล์ที่ patch มาถูก · ต้อง **จับได้** เมื่อไบต์อื่นถูกแก้ · และต้องไม่ผ่านไฟล์ reARMP rebuild"""
    import tempfile
    from build_text import make_mappings
    from patch_text_inplace import patch

    name = "controller_guide.bin"
    orig = ORIG_DIR / name
    mappings, _ = make_mappings({name})
    src = orig.read_bytes()
    good, hits, _ = patch(src, mappings[name])
    tmp = Path(tempfile.mkdtemp(prefix="chkinpl_"))
    (tmp / name).write_bytes(good)
    r1 = check_one(orig, tmp / name)
    print("selftest: ไฟล์ที่ patch ถูกต้อง (%d สตริง) -> %s" % (hits, "PASS" if not r1 else "FAIL " + str(r1)))

    tamper = bytearray(good)
    pos = _i32(src, MAIN_PTR_OFF)          # header ของตารางหลัก — ไม่ใช่ offset table แน่นอน
    tamper[pos] ^= 0xFF
    (tmp / "tamper.bin").write_bytes(bytes(tamper))
    r2 = check_one(orig, tmp / "tamper.bin")
    print("selftest: ไฟล์ที่ถูกแก้ไบต์อื่น -> %s" % ("PASS (จับได้)" if r2 else "FAIL (ตรวจไม่เจอ)"))

    rebuilt = paths.PROJECT / "release/JudgmentThai-th-v1.1.3/files/JudgmentThai/db.judge.en/en" / name
    r3 = check_one(orig, rebuilt) if rebuilt.exists() else ["(ไม่มีไฟล์ v1.1.3 ให้เทียบ)"]
    print("selftest: ไฟล์ reARMP rebuild (v1.1.3) -> %s" % ("PASS (จับได้)" if r3 else "FAIL (ตรวจไม่เจอ)"))
    ok = (not r1) and bool(r2) and bool(r3)
    print("selftest: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--dir", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    build_dir = Path(args.dir) if args.dir else BUILD_TEXT
    names = sorted(p.name for p in build_dir.glob("*.bin"))
    if args.only:
        want = {b if b.endswith(".bin") else b + ".bin" for b in args.only}
        names = [n for n in names if n in want]
    fails, known = 0, []
    for n in names:
        orig = ORIG_DIR / n
        if not orig.exists():
            print("!! %s: ไม่พบต้นฉบับใน extracted/db_en" % n)
            fails += 1
            continue
        bad = check_one(orig, build_dir / n)
        if bad and n in KNOWN_REBUILT:
            known.append(n)
            continue
        if bad:
            fails += 1
            print("!! %s: %s" % (n, " · ".join(bad[:3])))
    if known:
        print("ข้อยกเว้นที่รู้อยู่แล้ว (แก้เซลล์ float ในที่ · ตรวจใน gen_font_bin.py): %s" % ", ".join(known))
    print("\nตรวจ %d bins · ผ่าน %d · ไม่ผ่าน %d · ยกเว้น %d" % (len(names), len(names) - fails - len(known), fails, len(known)))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
