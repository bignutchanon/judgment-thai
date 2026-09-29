# HANDOFF — Judgment ม็อดแปลไทย (JETH)

> **🔜 งานถัดไป (อัปเดต 29 ก.ย. 2026 รอบบ่าย)**
> 1. **รอเจ้าของดูจอ — แบนเนอร์แข่งโดรน** (รอบที่สอง/รอบสุดท้าย/ถูกตัดสิทธิ์/หมดเวลา · `patch_drone_lap_banner.py`) · ถามแล้ว เจ้าของ "ยังไม่ได้ดู" · ถ้ายังไม่กลางแถบ ปรับ `-(30 + 1.68 x ฟอนต์)` / ขนาดฟอนต์ในสคริปต์ แล้ว `--write` + คัดลอก + SRMM `-s`
> 2. **เกลาบท 1 ✅ เจ้าของเล่นผ่าน · บท 2 เสร็จ + deploy แล้ว (148 คีย์ · db 159/159) รอเจ้าของเล่นบท 2** — `docs/polish_plan.md` §10 · ถัดไป: บท 3 (`make_polish_chunks.py --chapter 3` · 2 ชิ้น → 4 ตัว: findings_01/02 (A) + 51/52 (B)) · เดิม: — สรุปใน `docs/polish_plan.md` §9 · 531 คีย์ · เจ้าของตัดสิน: lead ตัดสินทั้งหมด/เจ้าของตรวจในเกม · ชิ้นละ 2 ตัว · เก็นดะ→ยากามิ = เธอ · ฮัตโตริ = ผม/คุณ ประชด · (lead) ชินทานิ→ยากามิ = นาย · ถัดไป: รับจุดที่เจ้าของเจอในเกม → แก้ตรง → เริ่มบท 2 (`make_polish_chunks.py --chapter 2` · บท 2 ชิ้นเดียว → 2 ตัว) · ยังไม่ถาม: รอบออกรุ่น (§8 ข้อ 5)
> 3. **กวาดอังกฤษ §2.1 เสร็จ + deploy แล้ว (db 159/159 ตรงบิลด์) รอเจ้าของดูจอ**: `is_translatable` เก็บ `I...`/`I-I...` + ป้ายลงท้าย `:` · batch `ENSWEEP` 6 คู่ (คือ... · ค-คือ... · คะแนน: · ความยาก: · เงิน: · บท:) · แก้ done 6 คู่ (Flight → การบิน · OFF → "ปิด" · เอิร์ธแองเจิล · แฟ้มคดี · เอ็ม ไซด์ คาเฟ่ ×2) · master 50,303 คู่ · **"Quit game…" คงอังกฤษ** (Win32 MessageBox ไม่ใช้ฟอนต์เกม · batch_WINDLG — แจ้งเจ้าของแล้ว) · ด่าน: wrap 0 · คำเบิ้ล 0 · เพศ 0 · check_inplace 158/158 + font.bin · preview ผ่าน
> 4. ก่อนแพ็ก release ถัดไป: ถอด `mods/Easy picking thumbturn` + `mods/EasyThumbturnTolerance` (ของส่วนตัวเจ้าของ) · `drone_play.bin` ใน build/ui จะติดไปกับ release (ต้องผ่านการดูจอก่อน)
> · หมายเหตุ support: เจ้าของเจอ "เคอร์เซอร์เมนูเบิ้ล กดทีเดียวเลื่อนสองที" — ไม่ใช่ม็อด (ม็อดไม่มีไฟล์ input) · เครื่องเจ้าของ: จอ 144 Hz + `graphics.ini` v_sync=1 fps_cap=0 + จอย Xbox ผ่าน Bluetooth (Windows เห็นเป็น XINPUT + HID สองตัว) · แนะนำ: ล็อก 60 fps → ปิด Steam Input เฉพาะเกม → เสียบสาย · ยังไม่ได้ผลทดสอบกลับมา

> **เกลาบทเนื้อเรื่องหลักทีละบท — วางแผน + เตรียมของแล้ว ยังไม่เริ่ม (29 ก.ย. 2026 · เจ้าของสั่ง "วางแผนกับเตรียมของก่อน ยังไม่ต้องเริ่มทำ")** · แผนเต็ม `docs/polish_plan.md` (ขอบเขต 13 บท 20,440 บรรทัด 27 ชิ้น · ขั้นตอนต่อบท · ต้นทุน · **เรื่องที่เจ้าของต้องตัดสิน 5 ข้อ**) · ของที่เตรียม: `scripts/make_polish_chunks.py` (ตัดชุดงานรายบท · `--stats`) · `translations/review/polish/POLISH_BRIEF.md` (บรีฟ + ตัวอย่างเทียบมาตรฐาน 7 ข้อจากบท 1) · `translations/review/polish/context/` (เรื่องย่อ 13 บท + ทะเบียนเพศ ย้ายจาก build/gender ที่ถูก gitignore + อัปเดตคำเจ้าของ) · `scripts/polish_report.py` (รวมผล + ตรวจกติกา + เตือนเพศ/ใช้ร่วม/คำล็อก + เขียนผู้พูด) · ชุดงานบท 1 สร้างแล้ว `polish/ch01/` · apply ใช้ `apply_sweep_findings.py --dir polish/chNN` ของเดิม · **+ กวาดอังกฤษที่แปลไม่ครบ** (เจ้าของสั่งเพิ่ม · "บางประโยคเจอ I..."): สาเหตุ `extract_all_en.is_translatable` ต้องมีละติน ≥ 2 ตัว + คำเดียวลงท้าย `:` = identifier → "I..." "I-I..." "Score:" "Chapter:" ไม่เคยเข้าคิว · `scripts/find_english_leftovers.py` (ใหม่ · เดินจากไฟล์เกม) → `translations/review/english/report.md`: A ตกคิว 26 (เห็นจริง ~9) · B อังกฤษปน 30 คำ · C คงอังกฤษทั้งบรรทัด 312 (ส่วนใหญ่รหัส/ชื่อเกม) · ชุดงานเกลาติดป้าย [ยังไม่แปล]/[ไม่มีใน master]/[มีอังกฤษ] + หมวด E · แผนข้อ 2.1 (คีย์ใหม่ → batch เสริม ENSWEEP แบบ UICAPS · ยังไม่แก้อะไร) · ⏳ **รอเจ้าของตัดสิน** (เริ่มบทไหน · โมเดล · ความลึก · ระดับการตรวจ · รอบออกรุ่น · ทำกวาดอังกฤษก่อนไหม)

