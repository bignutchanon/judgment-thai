# HANDOFF — Judgment ม็อดแปลไทย (JETH)

> อัปเดตล่าสุด: 14 ส.ค. 2026 — bootstrap repo (ยังไม่เริ่มงานจริง)

## สถานะ: Phase 0 — bootstrap

สร้างโครง repo + CLAUDE.md จากการ research ในโปรเจกต์ K3 — เกมยังไม่ได้ติดตั้งในเครื่อง ยังไม่ extract อะไรทั้งสิ้น

## งานถัดไป (เรียงลำดับ)
1. ผู้ใช้ติดตั้งเกม (Steam) → บันทึก path ลงตาราง GAME ใน CLAUDE.md + ตั้ง env `JUDGE_GAME`
2. verify codename: หา `db.judge.en.par` (หรือชื่อจริง) ใน `runtime/media/data/` — แก้ CLAUDE.md ถ้าไม่ตรง
3. copy เครื่องมือจาก K3: `tools/ParTool.exe`, `tools/reARMP_fixed.py`, `tools/SRMM-4.8.4/`
4. port สคริปต์ pipeline จาก K3 (`scripts/`) — แทน bis→judge + สร้าง `scripts/paths.py`
5. extract db par + สร้าง `docs/research.md` (โครงไฟล์, รายชื่อ bin, จำนวนบรรทัด, ภาษาที่มี)
6. survey ฟอนต์ (`survey_fonts.py` ตาม FONT_PLAYBOOK) — ห้าม copy slot map จาก K2R/K3
7. font PoC ในเกม (donor Cyrillic แบบ K2R/K3 เป็นสมมติฐานแรก) — ผู้ใช้ทดสอบ
8. โหลดม็อด MOD2SUB (nexus judgment/228) มาแกะรายชื่อไฟล์ที่เขาแตะ เทียบกับ worklist เรา
9. glossary + PRONOUN_MATRIX ตัวละคร Judgment (Yagami, Sugiura, Higashi, Genda, Saori ฯลฯ) — Kaito ล็อกแล้ว (มาซาฮารุ ไคโตะ)

## ข้อควรจำ
- ลำดับแนะนำ: ทำ Judgment ภาคแรกให้จบก่อน Lost Judgment — ได้ TM ตัวละครหลักไปใช้ต่อ
- โปรเจกต์พี่น้อง: `D:\Projects\lost-judgment-thai` (glossary ตัวละครต้องล็อกร่วมกัน)
