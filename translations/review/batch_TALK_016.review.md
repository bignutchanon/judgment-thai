# รายงานตรวจ QC — batch_TALK_016

ไฟล์: `translations/done/batch_TALK_016.done.json` (250 คีย์ จาก talk.bin — a01 Twisted Trio/Panty Professor · friend_a40 Moroboshi/ชุมชนคนไร้บ้าน · friend_a23 Haoyu Xiu · friend_a32/a33 Poppo/Alice · friend_a41 ร้านขนม Takemitsu ถูกรีดไถ)

## สรุปผล
- ตรวจผู้พูดครบทั้ง 250 คีย์ด้วย `extracted/facts/talk_speaker.json` (สคริปต์วนเทียบทีเดียว) — **ไม่พบคีย์ไหนขาด/ไม่พบผู้พูด** และผู้พูดที่นักแปลตีความตรงกับตารางผู้พูดทุกจุด (รวมกรณี dupes เช่น "H-Hey!" / "For crying out loud..." / "Thank you very much! Please come again!" / "Sure, why not..." / "Sure. I'm Takayuki Yagami." — คำแปลที่ใช้เป็นกลางพอสำหรับผู้พูดทุกคนในรายการ dupes แล้ว)
- `python scripts/merge_qc.py --dry-run --only TALK_016` → **ผ่าน 250 · ตก 0 · ขาด 0**
- ไม่พบสัญลักษณ์ต้องห้าม (♪ ❤ ♥ ★ ☆ • ※) หลุดเข้าคำแปล (ต้นฉบับมี ♪ ที่ "Kondo-san's done it again! ♪" แต่นักแปลตัดออกจากคำแปลไทยแล้วถูกต้อง)
- แท็ก `<font_kind=yakuza_italic>`, `<t:get_poppo_point>`, `<t:now_poppo_point=friend_032_kizuna_point>` ครบเป๊ะทุกจุด, จำนวน/ตำแหน่งตรงกับ EN
- ช่องว่างท้ายสตริง 2 จุด (บรรทัด poppo point) คงไว้ตรงกับต้นฉบับ
- ยากามิ "ผม" ตลอดทั้ง batch ไม่มีจุดไหนหลุดไป กู/มึง/แก (เจอ "กู" ปนใน "ยากูซ่า" ซึ่งเป็นส่วนหนึ่งของคำ ไม่ใช่สรรพนาม — ไม่นับ)
- คู่อันธพาลรีดไถ (Shakedown Superior/Subordinate) ที่ Takemitsu: ลูกน้องใช้ "ครับ/ผม" เฉพาะตอนพูดกับอานิกิของตัวเอง ("ครับผม... ได้เลยครับ..." / "ไม่ครับ... ไม่เลยครับ...") และใช้ กู/มึง (T3) กับ Takemitsu/Yagami ที่เป็นคนนอก — ไม่พบบรรทัดไหนผสมสองระดับ
- คำล็อก glossary ตรวจแล้ว: The Twisted Trio → สามโรคจิต ✓ · Panty Professor → ศาสตราจารย์กางเกงใน ✓ · Public Park Three → สวนสาธารณะสาม ✓ (ทั้ง 3 จุดที่ปรากฏ)
- ชื่อใหม่ที่ lead รับ (คนโดะ/ฮามานากะ/มุราโอะ/เทราโอกะ/ฟุคุฮาระ/โมโรโบชิ/เฮ่าอวี่ ซิว/ทาเคมิตสึ) สะกดตรงกับที่ lead อนุมัติทุกจุด — honorific ตาม EN ตรงตัว (Moroboshi-sensei → โมโรโบชิเซนเซ, -san → ซัง) ถูกต้องหมด

## จุดที่แก้ (5 จุด — แก้ในไฟล์ done.json แล้ว)

### 1. คำล็อก glossary ไม่ตรง (1 จุด)
- "Children's Park" แปลว่า **"สวนเด็กเล่น"** ผิดจากคำล็อก → แก้เป็น **"สวนเด็ก"** ตาม glossary.md/lead's ruling
  (บรรทัด: "Y-Yeah, he should be underground in the sewers... You can get there through a manhole in the Children's Park...")