> **หลัง v1.2.1 (29 ก.ย. 2026) — เจ้าของส่งภาพแข่งโดรน: "คำว่ารอบที่สองมันตกกรอบ"** · แถบมืดกลางจอ (obi · y 206-277 ที่ 1080p) ว่าง ส่วน "รอบที่สอง" ตัวเล็กไปนอนใต้แถบ (หมึก y 279-298) · ต้นทาง `ui.judge.en.par/en/scene/drone_play.bin` ตารางย่อย `lap_info_text` แถว `second`/`final` (ui_text.bin แถว 686 "Second Lap" / 685 "Final Lap") = ข้อความฟอนต์สไปรต์ (col47 = 0 · กล่อง 1200x60 pivot กลาง · สเกล 0.7 · col81 ช่องไฟ +4) → ไทย fallback ไปฟอนต์ปกติแล้วถูกวางที่ pos.y + pivot.y (ขอบล่างกล่อง) กลไกเดียวกับหัวข้อเมนูโดรนรอบ 20 · ภาพที่สอง "ถูกตัดสิทธิ์" (ui_text 704-706 · element `retire` text1-3) อาการเดียวกัน (แถบ y 480-598 · หมึก 605-647) → `scripts/patch_drone_lap_banner.py --write` (ใหม่) ครอบ 3 แบนเนอร์: lap_info_text second/final (ฟอนต์ 30) · retire text1-3 + count_down_time_limit text1-3 ("หมดเวลา" 676-678 · ยังไม่มีภาพแต่โครงเดียวกัน · ฟอนต์ 36) · col11 pos.y = -(30 + 1.68 x ฟอนต์) (เงา text1 คง +3) · col47 0 → ฟอนต์ · col81 ช่องไฟ → 0 (กันมาร์กเยื้อง) · โมเดลจาก fit สองภาพ: UI อ้างอิง 1600x900 (x1.2 ที่ 1080p) · ฟอนต์ตั้งต้นตอน col47 = 0 ≈ 18.5 · ขอบบนเซลล์ = pos.y + pivot.y + 0.78 x ฟอนต์ · 48 ไบต์ · decode กลับต่าง 24 เซลล์ตามตั้งใจ (จาก 628,672) · คัดลอกไฟล์เดียวเข้า `mods/JudgmentThai/ui.judge.en/en/scene/` + `ShinRyuModManager -s` (ไม่ได้รัน deploy_spoil เต็ม) · ⏳ **รอเจ้าของดูบนจอ** (เกมเปิดค้างตั้งแต่ 9:40 ต้องเปิดใหม่) · ยังไม่ได้แพ็ก release
> · ของเล่นส่วนตัวของเจ้าของใน `mods/` ตอนนี้ (ไม่ใช่ของม็อด — **ถอดก่อนแพ็ก/ก่อน deploy_spoil** เพราะ SRMM โหลดทุกโฟลเดอร์): `Easy picking thumbturn` (Nexus #307 · bin แบบ reARMP rebuild) + `EasyThumbturnTolerance` (ผ่อน tolerance ใน `minigame_lock_picking_thumbturn_constant_value.bin` · patch ในที่)

> **release v1.2.1 (28 ก.ย. 2026) — เจ้าของเปิดเกมดูแล้วสั่ง "release ได้"** · แก้คำแปลอย่างเดียว (ตีหก · คำเบิ้ล 215 ข้อความ · มาจอง ฮัง — ดูบรรทัดถัดไป) · v1.2.0 มียอดโหลด 10 จึงออกเลขใหม่แทนแพ็กทับ · `package_release.py --version 1.2.1` → `release/JudgmentThai-th-v1.2.1.zip` (12,338,426 B · md5 `0f94dd26c2694499dc48a353d98b0029` · 327 ไฟล์) · **เทียบกับ zip v1.2.0: ชุดไฟล์เหมือนกันทุกชื่อ ต่างแค่ db 22 bin + README/mod-meta (เลขรุ่น)** · ฟอนต์/ui ไม่เปลี่ยน · ไฟล์ mod ใน zip ตรงกับที่ deploy (เว้น mod-meta.yaml ที่มีเลขรุ่น) · notes `release/notes-v1.2.1.md` · `patch.md` → v1.2.1 (games.ts + ร่างข่าว 4.7 รวมของ v1.2.0) · commit + แท็ก v1.2.1 + `gh release create --latest` · **ถัดไป**: ส่ง `patch.md` ให้ `yakuza-wiki`

> **หลัง v1.2.0 (28 ก.ย. 2026) — เจ้าของสั่ง "แก้คำแปลแปลก ๆ เช่น ตีหก กับคำเบิ้ล (เจ้าหน้าที่ที่)"** · `scripts/fix_doubled_words.py` (ใหม่ · กฎ old→new ~160 ข้อ แก้ที่ done แล้ว remerge) · **เวลา**: ตีหก ไม่มีในภาษาไทย (ตีใช้แค่ 1-5 นาฬิกา) → หกโมงเช้า 7 บรรทัด (คดีคุเมะ · "ระหว่างตีสองถึงหกโมงเช้า") · "2-3 นาฬิกา" → ตีสองถึงตีสาม · "sewer o'clock" แปลใหม่ · **คำเบิ้ล**: ที่ที่/สถานที่ที่/พื้นที่ที่/ที่ที่เกิดเหตุ ~70 (เจ้าหน้าที่ที่รีบไป → ตำรวจที่รีบไป · ที่ที่ผมเคยทำงาน → ที่ผมเคยทำงาน ฯลฯ) · คนคน (คนคนนั้น/คนคนเดียวกัน → คนนั้น/คนเดียวกัน) · ขอบคุณคุณ ~30 (→ ต้องขอบคุณ / ยกความดีให้) · ติดหนี้บุญคุณคุณ · ชื่อลงท้าย -นะ + นะ (มัตสึกาเนะนะ · โชโนะนะ · ชนะนะ) · อื่น ๆ (สิบสิบหนึ่ง → 10-10-1 · คู่มือมือ → ตารางมือไพ่ · ลูกมือมืออาชีพ · ผู้เสียชีวิตเสียชีวิต · กับกับดัก · ให้ให้ · ข้าวของของ · คุณภาพภาพ · ไอ้หนุ่มใหญ่โตโตเกียว → ไอ้หนุ่มโตเกียวจอมกร่าง) · รวม 215 ข้อความ · คงไว้ตั้งใจ: คำซ้ำที่ EN ซ้ำเอง (โอเค โอเค · ไม่ ไม่ ไม่) · ขอขอบคุณ (ทางการ) · ทุกคนคนละ · มีมีด · **`fix_doubled_words.py --check` ต้องได้ 0 ก่อน deploy** (สแกน master หา ตีหก-ตีสิบ + คำเบิ้ลชุดนี้) · QC: remerge ตก 0 · wrap 0 (TALK_062 เรียงใหม่แทนตัดกลาง "คน หนึ่ง") · gender 0 · `build_text --clean` 157 · `gen_font_bin` ผิดคาด 0 · `check_inplace_bins` 158/158 · preview ผ่าน · deploy แล้ว db 159/159 ตรง build · เจ้าของเปิดเกมดูแล้ว → ปล่อยเป็น v1.2.1 · **มาจอง han = ฮัง** (เจ้าของสั่ง 28 ก.ย. 2026 · เดิมปน "สองฮัง" กับ "1 ฮัน"): กฎท้าย `normalize_terms.RULES` 2 ข้อ (ตัวเลข/${value} + ฮัน · ฮัน/ฟุ) ผ่าน `fix_owner_terms.py --write` → master 5 บรรทัด (batch_080 · 099) + docs/side_content_context_judge.md · **ไม่แตะ honorific คันไซ -han = ฮัน** (docs/reference/rgg_universe_context.md) · ฮันนีแทรป/ฮันนีมูน ไม่โดน · บิลด์/check/deploy ซ้ำแล้ว db 159/159 ตรง build

> **หลัง v1.2.0 (28 ก.ย. 2026) — เจ้าของส่งภาพ CASE FILE: แท็บ "ภารกิจ / คดีหลัก / คดีเสริม" ตัวอักษรเบียดซ้อน** · ไม่ได้เกิดจากงานฟอนต์รอบนี้: พยัญชนะในป้ายเหมือน v1.1.4 ทุกพิกเซล (cp เดิม · advance เดิม · ความกว้างรวมเท่าเดิม) และป้ายไทยแคบกว่า EN (คดีหลัก 112 vs "Main Case" 161 px atlas) จึงไม่ใช่การบีบให้พอดีกล่อง · วัดจากภาพ: "คดีหลัก" กว้าง 51 px แต่ควรเป็น 66 px (ฟอนต์ 22) · **สาเหตุ: ตาราง scene ของ UI col81 = ช่องไฟระหว่างตัวอักษร (int8 มีเครื่องหมาย · 254 = -2 · 255 = -1)** — แท็บ CASE FILE (`pause_todo_judge.bin` / `text` ฟอนต์ 22 กล่อง 220x30) = -2 หักทุกตัวอักษร รวมมาร์กและเซลล์ตัวนำ → คดีหลัก 8 ตัว ≈ -15 px ตรงกับที่วัด · (โน้ตเก่าใน `patch_drone_menu_titles.py` ที่เดาว่า col81 = โหมดฟอนต์ภาพ น่าจะผิด — ค่า 2/4/6 ที่โดรนคือช่องไฟบวก) · `scripts/patch_ui_tracking.py --write` (ใหม่): col81 ติดลบ → 0 เฉพาะ element ข้อความ (ข้ามชื่อ num/time/nom · ฟอนต์ 0 · มินิเกมตีเบสบอล -5) = 18 element ใน 9 ไฟล์ (pause_todo · pause_item · pause_map · pause_skill · pause_complete · pause_album · pause_crowdkanpa · pause_map_sugoroku · smartphone) · แก้ต่อจากไฟล์ใน build/ui ถ้ามีอยู่แล้ว · ไบต์อื่นเท่าต้นฉบับ · deploy แล้ว (mismatch 0 · แจ้ง session ce/f4 ก่อน-หลัง) · ⚠ เกมเปิดอยู่ตอน deploy (PID 29680) ต้องเปิดใหม่ · ✅ เจ้าของเปิดเกมดูแล้วผ่าน → สั่ง release เป็น v1.2.0 (แพ็กซ้ำ · ดูบรรทัด release ข้างล่าง)

> **release v1.2.0 (28 ก.ย. 2026) — เจ้าของสั่ง "release ให้หน่อย"** · รวมงานรอบ 24 (ลูกพี่ · ไอ้ตัวตุ่น · ไอ้ปากดี) + รอบ 25 (Sarabun · วางมาร์กตามฟอนต์ · ญ ฐ ไม่มีเชิง · ระยะบรรทัด +24/+12) + การ์ด/ป้ายรูปภาพไทย 119 ใบ · **เจ้าของตัดสินใจ (ถามตอนแพ็ก)**: ใส่ป้ายรูปภาพ **ทั้งที่ยังไม่มีใครเห็นบนจอ** (ตำแหน่งตัวละคร 18 · telop 24 ยังเป็นร่าง) · ระยะบรรทัด = เห็นบนจอแล้ว โอเค · เลขรุ่น 1.2.0 · แก้ก่อนแพ็ก: `·` → ` / ` ในคำอธิบายหลักฐาน Chatter ของฮาจิทานิ (batch_095 · atlas เกมวาด U+00B7 เป็น ÷ · master เหลือ `·` 0) · เครดิต README เพิ่ม Taviraj (ฟอนต์บนป้ายภาพ) · ตรวจก่อนแพ็ก: `build_text --clean` 157 · `gen_font_bin` ผิดคาด 0 · `check_inplace_bins` 158/158 (+font.bin) · `test_slot_alloc` 12/12 · wrap/gender 0 · deploy แล้ว (เกมเปิดอยู่ตอน deploy → ต้องเปิดเกมใหม่) · **zip ตรง build ทุกไฟล์**: db 159 · ui 157 (font 3 · scene 35 · dds 119) · ฟอนต์ 2 · `release/JudgmentThai-th-v1.2.0.zip` (12.3 MB = 12,338,470 B · md5 `14ed23f4816cd3164e44f6c0ab7015b2` · 327 ไฟล์ — **แพ็กซ้ำ 28 ก.ย. ~02:00 โดย session 5a ใส่ตัวแก้ช่องไฟแท็บ CASE FILE** ตามที่เจ้าของทดสอบผ่านแล้วสั่ง release เป็น 1.2.0 · zip เดิม 11,962,419 B / md5 c26da4d3… ยอดโหลด 0 จึงแทนที่ใน release เดิม + ย้ายแท็ก v1.2.0 ไปคอมมิตใหม่) · notes `release/notes-v1.2.0.md` · `patch.md` → v1.2.0 (games.ts + ร่างข่าว 4.6) · `font/candidates/` เข้า .gitignore · session คู่ขนาน (5a · f4) ถูกขอให้หยุด build/deploy ระหว่างแพ็ก · **ถัดไป**: ส่ง `patch.md` ให้ `yakuza-wiki` · รอผู้เล่นยืนยันป้ายรูปภาพ (Parless โหลด .dds loose จาก ui par ได้จริงไหม · เลขบท · ตัวเส้นขอบ) · เจ้าของอนุมัติข้อความร่างใน `caption_cards.json`

> **การ์ดชื่อบท + การ์ดแนะนำตัวละครเป็นไทย (28 ก.ย. 2026 · session คู่ขนานกับรอบ 25) — deploy แล้ว รอเจ้าของดูจอ**
> · research: ข้อความบนการ์ด "Chapter 01 / Three Blind Mice" และ "LAWYER AT… / ISSEI HOSHINO" **เป็นรูปวาดสำเร็จ** ไม่ใช่ฟอนต์ — `ui.judge.en.par/en/texture/caption_chapter_judge_NN.dds` (1024x256 · บนทึบ/ล่างเส้นขอบ) · `caption_chapter_judge.dds` (ป้าย Chapter ใช้ร่วม) · `caption_chapter_numNN_judge.dds` (เลข · บท 13 = ป้าย Final Chapter) · `caption_character_<ชื่อ>.dds` 23 ใบ (ชื่อ/ตำแหน่ง ทึบ+เส้นขอบ · เงา glow อบในรูป) · พื้นหลังควันคือ `chapter_sequence.usm` ใน movie.par (CRI CPK ไม่ใช่ PARC) · texlist หั่นตัวเส้นขอบเป็นชิ้นตามตัวอักษร EN (แถว EN: บท = 3 · ตัวละคร = 2)
> · `scripts/make_caption_cards.py --write` (ใหม่) → 38 dds (ขนาด/header ตรงต้นฉบับ) + scene บท 1-12 แก้ col10 ของ `num_0` 70 → 9..13 (4 ไบต์/ไฟล์ แก้ในที่) ให้ "บทที่ 01" อยู่กลางจอ · ฟอนต์ Taviraj · ขึ้นรูปด้วย HarfBuzz · ชื่อบท = กึ่งกลางขนาดเต็ม (ไม่หลบช่องชิ้นเส้นขอบ — `--chapter-safe` ถ้าต้องหลบ) · ชื่อตัวละคร = หลบช่อง (โฮชิโนะตัวเล็กเพราะช่องชื่อต้นแคบ · `--allow-cut` = ตัวใหญ่) · พรีวิว `build/preview/caption_cards/` (`chapter_cards.png` = การ์ดเต็มใบเทียบ EN)
> · ข้อความ: ชื่อบท/ชื่อคนจาก master · **ตำแหน่งตัวละคร 18 ข้อความใน `translations/caption_cards.json` = ร่าง รอเจ้าของอนุมัติ** · deploy 28 ก.ย. (deploy_spoil ปกติ · ui.judge.en 56 ไฟล์ ตรง build ทุกไฟล์ · MLO มีไฟล์ใหม่)
> · **+ ป้ายชื่อศัตรูตอนเริ่มต่อสู้ 57 ใบ** (`bc_eb_*` 800x100 ชิดขวา · `bc_sb_*` 1000x200 กลาง/สองบรรทัด "ตำแหน่ง + ชื่อ") — เป็นรูปเหมือนกัน (caption.bin `name_texture_id`) · ข้อความจาก `message` ของ caption.bin ผ่าน master (แยก "ชื่อ, ตำแหน่ง" ตามจุลภาค) · 2 ใบที่ caption.bin ไม่มีข้อความอยู่ใน `caption_cards.json` → `battle_overrides` · แสงเรืองส้ม fit จากต้นฉบับ · บิลด์ใหม่จาก master ล่าสุด + **deploy แล้ว 28 ก.ย.** (ui.judge.en 124 ไฟล์ ตรง build ทุกไฟล์ · MLO 284 ไฟล์) รอเจ้าของดูจอ
> · **+ ป้ายสถานที่/เวลาในคัตซีน 24 ใบ** (`telop_<ฉาก>.dds` 1920x120 ชิดขวา x 1798 · เงาดำ gauss sigma 5 x2) — ข้อความไม่มีในไฟล์เกม → `caption_cards.json` หัวข้อ `telops` (ร่าง · ศาลเขตโตเกียว/ห้องเยี่ยมญาติ ตาม Lost Judgment · ที่เหลือตาม master/glossary) · deploy แล้ว 28 ก.ย. (ui.judge.en 148 ไฟล์ · MLO 308)
> · ⏳ ต้องดูบนจอ: (1) Parless โหลด .dds loose จาก ui par ได้จริงไหม (scene loose ยืนยันแล้ว แต่ texture ยังไม่เคย) (2) เลข 01 ขยับตามจริงไหม — ถ้าแอนิเมชันทับตำแหน่ง จะเห็น "บทที่   01" ห่าง → คืนป้ายชิดขวาเดิม (3) ตัวเส้นขอบตอนแอนิเมชันเผยตัวอักษรขาดรับได้ไหม

> **รอบ 25 (27 ก.ย. 2026) — เจ้าของแจ้ง: ข้อความสองบรรทัด สระล่างบรรทัดบนชนสระบน/วรรณยุกต์บรรทัดล่าง ("อยู่" เหนือ "นั้น")**
> · **สาเหตุ (วัดจาก atlas)**: อังกฤษกินที่ -25..+6 px รอบเส้นฐาน (ตัวมีหมวก -33) · ไทย -44..+11 (วรรณยุกต์ซ้อนเหนือสระบน · ุ ู) = สูงกว่าอังกฤษ ~1.7 เท่า แต่ระยะบรรทัดของเกมตั้งไว้สำหรับอังกฤษ · จำลองสองบรรทัดที่ระยะ 44 px (ซับคัตซีน ถ้าสมมติฐานข้างล่างถูก) ได้ภาพชนแบบเดียวกับที่เจ้าของเห็น · เจอบั๊กแถม: วรรณยุกต์ชั้นบน (hlevel 1) ล้นขอบบนเซลล์ (y < 0) ถูก clamp ลงมาแตะสระ — นี้ ชี้ ครื้น ซึ้ง (้ ของ นี้ ติด ี)
> · **แก้ 1 — ระยะบรรทัด (⏳ สมมติฐาน รอเจ้าของดูจอ)**: `scripts/patch_line_spacing.py --write` (ใหม่) — ตาราง scene ของ UI 121 คอลัมน์ · **col84 (1 ไบต์) = 8** เฉพาะข้อความเนื้อเรื่อง + template บางตัว (เมนูไตเติล/ตัวเลือก/popup — ดู `--scan`) ที่อื่น 0 → น่าจะเป็นระยะบรรทัดเพิ่ม (เมนูไตเติล col84 = 8 ไม่มีขอบหนาในภาพจริง จึงไม่น่าใช่ความหนาขอบ) · บวก +12 px atlas: `telop.bin` text/text_talk/text_memories 8→20 · `message_window_judge.bin` text_talk/text_message 8→18 (ไบต์เปลี่ยน 3+2 · ที่เหลือเหมือนต้นฉบับ) · ส่งเป็น loose `mods/JudgmentThai/ui.judge.en/en/scene/` · ถ้าได้ผล: พิจารณาขยายไปกล่องหลายบรรทัดที่ col84 = 0 (dialog/tutorial) ด้วย
> · **แก้ 2 — ย่อมาร์ก**: `title_encode.MARK_SCALE = 0.89` + `glyph_ppem()` (มาร์กทั้งคลาสวาดเล็กลง ไม่ใช่ normalize รายตัว) · `slot_alloc`: ที่กันให้สระบนคิดจากกลิฟจริง (`TONE_BEARERS`) แทนค่าคงที่ 12 · `LOWER_GAP` 2→1 · ผล: ไทย -43..+10 · วรรณยุกต์ชั้นบนไม่ถูก clamp แล้ว (เหลือ ๊ ตัวเดียว) · การจัด cp ไม่เปลี่ยน (ตรวจแล้ว ทุกเซลล์ข้อความ/ชนิด/variant เดิม) · ⚠ ย่อมาร์กอย่างเดียวไม่พอ (ที่ระยะ 44 ยังชิด) — ตัวแก้หลักคือข้อ 1
> · บิลด์: `slot_alloc --write` · `test_slot_alloc` 12/12 · atlas+italic · `build_text --clean` 157 · `gen_font_bin` ผิดคาด 0 · `check_inplace_bins` 158/158 (+font.bin) · wrap/gender 0 · **deploy 23:40 รอเจ้าของดูจอ** (ดูซับคัตซีน + กล่องคุยที่ขึ้นสองบรรทัด: บรรทัดห่างขึ้นไหม · ถ้าไม่ห่าง = col84 ไม่ใช่ระยะบรรทัด → ถอยข้อ 1 แล้วหาคอลัมน์อื่น) · ยังไม่ commit/แพ็ก
> · ลำดับบิลด์เพิ่ม `patch_line_spacing.py --write` ต่อจาก `patch_drone_menu_titles.py --write` (CLAUDE.md แก้แล้ว)
> · **เทียบฟอนต์ต้นแบบ (เจ้าของถาม "ลองฟอนต์อื่นนอกจาก Sarabun")**: `scripts/compare_fonts.py` (ใหม่) สลับ `title_encode.THAI_TTF` แล้วรันสายผลิตจริงในหน่วยความจำ (ไม่เขียน slotmap/atlas) → `build/font/compare/{looped,loopless}.png` + `summary.md` · ฟอนต์ OFL 13 ตัวที่ `font/candidates/` (+ OFL_*.txt · variable font instance เป็น static แล้ว) · ตัวเด่น: **Noto Sans Thai Looped Condensed** (มีหัว · บรรทัดสั้นลง 15% · สูง -41..+11 · เส้น 94% ของอังกฤษ) และ **Noto Sans Thai Condensed** (ไม่มีหัว · สั้นลง 15% · สูง -39..+7 เตี้ยสุด = ชนบรรทัดน้อยสุด) · Kanit/Prompt/Plex Medium หนาเกินอังกฤษ 20-35% · ⏳ รอเจ้าของเลือก — ถ้าเปลี่ยน: ตั้ง `THAI_TTF` (หรือ `paths.SARABUN_TTF`) แล้วรันสายบิลด์เต็ม (cp ไม่เปลี่ยน แต่ advance/ตำแหน่งมาร์กเปลี่ยนทั้งชุด)
> · **เจ้าของเลือก Noto Sans Thai Looped Condensed → เปลี่ยนแล้ว + deploy (รอดูจอ)**: `paths.THAI_TTF` = `font/NotoSansThaiLooped-Condensed.ttf` (+ `font/OFL_NotoSansThaiLooped.txt`) · `title_encode.THAI_TTF` อ่านจากตัวนี้ (`SARABUN_TTF` ยังอยู่ให้ inject_thai_judge/sdf ตัวเก่า) · เครดิตใน README ของ `package_release.py` ใช้ `paths.THAI_FONT_NAME` แล้ว · ⚠ ถ้ายืนยันใช้: แก้เครดิต Sarabun ใน `patch.md` (บรรทัด 72/184) + `release/nexus_upload.txt` ด้วยมือ · ppem 38 · ชั้นความกว้าง [8,13,15,19,23] · test 12/12 · `check_inplace_bins` 158/158 · wrap/gender 0 · preview ผ่าน · ถ้าเจ้าของไม่ชอบ: ตั้ง `THAI_TTF` กลับเป็น Sarabun แล้วรันสายบิลด์เต็ม
> · **28 ก.ย. เจ้าของขอลอง Taviraj → เปลี่ยน + deploy แล้ว (รอดูจอ · Noto ที่ deploy ก่อนหน้ายังไม่มีใครเห็นบนจอ ถูกแทนที่)**: `paths.THAI_TTF` = `font/Taviraj-Regular.ttf` (serif · มีหัว · OFL-Taviraj.txt) · ppem 39 · สูง -43..+11 เท่า Sarabun · **บรรทัดยาวกว่า Sarabun ~10%** (กว้างกว่า Noto Condensed ~29%) → ซับอาจตัดขึ้นบรรทัดใหม่บ่อยขึ้น · เจอบั๊กแฝง: ink กว้างเกิน 30 px (ฒ 32 · ณ 31) ล้นเซลล์ 32 px ที่เริ่มวาด x=2 → ขอบขวาถูกตัด + R ติดลบ (`test_slot_alloc` 1g ตก) → เพิ่ม `title_encode.render_glyph()` บีบแนวนอนเฉพาะตัวที่เกิน `MAX_INK_W = 30` (≤15% ตามกฎรอบ 8-9 · Sarabun/Noto ไม่มีตัวเกิน = ผลเดิมทุกพิกเซล) · slot_alloc + inject ใช้ตัวนี้ร่วมกัน · test 12/12 · `check_inplace_bins` 158/158 · wrap/gender 0 · ภาพเทียบทุกฟอนต์ `build/font/compare/{looped,loopless,serif}.png`
> · `preview_line.py` แก้แล้ว: อังกฤษ/สัญลักษณ์เคยใช้ advance ประมาณ 14 px ทุกตัว → "[X]" "(100%)" ดูเบียดทั้งที่ในเกมปกติ · ตอนนี้อ่าน (L, R) เดิมจาก `extracted/db_en/en/font.bin.json` (คู่ 5-6) = ช่องไฟเดียวกับเกม
> · **28 ก.ย. เจ้าของแจ้ง "ไม้เอกลอยออกจากสระ อี" → มาร์กวางตามฟอนต์ต้นแบบแล้ว + deploy (รอดูจอ)**: เดิมวางสระบน/วรรณยุกต์ **กึ่งกลาง ink ฐาน** แต่ฟอนต์ไทยวาง **ชิดขวา** (สระเหนือเสาขวา · วรรณยุกต์ซ้อนอยู่ปลายขวาของสระ) → ่ ไปอยู่กลาง ี ห่างหางสระ (ที่ นี่ กี้ สิ่ง) · `scripts/mark_anchor.py` (ใหม่) shape ฐาน+มาร์ก (และฐาน+สระบน+วรรณยุกต์) ด้วย HarfBuzz จากฟอนต์ต้นแบบที่ ppem เดียวกัน วัด off = ขอบขวามาร์ก − ขอบขวาฐาน · `slot_alloc.anchor_classes()` แบ่งชั้นฐานตาม off ของ ิ (เฉพาะพยัญชนะ+ฤฦ ถ่วงด้วยความถี่คู่ฐาน-มาร์ก · ฐานเก็บชั้นที่ `mclass` · `SlotMap.wclass_of` ใช้ mclass ก่อน) · place ของแต่ละ variant = ค่าเฉลี่ยถ่วง off − ความกว้างมาร์กของเรา − RSB (ยึดขอบขวา เพราะมาร์กถูกย่อ) · วัดไม่ได้ → ถอยไปกึ่งกลางแบบเดิม · Taviraj: ชั้น ปฝฟ / ษ / ขฃฉชซฐฒธนรวศสห / ที่เหลือ (ชั้นที่ 5 ว่าง) · ภาพเทียบกับ HarfBuzz ตรงแนวนอนทุกคำที่ลอง (ที่ นี่ ปี่ ศักดิ์ ต้อง กี้ สิ่ง ฟื้น น้ำ คุ้ม) · test 12/12 · `check_inplace_bins` 158/158 · wrap/gender 0 · deploy 00:07 (ui.judge.en 56 ไฟล์ รวมการ์ดของ session คู่ขนาน — ไฟล์เดียวกับที่ session นั้น deploy ไว้)
> · **ญ ฐ ไม่มีเชิงเมื่อมีสระล่าง (เจ้าของทัก กตัญญู ู ทับเชิง ญ)**: `title_encode.LESS_BASES = "ญฐ"` + `render_less()` เอากลิฟจาก GSUB ของฟอนต์ (shape ญ+ุ → Taviraj `yoYingthai.less`/`thoThanthai.less` · ฟอนต์ไม่มี → ตัดหมึกใต้เส้นฐาน) · slot_alloc เพิ่มเซลล์ฐาน variant `"less"` 2 เซลล์ (ใช้ 156 · เหลือ 25) · `SlotMap.encode` มอง ahead: ญ/ฐ ที่ตัวถัดไปเป็น ุ ู ฺ → ใช้เซลล์ less · decode ได้ตัวเดิม (round-trip ผ่าน) · test 1d รวม variant ในคีย์แล้ว · ⚠ master ปัจจุบันมี ญ/ฐ + สระล่าง **0 ครั้ง** (กตัญญู มีแค่ในประโยคทดสอบ) = กันไว้ล่วงหน้า · ฎ ฏ + สระล่าง (ฟอนต์ใช้ .short + ุ.small) ยังไม่ทำ — master 0 ครั้งเช่นกัน · deploy 00:2x ตรง build ทุกไฟล์ (mismatch 0)
> · **เจ้าของสั่งกลับเป็น Sarabun (คงการวางมาร์กตามฟอนต์ + ญ ฐ ไม่มีเชิง + ระยะบรรทัด) → deploy แล้ว**: `paths.THAI_TTF = SARABUN_TTF` · Sarabun มี `yoYingthai.less`/`thoThanthai.less` เหมือนกัน · แก้บั๊ก `anchor_classes`: edges ของ `width_classes` ปัดด้วย int() เข้าหาศูนย์ พอใช้กับค่าติดลบชั้นติดกันถูกรวม (Sarabun เหลือใช้ 3 จาก 5 ชั้น) → เลือกชั้นจากตัวแทนที่ใกล้สุดแทน · ชั้น Sarabun: ปฝ / ฟษ / งฉชซฐณธภรศสฬฮ / กขฃค…อ / ฆญพม · ภาพเทียบ HarfBuzz ตรงทุกคำ · test 12/12 · `check_inplace_bins` 158/158 · wrap/gender 0 · mismatch 0 · ⚠ **ตอน deploy เกมเปิดอยู่** (Judgment.exe) — ฟอนต์ในหน่วยความจำยังเป็นชุด Taviraj แต่ bin ข้อความเป็นชุด Sarabun → ต้องปิดเกมเปิดใหม่ก่อนดูผล · เครดิต README กลับเป็น Sarabun อัตโนมัติ (`THAI_FONT_NAME`)
> · **28 ก.ย. เจ้าของ: Sarabun อ่านง่ายกว่า · บรรทัดยังซ้อน อยากให้ห่างกว่านี้** (เกมเปิด 00:36 หลัง patch +12 อยู่ใน mods ตั้งแต่ 23:40 = เห็น +12 แล้วยังไม่พอ หรือ col84 ไม่ใช่ระยะบรรทัด — ยังแยกไม่ได้) → `patch_line_spacing.py` เปลี่ยน TARGETS เป็นรายการ (ชื่อ, ขนาดฟอนต์, col84 เดิม, px ที่เพิ่ม): ข้อความเนื้อเรื่อง **+24** (telop 8→32 · message_window 8→28) · กล่องหลายบรรทัดอื่น +12 (snack_telop · question_text · popup_window(_new) · common_dialog_message(_large) · common_window_dialog · common_dialog_tutorial · info_dialog · tips · tutorial fs24) = 13 ไฟล์ · ⏳ ถ้าเจ้าของเห็นว่าไม่ห่างขึ้นเลย = col84 ไม่ใช่ระยะบรรทัด → ถอยทั้งชุดแล้วหาทางอื่น (ย่อความสูงไทย / หาคอลัมน์อื่น) · ⚠ deploy 00:44 ชนกับ session `judgment-thai-7d` ที่ rebuild build/text พร้อมกัน (แก้ master ด้วย `fix_owner_terms.py`) → ในเกมมี db 9 ไฟล์เก่ากว่า build · ไม่ deploy ซ้ำ (กติกา 11) · 7d deploy ปิดท้าย 00:47 (เกมปิดอยู่) → ตรวจแล้วฟอนต์ + db 159 + ui ตรง build ทุกไฟล์ (mismatch 0) · ข้อความในเกมตอนนี้ = ของ 7d (ลูกพี่ · ไอ้ตัวตุ่น · ไอ้ปากดี) + ฟอนต์/ระยะบรรทัดของรอบนี้
> · เจอระหว่างทาง: atlas ต้นฉบับของเกมวาด **U+00B7 `·` เป็นรูป `÷`** → master มี 1 บรรทัด (คำอธิบายหลักฐานหน้า Chatter ของฮาจิทานิ "…Don Quijote · 10 นาทีก่อน…") จะขึ้น ÷ ในเกม — ยังไม่แก้ (ต้องผ่าน done → merge_qc) · ควรเพิ่มกฎ QC ห้าม `·` ในคำแปล

> **รอบ 24 (27-28 ก.ย. 2026) — คำสั่งเจ้าของ: aniki → ลูกพี่ · the Mole → ไอ้ตัวตุ่น · แก้ "smart ass"** · **the Mole**: ไส้ศึก → **ไอ้ตัวตุ่น** 288 บรรทัด (ชื่อ JA モグラ = ตัวตุ่น ยากามิตั้งเพราะคนร้ายมุดหายใต้ดิน — ไส้ศึก มาจากความหมาย "สายลับ" ของ EN และสปอยล์ว่าคนร้ายเป็นคนใน · "หาตัว/จับตัว the Mole" ยุบเป็น หา/จับไอ้ตัวตุ่น) · คำยาวขึ้น 4 ตัว → `fix_thai_wrap --write` 34 ข้อความ · ⚠ LJ ใช้ ไส้ศึก 1 จุด ("The Mole") ต้องตามแก้ตอนทำ LJ · สคริปต์เปลี่ยนชื่อ `fix_aniki.py` → **`scripts/fix_owner_terms.py`** (คำเก่าใน TERMS · กฎจริงอยู่ท้าย normalize_terms.RULES) · ⚠ **ชนกับ session ฟอนต์คู่ขนาน**: build_text รอบ Mole ใช้ slotmap ใหม่ของอีก session (00:40:53 · Sarabun + font-anchor) · deploy ของสอง session ทับช่วงเดียวกัน → deploy ซ้ำตอน 00:47 แล้วตรวจ md5: db 159/159 · atlas 2/2 · ui 67/67 ตรง build · เลิกทับศัพท์ "อานิกิ" (ตาม K3) ทั้งเกม: ติดชื่อ = ลูกพี่+ชื่อ (ลูกพี่ไคโตะ/ลูกพี่ฮิงาชิ) · A-Aniki = ล-ลูกพี่ · EN "Kaito-aniki" 6 บรรทัดที่เคยแปล "พี่ไคโตะ" ปรับเป็น ลูกพี่ไคโตะ ด้วย → `scripts/fix_owner_terms.py --write` (ดึงเฉพาะกฎ aniki 3 ข้อที่เพิ่มท้าย `normalize_terms.RULES`) · done 16 batch · master 41 บรรทัด · อานิกิ เหลือ 0 · glossary/PRONOUN_MATRIX/characters_main/CLAUDE.md แก้ตาม · "What was that, smart ass!?" (sound_auth ฉากดอรายากิ — ตอบมุกประชดของยากามิ) ไอ้เก่งเกิน → **ไอ้ปากดี** · "...ya smart ass!" (TALK_013) ไอ้เจ้าเล่ห์ → ไอ้ปากดี · ⚠ กับดัก: `remerge_stale --write` เคยจะ merge batch_080 ที่ done ยังเป็นไทยของคีย์ `Quit game...` (MessageBox Windows ต้องคง EN) → sync done ให้เป็น EN ตาม master แล้ว · ⚠ `normalize_terms.py --write` แบบทั้งโปรเจกต์ยังมีกฎเก่าค้างเสนอ ~16 จุดใน done (คนโด/คนจัง/โรค อัลไซเมอร์/พินฟุ ฯลฯ) — ยังไม่ได้ตรวจว่าจริงหรือ false positive (regex `คนโด(?!ะ)` อาจชน คนโดน) ห้ามรันรวดโดยไม่ดู · บิลด์ `build_text --clean` 157 · `gen_font_bin` ผิดคาด 0 · `check_inplace_bins` 158/158 (+font.bin) · wrap/gender check 0 · preview ผ่าน · **deploy แล้ว รอเจ้าของดูจอ · ยังไม่แพ็ก release/commit**

> **รอบ 23 (15 ก.ย. 2026) — บั๊กผู้เล่น v1.1.3 "not responding ทุก ~30 นาที" → เปลี่ยนตัวเขียนไฟล์ทั้งชุดเป็น "patch ในที่" (พอร์ตจาก Gaiden/Y8) · บิลด์+deploy 22:13 · **เจ้าของสั่ง release ทันที (ไม่รอทดสอบ)** → แพ็ก v1.1.4 22:22 · GitHub release v1.1.4 · commit รอบนี้ (ดู git log)**
> · **รายงาน** (ชีต `bug_logs` 15/9 15:06 · v1.1.3 · หมวด เกมค้าง/เกมเด้ง · ไม่ระบุฉาก ไม่มีภาพ/เซฟ · สเปกบอกแค่ "เกมส์ Ver 1.12" · ติดต่อกลับ safeee24@gmail.com):
> "หลังลง mod ไทย ตัวเกม not responding เองตลอด ทุก ๆ ประมาณ 30 นาที · ทดสอบก่อนลง mod เล่นยาวเกิน 3 ชม. ไม่มีปัญหา" (Judgment.exe ของเราเป็น file version 1.0.0.12 = "1.12" น่าจะหมายถึงตัวนี้)
> · **ตรวจฝั่งเราแล้วปกติ**: `fix_thai_wrap --check` 0 · `fix_dialogue_gender` 0 · `YakuzaParless.ini` ไม่มีอะไรทำงานเป็นรอบ (RebuildMLO/Reloading/Log ปิดหมด) · Event Log เครื่องเราไม่มี Application Hang/Error ของ Judgment.exe ใน 45 วัน
> · ฟอนต์ drop-in ขนาดเท่าต้นฉบับ (393,344 B = BC4 เดิม) · loader ที่แจก = SRMM 4.8.3.0 exe + Ultimate ASI Loader 6.6.0 + YakuzaParless.asi (16 พ.ค. 2026) · ความยาวสตริงไทย (ไบต์) สูงสุดต่อตารางอยู่ในระดับเดียวกับ EN (manual 2,814 vs 2,627)
> · **research เว็บ (agent · Steam/Nexus/GitHub/PCGW/Reddit ผ่าน jina+cookie age-gate)**: "Ver 1.12" = แพตช์ Steam ล่าสุด (29 มี.ค. 2023 · โชว์บนไตเติล) = ผู้แจ้งใช้ Steam ปกติ · เกมใช้ Denuvo · อาการเดียวกันเป๊ะเคยถูกแจ้งใต้ม็อด **Judgment Retrial** (SRMM/Parless เหมือนเรา · Nexus 203 · ธ.ค. 2023 "after some time the game just goes not responding… 30 minutes or even 2 hours") แล้วผู้แจ้งคนนั้นสรุปเอง 2 ม.ค. 2024 ว่า "It was a game issue not a mod issue" · กระทู้บั๊กทางการมี "Judgment is not responding" ในเกมต้นฉบับ (2022-2024) และ ส.ค. 2026 โทษไดรเวอร์ NVIDIA 616.56 ("rollback is the only way") · SRMM/RMM/Parless ไม่มี issue เรื่องค้างเป็นรอบเลยใน 4 ปี · MOD2SUB ปิดคอมเมนต์ (bugs 2 รายการ ไม่มีค้าง)
> → สรุป 2 ผู้ต้องสงสัย: (A) เลย์เอาต์ bin ที่ reARMP ประกอบใหม่ (ของเรา — แก้แล้วรอบนี้) · (B) เกม/ไดรเวอร์ (vanilla 3 ชม. ของผู้แจ้งเป็นตัวอย่างเดียว) — ต้องให้ผู้แจ้งลอง v1.1.4 + ตอบคำถามท้ายบล็อก
> · **round-trip bin ที่ ship ทั้ง 159 ไฟล์** (สคริปต์ scratchpad `roundtrip_all.py`): ค่าที่ไม่ใช่สตริงเท่าต้นฉบับทุกเซลล์ **แต่ไฟล์ที่ reARMP ประกอบใหม่มีเลย์เอาต์ต่างจาก SEGA**: main table ย้ายไป 0x20 (ต้นฉบับ controller_guide อยู่ 0xD260) · ขนาดต่าง (controller_guide 59,024 → 55,232 B) · TEXT_COUNT dedup 19 bin · `SPECIAL_FIELD_INDICES` งอกศูนย์ท้ายใน complete / complete_group / shop (44 ตารางย่อย) / verification_todo_item / minigame_photo_shooting_mission_todo_item
> → **ตรงกับบทเรียนที่ Y8 (20 ส.ค.) และ Gaiden (21 ส.ค. · CLAUDE.md ข้อ "ไฟล์ bin ต้องสร้างด้วย patch ในที่") พิสูจน์ในเกมแล้ว**: ไฟล์ที่ reARMP ประกอบใหม่ทำเกมค้าง/เด้งที่จอสอนปุ่มครั้งแรกของมินิเกม (`controller_guide.bin`) แม้ rebuild เป็น EN ล้วน · ผู้เล่นยืนยันหายหลังเปลี่ยนเป็น patch ในที่
> = สาเหตุที่น่าจะเป็นที่สุดของรายงาน 15/9 และย้อนไปอธิบายรายงาน 7/9 (VR Dice & Cube ค้างตอนเล่นครั้งแรก — รอบ 22 เคยตัดสินว่าเป็นบั๊กเกมต้นฉบับ ต้องทบทวน) · JETH ใช้ reARMP rebuild ทั้ง 159 bin มาตั้งแต่ v1.0 (22 ส.ค.) ก่อนบทเรียนนี้ถูกจดใน Gaiden 1 วัน
> · **ทำแล้ว (โค้ด)**: `scripts/patch_text_inplace.py` (พอร์ต Gaiden · เดินทุกตาราง/ตารางย่อยชนิด 9 · ต่อสตริงท้ายไฟล์ + แก้เฉพาะ text offset table · รับ mapping ที่ `SlotMap.encode()` แล้ว · `--selftest all` = **157 bin ผิดคาด 0** — decode เทียบต้นฉบับทีละเซลล์ 459,757 เซลล์ใน talk.bin)
> · `scripts/check_inplace_bins.py` (ไบต์ในช่วงความยาวเดิมต้องเท่าต้นฉบับยกเว้น text offset table · selftest 3/3: ไฟล์ดีผ่าน · ไบต์แปลกจับได้ · ไฟล์ v1.1.3 จับได้) · `build_text.py --builder inplace|rebuild` (**ค่าเริ่มต้น inplace** · `SKIP_VALUES = {message_dialog.bin: [ok]}` กัน identifier ชนิดกล่องข้อความ · rebuild เก็บไว้เทียบเท่านั้น)
> · `gen_font_bin.py` patch float ในที่ลง kerning_table ของ meta_ot_cond_book@0x20 + italic@0x2FB0 (+ ตรวจกลับทุกครั้ง: 1,848 เซลล์ ผิดคาด 0 · ไบต์ต่าง 6,950 ≤ 7,392 · ขนาดเท่าเดิม 26,048 B) · `--rebuild` = วิธีเดิม
> · **บิลด์**: `build_text.py --clean` 157 bin 1.8 วินาที ล้มเหลว 0 · `gen_font_bin.py` · `check_inplace_bins.py` **158/158 ผ่าน** (+font.bin ยกเว้น ตรวจในตัวเอง) · round-trip JSON ของ build: struct 0 · TEXT_COUNT 0 · ต่างเฉพาะสตริง + kerning · `test_slot_alloc` 12/12 · `test_qc_tools` 14/14 · **deploy 22:13** (db 159 · ui 4 · MLO)
> · ขนาด mods โตขึ้นเพราะ pool อังกฤษเดิมคงอยู่ (talk 2.96→4.86 MB · sound_auth 1.64→3.12 MB · auth 0.37→0.67 MB) — Gaiden เจอแบบเดียวกัน ไม่มีผลกับเกม
> · **release v1.1.4**: `package_release.py --version 1.1.4` → `release/JudgmentThai-th-v1.1.4.zip` (9.3 MB = 9,349,944 B · md5 `f7aafb76a831f770803ca32d4521ed1c` · 174 ไฟล์ · 159 bin + ui 4 · ต่างจาก v1.1.3 เฉพาะ bin 158 + README/mod-meta) · `check_inplace_bins.py --dir release/JudgmentThai-th-v1.1.4/files/JudgmentThai/db.judge.en/en` 158/158 ผ่าน · notes `release/notes-v1.1.4.md` · `patch.md` อัปเป็น v1.1.4 (games.ts + ข่าว 4.5 + หัวข้อ 3) · GitHub: https://github.com/bignutchanon/judgment-thai/releases/tag/v1.1.4
> · **ถัดไป**: (1) ปล่อยแล้วโดยยังไม่มีใครทดสอบบนจอ — เจ้าของ/ผู้เล่นทดสอบ v1.1.4: เล่นต่อเนื่อง >1 ชม. · ใช้เซฟใหม่/เซฟที่ยังไม่เคยเล่นมินิเกม เข้ามินิเกมให้จอสอนปุ่มขึ้น (ดาร์ท/โป๊กเกอร์/VR Dice & Cube/โดรน) · เปิดร้านค้า + หน้า completion + evidence
> (2) ส่ง `patch.md` ให้ `yakuza-wiki` (games.ts v1.1.4 + ข่าว 4.5) · ถ้าผู้เล่นยืนยันหาย → ปิดเคส 7/9 + 15/9 และแก้ memory VR · ถ้าไม่หาย → ผู้ต้องสงสัย (B) เกม/ไดรเวอร์ ไล่ตามคำถามท้ายบล็อก
> (3) ตอบผู้แจ้ง safeee24@gmail.com (ร่างอยู่ท้ายบล็อกนี้) — ขอให้ลอง v1.1.4 ก่อน ถ้ายังค้าง: bisect ลบ `mods\JudgmentThai` ทิ้งฟอนต์ไว้ · ส่ง Event Viewer (Windows Logs → Application → Application Hang · Judgment.exe) + `srmm_log.txt` + สเปก/ที่เก็บเกม + ม็อดอื่นใน `mods\`
> (4) ทบทวน memory/บันทึก VR Dice & Cube 7/9 หลังผลทดสอบ (ถ้า v1.1.4 หาย = เคสเดียวกับ Gaiden poker/blackjack ไม่ใช่บั๊กเกมต้นฉบับ)
> · **ร่างคำถามถึงผู้แจ้ง** (ส่งหลังปล่อย v1.1.4): ① ตอนค้างกำลังทำอะไร (เดินในเมือง/คัตซีน/ต่อสู้/เมนู/หน้าโหลด) ② ค้างแล้วกลับมาเองไหม หรือต้องปิด ③ ลงด้วย install.bat ใช่ไหม · ในโฟลเดอร์ `runtime\media\mods` มีอะไรบ้าง ④ Event Viewer มีรายการ Application Hang ของ Judgment.exe ไหม (ส่งภาพ) ⑤ สเปก CPU/GPU/RAM · เกมอยู่ SSD หรือ HDD · Steam แท้อัปเดตล่าสุด ⑥ เซฟ (โฟลเดอร์ `Documents\SEGA\Judgment` หรือ Steam userdata) ถ้าสะดวก

> **รอบ 22 ปิด (7 ก.ย. 2026) — apply ผล register + blind แล้ว · บิลด์+deploy 11:06 · commit `36f9e65` · release v1.1.3 แล้ว 11:10** (เจ้าของสั่ง "blind test ผ่านแล้ว release เลย ที่เหลือให้ user แจ้งมาเอง")
> · `release/JudgmentThai-th-v1.1.3.zip` (8.3 MB · md5 `fed8bbb838748fe0787303216d63e221` · 159 bin + ui 4) · notes `release/notes-v1.1.3.md` · GitHub release v1.1.3 asset ขึ้นแล้ว (ยืนยันด้วย `gh release view`) · `patch.md` อัปเป็น v1.1.3 พร้อมข่าวสำหรับ yakuza-wiki
> · register ชิ้น 01 ยิงใหม่ (sonnet ~300k token) = 11 finding (L 9 · V 2) → รวม 6 ชิ้น 81 finding (high 69) · ผู้พูด ? ระบุได้ high 1,705 · med 1,482 · low 389 · เหลือไม่รู้ 78
> · `register_report.py --write` → `translations/speech_speakers/*.json` (พากย์ 3 ตาราง) + `build/gender/cinema_low_R.json` → `merge_cinema_low.py --write` (ตัดสินแล้ว 283 · ข้าม low 24)
> · **คำตัดสิน lead register**: `apply_sweep_findings.py --dir register --mid --reject-ids R02-0171,R02-0172,R04-0946-0949,R04-0378 --write` → **รับ 45** (L 39 · V 3 · G 1 · H 1 · N 1) / 16 batch
> ปฏิเสธ 7: ตัด "คุง" ของเก็นดะ (2) · มัตสึกาเนะดุไคโตะ กู/มึง (4 · §3 รุ่นพี่→รุ่นน้อง) · R04-0378 "Um... Yagami-san?" ใช้ของ blind (กลางเพศ "เอ่อ...ยากามิซัง?" เพราะคีย์ใช้ร่วม) · S 28 จุดไม่มีคำแก้ (ข้อมูลผู้พูดเข้า speakers แล้ว)
> · lead แก้ th_new เอง 1 จุด: R04-0039 ยากามิ→ฮามุระ "ว่ะ" → "มากกว่ามั้ง" ให้เข้ากับ ผม/นาย
> · **blind**: แทน th_new 4 จุดตามที่ตัดสิน (B02-0106 "ฮิฮิ!" · B03-0990 "เอ่อ...ยากามิซัง?" · B04-1142 "นี่ รับไปเลย" · B01-0904 "เรื่องของกู!") + เขียน `review/blind/findings_06.json` (lead 6 จุดจากตรวจเชิงกล:
> B01-0717 ยากามิ ผม · B01-1217/1218 "รับ|ว่าความ" ย้ายช่องว่าง · B01-1224 "ของ|คุณ" · **B01-0706/0709 ฮัตโตริ คุณ→มึง ให้ T3 ทั้งฉาก a01_120** (เดิม "ดูบริบท" — lead ตัดสินเอง) · B01-1221 ฮามุระ "หัวหน้ากู" คงไว้ (แทร็กคู่ 1220 ก็ กู)
> → `--dir blind --mid --reject-ids B02-1345,B03-1041,B03-1449 --write` = **รับ 26** / 15 batch
> · `make_dialogue_gender.py --write` (รู้เพศ 41,342 · +speech +mahjong) → `fix_dialogue_gender.py --write` **9 บรรทัด** (ชินทานิ/ยากามิ/rouge_boy/ฮิราซาวะ คะ→ครับ 6 · Club Sega Employee ครับ→ค่ะ 3 — RE_KHA ใหม่จับคำถาม "คะ" ได้แล้ว)
> · แก้มือเพิ่ม 3 บรรทัด (batch_051/062): ซุกิอุระ "เขาอยู่นั่นไงคะ" 2 แทร็ก → ครับ (**fixer ไม่จับ คะ กลางประโยค** — ตาราง "ขัดกัน" เห็นแต่สคริปต์ไม่เสนอ) · rouge_boy "คุณซาโอริซัง" → "ซาโอริซัง"
> · ตาราง "ขัดกัน" ที่เหลือหลังแก้ = ผลลวง: "คาดคะเน" (มี คะ) + pause_message/talk `mixed` ที่ยากามิเป็นผู้พูดจริง (ผม ถูกแล้ว)
> · QC: `remerge_stale` ค้าง 0 · `merge_qc` ผ่าน 50,315 ตก 0 · `fix_thai_wrap --check` 0 · `fix_dialogue_gender` 0 · `test_qc_tools` 14/14 · `test_slot_alloc` 12/12
> · บิลด์ `--clean` 157 bin ล้มเหลว 0 · `gen_font_bin` 26,064 B · strip_ui (donor 3/36) · patch_drone · **deploy 11:06** (db 159 ไฟล์ · ui · MLO)
> · **ถัดไป**: (1) รอรายงานผู้เล่นบน v1.1.3 (ชีต `bug_logs`) — จุดที่ควรถูกยืนยัน: ชินทานิ "ต้องการอะไรหรือครับ?" บท 1 · ยากามิกับฮามุระ "นาย" ใน a02_020 · ฮัตโตริ a01_120 มึงทั้งฉาก · โคโรเนียง Dice & Cube
> (2) ค้างเดิม: (8) บท 2 ซับหาย "ยินดีที่รู้จักครับ" ไม่มีภาพ · run ไทยคั่นด้วย "..."/"!" ยังไม่วัดรวม (รอหลักฐานจอ)
> (3) ถ้าทำ register/blind บท 4-13: ชิ้น ~600 บรรทัด · ไม่ให้ agent เขียน speakers ทุกบรรทัด · เพิ่ม "คะ กลางประโยค" ให้ `fix_dialogue_gender`

> **รอบ 22 ต่อ (7 ก.ย. 2026 สาย) — ทีม "เติมเพศ + ตรวจสรรพนาม/ระดับภาษา บท 1-3 + VR" (เจ้าของเลือกขอบเขต B) · สถานะตอนเขียน: ทีม 12 ตัว
> ส่งแล้ว 11 · **ยังรัน register ชิ้น 01 ตัวเดียว** (ผลจะโผล่ที่ `translations/review/register/speakers_01*.json` + `findings_01.json` — ถ้า session ใหม่ไม่เห็นไฟล์นี้ ให้ยิง agent ใหม่
> ด้วย prompt เดิม: บทบาท/อินพุต/เอาต์พุตตาม `translations/review/register/REGISTER_BRIEF.md` · ชิ้น chunk_01.tsv 1,200 บรรทัด · sonnet) · ยังไม่ commit · ยังไม่บิลด์**
> · ชิ้น 02 = 18 finding (L 14 · H 2 · G 1 · N 1) ผู้พูดครบ 1,050 — ชินทานิใช้ ฉัน/แก กับยากามิในฉากกลุ่ม 7 จุด (กติกา: ฉัน เฉพาะสองต่อสอง) · คู่สนทนาเรียกยากามิ "แก" → "นาย"
> · **คำตัดสิน lead ล่วงหน้าเพิ่ม**: H ที่เสนอตัด "คุง" จาก "ยากามิคุง" ของเก็นดะเพราะ EN ไม่มี honorific (R02-0171/172) = **ปฏิเสธ** (เสียง JA เก็นดะเรียก 八神くん · PRONOUN_MATRIX §2 ให้ ยากามิคุง)
> · **ทำแล้ว (ข้อมูล)**: talk.bin ผู้พูด unknown 22 ชื่อ → `build/gender/talk_overrides_P1-3.json` → `merge_speaker_overrides --write` + `make_talk_speaker --write` (ทะเบียน 134 ชื่อ · ชาย +10 หญิง +2 กลาง +1 · ที่พิสูจน์ไม่ได้คง unknown)
> · คัตซีน 255 แถว low/unknown ใน 52 ฉาก → `make_cinema_low_work.py` (C1/C2) → ทีมตัดสิน → `merge_cinema_low.py --write --override` (รับ 230 แถว · แก้ผู้พูดเดิม 3 แถว: a04_020 r31 Hamura→Shioya · a12_030 r10/r11 → Sugiura/Shono · a10_020 r11 → Yagami · a06_010 r9-10 → Tashiro)
> · มาจอง 26 คน → `translations/mahjong_npc_gender.json` (เว็บไม่มีข้อมูล · รับชาย 2 จากฉายา King/Strongman · หญิง 4 จากชื่อตัว+โทน · ที่ทีมเดาชายจากนามสกุล 6 คน lead ลดเป็น low)
> · `check_speaker_gender.RE_KHA` ตัด `(?<![ก-ฮ])` (จับ "ไหมคะ/หรือคะ" ได้แล้ว · test_qc_tools 14/14) · `fix_line_gender.SKIP_VOICERS` เพิ่ม seiya_girl1-3 (ตารางบอกชาย ที่จริงแฟนสาว)
> · `make_dialogue_gender.py` เพิ่มแหล่ง `speech` (`translations/speech_speakers/<ตาราง>.json` จากทีม register) + `mahjong` → รันแล้ว: รู้เพศ 41,283 (+416) · `fix_dialogue_gender` เสนอ 10 บรรทัด **ยังไม่เขียน** (รอ apply finding ทีมก่อน กันทับ)
> · glossary บรรทัด King Koro-nyan แก้เป็น ราชาโคโระเนียง (ตรงกฎ normalize + master 22 จุด · ชิ้น 06 ชี้)
> · **ผล register ที่ได้แล้ว**: ชิ้น 03 = 28 finding (S 24 ป้าย seiya_girl · L 3 · H 1) ผู้พูดครบ 869 · ชิ้น 04 = 15 (L 10 · S 3 · G 1 · V 1) · ชิ้น 05 = 9 (L 7 · S 1 · V 1) · ชิ้น 06 = 0
> แพตเทิร์น: ยากามิหลุด ฉัน/กู/มึง นอกวงเล็บ (a02_020 กับฮามุระ 5 จุด · c03 2 จุด) · อายาเบะฉากสายข่าวหลุด "ฉัน" 4 จุด · **คำตัดสิน lead ล่วงหน้า**: มัตสึกาเนะดุไคโตะด้วย กู/มึง (R04-0946-0949) = อนุญาตตาม §3 รุ่นพี่→รุ่นน้อง → ปฏิเสธ
> · อายาเบะฉาก L'Amant ใช้ "ผม" ทั้งฉาก ~60 บรรทัด = คงไว้ (สม่ำเสมอ ไม่แก้เป็นชุดใหญ่บนการตีความกฎ)
> · **token ใช้ไป ~2.5M** (register ชิ้นละ 300-400k · คัตซีนชิ้นละ ~300k) เกินประมาณการ 1.5M — รอบหน้าถ้าจะทำบท 4-13 ให้ตัดชิ้นเล็กลง (~600 บรรทัด) และไม่ให้ agent เขียน speakers ทุกบรรทัด
> · **ถัดไป (ทำตามลำดับ หลังชิ้น 01-02 ส่ง)**: (1) `python scripts/register_report.py --write` → `translations/review/register/report.md` + `speech_speakers/*.json` + `build/gender/cinema_low_R.json`
> (2) `python scripts/merge_cinema_low.py --write` (3) lead อ่าน report.md ตัดสิน → `python scripts/apply_sweep_findings.py --dir register --write` (+ `--mid-ids`/`--reject-ids` · finding ใช้ฟิลด์ sev แทน conf — shim ใส่แล้ว)
> (4) `python scripts/remerge_stale.py --write` (5) `python scripts/make_dialogue_gender.py --write` → `python scripts/fix_dialogue_gender.py --write` → `remerge_stale.py --write`
> (6) blind test: `python scripts/apply_sweep_findings.py --dir blind --write --mid` หลังแทน th_new 4 จุดด้วยของ lead (B02-0106 "ฮิฮิ!" · B03-0990 "เอ่อ...ยากามิซัง?" · B04-1142 "นี่ รับไปเลย" · B01-0904 ใช้ถ้อยคำรอบ 21 คง `<font_kind>`) และ `--reject-ids B02-1345,B03-1041,B03-1449`
> (7) QC: `merge_qc.py` ตก 0 · `fix_thai_wrap.py --check` 0 · `fix_dialogue_gender.py` 0 · `test_qc_tools.py` (8) บิลด์: `build_text.py --clean` → `gen_font_bin.py` → `strip_ui_sprite_slots.py --write` + `patch_drone_menu_titles.py --write` → `deploy_spoil.py` (9) อัปเดต HANDOFF + commit (ยังไม่แพ็ก release จนเจ้าของทดสอบ)

> **รอบ 22 (7 ก.ย. 2026 เช้า) — เช็คบัคผู้เล่น + blind test รอบแรก (ยังไม่แก้คำแปล · ยังไม่ commit):**
> · **บัคใหม่ 1 รายการ** (ชีต `bug_logs` 7/9 03:44 · v1.1.2 · บท 3 VR Paradise "เกมค้างแต่ยังรัน" · มีวิดีโอ 202 วิ + ภาพ):
> ดึงเฟรมวิดีโอมาดูแล้ว = Dice & Cube ทอยเต๋าได้ 2 แล้วหมากค้าง "เหลืออีก 2 ช่อง" ในอุโมงค์ >60 วิ · โคโรเนียนพูดวนได้ · Esc เมนูพักขึ้น
> → **น่าจะเป็นบั๊กเกมต้นฉบับบน PC ไม่ใช่ม็อด**: round-trip bin ที่ ship ทั้ง 159 ไฟล์ (สคริปต์ชั่วคราวใน scratchpad) bin ที่ VR ใช้
> (`msg/talk/ui_text/sugoroku_event_rule/random_slot_item`) ต่างจากต้นฉบับเฉพาะข้อความ + TEXT_COUNT dedup · tag/placeholder ทั้ง master ตรง ·
> กระทู้บั๊กทางการ Judgment บน Steam (716 โพสต์) มีรายงาน Paradise VR crash/ค้าง "ทำอะไรไม่ได้" ซ้ำ ๆ ตั้งแต่ปี 2022 ถึง ส.ค. 2026 (แนะลดกราฟิก + ล็อก 60 fps)
> · ผู้แจ้งไม่ทิ้งช่องทางติดต่อ → ถ้าตอบให้ขอ: ทดสอบซ้ำโดยถอนม็อด · ลดกราฟิก/60 fps · ส่งเซฟ+สเปก · ข้อสังเกตข้างเคียง: reARMP เติมศูนย์ต่อท้าย
> `SPECIAL_FIELD_INDICES` ใน `complete/complete_group/shop/photo_shooting_mission_todo_item/verification_todo_item` (ship มาตั้งแต่ v1.0 ไม่มีรายงาน)
> · **blind test รอบแรก (เจ้าของสั่ง "ลอง blind test" = ทีมอ่านไทยล้วนไม่เห็น EN)**: `scripts/make_blind_chunks.py` → `translations/review/blind/chunk_01-05.tsv`
> (บทนำ + บท 1-3 คัตซีน/พากย์/บทพูดเดิน + Dice & Cube ทั้งหมด = 5,897 บรรทัด · 256k อักษร · มีผู้พูด+เพศ · `[อีกแทร็ก]` = ซับอีกภาษาเสียง) ·
> บรีฟ `BLIND_BRIEF.md` หมวด U/N/T/P/R/S/F · ทีม sonnet 5 ตัว **ใช้ token ~1.1M (≈240k/ชิ้น 1,400 บรรทัด — สูงกว่าประมาณการ 2.4 เท่า เพราะไทยกิน token)**
> · ผลทีม 25 จุด (high 9) คะแนนอ่านลื่น 4-4.5/5 · **แต่ lead สุ่มอ่านเอง 120 บรรทัดเจอ 6 จุดที่ทีมไม่จับเลย (recall 0%)** — ทีมจับ typo/เพศผิด/ชื่อแปลกได้ดี
> แต่ปล่อยผ่านการผสมระดับสรรพนามในฉาก (มึง↔คุณ) และช่องว่างผ่าคำประสม (รับ|ว่าความ) เพราะบรีฟสั่งไม่ให้จดช่องว่างขอบวลี · ชิ้น 05 ผู้อ่านนับหัวตาราง id เลื่อน 1 (แก้แล้ว)
> · `scripts/blind_report.py` → `report.md` + `findings_all.json` (แนบ EN/ผู้พูด · สอบเทียบ · ตรวจเชิงกล 3 แบบ: ช่องว่างผ่าคำในพจนานุกรม (pythainlp — ผลลวงเยอะ ตัดแล้วเหลือ 4)
> · ยากามิพูด ฉัน (เจอ B03-0621) · ผสม กู/มึง กับ ผม/ครับ ต่อฉาก (0)) · **คำตัดสิน lead ใน `lead_verdicts.json`: รับ 27 · ปฏิเสธ 3 · ดูบริบท 2** —
> ปฏิเสธเพราะคำแปลถูกแต่ **ป้ายเพศข้อมูลผิด** (`voicer_gender.json`: seiya_girl2=male · alpes_boy=female → ต้องแก้ข้อมูล) และ "Shirosaki-sensei" แปลตามกฎ
> · ⚠ `fix_dialogue_gender` ไม่จับ B01-1211 "ต้องการอะไรหรือคะ?" (คิว shintani ชาย) — **สาเหตุ: `check_speaker_gender.female_markers` ดูแค่ RE_KHA (ค่ะ)
> ไม่รวมคำถาม "คะ"** → ผู้พูดชายลงท้ายคำถามด้วย คะ หลุดทั้งเกม (ยังไม่แก้ รอเจ้าของสั่ง — ถ้าเพิ่ม คะ ต้องกันคำอย่าง "คะแนน") · **ถัดไป**: เจ้าของตัดสินว่าจะเขียน 27 จุดที่รับลง done
> (ใช้ `apply_sweep_findings.py` ได้ถ้าชี้ไป `review/blind` + ใช้ th_new ของ lead แทนของทีมใน 4 จุดที่ระบุ) · ถ้าจะทำ blind รอบสอง ให้ปรับบรีฟด้วยตัวอย่างสอบเทียบ 6 จุด + เพิ่มผู้พูดให้บรรทัด ? (3,531/5,897)

> **รอบ 21 (6 ก.ย. 2026 เช้า):** รายงานผู้เล่นชุดใหม่ใน Google Sheet `bug_logs` แท็บ Judgment วันที่ 6/9 มี 10 รายการ
> (v1.1.1 · ผู้แจ้งคนเดียว ไม่ทิ้งช่องทางติดต่อ) · แก้แล้ว 3 รายการที่ระบุสตริงได้จากภาพ:
> (4) "แ-คุณ!" → "ค-คุณ!" (`batch_020`) · (9) "(สินี่คงเป็นฝาแฝดกันสินะ)" → "(สงสัยจะเป็นฝาแฝดกันสินะ)" (`batch_TALK_015`) ·
> (10) โจรกางเกงใน — ย้ายช่องว่างที่ `fix_thai_wrap` แทรกกลางวลีไปขอบวลี (`batch_TALK_015` · run ยาวสุด 34)
> · กวาดคลาสเดียวกับ (4) ทั้ง master = ติดอ่าง "X-คำ" ที่ X ไม่ใช่ตัวแรกของคำ → แก้เพิ่ม 3 จุด (`D-Damn you!`
> TALK_011 · `(C-Crap!)` TALK_038 · `Y-You're lying!` TALK_056) · ที่เหลือ 12 จุดเป็นแบบ "อ-เอ่อ / ห-ใคร" เสียงตรงกัน ปล่อยไว้
> · merge_qc ตก 0 · `fix_thai_wrap --check` 0 · `fix_dialogue_gender` 0 · บิลด์ `--clean` 157 bin ล้มเหลว 0 · gen_font_bin ·
> strip_ui + patch_drone · deploy แล้ว 11:51 (db 159 ไฟล์ · ui 4 ไฟล์ · MLO 8,064 B) · **ยังไม่ commit / ยังไม่แพ็ก release**
> · **ต่อ (เที่ยง 6 ก.ย.) — ได้ภาพครบจากเจ้าของ (`C:/Users/BigNut/Downloads/bug_judgment/issue_*.png`) แก้อีก 6 ข้อ + deploy รอบสอง:**
> (1)(2) `Homewrecker` / `Homewrecker's face` → "หญิงชู้" / "ใบหน้าหญิงชู้" (`batch_117` · คีย์นี้ใช้เฉพาะคดี sidA11 โนริโกะ แถวเดียวใน
> `minigame_photo_shooting_mission_todo_item` + `minigame_stalking_mission` → เพศหญิงถูกต้อง ไม่ชนคดีอื่น)
> · (3) ป้าย "รับงานจากสำนักงาน…" (`talk_system_msg` · `batch_132`) ล้นกรอบเพราะ `<color>` คั่นกลางช่วงไทยไม่มีช่องว่าง →
> **`fix_thai_wrap.py` มองไม่เห็น run ที่มี tag คั่น** (THAI_RUN ตัดที่ tag) → แพตช์รอบ 21: `worst()` วัดหลังตัด tag ·
> `split_span()` ตัดที่ขอบ tag ก่อน ถ้ายังยาวค่อยผ่าคำ · tag ปิดเกาะคำหน้า tag เปิดเกาะคำหลัง → `--write` แตะ **129 ข้อความ / 54 batch**
> (talk 71 · manual 37 · sound_auth 9 · pause_tutorial 6 …) → `remerge_stale --write` ค้าง 0 · `--check` 0
> · (5) "อย่ามายุ่งเรื่องกูวะ!" → "อย่ามายุ่งเรื่องของกู!" ลด วะ ซ้ำสองบรรทัด (`batch_020`) · (6) "Welcome... or whatever." →
> "ยินดีต้อนรับ... หรืออะไรก็ช่างเถอะ" (`batch_030`) · (7) แผงลิมิตเดิมพันแบล็กแจ็ก (`ui_text` แถว 131-133 `Bet Limit/Max/Min`)
> ป้ายไทยจมลง ~28 px เพราะจอคาสิโนวาดด้วย `casino_font` (สไปรต์ 256 cp) แล้ว fallback ไป meta ทั้งสตริง (cell 64 vs 32) →
> **ตัดสินคง EN "Bet Limit / Min / Max"** (`batch_109` · คีย์ `Max` ใช้ร่วมอีก 3 แถว 719/1379/1760 = โผล่เป็น EN ด้วย ยอมรับได้)
> — ถ้าอยากได้ไทยต้องหา offset แนวตั้งในเอนจิ้น ยังไม่มีทาง
> · merge_qc ทั้ง master ผ่าน 50,315 ตก 0 · `test_qc_tools` 14/14 · บิลด์ 157 bin ล้มเหลว 0 · gen_font_bin · deploy รอบสอง ~12:10
> · **ค้าง 1 รายการ**: (8) บท 2 หลังแนะนำตัว ซับหายเทียบเสียงพากย์ "ยินดีที่รู้จักครับ" — ไม่มีภาพ ต้องรู้ฉาก/ผู้พูด
> · ⚠ ข้อสังเกตยังไม่ได้ทำ: run ไทยที่คั่นด้วย "..." / "!" (ไม่ใช่ช่องว่าง) ยังวัดแยกกันอยู่ — ถ้าเอนจิ้นไม่ตัดที่เครื่องหมายวรรคตอน
> จะล้นได้เหมือนกัน (เช่น "จะให้โอกาส...ที่เหลือเชื่อ...ได้ลองใช้ถุงมือ…" 76 ตัว) รอหลักฐานจากจอก่อนค่อยขยายเกณฑ์
>
> · **Sweep ทั้งเกม (บ่าย 6 ก.ย. — เจ้าของสั่ง "ใช้ team subagent ปูพรม"):** `scripts/make_sweep_chunks.py` ตัด master 49,639 คู่
> (ตัด EULA + คู่คง EN) เป็น 35 ชิ้น `translations/review/sweep/chunk_NN.tsv` · brief `SWEEP_BRIEF.md` หมวด A-G · ทีม sonnet 30 ตัว
> (~200k token/ตัว รวม ~6.2M — เกินประมาณการ 2x เพราะไทยกิน token มาก · เพดาน 12 ตัวพร้อมกัน) · ผล `findings_NN.json` 141 จุด
> (C 84 · E 21 · F 17 · A 9 · D 9 · G 1) → `scripts/apply_sweep_findings.py` (ตรวจ 
/tag/run≤36/ยาว-สั้นผิดปกติ · `--skip-cat` `--mid-ids`
> `--reject-ids`) **รับ ~95 จุด** · รายงานเต็ม `apply_report.md`
> · คำตัดสิน lead: **ติดอ่าง (F) ล็อกกติกา "ตัวหน้าขีด = ตัวเขียนตัวแรกของคำ"** (สถิติ master 442:8 · ทีมเสนอขัดกันเอง) แล้ว normalize
> ทั้ง done ด้วยสคริปต์ ไม่ใช้ผล F ของทีม · ปฏิเสธ ดิฉัน/ฉัน ของอามาเนะ (ชิ้น 03 กับ 10 เสนอสวนทางกัน = สไตล์) · "น่ารักออก" ถูกอยู่แล้ว
> · ชื่อ: Asuka Momokaze → **อาซึกะ โมโมคาเซะ** (glossary §7 บรรทัด 241 ยังเขียน อาสึกะ ขัดกับคำตัดสินบรรทัด 536 — ต้องแก้ตาราง) ·
> Haoyu Xiu → เฮ่าอวี้ ซิว · Kiyoshiro Asamura → คิโยชิโร (ไม่มีไม้เอก) · Kon-chan → คนจัง
> · กวาดเชิงกลตามแพตเทิร์นที่ทีมพบ: โดะยเฉพาะ · แล้ ว · อี กรอบ · ขอบ คุณ · หหรวน · นั่งเฉยอยู่เฉยๆ · **"อาจารย์อร์" = เซนเซอร์ที่โดนกฎ -sensei
> กิน** (1 จุด ui) · ⚠ `normalize_terms.py` บรรทัด 73 เคยกลับทาง (อาจารย์เก็นดะ→เก็นดะเซนเซ) = รัน --write เมื่อไหร่คำตัดสิน 5 ก.ย. หาย → แก้แล้ว
> · พลาดที่จับได้: แทน "โดะน→โดน" ไปโดน "คิโดะน่า" 3 จุด (แก้กลับ) · ยุบช่องว่างซ้ำไปโดนข้อความคง EN 17 จุด (คืนแล้ว · คง EN 661) ·
> ทีมเสนอ "ไม่ค่ะ" ให้อาซึสะ โอทากิ แต่ `fix_dialogue_gender` (ตารางผู้พูดจากไฟล์เกม) บอกชาย → เชื่อไฟล์เกม คืนเป็น ครับ
> · สุดท้าย: merge_qc ผ่าน 50,315 ตก 0 · wrap 0 · gender 0 · test_qc_tools 14/14 · บิลด์ 157 bin · deploy รอบสาม · **ยังไม่ commit**
> · ข้อสังเกตทีม (ไม่ได้ทำ): ♪ ในเพลงซานะหาย 4 บรรทัด (ชิ้น 01) · `•` ใน tag color ของ manual VR — รับแล้วรอดูบนจอว่า encode ได้
>
> · **release v1.1.2 (6 ก.ย. 13:13 — เจ้าของสั่ง "release เลย เดี๋ยวให้ user test")**: `release/JudgmentThai-th-v1.1.2.zip` (8.3 MB · 159 bin + ui 4) ·
> notes `release/notes-v1.1.2.md` · GitHub release v1.1.2 (สูตร `gh release create` + `upload` เดิม) · `patch.md` อัปเป็น v1.1.2 · commit รอบ 21 ทั้งชุด
> (done 100+ batch · master · fix_thai_wrap tag-aware · normalize_terms กฎ -sensei กลับทาง · make_sweep_chunks / apply_sweep_findings · review/sweep/)
> · ยังไม่มีใครยืนยันบนจอสำหรับรอบ 21 — รอรายงานผู้เล่นรอบถัดไป · ข้อ (8) ซับหาย "ยินดีที่รู้จักครับ" ยังค้าง
>
> · (รายการเดิมตอนเช้า) **ค้าง 7 รายการ** (ยังไม่ได้ดูภาพ): (1)(2) คดีเสริม "จุดมืดมิดที่สุด" แปล "ชายชู้" ทั้งที่เป้าหมายเป็นผู้หญิง (ภารกิจถ่ายภาพ + เริ่มสะกดรอย)
> · (3) บอร์ดสรุปคดีหลังจบคดีเสริมตกขอบ · (5) "อย่ามายุ่งเรื่องของกูวะ!" สำนวน · (6) บ่อตกปลาพบไคโตะ บท 2 ประโยคแปลก ·
> (7) จอหลังเข้าคาสิโน บท 2 ตกกรอบ · (8) บท 2 หลังแนะนำตัว ซับหายเทียบเสียงพากย์ "ยินดีที่รู้จักครับ" (ไม่มีภาพ — ต้องหาจากบริบท)

> **รอบ 20 (5 ก.ย. 2026 บ่าย — ต่อจากรอบ 19):** ปิด issue สุดท้ายในรายงานผู้เล่น = **MV intro "ซับแปลก ๆ"** (27/8)
> ต้นทาง: `auth.bin → a01_035 → cinema_telop` 8 แถว มีเวลาแต่ไม่มีข้อความ (TEXT_COUNT 0) · ไฟล์ต้นฉบับ
> ตั้งพอยน์เตอร์ตารางข้อความ (main table +0x24) = **0** สำหรับตารางที่มีคอลัมน์สตริงแต่ไม่มีข้อความ
> (สำรวจทั้ง db: 682/692 ตาราง) แต่ `tools/reARMP_fixed.py` (ทุกโปรเจกต์พี่น้อง K3/LJ/Gaiden/Y6/Y7/Y8/Ishin/
> Pirate/K2R/K1 ใช้โค้ดเดียวกัน) เขียนให้ชี้ไป column types → `textoff[0]` = ไบต์ขยะ → เอนจิ้นวาดสตริง
> สุ่มกลางไฟล์บน telop ว่างของ MV · แก้ที่ reARMP บรรทัด "JETH fix (5 Sep 2026)" (ตารางมีคอลัมน์ type 13
> + TEXT_COUNT 0 → เขียน 0 · ตารางไม่มีคอลัมน์สตริงคงพฤติกรรมเดิม) · ผล: 83 ตารางใน 157 bin เปลี่ยนเป็น 0
> (auth 1 · complete_checklist 59 · manual 5 · msg 6 · talk 5 · pause_message 4 · controller_guide 2 ·
> minigame_stalking_mission 1) · round-trip JSON ของ auth.bin เท่าต้นฉบับ · บิลด์ `--clean` 157 bin ล้มเหลว 0 ·
> `gen_font_bin` regen (`--clean` ลบ font.bin ออกจาก stage — ต้องรันซ้ำทุกครั้ง) · deploy แล้ว (163 ไฟล์ · MLO 8,022 B)
> ✅ **ผู้เล่นยืนยันบนจอแล้ว (5 ก.ย. บ่าย): MV ไม่มีซับแปลกอีก** — สาเหตุ reARMP ยืนยันจริง ปิด issue นี้ได้
> ⚠ โปรเจกต์พี่น้องทุกตัวมีบั๊กนี้ — ถ้าเจอ "ซับ/ข้อความสุ่มโผล่บนจอที่ควรว่าง" ให้พอร์ตแพตช์นี้ไป
> (ห้ามแก้ในโปรเจกต์อ่านอย่างเดียวจากที่นี่) · เช็กลิสต์ทดสอบผู้เล่นเพิ่มข้อ 6: MV เปิดเกม ไม่มีซับแปลก
> · ✅ **แพ็กแล้ว `release/JudgmentThai-th-v1.1.1.zip` (8.3 MB · 159 bin + ui.judge.en 4 ไฟล์ · 5 ก.ย. 13:41)** หลังผู้เล่นยืนยันครบ 3 จุด (MV · CASE FILE · เมนูโดรน)
> · 🚀 **repo ขึ้น GitHub แล้ว**: https://github.com/bignutchanon/judgment-thai (public · commit รอบ 19+20 `fc338a0` + patch.md `94ae6b7`)
> · release **v1.1.1**: https://github.com/bignutchanon/judgment-thai/releases/tag/v1.1.1 — notes จาก `release/notes-v1.1.1.md`
>   (สูตรเดียวกับ LJ: `gh release create vX -R bignutchanon/judgment-thai --notes-file release/notes-vX.md --latest` แล้ว `gh release upload vX release/JudgmentThai-th-vX.zip`)
>   ⚠ ถ้า asset zip ยังไม่ขึ้นบนหน้า release = การอัปโหลดจาก session นี้ถูกบล็อก ให้เจ้าของรัน `gh release upload` เอง
> · `patch.md` เขียนฉบับ v1.1.1 แล้ว (URL download GitHub · changelog · ร่างข่าว 4.3) พร้อมส่งให้ `yakuza-wiki`
> · `.gitignore` เพิ่ม release/ shots/ scratch_*.txt out*.txt *.bin.json ที่ root — ของแตกจากเกม/ไฟล์แจกไม่ commit
>
> **รอบ 20 ต่อ (บ่าย 5 ก.ย. — ผู้เล่นส่งภาพ 2 ชุดหลังบิลด์รอบ 19):**
> **(ก) เมนูโดรน** หัวข้อ 4 อันเป็นไทยแล้วแต่ตกลงใต้เส้นคั่นทับคำอธิบายของแถวที่เลือก — ต้นทาง:
> `ui.judge.en.par/en/scene/pause_drone.bin` ตารางย่อย `top_menu_list_item0..3` (121 คอลัมน์ column-major ·
> type 2 = 1 ไบต์/แถว · type 7 = float 4 ไบต์/แถว) element `category` = หัวข้อโหมดฟอนต์ภาพ (`drone_font`)
> กล่อง 800x80 pivot (0,40) pos y=-17 → ตอน fallback ไปฟอนต์ปกติ เอนจิ้นวางข้อความที่ pos.y+pivot.y = +23
> (ขอบล่างกล่อง) ทับคำอธิบาย (+22..42) · แก้ระดับไบต์ด้วย `scripts/patch_drone_menu_titles.py --write`
> (col11 -17 → -62 · col47 ขนาดฟอนต์ 0 → 30 · 4 แถว · 12 ไบต์) → `build/ui/ui.judge.en/en/scene/pause_drone.bin`
> → `deploy_spoil` ส่งทั้งโฟลเดอร์ (mods ui.judge.en ตอนนี้ 4 ไฟล์) · ✅ **ผู้เล่นยืนยันบนจอแล้ว (5 ก.ย. บ่าย)** —
> หัวข้ออยู่เหนือเส้น ไม่ทับคำอธิบาย และ col47 = ขนาดฟอนต์ตอน fallback จริง (หัวข้อใหญ่ขึ้นเป็น 30)
> จอที่ใช้ฟอนต์สไปรต์อื่น (คาสิโน `casino_font` · `common_font` · หัว DRONE LAB ใน `drone_labo`) น่าจะมีอาการ
> เดียวกันแต่ยังไม่มีภาพ · เครื่องมือถอด scene: reARMP ใช้ decode ได้ (JSON 12 MB) แต่ **ห้าม encode กลับ**
> **(ข) CASE FILE ยังล้น** ทั้งที่รอบ 19 แทรกช่องว่างแล้ว — ถอดสตริงจาก bin ที่ deploy ยืนยันว่ามีช่องว่างจริง แต่เอนจิ้น
> ไม่ตัดที่ช่องว่างนั้น · เทียบจุดตัด 7 จุดจากภาพกับความกว้างจำลอง (advance จาก slotmap) ไม่มี metric ไหนสอดคล้อง
> จนพบกติกา: **ช่องว่างใช้ตัดบรรทัดได้ก็ต่อเมื่อคำถัดไปยาว ≤ ~40 ตัว (นับหลัง encode)** — คำ 43-49 ตัว
> เอนจิ้นข้ามช่องว่างหน้าคำแล้วไปตัดที่ช่องว่างถัดไปแทน (บรรทัดจึงล้นออกขวา) · คำ ≤ 40 ตัดได้ทุกจุด
> → `fix_thai_wrap.py`: FLOOR 60 → **36** · TARGET 52 → **30** · เลิกใช้ p99 ต่อบิน (เกณฑ์เป็นความยาวคำ ไม่ใช่กล่อง)
> · แก้ done ~1,300 ข้อความ → remerge → master 50,297 คู่ · run ไทยยาวสุดทั้ง master = 36 · merge_qc ตก 0 ·
> บิลด์ 157 bin · gen_font_bin · deploy แล้ว · ✅ **ผู้เล่นยืนยันบนจอแล้ว (5 ก.ย. บ่าย) — CASE FILE ไม่ล้นอีก** กติกาคำ ≤ ~40 ตัวยืนยันจริง
> สายบิลด์เต็มตอนนี้: `slot_alloc --write → inject_thai_title --slotmap → cp italic → build_text --clean →
> gen_font_bin → strip_ui_sprite_slots --write → patch_drone_menu_titles --write → deploy_spoil`

> **สรุปสั้นสุดสำหรับ session ใหม่ (5 ก.ย. 2026 · รอบ 19):** ปล่อยไปแล้ว v1.1 · ตอนนี้ **ในเกมคือบิลด์
> หลังแก้ bug ครบทุกข้อจากรายงานผู้เล่น 5 ก.ย.** (deploy แล้ว · **ยังไม่แพ็ก release** — เจ้าของสั่งรอให้
> ผู้เล่นยืนยันบนจอก่อน) สิ่งที่เปลี่ยนจาก v1.1: (1) เพศผู้พูด — ตารางรวมทุกแหล่ง 40,889 ข้อความ +
> คัตซีนระบุผู้พูดครบ 102 ฉาก แก้ 39 บรรทัด (2) `-sensei` → **อาจารย์+ชื่อ** ทั้งเกม 342 บรรทัด
> (3) "No." → "ไม่" · "ไข้ยากามิ" → "กระแสยากามิ" (4) **สระอำแตกเป็น ํ + า** ตอน encode (slotmap 154 เซลล์
> · atlas ใหม่) (5) จอโดรน/คาสิโน — ล้าง donor ในฟอนต์สไปรต์ UI ส่งผ่าน `mods/JudgmentThai/ui.judge.en`
> (6) CASE FILE ตกกรอบ — `fix_thai_wrap.py` แทรกช่องว่างที่ขอบคำ (ช่วงไทย ≤ 60 ตัว) 750 ข้อความ
> **งานถัดไป** (ตามลำดับ): ① รอผลทดสอบผู้เล่น 5 จุด (CASE FILE บท 1 · คำที่มี ำ · เมนูโดรน+คาสิโน ·
> ฉากเปิด a01_010 · ซับทั่วไป) ② ถ้าผ่าน → `python scripts/package_release.py --version 1.1.1`
> (ใส่ `ui.judge.en` ให้แล้ว) + `patch.md` ③ MV intro "text แปลก ๆ" ยังไม่รู้ต้นทาง — ต้องขอแคป
> ④ git ยังไม่ commit งานรอบ 19 ทั้งหมด (ไฟล์ใหม่: scripts 8 ตัว · translations/cinema_speakers/ 102 ไฟล์ ·
> speaker_gender_overrides.json · gender_exceptions.json · docs/dialogue_gender_table.md · extracted/ui_en/ ห้าม commit ใหญ่)
> · สายบิลด์เต็มตอนนี้: `slot_alloc --write → inject_thai_title --slotmap → cp italic → build_text --clean →
> gen_font_bin → strip_ui_sprite_slots --write → deploy_spoil` · ก่อน deploy รัน `fix_dialogue_gender.py` (ต้อง 0) +
> `fix_thai_wrap.py --check` (ต้อง 0) + `test_slot_alloc.py` 12/12 · รายละเอียดทั้งหมดในหัวข้อ "รอบ 19" ข้างล่าง

> **สรุปรอบก่อนหน้า (22 ส.ค. 2026 · รอบ 16):** โหมด EN วาดข้อความทุกชั้นด้วย bitmap
> grid `data/font.judge/en/meta_ot_cond_book.dds` ตัวเดียว (16 คอลัมน์ · cell 32x64 · 384 เซลล์ ·
> ขยายไม่ได้) แต่ **advance ของทุกเซลล์เราตั้งเองได้** ผ่าน `kerning_table` ใน
> `db.judge.en.par → en/font.bin` (ไม่ใช่ใน exe อย่างที่รอบ 3-15 เชื่อ) → มาร์ก advance = 0 ได้
> จึงเลิก pre-compose แล้ว **หนึ่งตัวอักษรหนึ่งเซลล์**
> เครื่องมือ: `slot_alloc.py` · `inject_thai_title.py --slotmap` · `build_text.py` ·
> `gen_font_bin.py` (ตาราง advance) · `preview_line.py` (จำลองการวาดออกมาเป็น PNG) ·
> `deploy_spoil.py` (deploy / `--restore`)
> **อ่านหัวข้อ "รอบ 17" (ตัวนำสลับฟอนต์) และ "รอบ 16" ข้างล่างก่อนแตะฟอนต์ทุกครั้ง**

## 🧩 5 ก.ย. 2026 (รอบ 19) — ตารางเพศผู้พูดทั้งเกม + กวาดคำแปลรอบสอง (ปิดช่องโหว่คัตซีน/แชท/ผู้พูด unknown)

### ที่มา

รายงานผู้เล่น 5 ก.ย. 2026 (Google Sheet `bug_logs` แท็บ Judgment · v1.1): "คำลงท้ายผิดเพศของตัวละครบางคน
ในคัตซีนฉากเริ่มเกม" — ทั้งที่รอบ 18 กวาดด้วยคิวเสียงไปแล้ว 87 บรรทัด นับใหม่จากไฟล์จริงพบว่า
บรรทัดที่แปลระบุเพศไว้ 14,100 บรรทัด **ไม่มีหลักฐานผู้พูดเลย 2,362** (คัตซีน `auth.bin` 992 ·
แชท `pause_message.bin` 721 · บันทึกยากามิ ~500) และอีก **1,771 บรรทัดอยู่กับผู้พูด `talk.bin`
ที่ทะเบียนเป็น unknown** (123 ชื่อ) ซึ่ง `check_speaker_gender` ข้ามให้เงียบ ๆ

### ทำอะไร

* ทีม subagent sonnet 14 ตัว (ยิงพร้อมกัน ~15 นาที): 11 ตัวอ่านบริบทคัตซีนทีละฉากแล้วระบุผู้พูด+เพศ
  **ทุกแถว** (102 ฉาก · 2,374 แถว → `translations/cinema_speakers/<ฉาก>.json`) · 3 ตัวพิสูจน์เพศ
  ผู้พูด unknown 123 ชื่อจากบทพูด EN (→ `translations/speaker_gender_overrides.json` · ชาย 79 · หญิง 27 ·
  neutral 4 · ยังไม่ยืนยัน 23)
* ตารางรวมทุกแหล่ง `extracted/facts/dialogue_gender.json` + สรุป `docs/dialogue_gender_table.md`
  (**นี่คือ "ตารางบทพูดแยกชายหญิงทั้งเกม"**): ข้อความที่รู้เพศ 40,889 — ชาย 34,472 · หญิง 5,548 ·
  ใช้ร่วมสองเพศ 262 (ต้องกลาง) · บรรยาย 132 · ไม่ยืนยัน 381
* กวาด master_th: ขัดกัน 49 → แก้ 39 บรรทัด (ชาย→หญิง 5 · หญิง→ชาย 2 · →กลาง 32) · เหลือ 10 ที่ตั้งใจ
  ไม่แตะ (สรรพนาม "ผม" กลางประโยคของบรรทัดที่ธง ambiguous ของแชทน่าจะเป็น artifact — เนื้อความเป็นยากามิชัด)
* จุดที่ผู้เล่นเห็นจริง: `a01_010` (ออฟฟิศเก็นดะ) ซาโอริพูด "Trust me" → เคย "เชื่อผมสิ" · `a01_090`
  พนักงานต้อนรับหญิง "เชิญทางนี้เลยครับ" / ผู้ช่วยชายเสิร์ฟชา "ชาค่ะ" · ไคโตะ "ดิฉันว่า…" · ยากามิ "พยายามได้ดีค่ะ"
* บิลด์+deploy แล้ว: 157 bin ล้มเหลว 0 · `font.bin` regen · `check_speaker_gender` 0 · `test_qc_tools` 14/14
  **ยังไม่ได้แพ็ก release ใหม่** (v1.1 ยังเป็นไฟล์เดิม)

### เครื่องมือใหม่ (ลำดับใช้งาน)

```
python scripts/make_cinema_work.py            # แฟ้มงานคัตซีนให้ทีม (build/gender/cinema/G01..G11.md)
python scripts/make_talk_unknown_work.py      # แฟ้มงานผู้พูด unknown (build/gender/talk_unknown_P1..P3.md)
python scripts/merge_speaker_overrides.py --write   # รวมผลทีม -> translations/speaker_gender_overrides.json
python scripts/make_talk_speaker.py --write   # อ่านทะเบียน (รองรับคีย์ "<ชื่อ>#<speaker_id>" สำหรับป้ายที่ใช้ซ้ำ)
python scripts/make_dialogue_gender.py --write      # ตารางรวม + docs/dialogue_gender_table.md
python scripts/fix_dialogue_gender.py --write       # แก้ done/ ตามตารางรวม -> remerge_stale.py --write
```

ข้อยกเว้นที่ lead ตัดสิน: `translations/gender_exceptions.json` (ตัวแก้ข้าม) · ป้ายผู้พูดที่เกมใช้ซ้ำ
กับคนละตัวละคร (`???` 6 id · `Mijore Employee` 2 · `M Side Cafe Employee` 2) ตั้งเพศต่อ id ในทะเบียนแล้ว

### ต่อ (บ่าย 5 ก.ย.) — ไล่ bug จากรายงานผู้เล่น + คำสั่งเจ้าของ (ยังไม่ปล่อย release — รอแก้ครบทุก issue)

| งาน | ทำอะไร | สถานะ |
|---|---|---|
| D "ไม่มี→ไม่ใช่" | `No.` → **"ไม่"** (เดิม "ไม่ใช่" — สตริงใช้ร่วมทั้งเกม ซาโอริตอบคำถาม "มีงานไหม") | ✅ deploy |
| F "แปลคำผิด" ฉากเปิด | `Yagami fever` → **กระแสยากามิ** (เดิม "ไข้ยากามิ") | ✅ deploy |
| `-sensei` | เจ้าของสั่ง **เซนเซ → อาจารย์+ชื่อ** ทั้งเกม (อาจารย์เก็นดะ/ชินทานิ/โมโรโบชิ/โฮชิโนะ/คาตากิริ/ชิโรซากิ/โชโนะ/สไมล์ · เรียกลอย ๆ = อาจารย์) กวาด done 342 บรรทัด · glossary/PRONOUN_MATRIX/CLAUDE.md แก้ตามแล้ว | ✅ deploy |
| E จอโดรนเพี้ยน | พอร์ตวิธี LJ-015: **ล้างแถว donor ในตารางฟอนต์สไปรต์ UI** `ui.judge.en.par/en/font/*.bin` (256 แถว = codepoint · แก้ระดับไบต์ที่ `0x80 + แถว×16`) → `scripts/strip_ui_sprite_slots.py --write` → `build/ui/ui.judge.en/en/font/` 3 ไฟล์ (`drone_font` 20 ช่อง · `casino_font` 7 · `common_font` 3) → `deploy_spoil.py` ส่งเป็น loose `mods/JudgmentThai/ui.judge.en` (+ `--restore` ลบ · `package_release.py` ใส่ให้) · ต้องแตก par ก่อน: `tools/ParTool.exe extract <ui.judge.en.par> extracted/ui_en` | ⏳ deploy แล้ว รอผู้ใช้ดูจอ |
| MV intro "text แปลก ๆ" (27/8) | **เจอต้นทางแล้ว (รอบ 20 — ดูหัวข้อบนสุด)**: ฉากเปิด `a01_035` ใน `auth.bin` มีตาราง `cinema_telop` 8 แถวที่มีเวลาแต่ **ไม่มีข้อความ** (TEXT_COUNT 0 · `use_telop: 1`) และ `tools/reARMP_fixed.py` เขียนพอยน์เตอร์ตารางข้อความ (+0x24) ของตารางแบบนี้ให้ชี้ไป column types แทน 0 อย่างต้นฉบับ → เอนจิ้นอ่าน text index 0 ผ่านค่าขยะ = สุ่มสตริงกลางไฟล์ขึ้นเป็นซับ (ตำแหน่งขยะเปลี่ยนทุกบิลด์ อาการจึงไม่คงที่) · แก้ reARMP แล้วบิลด์+deploy ใหม่ | ✅ **ผู้เล่นยืนยันบนจอแล้ว 5 ก.ย. บ่าย — ซับแปลกหายไป** |
| B สระอำห่าง ("อ ำ") | ตามข้อเสนอเจ้าของ: **แตก ำ → ํ + า** ใน `slot_alloc.decompose_am()` (ใช้ทั้งตอนนับความถี่และ `encode()` · `decode()` ประกอบกลับด้วย `recompose_am()` ให้ round-trip เดิมผ่าน) · วรรณยุกต์ที่นำหน้า ำ (น้ำ = น ้ ำ) ย้ายไปหลังนิคหิต → encoder ยกขึ้น hlevel 1 เหนือวงกลมเอง · เซลล์ ำ ถูกถอดจาก MANDATORY · slotmap ใหม่ **154 เซลล์** (ฐาน 56 · มาร์ก 98 · เหลือ 27) · test 12/12 · atlas+italic+font.bin+157 bin บิลด์ใหม่ · preview `build/font/preview_am.png` วงกลมซ้อนพยัญชนะพอดี ทั้ง คำ/ทำ/น้ำ/สำนักงาน | ✅ deploy รอผู้ใช้ดูจอ |
| A CASE FILE ตัวหนังสือตกกรอบ | สาเหตุ = เอนจิ้นตัดบรรทัดที่ช่องว่างเท่านั้น ช่วงไทยติดกัน ~85-90 ตัว (ไม่มีช่องว่าง) ยาวเกินกล่อง (~75-80 ตัว) จึงถูกตัดทิ้งขอบขวา (K3 เจอแบบเดียวกันแต่เรียงแนวตั้ง) → พอร์ต `scripts/fix_thai_wrap.py` จาก K3: ตัดคำด้วย pythainlp newmm + พจนานุกรมชื่อเฉพาะโปรเจกต์ 4,017 คำ แล้วแทรกช่องว่างที่ขอบคำให้ช่วงติดกันไม่เกิน **60 ตัว** (TARGET 52 · K3 ใช้ 44 เพราะกล่องประวัติแคบกว่า — เกณฑ์ 44 จะแตะ 3,734 ข้อความ เกณฑ์ 60 แตะ 750) · แก้ done 750 ข้อความ/112 batch → remerge · merge_qc ตก 0 · บิลด์ 157 bin · deploy | ✅ รอผู้ใช้ดูจอ CASE FILE |

กับดักเพิ่ม: `batch_002.done.json` เคยค้างต่าง master 16 คีย์ (a01_010 เป็น ค่ะ ขณะ master กลางตามรอบ 13)
— `remerge_stale --write` จะดึงกลับได้ จึง sync done ให้ตรง master แล้ว

### สถานะไฟล์/ตัวเลข ณ ปิด session 5 ก.ย. 2026

* `master_th.json` 50,297 คู่ · `merge_qc --dry-run` ผ่าน 50,315 ตก 0 · `check_speaker_gender` 0 ·
  `fix_dialogue_gender` เสนอ 0 · `fix_thai_wrap --check` เสนอ 0 · `test_slot_alloc` 12/12 · `test_qc_tools` 14/14
* slotmap **154 เซลล์** (ฐาน 56 · มาร์ก 98 · pool 181 เหลือ 27) — atlas + italic + `font.bin` ตรงกับ slotmap นี้
* deploy ในเกม: `mods/JudgmentThai/db.judge.en` 159 ไฟล์ + `ui.judge.en/en/font/` 3 ไฟล์ + ฟอนต์ drop-in 2 dds
  · MLO 8,022 B · ถอนด้วย `deploy_spoil.py --restore` (ลบ ui.judge.en ให้ด้วยแล้ว)
* ของที่ **ยังไม่ commit**: ทุกอย่างในรอบ 19 · `extracted/ui_en/` (293 MB แตกจาก par — ห้าม commit · ถ้าหายให้แตกใหม่ด้วย
  `tools/ParTool.exe extract <ui.judge.en.par> extracted/ui_en`)
* release ล่าสุดที่แจก = v1.1 (ไม่มีของรอบ 19) — เวอร์ชันถัดไปเสนอ **v1.1.1** หลังผู้เล่นยืนยัน

### เช็กลิสต์ทดสอบที่ส่งให้ผู้เล่น (รอผล)

| จุด | ดูอะไร | ถ้าพัง สงสัยอะไรก่อน |
|---|---|---|
| CASE FILE บท 1 (คดีฆาตกรรมต่อเนื่อง) | ข้อความไม่ตกกรอบขวา | เกณฑ์ 60 ยังกว้างไป → ลด FLOOR/TARGET ใน `fix_thai_wrap.py` |
| คำที่มี ำ (สำนักงาน · น้ำ · ทำ) | วงกลมชิดพยัญชนะ · น้ำ วรรณยุกต์อยู่เหนือวงกลม | variant ํ (5 ชั้น wclass) — ดู `preview_am.png` เทียบ |
| เมนูโดรน (Drone Lab) + คาสิโน | หัวข้อเป็นไทยอ่านออก (ฟอนต์ธรรมดา ไม่ใช่ฟอนต์ตกแต่ง) | ตาราง sprite font อื่นที่ยังไม่ได้ strip / fallback chain ไม่ถึง meta |
| ฉากเปิด a01_010 (ออฟฟิศเก็นดะ) | ซาโอริลงท้าย ค่ะ/ฉัน · "อาจารย์เก็นดะ" | `translations/cinema_speakers/a01_010.json` |
| ซับบทสนทนาทั่วไป | สระ/วรรณยุกต์ไม่ลอย ไม่มี tofu (จัดเซลล์ใหม่ทั้งชุด) | `slot_alloc.py` — เทียบ `docs/slot_alloc.md` |
| ~~MV เปิดเกม~~ | ✅ ผ่านแล้ว 5 ก.ย. บ่าย (reARMP fix) | — |
| ~~เมนูโดรน (รอบ 20 ข)~~ | ✅ ผ่านแล้ว 5 ก.ย. บ่าย — หัวข้อเหนือเส้น ขนาด 30 ใหญ่กว่าคำอธิบาย (col47 มีผลตอน fallback จริง) | — |
| ~~CASE FILE (รอบ 20 ข)~~ | ✅ ผ่านแล้ว 5 ก.ย. บ่าย — ทุกบรรทัดอยู่ในกรอบ (FLOOR 36 / TARGET 30 ยืนยันบนจอ · กติกา "คำถัดไป ≤ ~40 ตัว" ยืนยันจริง) | — |

### กับดักที่เจอรอบนี้

1. **ป้ายชื่อผู้พูดใน `talk_talker.bin` ไม่ใช่ตัวละครหนึ่งต่อหนึ่ง** — `???` ใช้กับ 6 คน (มีทั้งยูริกะ ทาชิบานะ
   ที่เป็นหญิงและมือระเบิดชาย) ตั้งเพศต่อชื่อจึงผิด → ทะเบียนรับคีย์ `ชื่อ#id`
2. **คำใบ้ cue/talk บนประโยคสั้น ("Huh?", "Thank you", "Shut up!") ชนกันข้ามฉาก** เพราะ map ด้วยข้อความ EN
   ทั้งเกม — ทีมคัตซีนใช้บริบทฉากทับ และตารางรวมนับเป็น `mixed` (กลางเพศ) ซึ่งถูกต้องอยู่แล้ว
   เพราะสตริงเดียวกัน = คำแปลเดียวกันทุกจุด
3. `to_neutral` เดิมไม่ตัด "ไหมคะ/เหรอคะ/หรือคะ" · `คะ` ใน "ราคะ" ถูกจับเป็นคำลงท้าย → แก้ regex ทั้งสองแล้ว

## 🔥 29 ส.ค. 2026 (รอบ 17) — เจอสาเหตุ "ตัวอักษรเพี้ยนเป็น À È Ú Á" แล้ว: จอที่ใช้ฟอนต์ `yakuza`

### อาการ

ผู้ใช้ส่งภาพเมนูโดรน (Drone Lab): หัวข้อเมนู 4 อัน (FLIGHT / CUSTOMIZE / RACE RECORD /
OPERATION) ขึ้นเป็นอักษรละตินตัวใหญ่ `À È Ú Á` แล้วมีตัวไทย **ตัวเล็ก** ต่อท้าย ส่วนคำอธิบาย
ใต้เมนู ("แต่งโดรนของคุณ") และป้าย SPEC ("ความทนทาน / ความเร็ว / การบังคับ") ในจอเดียวกัน
**เป็นไทยถูกต้องทุกตัว** — อาการเดียวกับ "ป้าย EX สีเขียวตอนต่อสู้" ที่รายงานไว้ตอนปล่อย v1.0

### สาเหตุ (ยืนยันด้วยการจำลองการวาดออกมาเทียบกับภาพ)

โหมด EN ไม่ได้วาดทุกชั้นด้วย `meta_ot_cond_book` อย่างที่รอบ 16 สรุปไว้ — **UI บางจอตั้งฟอนต์
เป็น `yakuza`** (แถวที่ 3 ของ `en/font.bin` · ไฟล์ `data/font.judge/en/yakuza.dds`
256x512 · cell 16x32 · 16 คอลัมน์ · **225 กลิฟ = cp U+0020-U+0100**) ซึ่งเป็นฟอนต์ bitmap
สไตล์หัวข้อ มี ASCII + Latin-1 ครบทุกตัว → เซลล์ donor ของเราในช่วง U+00C0-U+00FF
จึงออกมาเป็น `À È Ú Á` ตัวจริงของฟอนต์นั้น (แถวนี้ไม่มี `kerning_table` = ตั้ง advance ไม่ได้
วาดแบบ fixed pitch จึงห่างเป็นช่อง ๆ)

**ลูกเล่นของเอนจิ้นที่เป็นทางออก:** พอเจอ codepoint แรกที่ฟอนต์นั้น "ไม่มี" มันจะสลับไปวาดด้วย
`meta_ot_cond_book` **แล้ววาดด้วยฟอนต์นั้นต่อจนจบสตริง** (ไม่ใช่สลับเฉพาะตัวนั้น) —
พิสูจน์โดยจำลองการวาดสองแบบ (สลับทีละตัว vs สลับแล้วอยู่ยาว) แล้วเทียบกับภาพผู้ใช้:
แบบ "สลับแล้วอยู่ยาว" ตรงทุกบรรทัด (เช่น `การบิน` = ใหญ่ `ÀʞèÚ` + เล็ก `ิน` ทั้งที่ `น`
เป็น donor ที่ `yakuza` มีกลิฟ · `การบังคับ` = ใหญ่ 4 ตัว + เล็ก `ังคับ`)
สคริปต์จำลอง: `build/font/_sim_stay.png` เทียบ `_sim_perglyph.png`

### วิธีแก้ — เซลล์ "ตัวนำ" (sentinel) U+0165

แทรก codepoint ที่ **ฟอนต์อื่นไม่มีแต่ `meta_ot_cond_book` มี** ไว้หน้าอักษรไทยทุกช่วง
→ บังคับเอนจิ้นสลับมาใช้ atlas ของเราตั้งแต่ตัวแรก ไม่ว่าจอนั้นตั้งฟอนต์อะไรไว้

* เลือก **U+0165**: เกิน 225 กลิฟของ `yakuza` · `tbgm_0p_ja` ไม่มี Latin Ext-A เลย (ตรวจแล้ว) ·
  ยังอยู่ในตาราง 332 แถวของ `kerning_table` (แถว 325) จึงตั้ง advance = 0 ได้ · EN ไม่ใช้
* เซลล์นี้ **วาดเป็นเซลล์ว่าง** + `L = R = 1.0` → advance = 36 - 18x2 = **0 px**
  จึงมองไม่เห็นและไม่ขยับ layout ของจอที่ปกติอยู่แล้ว
* `SlotMap.encode()` แทรกให้เองที่ **ต้นของทุกช่วงไทย** (ช่วง ASCII คั่นแล้วขึ้นช่วงใหม่ก็แทรกอีก)
  — เผื่อกรณีเอนจิ้นสลับฟอนต์กลับเมื่อเจอ ASCII ที่ฟอนต์เดิมมี
* `decode()` คืนค่าเป็นสตริงว่าง → round-trip เดิมยังผ่าน (test 12/12)

โค้ดที่แก้: `scripts/slot_alloc.py` (`SENTINEL_CP`, `SENTINEL_SPEC`, `SlotMap.encode`) ·
`scripts/inject_thai_title.py` (วาดเซลล์ว่าง + ตรวจ "ต้องไม่มีหมึก")

### สถานะ

* บิลด์ใหม่ครบสายแล้ว: slotmap **151 เซลล์** (150 เดิม + ตัวนำ · เซลล์เดิมไม่ขยับสักตัว) ·
  atlas + italic · `build_text.py` 157 bin ล้มเหลว 0 · `font.bin` · `preview_line.png` ผ่านตา
* deploy ลงเกมแล้ว (font drop-in + `mods/JudgmentThai/db.judge.en` 159 ไฟล์ + regen MLO)
* ⏳ **ยังไม่มีใครเห็นบนจอ** — สมมติฐาน "เจอ cp ที่ฟอนต์นั้นไม่มี แล้วสลับไปวาดด้วยฟอนต์
  fallback ยาวจนจบสตริง" มาจากการจำลองการวาดเทียบกับภาพเดียว **ยังไม่ผ่านการทดสอบในเกม**
  แผนคือปล่อยให้ผู้เล่นทดสอบแล้วรอผลกลับ
* **ปล่อย v1.0.1 ตามคำสั่งเจ้าของโปรเจกต์ 29 ส.ค. 2026** ทั้งที่ยังไม่ยืนยันบนจอ — เจตนาคือ
  ให้ผู้เล่นช่วยทดสอบแล้วรายงานกลับ · `release/JudgmentThai-th-v1.0.1.zip`
  (8,067,493 B · sha256 `77b2bfc5d4af3acb…` · 159 bin + 2 dds + ตัวโหลด + ตัวติดตั้ง)
  ตรวจในซิปแล้ว: `font.bin` อยู่ครบ · คำแปลที่แก้เพศรอบ 18 อยู่ในบินจริง (สุ่ม encode เทียบแล้วตรง
  และรูปเก่าหายไปแล้ว)
* `patch.md` อัปเดตเป็นฉบับปล่อยจริง: ข่าวข้อ 1 ฟอนต์ · ข้อ 2 เพศผู้พูด 87 บรรทัด ·
  ขอให้ผู้เล่นช่วยยืนยันสองจุดของข้อ 1 กลับมา
* **เหลือขั้นตอนของเจ้าของ**: อัปซิปขึ้น Drive แบบ Manage versions (ทับไฟล์เดิม ลิงก์ไม่เปลี่ยน)
  แล้วให้ session ของ `yakuza-wiki` ลงข่าวตาม `patch.md`
* บทเรียนที่ได้ต่อ: **ฟอนต์ในเกมไม่ได้มีตัวเดียว** — จอไหนตั้งฟอนต์เป็น `yakuza`/`gothic`/`symbol`
  ก็ไม่มีไทย
* **ขอบเขตที่ตัวนำครอบจริง (อย่าเคลมเกินนี้):** ตรวจไฟล์ฟอนต์ทุกตัวที่มีอยู่ใน
  `data/font.judge/en/` แล้ว ไม่มีตัวไหนมีกลิฟ U+0165 — `yakuza` (225 กลิฟ ถึง U+0100) ·
  `tbgm_0p_ja` (ไม่มี Latin Ext-A เลย) · `gothic` (8 กลิฟ) · `symbol` (104 กลิฟ ถึง U+0067)
  → ตัวนำบังคับสลับฟอนต์ได้กับทุกตัวที่เกมโหลดในโหมด EN
  **แต่ยังไม่ได้พิสูจน์** ว่า fallback ของทุกฟอนต์ชี้มาที่ `meta_ot_cond_book` (เห็นกับตาแค่กรณี
  `yakuza`) ถ้าจอไหน chain ชี้ไปฟอนต์อื่น อาการจะกลายเป็น "ว่างเปล่า" แทน "อักษรละติน"
  → เจอข้อความหายทั้งบรรทัดในจอไหน ให้สงสัยข้อนี้ก่อน
* ผลข้างเคียงที่ยอมรับไว้: จอที่ fallback จะวาดด้วย **ขนาดของ `meta_ot_cond_book`** ซึ่งเล็กกว่า
  ฟอนต์หัวข้อเดิม — หัวข้อบางจอจึงตัวเล็กกว่าที่เกมออกแบบไว้ (ไม่ใช่บั๊กใหม่)

## 🔥 22 ส.ค. 2026 (รอบ 16) — เจอตาราง advance แล้ว สถาปัตยกรรมฟอนต์เปลี่ยนทั้งชุด

### เจออะไร

ตารางความกว้างที่ตามหามาสามรอบ (สแกน `Judgment.exe` 394 MB และ RAM 5.6 GB ไม่เจอ)
**ไม่ได้อยู่ใน exe** — อยู่ในไฟล์ข้อมูลที่เราแก้ได้มาตลอด:

```
data/db.judge.en.par
  └── en/font.bin                      (ARMP v2 · 25 แถว = ฟอนต์ในเกม)
        └── แถว "meta_ot_cond_book"
              └── คอลัมน์ kerning_table   (ARMP ซ้อนอีกชั้น · 332 แถว x 6 คอลัมน์ float)
```

เจอเพราะกลับไปแกะม็อดไทยเก่า MOD2SUB อีกรอบแล้วพบว่าสรุปเดิม ("แก้แค่ `.dds` ไฟล์เดียว")
**ผิด** — เขาแก้ `db.judge.en.par` ด้วย และ diff ออกมาโดนแค่ `font.bin` 71 แถว ตรงช่วง
cell 0x81-0x14B = ช่อง donor ของเราเป๊ะ

### สูตร

```
advance  = 36 - 18.0 x (L + R)        # L = คอลัมน์คู่ซ้าย · R = คอลัมน์คู่ขวา
x_offset = -18.0 x L                  # กลิฟถูกเลื่อน "ซ้าย" จากตำแหน่งปากกา
```

ยืนยันสองทางอิสระ:
* fit กับ probe หวีของเราเอง 171 จุด → คลาดเคลื่อนเฉลี่ย **0.27 px** สูงสุด 2.0 px
* fit กับภาพในเกมของ MOD2SUB (แถบภารกิจ "เอาชนะพวกอันธพาล| Defeat the Thugs") → **rms 0.23 px**

6 คอลัมน์ = 3 คู่ (L,R) สำหรับขนาดวาด 3 แบบ · เมนูไตเติลใช้คู่ (5,6) · แถบภารกิจใช้คู่ (3,4)
→ **เขียนค่าเดียวกันลงทั้งสามคู่เสมอ** (MOD2SUB ก็ทำแบบนี้)

ค่าที่เก็บเป็นหน่วยครึ่ง em: เซลล์เต็ม = 2.0 · `L + R = 2.0` แปลว่า advance = 0 พอดี · เกิน 2.0 = ติดลบ

### ผลที่ตามมา (ของเก่าเลิกใช้หมด)

| เดิม (รอบ 3-15) | ตอนนี้ (รอบ 16) |
|---|---|
| ต้อง pre-compose ฐาน+มาร์กเป็นกลิฟเดียว | **หนึ่งตัวอักษรหนึ่งเซลล์** มาร์ก advance = 0 ซ้อนจริง |
| advance ตายตัว เซลล์ว่าง Ext-A = 36 px | ฐาน advance = ink + side bearing (ซ้าย 1 ขวา 3) |
| จับคู่ donor ตามความกว้าง (`donor_widths.json`) | donor ตัวไหนก็ได้ — เราตั้งค่าเอง |
| Ext-B tofu "เอนจิ้นไม่มี mapping" | tofu เพราะ `kerning_table` มีแค่ 332 แถว = ถึง **U+016B** |
| สระลอย ~3 ตัว/100 · ตัวห่าง ~20% | ทั้งสองอาการหายตามการออกแบบ (รอผู้ใช้ยืนยันบนจอ) |

### ระบบใหม่ย่อ ๆ

* `scripts/font_metrics.py` — สูตร ที่มา หลักฐาน ค่าคงที่ (K = 18.0 · CELL_ADV = 36 · LSB 1 · RSB 3)
* `scripts/slot_alloc.py` — จัดสรรเซลล์: ฐาน 57 ช่อง + **variant ของมาร์ก** 93 ช่อง = 150 (pool 182)
  - `wclass` 5 ชั้น — มาร์กต้องเลื่อนซ้ายเท่าไรขึ้นกับความกว้างฐานตัวก่อนหน้า
    (k-means ถ่วงความถี่ · ความเยื้องกลางเฉลี่ย **0.84 px** ในหน่วย atlas)
  - `hlevel` 2 ชั้น — วรรณยุกต์ที่ต้องซ้อนเหนือสระบนอีกที (ที่ ปื้ ญี่)
  - **ไม่ต้องยกมาร์กเมื่อฐานเป็นตัวสูง** (ป ฝ ฟ) — หางสูงเป็นเส้นบางชิดซ้าย มาร์กวางกลางไม่ชน
    (ลองยกแล้วมาร์กชนขอบบนเซลล์จนถูกตัด — เหนือเส้นฐานมีที่แค่ 44 px)
* `scripts/gen_font_bin.py` — เขียน (L,R) ลง `kerning_table` ทั้งแถว `meta_ot_cond_book`
  และ `meta_ot_cond_book_italic` → `build/text/db.judge.en/en/font.bin`
* `scripts/preview_line.py` — **จำลองการวาดของเอนจิ้น** จาก atlas + ตารางจริง ออกมาเป็น PNG
  (ผู้ใช้เป็นคนเปิดเกม รอบ feedback แพง — ต้องดู PNG ให้ผ่านตาก่อนส่งทุกครั้ง)

### สายบิลด์ (ลำดับนี้เท่านั้น)

```
python scripts/slot_alloc.py --write
python scripts/inject_thai_title.py --slotmap
cp build/font/meta_ot_cond_book.dds build/font/meta_ot_cond_book_italic.dds
python scripts/build_text.py --workers 8 --clean
python scripts/gen_font_bin.py
python scripts/preview_line.py          # ตรวจด้วยตาก่อน
python scripts/deploy_spoil.py          # --restore ถอน
```

### สถานะ ณ ตอนนี้

* deploy แล้ว: atlas 150 เซลล์ + `mods/JudgmentThai/db.judge.en` **159 ไฟล์** (มี `font.bin` แล้ว)
* `test_slot_alloc.py` **12/12 ผ่าน** · `build_text.py` 157 bin ล้มเหลว 0
* round-trip ตรวจแล้ว: `font.bin` ที่บิลด์อ่านกลับได้ค่า (L,R) ตรงทุกค่า · แถวที่ไม่ได้ยึด
  ไม่เปลี่ยนสักแถว · สตริงใน `title_root.bin` ถอดกลับเป็นไทยเดิมได้
* **ยังไม่ได้ยืนยันบนจอ** — รอผู้ใช้เปิดเกม

### งานที่ยกเลิกถาวร

ล่าตาราง width ใน exe/RAM (`find_width_table.py`, `patch_widths_mem.py`, `title_comb.py`,
`measure_comb.py`, `deploy_probe.py`, `translations/donor_widths.json`) — จบแล้ว ไม่ต้องทำต่อ
เก็บสคริปต์ไว้เฉย ๆ เผื่ออ้างอิงประวัติ

## 🧩 29 ส.ค. 2026 (รอบ 18) — พอร์ต "เพศผู้พูดจากคิวเสียง" มาจาก Lost Judgment แล้วกวาดคำแปล

### ที่มา

โปรเจกต์ LJ ทำเอกสารกลางของตระกูล Dragon Engine ไว้:
`D:\Projects\lost-judgment-thai\docs\reference\CUE_GENDER_METHOD.md` (อ่านอย่างเดียว ห้ามแก้จากที่นี่)
สรุปวิธี: ทุกแถวบทพูดใน `sound_auth.bin` ผูกกับ **ชื่อคิวเสียง** ซึ่งลงท้ายด้วย id ของ voicer
→ `sound_voicer.sex` ชี้เพศได้ **รายบรรทัด** (ไม่ต้องผ่านชื่อผู้พูดซึ่งใช้ซ้ำหลายคนได้)

ส่วนต่างของภาคนี้ + ผลที่ได้ + กับดัก: `docs/reference/cue_gender_judgment.md`
(สรุป: บทพูด EN อยู่คอลัมน์ **4 กับ 6** ไม่ใช่ 4/13 · คอลัมน์ชื่อผู้พูด **ว่างทั้งเกม** ·
`sound_voicer` ของภาคนี้ **ไม่มี** `voice_type`)

### ผล

```
แถวบทพูดที่มีข้อความ 9,863 · ผูกคิวและรู้เพศ 9,863 (100%)
ข้อความไม่ซ้ำที่ชี้ขาดได้ 15,399 — ชาย 14,057 · หญิง 1,274 · ปนสองเพศ 68
กวาด master_th: ขัดกัน 94 -> แก้ 87 · เหลือ 8 (ตั้งใจข้าม)
```

กลุ่มที่ผิดหนักสุด: บท **ซาโอริ** (เลขาหญิง) ถูกแปล "ครับ/ผม" ทั้งฉาก และบท **ชินทานิ**
(ทนายชาย) ถูกแปล "ค่ะ" ทั้งฉาก — นักแปลไม่มีทางรู้ เพราะ `sound_auth.bin` ไม่มีคอลัมน์ชื่อผู้พูด

### กับดักใหม่ที่เจอ (ยังไม่มีในเอกสารกลางของ LJ — ถ้าจะเติมต้องไปแก้ที่ repo นั้น)

1. **`sex` บางแถวเป็นเพศของนักพากย์ ไม่ใช่ของตัวละคร** — `sumire` (โฮสเตสหญิง) = 1 ชาย ·
   `kjart_woman` = 1 ชาย · `alpes_boy` (เด็กเสิร์ฟชาย) = 2 หญิง
   → กติกา: คิวเสียงเป็นหลัก แต่ถ้าขัดกับ `characters_main.json`/บทในเกม **ตัวละครชนะ**
   แล้วใส่ชื่อลง `SKIP_VOICERS` ใน `scripts/fix_line_gender.py` พร้อมเหตุผล
   (ตัวละครหลักทุกตัวที่เทียบแล้วตรงกันหมด — พลาดเฉพาะ NPC)
2. **สองแหล่งขัดกัน = บรรทัดใช้ร่วมกันจริง ต้องกลางเพศ** — คิวเสียงว่าเพศหนึ่ง แต่
   `talk_speaker.json` ว่าอีกเพศ (เคสจริง `Good luck.` = มาฟุยุ vs ยากามิ) สคริปต์เช็คให้แล้ว

### เครื่องมือใหม่

| สคริปต์ | ทำอะไร |
|---|---|
| `scripts/make_line_gender.py --write` | สร้าง `extracted/facts/line_gender.json` |
| `scripts/check_line_gender.py` | ตรวจอย่างเดียว (`--json` ส่งต่อได้) |
| `scripts/fix_line_gender.py --write` | แก้ `translations/done/` แล้วรัน `remerge_stale.py --write` ต่อ |

ตรวจหลังแก้: `check_line_gender` เหลือ 8 (ตั้งใจข้าม) · `check_speaker_gender` **0** ·
`test_qc_tools` 14/14 · `build_text` 157 bin ล้มเหลว 0 · แพ็ก `v1.0.1` ใหม่ + deploy ลงเกมแล้ว

⚠ **ลำดับบิลด์**: `build_text.py --clean` ลบ `build/text/db.judge.en/en/font.bin` ทิ้ง
ต้องรัน `gen_font_bin.py` **หลัง** เสมอ ไม่งั้นไฟล์แจกจะได้ 158 bin (ขาด font.bin) แล้วฟอนต์เพี้ยนทั้งเกม

### ยังไม่ได้ทำ

ซับ **จีนตัวเต็ม 13,647 แถว** ใน `sound_auth_subtitles_speech_list_*.bin` ผูกเลขคิวเดียวกัน
ใช้เป็นหลักฐานชั้นสองได้ (จีนแยก 他/她 = เพศของคนที่ถูกพูดถึง ซึ่ง EN ไม่บอก)
**ไม่มีบทพูดภาษาญี่ปุ่นในไฟล์เกมฝั่ง PC EN** — ที่เป็นญี่ปุ่นมีแค่ชื่อฉาก/ชื่อตัวละครใน
`timeline*.bin` กับ `talk_talker.bin` (ป้ายกำกับภายใน ไม่ใช่บทพูด)

## 📌 สรุปสถานะ ณ ปลาย session 22 ส.ค. 2026 (รอบ 15) — อ่านตรงนี้ก่อน

### ตอนนี้ในเกมคืออะไร
บิลด์ไทยเล่นจริงทั้งเกม (ไม่ใช่บิลด์ทดสอบแล้ว): ฟอนต์ `meta_ot_cond_book.dds` 202 เซลล์ +
`mods/JudgmentThai/db.judge.en` 158 ไฟล์ · ถอนได้ทุกเมื่อด้วย `python scripts/deploy_spoil.py --restore`

### สายบิลด์ (รันตามลำดับนี้เสมอ)
```
python scripts/slot_alloc.py --write        # จัดสรรเซลล์จาก master_th + donor_widths
python scripts/inject_thai_title.py --slotmap   # วาดกลิฟลง atlas
python scripts/build_text.py --workers 8 --clean # บิลด์ 157 bin
python scripts/deploy_spoil.py              # ลงเกม (--restore ถอน)
python scripts/deploy_probe.py              # สลับเป็นบิลด์ probe หวี (--play กลับมาเล่น)
```
ทุกอย่างอ่าน `translations/slotmap.json` ตัวเดียวกัน — แก้ที่เดียวแล้วรันใหม่ทั้งสองฝั่ง

### ตัวเลขล่าสุด
- `master_th.json` **50,297 คู่** (เพิ่ม batch `UICAPS` 30 คู่ + `WINDLG` 2 คู่ + `CINEMA_A01010` 16 คู่)
- บิลด์ **157 bin · แทนที่ 62,7xx สตริง · encode ไม่ผ่าน 0 · บิลด์ล้มเหลว 0** (~6 วินาที)
- slotmap: pool 202 · ใช้ 202 · **กลิฟเดียว 96.8%** · อ่านออกรวม 100%
- `python scripts/test_slot_alloc.py` = 6/6 · `check_speaker_gender.py` = 0 · `normalize_terms.py` = 0

### ⚠ สิ่งที่ยังค้าง (เรียงตามที่ผู้ใช้บ่นจริง)
1. **ตัวอักษรห่างกว่าปกติ ~20%** — เพดานของเอนจิ้น: advance ของ donor อยู่ในตาราง width ที่
   **ไม่ได้อยู่ในไฟล์ใด ๆ** และ 140 จาก 202 เซลล์มี advance ตายตัว 36-38 px ขณะที่กลิฟไทยกว้าง 15-24 px
   · บรรเทาแล้วด้วยการ **วาดกลิฟไว้กลาง advance** (แทนชิดซ้าย) — ผู้ใช้ยังไม่ได้ยืนยันผลบนจอ
2. **สระ/วรรณยุกต์ลอยประมาณ 3 ตัวต่อ 100 ตัวอักษร** — คลัสเตอร์ที่ไม่ได้เซลล์ต้องแตกเป็นฐาน+มาร์ก
3. ทั้งสองข้อจบได้ถ้าหา **ตาราง width** เจอแล้วแก้ค่า (ดูหัวข้อถัดไป)

### เส้นทางที่เหลือ: หาตาราง width ให้เจอ
เป้าหมายถ้าแก้ได้: ตั้ง advance ของมาร์ก = 0 (ซ้อนบนฐานจริง เลิก pre-compose) และตั้ง advance
ของฐาน = ความกว้างกลิฟ + ช่องไฟ (ระยะธรรมชาติ) → จบทั้งสองอาการ และเซลล์เหลือเฟือ

ตรวจไปแล้ว (อย่าทำซ้ำ):
- ❌ ไม่ได้อยู่ในไฟล์ฟอนต์: `meta_ot_cond_book.dds` ไม่มี `.bin` คู่ · `gothic.bin`/`symbol.bin`
  correlation กับค่าที่วัดจริง < 0.3
- ❌ ไม่ได้อยู่ใน `ui.judge.en.par`: แตกครบแล้ว `en/font/` มี 36 ไฟล์ ทุกไฟล์ 5,456 ไบต์ เป็นตาราง
  ARMP 256 แถว แต่เป็น **cp → sprite index ของฟอนต์ตัวเลข UI** (col1=texture id, col3=index) ไม่ใช่ความกว้าง
- ❌ สแกน `Judgment.exe` (394 MB) ด้วยลายเซ็นความกว้าง ink ของ ASCII — ไม่เจอ
- ❌ สแกน RAM 5.6 GB ด้วยลายเซ็น 202 ค่า — ไม่เจอ (**ลายเซ็นผิดเอง**: ใส่ค่า 36/38 ที่เป็น
  ค่า default ของเซลล์ว่างปนไปด้วย ซึ่งน่าจะไม่ได้เป็น entry ในตาราง)
- ⏳ กำลังรัน/ยังไม่จบ: สแกน exe + RAM ด้วย **ลายเซ็นที่ถูก = 62 codepoint ที่มี advance จริง (ค่า 9-32)**
  สคริปต์: `scratchpad/scan_exe_focus.py` (ไฟล์) และ `scripts/patch_widths_mem.py --scan` (RAM ต้องเปิดเกมค้าง)

เครื่องมือพร้อมแล้ว: `scripts/patch_widths_mem.py` (หาโปรเซส · เดินหน่วยความจำ · อ่าน/เขียน ·
ค้นด้วย correlation) — ยังไม่เคยเจอเป้า จึงยังไม่ได้ทดสอบส่วนเขียน

### ✅ ผลตรวจม็อดไทยเก่า MOD2SUB (แกะซิปเทียบไฟล์ต่อไฟล์ 22 ส.ค. 2026)
`C:/Users/BigNut/Downloads/JUDGMENTMOD2SUBTHENGoogleV1.2-.../JusgmentModThaiV1.2.zip`
- แก้แค่ **`meta_ot_cond_book.dds`** ไฟล์เดียว (วาดไทยลงเซลล์ donor เหมือนเรา · 196 เซลล์ ·
  **ไม่มี pre-compose เลย** = สระลอยหนักกว่าเรา)
- `tbgm_0p_ja` / `gothic` / `symbol` / `yakuza` **เหมือนต้นฉบับ 100%** · **ไม่แตะ exe**
- สรุป: ไม่มีทางลัดที่เราพลาด เขาชนกำแพงเดียวกันแล้วยอมรับมัน

### บทเรียนสำคัญของ session นี้ (อย่าให้เกิดซ้ำ)
1. **ห้ามเดา advance** — เดา ±4 px ทำให้ตัวอักษรวาดทับกันจนดูเหมือน "ตัวหาย" (ง ทับ ค, า ทับ ก)
   ตอนนี้ `translations/donor_widths.json` วัดจริงครบ 202/202 ไม่มีค่าเดาเหลือ
2. **ผังของ probe ต้องอ่านจากไฟล์ที่ deploy จริง** (`title_root.bin`) ห้ามคำนวณซ้ำ —
   คำนวณซ้ำหลังไฟล์เปลี่ยน ทำให้ค่าที่วัดไปลงผิด codepoint ทั้งแถว
3. **แถวที่เคอร์เซอร์เมนูเลือกอยู่ = ตัวมืดบนแถบขาว** ต้องกลับขั้ว mask ถึงจะวัดได้ (เสียไป 1 รอบ)
4. **ข้อความที่ Windows เป็นคนวาด (MessageBox ตอน Alt+F4) ต้องคง EN** — ฟอนต์ระบบไม่มีกลิฟไทย
   ของเรา จะโผล่เป็นละตินมั่ว → คีย์ `Quit game and return to desktop?...` ใน `msg.bin` ล็อก EN แล้ว
5. **บทคัตซีน (`auth.bin/cinema_telop`) ไม่มีคอลัมน์ผู้พูด** → ห้ามเดาเพศ ถ้าระบุไม่ได้ใช้สำนวนกลาง

## ✅ 22 ส.ค. 2026 (รอบ 14) — วัด advance ได้ครบ + เขียนตัวจัดสรรใหม่ทั้งชุด

### ผล probe หวี (ภาพผู้ใช้ `shots/comb.png`)
| สิ่งที่วัด | ค่า |
|---|---|
| scale | 0.77 px จอ ต่อ 1 px atlas |
| advance ของ `M` | 28 px atlas (ink 22 -> side bearing 6) |
| **เซลล์ว่างใน Latin Ext-A ทุกช่อง** | **36 px เท่ากันหมด** (กว้างกว่าเซลล์ 32 px) |
| เซลล์ที่เป็นตัวอักษรจริงในตาราง exe | 11-32 px ตามตัวอักษร (¢ £ ¤ ¦ § ... วัดได้รายตัว) |
| **เอนจิ้นตัดกลิฟตาม advance ไหม** | **ไม่ตัด** — แถว `MM¡¡¡¡MM` ตัว M ล้นทับกันเป็นก้อน |
| วัดได้จริง | 121 donor · เดา 26 (แถวที่โดนแถบไฮไลต์เมนูบัง) · ประมาณจาก ink 69 |
ผลอยู่ใน `translations/donor_widths.json` (หน่วย px ของ atlas = advance จริง ไม่ใช่ ink)

**นี่คือคำตอบว่าทำไมตัวห่าง**: กลิฟไทยกว้าง 15-24 px แต่ 129 จาก 202 เซลล์มี advance 36 px
→ เหลือช่องว่าง 12-20 px ต่อตัว และตัวจัดสรรเดิม "เดา" ความกว้าง donor ที่วัดไม่ได้ จึงจับคู่มั่ว

### ตัวจัดสรรใหม่ (`slot_alloc.py` เขียนใหม่ตั้งแต่ demand ถึง encode)
- `MARKS_PER_CELL` 1 -> **2** : `ที่ นี้ ได้ ต้อง` เป็นกลิฟเดียวได้แล้ว (นี่คือต้นเหตุ "สระลอย"
  ที่เห็นบนจอ — คำที่มี ฐาน+สระ+วรรณยุกต์ คือคำที่ใช้บ่อยที่สุดในภาษาไทย)
- donor_w เปลี่ยนความหมายจาก "ความกว้าง ink" เป็น **advance จริง** → จับคู่ด้วยช่องไฟที่เหลือ
  (`fit()` คืน slack) ยูนิตความถี่สูงได้ donor ที่พอดีที่สุดก่อน
- รองรับ **ยูนิตหลายคลัสเตอร์ในเซลล์เดียว** (เพราะเอนจิ้นไม่ตัดกลิฟ) — `encode()` จับคู่ยาวสุดก่อน
- `inject_thai_title.py` วาดยูนิตหลายคลัสเตอร์ได้ (`_split_clusters` + `_draw_cluster`)

### เลือกกลยุทธ์ด้วยการจำลอง ไม่ใช่ความรู้สึก (`scratchpad/sim.py`)
วัดสองค่าจากคลังจริง 4,000 ประโยค: advance เฉลี่ยต่อตัวอักษร + จำนวนมาร์กลอยต่อ 100 ตัว

| กลยุทธ์ | advance/ตัว | มาร์กลอย/100 |
|---|---|---|
| **A ตัวเดี่ยว + คลัสเตอร์ (เลือกใช้)** | **23.89** | **3.26** |
| B ตัวเดี่ยว + คู่ | 28.75 | 26.54 |
| C ตัวเดี่ยว + คลัสเตอร์ 120 + คู่ | 23.87 | 3.85 |
| D ตัวเดี่ยว + คลัสเตอร์ 60 + คู่ | 24.91 | 8.82 |
บทเรียน: **ยูนิตคู่กินเซลล์ที่คลัสเตอร์ต้องใช้ ทำให้สระลอยมากขึ้น** จึงจัดคลัสเตอร์ก่อนเสมอ
(ค่าอ้างอิง: ธรรมชาติของฟอนต์ = 19-20 px/ตัว → ตอนนี้กว้างกว่าธรรมชาติ ~20-25% แต่สม่ำเสมอ)

### สถานะบิลด์
`slot_alloc --write` (198/202 เซลล์ · กลิฟเดียว 96.63%) → `inject --slotmap` → `build_text`
(157 bin · 62,7xx สตริง) → deploy แล้ว · test_slot_alloc 6/6

## 🔎 22 ส.ค. 2026 (รอบ 13) — ผลบิลด์จริงบนจอ: เจอ 3 อาการ แก้ไป 2 เหลือ 1 รอวัด

ผู้ใช้เล่นบิลด์เต็มแล้วส่งภาพ 6 ใบ (ไตเติล / เมนู / จอเซฟอัตโนมัติ / ซับบทสนทนา 3 ใบ)

### อาการ 1 — กล่องสี่เหลี่ยม (tofu) ⛔ **สาเหตุ: Latin Extended-B เอนจิ้นไม่รองรับ**
เซลล์ที่ขึ้นกล่องคือ `บั`=U+0184 และ `มู`=U+018F ทั้งคู่อยู่ช่วง **U+0180-019F = Latin Extended-B**
(ไม่ใช่ Ext-A อย่างที่เข้าใจกันมาตั้งแต่รอบ 3 — Ext-A จบที่ U+017F) เซลล์ใน atlas มีหมึกครบ
= ปัญหาอยู่ที่ mapping ในเอนจิ้น ไม่ใช่ฝั่งเรา · รอบ 3-12 ทดสอบไม่เกิน U+017F จึงไม่เคยเจอ
→ แยก tier `extb` ออกจาก `DEFAULT_TIERS` ถาวรใน `slot_alloc.py` (pool 234 -> **202 ช่อง**)
ผลข้างเคียง: cluster ที่เคยได้ช่องตกไป fallback เพิ่ม (กลิฟเดียว 98.85% -> 97.97% · อ่านออกยัง 100%)

### อาการ 2 — สระ/วรรณยุกต์ลอย + ช่องไฟห่างเป็นช่วง ⏳ **ต้องวัดความกว้าง donor**
ช่องไฟห่างเฉพาะ **หลังเซลล์ที่ใช้ donor ซึ่งเดิมเป็นเซลล์ว่างใน atlas** (ยังไม่รู้ advance 151 ช่อง)
เพราะ advance มาจากตาราง width ใน exe → เกมเลื่อนเคอร์เซอร์กว้างกว่ากลิฟจริง มาร์กที่ตามมา
(กรณี cluster 2 มาร์กที่ต้องแตกเป็นเซลล์เดี่ยว) จึงไปตกทางขวาแทนที่จะซ้อนบนฐาน
- ลองหาตารางใน `Judgment.exe` (394 MB) ด้วย `scripts/find_width_table.py` (สแกน u8/u16/f32
  หลาย stride · กรองด้วยอสมการความกว้าง ASCII แล้วค่อยคิด correlation) — **u8 stride 1 ไม่เจอ**
- จึงทำ **probe หวี** วัดทั้ง 151 ตัวได้ในภาพเดียว:
  `scripts/title_comb.py` (ผัง) · `scripts/measure_comb.py` (อ่านภาพ) · `scripts/deploy_probe.py`
  (สลับเกมไป-กลับระหว่างบิลด์เล่นจริงกับ probe ด้วยคำสั่งเดียว)
  หลักการ: วาดขีดตั้งเหมือนกันทุกเซลล์ที่ไม่รู้ค่า เรียงเป็นแถวในเมนูไตเติล — ระยะระหว่างขีด = advance
  แถวแรก `MMMMMMMM` เป็นแถวเทียบมาตราส่วน (M ของเกมเอง รู้ ink width จาก atlas)
- **แถวสุดท้ายเป็นคำถามที่ตัดสินสถาปัตยกรรมทั้งหมด**: `MM¡¡¡¡MM` โดยเซลล์ `¡` (advance แคบ)
  ถูกวาดเป็นกลิฟ M กว้าง — ถ้าเอนจิ้น **ไม่ตัด** กลิฟตาม advance (กลิฟล้นไปทับตัวถัดไป)
  แปลว่าทำ "ฐานบน donor advance แคบ + มาร์กในเซลล์ถัดไป" ได้ = ประกอบสระ/วรรณยุกต์ได้ทุกคู่
  โดยไม่ต้อง pre-compose ทุกคลัสเตอร์ → ปม "ต้องการ 435 เซลล์ มีจริง 202" จบทันที

### อาการ 3 — เพศผู้พูดในคัตซีนไม่ตรงตัวละคร ✅ แก้ฉากที่ผิดแล้ว
**สาเหตุเชิงโครงสร้าง: `auth.bin/<ฉาก>/cinema_telop` ไม่มีคอลัมน์ผู้พูดเลย** (มีแค่เวลาเริ่ม/จบ
และข้อความ 2 ชุด = ชุดซับ JA กับชุดพากย์ EN) นักแปลจึงไม่มีข้อมูลให้ค้น ต้องอาศัยบริบทฉากล้วน
→ เครื่องมือใหม่ `scripts/audit_cinema_gender.py` (+ `docs/cinema_gender_audit.md`)
ทั้งเกมมีบรรทัดลงท้ายแบบหญิงแค่ **51 บรรทัดใน 6 ฉาก** · ตรวจทีละฉากแล้ว:
- `a05_020` `a05_040` = เทราซาวะ (หญิง ยืนยันจากบท "I'm Terasawa") · `a13_190` `a01_060`
  `a01_090` = พนักงานหญิงในสำนักงาน → **ถูกอยู่แล้ว ไม่แตะ**
- `a01_010` (ออฟฟิศเก็นดะรับโทรศัพท์) = ฉากที่ผิดจริง — ภาพผู้ใช้เห็นพนักงาน**ชาย**กำลังพูด
  บรรทัดที่แปลลงท้าย ค่ะ → **ตัดคำลงท้ายบอกเพศออก 16 บรรทัด** (batch `CINEMA_A01010`)
  เก็บ ค่ะ ไว้เฉพาะบรรทัดที่บทระบุว่าซาโอริรับสาย ("Genda Law, Saori speaking")
  เหลือบรรทัดเสี่ยงทั้งเกม 35 บรรทัด (ตรวจแล้วว่าเป็นผู้หญิงจริงทุกบรรทัด)
**กติกาใหม่สำหรับบทคัตซีน: ถ้าระบุผู้พูดไม่ได้ ห้ามเดาเพศ — ใช้สำนวนกลาง**

### อาการ 4 (เจอเอง ไม่ได้อยู่ในรายงานผู้ใช้) — เมนูยังเป็นอังกฤษ
`CONTINUE` `SETTINGS` `REPLAY` `EASY/NORMAL/HARD/LEGEND` ฯลฯ ไม่เคยเข้าคิวแปลเลย เพราะ
`is_translatable()` ตัดคำ ALLCAPS ยาว >3 ทิ้ง (กติกากัน SCREAMING_ENUM ที่ port มาจาก K3)
→ เลิกตัดด้วยรูปคำ (เหลือกันแค่ >16 ตัวอักษร) + ย้าย `minigame_live_chat_chat_commands.bin`
(คำสั่งแชตโรมาจิ 291 คำ) เข้า `KEEP_EN_BINS` → collect ใหม่ได้ unique 53,912 (+321)
→ แปลเพิ่ม 30 คู่ผ่าน merge_qc (batch `UICAPS`) → **master_th 50,297 คู่**

### สถานะเกม ณ ตอนนี้
ในเกมคือ **บิลด์ probe หวี** (เมนูไตเติลเป็นแถวขีด) รอผู้ใช้แคปภาพเป็น `shots/comb.png`
แล้วรัน `measure_comb.py` → `deploy_probe.py --play` เพื่อกลับไปบิลด์ไทยเล่นจริง

## ✅ 22 ส.ค. 2026 — ต่อสายครบทั้งเส้น: ฟอนต์ + ข้อความทั้งเกม บิลด์และ deploy แล้ว

ปิดงานข้อ 2, 3 และ 5 ของ "งานถัดไป" รอบสปรินต์สี่ในรอบเดียว — ตอนนี้ในเกมคือ **บิลด์จริง**
ไม่ใช่บิลด์ทดสอบอีกต่อไป

### สิ่งที่ทำ (ทำซ้ำได้ด้วย 3 คำสั่งนี้ ตามลำดับ)

```
python scripts/slot_alloc.py --write --probe          # จัดสรร 234 เซลล์จากคลังจริง 50,267 คู่
python scripts/inject_thai_title.py --slotmap         # วาดกลิฟทั้ง 234 เซลล์ลง atlas
python scripts/build_text.py --workers 8 --clean      # บิลด์ 156 bin จาก master_th
python scripts/deploy_spoil.py                        # drop-in ฟอนต์ + mods + regen MLO
```

| ขั้น | ผล |
|---|---|
| slotmap (regen จากคลังปิดคิวแล้ว) | ต้องการ 435 เซลล์ · จัดสรร 234 · กลิฟเดียว 98.846% · **อ่านออกรวม 100%** |
| ฟอนต์ `build/font/meta_ot_cond_book.dds` | แก้ 234 เซลล์ · เซลล์ที่ EN ใช้ (© ® ¥ ± ÷ é ê ö ü ...) ไม่ถูกแตะ (ตรวจกลับ bit-identical) |
| ข้อความ `build/text/db.judge.en/en/` | **156 bin · แทนที่ 62,718 สตริง · ประโยคไทย unique 48,809 · encode ไม่ผ่าน 0 · บิลด์ล้มเหลว 0** (5 วินาที) |
| deploy | 157 ไฟล์เข้า `mods/JudgmentThai/db.judge.en` (156 + `ui_layer_text.bin` ที่แพตช์ระดับไบต์) · MLO 7,817 B |

### เครื่องมือใหม่/ที่เปลี่ยน
| ไฟล์ | ทำอะไร |
|---|---|
| `scripts/build_text.py` (**ใหม่**) | บิลด์ข้อความทั้งเกม: `strings_by_bin.json` × `master_th.json` → `SlotMap.encode()` → reARMP → `build/text/db.judge.en/en/*.bin` · ขนานด้วย `--workers` · ข้าม `DENY_BINS`/`KEEP_EN_BINS`/`RAW_BINS` · ตรวจกลับระดับไบต์ทุก bin · เขียน `build/text/build_report.md` |
| `scripts/inject_thai_title.py --slotmap` | โหมดผลิตจริง — วาดทุกเซลล์ตาม `SlotMap.glyph_plan()` แทนผังทดสอบที่ hardcode ไว้ |

**ฟอนต์กับข้อความอ่าน map เดียวกันแล้ว** (`translations/slotmap.json`) — แก้การจัดสรรที่เดียว
แล้วรันสองคำสั่งข้างบนใหม่ ทั้งสองฝั่งตรงกันเสมอโดยโครงสร้าง

### ตรวจแล้วว่าเส้นทางถูกต้อง (ไม่ใช่แค่ไฟล์ออกมา)
- roundtrip: `title_root.bin` ที่บิลด์แล้ว → reARMP decode → `SlotMap.decode()` ได้ไทยเดิมกลับมาครบ
  (87 สตริง เช่น "เริ่มเกมใหม่" "เล่นต่อจากเกมที่บันทึกไว้")
- `python scripts/test_slot_alloc.py` = 6/6 (รวมข้อ 5: encode ทั้งคลัง 96,415 ประโยคไม่ throw)

### 🔜 งานถัดไป
1. ⏳ **ผู้ใช้เปิดเกมทดสอบบิลด์จริง** — ดูสามอย่าง: (ก) ข้อความไทยขึ้นครบทุกจอไหม
   (ข) ช่องไฟเพี้ยนตรงไหน (= เซลล์ที่ใช้ donor ที่ยังไม่รู้ความกว้าง 183 ช่อง)
   (ค) `ui_layer_text.bin` (MISSION/TIPS) ทำให้แครชไหม — ถ้าแครช ลบไฟล์นี้ไฟล์เดียวออกจาก mods
2. วัดความกว้าง donor 183 ช่องที่เหลือ (แผน `build/text/WIDTH_PROBE.md`) → `translations/donor_widths.json`
   → รัน slot_alloc + inject + build ใหม่ (ตอนนี้ 33 เซลล์ยังบีบเกินเพดาน 15%)
3. ถอนบิลด์ได้ทุกเมื่อ: `python scripts/deploy_spoil.py --restore`

> **อัปเดตล่าสุด 21 ส.ค. 2026 — ✅ คิวแปลปิดครบทั้งเกม: `master_th.json` 50,267 คู่ (205/205 batch
> แปล+ตรวจ+merge ครบ)** · QC ทั้งคลังผ่านหมด (รายละเอียด + งานถัดไปอยู่หัวข้อ "สปรินต์แปลรอบที่สี่")
> งานที่เหลือทั้งหมดเป็นฝั่งเทคนิค: วัดความกว้าง donor → ต่อสายฟอนต์กับ slotmap → บิลด์ deploy

> อัปเดตก่อนหน้า: 20 ส.ค. 2026 — ทีมเก็บข้อมูลเนื้อหา 6 เอเจนต์ส่งงานครบ (story/ตัวละคร/side content/glossary/RGG universe)
> ก่อนหน้านั้นรอบเดียวกัน: extract ครบ 1,358 bin · เขียน `docs/research.md` · วางระบบ
> slot allocator (`scripts/slot_alloc.py` → `translations/slotmap.json`, ทดสอบผ่าน 6/6)
> **session ใหม่: อ่าน `docs/research.md` ก่อน แล้วค่อยไล่ HANDOFF ตามต้องการ**

## ✅ ทีมเก็บข้อมูลเนื้อหาในเกม — เสร็จครบ 6 เอเจนต์ (20 ส.ค. 2026)

Phase 1 (เตรียมข้อมูลให้นักแปล) จบแล้ว — ก่อนสั่งทีม lead ดึง "ข้อเท็จจริงจากไฟล์เกม" ออกมาก่อน
ด้วย `scripts/make_translator_facts.py` → `extracted/facts/*.json` +
`docs/reference/judge_extract_facts.md` (ผู้พูด 473 แถว / 439 ชื่อไม่ซ้ำ · บท 13 · missions 550 ·
friends 54 · evidence 103 · scenario summary 62 · items 1,071 · skills 126 · complete 499 ·
places 182 · shops 46 · manual 200) แล้วเขียนบรีฟทีมที่ `docs/reference/DATA_COLLECTOR_BRIEF.md`

### ผลงานที่ส่งแล้ว

| ไฟล์ | เนื้อหา |
|---|---|
| `docs/story_context_judge.part1/2.md` | เนื้อเรื่องครบ 13 บท (เหตุการณ์ · ตัวละคร · หลักฐานที่คืบหน้า · จุดที่นักแปลต้องระวัง) + จุดเชื่อมจักรวาล RGG |
| `translations/characters_main.json` | ตัวละครหลัก 27 ตัว (บทบาท/บุคลิก/โทนเสียง/สรรพนามรายคู่/สปอยล์ที่ต้องระวัง) |
| `translations/characters_side.json` | 68 กลุ่ม — เพื่อนแยกรายคน 52 + กลุ่มหมวด 16 · ครอบคลุมชื่อผู้พูดครบ |
| `translations/glossary.md` | คำล็อกจากภาคก่อน 29 + เสนอใหม่ 92 (เน้นศัพท์กฎหมาย/สืบสวน 24) |
| `translations/PRONOUN_MATRIX.md` | ตารางสรรพนามตามคู่ความสัมพันธ์ + กฎ fallback |
| `docs/side_content_context_judge.md` | Side Case 50 · เพื่อน 54 · แฟน 4 · มินิเกมครบชุด · ร้าน 46 · completion 34 หมวด |
| `docs/reference/rgg_universe_context.md` | ไทม์ไลน์ซีรีส์ · คามุโรโจ 101 · ตระกูล/องค์กร · ตัวละครข้ามภาค · ของประจำซีรีส์ + คำล็อก |
| `docs/research_characters_judge.md` / `_side_judge.md` | รายงานเหตุผลการตั้งชื่อ + กับดักที่เจอ |

### ค้นพบสำคัญ: Judgment มีคำแปลไทยที่ ship แล้วอยู่ก่อน

Judgment เคยรับเชิญใน Gaiden (โคลอสเซียม) และมีข้อความตกค้างในตารางร่วมของ Dragon Engine ฝั่ง Y7
→ มีคำล็อกอยู่แล้วมากกว่าที่ CLAUDE.md รุ่นแรกเข้าใจ (ซึ่งบอกว่ามีแค่ Kaito):
`Yagami → ยากามิ` · `Yagami Detective Agency → สำนักงานนักสืบยากามิ` · `Toru Higashi → โทรุ ฮิงาชิ` ·
`Matsugane (Family) → มัตสึกาเนะ / ตระกูลมัตสึกาเนะ` · `Kyorei Clan → ตระกูลเคียวเรอิ` ·
`Mafuyu → มาฟุยุ` · `Kuroiwa → คุโรอิวะ` · `Genda-sensei → เก็นดะเซนเซ` · `"the Mole" → ไส้ศึก`

ยืนยันจากคำที่ ship จริงใน `yakuza-gaiden/translations/master_th.json` (ยากามิ 7 จุด · ฮิงาชิ 11 ·
มัตสึกาเนะ 2) และ `glossary_y7.md` tranche 18 (บรรทัด 446-449, 807)

### คำตัดสินของ lead รอบนี้ (มีหลักฐาน ไม่ต้องถามซ้ำ)

1. **Yagami = ยากามิ** (ไม่ใช่ "ยางามิ" ที่เอกสารรุ่นแรกของ repo นี้ใช้) — `glossary_gaiden.md`
   บรรทัด 80 บันทึกไว้เองว่า lead เคยแก้จาก ง เป็น ก มาแล้วตามกฎ g กลางคำ = ก
2. **Matsugane = มัตสึกาเนะ** — Gaiden ship จริงชนะ Y7 ที่เคยเขียน "มัตสึงาเน" (ตาม priority ใหม่กว่าชนะ)
3. **Kyorei = ตระกูลเคียวเรอิ**
4. **ไทม์ไลน์**: Judgment (2018) อยู่ก่อนการยุบตระกูลโทโจ (Y7, 2019 — ไม่ใช่ Y6 อย่างที่
   `story_context_y7.md` ของ repo K3 เขียนผิดไว้) → แปลโดยถือเส้นเวลาเดียวกับซีรีส์หลักได้เลย
   ⚠ ประโยคที่ผิดอยู่ใน repo K3 — จดไว้แก้ตอนกลับไปทำภาคนั้น

เครื่องมือกวาดคำ: `scripts/normalize_terms.py` (`--write` เพื่อแก้จริง) — แก้ไปแล้ว 191 จุด
สคริปต์**ข้าม** `CLAUDE.md`/`HANDOFF.md` โดยตั้งใจ เพราะสองไฟล์นี้เก็บตัวอย่างคำผิดไว้เตือน

### ✅ คำตัดสินของผู้ใช้ 20 ส.ค. 2026 (ล็อกแล้ว บันทึกลง glossary/PRONOUN_MATRIX/characters_main แล้ว)

| เรื่อง | คำตัดสิน |
|---|---|
| สรรพนามยากามิ | **"ผม" ทุกฉาก** รวมกับไคโตะ — ห้ามสลับเป็น "ฉัน" รายฉาก (ความกันเองสื่อผ่านคำเรียก/คำลงท้ายแทน) · แยกเสียงจากคิริวที่ล็อก "ฉัน" |
| `alibi` | **พยานที่อยู่** (ศัพท์กฎหมายไทยจริง) — ห้ามทับศัพท์ "อาลิไบ" |
| Crane / Snake / Tiger Style | **ท่ากระเรียน / ท่างู / ท่าเสือ** (แปลความหมาย) ⚠ ตั้งใจต่างจากคำล็อก Y7 ที่ใช้ "สไตล์" |
| Saori Shirosaki vs Shiosaki | **ชิโรซากิ** — นับในไฟล์เกม: `Shirosaki` 22 ครั้งใน 6 bin vs `Shiosaki` 1 ครั้ง (typo จุดเดียวใน `evidence_item_to_update.bin`) |

### รอบเสริม 21 ส.ค. 2026 — ระบบสรรพนามจับคู่ + พิสูจน์เพศ (คำสั่งผู้ใช้)

**กฎใหม่ (บังคับทั้งโปรเจกต์ ทับกฎเดิมที่ขัดกัน)** — เขียนไว้ที่ `translations/PRONOUN_MATRIX.md` §0:
สรรพนามต้องมาเป็นคู่ · **T1 ผม/ดิฉัน ↔ คุณ** (ทางการ ครับ/ค่ะ) · **T2 ฉัน ↔ แก** (กันเอง) ·
**T3 กู ↔ มึง** (หยาบ) · ห้ามผสมข้ามระดับ · ยากามิ = T1 เสมอ ห้าม T3 (กับคนสนิทเรียกชื่อแทน "คุณ" ได้)

**§0.1 กติกาพิสูจน์เพศก่อนแปล**: ห้ามเดาเพศจากชื่อ ต้องมีหลักฐานจากไฟล์เกม (สรรพนาม EN he/she ·
Mr./Ms. · sir/ma'am · บทบาทที่ระบุเพศ · honorific -kun/-chan = หลักฐานอ่อน ใช้เดี่ยวไม่ได้)
พิสูจน์ไม่ได้ = `gender: unknown` แล้วแปลเลี่ยงสรรพนาม/คำลงท้ายบอกเพศ

**ผลที่ลงไฟล์แล้ว**
- `characters_main.json` (27) + `characters_side.json` (68) มีฟิลด์ `pronoun_tier` ทุก entry และ
  สรรพนามถูกเขียนใหม่ให้จับคู่ถูกระดับ · main: T1 16 · T2 3 · T3 3 · สลับตามบริบท 1 (Ayabe) ·
  ไม่มีบทพูดสด 5
- ฟิลด์ `gender` / `gender_confidence` / `gender_evidence` ผสมเข้าไฟล์ตัวละครแล้วด้วย
  `scripts/apply_gender.py --write` (94 entry) — หลักฐานเต็มที่
  `extracted/facts/gender_evidence.json` + `docs/reference/gender_evidence_judge.md`
- **ตัวหลัก 27/27 พิสูจน์ได้ทั้งหมด confidence สูง** (ชาย 24 · หญิง 3: Shirosaki, Fujii, Terasawa)
- **ยังพิสูจน์ไม่ได้ 12 รายการ — นักแปลต้องเลี่ยงสรรพนาม/ครับ-ค่ะ กับกลุ่มพวกนี้**:
  `friend_hatano` `friend_xiu` `friend_kyushu_no1_star_owner` `friend_amamiya` `friend_tachibana`
  `friend_fukutsu` `friend_ida` + กลุ่มรวม `police` `media_press` `mystery_placeholder`
  `tanaka_imposter_case` `meta_system`
- แก้ข้อมูลผิดที่ทีมพิสูจน์เพศจับได้: **"Zhuang Shi" ไม่ใช่คน — เป็นแมว**
  (`talk.bin.json`: "Zhuang Shi isn't my cat. He is the pet cat of...") ย้ายจากกลุ่ม `foreign_gang`
  ไป `animal_mascot` แล้ว

**เครื่องมือบังคับกฎ**: `scripts/check_pronoun_pairs.py` จับการผสมข้ามระดับ ("ผม…มึง", "กู…ครับ",
สองระดับในบรรทัดเดียว) · โหมด `--docs` ข้ามข้อความที่เป็นคำอธิบายกฎ · ใช้กับ `master_th.json`
ทุก batch ตอน QC · `scripts/test_pronoun_pairs.py` ผ่าน 15/15 (รวมเคสหลอกที่สำคัญ: ยากูซ่า/แก๊ง/
คุณภาพ/แกง/ฉันทะ/เส้นผม ต้องไม่ถูกจับผิด) · ตอนนี้สแกนไฟล์ตัวละคร+matrix ได้ 0 ปัญหา

### ค้างเชิงเทคนิค (⏳)

- สรรพนาม/คำเรียกจริงต้องยืนยันกับบทพูดใน `talk.bin.json` ตอน batch แปลแรก (ตอนนี้อนุมานจากบทบาท)
- ยศยากูซ่า "Captain"/"Patriarch" ยังไม่มีคำไทยล็อก
- wiki เข้าไม่ได้รอบนี้ (`judgment.fandom.com` ติด CAPTCHA แม้ผ่าน r.jina.ai · IGN 403)
- typo ในไฟล์เกมจริง: `judge_m_BTL13_0020.mission_info` สะกด "Matsunage" (ควรเป็น Matsugane)
- `docs/story_context_judge.part1/2.md` ไฟล์ละ ~45 KB (เกินเกณฑ์ ~40 KB เล็กน้อย ตั้งใจไม่แตกเพิ่ม)

## ✅ งานรอบล่าสุด 20 ส.ค. 2026 — extract ครบ 1,358 bin + `docs/research.md` + ระบบ slot allocator

### 1. extract ครบทั้ง par แล้ว

- `scripts/extract_all_en.py` (port จาก K3, แก้ให้ชี้ `extracted/db_en/en/`) แปลง **1,358 bin →
  JSON สำเร็จ 1,351** ใน 149 วินาที (10 workers)
- ผลลัพธ์: `extracted/strings_by_bin.json` · `extracted/unique_strings.json` ·
  `extracted/extract_report.md` · JSON คู่ `.bin.json` อยู่ข้าง ๆ ไฟล์ bin
- ตัวเลข: **unique string 53,591** · bin ที่มีข้อความ 213 · แถวรวมทุก bin 376,263
- ARMP **v2** · มี sub-table ซ้อน (บทสนทนาอยู่ลึกหนึ่งชั้น: `/<row>/<talk_id>/text/<n>//3`)
  → **ห้ามนับงานแปลจาก `ROW_COUNT`**
- **fail 7 ไฟล์** — 6 ตัวเป็นตาราง dev/พารามิเตอร์ (ข้ามได้) แต่ **`ui_layer_text.bin` มีข้อความจริง**
  (`MISSION` `TIPS` `Even Odd` `2to1` `1-18 19-36` = ป้ายคาสิโน/รูเล็ต) → ต้องเลือกระหว่าง
  byte-patch (`scripts/patch_bin_strings.py`) หรือคง EN — ยังไม่ตัดสิน
- สารบัญเต็มต่อไฟล์: `scripts/make_bin_index.py` → `extracted/bin_index.json` + `docs/bin_index.md`

### 2. `docs/research.md` — เอกสารข้อเท็จจริงหลักของโปรเจกต์

รวม 8 หัวข้อ: โครงไฟล์เกม · ผล extract + โครง ARMP + bin ที่ fail · bin ที่มีข้อความ (top-15 +
กับดัก false positive) · **สถาปัตยกรรมฟอนต์ที่พิสูจน์บนจอแล้วทั้ง 7 ข้อ** · ระบบ slot allocator ·
เส้นทาง deploy · ช่องว่างความรู้ที่เหลือ 7 ข้อ · บทเรียนสำหรับ Lost Judgment
→ session ใหม่อ่านไฟล์นี้ไฟล์เดียวก็ตามงานทันโดยไม่ต้องไล่ HANDOFF ทั้งไฟล์

### 3. ระบบ slot allocator (ของใหม่รอบนี้ — พร้อมใช้ผลิตจริง)

`scripts/slot_alloc.py` ตัดสินว่า 384 เซลล์ของ `meta_ot_cond_book` จะถูกแบ่งอย่างไรทั้งเกม
เขียนผลเป็น **`translations/slotmap.json`** ที่ฝั่งฟอนต์กับฝั่งข้อความอ่านร่วมกัน (map เดียว)

- **pool 234 ช่อง** = Latin-1 letter 64 + Latin Ext-A 160 + Latin-1 symbol 32 − สงวน 22
- **กันชนสองทาง (คิดจากข้อมูลจริง ไม่ใช่เดา)**: cp ที่ข้อความอังกฤษของเกมใช้ 18 ตัว
  (`NBSP ¥ © ® ± à á ã ä ç é ê í ñ ó ö ú ü`) + cp ที่คำแปลไทยเองใช้อีก 4 (`° · × ÷`)
  → allocator หักออกอัตโนมัติ และ `SlotMap.encode()` จะหยุดพร้อมบอกตัวที่ชนถ้าเจอในข้อความ
- **นโยบาย: ฐาน + มาร์ก 1 ตัว** ต่อเซลล์ · จัดสรรตัวบังคับก่อน (พยัญชนะ 44 + สระเดี่ยว 11 +
  มาร์กเดี่ยว 16 = ไม่มีทางเจอ tofu) แล้วเติม cluster ตามความถี่จริงจากคลังแปลที่ ship แล้ว
  3 ภาค (K3 + Gaiden + Y6 = **96,415 ประโยค / 3,228,722 cell occurrence**)
- **ผล: กลิฟเดียว 98.81% · เรนเดอร์ได้ 100.00%** (ที่เหลือ 1.19% ใช้ fallback แตกฐาน+มาร์กเดี่ยว
  มาร์กเลื่อนขวาเล็กน้อย) · cluster ตกขอบ 196 ตัว ความถี่ต่ำสุด ๆ (`ซื` `ธิ` `ล์` ~700/3.2M)
- **ตรวจแล้ว**: `python scripts/test_slot_alloc.py` ผ่าน **6/6** (ไม่แตะ ASCII · ไม่ชน EN ·
  `decode(encode(s)) == s` ทั้งคลัง 96,415 ประโยค · ฐานไทยครบทุกตัว)
- รายงานอ่านคน + ตารางจัดสรรเต็ม: `docs/slot_alloc.md`

### 4. งานถัดไป (เรียงตามลำดับที่ควรทำ)

1. **วัดความกว้าง donor เซลล์ว่าง 183 ช่อง** (blocker เดียวของฝั่งฟอนต์ที่เหลือ)
   สมมติฐาน: เซลล์ว่างทั้ง Latin Ext-A ใช้ค่า default ตัวเดียวกันหมด (รอบ 6 เจอว่ากลุ่ม control
   ได้ระยะเท่ากันทุกตัว) → วัดแค่ 6 ตัวกระจายทั่วช่วงก็รู้ผล · แผนพร้อมที่
   `build/text/WIDTH_PROBE.md` (สร้างด้วย `slot_alloc.py --probe`) · ได้ค่ามาแล้วเติมลง
   `translations/donor_widths.json` แล้วรัน `slot_alloc.py --write` ใหม่
2. ต่อสายฟอนต์เข้ากับ slotmap: ให้ `inject_thai_title.py` รับ `SlotMap.glyph_plan()` แทน
   `title_menu_map.CELLS` (ตอนนี้ยังเป็นผังของเมนูไตเติลอย่างเดียว 35 เซลล์)
3. ต่อสายข้อความ: port `apply_thai.py`/`deploy.py` จาก K3 ให้ encode ผ่าน `SlotMap.encode()`
4. `ui_layer_text.bin` — ตัดสินว่า byte-patch หรือคง EN
5. เปิด pipeline แปล: `make_worklist.py` + DENY_BINS (คัด bin ที่เป็น identifier ล้วนออก —
   ดู ⚠ ใน `docs/research.md` §3) + speaker_map จาก `talk_talker.bin` (437 ชื่อ)

> ⚠ **ในเกมยังมีบิลด์ทดสอบรอบ 12 ค้างอยู่** (บทสนทนาทุกบรรทัดเป็นข้อความทดสอบ `เอ บี`
> + ฟอนต์ที่ฉีดไทยแล้ว) — ถอดด้วย `python scripts/deploy_spoil.py --restore` เมื่อไม่ต้องแคปแล้ว

## ✅ สปรินต์แปล — รอบที่สี่ 21 ส.ค. 2026 (**คิวแปลปิดครบทั้งเกม**)

> **`master_th.json` = 50,267 คู่ = 100% ของคิว** (205/205 batch แปลครบ ตรวจครบ merge ครบ)
> รอบนี้เดินต่อจาก 44,974 (89.5%) จนจบคิว TALK_052 – TALK_072 · ยืนยันสถานะจริงเสมอ:
> `python scripts/sprint_status.py --next 5` → "ว่างถัดไป: - (แจกครบแล้ว)"

### สถานะ QC ทั้งคลัง ณ ตอนปิดคิว (รันซ้ำได้ทุกตัว ต้องได้ผลเดิม)

| คำสั่ง | ผล |
|---|---|
| `python scripts/check_speaker_gender.py` | ขัดเพศผู้พูด **0** |
| `python scripts/check_pronoun_pairs.py --files translations/master_th.json` | **0** |
| `python scripts/fix_honorific_san.py` | **0** |
| `python scripts/check_pair_shuffle.py` | 2 คู่ (ตรวจมือแล้ว false positive ทั้งคู่ — "Why don't you…" แปลเป็นประโยคชวนแบบไทย) |
| `python scripts/normalize_terms.py` | **0** |
| `python scripts/test_slot_alloc.py` | 6/6 |
| `python scripts/test_pronoun_pairs.py` | 34/34 |
| `python scripts/test_qc_tools.py` | 14/14 (ไฟล์ใหม่รอบนี้) |

### 🧰 เครื่องมือใหม่ที่เกิดในสปรินต์สี่ (ใช้ต่อได้ทั้งภาคนี้และ Lost Judgment)

| ไฟล์ | ทำอะไร |
|---|---|
| `scripts/check_speaker_gender.py` | คำลงท้าย/สรรพนามขัดเพศผู้พูดจริง + คำล็อกสรรพนามรายตัวละคร (ต้องได้ 0 ก่อน merge) |
| `scripts/check_pair_shuffle.py` | คำแปลติดคีย์ผิด (สัญญาณ Q/D/L) — ใช้ `--min-signals 1` ต่อ batch |
| `scripts/check_skill_name_quotes.py` | ชื่อทักษะที่ถูกอ้างเป็น EN ในข้อความปลดล็อก (`--write` แก้ได้) |
| `scripts/fix_locked_name_quotes.py` | ชื่อไอเทม/ร้าน/คอร์สที่ล็อกไทยแล้วแต่ประโยคยังเป็น EN + คีย์ที่ต้องคง EN |
| `scripts/patch_bin_raw.py` | แพตช์ ARMP bin ระดับไบต์ (เติมสตริงท้ายไฟล์ + ย้าย pointer) สำหรับ bin ที่ reARMP rebuild ไม่ได้ |
| `scripts/test_qc_tools.py` | เทสต์เคสหลอกของสองตัวตรวจแรก (14/14) — แก้ regex เมื่อไรต้องรันก่อน |

### 🔜 งานถัดไป (คิวแปลจบแล้ว งานที่เหลือคือฝั่งเทคนิคล้วน)

1. **วัดความกว้าง donor เซลล์ว่าง 183 ช่อง** — blocker เดียวที่เหลือของฝั่งฟอนต์
   (แผนพร้อมที่ `build/text/WIDTH_PROBE.md` · ได้ค่าแล้วเติม `translations/donor_widths.json` แล้วรัน `slot_alloc.py --write`)
2. ต่อสายฟอนต์เข้ากับ slotmap: `inject_thai_title.py` รับ `SlotMap.glyph_plan()` แทน `title_menu_map.CELLS`
3. ต่อสายข้อความ: port `apply_thai.py`/`deploy.py` จาก K3 ให้ encode ผ่าน `SlotMap.encode()` แล้ว **บิลด์ทั้งเกมจาก master_th 50,267 คู่**
4. `ui_layer_text.bin` — build ทดสอบพร้อมแล้วที่ `build/text/db.judge.en/en/ui_layer_text.bin` (ดู §ปลดบล็อกด้านล่าง) ⏳ รอผู้ใช้เปิดเกมยืนยันว่าไม่แครช
5. ⚠ **ในเกมยังมีบิลด์ทดสอบรอบ 12 ค้างอยู่** — ถอดด้วย `python scripts/deploy_spoil.py --restore`



> เดินทีมนักแปล/ผู้ตรวจ sonnet คู่ขนานต่อจากรอบสาม · เริ่มที่ master 44,974 (89.5%)
> ดูสถานะจริงเสมอ: `python scripts/sprint_status.py --next 6`
> ขั้นตอนต่อ batch เหมือนรอบสามทุกประการ (normalize → merge_qc --dry-run → spawn ผู้ตรวจ → merge_qc --only)

### บั๊กคลาสใหม่ที่เจอรอบนี้ (สำคัญกว่าตัวเลขความคืบหน้า)

**1. คำแปลติดคีย์ผิดทั้งบล็อก (block shuffle)** — ผู้ตรวจ TALK_057 เจอ 6 คู่ EN↔TH สลับข้ามกัน
(บทของอามาเนะไปติดคีย์ของยากามิ) · `merge_qc` และ `check_pronoun_pairs` จับไม่ได้เพราะไทยถูกไวยากรณ์ทั้งคู่
→ เครื่องมือใหม่ **`scripts/check_pair_shuffle.py`** (สัญญาณ Q = EN เป็นคำถามแต่ไทยไม่มีคำถาม ·
D = ชุดตัวเลขไม่ตรง · L = สัดส่วนความยาวผิดปกติ) · ทดสอบด้วยการฉีดบั๊กจำลองแล้วจับได้ ·
**สแกน master ทั้งไฟล์ด้วยเกณฑ์ 2 สัญญาณ → 6 คู่ ตรวจมือแล้ว false positive ทั้งหมด**
= บั๊กนี้ไม่ได้กระจายทั้งคลัง · ใส่เป็นขั้นบังคับในบรีฟผู้ตรวจ + บรีฟนักแปลแล้ว

**2. ชื่อที่ล็อกแล้วไม่ตรงกันข้าม bin (44 จุดใน 6 batch)** — ตารางชื่อ (ไอเทม/ร้าน/คอร์ส/ทักษะ) กับ
ประโยคที่อ้างถึงชื่อนั้นอยู่คนละ bin คนละ batch นักแปลที่ทำประโยคไม่รู้ว่าอีก batch แปลไทยไปแล้ว
→ เครื่องมือใหม่ **`scripts/check_skill_name_quotes.py`** (ชื่อทักษะในข้อความปลดล็อก) และ
**`scripts/fix_locked_name_quotes.py`** (ไอเทม/ร้าน/คอร์ส + คีย์ที่ต้องคง EN)
รายละเอียดคำตัดสินทั้งชุดอยู่ท้าย `translations/glossary.md`

**3. กับดัก `"batch": "057"`** — คิว TALK ต้องใส่ `"TALK_057"` ตามชื่อไฟล์ · ใส่เลขเปล่าแล้ว `merge_qc`
ไปเทียบ `worklist/batch_057.json` (คนละคิว) แล้วรายงาน "ขาด 250" ทั้งที่แปลครบ · นักแปล 3 คนติดกับดักนี้
→ เขียนเตือนไว้ในบรีฟนักแปลแล้ว

### คำตัดสิน lead รอบสี่ (บันทึกลง glossary/characters_side แล้ว)
- **อามาเนะ = "ฉัน"** เป็นค่าเริ่มต้นตั้งแต่ช่วงเควสเดตเป็นต้นไป ("ดิฉัน" เฉพาะฉากแรกพบ) —
  ผู้ตรวจ TALK_057 แก้ให้ 64 จุด · ล็อกลง `characters_side.json` แล้ว
- `Ryuzenji Group` → **กลุ่มบริษัทริวเซนจิ** ("ตระกูล" สงวนให้ครอบครัวยากูซ่าเท่านั้น)
- `patriarch` → **หัวหน้าตระกูล** · `Tsumugi` → **สึมุกิ** (กันสลับพยางค์ ใส่กฎใน `normalize_terms.py`)
- `Skill App` → **แอปทักษะ** (หลุดเป็น "แอปสกิล" 3 จุด) · `embondagement` → **การจองจำรัก**
- `Serenade` → **เซเรเนด** · `Top of Ocean Hotel` → **ท็อปออฟโอเชียนโฮเทล** · `Devil Aragaki` → **เดวิลอารากากิ**
- **คง EN**: `Wette Kitchen` · `Don Quijote` · `Clan Creator` · `Motor Raid` · แฟรนไชส์ SEGA
- **ยากามิห้ามใช้ "แก" เด็ดขาด** (ผู้ตรวจเจอซ้ำ 6 จุดใน TALK_052 · 2 จุดใน TALK_056) → เขียนเป็นข้อ 1.5 ในบรีฟนักแปล
- **ผู้พูดที่ตารางขึ้น `???` (ปิดชื่อก่อนเฉลย)** — ทำตารางไว้ในบรีฟนักแปลแล้ว · ยืนยันครบรอบนี้:
  `914` ในตาราง `judge_friend_g02` = **ไดจิ ริวเซนจิ** · `914` ในตาราง `judge_friend_g04` = **ยุกโกะ**
  (คนละคนกัน — ไอดีซ้ำข้ามตารางได้) · `Debt Collector` ในตาราง `judge_friend_a51` = **คามากูจิ ก่อนเปิดชื่อ**

**4. คำลงท้าย/สรรพนามขัดเพศผู้พูดจริง + สรรพนามที่ล็อกรายตัวละคร**
→ เครื่องมือใหม่ **`scripts/check_speaker_gender.py`** เทียบคำแปลกับ **เพศผู้พูดจริงจาก `talk.bin`**
(`extracted/facts/talk_speaker.json`) และบังคับคำล็อกรายตัว (ยากามิ = "ผม" เสมอ ห้าม แก/กู/ฉัน)
ข้ามให้เองแล้ว: บรรทัดที่มี `dupes` · เพศ `unknown` · คำในเครื่องหมายคำพูด (ยกคำพูดผู้ชายมาเล่า)
**เจอของที่ ship ไปแล้ว 12 จุด** (ซานะ/สึกิโนะ/อามาเนะ/นานามิพูด "ครับ" · ยากามิพูด "ค่ะ" · ยากามิพูด
"กูขอโทษ"/"นี่ มึง!") · แก้หมดแล้ว ตอนนี้ทั้งคลัง 0
- **กติกาที่ได้จากบั๊กนี้**: คีย์ที่ใช้ทั้งใน `talk.bin` และคัตซีน (`auth.bin`/`sound_auth.bin`) **ผู้พูดคนละคนได้**
  → ต้องแปล **กลาง ไม่ผูกเพศ** ไม่ใช่สลับเพศตามตาราง (เคสจริง: `Excuse me.` `Indeed.` `Definitely!`)
- เขียนเทสต์ **`scripts/test_qc_tools.py` (14/14)** คุมเคสหลอกของทั้งสองตัวตรวจ (เส้นผม/ทรงผม/คะแนน/
  โยคะ/**โปรแกรม**/ยกคำพูดมาเล่า) · ระหว่างทางเจอบั๊ก regex ที่ใช้ร่วมกับ `check_pronoun_pairs.py`
  สองจุด (`ค่ะ` มี lookbehind ผิดจนพลาด "แน่นอนค่ะ" · "แก" ไปแมตช์กลางคำ "โปรแกรม") — แก้ทั้งสองไฟล์แล้ว

