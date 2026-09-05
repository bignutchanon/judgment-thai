# Review — batch_TALK_002 (250 strings, talk.bin — บุก KJ Art / คดีคุเมะ / Chatter tutorial / คาสิโน / Paradise VR)

ผู้ตรวจ: QC · วันที่ 21 ส.ค. 2026
ผล `merge_qc.py --dry-run --only TALK_002`: **ผ่าน 250 · ตก 0 · ขาด 0**
ผล `check_latin_leftovers.py --only TALK_002`: **พบคำละตินตกค้าง 0 แบบ**

ไฟล์นี้ผ่านมือแก้มาแล้วสองรอบ (นักแปล → lead สั่งแก้ชื่อปุ่มคาสิโน → นักแปลแก้ 21 คีย์) —
รอบนี้ไล่ตรวจทั่วทั้ง 250 คีย์อีกครั้ง พบและแก้เพิ่มอีก **21 จุด**

## สรุปตามหมวด (อิงหัวข้อ REVIEWER_BRIEF ข้อ 1-8)

### (3) คำล็อกไม่ตรง glossary — 2 จุด
อาวุธในคดีคุเมะ (`ice pick`) ล็อกไว้ใน glossary.md §11 บรรทัด 354 ว่า **"เหล็กเจาะน้ำแข็ง"**
(ระบุชัดว่า "อาวุธในคดีคุเมะ" ตรงกับ batch นี้เป๊ะ) แต่พบคำแปลสองจุดใช้คนละคำกัน ไม่ตรงคำล็อก
และไม่ตรงกันเองด้วย (ผิดซ้อนทั้งข้อ 3 และข้อ 8):

| Key (ย่อ) | เดิม | แก้เป็น |
|---|---|---|
| `(The cause of death was severe brain trauma...like an ice pick.)` | เหล็ก**แหลม**ทุบน้ำแข็ง | **เหล็กเจาะน้ำแข็ง** |
| `The cops think the murderer used something like an ice pick...` | เหล็กทุบน้ำแข็ง | **เหล็กเจาะน้ำแข็ง** |

### (2)+(8) สรรพนาม/คำลงท้ายผิดคน — ดีลเลอร์คาสิโนสลับเพศกลางฉาก — 7 จุด
ดีลเลอร์แบล็กแจ็ก/โป๊กเกอร์/โฮลเด็มทั้งชุดในไฟล์นี้ (~40 บรรทัด) ยืนยันเป็น **หญิง** ชัดเจน — ใช้ "ดิฉัน"
ตรงตัว 2 จุด ("ดิฉันจะตั้งอัตราจ่ายสามเท่าให้ค่ะ") และใช้ ค่ะ/คะ เกือบทุกบรรทัด แต่พบ 7 บรรทัดหลุดเป็น
"ครับ" (จั่วไพ่เพื่อนบ้านเดียวกันเป็น ค่ะ) ทำให้ดีลเลอร์คนเดียวฟังดูสลับเพศกลางฉาก — แก้ให้ตรงกับ
ทะเบียนที่ยืนยันแล้วทั้งหมด: `You are on quite a roll, sir.` · `You are doing great, sir.` ·
`Selecting "Hit" will draw a card.` · `Try taking insurance this round.` ·
`However, you still only have one pair.` · `You have two fives: one pair.` ·
`You have a full house. Select Raise and try your luck.` (ครับ → ค่ะ/คะ ทั้ง 7 จุด)

### (2) เพศไม่ชัด = ห้ามเดา — พนักงาน Paradise VR/Dice & Cube ใส่ "ครับ" ทั้งที่ไม่มีหลักฐาน — 10 จุด
ตรวจแล้ว: ไม่มี voice line ผูกกับ NPC นี้เลย (`Welcome to Paradise VR!` ไม่พบใน `sound_auth.bin.json`
เท่ากับเป็นข้อความไม่มีเสียงพากย์) และไม่พบชื่อ/เพศใน `voicer_gender.json`, `speech_speaker_map.json`,
`speaker_by_subtable.json`, `places.json`, `docs/side_content_context_judge.md` เลยสักจุด — **ไม่มีหลักฐานเพศใด ๆ**
นักแปลรอบก่อนใส่ "ครับ" ทุกบรรทัดของ NPC นี้โดยไม่มีที่มา ผิดกฎ §0.1 ("เพศไม่ชัด = ห้ามเดา") — ตัด "ครับ"
ออกทั้งหมด (ไม่ใส่ ค่ะ แทนด้วยเพราะไม่มีหลักฐานเพศหญิงเช่นกัน) 9 จุด: `Welcome to Paradise VR!` ·
`Sir, do you have Play Passes?...` · `Oh, a free trial Play Pass!...` · `Have you played Dice & Cube before?` ·
`I'll guide you through the Short Course today.` · `Customers who do well on the Short Course...` ·
`The condition is to clear the stage...` · `That's all there is to it. Now please put on these VR goggles...` ·
`And you're all set! Enjoy your trip to virtual Kamurocho!`
— บวก `Thank you for your patronage!` (บรรทัดของ NPC แจกของรางวัลชุดเดียวกัน "Silver Plate/Copper Plate"
ที่ยืนยันจาก `items.json` id `judge_sugoroku_item_saragin` ว่าเป็นไอเทมในระบบ Dice & Cube เช่นกัน — ไม่มี
หลักฐานเพศเหมือนกัน) รวม **10 จุด**
⚠ บรรทัด `No, this is my first time.` = คำตอบของยากามิเอง (ชายยืนยันแล้ว) **ไม่แตะ** ยังคง "ครับ" ไว้ตามเดิม

