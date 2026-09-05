#!/usr/bin/env python3
"""patch string ใน ARMP bin แบบระบุคู่ (EN เดิม -> ไทย) — ใช้ทำ build ทดสอบ/สปอย

รับนิยามงานจาก EDITS ด้านล่าง: ต่อ bin ระบุรายการ (exact EN, ไทย, mode)
  mode "real"  = ใส่ไทยแท้ (ต้องมี record real-cp ในฟอนต์แล้ว)
  mode "donor" = encode เป็น donor ตาม y6_slotmap
แทนที่ทุก cell ที่ค่าตรงเป๊ะกับ EN เดิม (ทั้ง bin)

ใช้:  python scripts/patch_bin_strings.py
อ่าน  extracted/db_en/en/<bin> (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/<bin> (โครงพร้อม copy เข้า mods)
"""
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from y6_slotmap import ENCODE

STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / "_work"

# bin -> [(exact EN, ไทย, mode)]
EDITS = {
    "ui_text.bin": [
        ("Press any button", "กดปุ่มใดก็ได้", "real"),
    ],
    "msg.bin": [
        ("Save completed.", "บันทึกเรียบร้อยแล้ว", "real"),
        ("Load completed.", "โหลดเรียบร้อยแล้ว", "donor"),
    ],
}


def donor_encode(s):
    out = []
    for c in s:
        if c in ENCODE:
            out.append(chr(ENCODE[c]))
        elif "฀" <= c <= "๿":
            raise SystemExit(f"ตัวอักษรไทยไม่มีใน slotmap: {c!r} (U+{ord(c):04X})")
        else:
            out.append(c)
    return "".join(out)


def walk_replace(node, mapping, stats):
    """เดินทุก dict/list แทนค่า string ที่ตรงเป๊ะ"""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and v in mapping:
                node[k] = mapping[v]
                stats[v] = stats.get(v, 0) + 1
            else:
                walk_replace(v, mapping, stats)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            if isinstance(v, str) and v in mapping:
                node[i] = mapping[v]
                stats[v] = stats.get(v, 0) + 1
            else:
                walk_replace(v, mapping, stats)


def patch_bin(bin_name, edits):
    src = paths.EXTRACTED / "db_en" / "en" / bin_name
    assert src.exists(), f"ไม่พบ {src}"
    WORK.mkdir(parents=True, exist_ok=True)
    STAGE.mkdir(parents=True, exist_ok=True)
    work_bin = WORK / bin_name
    shutil.copy2(src, work_bin)

    r = subprocess.run([sys.executable, str(paths.REARMP), str(work_bin)],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP export {bin_name} ล้ม"
    work_json = WORK / (bin_name + ".json")
    data = json.loads(work_json.read_text(encoding="utf-8"))

    mapping = {en: (th if mode == "real" else donor_encode(th))
               for en, th, mode in edits}
    stats = {}
    walk_replace(data, mapping, stats)
    for en, th, mode in edits:
        n = stats.get(en, 0)
        print(f"  {bin_name}: '{en}' -> {th} [{mode}] x{n}")
        assert n > 0, f"ไม่พบ '{en}' ใน {bin_name}"

    work_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    r = subprocess.run([sys.executable, str(paths.REARMP), str(work_json)],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP rebuild {bin_name} ล้ม"
    rebuilt = WORK / (bin_name + ".json.bin")
    assert rebuilt.exists()
    out = STAGE / bin_name
    shutil.copy2(rebuilt, out)

    blob = out.read_bytes()
    for th_enc in mapping.values():
        assert th_enc.encode("utf-8") in blob
    print(f"  -> {out} ({out.stat().st_size} B)")


def main():
    for bin_name, edits in EDITS.items():
        patch_bin(bin_name, edits)
    print("เสร็จ — รัน deploy_spoil.py เพื่อส่งเข้าเกม")


if __name__ == "__main__":
    main()
