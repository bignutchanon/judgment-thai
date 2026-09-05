# QC Review — batch_034 (ไซด์เควส "จมูกแดง" บทที่ 3)

สถานะ: **ผ่าน** — `merge_qc.py --dry-run --only 034` → ผ่าน 250 · ตก 0 · ขาด 0

## จำนวนที่แก้: 10 จุด (จาก 250 คู่)

### 1. แปลผิดความหมาย (1 จุด)
- `"He tracked Red Nose down and took the money back.\nBut Kaito-san's still out in the cold."`
  เดิมแปล "out in the cold" (สำนวน = ถูกทิ้งขว้าง/ไม่ได้รับความเป็นธรรม) เป็น **"ยังต้องเร่ร่อนต่อไป"**
  ซึ่งหมายถึงไร้บ้านจริง ๆ — ผิดความหมายและชนกับบริบท (จมูกแดงต่างหากที่ไร้บ้าน ไคโตะเป็นแค่ถูกไล่ออกจาก
  ตระกูล/ไม่ได้รับการล้างมลทิน) แก้เป็น **"ยังโดนลอยแพเหมือนเดิม"**

### 2. สรรพนามผิดคู่ (6 จุด — ยืนยันด้วย field "1" speaker-slot id ใน sound_auth.bin.json)
ไล่ตาม speaker-slot id ยืนยันได้ว่าฉากโทรศัพท์ระหว่างยากามิ-ไคโตะ (id 638=ยากามิ, 636=ไคโตะ) กับ
ฉากที่สวนเด็ก/บาร์ชาร์ลส์ (id 641/643=ยากามิ-ไคโตะรอบสอง) มีบรรทัดที่ยากามิใช้ "ครับ" คุยกับไคโตะ
แบบสองต่อสอง (ไม่มีบุคคลที่สาม) ซึ่งขัดกฎ PRONOUN_MATRIX §1 ("ไม่มีคำลงท้ายสุภาพระหว่างกัน เว้นมี
บุคคลที่สามฟังอยู่") — สังเกตว่า field "6" (คำแปลอีกฉบับของบรรทัดเดียวกัน) ไม่มี "ครับ" อยู่แล้ว ยืนยัน
ว่าเป็นจุดที่นักแปลพลาดไม่สม่ำเสมอ:
- `"On my way to the Children's Park...\nThink I might run into the thief."` — ตัด ครับ
- `"Not sure. But even if he isn't,\nI might find a lead or two."` — ตัด ครับ
- `"Looks like it."` — ตัด ครับ (กลับไปตรงกับ ref_tm เดิม)
- `"Let's head to Charles then."` — ตัด ครับ (sibling "Higashi should be at Charles." ไม่มี ครับ)

และอีก 2 จุด: ไคโตะ (speaker id 641, T2 "ฉัน") ใช้ "ครับ" หลุด T2 ในฉากสวนเด็ก (ทั้งที่บรรทัดอื่น ๆ
ของไคโตะในฉากเดียวกันไม่มี ครับ เลย — ไม่สม่ำเสมอในตัวละครเดียวกัน):
- `"Where would he have even gotten a gun?"` — ตัด ครับ
- `"Where would he even have\ngotten a gun?"` — ตัด ครับ

(บรรทัดอื่นที่มี "ครับ" ของยากามิ→ไคโตะ/ฮิงาชิ ที่ยังมีคนอื่นอยู่ในฉากด้วย เช่น "Who do you think
killed him?", "Yeah. Captain Hamura." ปล่อยไว้ตามเดิม เพราะมีบุคคลที่สาม — ตรงกับข้อยกเว้นในกฎ)

### 3. คำล็อกไม่ตรง glossary (2 จุด)
- `"Let's head to Charles then."` และ `"Higashi should be at Charles."` — ยังคง EN "Charles" อยู่
  ทั้งที่ lead ล็อก **Charles → ชาร์ลส์** แล้วใน batch_033 — แก้ให้ตรงตามคำสั่งงาน

### 4. ความสม่ำเสมอภายใน batch (1 จุด)
- `"My legs're kinda shot, though, as you can see.\nNo playtime for this hobo."` ใช้ "คนเร่ร่อน"
  ขณะที่ sibling variant "But my legs are shot to shit.\nNo VR for this hobo." (คนพูดเดียวกัน จุดเดียวกัน)
  ใช้ "คนไร้บ้าน" — แก้ให้ตรงกัน (ใช้ "คนไร้บ้าน")

### 5. ภาษาไทยไม่เป็นธรรมชาติ (1 จุด)
- `"Fine. I'll come."` → เดิม "ก็ได้ ฉันไปด้วยก็ได้" ซ้ำคำ "ก็ได้" สองรอบ — แก้เป็น "ก็ได้ ฉันไปด้วย"
  ให้ตรงกับ sibling ("Okay. I'll come." = "ก็ได้ ฉันไปด้วย")

## ผลยืนยันผู้พูด idx 201-225 ("You're late, Kaito-san" section)

ไล่ field `"1"` (speaker-slot id) ใน `extracted/db_en/en/sound_auth.bin.json` แถว 350-443
(ตาราง `speech_list_judge_main_c03`) เทียบกับบรรทัดที่ยืนยันได้อยู่แล้วในฉากเดียวกัน (เช่น
"To rub me out?" ใช้ "me" = ไคโตะพูดเอง, "(...pinned it on Kaito-san...)" = มุมมองยากามิ) สรุปแมป
ได้ชัดเจนทั้งฉาก:

**ฉากสวนเด็ก (id 641/642/643):**
- **643 = ยากามิ** — พูด `"You're late, Kaito-san."` (แถว 402), `"You're coming too, right
  Kaito-san?"` (แถว 413), `"I'm gonna go talk to Higashi."`, `"Let's head to Charles then."`
  → **ยืนยัน: "You're late, Kaito-san." เป็นบทของยากามิพูดทักไคโตะที่มาช้า** (ไม่ใช่คนอื่นพูดใส่ไคโตะ)
  คำแปลปัจจุบัน "มาช้านะ ไคโตะซัง" ใช้ได้ ไม่ต้องแก้
- **641 = ไคโตะ** — พูด `"Sorry, but my buddy here's got more fight..."` (อวดยากามิให้แก๊ง),
  `"Is this the guy who was looking for Red Nose? This him?"`, `"I... I just can't believe it.
  Higashi's not a murderer."`, `"Where would he even have gotten a gun?"` (T2 "ฉัน")
- **642 = หัวหน้าแก๊งคนไร้บ้านสูงวัย** — พูดทุกบรรทัดเล่าเรื่องศพ/ตำรวจ/Tojo Clan yakuza

**ฉากบาร์ชาร์ลส์ (id ใหม่ต่อ — 644/645/646, คนละเลขแต่ตัวละครเดิม):**
- **644 = ฮิงาชิ** — ปฏิเสธการฆ่า, เฉลย "They wanted to rub you out of the picture, Kaito"
  (ใช้ "พี่ไคโตะ" ตรงกับที่ lead กำหนด T1+"พี่ไคโตะ")
- **645 = ไคโตะ** — ยืนยันจาก "To rub **me** out?" ที่ใช้สรรพนามอังกฤษชี้ตัวเอง
- **646 = ยากามิ** — ยืนยันจาก monologue tag `"(So Hamura staged a robbery and pinned it on
  Kaito-san...)"` ที่เป็นมุมมองบุคคลที่หนึ่งของยากามิพูดถึงไคโตะแบบบุคคลที่สาม

## คำที่ควรเพิ่ม glossary
- ไม่มีคำใหม่ที่ต้องล็อกเพิ่ม — ชื่อเฉพาะทั้งหมดในไฟล์นี้ (Red Nose/Theater Alley/Children's Park/
  Play Pass/Suguroku/Dice & Cube/Paradise VR/Charles) ตรงกับตารางที่ lead ตัดสินไว้แล้วครบ

## จุดที่ยังไม่แน่ใจ อยากให้ lead ตัดสิน
- `"You find him?"` (NPC พูดกับยากามิ ยืนยัน speaker id 634≠ยากามิ) แปลว่า "เจอเขาไหมครับ?" —
  ใช้ "ครับ" ซึ่งดูสุภาพเกินบุคลิกเดิมของ NPC ที่เพิ่งพูด "yeah?" ห้วน ๆ ก่อนหน้า — ไม่ชัดเจนพอจะถือว่า
  "ผิดจริง" (ไม่มีกฎล็อกบุคลิก NPC รายนี้) จึงไม่แก้ แต่ทิ้งข้อสังเกตไว้เผื่อทีมแฟ้มตัวละครอยากกำหนดโทน
  ให้ NPC กลุ่มนี้ชัดเจนกว่านี้ในอนาคต
- มุกจมูกแดง ("I don't think his nose is all that red." / "You call that a red nose? I sure as
  hell don't.") ยังคงทำงานได้หลังแปลเป็น "จมูกแดง" — ตรวจแล้วไม่มีปัญหา