### คำตัดสิน lead รอบสี่ (ต่อ — ครึ่งหลังของสปรินต์)

- **ทะเบียนตัวละคร**: อามาเนะ = ฉัน · **มาโดกะ = ฉัน** (ไม่ใช่ "หนู") · **เรียว สึซากิ คง T1** (ข้อเสนอขยับ T2 ตกไป
  — ความขี้เมาสื่อผ่านถ้อยคำ ไม่ใช่ลดระดับสรรพนาม) · การ์ดใหม่ **`friend_seiya`** (T2 ฉัน/นาย ไม่ใช้ ครับ)
- **แก้ข้อมูลเพศในไฟล์ตัวละคร**: `friend_tachibana` (ยูริกะ) = **หญิง confidence สูง** (หลักฐาน `voicer_gender.json`)
  · `smoking_area_regulars` = **ชาย confidence สูง** (หลักฐาน EN ในบท) — เดิมขึ้น low ทำให้ผู้ตรวจเกือบแก้บทที่ถูกอยู่แล้ว
  · เติมเพศที่พิสูจน์แล้วอีก 12 ราย ลง `OVERRIDES` ของ `scripts/make_talk_speaker.py` (Girl in a School Uniform ·
  Lady in a Fancy Dress · Man in a Ski Mask · Debt Collector · Seiya/Madoka/Kasai/Honda/Koizuka/Iyama/Ushimata)
  · `Tsumugi` = ชื่อจริงของอามาเนะ (คนเดียวกัน) → ใส่ `aliases` ในการ์ดแล้ว
