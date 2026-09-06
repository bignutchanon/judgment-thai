#!/usr/bin/env python3
"""ตัด master_th.json เป็นชิ้นสำหรับทีมผู้ตรวจกวาดคุณภาพ (sweep รอบ 21 — 6 ก.ย. 2026)

ที่มา: รายงานผู้เล่น 6 ก.ย. เจอคำแปลผิดความหมาย/เพศคำนามผิดบริบท/คำเพี้ยน/ติดอ่างผิดตัว/ช่องว่างผ่าวลี
ที่ QC อัตโนมัติจับไม่ได้ → ให้ agent อ่านคู่ EN→TH ทีละชิ้นแล้วรายงานเฉพาะจุดบกพร่องเป็น JSON

ใช้:  python scripts/make_sweep_chunks.py            # เขียน translations/review/sweep/chunk_NN.tsv
เอาต์พุต: chunk_NN.tsv (คอลัมน์ id · bin · EN · TH — \n ในข้อความเขียนเป็น \n ตัวอักษร)
          + index.json (id → key EN) สำหรับ apply_sweep_findings.py
"""
import io
import json
import os
import sys
from collections import OrderedDict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

OUT = paths.TRANSLATIONS / "review" / "sweep"
CHUNK_CHARS = 150_000        # ~EN+TH รวม ต่อชิ้น (≈ 90-110k tokens เมื่อรวม prompt)
SKIP_BINS = {"pause_license.bin"}   # EULA คง EN


def main():
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    sbb = json.load(io.open(paths.EXTRACTED / "strings_by_bin.json", encoding="utf-8"))
    loc = {}
    for b, ss in sbb.items():
        for s in ss:
            loc.setdefault(s, b)
    # จัดกลุ่มตาม bin เพื่อให้ผู้ตรวจเห็นบริบทเดียวกัน (talk/sound_auth = บทพูดเรียงตามลำดับในไฟล์)
    by_bin = OrderedDict()
    for b, ss in sbb.items():
        if b in SKIP_BINS:
            continue
        for s in ss:
            th = master.get(s)
            if not isinstance(th, str) or th == s or loc.get(s) != b:
                continue
            by_bin.setdefault(b, []).append((s, th))
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("chunk_*.tsv"):
        old.unlink()
    index, chunks, cur, size = {}, [], [], 0
    order = sorted(by_bin.items(), key=lambda kv: -len(kv[1]))
    for b, pairs in order:
        for en, th in pairs:
            n = len(en) + len(th)
            if cur and size + n > CHUNK_CHARS:
                chunks.append(cur)
                cur, size = [], 0
            cur.append((b, en, th))
            size += n
    if cur:
        chunks.append(cur)
    esc = lambda s: s.replace("\\", "\\\\").replace("\t", " ").replace("\n", "\\n")
    for i, ch in enumerate(chunks, 1):
        lines = ["id\tbin\tEN\tTH"]
        for j, (b, en, th) in enumerate(ch, 1):
            sid = f"{i:02d}-{j:04d}"
            index[sid] = en
            lines.append(f"{sid}\t{b.replace('.bin','')}\t{esc(en)}\t{esc(th)}")
        (OUT / f"chunk_{i:02d}.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
    tot = sum(len(c) for c in chunks)
    print(f"ชิ้น {len(chunks)} · คู่ {tot:,} · เฉลี่ย {tot // len(chunks):,} คู่/ชิ้น")
    for i, ch in enumerate(chunks, 1):
        bins = OrderedDict()
        for b, _, _ in ch:
            bins[b] = bins.get(b, 0) + 1
        print(f"  chunk_{i:02d}: {len(ch):5,} คู่ · " + " · ".join(f"{b.replace('.bin','')} {n}" for b, n in list(bins.items())[:4]))


if __name__ == "__main__":
    main()
