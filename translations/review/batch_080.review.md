# บันทึกตรวจ QC — batch_080

**ประเภท**: batch ข้อความระบบ/UI ล้วน (message_dialog, option, pause_*, save_data_detail, ui_text, มินิเกม, msg.bin) — 250 keys
**ผลตรวจ**: แก้ 5 จุด แล้วรัน `python scripts/merge_qc.py --dry-run --only 080` → **ผ่าน 250 · คง EN 13 · ตก 0**

## จุดที่แก้ (5 จุด)

### 1. บั๊กจริง — ข้อความหลุด EN 100% (ไม่ใช่ enum/tag ที่ควรคง EN)
`<platform_not=solstice>Quit game and return to desktop?</platform_not><platform=solstice>Are you sure you want to exit the game?</platform>`
เดิม: คำแปลทั้งค่าเป็น EN ล้วน (คัดลอกมาจาก `ref_tm` ที่ก็ทิ้งไว้เป็น EN เหมือนกัน — เป็นความผิดพลาดสืบทอดมาจาก TM ภาคก่อน ไม่ใช่แค่จุดที่ตั้งใจคง EN) ทั้งที่มีข้อความ user-facing จริงอยู่ในนั้น (เทียบกับ "Quit game and return to desktop? Unsaved data will be lost." ที่แปลปกติในไฟล์เดียวกัน)
แก้เป็น: `<platform_not=solstice>จะออกจากเกมและกลับสู่เดสก์ท็อปไหม</platform_not><platform=solstice>แน่ใจหรือไม่ว่าต้องการออกจากเกม?</platform>`
(สอง sentence สอดคล้องกับคำแปลที่ใช้จุดอื่นในแบตช์เดียวกัน: "Quit game and return to desktop?...” → "จะออกจากเกมและกลับสู่เดสก์ท็อปไหม" / "Are you sure you want to exit the minigame?" → แพทเทิร์น "แน่ใจหรือไม่ว่าต้องการออกจาก...") — แท็ก `<platform_not=solstice>`/`<platform=solstice>` คงไว้ไบต์เดิมเป๊ะ

### 2. อักขระพิเศษหาย — trailing space
`"Autosave: ${chapter_title} "` (มี space ท้าย 1 ตัวใน EN ต้นฉบับ) เดิมคำแปล `"ออโต้เซฟ: ${chapter_title}"` ไม่มี space ท้าย → เติม space ท้ายกลับให้ตรงกับต้นฉบับ: `"ออโต้เซฟ: ${chapter_title} "`

### 3. ความสม่ำเสมอศัพท์ UI ภายใน batch — เทมเพลต "Reset to default X settings?"
EN ใช้เทมเพลตเดียวกันซ้ำ 4 ครั้ง (game/audio/brightness/game+excludes) แต่คำแปลเดิมมี 2 โครงสร้างต่างกัน:
- audio/brightness ใช้ "รีเซ็ตการตั้งค่า[X]เป็นค่าเริ่มต้นหรือไม่?" (2 จุด — ไม่แก้ ถูกอยู่แล้ว)
- game (ทั้ง 3 แบบ: เปล่า / Excludes Difficulty / Excludes Difficulty and Autosave) ใช้โครงสร้างอื่น "รีเซ็ตเป็นค่าเริ่มต้นของเกมหรือไม่?" / "รีเซ็ตค่าเกมเป็นค่าเริ่มต้นไหม" (ไม่ตรงกันเองด้วยซ้ำ ทั้งลำดับคำและคำลงท้าย ไหม/หรือไม่)

แก้ให้ทั้ง 3 จุด "game" ใช้แพทเทิร์นเดียวกับ audio/brightness/graphic:
- "Reset to default game settings?" → "รีเซ็ตการตั้งค่าเกมเป็นค่าเริ่มต้นหรือไม่?"
- "Reset to default game settings? (Excludes Difficulty)" → "รีเซ็ตการตั้งค่าเกมเป็นค่าเริ่มต้นหรือไม่? (ไม่รวมระดับความยาก)"
- "Reset to default game settings? (Excludes Difficulty and Autosave)" → "รีเซ็ตการตั้งค่าเกมเป็นค่าเริ่มต้นหรือไม่? (ไม่รวมระดับความยากและบันทึกอัตโนมัติ)"

ตอนนี้ทั้ง 5 entry ของเทมเพลต "Reset to default X settings?" ใช้โครงเดียวกันหมด

## ตรวจแล้วผ่าน (ไม่ต้องแก้)

- **placeholder `${...}`**: ครบทุกจุด ไม่มีสลับ/หาย ตรวจด้วยสคริปต์เทียบ set ของ placeholder ทุก key ระหว่าง EN/TH — 0 mismatch
- **tag `<color=...>` `<symbol=...>` `<platform...>`**: ครบ/ตรงเป๊ะทุกจุด (นอกจากข้อ 1 ที่แก้แล้ว)
- **จำนวน `\n`**: ตรงกับต้นฉบับทุก key
- **U+3000 (ideographic space)**: พบใน 1 จุด (`${save_id}　${chapter_title}`) เป็น placeholder ล้วน ไม่มีเนื้อหาให้แปล คงไบต์เดิมถูกต้อง
- **em dash —**: พบใน 2 จุด ("Failed to save—not enough space." / "Unable to progress — continue...") คงไว้ถูกต้องทั้งคู่
- **อักขระ Latin มีเครื่องหมาย/Cyrillic**: สแกนทั้งไฟล์ไม่พบตัวอักษรนอก ASCII/Thai block เลย (นอกจากลูกศร → ใน placeholder-only string ที่คงไว้ตามต้นฉบับ) — ปลอดภัยจากปัญหาชนกลิฟฟอนต์
- **คง EN 13 จุด (หลังแก้ข้อ 1 จาก 14 เหลือ 13)**: ตรวจทีละจุดแล้วสมเหตุสมผลทั้งหมด — 1 คีย์ enum ภายใน (`yesno`), 1 ชื่อเกม/แบรนด์ (`Judgment`), ที่เหลือ 11 จุดเป็น string ที่มีแต่ placeholder ล้วน (เช่น `${month}/${day}/${year}`, `${hour}:${min}`, `${now}`, `${numer}/${denom}` ฯลฯ) ไม่มีเนื้อหาให้แปลจริง
- **"Yagami is too full to gain SP" (6 จุดที่ใช้ประโยคนี้ประกอบ)**: แปลตรงตัวถูกต้อง สะกด "ยากามิ" ตรงคำล็อก (ก ไม่ใช่ ง) ครบทุกจุด
- **EX Gauge → เกจ EX**: ใช้ตรงกันทุกจุดที่ปรากฏ (9+ จุด) · **SP**: คง EN ทุกจุดตามคำล็อก ไม่มีจุดไหนแปลเป็นไทย
- **ความสม่ำเสมอศัพท์อื่น**: money/points/SP/chips/tags ("You don't have enough X") ใช้แพทเทิร์น "คุณมี X ไม่พอ" ตรงกันทุกจุด · full-inventory pattern ("ซื้อ...ไม่ได้เพราะกระเป๋าเต็ม") ตรงกันทั้ง weapon/armor/item · Save/Load/Saving/Loading ("บันทึก"/"โหลด") ตรงกันทุกจุด
- **ความยาว**: ไม่พบข้อความ TH ที่ยาวเกินสัดส่วนจนน่าเป็นห่วง ปุ่ม/label สั้นแปลสั้นตามต้นฉบับ
- **คำราชาศัพท์**: ไม่พบ

## เทียบกับ master_th.json

ไล่ตรวจศัพท์ UI มาตรฐาน (Cancel/Quit/OK/Yes/No/Back/Next/Close/Help/Select/Settings/Continue/Retry/Skip/Save/Load ฯลฯ) — **ยังไม่มีคำเหล่านี้ merge เข้า master_th.json มาก่อน** (batch นี้น่าจะเป็น batch UI ชุดแรกที่แตะคำเหล่านี้) จึงไม่มีจุดขัดแย้งข้ามภาคให้ตรวจในรอบนี้ — เสนอให้ล็อกคำเหล่านี้เข้า glossary ทันทีที่ merge (ดูหัวข้อถัดไป) เพื่อให้ batch UI อื่นที่ตามมาอ้างอิงได้

## ศัพท์ UI ที่เสนอให้ล็อกเข้า glossary (ยืนยันโดย lead — ไม่ได้แก้เอง)

| EN | ไทยที่ใช้ใน batch นี้ |
|---|---|
| Cancel | ยกเลิก |
| Quit | ออก |
| OK / ok | ตกลง |
| Yes | ใช่ |
| No | ไม่ |
| Back | ย้อนกลับ |
| Next | ถัดไป |
| Close | ปิด |
| Help | ช่วยเหลือ |
| Select | เลือก |
| Settings | ตั้งค่า |
| Saving... / Loading... | กำลังบันทึก... / กำลังโหลด... |
| Save completed. / Load completed. | บันทึกเสร็จสิ้น / โหลดเสร็จสิ้น |
| yen | เยน |

## จุดที่อยากให้ lead ตัดสิน

1. **ลำดับ placeholder วันที่ `${month}/${day}/${year}`** — ไม่ได้สลับเป็น วัน/เดือน/ปี ตามธรรมเนียมไทย เพราะไม่แน่ใจว่า engine ยอมให้สลับตำแหน่ง placeholder ในสตริงนี้ได้จริงหรือไม่ (ถ้าเป็นแค่ format string ที่ substitute ตรงตำแหน่ง การสลับ `${day}/${month}/${year}` ก็ปลอดภัย แต่ถ้ามี logic อื่นผูกกับลำดับ อาจพัง) — คงลำดับเดิมไว้ตามกติกา QC brief ข้อ 1 รอ lead ยืนยันว่าสลับได้หรือไม่ก่อนเปิด batch UI อื่นที่มีวันที่แบบเดียวกัน
2. **`<platform_not=solstice>` / `<platform=solstice>`** — เป็น tag เงื่อนไขแพลตฟอร์ม (solstice น่าจะหมายถึง console เจ้าใดเจ้าหนึ่ง) พบครั้งแรกใน batch นี้ ยังไม่มีคำอธิบายใน glossary/บรีฟว่า tag นี้ทำงานอย่างไร — ถ้ามี string อื่นแบบนี้อีกใน batch ถัดไป ให้ตรวจสอบรูปแบบเดียวกัน (คือ EN ทั้งสองฝั่งแท็กต้องแปล ไม่ใช่ปล่อย EN)
3. **"Clan Creator"** ("Clan Creator victory" → "ชัยชนะใน Clan Creator") และ **"Majima Saga"** — ทั้งสองน่าจะเป็น legacy string จาก engine ร่วม (Judgment ไม่มีเนื้อหา Majima Saga/Clan Creator จริงในเกม) เข้าข่ายเดียวกับที่ lead เคยตั้งข้อสังเกตเรื่อง "Yagami is too full" — ไม่แก้อะไรเพิ่มเติม (แปลไว้เผื่อ string ไม่ถูกเรียกใช้จริง) แต่แจ้งไว้เผื่อ lead อยากเพิ่มเป็นรายการ "legacy string ที่ไม่ปรากฏในเกมจริง" อย่างเป็นทางการ