- **คำล็อกใหม่**: `extract` (ระบบคราฟต์) = **สารสกัด** (ไม่ใช่ "ยาสกัด" — กวาด 38 จุด) · `crowdfunding` = **ระดมทุน**
  (แบรนด์ `Quickstarter` คง EN) · `soapland` = **ร้านอาบอบนวด** · `Ikinari Steak` = **อิคินาริสเต๊ก** ·
  `batting center` = **สนามตีลูก** · `barker` = **คนเรียกแขก** · `image club` = **อิมเมจคลับ** ·
  `Scavenger Hunt` = **ภารกิจล่าของ** · `tengu` = **เทงงุ** · `fuck you` (เพื่อนโมโห) = **ไปตายซะ**
  · `bombing` (วงการโฮสต์) = **ทิ้งบอมบ์** · `White Tiger` = **ไวท์ไทเกอร์** · `Esmeralda Special`/`Geisha 1500`
  = **เอสเมอรัลดา สเปเชียล / เกอิชา 1500**
- **ชื่อที่กันสับสน**: `Taka` (ฉายาที่ฮัตตันตั้งให้) = **ทากะ** ≠ `Tak` ของไคโตะ = **ทาคุ** ·
  `Rinko` = **รินโกะ** (ไม่ใช่ ริงโกะ = แอปเปิล) · `Akko` = **อักโกะ** · **มี "Yosuke" สองคน**
  (โยสึเกะ ซาโอโตเมะ T1 กับ NPC สูบบุหรี่ `speaker_id 735` เพศ unknown) ห้ามยกทะเบียนข้ามคน
