#!/usr/bin/env python3
"""แทนที่ข้อความในไฟล์ ARMP โดย **ไม่ประกอบไฟล์ใหม่** (patch ในที่) — พอร์ตจาก Gaiden/Y8 15 ก.ย. 2026

ทำไมต้องมีตัวนี้: `build_text.py --builder rebuild` ถอด .bin เป็น JSON แล้วให้ reARMP ประกอบไฟล์ใหม่
ทั้งไฟล์ ผล decode กลับมาเท่าต้นฉบับทุกเซลล์ แต่ **เลย์เอาต์จริงไม่เหมือนของ SEGA** (main table ย้ายมา
ต้นไฟล์ · padding/ขนาดต่าง · `SPECIAL_FIELD_INDICES` งอกศูนย์ท้าย · text pool ถูก dedup) —
Y8 (20 ส.ค. 2026) และ Gaiden (21 ส.ค. 2026) พิสูจน์ในเกมแล้วว่าไฟล์แบบนั้นทำเกมค้าง/เด้งที่จอสอนปุ่ม
ครั้งแรกของมินิเกม (`controller_guide.bin`) **แม้ rebuild เป็น EN ล้วน** = ปัญหาอยู่ที่ตัวเขียนไฟล์
ไม่ใช่คำแปล · JETH เปลี่ยนมาใช้ตัวนี้เป็นค่าเริ่มต้นหลังรายงานผู้เล่น 15 ก.ย. 2026 (v1.1.3 "not responding
ทุก ~30 นาที") เพราะ round-trip พบศูนย์งอกแบบเดียวกันใน complete/complete_group/shop/
verification_todo_item/minigame_photo_shooting_mission_todo_item

วิธี: เดินทุกตาราง (รวมตารางย่อยในคอลัมน์ชนิด 9 ทุกชั้น) อ่าน text offset table ของแต่ละตาราง
ต่อสตริงใหม่ไว้ท้ายไฟล์ แล้วแก้ **เฉพาะตัวเลขใน text offset table** ให้ชี้สตริงใหม่ — ไบต์อื่นทุกไบต์
เหมือนต้นฉบับเป๊ะ (ตรวจได้ด้วย `scripts/check_inplace_bins.py`)

mapping = {EN: สตริงที่เข้ารหัส donor แล้ว} (ผลของ `SlotMap.encode()` — build_text.make_mappings ทำให้)
ตัวนี้ **ไม่ encode เอง** ต่างจากฉบับ Gaiden ที่รับไทยดิบ

ใช้:
  python scripts/patch_text_inplace.py <input.bin> <mapping.json> <output.bin> [--skip-values a,b]
  python scripts/patch_text_inplace.py --selftest <bin>[,<bin>...]   # patch แล้ว decode เทียบต้นฉบับทีละเซลล์
  python scripts/patch_text_inplace.py --selftest all                # ทุก bin ที่ build_text จะบิลด์

--skip-values: ค่าอังกฤษที่ห้ามแทนที่ในไฟล์นี้ (identifier ของเอนจิ้นที่บังเอิญตรงกับข้อความ)
--selftest: ต้องต่างจากต้นฉบับ **เฉพาะเซลล์ที่มีคำแปล** และค่าใหม่ต้องเท่ากับ mapping[EN] เป๊ะ
"""
import concurrent.futures as cf
import io
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")   # กติกาเหล็กข้อ 6
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402

MAIN_PTR_OFF = 0x10
VERSION_OFF = 0x0A      # เวอร์ชัน ARMP (<H) — v2 เก็บค่าคอลัมน์ชนิด table เป็น 8 ไบต์
TYPE_TABLE = 9          # คอลัมน์ที่เก็บ "ตารางย่อย" (พอยน์เตอร์ไปยัง header ของอีกตาราง)

# ออฟเซ็ตของฟิลด์ใน table header
H_ROW_COUNT = 0x00
H_COL_COUNT = 0x04
H_TEXT_COUNT = 0x08
H_PCOL_TYPES = 0x18
H_PCOL_CONTENT = 0x1C
H_STORAGE_MODE = 0x23
H_PTEXT = 0x24
H_PSUBTABLE = 0x3C
H_PCOL_TYPES_AUX = 0x48


def _i32(buf, off):
    return struct.unpack_from("<i", buf, off)[0]


def _version(buf):
    return struct.unpack_from("<H", buf, VERSION_OFF)[0]


def read_cstr(buf, off):
    end = buf.index(b"\x00", off)
    return buf[off:end]


