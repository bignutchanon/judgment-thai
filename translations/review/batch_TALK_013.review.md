# QC Review — batch_TALK_013

ตรวจ 250 key จาก `talk.bin` — a06/a07 (คดีมือระเบิด/The Mad Bomber) + a18/a19/a30/a45 (อามาเนะหมอดู/เมกุโระ)
เทียบกับ `translations/worklist/batch_TALK_013.json` (EN) + `extracted/facts/talk_speaker.json` (speaker/gender/table รายบรรทัด)

## สรุปผล

- **แก้ทั้งหมด 14 จุด** ในไฟล์ `translations/done/batch_TALK_013.done.json`
- `python scripts/check_pronoun_pairs.py --files translations/done/batch_TALK_013.done.json` → **พบปัญหา 0 จุด**
- `python scripts/merge_qc.py --dry-run --only TALK_013` → **ผ่าน 250 · ตก 0 · ขาด 0**
- ไม่พบสัญลักษณ์ต้องห้าม (♪❤♥★☆•※) หรือ Latin ที่มีเครื่องหมาย (accented) ในไฟล์นี้

## 1. ประเด็นหลักของ batch — สรรพนามมือระเบิด (11 จุด)

ตรวจตามคำตัดสิน lead: เกณฑ์คือ **ความหยาบของ EN บรรทัดนั้นเอง** ไม่ใช่การเดาว่าเป็นมือระเบิด
ไล่ทุกบรรทัดของ `???`/`The Mad Bomber` เทียบกับ `talk_speaker.json` (ยืนยันลำดับจริงในตาราง a06→a07)
พบ 11 บรรทัดที่นักแปลใช้ **T3 กู/มึง** ทั้งที่ EN ยังไม่มีคำหยาบ/สบถ (แค่เยาะเย้ย/สุภาพ-แดกดัน หรือให้เบาะแส)
— แก้กลับเป็น **ฉัน↔คุณ** ให้ตรงโทนเดียวกับ TALK_012 ทั้งหมด:

| EN (ย่อ) | เดิม | แก้เป็น |
|---|---|---|
| Don't you feel like a fool for paying taxes...? | มึง | คุณ |
| Hahaha, I like your style, Yagami-san... | กู/มึง | ฉัน/คุณ |
| This new bomb I've set up... packs a real punch. | กู | ฉัน |
| There's an ox inside the inn. That's where you'll find it. | มึง | คุณ |
| Hahaha, wonderful! You've done wonderfully, Yagami-san! | มึง | คุณ |
| Hold your tongue. ...blame Kamurocho, not me. | กู/มึง | ฉัน/คุณ |
| Save your taunts. You'll eat those words... | มึง | คุณ |
| Haha... Glad you decided to answer the phone. I was getting lonely. | กู/มึง | ฉัน/คุณ |
| A grudge? You're the one who started this, Yagami-san... | มึง | คุณ |
| It would have gone off... but you just had to play hero! | มึง | คุณ |
| Your hint is... The pigeon coos among the cherry blossoms! | มึง | คุณ |

**หลังแก้ เหลือ T3 (กู/มึง) จริง 11 บรรทัด** — ทุกบรรทัดมีคำหยาบ/บริบทไคลแม็กซ์รองรับชัดเจน:
`dumbass` (ไอ้โง่) · ฉากเฉลย "I am the last bomb!" (ชูระเบิดขู่ระเบิดตัวเอง) · `trash` + ปราศรัยก่อนระเบิดตัวเอง (sons of bitches / assholes / sacrificing myself) · `Hell no!` · `Fuck you! ...shithead!` · `smartass...asshole!` · และบรรทัดถัดไปทันที "I'm the one in charge here." (ต่อเนื่องอารมณ์จากบรรทัด asshole)

### จุดที่ไม่แน่ใจ — ขอให้ lead ยืนยัน
บรรทัด **"Your hint is... The pigeon coos among the cherry blossoms!"** อยู่ติดกันทันทีหลัง
"...Stop it if you can, **dumbass**!" (ยังเป็น T3 ถูกต้อง) — ตัวบรรทัดเองไม่มีคำหยาบ จึงแก้เป็น "คุณ" ตามเกณฑ์
"ความหยาบของบรรทัดนั้นเอง" แต่ก็เป็นลมหายใจเดียวกับที่เพิ่งด่า "ไอ้โง่" ไปหมาด ๆ — ถ้า lead มองว่าควรนับเป็น
ช่วงอารมณ์เดียวกัน (คงมึง/กู ต่อเนื่อง) ให้แจ้งกลับมา จะสลับกลับให้

## 2. Honorific หลุด — Meguro-san (3 จุด)