- **honorific ทับศัพท์ติดชื่อ ไม่มีขีดกลาง** (master ใช้แบบไม่มีขีด 2,144 จุด vs มีขีด 1) ยกเว้นชื่อสินค้า "บุน-จัง"
- **มุกชื่อยากุของยูริกะ ทาชิบานะ** แปลไทยครบชุด: ต้อยต้อย · หงส์อิ๊ด · ชูรินโปเตโต้ · ซูลุงโค · **พินอู๊ย**
  (คงอังกฤษตัวเดียวจะโดดกลางบทไทย · ยากามิสวนว่า "ผมว่ามันน่าจะ \"อู๊ย\" มากกว่านะ" รับมุก painful)
- **กฎใหม่ใน `PRONOUN_MATRIX.md`**: ตัวละครที่ **สวมบทบาทชั่วคราว** ใช้ทะเบียนของบทที่สวมได้ แล้วสลับกลับตอนเฉลย
  (นักเรียนปลอมใช้ "หนู" → "ฉัน") · แต่ยากามิแกล้งเป็นคู่รักไปสะกดรอย **ไม่เข้าข่าย** (แสดงต่อหน้าเป้าหมาย ไม่ใช่เปลี่ยนตัวตน)

### ⚠ บทเรียนของ lead รอบนี้ (อย่าให้เกิดซ้ำ)

