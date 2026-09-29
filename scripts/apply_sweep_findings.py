#!/usr/bin/env python3
"""รวม findings จากทีม sweep (translations/review/sweep/findings_*.json) แล้วเขียนคำแก้ลงไฟล์ done ต้นทาง

ตรวจก่อนเขียนทุกจุด: id มีใน index · key อยู่ใน done batch ไหนสักไฟล์ · จำนวน \\n เท่าเดิม · tag ชุดเดิม ·
ช่วงไทยติดกันหลังตัด tag <= 36 · ยาวไม่เกิน 1.5x — อักษร donor/สรรพนามให้ merge_qc ตรวจซ้ำตอน remerge

ใช้:  python scripts/apply_sweep_findings.py                    # รายงานอย่างเดียว
      python scripts/apply_sweep_findings.py --write            # เขียน conf=high ทั้งหมด
      python scripts/apply_sweep_findings.py --write --mid      # รวม mid ด้วย
      python scripts/apply_sweep_findings.py --only 07,12       # เฉพาะชิ้นที่ระบุ
รายงาน: translations/review/sweep/apply_report.md (ทุกจุด ทั้งที่รับ/ปฏิเสธ พร้อมเหตุผล)
"""
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths

SWEEP = paths.TRANSLATIONS / "review" / "sweep"
DONE = paths.TRANSLATIONS / "done"
TAG_RE = re.compile(r"<[^<>]*>|%[0-9]*\$?[sdxufi%]|\$\{[^}]*\}|~[^~\s]{0,40}~")
THAI_RUN = re.compile(r"[฀-๿]+")
MAX_RUN = 36


def unesc(s):
    return s.replace("\\n", "\n").replace("\\\\", "\\")


def validate(old, new):
    if not isinstance(new, str) or not new.strip():
        return "ว่าง"
    if new == old:
        return "เหมือนเดิม"
    if old.count("\n") != new.count("\n"):
        return "\\n ไม่เท่า"
    if TAG_RE.findall(old) != TAG_RE.findall(new):
        return "tag ไม่ตรง"
    w = max((len(r) for r in THAI_RUN.findall(re.sub(r"<[^<>]*>", "", new))), default=0)
    if w > MAX_RUN:
        return "ช่วงไทย %d > %d" % (w, MAX_RUN)
    if len(new) > max(len(old) * 1.5, len(old) + 12):
        return "ยาว %d vs %d" % (len(new), len(old))
    if len(new) < len(old) * 0.6 and len(old) - len(new) > 8:
        return "สั้นผิดปกติ %d vs %d (ตัดเนื้อหาทิ้ง?)" % (len(new), len(old))
    return None


