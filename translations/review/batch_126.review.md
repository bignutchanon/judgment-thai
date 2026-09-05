# รายงานตรวจ QC — batch_126

ผู้ตรวจ: QC agent · แหล่งที่มา: `qsearch_result.bin` · `qsearch_search.bin` · `reward_delivery_box.bin` ·
`reward_judge_clear_achievement.bin` · `rumble.bin` · `save_data_detail.bin` · `scene.bin` ·
`scene_scenario_color_set.bin` · `scene_scenario_explanation.bin` · `talk_system_msg.bin`

## สรุป

- ตรวจทั้ง 250 คู่ (dry-run เดิมจาก lead: ผ่าน 250 · คง EN 15 · ตก 0)
- **แก้ 3 จุด** ทั้งหมดเป็นปัญหา "คำที่ ship แล้วต้องชนะ" (ข้อ 3 ในลำดับตรวจ — คำล็อกไม่ตรงกับที่ ship แล้ว)
- รัน `python scripts/merge_qc.py --dry-run --only 126` ซ้ำหลังแก้ → **ผ่าน 250 · คง EN 15 · ตก 0** (ไม่เปลี่ยนจากเดิม เพราะ merge_qc ตรวจแค่เชิงกล ไม่ตรวจคำแปลผิด)
- รัน `python scripts/check_latin_leftovers.py --only 126` → พบละตินตกค้าง 33 แบบ **ทั้งหมดเป็นของที่ตั้งใจคง EN**: `@handle` ฟีดโซเชียล (ตามบรรทัดฐาน batch_125) · `D&C` (ล็อกคง EN แล้ว) · `Ryu Ga Gotoku Studio` (เครื่องหมายการค้า) · `QR` (ตัวย่อคง EN) — ไม่มีจุดไหนต้องแก้เพิ่ม

## จุดที่แก้ (หมวด 3 — คำล็อกไม่ตรง glossary/ของที่ ship แล้ว)

1. **`Bright Barista Kaede @hana_kaede`** — เดิมแปลชื่อ "Kaede" เป็น **"เคเอเดะ"** ผิดหลักทับศัพท์ และขัดกับที่ ship แล้วจริงใน `master_th.json` สองจุด (บรรทัด 21809 `Kaede Sanada`→คาเอเดะ ซานาดะ, บรรทัด 26573 `Kaede`→คาเอเดะ) → แก้เป็น **"บาริสต้าสดใส คาเอเดะ @hana_kaede"**

2. **`"Cipher Secrets: Mind over Matter" Project Achievement Bonus:\n<color=striking>Mind Over Matter`** — เดิมแปลว่า `โบนัสความสำเร็จโปรเจกต์ "Cipher Secrets: จิตเป็นใหญ่กว่ากาย":...` ซึ่งขัดกับที่ ship แล้วจริงสองจุด: (ก) คงคำว่า "Cipher Secrets" เป็น EN ทั้งที่ ship แล้วเป็น **"ปริศนารหัสลับ"** (`master_th.json:30351`) (ข) "Mind over Matter" แปลใหม่เป็น "จิตเป็นใหญ่กว่ากาย" ทั้งที่ ship แล้วเป็น **"จิตเหนือกาย"** → แก้เป็น `โบนัสความสำเร็จโปรเจกต์ "ปริศนารหัสลับ: จิตเหนือกาย":\n<color=striking>จิตเหนือกาย` (คงโครงสร้างไม่มี `</color>` ปิดตามต้นฉบับ EN ที่ตัดทิ้งไว้เหมือนกัน)

3. **`"Cipher Secrets: Brains over Brawn" Project Achievement Bonus:\n<color=striking>Brains Over Brawn`** — ปัญหาเดียวกัน: เดิมคง "Cipher Secrets" เป็น EN + แปล "Brains over Brawn" เป็น "สมองเหนือพลัง" ทั้งที่ ship แล้วเป็น **"ปริศนารหัสลับ: ปัญญาเหนือพลัง"** (`master_th.json:30354`) → แก้เป็น `โบนัสความสำเร็จโปรเจกต์ "ปริศนารหัสลับ: ปัญญาเหนือพลัง":\n<color=striking>ปัญญาเหนือพลัง`