**นับความถี่ในไฟล์ไม่ใช่หลักฐาน ถ้ามีคำตัดสินพร้อมเหตุผลอยู่แล้วใน glossary** — รอบนี้ lead เผลอกลับคำตัดสิน
`Kon-chan` จาก "คงจัง" (ล็อกไว้ก่อนพร้อมเหตุผล: "คนจัง" อ่านพ้องกับคำว่า "คน") เป็น "คนจัง" เพราะนับความถี่
อย่างเดียว · จับได้ตอนผู้ตรวจ TALK_071 ทักเรื่องสะกด `Kondo` (= **คนโดะ** ship 14 จุด ไม่ใช่ "คนโด")
→ คืนค่าเดิม + ใส่กฎกวาดย้อนหลังแล้ว · **ก่อนตั้ง/แก้คำล็อกทุกครั้ง ต้อง grep `glossary.md` ก่อนเสมอ**

### ⛏ ปลดบล็อก `ui_layer_text.bin` (ค้างจากรอบก่อน — ข้อ 4 ของ "งานถัดไป")
reARMP rebuild ไฟล์นี้ไม่ได้ แต่แกะโครงไบต์เจอว่าเป็นบล็อกสตริง NUL + **ตาราง pointer u32** และ
**ไม่มีฟิลด์ขนาดไฟล์ในเฮดเดอร์** → เขียน **`scripts/patch_bin_raw.py`** เติมสตริงไทยท้ายไฟล์แล้วย้าย pointer
(จำเป็น เพราะ donor 1 เซลล์ = 2 ไบต์ UTF-8 ทับที่เดิมไม่มีทางพอ: `MISSION` 7 B → ภารกิจ 10 B)
build ทดสอบอยู่ที่ `build/text/db.judge.en/en/ui_layer_text.bin` — ⏳ **รอผู้ใช้เปิดเกมยืนยันว่าไม่แครช**
ป้ายตัวเลขรูเล็ต (`0/00` `2to1` `1-18 19-36` `1st/2nd/3rd 12`) คง EN · หลักฐานเต็มใน `docs/research.md` §2

