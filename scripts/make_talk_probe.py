#!/usr/bin/env python3
"""ทดสอบว่า **บทสนทนา/ซับในเกม** วาดด้วยฟอนต์ไหน — แพตช์ `talk.bin` ทุกบรรทัดพร้อมกัน

เหตุผลที่ต้องแพตช์ทุกบรรทัด: เราหาบรรทัดที่ผู้ใช้จะเจอ "แน่ ๆ ภายในสองนาที" ไม่ได้ (เซฟอยู่กลาง
บทที่ 4) การเขียนข้อความทดสอบลงทุกบรรทัดจึงรับประกันว่าเดินไปคุยกับใครก็เห็น

แต่ละบรรทัดถูกแทนด้วยข้อความเดียวกันที่ encode สองแบบวางคู่กัน:
  `เอ` = donor ของฟอนต์ไตเติล `meta_ot_cond_book` (พิสูจน์แล้วว่าขึ้นทั้งไตเติล/จอโลโก้/เซฟ-โหลด)
  `บี` = donor ของฟอนต์ข้อความหลัก `tbgm_0p_ja` (Cyrillic/Samaritan ตาม y6_slotmap)

อ่านผลจากซับที่ขึ้นจอ:
  เห็น `เอ` อย่างเดียว  -> ซับใช้ฟอนต์ไตเติล = ทั้งเกมอยู่บนตาราง 384 เซลล์ (โจทย์โควตา)
  เห็น `บี` อย่างเดียว  -> ซับใช้ tbgm_0p_ja = ข้อความหลักมี slot ว่าง 2,157 ช่อง สบาย
  เห็นทั้งคู่          -> engine มี fallback ข้ามฟอนต์
  ไม่เห็นทั้งคู่        -> ซับใช้ฟอนต์ตัวที่สาม (ต้องไล่ต่อ)

⚠ นี่คือบิลด์ทดสอบล้วน บทสนทนาทั้งเกมจะกลายเป็นข้อความทดสอบ — ถอดด้วย
`python scripts/deploy_spoil.py --restore` หรือ build ใหม่โดยไม่รวมสคริปต์นี้

ใช้:  python scripts/make_talk_probe.py
อ่าน  extracted/db_en/en/talk.bin (ต้นฉบับ — ไม่แตะ)
เขียน build/text/db.judge.en/en/talk.bin
"""
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from make_extra_tests import tbgm_encode
from title_encode import encode
from title_menu_map import ENCODE

SRC = paths.EXTRACTED / "db_en" / "en" / "talk.bin"
STAGE = paths.BUILD / "text" / "db.judge.en" / "en"
WORK = paths.BUILD / "text" / "_work_talk"

MIN_LEN = 12          # แตะเฉพาะสตริงที่ยาวพอจะเป็นบทพูดจริง (เลี่ยง key/ชื่อคอลัมน์)


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    STAGE.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC, WORK / SRC.name)

    r = subprocess.run([sys.executable, str(paths.REARMP), SRC.name],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP export ล้ม: {r.stderr[-400:]}"
    jf = WORK / (SRC.name + ".json")
    data = json.loads(jf.read_text(encoding="utf-8"))

    probe = encode("เอ", ENCODE) + " " + tbgm_encode("บี")
    print(f"ข้อความทดสอบ: {probe!r}  (เอ=ฟอนต์ไตเติล · บี=tbgm_0p_ja)")

    count = 0

    def walk(node):
        nonlocal count
        if isinstance(node, dict):
            for k, v in list(node.items()):
                if isinstance(v, str):
                    if len(v) >= MIN_LEN and " " in v and not k.startswith("reARMP"):
                        node[k] = probe
                        count += 1
                else:
                    walk(v)

    walk(data)
    print(f"แทนข้อความ {count} บรรทัด")
    assert count > 1000, "แทนได้น้อยผิดปกติ — โครงไฟล์อาจไม่ตรงที่คาด"

    jf.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    r = subprocess.run([sys.executable, str(paths.REARMP), jf.name],
                       cwd=str(WORK), capture_output=True)
    assert r.returncode == 0, f"reARMP rebuild ล้ม: {r.stderr[-400:]}"
    rebuilt = WORK / (SRC.name + ".json.bin")
    assert rebuilt.exists(), "ไม่พบ bin ที่ rebuild"

    out = STAGE / SRC.name
    shutil.copy2(rebuilt, out)
    assert probe.encode("utf-8") in out.read_bytes(), "ข้อความทดสอบไม่อยู่ใน bin"
    print(f"เขียน {out} ({out.stat().st_size} B, ต้นฉบับ {SRC.stat().st_size} B)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
