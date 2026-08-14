# HANDOFF — Judgment ม็อดแปลไทย (JETH)

> อัปเดตล่าสุด: 14 ส.ค. 2026 — bootstrap จาก session research ในโปรเจกต์ K3 (ยังไม่เริ่มงานในเกมจริง)
> เอกสารนี้เขียนให้ session ใหม่ใน repo นี้ทำงานต่อได้ทันทีโดยไม่ต้อง research ซ้ำ

## บริบท: repo นี้มาจากไหน

สร้างเมื่อ 14 ส.ค. 2026 ระหว่าง session ของโปรเจกต์ K3 (`D:\Projects\yakuza-kiwami-3`) หลังผู้ใช้สั่ง research การทำม็อดแปลไทย Judgment/Lost Judgment ทีมแปลชุดนี้ทำม็อดไทยสาย RGG มาแล้ว: K2R → Pirate → Y7 → Y8 → Gaiden (ship v1.0 แล้ว) → K3 (กำลังทำ ~66%) — pipeline ทั้งหมดอยู่ในโปรเจกต์เหล่านั้นและ **พร้อม port มาใช้** อ่าน `CLAUDE.md` ของ repo นี้ก่อน (กติกาเหล็ก + ตาราง path ครบ)

## ข้อเท็จจริงที่ verify แล้ว (จาก research 14 ส.ค. 2026 — ไม่ต้องค้นซ้ำ)

1. **SRMM/RMM (Parless) รองรับ Judgment อย่างเป็นทางการ** (Steam เท่านั้น) — อยู่ในรายชื่อ Supported Games ของ RyuModManager wiki (repo archived พ.ย. 2023 แต่ SRMM ที่เราใช้คือ fork ที่ยังไปต่อ) → loose file ผ่าน `mods/` ใช้ได้ ไม่ต้องทดสอบแบบเดา ๆ เหมือน K3
2. **มีม็อดไทย Google MT อยู่แล้ว**: "Judgment MOD2SUB TH EN google V1" — https://www.nexusmods.com/judgment/mods/228 — ติดตั้งแบบวางทับ `runtime/media` = พิสูจน์ว่าเส้นทาง ARMP+font ไทยแสดงผลได้จริงในเกมนี้ · **ห้ามใช้เป็น TM** (คุณภาพ MT) แต่โหลดมาแกะรายชื่อไฟล์ที่เขาแตะได้ (ประหยัดเวลา research มาก) · หมายเหตุ: Nexus บล็อก WebFetch (403) — ต้องเปิดเบราว์เซอร์/โหลดเอง
3. **เอนจิ้น**: Judgment (2018, PC port 2022 ฐาน PS5 remaster) = Dragon Engine รุ่นยุค Y6/Kiwami 2 → ภาคต้นแบบใกล้สุดคือ **K2R** (`D:\Projects\yakuza-kiwami-2-mod`) ทั้งโครง par และฟอนต์ (donor Cyrillic U+0400 — K3 ก็ใช้สายนี้และ font PoC ผ่านในเกมแล้ว)
4. **codename ภายในคาดว่า `judge`** — ยังไม่ยืนยันจากไฟล์จริง (เกมยังไม่ติดตั้ง) · ที่ยืนยันแล้วคือแพเทิร์นตระกูล: `db.<code>.<lang>.par` (LJ = `db.coyote.en.par`, Y7 = yazawa, Gaiden = aston, K3 = bis)
5. ภาษาในเกม: EN/JA (ม็อด Retrial เพิ่ม zh/ko ได้ = ช่อง lang ยืดหยุ่น) — carrier น่าจะเป็น EN ตามธรรมเนียมทุกภาค

## สถานะ: Phase 0 จบ — โครง repo + CLAUDE.md + FONT_PLAYBOOK พร้อม · เกมยังไม่ติดตั้ง

## งานถัดไป (เรียงลำดับ ทำต่อได้เลย)

**ขั้น 1 — รอผู้ใช้ติดตั้งเกม (blocker เดียวตอนนี้)**
ติดตั้งแล้ว: จด path ลง CLAUDE.md ตาราง GAME + ตั้ง env `JUDGE_GAME` — ตอน research เช็คแล้วไม่มีใน `D:\SteamLibrary\steamapps\common`

**ขั้น 2 — verify สมมติฐานกับไฟล์จริง (งานแรกของ session ถัดไป)**
- `ls <GAME>/runtime/media/data/` → หา `db.judge.en.par` (ถ้าชื่ออื่น แก้ CLAUDE.md ทันที) + `font.judge.par` + รายชื่อ lang par ทั้งหมด
- เช็คว่ามี `motion/`, `stay/` layout แบบยุค K2 หรือ layout ใหม่ — มีผลกับ DENY_BINS