## 🔄 สปรินต์แปล — รอบที่สาม 21 ส.ค. 2026 (หยุดพักที่ **master 44,974 คู่ = 89.5%**)

> รอบสามเดินทีมนักแปล/ผู้ตรวจ sonnet คู่ขนาน ทำคิว TALK ไปได้ **TALK_007 – TALK_051 (45 batch = 11,250 string)**
> merge เข้า master ครบทุกตัวที่ตรวจแล้ว · **batch ว่างถัดไป = TALK_052** · เหลืออีก 21 batch (~5,300 string)
> ดูสถานะจริงเสมอ: `python scripts/sprint_status.py --next 5`

### วิธีเริ่มต่อ (ทำตามนี้ได้เลย)
1. `python scripts/sprint_status.py --next 6` → ดู batch ว่าง
2. spawn นักแปล sonnet 4-6 ตัว ตัวละ batch (คำสั่งเต็มดูรูปแบบใน `docs/reference/TRANSLATOR_BRIEF_judge.md` + กติกาสะสมด้านล่าง)
3. งานเข้า → `python scripts/normalize_terms.py --write` → `merge_qc.py --dry-run --only <batch>` → spawn ผู้ตรวจ → `merge_qc.py --only <batch>` → เติมคิวใหม่
4. หลังกวาด normalize ทุกครั้ง: `python scripts/remerge_stale.py --write` (กัน master ค้างคำเก่า)

### กติกาที่สะสมได้ในรอบสาม (ใส่ในคำสั่งนักแปลทุกตัว)
- **ชื่อ/ศัพท์ที่ ship แล้วชนะกฎทับศัพท์เสมอ** — ค้น `master_th.json` ก่อนตั้งรูปใหม่ · รอบนี้เจอชนกันรอบละ 1-3 ชื่อเพราะนักแปลใช้กฎแทนการค้น (ซุนาดะ · สึซากิ · ฟุมิเอะ · คาตากิริ · เคฮิน · สึกิโนะ · แบล็กแจ็ก · มาจอง)
- **`ref_tm` ขัดกับ master = ทิ้ง ref_tm** — ref_tm เองสะกดผิดหลายจุด (มาจองก์ · โออิโจ-คาบุ) และมีสรรพนามผิดตัวละคร
- **เพศที่พิสูจน์ไม่ได้ = ห้ามเดาจากชื่อ/บทบาท** — จุดที่พลาดบ่อยที่สุดคือเผลอใส่ "ครับ" ให้ตัวประกอบ (เก็บได้ 34 จุดใน TALK_028, 25 ใน TALK_027, 8 ใน TALK_035)
- **"ข้า/เจ้า" ห้ามใช้** ยกเว้น: บทพีเรียด/สวมบทบาทแฟนตาซี (ท่านแบรม · ไดจิ ริวเซนจิ · ผู้พิพากษาจอมถ้ำมอง) · ตระกูลอามอน · ไรอัน อาคอสตา — **มาสคอต/สำเนียงบ้านนอกไม่เข้าข่าย**
- **ตัวละครสุภาพที่โมโหให้แสดงอารมณ์ด้วยถ้อยคำ ไม่ใช่เปลี่ยนเป็น T3**
- **ยากามิเรียกเพื่อนหญิงว่า "คุณ" เป็นค่าเริ่มต้น** · "เธอ" เฉพาะเควสซานะหลังสารภาพใจ (ดูเลขแถวจุดตัดใน PRONOUN_MATRIX) · แต่ "เธอ" บุรุษที่ 3 ในบทรำพึงใช้ได้ปกติ
- **แท็ก `<color=...>` และ `<font_kind=...>` ต้องแปลข้อความข้างใน** (จุดบอด — เคยหลุดชื่อกาแฟ 16 จุด)
- **ช่องว่างระหว่างไทยกับอักษรละตินต้องมีเสมอ** (`โค้ด ESC` ไม่ใช่ `โค้ดESC`)
- **เวลาจริงในคดีต้องแปลง โมง/ทุ่ม ให้ถูก** (11 PM = ห้าทุ่ม) แต่**ปริศนาตัวเลขไม่ต้องแปลง**

### เครื่องมือที่อัปเกรดในรอบสาม
| ไฟล์ | เปลี่ยนอะไร |
|---|---|
| `scripts/make_talk_speaker.py` | เพิ่มฟิลด์ **`dupes`** (ข้อความ 376 บรรทัดถูกใช้ซ้ำหลาย subtable — เดิมเก็บผู้พูดได้คนเดียว ชี้ผิดเงียบ ๆ) + ตาราง **ALIASES/OVERRIDES เพศที่ทีมพิสูจน์แล้ว ~40 ตัวละคร** (ตอนนี้ male 10,021 · female 2,678 · unknown 5,711) |
| `scripts/check_latin_leftovers.py` | แก้บั๊ก allowlist เทียบแบบ substring กับคำสั้น (`id`/`ex`/`pc`) ที่กลืนคำตกค้างทั้งกอง · เพิ่มการกรอง `@handle`/`#hashtag` ของ Chatter · หลัง audit เหลือ 22 จาก 239 คำ |
| `scripts/check_pronoun_pairs.py` | แก้ false positive 3 ชุด: `รังแก` · `วิกผม/ทรงผม` · `ทากูจิ` — เทสต์ `test_pronoun_pairs.py` ตอนนี้ **34/34** |
| `scripts/remerge_stale.py` | เพิ่มการ์ด: ข้าม batch ที่ยังไม่มีไฟล์ review (เคยเผลอ merge งานที่ผู้ตรวจยังทำอยู่) |
| `scripts/fix_honorific_san.py` (ใหม่) | กวาด `Yagami-san` ที่แปลเป็น "คุณยากามิ" → "ยากามิซัง" (กฎนี้เคยซ่อนอยู่ในไฟล์ตัวละคร นักแปลพลาด 7/7 จุดใน batch เดียว · ของเก่าตกค้าง 29 จุดใน 11 batch) |
| `scripts/normalize_terms.py` | เพิ่มกฎคำล็อกอีก ~20 ข้อ · **แก้บั๊กกฎทับกันเอง 2 จุด** (`แทค`→ทาคุ ไปทับ "คอนแทคเลนส์" · `รวน หวัง` ไปทับ "หรวน หวัง" จนได้ "หหรวน") — กฎใหม่ที่เป็นคำสั้นต้องใส่ lookbehind เสมอ |

### บั๊กคุณภาพที่จับได้ในรอบสาม (ตัวอย่างที่ผู้เล่นจะเห็น)
- ชื่อช่องกระดาน Dice & Cube ในบทพูดเป็นอังกฤษ ทั้งที่การ์ดสอนเล่นแปลไทย ship ไปแล้ว (26 บรรทัดใน 2 batch)
- `11 PM` แปลเป็น "สี่ทุ่ม" ชนกับเวลาอีกจุดในคดีเดียวกัน → ไทม์ไลน์คดีพัง
- `"So long, then."` (ลาก่อน) แปลเป็น "งั้นก็แล้วแต่คุณเลย" — กลับความหมาย
- ทานากะ (ตัวปลอมที่จริงคือสตอล์กเกอร์) มี "ผม/ครับ" หลุด **ก่อน**ฉากเฉลย → สปอยล์ปม
- `"take a picture with yours truly"` → "ตัวเอง" (ผู้พูดชวนถ่ายกับตัวเอง ไม่ใช่ให้อีกฝ่ายถ่ายเดี่ยว)
- บรรทัด "ทำอะไรกับผมอยู่นั่น?" — "ผม" ตรงนี้แปลว่าเส้นผม แต่ยากามิใช้ "ผม" แทนตัวเอง ผู้เล่นอ่านผิดแน่

---

## 🔄 สปรินต์แปล — รอบที่สอง 21 ส.ค. 2026 (ประวัติ)

> session รอบสองเดินทีมนักแปล/ผู้ตรวจ sonnet คู่ขนานตลอด · **batch ปกติ (normal) 133 ตัวแปล+ตรวจ+merge ครบแล้ว**
> เหลือเฉพาะคิว **TALK (72 batch = `talk.bin` ล้วน)** · ดูสถานะจริงเสมอด้วย `python scripts/sprint_status.py --next 5`

### เครื่องมือใหม่ที่สร้างในรอบนี้ (สำคัญมากกับงานที่เหลือ)
| ไฟล์ | ทำอะไร |
|---|---|
| `scripts/make_talk_speaker.py` → `extracted/facts/talk_speaker.json` | **ตารางผู้พูดรายบรรทัดของ `talk.bin` 18,410 บรรทัด · 394 ผู้พูด** (ฟิลด์ `"2"` ของแถว = id ผู้พูด ชี้ไป `talk_talker.bin` · `"3"` = ข้อความ · ชื่อ subtable = คดี เช่น `judge_side_a11`) — ก่อนมีไฟล์นี้ นักแปลคิว TALK ต้องเดาผู้พูดเอง และเดาผิดราว 3% (7 จุด/250 ใน TALK_006) |
| `scripts/make_popup_gender.py` → `extracted/facts/popup_gender.json` | เพศ/อายุ/ย่าน/เวลา ของคำพูดลอยชาวเมือง 369 บรรทัด (ชาย 226 · หญิง 143) จากชื่อแถวใน `character_npc_popup_text.bin` |
| `scripts/make_multibin_index.py` → `docs/reference/multibin_keys.md` | 1,650 คีย์สั้นที่ใช้ซ้ำหลาย bin (`Medium` = ทรงผม + ระดับกราฟิก · `Up` = ทรงผม + ปุ่มทิศทาง) — คำแปลเดียวต้องใช้ได้ทุกบริบท · ถามทีละคีย์ `--key "Medium"` |
| `scripts/check_latin_leftovers.py` | จับอักษรละตินตกค้างในคำแปล (ชื่อร้านที่ลืมทับศัพท์ เช่น `ไปยัง Earth Angel`) · มี allowlist คำที่ตั้งใจคง EN |
| `scripts/remerge_stale.py` | หา batch ที่ไฟล์ done ไม่ตรง master แล้ว merge ใหม่ให้ (`--write`) — **ต้องรันทุกครั้งหลัง `normalize_terms.py --write` ทั้งโปรเจกต์** ไม่งั้นคำเก่าค้างใน master |

### บทเรียนรอบนี้ (อย่าให้เกิดซ้ำ)
- **หลังกวาดคำทั้งโปรเจกต์ต้อง `remerge_stale.py --write` เสมอ** — รอบนี้เคยมีคำเก่าค้างใน master 12 batch
- **ห้ามเขียน regex ลบช่องว่างแบบเหมารวมกับคำแปล** — lead เคยทำ `
` หาย 22 คีย์ (กู้จาก master ได้เพราะยังไม่ merge)
- **สัญลักษณ์ `♪ ❤ ♥ ★ ☆ • ※` ห้ามมีในคำแปล** (ยืนยันกับ `slotmap.json`: ไม่มีเซลล์ → tofu) · ยกเว้นคีย์ที่ตั้งใจคงต้นฉบับทั้งบรรทัด (บทจีน legacy) · เคยมีผู้ตรวจ "คืน ♪ กลับ" เพราะเห็น master ship ไว้ 17 จุด — นั่นคือบั๊กเก่า ไม่ใช่ precedent
- **เนื้อหาค้างจากภาคอื่นในตารางเดียวกัน**: `caba_sora`/`caba_hikaru` (ซับจีน Y6) · `sub_a13`/`sub_a14` ตาราง `paul` (เควสต์ปาเป้า Kiwami 2 อ้าง 桐生) — ไม่มีใน `speech_speaker_map.json` = เกมไม่เรียกใช้ → บทจีนคงต้นฉบับ บท EN แปลตรงตัว
- **ปุ่มบนจอกับบทพูดที่อ้างถึงปุ่มต้องใช้คำเดียวกัน** (เคส Hit/Stand/Fold/Bet ใน TALK_002)
- ตัวตรวจสรรพนามเคย false positive 2 คลาสใหม่: `ทากูจิ` (มี "กู") · `ผมดำ/ผมยาว` (คำบรรยายเส้นผม) — แก้ regex + `test_pronoun_pairs.py` 31/31 ผ่านแล้ว

### สถานะล่าสุด (หยุดพัก 21 ส.ค. 2026 รอบสอง)
- **merge เข้า `translations/master_th.json` แล้ว 33,974 คู่ = 67.6%** (เริ่ม session นี้ที่ 24,774 = 49.3% · +9,200 คู่)
- ส่งงานแล้ว 139 batch · **ตรวจครบ 139 · merge ครบ ไม่มีคิวค้าง ไม่มี agent ค้าง**
- **batch ปกติ (normal) 133 ตัวจบครบทั้งหมดแล้ว** — ที่เหลือคือคิว **TALK 66 batch** (`talk.bin` ล้วน ≈ 16,500 string)
- batch ว่างถัดไป: **TALK_007** (ดูจริงด้วย `python scripts/sprint_status.py --next 5`)

### เริ่มงาน session หน้าอย่างไร
1. `python scripts/sprint_status.py --next 6` → ได้ batch ว่างถัดไป
2. spawn นักแปล sonnet ทีละ batch (บรีฟ: `docs/reference/TRANSLATOR_BRIEF_judge.md` — **มีหัวข้อ `talk_speaker.json` แล้ว**)
3. งานจบ → `normalize_terms.py --write --only <ไฟล์>` → `merge_qc.py --dry-run --only NNN` (ต้องตก 0) → spawn ผู้ตรวจ → `merge_qc.py --only NNN`
4. ทุกครั้งที่ล็อกคำใหม่: เพิ่มกฎใน `normalize_terms.py` → เขียน glossary → `normalize_terms.py --write` ทั้งโปรเจกต์ → **`remerge_stale.py --write`**

### คำตัดสินคำล็อกรอบนี้ (อยู่ครบใน `translations/glossary.md` บล็อก "คำตัดสิน lead รอบ sprint 21 ส.ค. 2026")
Rei = เรย์ · Kyushu No. 1 Star = คิวชูนัมเบอร์วันสตาร์ (แก้ย้อนหลัง 5 batch) · Kajihira Group = กลุ่มคาจิฮิระ (แก้ย้อนหลัง 11 batch) · Chatter/Stijl→สติล/Quickstarter · Play Pass = เพลย์พาส · ปุ่มคาสิโนทั้งชุด (Hit=ตี · Check=เช็ก ฯลฯ) · ตระกูล Quickstep คง EN · แคตตาล็อกโดรน (แบรนด์ EN + หลัง colon ไทย + ลำดับคำไทย) · §13.1 ตาราง yaku 65 คำ · §14 ฟิลเตอร์กล้อง 22 ชื่อ

### สถานะเดิมตอนเริ่ม session นี้ (24,774 คู่ = 49.3%)

> **หยุด agent ทั้งหมดแล้วตามคำสั่งผู้ใช้ (context เต็ม) — session ใหม่เริ่มจากหัวข้อนี้ได้เลย**

### สถานะตัวเลข
- 205 batch (normal 133 · talk 72) · คิวรวม 50,267 string
- **merge เข้า `translations/master_th.json` แล้ว 24,774 คู่ (49.3%)**
- แปลเสร็จ 104 batch · ตรวจแล้ว 101 batch
- **เนื้อเรื่องหลักบทที่ 1-13 แปลครบทั้งหมดแล้ว** · ที่เหลือเป็นเนื้อหาเสริม
  (ไอเทม · เมนูอาหาร · UI/manual · แฟ้มคดีไซด์เคส · กติกามินิเกม · แชท Friends/Girlfriend · ภารกิจ)

### งานค้างที่ต้องทำต่อทันที
1. **spawn ผู้ตรวจให้ batch 102 · 103 · 104** — แปลเสร็จแล้ว ผ่าน `merge_qc --dry-run` ตก 0 ทั้งสามตัว
   แต่ยังไม่มีไฟล์ `translations/review/batch_1{02,03,04}.review.md`
2. **batch 099 กับ 106 ถูกยกเลิกกลางคัน** — ยังไม่มีไฟล์ `done/` ต้อง **เริ่มแปลใหม่ทั้ง batch**
3. batch ว่างถัดไปหลังจากนั้น: 107 · 108 · 109 · 110 · 111 …
4. ดูสถานะจริงเสมอด้วย `python scripts/sprint_status.py --next 5`

### คำสั่งผู้ใช้ที่ยังมีผล
- เดินสปรินต์แบบ **6 คู่พร้อมกัน = นักแปล 6 + ผู้ตรวจ 6 (12 agent)** — ผู้ใช้ทักมาแล้วครั้งหนึ่งว่า
  ทีมเล็กลง ให้เติมคิวกลับทุกครั้งที่ agent ตัวไหนจบ
- ใช้ subagent model **sonnet** เท่านั้น
- **lead ห้ามแปลเอง** — หน้าที่คือ normalize → QC → spawn ผู้ตรวจ → merge → ตัดสินคำล็อก

### ลูปทำงานต่อ batch (lead ทำเอง)
1. นักแปล (sonnet) ส่ง `translations/done/batch_NNN.done.json`
2. `python scripts/normalize_terms.py --write --only translations/done/batch_NNN.done.json`
3. `python scripts/merge_qc.py --dry-run --only NNN` → ต้องได้ **ตก 0**
4. spawn ผู้ตรวจ (sonnet) พร้อมโจทย์: จุดที่นักแปลบอกเองว่าเดา + คำล็อกใหม่ที่เพิ่งเกิด + งานตรวจมาตรฐาน
5. ผู้ตรวจเสร็จ → `python scripts/merge_qc.py --only NNN` (นี่คือทางเดียวที่เขียน master_th ได้)
6. **ทุกครั้งที่ผู้ตรวจรายงานคำขัดกัน**: เพิ่มกฎใน `scripts/normalize_terms.py` → เขียน `translations/glossary.md`
   → รัน `normalize_terms.py --write` ทั้งโปรเจกต์ → หา batch ที่ merge ไปแล้วซึ่งมีคำเก่า → normalize + `merge_qc --only` ใหม่
   → ยืนยันว่า master เหลือคำเก่า 0

### เครื่องมือหาผู้พูด (สร้างในสปรินต์นี้ — ใช้ก่อนเดาเสมอ)
| ไฟล์ | เนื้อหา | สร้างใหม่ด้วย |
|---|---|---|
| `extracted/facts/speaker_by_subtable.json` | 1,410 คู่ `<ตารางแม่>#<speaker-slot id>` → ชื่อผู้พูด (ทดสอบตรง 10/10) | `python scripts/make_speaker_subtable.py --write` |
| `extracted/facts/chat_sender.json` | 1,521 บรรทัดแชท → `role` (yagami/contact/choice/chosen_echo/narration) + `contact` (18 คน) แม่นระดับบรรทัด | `python scripts/make_chat_sender.py --write` |
| `extracted/facts/voicer_gender.json` | เพศ voicer จากไฟล์เกม (ผิดได้เป็นราย ๆ เช่น `sumire`) | `python scripts/make_gender_table.py --write` |

### เอกสารที่ต้องอ่านก่อนสั่งงานทีม
- `translations/glossary.md` — **13 หมวด** (§9 ศาล · §10 UI · §11 ชื่อร้าน/มินิเกม · §12 นิติเวช · §13 มาจอง/ระบบ + คำล็อกท้ายไฟล์อีกยาว)
- `translations/PRONOUN_MATRIX.md` — **คำตัดสิน lead ทั้งหมดอยู่ท้ายไฟล์**
- `docs/reference/speaker_map_judge.md` · `docs/reference/TRANSLATOR_BRIEF_judge.md` · `REVIEWER_BRIEF_judge.md`

### บทเรียนสำคัญของสปรินต์ (อย่าให้เกิดซ้ำ)
- **บั๊กที่รอดถึงชั้นตรวจบ่อยที่สุดคือ "ผู้พูดผิดตัว"** ไม่ใช่ภาษาไทยไม่สวย — เครื่องมือสองตัวข้างบนแก้ปัญหานี้ได้เกือบหมด
- **`ref_tm` มีบั๊ก 4 คลาส**: คำล็อกเก่า · ช่องว่างแทรกกลางคำ/ชื่อเฉพาะ · เพศ/สรรพนามผิดตัว · สำนวนแปลผิดความหมาย
  → ต้องเทียบ glossary ก่อนใช้เสมอ แต่ **ถ้า ref_tm ถูกอยู่แล้วห้ามเขียนทับ**
- **ห้ามดัดคำแปลเพื่อหนี QC** — ให้รายงาน lead แล้ว lead แก้เครื่องมือ (แก้ false positive ไปแล้ว 6 คลาส:
  ยากูซ่า/ตระกูล · ขอบคุณ/คุณภาพ · แก๊ง/แกร่ง · คุณยาย/คุณลุง · กู้- · สุดกู่)
