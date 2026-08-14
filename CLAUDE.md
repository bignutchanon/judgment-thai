# JETH — Judgment ม็อดแปลไทย

Dragon Engine (รุ่นยุค Y6/Kiwami 2 — PC port 2022 ฐาน PS5 remaster) · codename ภายใน **`judge`** (⏳ ยังไม่ยืนยันจากไฟล์จริง — คาดจากแพเทิร์น `db.<code>.<lang>.par`) · โปรเจกต์ที่ `D:\Projects\judgment-thai`

ระบบทั้งชุดยกมาจากสาย **K2R → Pirate → Y7 → Y8 → Gaiden → K3** — pipeline: **ARMP text + SDF font (donor slot) + SRMM/drop-in**
ภาคต้นแบบใกล้สุดด้านเอนจิ้น/ฟอนต์: **K2R** (`D:\Projects\yakuza-kiwami-2-mod`) — donor Cyrillic U+0400 แบบเดียวกับ K3

เนื้อเรื่อง: ยางามิ ทนายผันตัวเป็นนักสืบ ไขคดีฆาตกรรมต่อเนื่องในคามุโรโจ — ตัวละครที่มีคำล็อกแล้ว: Masaharu Kaito = มาซาฮารุ ไคโตะ (glossary_gaiden)

## สถานะยืนยันแล้ว (research เบื้องต้น 14 ส.ค. 2026 จากโปรเจกต์ K3)
- SRMM/RMM (Parless) **รองรับ Judgment อย่างเป็นทางการ** (Steam เท่านั้น) → loose file ผ่าน `mods/` ใช้ได้
- มีม็อดไทย Google MT อยู่แล้ว: MOD2SUB — https://www.nexusmods.com/judgment/mods/228 — ใช้เป็น proof-of-concept + แกะดูรายชื่อไฟล์ที่เขาแตะได้ **ห้ามใช้เป็น TM** (คุณภาพ MT)
- ⏳ ยังไม่ได้ extract อะไรเลย — เกมยังไม่ได้ติดตั้งในเครื่อง

## อ่านก่อนทำงานทุก session
1. `HANDOFF.md` — สถานะล่าสุด + งานถัดไป
2. `docs/research.md` — ⏳ ยังไม่มี — งานแรกของ research phase คือสร้างจากการ extract จริง
3. `docs/reference/FONT_PLAYBOOK.md` — อ่านก่อนแตะฟอนต์ทุกครั้ง

## ตาราง path
| ชื่อ | ที่อยู่ | กติกา |
|---|---|---|
| PROJECT | `D:\Projects\judgment-thai` | งานทั้งหมดเขียนที่นี่ |
| GAME | ⏳ ยังไม่ได้ติดตั้ง (env `JUDGE_GAME` เมื่อลงแล้ว) | ห้ามแก้/ลบ/ทับไฟล์ใน `runtime/media/data/` · ห้ามเปิดเกมเอง (ผู้ใช้ทดสอบ) · เพิ่มไฟล์ได้เฉพาะโฟลเดอร์ mods + ไฟล์ SRMM |
| K3 | `D:\Projects\yakuza-kiwami-3` | อ่านอย่างเดียว (สคริปต์ pipeline ชุดล่าสุด + thai_encode donor Cyrillic) |
| GAIDEN | `D:\Projects\yakuza-gaiden` | อ่านอย่างเดียว (TM + glossary ใหม่สุดที่ ship แล้ว) |
| K2R | `D:\Projects\yakuza-kiwami-2-mod` | อ่านอย่างเดียว (**ต้นแบบเอนจิ้นรุ่นเดียวกัน** — ฟอนต์/donor/โครง par) |
| Y7 / Y8 / PIRATE | ตาม path ใน CLAUDE.md ของ K3 | อ่านอย่างเดียว |

## ไฟล์เกมเป้าหมาย (⏳ ทั้งหมดรอ verify ตอนติดตั้งเกม)
- ข้อความ: คาด `data/db.judge.en.par` (carrier = EN) → ARMP `.bin` แก้ด้วย `tools/reARMP_fixed.py` (copy จาก K3)
- ฟอนต์: คาด `data/font.judge.par` — **ห้าม copy slot map จากภาคอื่น** — รัน `survey_fonts.py` ก่อนตาม FONT_PLAYBOOK
- ภาษาในเกม: EN/JA (+ zh/ko ผ่านม็อด Retrial) — ตรวจรายชื่อ lang par จริงก่อนเลือก carrier

## กติกาเหล็ก (สืบทอดจาก K3 ทั้งชุด)
1. ห้ามแก้ไฟล์ใน `runtime/media/data/` — deploy ผ่านโฟลเดอร์ mods เท่านั้น ยกเว้นฟอนต์ (ข้อ 5)
2. ห้ามเปิดเกมเอง — การทดสอบในเกมเป็นหน้าที่ผู้ใช้
3. โปรเจกต์เก่าทุกตัวอ่านอย่างเดียว — จะแก้อะไรให้ copy เข้า PROJECT ก่อน
4. คำแปลรวมมีที่เดียว: `translations/master_th.json` เขียนผ่าน `scripts/merge_qc.py` เท่านั้น
5. ฟอนต์ loose ผ่าน Parless ใช้ไม่ได้ (เกมโหลดฟอนต์ก่อน hook) — ทดสอบฟอนต์ต้อง drop-in ทับ font par โดย **backup เป็น `.orig` ก่อนเสมอ**
6. console Windows = cp1252 — ทุกสคริปต์ `sys.stdout.reconfigure(encoding="utf-8")` + เปิดไฟล์ `encoding="utf-8"` · ห้ามส่งข้อความไทยผ่าน CLI args
7. reARMP ใช้ `tools/reARMP_fixed.py` เท่านั้น + path forward-slash
8. ห้ามรันเครื่องมือทีละไฟล์เป็นร้อยรอบ — เขียน loop ลง `scripts/`
9. agent ห้ามเขียนไฟล์ใหญ่ใน Write เดียว — แตก `.part` แล้ว merge
10. license/EULA/credits คงอังกฤษ
11. ห้ามรัน deploy ซ้อนสองตัวพร้อมกัน

## ธรรมเนียมทีม + Pipeline + กฎการแปล
ใช้ตาม CLAUDE.md ของ K3 ทุกข้อ (token budget, lead spawn คนเดียว, sonnet translators, merge_qc 7 เกณฑ์, DENY_BINS, DIALOG_TOKEN_RE ฯลฯ) — สคริปต์ port จาก K3 (แทนที่ bis→judge) และ **ค่า game-specific ต้อง verify กับไฟล์ Judgment จริงตอนใช้ครั้งแรก**
- glossary ลำดับความสำคัญ: **K3 > Gaiden > Y8 > Y7 > Pirate > K2R** (ใหม่กว่าชนะ) — ตัวละครฝั่ง Judgment (Yagami, Sugiura, Higashi, Genda ฯลฯ) ยังไม่เคยถูกล็อกในโปรเจกต์ไหน ยกเว้น Kaito — ตัดสินใน `translations/glossary.md` ก่อนเปิด sprint
- บทเรียนที่จ่ายแพงมาแล้ว: ดูหัวข้อเดียวกันใน CLAUDE.md ของ K3 + `docs/reference/FONT_PLAYBOOK.md` (copy มาแล้วในโปรเจกต์นี้)