### ช่องว่างตกค้างจาก ref_tm (bug ที่รู้จักแล้ว — glossary.md บรรทัด 462) — 2 จุด
`You made the right call buying insurance, sir. Well done.` (...ตัดสินใจ**ที่ ถูกต้อง**ค่ะ → ที่ถูกต้องค่ะ)
และ `As the dealer has a possible blackjack...` (...เป็น**จำนวน ครึ่งหนึ่ง**ของ... → จำนวนครึ่งหนึ่งของ...)
— ทั้งคู่เป็นคำที่ copy จาก ref_tm ตรง ๆ โดยไม่ได้ลบช่องว่างแทรกผิดตำแหน่งตามที่ glossary เตือนไว้แล้ว

## ผลตรวจผู้พูด 3 กลุ่มที่นักแปลพิสูจน์ไม่ได้ (ตามที่ lead สั่งให้ตรวจซ้ำ)

**(ก) บทสอน Chatter search** (`This is the search screen.` ... `He might be able to tell you where Aragaki went.`)
— ยืนยันจาก `docs/story_context_judge.part1.md` บรรทัด 190/194: **ซุกิอุระปรากฏตัวครั้งแรกบทที่ 4 ที่ KJ Art**
เท่านั้น จึงเป็นไปไม่ได้ที่จะเป็นผู้สอนในบทที่ 1 ตามที่นักแปลเคยเดา — ค้นใน `speech_speaker_map.json` /
`speaker_by_subtable.json` ไม่พบ speaker ผูกกับข้อความชุดนี้เลย (ไม่มี `speaker_exact` ให้) — **คำแปลปัจจุบัน
เลี่ยงสรรพนาม/คำลงท้ายทั้งชุดอยู่แล้ว ไม่ตัดสินว่าเป็นใคร** จึงไม่ผิด แต่ไม่ควรบันทึกว่า "น่าจะไคโตะ" ต่อไปโดยไม่มีหลักฐาน — ปล่อยผ่าน

**(ข) บททบทวนคดีคุเมะ** (`Victim was a Kansai thug...` ถึง `Priority number one is proving his alibi...`)
— ค้นใน `speech_speaker_map.json` (คีย์ `speech_list_judge_main_c01`) ไม่มีฟิลด์ `speaker_exact` ให้ (ไม่ผูกชื่อ
ผู้พูดในข้อมูลที่มี) — คำแปลปัจจุบันเลี่ยงสรรพนามทั้งหมดอยู่แล้ว (ไม่มี "ผม/ฉัน/กู" ปนในชุดนี้เลย) ปลอดภัยไม่ว่าจะ
เป็นยากามิหรือไคโตะพูด — ปล่อยผ่าน แต่ **แจ้ง lead**: ถ้าอยากยืนยันตัวจริงต้องไล่ id จาก `sound_auth.bin.json`
เทียบ `speaker_by_subtable.json` โดยตรง (งบ token รอบนี้ไม่พอจะไล่ทุกบรรทัด)

**(ค) พนักงาน Paradise VR / Dice & Cube** — แก้แล้วตามหัวข้อด้านบน (10 จุด) ยืนยันไม่มีหลักฐานเพศจริง ๆ

## ชื่อปุ่มคาสิโน — ตรวจครบทุกจุดที่อ้างถึงปุ่มแล้ว: **ตรงคำล็อกทั้งหมด ไม่มีจุดตกค้าง**