- **ตัวตรวจสรรพนาม** `scripts/check_pronoun_pairs.py` + เทสต์ `test_pronoun_pairs.py` (31/31) — แก้ regex เมื่อไรต้องรันเทสต์
- คำที่ ship แล้วใน `master_th.json` **ชนะ** คำที่เพิ่งเสนอเสมอ (เคสจริง: Batting Center · Dragon's Palace · mahjong)

## บริบท: repo นี้มาจากไหน

สร้างเมื่อ 14 ส.ค. 2026 ระหว่าง session ของโปรเจกต์ K3 (`D:\Projects\yakuza-kiwami-3`) หลังผู้ใช้สั่ง research การทำม็อดแปลไทย Judgment/Lost Judgment ทีมแปลชุดนี้ทำม็อดไทยสาย RGG มาแล้ว: K2R → Pirate → Y7 → Y8 → Gaiden (ship v1.0 แล้ว) → K3 (กำลังทำ ~66%) — pipeline ทั้งหมดอยู่ในโปรเจกต์เหล่านั้นและ **พร้อม port มาใช้** อ่าน `CLAUDE.md` ของ repo นี้ก่อน (กติกาเหล็ก + ตาราง path ครบ)

## ข้อเท็จจริงที่ verify แล้ว (จาก research 14 ส.ค. 2026 — ไม่ต้องค้นซ้ำ)

1. **SRMM/RMM (Parless) รองรับ Judgment อย่างเป็นทางการ** (Steam เท่านั้น) — อยู่ในรายชื่อ Supported Games ของ RyuModManager wiki (repo archived พ.ย. 2023 แต่ SRMM ที่เราใช้คือ fork ที่ยังไปต่อ) → loose file ผ่าน `mods/` ใช้ได้ ไม่ต้องทดสอบแบบเดา ๆ เหมือน K3
2. **มีม็อดไทย Google MT อยู่แล้ว**: "Judgment MOD2SUB TH EN google V1" — https://www.nexusmods.com/judgment/mods/228 — ติดตั้งแบบวางทับ `runtime/media` = พิสูจน์ว่าเส้นทาง ARMP+font ไทยแสดงผลได้จริงในเกมนี้ · **ห้ามใช้เป็น TM** (คุณภาพ MT) แต่โหลดมาแกะรายชื่อไฟล์ที่เขาแตะได้ (ประหยัดเวลา research มาก) · หมายเหตุ: Nexus บล็อก WebFetch (403) — ต้องเปิดเบราว์เซอร์/โหลดเอง
3. **เอนจิ้น**: ~~ต้นแบบใกล้สุด K2R~~ **แก้ 15 ส.ค.: ฟอนต์เป็น format `FONT!` ยุค Y6 → ต้นแบบจริงคือ Y6** (`D:\Projects\yakuza-6-thai`) · ฝั่งข้อความยังเป็นสาย ARMP v2/K3 ตามเดิม
4. **codename ภายในคาดว่า `judge`** — ยังไม่ยืนยันจากไฟล์จริง (เกมยังไม่ติดตั้ง) · ที่ยืนยันแล้วคือแพเทิร์นตระกูล: `db.<code>.<lang>.par` (LJ = `db.coyote.en.par`, Y7 = yazawa, Gaiden = aston, K3 = bis)
5. ภาษาในเกม: EN/JA (ม็อด Retrial เพิ่ม zh/ko ได้ = ช่อง lang ยืดหยุ่น) — carrier น่าจะเป็น EN ตามธรรมเนียมทุกภาค

## สถานะ: รอบ 3 deploy แล้ว 20 ส.ค. 2026 — เจาะฟอนต์หน้าไตเติลโดยตรง (รอผู้ใช้แคปภาพ)

### ค้นพบใหญ่ 20 ส.ค. 2026 — ทำไมหน้าไตเติลรอบ 1 ขึ้นว่างทั้งไทยแท้และ donor

หน้าไตเติลไม่ได้วาดด้วย `tbgm_0p_ja` แต่วาดด้วย `meta_ot_cond_book.dds` ซึ่ง **ไม่ใช่ฟอร์แมต
`FONT!`** — ไม่มีไฟล์ `.bin` metrics คู่เลย เป็น bitmap grid ล้วน decode แล้วได้ผังชัดเจน:
atlas 512x1536 BC4U, 16 คอลัมน์, cell 32x64, 384 เซลล์ = U+0000-007F ต่อด้วย U+00A0-019F
(ข้าม C1 block) — ตาราง width/kerning อยู่ใน exe ไม่ใช่ในไฟล์ data (precedent เดียวกับ
`hd2_hankaku.dds` ยุค Yakuza 0/Kiwami ที่ชุมชนบันทึกไว้) atlas นี้มีแค่ Latin/Latin-1/
Latin-Ext-A จึงไม่มีทั้งไทยและ Cyrillic = อธิบายผลรอบ 1 ครบทั้งสองแนว

### เครื่องมือใหม่
- `scripts/title_slotmap.py` — ผัง cell ของฟอนต์ไตเติล + donor pool (มีหมึก 61 ช่องใน
  Latin-1, ว่าง 152 ช่องใน Latin Ext-A) + `encode(text, group)`
- `scripts/inject_thai_title.py` — วาด Sarabun ลงเซลล์ (ล้างเซลล์ก่อน, patch เฉพาะ BC4
  block ที่เปลี่ยน, ตรวจกลับว่าเซลล์ที่ไม่ได้แก้ bit-identical) -> `build/font/meta_ot_cond_book.dds`
- `scripts/make_spoil_title2.py` — title_root.bin ทดสอบรอบ 3 -> `build/text/SPOIL_MAP_v3.md`
- `scripts/deploy_spoil.py` — เลิก hardcode รายชื่อไฟล์ฟอนต์ ตอนนี้ deploy ทุกไฟล์ใน
  `build/font` ที่มีคู่จริงในเกม และ `--restore` คืนจาก `.orig` ทุกไฟล์ที่เจอ

### ✅ ผลรอบ 3 (ภาพจากผู้ใช้ 20 ส.ค. 2026) — ไทยขึ้นหน้าไตเติลสำเร็จ

- ไทยขึ้นครบทั้ง **กลุ่ม A** (เซลล์มีหมึก U+00C0+) และ **กลุ่ม B** (เซลล์ว่าง U+0102+)
  → เซลล์ว่างเติมได้จริง ไม่มีปม "ช่องว่าง = tofu ถาวร" แบบ Y6 → แอ่ง donor ของฟอนต์ไตเติล
  = 61 + 152 = **213 ช่อง**
- ตัวฐานเรียงชิดปกติ = **ฟอนต์ไตเติล proportional จริง** (ต่างจาก tbgm_0p_ja ที่ fixed-pitch)
- ปัญหาที่เหลือ: **มาร์กกินที่แนวนอน** ("เริ่ ม", "ตั้ ง") เพราะ donor ที่ใช้ (Ñ Ò Ó Ô) กว้างเต็มตัว
- สมมติฐานที่ตามมา: ความกว้างมาจาก **codepoint ของ donor ผ่านตาราง width ใน exe** ไม่ใช่จาก
  รูปที่วาด → เลือก donor = เลือก advance ได้โดยไม่ต้องแตะ exe

### รอบ 4 deploy แล้ว 20 ส.ค. 2026 — รอผู้ใช้แคปหน้าไตเติล (วัดตาราง width)

สร้างด้วย `inject_thai_title.py --probe` + `make_spoil_title4.py` (นิยามแถวทั้งหมดใน
`scripts/title_probe.py`, ตารางอ่านผลใน `build/text/SPOIL_MAP_v4.md`)

| เมนูเดิม | เนื้อหา | อ่านผล |
|---|---|---|
| NEW GAME | ก x5 บน donor แคบ (¡ ¹ Í Ì Ï) | ระยะแคบสุดที่ทำได้ |
| CONTINUE | ก x5 บน donor กว้าง (Ò Ó Ô Õ Ö) | เทียบกับแถวบน = พิสูจน์ว่า advance มาจาก cp |
| VS MINIGAMES | ก x5 บนเซลล์ว่าง Ext-A | เซลล์ว่างได้ advance เท่าไร |
| SETTINGS | ก+่ สลับ 4 คู่ (NBSP / soft hyphen / ¨ / ´) | คู่ไหนวรรณยุกต์ลอยทับ ก = เจอ donor advance 0 |
| REPLAY | เริ่ม แบบ pre-composed (ริ่ = กลิฟเดียว) | เป้าหมายที่อยากได้ |
| EXIT GAME | เริ่ม แบบ per-char มาร์กบน donor แคบ | เทียบตรงกับ REPLAY |

ทางแยกหลังรอบ 4: ถ้าเจอ donor advance ≈ 0 → per-char + มาร์กลอย (slot น้อย ยืดหยุ่นสูง) ·
ถ้าไม่เจอ → pre-composed cluster เหมือน Y6 แต่จำกัดด้วย 213 ช่องของฟอนต์ไตเติล (ไม่พอสำหรับ
2,990 cluster เต็มระบบ → ต้องแยกนโยบายระหว่างฟอนต์ไตเติลกับฟอนต์ข้อความหลัก)

### ✅ ผลรอบ 4 (ภาพจากผู้ใช้ 20 ส.ค. 2026) — ยืนยันกลไก advance

- `ก` ตัวเดียวกันบน donor แคบ (¡ ¹ Í Ì Ï) เรียง**ชิด**กว่าบน donor กว้าง (Ò Ó Ô Õ Ö) ชัดเจน
  → **advance มาจาก codepoint ของ donor ผ่านตาราง width ใน exe ไม่ใช่จากรูปที่เราวาด**
  = เลือก donor คือเลือกระยะ ทำได้ทั้งหมดในชั้น data ไม่ต้องแตะ exe/DLL
- เซลล์ว่าง Latin Ext-A ได้ advance ปกติ (ไม่ใช่ 0)
- pre-composed cluster ("ริ่" กลิฟเดียว) ให้ผลสวยตามคาด · per-char + มาร์กบน donor แคบ
  อ่านออกเช่นกันแต่ยังมีช่องไฟแทรก
- แถวผู้สมัคร advance-0 ใส่ 4 ตัวรวมแถวเดียว **อ่านผลกำกวม** → แยกทดสอบใหม่ในรอบ 5

### รอบ 5 deploy แล้ว 20 ส.ค. 2026 — หา donor ที่ advance = 0 (รอผู้ใช้แคป)

ผัง `scripts/title_probe5.py` · หนึ่งผู้สมัครต่อหนึ่งแถว · ทุกแถวเป็น `ก`+`่` สลับกัน 3 คู่
(ฐานเป็น È U+00C7 เหมือนกันหมด) — NEW GAME = NBSP · CONTINUE = soft hyphen ·
VS MINIGAMES = ¨ · SETTINGS = ´ · REPLAY = ¡ · EXIT GAME = `ก` 3 ตัวล้วน (ควบคุม)

อ่านผล: วรรณยุกต์ลอยทับ ก = advance 0 (เป้าหมาย) · แยกออกมาเป็นตัวถัดไป = advance > 0 ·
ไม่เห็นวรรณยุกต์เลย = engine ข้าม codepoint นั้น

คำสั่ง build: `python scripts/inject_thai_title.py --map title_probe5` +
`python scripts/make_spoil_title4.py --map title_probe5` + `python scripts/deploy_spoil.py`

### ✅ ผลรอบ 5-6 — ไม่มี codepoint ไหน advance = 0 (ปิดเส้นทาง per-char)

ทดสอบผู้สมัครแล้ว 10 ตัว แยกหนึ่งตัวต่อหนึ่งแถว รูปแบบ `ก`+`่` สลับ 3 คู่:
- รอบ 5: NBSP U+00A0 · soft hyphen U+00AD · ¨ U+00A8 · ´ U+00B4 · ¡ U+00A1
- รอบ 6: U+0001 · U+0005 · U+000E · U+001F · U+007F (ช่วง control ที่เซลล์ว่าง)

ทุกตัว **วาดกลิฟออกมาจริง แต่กินที่แนวนอนหมด** — วรรณยุกต์แยกเป็นตัวถัดไป ไม่มีตัวไหนลอยทับ
กลุ่ม control ได้ระยะเท่ากันทุกตัว = ค่า default ของตาราง width ใน exe
→ **มาร์กลอยแบบ per-char ใช้ไม่ได้บนฟอนต์ไตเติล ต้องใช้ pre-composed cluster**
(cluster ทดสอบแล้วในรอบ 4 แถว REPLAY = "เริ่ม" กลิฟเดียว ผลออกมาสวย)

### รอบ 7 deploy แล้ว 20 ส.ค. 2026 — ทดสอบขยาย atlas (รอผู้ใช้แคป)

โจทย์ที่เหลือของเส้นทาง cluster คือจำนวนช่อง: ตารางเดิมจบที่ U+019F ใช้ได้จริง ~213 ช่อง
หักพยัญชนะ/สระเดี่ยว 68 เหลือ ~145 ช่องสำหรับ cluster (Y6 ทั้งเกมมี 403 cluster ไม่ซ้ำ)

รอบนี้ขยายภาพ atlas 1536 -> 2240 px (35 แถว = cp ถึง U+024F) แล้วแก้ `dwHeight` +
`dwPitchOrLinearSize` ใน DDS header ให้ตรง (สคริปต์ `inject_thai_title.py` ทำอัตโนมัติเมื่อ
เซลล์ที่ขอเกินขอบภาพ) วาง `ก` ที่ U+01A0 / U+01B0 / U+01C0 / U+0200 / U+024F แถวละ cp

อ่านผล: แถวใหม่ขึ้น `ก` = ขยาย atlas ได้ แอ่ง donor โตได้ตามต้องการ · ขึ้นว่าง = ตารางถูก
จำกัดใน exe ต้องอยู่ในโควตาเดิม · เมนูอังกฤษเพี้ยนทั้งจอ = engine อ่านความสูงเดิมค้าง
(LICENSE INFORMATION / ADDITIONAL CREDITS = ตัวชี้วัด) → `deploy_spoil.py --restore` ทันที

### ⛔ ผลรอบ 7 — ขยาย atlas ไม่ได้ (เพดานตายตัว 384 เซลล์)

ขยายภาพเป็น 2240 px + แก้ `dwHeight`/`dwPitchOrLinearSize` ให้ตรงแล้ว (payload 573,440 B
ตรงสูตร BC4) แต่ในเกม **ทั้งเมนูเละ** — ตัวอักษรอังกฤษสลับตำแหน่งกันมั่ว ("licen e nfo ma ion")
= engine ยึดขนาดตารางเดิมไว้ ไม่ได้อ่านความสูงจาก header · คืนฟอนต์ต้นฉบับแล้วทันที

**เพดานถาวร: 384 เซลล์** — นับที่ใช้ได้จริง: non-ASCII (U+00A0-019F) 256 ช่อง (มีหมึกเดิม 69
ทับได้ + ว่าง 187) + เซลล์ control ว่างอีก ~26 → ~260 ช่อง หักที่ควรสงวนให้ EN (© ® ¥ « » ¿)

### รอบ 8 deploy แล้ว 20 ส.ค. 2026 — เมนูไทยของจริงด้วย pre-composed cluster (รอผู้ใช้แคป)

เครื่องมือใหม่ (นี่คือรูปแบบที่จะใช้จริง ไม่ใช่ probe แล้ว):
- `scripts/title_encode.py` — `segment()` แบ่งข้อความเป็นเซลล์แบบ Y6 (ฐาน + สระบน/ล่าง ≤1 +
  วรรณยุกต์ ≤1) และ `build_map()` จัด donor อัตโนมัติโดย **จับคู่ตามความกว้าง** (เรียงกลิฟกับ
  donor ตามความกว้าง ink แล้วจับคู่ตามลำดับ) คืนค่าที่สามเป็นความกว้างเป้าหมายด้วย
- `inject_thai_title.py` รับความกว้างเป้าหมายแล้ว **บีบกลิฟตามแนวนอน** ให้พอดี advance ที่
  donor นั้นจะได้จาก exe (ฟอนต์เป็น Condensed อยู่แล้ว บีบเล็กน้อยจึงเข้ากับดีไซน์ · บีบไม่เกิน 40%)
- `scripts/title_menu_map.py` — ข้อความเมนูไทย 8 สตริง → ใช้ **31 เซลล์ จาก pool 49 ช่อง**

ข้อความที่ควรเห็น: เริ่มเกมใหม่ / เล่นต่อ / มินิเกมสองผู้เล่น / ตั้งค่า / ดูฉากย้อนหลัง /
ออกจากเกม + คำอธิบายใต้จอ 2 แถว · LICENSE INFORMATION กับ ADDITIONAL CREDITS คงอังกฤษ
(กติกาข้อ 10 + เป็นตัวควบคุมว่าฟอนต์อังกฤษไม่พังจากการทับเซลล์ตัวมีเครื่องหมาย)

ชุด `tbgm_0p_ja` ของรอบ 2 (จอ press any button + toast เซฟ/โหลด) ยัง deploy อยู่ด้วย →
ให้ผู้ใช้เดินดูจอในเกมด้วย จะได้รู้ว่าจอไหนใช้ฟอนต์ไหน = ตัวเลขสำหรับคำนวณโควตา cluster จริง

### ✅✅ รอบ 8-9 — เมนูหน้าไตเติลภาษาไทยใช้งานได้จริง (ยืนยันบนจอ 20 ส.ค. 2026)

รอบ 8 ขึ้นครบทุกแถวแต่ **ขนาดตัวอักษรไม่สม่ำเสมอ** (ผู้ใช้จับได้: `ใ` เล็กเกิน, `มินิเกมสองผู้เล่น`
ขนาดเด้งทั้งคำ) สาเหตุ: renderer สเกลกลิฟทีละตัวให้ ink สูงเท่ากันหมด ตัวที่มีหางบน (ใ ไ โ ป ฝ ฟ)
จึงถูกย่อ และบีบแนวนอนคนละอัตราต่อเซลล์

รอบ 9 แก้แล้ว ผ่านการยืนยันบนจอ:
- ใช้ **ppem เดียวกับทุกตัวอักษร** (ตั้งจาก `ก` = 22px) แล้ววางตาม **เส้นฐานจริง** —
  ปล่อยสัดส่วนธรรมชาติของฟอนต์ทำงาน (ห้ามกลับไป normalize ความสูงรายตัวเด็ดขาด)
- มาร์กวางเป็นชั้นเหนือ ink ของฐานที่วัดจริง (สระบนชั้น 1 → วรรณยุกต์ชั้น 2)
- บีบแนวนอนจำกัดไม่เกิน 15% (`MIN_SQUEEZE = 0.85`)
- จัด donor แบบ **กว้างสุดเลือกก่อน + จับ donor ที่ความกว้างใกล้สุด** (ไม่ใช่เรียงจับคู่ตามลำดับ)
- โค้ด render/ppem อยู่ที่ `title_encode.py` (`render_at`, `ppem`, `natural_width`) ใช้ร่วมกับ
  `inject_thai_title.py` ไฟล์เดียว ไม่มีสำเนาซ้ำ

**สถานะ: เส้นทางฟอนต์หน้าไตเติล/เมนู = จบแล้ว พร้อมใช้ผลิตจริง**

### ✅ รอบ 10 — จอโลโก้ (Press any button) ก็ใช้ฟอนต์ไตเติล (ยืนยันบนจอ 20 ส.ค. 2026)

รอบ 2 เขียนแถวนี้ (`ui_text.bin` แถว 1889, ยืนยันด้วย diff กับต้นฉบับ) เป็น **codepoint ไทยจริง**
ซึ่งใช้ได้เฉพาะกับ `tbgm_0p_ja` ที่เพิ่ม record ไทย → จอขึ้นว่าง · รอบ 10 เขียนใหม่ด้วย donor ของ
`meta_ot_cond_book` แล้วขึ้น `กดปุ่มใดก็ได้` อ่านออกชัด

→ **จอโลโก้ + เมนูไตเติล = `meta_ot_cond_book` ทั้งคู่** · สคริปต์: `scripts/make_press_any.py`
(ข้อความเก็บที่ `title_menu_map.EXTRA` เพื่อให้ build_map จองเซลล์ให้ด้วย — ตอนนี้ใช้ 35/49 ช่อง)

### ✅ รอบ 11 — UI ในเกม (จอเซฟ/โหลด) ก็ใช้ฟอนต์ไตเติล

ทดสอบคู่เทียบในจอเดียวกัน (`msg.bin`): กล่องหลังเซฟเขียนด้วย donor ของ `meta_ot_cond_book`,
กล่องหลังโหลดเขียนด้วย donor ของ `tbgm_0p_ja` (Cyrillic ตาม y6_slotmap)
- **หลังเซฟ: `บันทึกเรียบร้อยแล้ว` ขึ้นชัดเจน**
- **หลังโหลด: ว่างเปล่า**
→ จอเซฟ/โหลด (และน่าจะทั้งชั้น UI) วาดด้วย `meta_ot_cond_book` · donor ของ tbgm ไม่ขึ้นที่นั่น
→ รอบก่อนที่กล่องเซฟว่าง ไม่ใช่เพราะเกมไม่รับ record cp ไทยที่เพิ่มใน tbgm แต่เพราะ **จอนั้นไม่ได้ใช้ tbgm**

### รอบ 12 deploy แล้ว — บทสนทนา/ซับใช้ฟอนต์ไหน (รอผู้ใช้เล่นแล้วแคป)

`scripts/make_talk_probe.py` แทนบทพูดใน `talk.bin` **ทุกบรรทัด (19,055 บรรทัด)** ด้วยข้อความ
ทดสอบเดียวกัน `เอ บี` โดย `เอ` encode ด้วย donor ฟอนต์ไตเติล และ `บี` encode ด้วย donor ของ
`tbgm_0p_ja` — เดินไปคุยกับใครก็เห็น ไม่ต้องหาบรรทัดที่ trigger ได้

อ่านผล: เห็น `เอ` = ซับอยู่บนตาราง 384 เซลล์ (โจทย์โควตาใหญ่) · เห็น `บี` = ซับอยู่บน tbgm
(slot ว่าง 2,157 ช่อง สบาย) · เห็นทั้งคู่ = มี fallback · ไม่เห็นทั้งคู่ = ฟอนต์ตัวที่สาม

⚠ บิลด์นี้ทำให้บทสนทนาทั้งเกมเป็นข้อความทดสอบ — ถอดด้วย `deploy_spoil.py --restore`

### ✅✅ รอบ 12 — **ทั้งเกมวาดด้วยฟอนต์เดียว: `meta_ot_cond_book`** (ยืนยันบนจอ 20 ส.ค. 2026)

ซับบทสนทนา (คุยกับ Hoshino) แสดง `เอ` = donor ของฟอนต์ไตเติล ส่วน `บี` = donor ของ `tbgm_0p_ja`
ออกมาเป็น **กล่อง tofu** → ซับใช้ atlas เดียวกับไตเติล/UI ทุกจอ

**ข้อสรุปสถาปัตยกรรมของโปรเจกต์นี้ (สำคัญที่สุดที่ได้จาก session นี้):**
- carrier EN ของเกมวาดข้อความทุกชั้น (ไตเติล / จอโลโก้ / UI เซฟโหลด / ซับบทสนทนา) ด้วย
  bitmap grid `meta_ot_cond_book.dds` เพียงตัวเดียว — **เพดาน 384 เซลล์ ขยายไม่ได้**
- `tbgm_0p_ja` (7,093 กลิฟ, slot ว่าง 2,157) **ไม่ถูกใช้เลยในโหมด EN** → งานที่ทำไว้กับไฟล์นั้น
  (donor Cyrillic + record cp ไทยที่เพิ่ม) ใช้ไม่ได้กับเส้นทางนี้ เก็บไว้เผื่อโหมด JA เท่านั้น
- cp ที่ไม่มีในตาราง = วาดเป็นกล่อง tofu (ไม่ใช่ว่างเปล่า) — ใช้เป็นสัญญาณ debug ได้

### โควตาเซลล์ vs ความต้องการจริง (คำนวณจากคลังแปล Y6 ทั้งเกม 37,209 ประโยค)

ช่องที่ใช้ได้โดยไม่แตะ ASCII (ต้องเก็บไว้ให้ LICENSE/CREDITS): non-ASCII U+00A0-019F 256 ช่อง
+ เซลล์ control ที่ว่าง ~25 ช่อง = **~281 ช่อง**

| วิธีแบ่งเซลล์ | เซลล์ไม่ซ้ำที่ต้องใช้ | ครอบคลุมด้วย 282 ช่อง |
|---|---|---|
| ฐาน + มาร์กทั้งหมดรวมเป็นกลิฟเดียว | 634 | 99.22% |
| **ฐาน + มาร์ก 1 ตัว** (มาร์กตัวที่ 2 แยกเซลล์) | **391** | **99.76%** |

→ แผนที่เลือก: **ฐาน+มาร์ก 1 ตัว** + สำรอง 15 ช่องไว้เป็น "มาร์กเดี่ยว" สำหรับ cluster หายาก
(ยอมให้มาร์กเลื่อนขวาเล็กน้อยแบบที่เห็นในรอบ 5) = เรนเดอร์ได้ 100% โดยหน้าตาสวย ~99.8%

### งานถัดไปหลังจากนี้
1. ยังค้าง: **toast เซฟ/โหลดในเกม** (`msg.bin` — เซฟ = ไทยจริง, โหลด = donor Cyrillic บน
   `tbgm_0p_ja`) เป็นตัวชี้ว่า UI ในเกมวิ่งบนฟอนต์ไหน และ tbgm รับ record cp ไทยที่เพิ่มเข้าไปไหม
2. โควตาฟอนต์ไตเติล: 384 เซลล์ ใช้ได้จริง ~260 · เมนูไตเติล 8 สตริงใช้ไป 31 เซลล์
   → ต้องรวบรวมข้อความทั้งหมดที่วาดด้วยฟอนต์นี้ก่อน แล้วนับ cluster ไม่ซ้ำ
3. Nexus เข้าได้แล้วผ่าน `https://r.jina.ai/<url>` (ยืนยัน 20 ส.ค. 2026 — ดึงหน้า
   judgment/mods/228 สำเร็จ) แต่รายชื่อไฟล์/ดาวน์โหลดยังต้องล็อกอิน = งานผู้ใช้

### ที่ผู้ใช้ต้องแคป — รอบ 3 (เสร็จแล้ว)
| เมนูเดิม | ข้อความไทย | กลุ่ม donor | ตอบ |
|---|---|---|---|
| EXIT GAME | ออกจากเกม | A = เซลล์มีหมึก U+00C0+ | ไทยขึ้นไหม + ระยะห่าง |
| PHOTO GALLERY | ออกจากเกม | B = เซลล์ว่าง U+0102+ | เติมเซลล์ว่างได้ไหม (ข้อความเดียวกับข้างบน = เทียบตรง) |
| NEW GAME | เริ่มเกมใหม่ | A | มาร์กได้ advance 0 หรือแยกตัว |
| SETTINGS | ตั้งค่า | A | มาร์กซ้อน 2 ชั้น |
| CONTINUE | เล่นต่อ | B | มาร์กบนเซลล์ว่าง |
| VS MINIGAMES / LICENSE / CREDITS | ไม่แตะ | — | ตัวควบคุม EN |

### research เว็บ 20 ส.ค. 2026 (6 agent — เอกสารเต็มใน `docs/research_web/`)
- ไม่มีใครในโลกแก้ปม fixed-pitch ของ Dragon Engine ได้ และไม่มีเอกสารฟอร์แมต `FONT!` ที่ไหนเลย
- **Retrial ไม่ใช่ม็อดแปล** (แก้ CLAUDE.md ทั้งสอง repo แล้ว) แต่ changelog มีเคส fix tofu ของ zh
- The Red Team (เวียดนาม) ปล่อย Lost Judgment เวียดหัวแล้ว **สกรีนช็อตแสดงระยะ proportional
  + วรรณยุกต์ซ้อนถูก** (มี tofu หลุดจุดหนึ่ง) — โหลดไฟล์ไม่ได้ (แจกผ่าน cloud PC) ติดต่อ
  Discord `discord.com/invite/theredteamvn` ถ้าจะถามวิธี
- **DragonTweak** (`github.com/Lyall/DragonTweak`) hook `Judgment.exe`/`LostJudgment.exe`
  ด้วย AOB scan + safetyhook ได้จริงทั้งที่มี Denuvo = harness พร้อมใช้ถ้าต้องไปทาง DLL
- Lost Judgment: `font.coyote.par` = `FONT!` ไม่ใช่ SDF (เกมติดตั้งแล้วที่ E:) แก้ CLAUDE.md ของ repo นั้นแล้ว

---

## สถานะเดิม: PoC deploy แล้ว 15 ส.ค. 2026 — รอผู้ใช้เปิดเกมแคปหน้าไตเติล (diagnostic A/B)

### ข้อค้นพบใหญ่ 14-15 ส.ค. 2026 (เกมติดตั้งแล้วที่ E:\SteamLibrary)
- **codename `judge` ยืนยัน** · db par เดียว: `db.judge.en.par` (ARMP v2, 1,358 bins, reARMP ใช้ได้) · ไม่มี ja par
- **ฟอนต์ = format `FONT!` ยุค Y6 เป๊ะ** (ไม่ใช่ K2R!) — loose folder `data/font.judge/en/` ไม่ใช่ par:
  `tbgm_0p_ja` (main, 7,093 glyphs, cell 40×40, capacity 9,250) + `gothic` (สัญลักษณ์ 8 ตัว) + `symbol` + `yakuza.dds` (bitmap ไม่มี bin — กับดักแบบ Y6 §8 ห้ามยุ่ง)
- donor Cyrillic 66 + Samaritan ครบตาม y6_slotmap 83/83 · slot ว่าง 2,157 · atlas ว่างใต้ y=3120
- **ม็อด Y7 Thai AI (MODV4) แกะแล้ว**: donor Cyrillic ธรรมดา ไม่ได้เพิ่ม cp ไทยจริง, metrics ไม่แตะ, บาง cp ใน text ไม่มีกลิฟในฟอนต์เลย (งานหยาบ) — ไม่มีเทคนิคใหม่ให้เรียน
- **build PoC สองแนวในไฟล์เดียว** (`scripts/inject_thai_judge.py`): วาด Sarabun 83 ตัวลงโซนว่าง atlas แล้วชี้ record 2 ชุด — (a) donor remap 83 (b) **เพิ่ม record cp ไทยจริง 83** (declared 7093→7176) — ถ้าเกมรับ (b) = เลิกใช้ donor ได้ทั้งโปรเจกต์
- db สปอย: `scripts/make_spoil_title.py` → title_root.bin เมนูไตเติลไทยสลับ real/donor รายแถว (แผนที่ใน `build/text/SPOIL_MAP.md`)
- deploy แล้ว (`scripts/deploy_spoil.py`): ฟอนต์ drop-in (.orig backup แล้ว) + SRMM ติดตั้ง + mods/JudgmentThai/db.judge.en/en/title_root.bin + MLO regen OK (1 mod / 1 file)
- ถอดทั้งหมด: `python scripts/deploy_spoil.py --restore`

### ผลเทสต์รอบ 1 (15 ส.ค. 2026 — ภาพหน้าไตเติลจากผู้ใช้)
- **db ม็อดโหลดผ่าน SRMM สำเร็จ** — แถวที่แปลเปลี่ยนจริง (VS MINIGAMES/LICENSE/CREDITS ที่ไม่แตะยังเป็น EN)
- **ทุกแถวไทยว่างเปล่า ทั้ง real-cp และ donor** → หน้าไตเติล**ไม่ใช้ tbgm_0p_ja** — ใช้ฟอนต์ condensed (คาด `meta_ot_cond_book.dds` — ไม่มี .bin คู่ = กับดักเดียวกับ yakuza.dds/Y6 §8) ไม่มีทั้ง Cyrillic ทั้งไทย
- ข้อสรุปเชิงนโยบาย (ตาม Y6): **หน้าไตเติล/เมนูที่ใช้ฟอนต์ bitmap → คง EN** · คำถาม real-cp vs donor ยังไม่ได้คำตอบ — ต้องเทสต์กับจอที่ใช้ tbgm จริง

### รอบ 2 deploy แล้ว — รอผู้ใช้เทสต์ (3 จุด ทริกเกอร์ง่าย)
| ที่ | ข้อความ | โหมด |
|---|---|---|
| จอ Press any button (ก่อนไตเติล) | กดปุ่มใดก็ได้ | real |
| เซฟเกม → ข้อความยืนยัน | บันทึกเรียบร้อยแล้ว | real |
| โหลดเซฟ → ข้อความยืนยัน | โหลดเรียบร้อยแล้ว | donor |
ผู้ใช้ทำ: เปิดเกม (ดูจอ press any button) → โหลดเซฟ (ดู toast) → เซฟเกม (ดู toast) → แคปทุกจุด
หมายเหตุ: title_root ไทยยังค้างใน mods อยู่ (ไม่เป็นไร — จอนั้นวาดไม่ได้ก็แสดงว่าง/EN เดิม)

### สิ่งที่ต้องอ่านจากภาพหน้าจอผู้ใช้ (หน้าไตเติล — รอบ 1, จบแล้ว)
| เมนู | ที่คาด | โหมด |
|---|---|---|
| NEW GAME → เริ่มเกมใหม่ | real-cp | เกมรับ record ที่เพิ่ม? |
| CONTINUE → เล่นต่อ | donor | เส้นทางพิสูจน์แล้วภาคอื่น |
| SETTINGS → ตั้งค่า | real-cp | mark ลอย ั ้ ่ |
| EXIT GAME → ออกจากเกม | real-cp | **ไม่มี mark = ตัวควบคุม** |
| ที่เหลือดู SPOIL_MAP.md | | |
อ่านผล: (1) แถว real ขึ้นไทย = เกมรับ record ใหม่ (2) mark ลอยอยู่ถูกที่ = engine อ่าน advance 0 (3) ระยะห่างตัวอักษร = ดู half/full-width classification (ปม Y6) — ถ้าห่างผิดปกติต้องดู engine เพิ่ม
⚠ หน้าไตเติลอาจวาดด้วย `yakuza.dds` bitmap (แบบ Y6 EN mode) — ถ้าเมนูโชว์ค้าง EN/หาย ให้ย้ายเป้าทดสอบไปซับใน-เกม (bin กลุ่ม sound_auth_subtitles / caption)

### ชุดฟอนต์ port จาก K3 แล้ว (14 ส.ค. 2026 — เตรียมทำ PoC/สปอยทันทีที่เกมลง)
- copy แล้ว: `scripts/{font_tool,thai_encode,inject_thai_sdf,survey_fonts}.py` + `tools/ParTool.exe` + `font/Sarabun-Regular.ttf`
- สร้าง `scripts/paths.py` (port จาก k3_paths — JUDGE_GAME env, codename `judge` ⏳, MOD_NAME=JudgmentThai)
- แก้ import `k3_paths`→`paths` ใน inject/survey แล้ว · inject มี guard: FONT_BASENAME=None → สั่งให้รัน survey ก่อน
- `python scripts/paths.py` self-check ผ่าน — เหลือ `--` เฉพาะของที่รอเกม/extract ตามคาด

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
