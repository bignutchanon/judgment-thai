# ตรวจ batch_TALK_032 — side_a14 (Iseya/Rei ต่อเนื่องจาก TALK_031) + side_a42 (โคอิไบรด์/ซูชิกิน) + side_a46

**ผล**: `merge_qc.py --dry-run --only TALK_032` ตก 0 (ทั้งก่อนและหลังแก้) · แก้จริง **1 จุด**

## วิธีตรวจ

1. ครอส 250 คีย์ทั้งหมดกับ `extracted/facts/talk_speaker.json` — จับคู่ได้ 100% (250/250, missing 0)
2. เทียบเพศ/ทะเบียนของทุกผู้พูดที่ `gender: "unknown"` กับหลักฐานจริง (voicer_gender.json, gender_evidence.json, honorific/สรรพนามใน EN, ป้ายชื่อบอกเพศในตัวเอง)
3. เทียบ Rei / Iseya / Young Janitor กับทะเบียนที่ใช้จริงใน `batch_TALK_031.done.json` (คดี A14 ต่อเนื่องกัน — ความเสี่ยงหลักที่ lead เตือนไว้)
4. รัน `check_latin_leftovers.py`, `fix_honorific_san.py` — ผ่านทั้งคู่ (0 ปัญหา)
5. สแกนสัญลักษณ์ต้องห้าม (♪❤♥★☆•※) — ไม่พบ

## แก้ไข 1 จุด — สรรพนามบอกเพศทั้งที่ยังพิสูจน์ไม่ได้ (กฎ §0.1 PRONOUN_MATRIX)