พบ `-san` ของ "Meguro-san" ถูกแปลเป็น "คุณเมกุโระ" ทั้ง 3 จุด ทั้งที่กฎ honorific (PRONOUN_MATRIX.md
คำตัดสิน 21 ส.ค. 2026) บังคับว่า **EN มี -san → ต้องแปล ซัง เสมอ** และเช็คกับ `master_th.json` (batch อื่นที่ merge ไปแล้ว)
พบว่าใช้ **"เมกุโระซัง"** สม่ำเสมอ 6/6 จุด — แก้ทั้ง 3 จุดให้ตรงกับ precedent:

- "That's Meguro-san, a regular of mine." → นั่นคือ**เมกุโระซัง** ลูกค้าประจำของดิฉันค่ะ
- "Do you remember Meguro-san?" → คุณจำ**เมกุโระซัง**ได้ไหมคะ?
- "(There's Meguro-san. It looks like he's had one too many.)" → (นั่น**เมกุโระซัง** ท่าทางเมาหนักไปหน่อยแล้วนะ)

("Amane-san" ในไฟล์นี้ถูกอยู่แล้วทุกจุด — "อามาเนะซัง")

## 3. ตรวจตามปกติ — ไม่พบข้อผิดพลาดเพิ่ม

- **ผู้พูดทั้ง 250 คีย์**: เทียบกับ `talk_speaker.json` ครบทุกบรรทัด (ดึง table+speaker จริงตามลำดับแถวใน
  `judge_side_a06`/`a07`/`a18`/`a19`) — ไม่พบคำแปลผิดตัวผู้พูด, ไม่พบ dupes ที่ขัดกับ table บนสุด
- **ยากามิ**: ใช้ "ผม" ทุกจุด ไม่มี T3 หลุด · บรรทัด "Listen, you son of a—" แปล "ฟังนะ ไอ้เวร—" ใช้คำด่าเป็นนามไม่ใช่สรรพนาม จึงไม่ผิดกฎ T1
- **เพศ**: เมกุโระ ยืนยันเพศชายจาก EN pronoun ("What's **his** deal?", "why did **he** run away") ตรงเกณฑ์ §0.1 ข้อ 1 — ใช้ "ฉัน/แก" (T2) สอดคล้อง ไม่ผิด · อามาเนะ/Fortune-teller Lady ยืนยันหญิงจาก "lady" + ล็อกจากตารางเดิม (Amane=female) — ใช้ ดิฉัน/ค่ะ ถูกต้อง · Convenience Store Clerk, Newscaster, Young Barker, Man from the Rip-off Bar (เพศ unknown) — คำแปลไม่มีคำลงท้ายหรือสรรพนามบอกเพศเลยสักจุด ผ่าน
- **คำล็อกใหม่จากนักแปล**: Ryu Asaka→ริว อาซากะ, Shangri-La→แชงกรีล่า, Black Alice→แบล็กอลิซ ใช้ตรงรูปเดียวกันทุกจุดที่ปรากฏ
- **สถานที่**: Akaushimaru→อากาอุชิมารุ, Kanrai→คันไร, Poppo→ป๊อปโป, Pink Street→ถนนพิงก์สตรีท, Tenkaichi Street→ถนนเทนไคจิ — ตรวจกับ `master_th.json` ที่ merge แล้วทุกคำ สะกดตรงกัน 100%
- **เวลาในคดี**: ไม่มีบรรทัดใดอ้างเวลานาฬิกา (AM/PM) ใน batch นี้ — ไม่มีจุดต้องเทียบ
- **สัญลักษณ์ต้องห้าม/Latin หลุด**: สแกนทั้งไฟล์ ไม่พบ

## 4. บันทึกไว้เผื่อ lead อยากตั้งกฎเพิ่ม

- **`-shi` (honorific ของ Tsukumo เรียกยากามิ "Yagami-shi")** ถูกตัดทิ้งเหลือแค่ชื่อเปล่า "ยากามิ" ทั้ง 3 จุดในไฟล์นี้
  (สม่ำเสมอ ไม่ขัดกันเอง) — แต่ยังไม่มีกฎเขียนไว้ใน glossary/PRONOUN_MATRIX (มีแค่ -san/-chan/-kun/-sama)
  เสนอให้ lead บันทึกเป็นกฎอย่างเป็นทางการ (ตัด -shi ทิ้ง = ค่าเริ่มต้น) กัน batch ถัดไปสับสน
- คำแนะนำเข้า glossary: "Meguro-san → เมกุโระซัง" ควรถูกบันทึกเป็นแถวล็อกใน §7 ให้ชัดเจน (ตอนนี้พึ่ง precedent
  ใน master_th.json เท่านั้น ไม่มีในตารางกฎ)

## ไฟล์ที่แก้
- `translations/done/batch_TALK_013.done.json` (14 จุด)
- `translations/review/batch_TALK_013.review.md` (ไฟล์นี้)