(ตรวจไขว้กับ `master_th.json` แล้วว่าคำอื่นในกลุ่มเดียวกันของ batch — Premier Darts / Miracle Darts / Artisanal Shogi Set / Unofficial-Unabridged-Ultimate D&C Strategy Guide / Hyper Propeller Q / Super Motor S / Low-Cost ESC / Low-Cost Turbo / Kamurocho Serial Killing / Kyorei Clan Serial Killing / Matsugane Family Robbery / Wild Jackson — **ตรงกับที่ ship แล้วทุกจุด** ไม่ต้องแก้เพิ่ม)

## ข้อสรุปเรื่องป้ายเซฟ 5 ภาษา (`save_data_detail.bin`)

**นักแปลทำถูกต้องแล้ว — ไม่ต้องแก้อะไร** ตรวจโครงตารางจริงใน `extracted/db_en/en/save_data_detail.bin.json` พบว่า:

- แต่ละแถว (เช่น `id_difficulty`, `id_play_time`, `id_completion_shop`) มีคอลัมน์ `text_for_ja/en/fr/es/de/it` เก็บข้อความ **ตามค่าตรง ๆ** ไม่ใช่โครงสร้างที่ parse โดยตำแหน่ง — pipeline ของทีมแปลเป็น flat string map (EN value → TH value) ไม่ผูกกับคอลัมน์ ดังนั้นแปลทุกภาษาให้เป็นข้อความไทยเดียวกันจะไม่ทำให้อะไรพัง
- **ยืนยันด้วยว่าข้อมูลต้นฉบับเองก็สลับคอลัมน์ภาษาไม่ตรง** — `text_for_fr` ของ `id_difficulty`/`id_play_time`/`id_chapter` ดันเป็นข้อความ**เยอรมัน** (เช่น `"Schwierigkeitsgrad:"`) ส่วน `text_for_de` ดันเป็นข้อความ**ฝรั่งเศส** (เช่น `"Chapitre :"`) — ยืนยันว่าห้ามเชื่อชื่อคอลัมน์ตรง ๆ แม้แต่ในไฟล์เกมเอง แปลตามค่า (value) ที่เจอจริงคือทางเดียวที่ปลอดภัย
- สรุป: การแปลทุกภาษาให้ออกมาเป็นไทยข้อความเดียวกัน (เช่น `[Total Play Time]`/`Gesamte Spielzeit:`/`Tiempo total de juego:`/`Temps de jeu total :`/`Tempo di gioco totale:` → "เวลาเล่นทั้งหมด") **ปลอดภัยและถูกต้อง** เพราะป้ายพวกนี้เป็นแค่ label แสดงผลตอนอ่านเซฟข้ามภูมิภาค ไม่ใช่ key ที่ตรรกะเกมใช้ parse — แนะนำ lead จดไว้เป็นบรรทัดฐานถาวรใน glossary §10 (ยังไม่มีบันทึกชัดเจนเรื่องนี้)

**เช็ค `[Completion Shop]`/`[Completion Mission]` ตามที่ขอ**: เทียบกับคอลัมน์ `text_for_en` จริงในไฟล์ — `id_completion_shop.text_for_en = "Shop Missions:"` และ `id_completion_mission.text_for_en = "City Missions:"` → คำแปล **"ภารกิจร้านค้า"** และ **"ภารกิจในเมือง"** ที่นักแปลเดาจากฝรั่งเศส/สเปน **ถูกต้องตรงกับความหมายจริง 100%**

## ผลตรวจฟีดโซเชียล (`qsearch_result.bin`/`qsearch_search.bin`)

ตรวจครบทุกโพสต์ (Wild Jackson feed 25 โพสต์ + timestamp) — ทำตามบรรทัดฐาน batch_125 ถูกต้อง:
- display name แปลไทย + คง `@handle` ละตินทุกจุด (ไม่มีจุดไหนแปล handle)
- เวลาแบบ "4h ago" → "4 ชม.ที่แล้ว" / "1d ago" → "1 วันที่แล้ว" ถูกต้องครบทุกจุด
- ชื่อมุก (`Cheapsk8er`→"จอมประหยัด" ตรงบรรทัดฐาน, `El Genio Muy Sabio`→"เจ้าอัจฉริยะสุดปราดเปรื่อง", `Drinks Like a Fish`→"นักดื่มตัวยง", `Not Natane`→"ไม่ใช่นาทาเนะ" ฯลฯ) แปลความหมายไว้ครบ มุกไม่หายและไม่ยาวเกินไป
- จุดเดียวที่ต้องแก้ในกลุ่มนี้คือชื่อ "Kaede" (ดูหัวข้อจุดที่แก้ข้อ 1)
- คำว่า "tastes like ass" แปลเป็น "รสชาติแย่/รสชาติแย่มาก" ทุกจุด (6 ที่) — เป็นการลดความหยาบลงเล็กน้อยแต่คงความหมายและโทนขำขันไว้ครบ ภาษาไทยไม่มีสำนวนอวัยวะเทียบเท่าที่เป็นธรรมชาติสำหรับบริบทนี้ ตัดสินใจว่า**ไม่ต้องแก้** (ไม่ผิดความหมาย ไม่ใช่คำล็อก)