### 2. เพศ Kondo ยังใช้ทะเบียนเลี่ยงเพศอยู่ ทั้งที่ lead สั่งให้ใช้ทะเบียนชายเต็มที่ (4 จุด)
lead ยืนยันว่า Kondo = ชาย (หลักฐาน "this homeless guy"/"him") และสั่งให้ **เลิกเลี่ยงเพศ** — แก้ "ฉัน" ที่ Kondo ใช้แทนตัวเองเป็น "ผม" ทั้ง 4 จุด (คำแปลอื่นที่ไม่มีสรรพนามแทนตัวของ Kondo ปล่อยไว้ตามเดิม เพราะไม่ได้ผิดอยู่แล้ว):
  - "'Scuse me... I don't mean to scare ya, but I need help bad..." → "...แต่ผมต้องการความช่วยเหลือด่วนจริงๆ..."
  - "My stomach, it's... killing me all of a sudden... *groan*" → "ท้องผมมัน..."
  - "No, don't do that... I don't have that kinda money..." → "...ผมไม่มีเงินขนาดนั้นหรอก..."
  - "Uhh, let me think... Well, I did some dumpster diving at Pink Street yesterday..." → "...เมื่อวานผมไปคุ้ยถังขยะ..."

หมายเหตุ: Moroboshi ตรวจแล้วใช้ "ผม" ครบทุกจุดอยู่แล้ว (ไม่ต้องแก้) — สอดคล้องกับหลักฐาน "Goro Moroboshi ... he used to be a doctor" ใน friends.json idx 35 และ "takemitsu: male" ใน voicer_gender.json สำหรับ Takemitsu Owner (นักแปลใช้ผม/ครับถูกต้องอยู่แล้ว แม้ lead ไม่ได้พูดถึงตัวนี้ตรงๆ)

## ผู้พูดที่ยังไม่มีหลักฐานเพศ — ตรวจแล้วไม่รั่ว
Hamanaka / Murao / Teraoka / Fukuhara / Xiu ใช้ "ฉัน"/เลี่ยงสรรพนามทั้งหมด ไม่มีคำลงท้ายบอกเพศ (ครับ/ค่ะ) หลุดมาสักจุด — ผ่าน

Alice ตรวจแล้วใช้ "ค่ะ/คะ" ครบทุกจุด สอดคล้องกับหลักฐานเพศหญิงที่มีอยู่แล้ว — ผ่าน

Tsukino ใช้ "ค่ะ/คะ" + "ฉัน" ถูกต้องตามทะเบียนหญิง, Yosuke ใช้ "ผม/ครับ" ถูกต้องตามทะเบียนชาย (ทั้งคู่มีเพศยืนยันแล้วจาก glossary.md §7 อยู่ก่อน ไม่ใช่ปัญหาใหม่ของ batch นี้)

## ปัญหาที่ต้องให้ lead ตัดสิน
ไม่มี — batch นี้ไม่มีจุดคลุมเครือที่ตัดสินเองไม่ได้

## คำที่ควรพิจารณาเพิ่มเข้า glossary/เอกสารอ้างอิง
- **Goro Moroboshi** (ชื่อเต็มของ "Moroboshi-sensei") — พบใน `friends.json` idx 35: "A homeless man who lives in the sewers. Apparently he used to be a doctor at a medical university." (hint หลักฐานเพศเพิ่มเติมนอกเหนือจากที่นักแปลเจอในเนื้อ batch เอง) — เสนอบันทึกไว้ใน `docs/reference/gender_evidence_judge.md`
- **Takemitsu (เจ้าของร้านขนม)** — `voicer_gender.json` มี "takemitsu: male" ตรง + `friends.json` idx 36 มี "he's had nothing but trouble" ยืนยันซ้ำ — เสนอเพิ่มเข้ารายชื่อเพศยืนยันแล้วเช่นกัน แม้ batch นี้นักแปลใช้ทะเบียนชายถูกต้องอยู่แล้วโดยไม่ต้องมีคำสั่ง lead ก็ตาม
- **"Kon-chan"** (ชื่อเล่นของ Kondo) แปลเป็น "คนจัง" (คน+จัง ตามพยางค์ที่ตัดจาก คนโดะ) — สะกดถูกต้องตามกฎ honorific+ชื่อที่ล็อก แต่คำว่า "คน" พ้องเสียงกับ "คน" (บุคคล) ในภาษาไทย อาจทำให้ผู้เล่นงงเล็กน้อยตอนอ่านลอย ๆ — ไม่ใช่ข้อผิดพลาด ปล่อยผ่านตามเดิม แต่แจ้ง lead ไว้เผื่อพิจารณา