**"Sushi Zanmai Employee"** ไม่มีหลักฐานเพศเลย (ไม่มีใน `voicer_gender.json`/`gender_evidence.json`, ไม่มี he/she หรือ sir/ma'am ชี้ตัวในบทนี้) — ต้องแปลกลางเพศ แต่พบ 1 บรรทัดหลุด:

- `"Sure. How can I help?"` : `"ได้ครับ มีอะไรให้ช่วยไหม"` → แก้เป็น `"ได้ มีอะไรให้ช่วยไหม"` (ตัด "ครับ" ทิ้ง)

บรรทัดอื่นของผู้พูดคนนี้ ("Huh? Seriously?" / "Nope, can't say that I have...") กลางเพศอยู่แล้ว ไม่ต้องแก้

## ตรวจแล้วผ่าน (ไม่แก้) — พร้อมเหตุผล

- **Young Chef** (ไม่มีหลักฐานเพศเช่นกัน) — ทั้งสองบรรทัดกลางเพศอยู่แล้ว ไม่มีปัญหา
- **Fukutsu** (เจ้าของ/พนักงานร้านรับจำนำ) — `gender_evidence.json` บอก `unknown, confidence: low, evidence: []` แต่บทนี้มียากามิเรียก **"sir"** ตรงตัวก่อนหน้าบททั้งหมดของฟุคุสึ ("Excuse me, sir. Have you bought any diamond rings...") ซึ่งเป็นหลักฐานเพศชนิดที่ 2 ตาม PRONOUN_MATRIX §0.1 (`sir/ma'am` ชี้ตัวตรง ๆ) — นักแปลใช้ "ผม/ครับ" ทั้งชุดถูกต้องตามหลักฐานนี้ **แนะนำให้ lead อัปเดต `gender_evidence.json` เพิ่มหลักฐานนี้เข้าไป** (ตอนสร้างไฟล์คงยังไม่เห็นบทนี้)
- **Koi Bride Owner** / **Sushi Gin Owner** — ตาราง `talk_speaker.json` ขึ้น unknown แต่ `voicer_gender.json` ยืนยัน `koinyoubou_master: male` และ `sushigincrew: male` (ชื่อ voicer ไม่ตรงกับชื่อ speaker ในตาราง talk_speaker เลยไม่จับคู่อัตโนมัติ) — นักแปลใช้ "ผม/ครับ" ถูกต้องทั้งสองตัว
- **Wakahara** — unknown ในตาราง แต่มี "he/him/guy" จากปาก Sushi Gin Owner ชี้ตัวชัดหลายจุด (ชายแน่นอน) — นักแปลใช้ "ฉัน" ล้วน (ไม่ใช้ ผม/ครับ เลย) ซึ่งไม่รั่วเพศแต่ก็ไม่ขัดหลักฐาน ถือว่าปลอดภัย ไม่ต้องแก้ (T2/T3 ของอาชญากรที่กำลังหนี)
- **Rei / Iseya / Young Janitor** — เทียบกับ `batch_TALK_031.done.json` แล้วตรงกัน: Iseya ใช้ "ผม" ทุกจุด, Young Janitor ไม่มีจุดอ้างถึงตัวเองในบทนี้ (ไม่ขัดกับที่เคยใช้ "ผม" ใน TALK_031), Rei มี 2 บรรทัดกลางเพศ ("H-How dare you!" / "Wh-What are you going to do?") แต่ไม่ใช่ข้อผิด — ใน TALK_031 เองก็มีบรรทัดสั้น ๆ ที่ Rei ไม่ใช้ ค่ะ เหมือนกัน (เช่น "Ah..." → "อ๊ะ...") เป็นรูปแบบธรรมชาติของคำอุทานสั้น ไม่ใช่การขัดทะเบียน
- **Pretty Woman** (หญิงจากชื่อ) / **Military Man** (ชายจากชื่อ) — บท a46 สั้น ทั้งคู่ใช้สรรพนามสอดคล้องกับเพศที่ชื่อบอกไว้ ("ผม" ของ Military Man, ไม่มีจุดขัดของ Pretty Woman)
- **ยากามิ** — "ผม" ทุกบรรทัด ไม่มี T2/T3 หลุดเลยทั้ง 250 คีย์ (รวมฉากที่ Wakahara/Iseya พูดห้าวใส่)
- **เก็นดะเซนเซ** — คำเรียกคงที่ "เก็นดะเซนเซ" ทุกจุด ตรงคำล็อก ไม่มี honorific อื่นหลุดเข้ามา
- **ทาเอโกะ นากาฮาระ** — ชื่อ+honorific ตรง glossary ทุกจุด ("ทาเอโกะ นากาฮาระ", "ยากามิซัง"), ใช้ "ดิฉัน"+ค่ะ ตลอด (T1 ทางการ ตาม EN "She/her/Ma'am" ชัดเจน) ไม่มีจุดหลุด
- **"arai" → "อาราอิ"** ตรงคำตัดสิน lead
- ชื่อสถานที่/องค์กร: โคอิไบรด์, บริษัทการค้าอิเซทานิ, โวลเคโน — ตรง glossary/สม่ำเสมอกับ TALK_031 ทุกจุด ("ซูชิกิน"/"ซูชิซันไม"/"โรงจำนำเอบิสุ" ไม่ถูกเอ่ยชื่อเฉพาะในบทสนทนาจริงของ batch นี้ มีแค่ป้ายผู้พูด จึงไม่มีจุดให้ตรวจคำนาม)
- แท็ก `<font_kind=yakuza_italic>...</font_kind>` (2 จุด, คำว่า "was") — แปลข้อความในแท็กแล้วทั้งคู่ ("เป็น") ไม่มี `<color=...>` ในไฟล์นี้
- honorific: `fix_honorific_san.py` ไม่ฟ้องจุดใดใน batch นี้ — Yagami-san/Genda-sensei/Wakahara-san/Miyamoto-san ทับศัพท์ครบ, "Ma'am" (ไม่ใช่ honorific ญี่ปุ่น) แปลเป็น "คุณ" เหมาะสม ไม่เติม honorific ที่ EN ไม่มี
- ช่องว่างไทย-ละติน / สัญลักษณ์ต้องห้าม / คำละตินตกค้าง — `check_latin_leftovers.py` และสแกนสัญลักษณ์ ผ่านหมด (0)

## เรื่องที่อยากให้ lead ตัดสิน / บันทึกเพิ่ม

1. **"dupes" ของ talk_speaker.json ในบทนี้มีแค่ 3 คีย์** (`You do?`, `C-Crap!`, `(Oh look, a cat.)`) ไม่ใช่ 12 คีย์ตามที่นักแปลรายงานไว้ในบันทึกงาน — ตรวจแล้วทั้ง 3 คีย์ dupes ชี้ไปตารางอื่นที่ไม่เกี่ยวกับฉากนี้เลย (`judge_friend_g02/g04`, `judge_side_a32`, `judge_3Dverification_cat`) ผู้พูดตัวบนสุด (Sushi Gin Owner / Wakahara / Yagami) ถูกต้องตามบริบท a42 อยู่แล้ว ไม่มีจุดไหนต้องแก้จาก dupes — เข้าใจว่านักแปลอาจนับจากเครื่องมือ/ขั้นตอนอื่น (เช่น multibin_keys) ไม่ใช่ field `dupes` นี้โดยตรง ไม่กระทบคุณภาพงานที่ส่งมา
2. **เสนอเพิ่มหลักฐานเข้า `gender_evidence.json`**: `friend_fukutsu` (Ebisu Pawn Shop) ควรอัปเดตจาก `unknown/low/[]` เป็นมีหลักฐาน `sir` address จาก batch นี้ (คีย์ `"Excuse me, sir. Have you bought any diamond rings from a man who looks like this sketch?"`) — ยกระดับ confidence ได้ ไม่ต้องรอ patch ด่วนแต่ฝากไว้ให้ทีมข้อมูลอัปเดตไฟล์กลาง
3. **เสนอเพิ่ม `voicer_gender.json` mapping**: `koinyoubou_master` (โคอิไบรด์) และ `sushigincrew` (ซูชิกิน) เป็น male ยืนยันอยู่แล้วในตารางนี้ แต่ `talk_speaker.json` ("Koi Bride Owner"/"Sushi Gin Owner") จับคู่ชื่อไม่ตรงเลยขึ้น unknown — ถ้าทีมเครื่องมือเพิ่ม alias mapping จะช่วยผู้ตรวจ batch หลัง ๆ ในคดีเดียวกันไม่ต้องไล่มือ

## คำที่ควรพิจารณาเพิ่มเข้า glossary

- ไม่มีคำใหม่ที่ต้องล็อกเพิ่มจาก batch นี้ — ชื่อทั้งหมดตรงกับที่ล็อกไว้แล้ว (โคอิไบรด์, บริษัทการค้าอิเซทานิ, โวลเคโน, เก็นดะเซนเซ, ทาเอโกะ นากาฮาระ, อาราอิ→อาราอิ)