def main():
    global SWEEP
    if "--dir" in sys.argv:                      # ใช้ซ้ำกับ review/blind และ review/register (รอบ 22)
        SWEEP = paths.TRANSLATIONS / "review" / sys.argv[sys.argv.index("--dir") + 1]
    write = "--write" in sys.argv
    take_mid = "--mid" in sys.argv
    def _opt(name):
        return set(sys.argv[sys.argv.index(name) + 1].split(",")) if name in sys.argv else set()
    skip_cat = _opt("--skip-cat")        # เช่น --skip-cat F  (หมวดที่ lead จัดการเองด้วยสคริปต์)
    mid_ids = _opt("--mid-ids")          # id ระดับ mid ที่ lead อ่านแล้วรับ
    reject_ids = _opt("--reject-ids")    # id ที่ lead ปฏิเสธแม้เป็น high
    only = None
    if "--only" in sys.argv:
        only = {x.zfill(2) for x in sys.argv[sys.argv.index("--only") + 1].split(",")}
    index = json.loads((SWEEP / "index.json").read_text(encoding="utf-8"))
    # ชุดงานเกลา (polish/chNN/chunk_*.tsv) เก็บ TH ตอนตัด — ถ้า master เปลี่ยนไปแล้ว (บทอื่นแก้คีย์ใช้ร่วม) ห้ามเขียนทับเงียบ ๆ
    seen_th = {}
    for cp in sorted(SWEEP.glob("chunk_*.tsv")):
        rows_ = cp.read_text(encoding="utf-8").splitlines()
        head = rows_[0].split("\t")
        if "id" not in head or "TH" not in head:
            continue
        ci, ct = head.index("id"), head.index("TH")
        for r in rows_[1:]:
            f = r.split("\t")
            if len(f) > ct:
                seen_th[f[ci]] = unesc(f[ct])
    master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
    key2batch, dones = {}, {}
    for dp in sorted(DONE.glob("batch_*.done.json")):
        d = json.loads(dp.read_text(encoding="utf-8"))
        dones[dp] = d
        for k in d.get("strings", {}):
            key2batch.setdefault(k, dp)

    rows, accepted = [], {}
    stat = Counter()
    for fp in sorted(SWEEP.glob("findings_*.json")):
        m = re.match(r"findings_(\d\d)", fp.name)
        if not m or (only and m.group(1) not in only):
            continue
        try:
            items = json.loads(fp.read_text(encoding="utf-8-sig"))
        except Exception as e:  # noqa: BLE001 — ไฟล์ agent อาจพัง ต้องรายงานไม่ใช่ล้ม
            rows.append((fp.name, "-", "-", "JSON พัง: %s" % e))
            stat["json พัง"] += 1
            continue
        if isinstance(items, dict):
            items = items.get("findings", [])
        for it in items:
            if not isinstance(it, dict):
                continue
            sid = str(it.get("id", ""))
            cat = str(it.get("cat", "?"))[:1]
            conf = it.get("conf") or it.get("sev") or "mid"      # ทีม blind/register (รอบ 22) ใช้ฟิลด์ sev แทน conf
            new = it.get("th_new")
            en = index.get(sid)
            if en is None:
                rows.append((fp.name, sid, cat, "id ไม่มีใน index")); stat["id ผิด"] += 1; continue
            old = master.get(en)
            if old is None:
                rows.append((fp.name, sid, cat, "key ไม่มีใน master")); stat["key ผิด"] += 1; continue
            if sid in seen_th and seen_th[sid] != old and new != old:
                rows.append((fp.name, sid, cat, "ไทยเปลี่ยนหลังตัดชุดงาน — lead ดูเอง")); stat["ไทยเปลี่ยนแล้ว"] += 1; continue
            if cat in skip_cat:
                rows.append((fp.name, sid, cat, "ข้ามหมวด (lead จัดการเอง)")); stat["ข้ามหมวด " + cat] += 1; continue
            if sid in reject_ids:
                rows.append((fp.name, sid, cat, "lead ปฏิเสธ")); stat["lead ปฏิเสธ"] += 1; continue
            if isinstance(new, str) and "\\n" in new and "\n" not in new:
                new = unesc(new)
            err = validate(old, new)
            if err:
                rows.append((fp.name, sid, cat, "ปฏิเสธ: " + err)); stat["ปฏิเสธ " + err.split()[0]] += 1; continue
            if conf != "high" and not take_mid and sid not in mid_ids:
                rows.append((fp.name, sid, cat, "mid — รอ lead")); stat["mid รอ"] += 1; continue
            if en not in key2batch:
                rows.append((fp.name, sid, cat, "key ไม่อยู่ใน done ไหนเลย")); stat["ไม่มี done"] += 1; continue
            if en in accepted and accepted[en][0] != new:
                rows.append((fp.name, sid, cat, "ซ้ำกับ finding อื่น (ใช้ตัวแรก)")); stat["ซ้ำ"] += 1; continue
            accepted[en] = (new, sid, cat, it.get("why", ""), old)
            rows.append((fp.name, sid, cat, "รับ (%s)" % conf)); stat["รับ " + cat] += 1

    touched = Counter()
    if write:
        for en, (new, *_rest) in accepted.items():
            dp = key2batch[en]
            dones[dp]["strings"][en] = new
            touched[dp.name] += 1
        for dp, d in dones.items():
            if touched[dp.name]:
                dp.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

    rep = ["# Sweep apply report", "",
           "รับ %d จุด · " % len(accepted) + " · ".join("%s %d" % kv for kv in sorted(stat.items())), "",
           "## รับแล้ว"]
    for en, (new, sid, cat, why, old) in accepted.items():
        rep.append("- `%s` [%s] %s\n  - EN: %r\n  - เดิม: %r\n  - ใหม่: %r" % (sid, cat, why, en[:120], old[:160], new[:160]))
    rep.append("\n## ทุกรายการ")
    for f, sid, cat, note in rows:
        rep.append("- %s `%s` [%s] %s" % (f, sid, cat, note))
    (SWEEP / "apply_report.md").write_text("\n".join(rep) + "\n", encoding="utf-8", newline="\n")
    print("findings รวม %d · รับ %d · " % (len(rows), len(accepted)) + " · ".join("%s %d" % kv for kv in sorted(stat.items())))
    if write:
        print("เขียน done: " + " · ".join("%s %d" % kv for kv in touched.items()))
        print("ขั้นถัดไป: remerge_stale.py --write → fix_thai_wrap.py --check → build_text --clean → gen_font_bin → deploy_spoil")
    return 0


if __name__ == "__main__":
    sys.exit(main())