ยึดตามบล็อก "คำตัดสิน lead รอบ sprint 21 ส.ค. 2026" (glossary.md บรรทัด 538 — ปุ่มคาสิโนต้องตรงกับ
ปุ่มบนจอ) ซึ่งเป็นคำตัดสินล่าสุดที่ทับ §13/บรรทัด 520 เดิม (`Double Down`→เพิ่มเดิมพันเท่าตัว, `Surrender`→ยอมแพ้
เป็นข้อเสนอเก่าที่ถูกแทนที่แล้ว): Hit→ตี · Stand→อยู่ · Fold→โฟลด์ · Call→คอล · Raise→เรส · Bet→เดิมพัน ·
Re-Bet→เดิมพันซ้ำ · Double Down→เพิ่มเดิมพันเท่าตัว · Split→แยกไพ่ · Surrender→ยอมแพ้ · Total→รวม ·
Check→เช็ก · Play Pass→เพลย์พาส — ไล่ทุกจุดที่อ้างถึงปุ่มในไฟล์นี้แล้ว **ตรงหมดทุกจุด ไม่มีคำอังกฤษหลุดหรือคำอื่นปน**
`Fold` ที่อธิบายว่า "(ถอนตัว)"/"(quit)" ในสองบริบท (ตอนอธิบายกติกา vs ตอนเป็นตัวเลือกใน sentence เดียวกับ
Raise/Call) อ่านแล้วไม่ชนกับ `Surrender`→"ยอมแพ้" เพราะเป็นคนละคำ ไม่มีจุดที่อ่านสับสน — ปล่อยผ่าน

## จุดที่ตรวจแล้วถูกต้อง (ตัวอย่างสำคัญ)

- ฉากบุก KJ Art (บทที่ 1) — ทุกความคิดในใจยากามิที่มีสรรพนามชัดใช้ "ผม" ครบ (T1 ล็อก) ไม่มี "ฉัน/กู" หลุด
  เทียบกับ `story_context_judge.part1.md` บทที่ 1 แล้วเนื้อเรื่องตรง (บุก KJ Art ช่วยน้องสาว Seiya ระหว่าง
  ไคโตะดึงความสนใจ, ตามหาห้องมุราเสะ — ตรงกับสรุป "ตระกูลเคียวเรอิลักพาตัวน้องสาว Seiya ที่ KJ Art")
- `Aragaki` → "อารากากิ" ตรงกับ `master_th.json` บรรทัด 31792 ที่ ship แล้ว (g กลางคำ = ก ตามกฎทีม) — ไม่ใช่
  ชื่อใหม่ที่ต้องตั้งเอง มี precedent อยู่แล้ว
- `Toshiro Kume` → "โทชิโร คุเมะ", `Tojo Clan` → "ตระกูลโทโจ", `Kyorei Clan` → "ตระกูลเคียวเรอิ",
  `alibi` → "พยานที่อยู่" — ตรงคำล็อกทุกจุด
- `<font_kind=yakuza_italic>...</font_kind>` (2 จุด), `<symbol=button_decide>` (2 จุด) — tag ครบ ตำแหน่งตรง
- `\n` ทุกคีย์ที่มีหลายบรรทัด (รวมกรณีพิเศษ `"A sugoroku message test. \nA sugoroku message test."` ที่มี
  trailing space ก่อน `\n` ในต้นฉบับ) — จำนวนและตำแหน่งตรงกับ EN ทุกจุด
- `Dice & Cube`, `Paradise VR`, `Chatter`, `KJ Art` — คง EN ถูกต้องครบ ไม่มีจุดที่ควรแปลแต่คง หรือคง EN
  ทั้งที่ควรแปล
- `Play Pass` → "เพลย์พาส" ทุกจุด (รูปเดียว ตรงคำล็อกล่าสุดที่ยกเลิก 3 รูปเก่า)

## คำที่ควรเพิ่มเข้า glossary

- ไม่มีคำใหม่ที่ยังไม่ล็อก — batch นี้เป็นเนื้อหาระบบ (คาสิโน/Paradise VR) + ฉากที่ใช้ศัพท์ล็อกอยู่แล้วทั้งหมด

## จุดที่อยากให้ lead ตัดสิน/ทราบ

1. `glossary.md` มีคำล็อก `Double Down`/`Surrender` ปนกันสองรูปในบล็อกเดียวกัน (บรรทัด 520 กับ 538) —
   ยึดบรรทัด 538 (ปุ่มคาสิโน sprint ล่าสุด) เป็นหลักเพราะใหม่กว่าและตรงกับที่ brief ระบุว่า "เพิ่งล็อกวันนี้"
   — เสนอให้ lead ลบ/แก้บรรทัด 520 ให้ตรงกันเพื่อไม่ให้นักแปล batch อื่นสับสนสองคำล็อกที่ขัดกันเอง
2. ผู้พูดกลุ่ม (ข) "บททบทวนคดีคุเมะ" ยังไม่มีหลักฐาน speaker ยืนยันในข้อมูลที่มี (ปลอดภัยเพราะคำแปล
   เลี่ยงสรรพนามอยู่แล้ว แต่ถ้าต้องการยืนยันจริงต้องไล่ id `sound_auth.bin.json` เทียบ `speaker_by_subtable.json`
   เพิ่มเติมนอกงบ token รอบนี้)