**ขั้น 3 — copy เครื่องมือ + port สคริปต์จาก K3** (K3 = ชุดล่าสุด อ่านอย่างเดียว copy เข้ามาก่อนแก้)
- `tools/`: `ParTool.exe` (1.3.4), `reARMP_fixed.py` (มี guard ROW_COUNT==0), `SRMM-4.8.4/` (ห้ามอัปเกรด 5.x — CLI ถูกตัด)
- `scripts/` จาก K3 (แทนที่ bis→judge, k3→jeth): `k3_paths.py` (→ `paths.py`), `extract_all_en.py`, `make_worklist.py`, `build_speaker_map.py`, `make_batch_brief.py`, `write_done.py`, `merge_qc.py`, `fix_thai_wrap.py`, `deploy.py`, `survey_fonts.py`, `thai_encode.py`, `font_tool.py`, `inject_thai_sdf.py`, `build_release.py`
- `font/Sarabun-Regular.ttf` จาก K3
- docs อ้างอิงที่ควร copy: `TRANSLATOR_BRIEF_y8.md`, `REWORK_RULES_pirate.md` (บัญชี DENY_BINS), `glossary_{gaiden,y8,y7,pirate,k2}.md` — ทั้งหมดอยู่ `yakuza-kiwami-3/docs/reference/`
- skill ทีม: adapt `yakuza-kiwami-3/.claude/skills/k3-team-lead/SKILL.md` → `.claude/skills/jeth-team-lead/`
- ⚠ ค่า game-specific ในสคริปต์ (รายชื่อ bin, tier table, BIN_HINT/CORE_RULES, ชื่อฟอนต์, DENY_BINS) ต้อง verify กับไฟล์ Judgment จริงทุกตัวตอนใช้ครั้งแรก — ห้ามเชื่อค่า K3

**ขั้น 4 — extract + สร้าง `docs/research.md`**
แตก `db.judge.en.par` → บันทึก: รายชื่อ bin + จำนวนบรรทัด, โครง ARMP, ภาษาที่มี, bin เสี่ยง engine table — รูปแบบเอกสารดู `yakuza-kiwami-3/docs/research.md` (ถ้ามีแล้ว) หรือของ Gaiden

**ขั้น 5 — font survey + PoC**
- backup `font.judge.par` → `.orig` ก่อนเสมอ
- `survey_fonts.py` — **ห้าม copy slot map จาก K2R/K3** (บทเรียน: รายชื่อฟอนต์ต่างกันทุกภาค) — อ่าน `docs/reference/FONT_PLAYBOOK.md` ทั้งไฟล์ก่อนแตะ
- สมมติฐานแรก: donor Cyrillic U+0400–U+0452 แบบ K2R/K3 → ฉีด Sarabun → drop-in → **ผู้ใช้ทดสอบในเกม** (ห้ามเปิดเกมเอง)
- font loose ผ่าน Parless ไม่โหลด (เกมโหลดฟอนต์ก่อน hook) — PoC ต้อง drop-in เท่านั้น

**ขั้น 6 — แกะม็อด MOD2SUB** (nexus judgment/228) — เทียบรายชื่อไฟล์ที่เขาแตะกับ worklist เรา หา bin ที่เราอาจตกหล่น

**ขั้น 7 — เตรียมข้อมูลนักแปลก่อนเปิด sprint** (ตามธรรมเนียม K3): `characters_main/side.json`, story context, speaker_map, `translations/glossary.md`, `PRONOUN_MATRIX.md` — freeze ก่อนเปิด sprint
- ตัวละครที่มีคำล็อกแล้ว: **Masaharu Kaito = มาซาฮารุ ไคโตะ** (glossary_gaiden — Kaito รับเชิญในโคลอสเซียม Gaiden)
- ต้องตัดสินใหม่: Yagami, Sugiura, Higashi, Genda, Saori, Hoshino, Kuwana ฯลฯ — glossary priority: K3 > Gaiden > Y8 > Y7 > Pirate > K2R
- ⚠ Issei Hoshino (ทนายใน Judgment) เคยถูกสับสนกับ Ryuhei Hoshino ของ Y7/Y8 มาแล้ว — ระวังตอนทำ characters json

## ข้อควรจำ
- **ทำ Judgment ให้จบก่อน Lost Judgment** — ตัวละครหลักชุดเดียวกัน จบภาคแรกได้ TM+คำล็อกไปใช้ต่อ · โปรเจกต์พี่น้อง: `D:\Projects\lost-judgment-thai` (LJ codename `coyote` ยืนยันแล้ว)
- ธรรมเนียมทีมทุกข้อตาม CLAUDE.md ของ K3: คิดค่า token ก่อนเสมอ (≤120k/batch) · subagent ห้าม spawn ต่อ · ทีมแปล sonnet · lead QC เอง · lead เฝ้า context ตัวเอง (~70% แจ้งผู้ใช้)
- อัปเดตไฟล์นี้ทุกรอบทำงาน