def walk_tables(buf, table_off, seen, version=None):
    """คืนออฟเซ็ตของทุกตารางในไฟล์ (ตารางหลัก + ตารางย่อยทุกชั้น)"""
    if version is None:
        version = _version(buf)
    if table_off in seen or table_off <= 0 or table_off + 0x50 > len(buf):
        return []
    seen.add(table_off)
    found = [table_off]

    # ตารางที่ผูกกับ header ตรง ๆ (ฟิลด์ pSubTable)
    found += walk_tables(buf, _i32(buf, table_off + H_PSUBTABLE), seen, version)

    row_count = _i32(buf, table_off + H_ROW_COUNT)
    col_count = _i32(buf, table_off + H_COL_COUNT)
    p_types = _i32(buf, table_off + H_PCOL_TYPES)
    p_content = _i32(buf, table_off + H_PCOL_CONTENT)
    p_aux = _i32(buf, table_off + H_PCOL_TYPES_AUX)
    storage_mode = buf[table_off + H_STORAGE_MODE]
    if col_count <= 0 or row_count <= 0 or p_types <= 0 or p_content <= 0:
        return found

    types = list(buf[p_types:p_types + col_count])
    table_cols = [i for i, t in enumerate(types) if t == TYPE_TABLE]
    if not table_cols:
        return found

    for ci in table_cols:
        if storage_mode == 1:
            if p_aux <= 0:
                continue
            shift = _i32(buf, p_aux + ci * 16 + 4)
            if shift < 0:
                continue
            for r in range(row_count):
                row_ptr = _i32(buf, p_content + 4 * r)
                if row_ptr <= 0:
                    continue
                sub = _i32(buf, row_ptr + shift)
                found += walk_tables(buf, sub, seen, version)
        else:
            col_ptr = _i32(buf, p_content + 4 * ci)
            if col_ptr <= 0:
                continue
            # ARMP v2 เก็บค่าคอลัมน์ชนิด table เป็น int64 (ช่องละ 8 ไบต์) — ตรงกับ valueSizes[9] ของ reARMP
            stride = 8 if version >= 2 else 4
            for r in range(row_count):
                sub = _i32(buf, col_ptr + stride * r)
                found += walk_tables(buf, sub, seen, version)
    return found


def patch(src, mapping, skip_values=frozenset()):
    """คืน (ไบต์ผลลัพธ์, จำนวน offset ที่แก้, จำนวนตาราง)"""
    main_off = _i32(src, MAIN_PTR_OFF)
    tables = walk_tables(src, main_off, set())

    out = bytearray(src)
    if len(out) % 16:                    # เริ่มบล็อกใหม่ที่ขอบ 16 ไบต์แบบไฟล์ของ SEGA
        out += b"\x00" * (16 - len(out) % 16)
    base = len(out)
    tail = bytearray()
    hits = 0
    # สตริงเดียวกันเก็บครั้งเดียว (text offset เป็นออฟเซ็ตสัมบูรณ์ จึงชี้ร่วมกันข้ามตารางได้)
    pool = {}

    for t in tables:
        text_count = _i32(src, t + H_TEXT_COUNT)
        p_text = _i32(src, t + H_PTEXT)
        if text_count <= 0 or p_text <= 0:
            continue
        for i in range(text_count):
            off = _i32(src, p_text + 4 * i)
            if off <= 0 or off >= len(src):
                continue
            try:
                en = read_cstr(src, off).decode("utf-8")
            except (UnicodeDecodeError, ValueError):
                continue
            if en in skip_values:
                continue
            new = mapping.get(en)
            if not new or new == en:
                continue
            enc = new.encode("utf-8") + b"\x00"
            at = pool.get(enc)
            if at is None:
                at = base + len(tail)
                pool[enc] = at
                tail += enc
                if len(tail) % 4:        # สตริงถัดไปเริ่มที่ขอบ 4 ไบต์
                    tail += b"\x00" * (4 - len(tail) % 4)
            struct.pack_into("<i", out, p_text + 4 * i, at)
            hits += 1

    out += tail
    if len(out) % 16:
        out += b"\x00" * (16 - len(out) % 16)
    return bytes(out), hits, len(tables)


# ---------------------------------------------------------------- selftest
def _decode(bin_path, work, tag):
    dst = work / (tag + ".bin")
    shutil.copy(bin_path, dst)
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, str(paths.REARMP), dst.name], cwd=str(work), env=env,
                       capture_output=True, timeout=3000)
    j = work / (dst.name + ".json")
    if not j.exists():
        raise RuntimeError("decode ล้มเหลว: %r" % r.stderr[-300:])
    return json.load(io.open(j, encoding="utf-8"))


