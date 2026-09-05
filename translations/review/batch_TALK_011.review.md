# QC — batch_TALK_011

ตรวจ 250 คู่ (EN↔TH) เทียบ `worklist/batch_TALK_011.json` กับ `done/batch_TALK_011.done.json`
source_bins: `talk.bin` · 4 ฉาก: A44 "Secrets of Cats" (ต่อจาก batch_010) · friend_a39 ช่างตัดเสื้อ Terahara/Le Marche ·
friend_a29 สูตรอาหาร Akaushimaru/Nasugawa · friend_a40 (1 บรรทัดสั้นใช้ซ้ำข้ามคดี — ดูหัวข้อ "คีย์ใช้ซ้ำ" ด้านล่าง)

ยืนยันผู้พูดทุกบรรทัดด้วย `extracted/facts/talk_speaker.json` (250/250 พบ ไม่มี MISSING) · เทียบ tag `<font_kind=...>`
ทุกคู่ด้วยสคริปต์ (0 mismatch) · รัน `check_latin_leftovers.py --done --only TALK_011` → พบ 0 ·
รัน `check_pronoun_pairs.py` → พบ 0

## ผล merge_qc.py

`python scripts/merge_qc.py --dry-run --only TALK_011` → **ผ่าน 250 · ตก 0** (หลังแก้)

## แก้ไป 1 จุด

### 1. บั๊กเฉพาะที่ lead สั่ง — คืนคำ "รังแก" (ตามคำสั่ง)

Regex `check_pronoun_pairs.py` เดิมจับ "รังแก" เป็นสรรพนาม "แก" ผิด (false positive) นักแปลจึงเลี่ยงไปใช้ "ระราน" —
lead แก้ regex แล้ว (`(?<!รัง)แก...`) ยืนยันแล้วว่า `"รังแก"` ผ่าน `check_pronoun_pairs.py` ปกติ (0 จุด)
คืนคำในจุดเดียวที่พบในไฟล์นี้:

- `"(Why would anyone pick on their friendly neighborhood tailor? I can't just let this slide.)"`
  "(ใครกันจะมา**ระราน**ช่างตัดเสื้อใจดีประจำย่านแบบนี้ ผมปล่อยผ่านไม่ได้หรอก)"
  → "(ใครกันจะมา**รังแก**ช่างตัดเสื้อใจดีประจำย่านแบบนี้ ผมปล่อยผ่านไม่ได้หรอก)"
  ("รังแก" ตรงความหมาย "pick on" มากกว่า — เป็นธรรมชาติกว่าในบริบทนี้)

ค้นทั้งไฟล์หาคำแปลตระกูล bully/harass อื่น ๆ (`pick on`, `bully`, `harass`, `mess with`) — พบแค่จุดนี้จุดเดียวในไฟล์นี้

## ตรวจผู้พูด — ผ่านทั้งหมด

เทียบ `talk_speaker.json` ครบ 250/250 · 15 ผู้พูด (Yagami 118 · Terahara 31 · Nasugawa 22 · Yakuza-esque Man 21 ·
Man in Black 18 · Wang 12 · Nekomiya 10 · Zhuang Shi 5 · Makihara 4 · Akaushimaru Employee 3 · Le Marche Employee 2 ·
Manager 1 · Young Female Customer 1 · Young Male Customer 1 · Moroboshi 1) — ไม่พบผู้พูดผิดตัว

- ยากามิ (`gender: male` ยืนยันจากตาราง) ใช้ "ผม" ทุกบรรทัด 118/118 · จุดที่มีคำว่า "แก" ปนอยู่ 4 จุด **ล้วนเป็น
  ยากามิพูดใส่แมว Zhuang Shi ตรง ๆ** (2nd-person address ต่อสัตว์เลี้ยง เป็นธรรมชาติในไทย ไม่ใช่การพูดใส่คน) — ไม่ใช่บั๊ก
- **Le Marche Employee → Terahara** และ **Akaushimaru Employee → Nasugawa** (ยืนยันจาก `characters_side.json`
  `friend_terahara`/`friend_nasugawa` change_talk_talker) ใช้ทะเบียนเดียวกันทั้งก่อน-หลังเปิดเผยชื่อ (ครับ/ผม สม่ำเสมอ)
- คำล็อก A44 ที่ lead ยืนยัน (Ruan Wang → หรวน หวัง · Zhuang Shi → จวง ซือ · Manager/Man in Black/Makihara = ชาย)
  ตรงกับที่ใช้ในไฟล์นี้ทั้งหมด — Wang พูดถึงตัวเองด้วย "ผม"/"ครับ" (ชาย) ตรงกับ Man in Black "ฉัน"/แทน Yagami ด้วย "แก"
  (ศัตรูข่มขู่ — T2/T3 ปนกันตามบทที่ตัวร้ายพูดหยาบใส่ยากามิ ไม่ใช่ยากามิพูดข้ามระดับ) · Makihara ใช้ ครับ/ผม สม่ำเสมอ

### เทียบข้ามไฟล์กับ batch_TALK_010 (อ่านอย่างเดียว ไม่ได้แก้)

ชื่อ/ทะเบียน Wang, Zhuang Shi, Man in Black, Manager, Makihara ตรงกันทั้งสองไฟล์ครบ · พบสิ่งที่ต้องแจ้ง lead:
**`batch_TALK_010.done.json` มี typo "ผมคือห**ห**หรวน หวัง" (ห ซ้ำ)** ในบรรทัด `"Yes, I am Ruan Wang. I apologize for
calling you out to a place like this."` — อยู่นอกขอบเขตที่แก้ได้ของ batch นี้ (ห้ามแตะไฟล์ batch อื่น) ขอให้ lead
มอบหมายแก้ใน TALK_010

