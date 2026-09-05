# รายงานตรวจ QC — batch_058

สถานะ: `python scripts/merge_qc.py --dry-run --only 058` → **ผ่าน 250 · ตก 0 · ขาด 0**

## แก้ไปทั้งหมด 15 จุด (ทุกจุดเป็นเรื่องเดียวกัน: ทะเบียนสรรพนามของฮัตโตริ)

**ปัญหาที่พบ**: นักแปลตั้งทะเบียนฮัตโตริเป็น T3 "กู" ตามค่า default ในไฟล์ตัวละคร (`characters_main.json`)
โดยยึดแค่แท็กบทที่ 9 ไม่ได้เช็คเนื้อหา EN จริงของฉากนี้ (นัดคุยงานวิจัย AD-9/อัลไซเมอร์ผ่านโฮชิโนะ)
— ตรวจ EN ทุกบรรทัดของฮัตโตริในฉากนี้แล้ว **ไม่มีคำหยาบเลย** (ไม่มี fuck/asshole/punk/bastard)
เป็นโทนกวนโมโหแบบนักข่าวเจ้าเล่ห์ ไม่ใช่ข่มขู่แบบยากูซ่า → ตามคำสั่ง lead ในบรีฟ ต้องถอยจาก T3 เป็น **T2 (ฉัน)**

**แก้ 14 บรรทัด**: `กู` (self-reference ของฮัตโตริ) → `ฉัน` ในบรรทัดต่อไปนี้ (ตัวแปร EN):
- "I only report on things that interest me..."
- "I'm not sure I'd go that far."
- "He just calls me in for favors..." (2 ตัวแปร)
- "Helps to be on good terms with the guy..." (2 ตัวแปร)
- "After all... I heard about Shintani-sensei's death..."
- "All right, all right. But you'll owe me for this." / "Fine, I get it. But... you'll owe me for this."
- "I guess my point is, dementia's not something to fear..." / "My point is, dementia's not some farfetched horror story..."
- "The way I see it... The real dangers here are ignorance and apathy..."
- "Good. I'd like to give you a rundown..." (2 ตัวแปร)

คำเรียกยากามิของฮัตโตริ **ไม่ต้องแก้** — จุดที่ EN เขียน "Yagami-san" ตรง ๆ ใช้ "ยากามิซัง" อยู่แล้ว (ถูกตามกฎ honorific-ตาม-EN)
จุดที่ EN ไม่มี honorific ใช้ "นาย" ซึ่งเป็นคำเรียกที่ยืนยันแล้วว่าใช้ได้ใน T2 ตามบรรทัดฐาน "ไคโตะ → ยากามิ: นาย/ทาคุ" ใน PRONOUN_MATRIX §override — ไม่ถือว่าข้ามระดับ

**แก้ 1 บรรทัด (จุดร้ายแรงกว่า — ยากามิใช้ "กู")**: `"I thought you called me here\nto talk about AD-9."`
ยืนยันแล้วว่าเป็นบทของ **ยากามิ** ไม่ใช่ฮัตโตริ (เป็นบทตัวเลือกพูดจาก `talk_select_select.bin` ที่ยากามิใช้ตัดบทคุยเรื่องส่วนตัวของฮัตโตริ ต่อเนื่องกับ "I'm here to talk AD-9." / "If that's not what this is about, I'm not sticking around." ซึ่งทั้งสามบทใช้ "ผม" ถูกต้องอยู่แล้ว ยกเว้นบรรทัดนี้บรรทัดเดียวที่หลุดเป็น "กู")
แก้ `นึกว่านายเรียกกูมา\nคุยเรื่อง AD-9 ซะอีก` → `นึกว่านายเรียกผมมา\nคุยเรื่อง AD-9 ซะอีก`
— ตรงกับกฎเหล็กข้อ 3 ในโจทย์: ยากามิห้ามใช้ กู/มึง/แก ทุกกรณี ถือเป็นจุดที่ร้ายแรงกว่าจุดอื่นเพราะเป็นตัวเอก

## ยืนยันผู้พูดด้วย speaker_exact / speaker-slot id (ตามที่ lead สั่งให้ตรวจ)

**สรุปยืนยันจาก `speech_speaker_map.json`** (chapter 09, key `speech_list_judge_main_c09`):
- **ฮัตโตริ**: "Hm? Oh, I didn't notice you there, Yagami-san." (×2 ตัวแปร) · "All right, I'm done. Thanks for stopping by/coming by, Yagami-san." (×2) · "Kinda strange sharing a bowl of ramen with you." (×2)
- **โฮชิโนะ**: "Sounds like the plan didn't go so well." (×2) · "Yes. Hattori-san is making time especially for you." (×2)
- **ยากามิ**: "They were desperate. Still, we did manage to talk to Hamura." · "Can we skip this part?"
- ที่เหลือในฉากร้านราเมง (rows 148–164, 169–190) ไม่มี `speaker_exact` ตรง ๆ — ไล่ตามลำดับบทสนทนา/เนื้อหาเทียบกับจุดที่ยืนยันแล้วข้างต้น สรุปได้ชัดเจนว่า: มุกล้อกล้องมือถือ (148–153) = ยากามิสลับกับฮัตโตริ, บทกดดันให้ไปคุย AD-9 (185–190) = ยากามิ↔ฮัตโตริ, บทบรรยายวิชาการอัลไซเมอร์ทั้งหมด (192–249 ไม่มีตัวเอ่ยนาม) = ฮัตโตริบรรยาย ยากามิสอด ("Yeah, yeah. It's tough, I get it." / "You're gonna even if I say no, right?" ใช้ ผม+ครับ ถูกต้องอยู่แล้ว)