def _cells(d, path=""):
    """ทุกค่าใบไม้ในตาราง (รวมตารางย่อย) -> {path: value}"""
    out = {}
    if isinstance(d, dict):
        for k, v in d.items():
            out.update(_cells(v, path + "/" + str(k)))
    elif isinstance(d, list):
        for i, v in enumerate(d):
            out.update(_cells(v, path + "/" + str(i)))
    else:
        out[path] = d
    return out


def selftest_one(name, mapping, skip_values=frozenset()):
    src_bin = paths.DB_EN / "en" / name
    orig_json = src_bin.with_name(name + ".json")
    work = Path(tempfile.mkdtemp(prefix="inpl_"))
    try:
        src = src_bin.read_bytes()
        out, hits, ntab = patch(src, mapping, skip_values)
        patched = work / "patched.bin"
        patched.write_bytes(out)
        got = _cells(_decode(patched, work, "a"))
        ref = _cells(json.load(io.open(orig_json, encoding="utf-8")) if orig_json.exists()
                     else _decode(src_bin, work, "b"))
        keys = set(got) | set(ref)
        bad, n_tr = [], 0
        for k in sorted(keys):
            a, b = got.get(k), ref.get(k)
            if a == b:
                continue
            if isinstance(b, str) and b not in skip_values and mapping.get(b) == a:
                n_tr += 1
                continue
            bad.append((k, a, b))
        return {"bin": name, "tables": ntab, "hits": hits, "cells": len(keys), "translated": n_tr,
                "bad": bad, "size": (len(src), len(out))}
    except Exception as e:                                   # noqa: BLE001
        return {"bin": name, "error": "%s: %s" % (type(e).__name__, e)}
    finally:
        shutil.rmtree(work, ignore_errors=True)


def selftest(which, workers=6):
    from build_text import SKIP_VALUES, make_mappings   # noqa: E402
    only = None if which == ["all"] else set(which)
    mappings, _ = make_mappings(only)
    if not mappings:
        print("ไม่มี bin ที่ต้องทดสอบ (ชื่อผิด หรือไม่มีคำแปล?)")
        return 2
    fails = 0
    with cf.ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(selftest_one, b, m, frozenset(SKIP_VALUES.get(b, ()))): b
                for b, m in sorted(mappings.items())}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            r = fut.result()
            if "error" in r:
                fails += 1
                print("[%3d/%3d] !! %-44s %s" % (i, len(futs), r["bin"], r["error"]))
                continue
            ok = not r["bad"] and r["hits"] > 0 and r["translated"] > 0
            if not ok:
                fails += 1
            print("[%3d/%3d] %s %-44s ตาราง %3d · แก้ %5d · เซลล์ %9s · คำแปล %5d · ผิดคาด %d · %s -> %s B"
                  % (i, len(futs), "ok " if ok else "!! ", r["bin"], r["tables"], r["hits"],
                     "{:,}".format(r["cells"]), r["translated"], len(r["bad"]),
                     "{:,}".format(r["size"][0]), "{:,}".format(r["size"][1])))
            for k, a, b in r["bad"][:5]:
                print("       %s: patched=%r orig=%r" % (k, a, b))
    print("\nselftest %d bin · ผิดคาด/ล้มเหลว %d · %s" % (len(mappings), fails, "PASS" if not fails else "FAIL"))
    return 1 if fails else 0


def main():
    args = sys.argv[1:]
    skip_values = frozenset()
    if "--skip-values" in args:
        i = args.index("--skip-values")
        skip_values = frozenset(v for v in args[i + 1].split(",") if v)
        del args[i:i + 2]
    if args and args[0] == "--selftest":
        if len(args) < 2:
            print(__doc__)
            return 2
        which = [b if b.endswith(".bin") or b == "all" else b + ".bin" for b in args[1].split(",") if b]
        return selftest(which)
    if len(args) < 3:
        print(__doc__)
        return 2
    in_bin, map_json, out_bin = args[:3]
    src = open(in_bin, "rb").read()
    mapping = json.load(io.open(map_json, encoding="utf-8"))
    out, hits, ntab = patch(src, mapping, skip_values)
    os.makedirs(os.path.dirname(os.path.abspath(out_bin)) or ".", exist_ok=True)
    open(out_bin, "wb").write(out)
    print("%s: patched %d string(s) ใน %d ตาราง (%s -> %s ไบต์) -> %s"
          % (os.path.basename(in_bin), hits, ntab, "{:,}".format(len(src)), "{:,}".format(len(out)), out_bin))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