## เพศ/สรรพนาม/คำล็อกอื่น — ผ่านหมด

- `Hayama-san` → ยืนยันชายถูกต้องจากข้อความ "He wants me to pretend..." ตรงตามที่นักแปลสรุป
- `Fumie Taniyama` → "ฟุมิเอะ ทานิยามะ" ตรงกฎทับศัพท์ทุกประการ
- ยากามิใช้ "ผม" ตลอดทุกบรรทัดคำร้อง/เนื้อเรื่องคดี ไม่มีหลุด T2/T3
- ชื่อคดี (Kamurocho/Kyorei Clan Serial Killing, Matsugane Family Robbery, X Murder ทั้ง 5 คดี) ตรงคำล็อกทุกตัว + ตรงกับที่ ship แล้วใน master_th (2 คดีที่มี precedent ตรงเป๊ะ)
- คง EN 15 คีย์ (`linear`/`LightBar`/`none`/`BigMotor`/`SmallMotor`/`ADV`/`BTL`/`SCN`/`PRE`/`BTLsubs`/`ADVsubs`/`debug`/`padv`/`ADVcln`/`BTLcln`) ยืนยันแล้วว่าเป็น enum ทางเทคนิคจริง (rumble motor type + scene type flag) ไม่ใช่คำที่ควรแปล — ถูกต้องตามที่ lead ทำเครื่องหมายไว้
- tag/`\n`/`<color>`/`<font_kind>` ครบทุกจุด รวมจุดที่ต้นฉบับ EN เองไม่มี `</color>` ปิด (2 จุดในกลุ่ม Cipher Secrets) — คงโครงสร้างเดิมตามต้นฉบับไม่เติมปิดเอง

## คำที่ควรเพิ่มเข้า glossary (เสนอ lead)

- `Kaede` → คาเอเดะ (ship แล้ว 2 จุดใน master_th แต่ยังไม่มีในตาราง §7/§📇 — ใส่ไว้กันซ้ำ)
- `Cipher Secrets` → ปริศนารหัสลับ · `Mind over Matter` → จิตเหนือกาย · `Brains over Brawn` → ปัญญาเหนือพลัง (ship แล้วทั้งหมดจาก batch_124 แต่ไม่มีในตาราง — เป็นสาเหตุตรงที่ batch_126 พลาด 2 จุดนี้)
- เสนอบันทึกกฎ "ป้ายเซฟ 5 ภาษาใน `save_data_detail.bin` แปลรวมเป็นไทยข้อความเดียวกันได้ปลอดภัย + คอลัมน์ fr/de ในไฟล์เกมสลับกันจริง" ไว้ใน §10 เป็นบรรทัดฐานถาวร กันผู้ตรวจ/นักแปล batch อื่นที่เจอ `save_data_detail.bin` อีกต้องมานั่ง verify ซ้ำ

## จุดที่ไม่แน่ใจ / อยากให้ lead ตัดสิน

ไม่มี — ทุกจุดตรวจสอบได้ข้อสรุปชัดเจนจากไฟล์เกมจริง (`extracted/db_en/en/save_data_detail.bin.json`) หรือจาก `master_th.json` ที่ ship แล้ว ไม่มีข้อขัดแย้งที่ต้องรอการตัดสินใจเพิ่ม

## บรรทัดสรุป dry-run (หลังแก้)

```
batch_126.done.json              ผ่าน  250  ตก   0  ขาด   0
รวม: ผ่าน 250 · คง EN 15 · ตก 0
```