**มินิเกมด่านรหัสผ่านโจฮัง** (`sound_auth.bin.json`, sub-table `speech_list_judge_main_c08`, rows ~640–663):
ไล่ field `"1"` (speaker-slot id) ยืนยันแล้ว:
- **id 1145 = ยากามิ** (พูดรหัสผ่าน/ตัวเลือกทั้งถูกและผิด — "Chateaubriand, blue." "You ever been mooned?" ฯลฯ รวมถึง **"It's fine! We'll be fine."** ซึ่งเป็นตัวแปรข้อความของ id เดียวกับ "What? No, of course not. I'll get it, I'll get it." แถว 647 — ยืนยันว่าเป็นบทยากามิ ไม่ใช่ผู้พูดไม่ทราบชื่อ)
- **id 1143 = ไคโตะ** (ยืนยันจาก "Nice goin', Tak!" ที่ id เดียวกันเรียกยากามิว่า "Tak")
- **id 1144 = พนักงานร้าน/คนในบ่อน** (ไม่มีชื่อ — "He says he wants steak." "Thank you for your order. Enjoy your meal.")
⚠ id ชุดนี้ใช้ได้เฉพาะในช่วงมินิเกมนี้เท่านั้นตามคำเตือนในบรีฟ ไม่ได้เอาไปแมปกับ `speakers.json`

ทั้งสองผู้พูด (ยากามิ id1145, ไคโตะ id1143) ในมินิเกมนี้แปลแบบเลี่ยงสรรพนามชัดเจน (ไม่มี "ผม"/"ฉัน" โผล่ในบรรทัดที่ตรวจ) ยกเว้นจุดที่ไคโตะพูด "You hungry, man? I can go grab you something..." ใช้ "ฉัน" ถูกต้องตาม T2 ของไคโตะอยู่แล้ว — ไม่ต้องแก้

## จุดที่ตรวจแล้วผ่าน ไม่ต้องแก้ (รายงานไว้เผื่อ lead อยากรู้ขอบเขตที่ตรวจ)

1. **cho-han → โจฮัง**: ตรวจครบทั้ง batch (2 จุดที่มีคำนี้) สะกดถูกทั้งคู่ ไม่มี "โจฮัง" ตกค้าง
2. **ศัพท์สเต๊กในด่านรหัสผ่าน**: ริบอาย/เซอร์ลอยน์/ชาโตบรียอง/เทนเดอร์ลอยน์/เวลดัน/มีเดียมแรร์/บลู และรหัส "มูน" — สะกดตรงกันทุกบรรทัดที่ปรากฏซ้ำ (คำสั่ง+คำตอบ) ไม่มีจุดไหนเพี้ยน
3. **Tak → ทาคุ**: ใช้ตรงกันทุกจุดที่ไคโตะ/ฮามุระเรียกยากามิ
4. **การจับคู่สรรพนามฮัตโตริ↔ยากามิ**: หลังแก้ 15 จุดข้างบนแล้ว ไม่มีบรรทัดไหนผสม "คุณ"(T1)/"ผม"(T1) ปนกับ "กู"(T3) อีก — ทะเบียนทั้งฉากเป็น T2 เดียวกันหมด (ฉัน↔นาย/ยากามิซัง)
5. ยากามิยังคง "ผม" ทุกบรรทัดในฉากนี้ (รวมจุดสารภาพ/ครุ่นคิดคนเดียวใน `<color=ｍonologue>`) ไม่มี แก/กู/มึง หลงเหลือ

## ไม่มีจุดที่ต้องให้ lead ตัดสินเพิ่มเติม

ทุกจุดยืนยันได้ชัดจากหลักฐานไฟล์เกม (speaker_exact + speaker-slot id + เนื้อหา EN) ไม่มี false positive ที่ต้องถกกับ lead

## เสนอเพิ่ม glossary (ไม่ได้แก้ glossary.md เอง ตามขอบเขตที่กำหนด)

- ยืนยัน pattern: เมื่อ default ทะเบียนตัวละครใน `characters_main.json` เป็น T3 แต่ฉากเฉพาะไม่หยาบ ให้ถอยเป็น T2 ทั้งฉาก (ไม่ใช่ผสม) — เสนอบันทึกเป็นตัวอย่างอ้างอิงใน `characters_main.json` ของฮัตโตริ ต่อจากโน้ต pronoun_self เดิม ว่า "ฉากนัดผ่านโฮชิโนะ/บทบรรยายวิชาการ = T2 ฉัน (batch_058 ยืนยัน) ต่างจากฉาก batch_047 id900 ที่เป็น T3 กู/มึง"