## คีย์ที่ใช้ซ้ำหลาย bin

บรรทัด `"All right, let's see here..."` (entry #184) ตาราง `talk_speaker.json` ชี้ว่าเป็นของ **Moroboshi** ที่
`judge_friend_a40` (คนละคดีกับฉากช่างตัดเสื้อ a39 ที่บรรทัดนี้ปรากฏจริงในบริบท — Terahara กำลังวัดตัว/ลองสูทให้ยากามิ)
คำแปล "เอาล่ะ ขอดูหน่อยนะ..." เป็นกลาง ไม่มีคำเพศ/ทะเบียนเฉพาะตัว ใช้ได้กับทั้งสองบริบทโดยไม่กระทบความถูกต้อง — ไม่ต้องแก้
แต่บันทึกไว้เผื่อ lead อยากเพิ่มเข้า `docs/reference/multibin_keys.md`

## ตรวจคำล็อกสถานที่/ชื่อ — ตรงทั้งหมด

Tenkaichi Street → ถนนเทนไคจิ · Millennium Tower → มิลเลนเนียมทาวเวอร์ · M Side Cafe → เอ็ม ไซด์ คาเฟ่ ·
Theater Avenue → เธียเตอร์อเวนิว · Batting Center → ศูนย์ฝึกตี (รูปทั่วไป ไม่ใช่ "ศูนย์ฝึกตีโยชิดะ" — ถูกต้อง
เพราะบทพูดนี้ไม่ได้ระบุสาขา) · Senryo Avenue → ถนนเซ็นเรียว · Nyan Nyan Café → คาเฟ่เนียนเนียน · Tender → เทนเดอร์ ·
Naotaro Terahara → นาโอทาโร่ เทราฮาระ · Masuda → มาสึดะ · Nekomiya → เนโกมิยะ · Akaushimaru → อากาอุชิมารุ —
ทุกจุดตรงกับที่ ship แล้วใน batch อื่น (`done/batch_088-124`)

## ตรวจอื่น ๆ — ผ่าน

- สัญลักษณ์ต้องห้าม (♪❤♥★☆•※): 0 · อักษรละตินมีเครื่องหมาย: 0
- แท็ก `<font_kind=yakuza_italic>` ปรากฏ 3 คู่ (entry #142, #241, #245) — ตรงกันทุกจุด ไม่มี tag mismatch
- ความยาว TH/EN: ไม่มีจุดที่ TH ยาวเกิน EN แบบผิดปกติ (ratio > 1.6) จากการเช็คอัตโนมัติ
- โทน "Yakuza-esque Man" (21 บรรทัด, ฉาก Terahara โดนลูกค้าเกรียนกวน) ใช้ กู/มึง/วะ/สิ สม่ำเสมอตลอดฉาก ตัดกับ
  Terahara ที่สุภาพ ครับ/ผม/ท่าน ตลอด — บุคลิกไม่หลุด

## คำที่ควรเพิ่มเข้า glossary

- ไม่มีคำใหม่ที่ยังไม่ล็อก — ชื่อคน/สถานที่ทั้งหมดในไฟล์นี้ตรวจแล้วมีอยู่ใน glossary.md หรือ ship แล้วในไฟล์อื่นครบ

## ประเด็นที่ต้องให้ lead ตัดสิน

1. **typo `batch_TALK_010.done.json`** — "ผมคือหรวน หวัง" (ห ซ้ำ) ต้องแก้ใน TALK_010 แต่ scope ผู้ตรวจนี้แตะไม่ได้
2. Wang เรียกตัวเองแค่ "หวัง" ใน entry #36 ("A pity that Wang did not understand its true value." →
   "น่าเสียดายที่หวังไม่เข้าใจคุณค่าที่แท้จริงของมัน") — สอดคล้องกับที่ batch_010 เคยใช้ "หวัง" เดี่ยว ๆ มาก่อนแล้ว
   (เช่น "เป็นหวังที่จ้างแกมาใช่ไหม!?") จึงไม่แก้เพื่อความสม่ำเสมอ แต่ตั้งข้อสังเกตว่า "หวัง" ชนกับคำไทยทั่วไป (หวัง=hope)
   เสี่ยงอ่านสะดุดเล็กน้อย — ถ้า lead อยากให้ใช้ "หรวน หวัง" เต็มทุกจุดที่ไม่มีคำอื่นช่วยขยายความ ควรสั่งเป็นนโยบายรวม
   ข้ามทั้งสอง batch พร้อมกัน (ไม่ใช่แก้เฉพาะจุดในไฟล์นี้ไฟล์เดียว)

## สรุป

แก้ 1 จุด (คืน "รังแก" ตามคำสั่ง lead) · merge_qc ตก 0 หลังแก้ · ผู้พูดถูกตัวครบ 250/250 · ชื่อ/คำล็อกตรง glossary
และตรงกับ batch_TALK_010 ทั้งหมด · ไม่มีคำใหม่เสนอเพิ่ม glossary · ส่งต่อ lead 2 ประเด็น (typo ใน TALK_010 นอกขอบเขต ·
นโยบายการเรียก "Wang" แบบเดี่ยว ๆ ข้าม batch)
