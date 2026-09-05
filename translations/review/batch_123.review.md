# บันทึกการตรวจ QC — batch_123

**ชนิด**: UI/ระบบ ล้วน — controller_guide · dialog_info · effect_*(param เอฟเฟกต์) · gamer_stat · input_action ·
input_game_state · msg_unit · option · pause_complete_profile (250 คีย์)
**ผล `merge_qc.py --dry-run --only 123`**: ผ่าน 250 · คง EN 29 · **ตก 0** (ก่อนแก้: ผ่าน 250 คง EN 29 ตก 0 เหมือนกัน
— lead รัน dry-run ไว้แล้วก่อนส่งตรวจ ตัวเลขไม่เปลี่ยนเพราะจุดที่แก้เป็นการแก้ความหมาย ไม่ใช่โครงสร้าง)

## แก้ไปทั้งหมด 1 จุด

1. **`Drone Shooting` — แปลผิดระบบ (เกือบตรงข้าม)**
   เดิม: `ถ่ายภาพด้วยโดรน` (ถ่ายรูปด้วยโดรน) → แก้เป็น `ยิงด้วยโดรน`
   เหตุผล: ตรวจ `extracted/db_en/en/controller_guide.bin.json` idx 69-70 พบ row name **`drone_vs_a`/`drone_vs_b`**
   (คู่กับ `input_game_state.bin` row **`drone_battle`** profile `Drone_Shooting`) — ปุ่มในโหมดนี้คือ
   `Shoot Bullet` (มีอยู่ใน batch เดียวกัน) ไม่ใช่โหมดถ่ายภาพ · ส่วนโหมดถ่ายภาพจริงคือคนละคีย์ **`Drone Photo`**
   (row name `drone_photo`) ซึ่ง batch นี้แปลถูกอยู่แล้วว่า `ภาพถ่ายโดรน` — นักแปลสลับความหมายสองระบบนี้กัน
   (เอาคำแปลถ่ายภาพไปใส่ระบบยิง) แก้ให้ตรงกับ action จริง (ยิงกระสุน) และคงโครงประโยค "ด้วยโดรน" เดิมไว้
   เพื่อให้จับคู่กับ `Drone Photo` อ่านเป็นชุดเดียวกันในเมนู

## ตรวจ "คง EN" ครบ 29 คีย์ — ยืนยันถูกทุกตัว

ไล่เทียบกับ `effect_body_damage.bin.json` / `effect_body_damage_param.bin.json` / `effect_charge_dust_generator.bin.json`
/ `effect_character_use_effect.bin.json` / `gamer_stat.bin.json` ทีละคีย์:

- **`blood` / `damage`** (นักแปลเขียนทับ ref_tm ที่เคยแปลไทย) — ยืนยันแล้วว่าเป็น **row name / คอลัมน์ `name`** ของ
  `effect_body_damage.bin` และ `effect_body_damage_param.bin` (คู่กับ `damage_face`/`damage_mune`/`damage_body`)
  ค่าในคอลัมน์ `data` เป็น blob เข้ารหัส (base64-ish) ไม่ใช่ข้อความแสดงผล — เป็นพารามิเตอร์เอนจิ้นจริง **นักแปลตัดสินถูก**
- **`smr/soz/skg/shg/sso/shm/sst/smd/skr`** — ยืนยันเป็นค่าคอลัมน์ `ptc_par` (particle effect asset id) ใน
  `effect_character_use_effect.bin.json` ผูกกับ `*character_id`/`aura_event_id` — พารามิเตอร์เอนจิ้นล้วน ถูกต้อง
- **`weak/normal/strong`** — ยืนยันเป็น row name ของ `effect_charge_dust_generator.bin` (คอลัมน์ `name` ซ้ำค่าเดียวกัน)
  คู่กับ blob `data` เข้ารหัส — enum ระดับเอฟเฟกต์ ไม่ใช่ข้อความ UI ถูกต้อง
- **`string`/`int`** — ยืนยันเป็นค่าคอลัมน์ `type` ใน `gamer_stat.bin.json` (`reach_chapter.type="string"`,
  `defeated_enemies.type="int"`) เป็น data type enum จริง ถูกต้อง
- **`<symbol=vf5_key_arrow_n8/n2/n6/n4>`** — แท็กปุ่มทิศทางสำหรับตู้เกม Virtua Fighter 5 ถูกต้องตามกฎ tag คง EN
- **`Out Run`** — เกมอาร์เคด SEGA จริง ตรงกับ §11 ที่ล็อกให้คง EN
- **`±${value}` / `${value}%`** — placeholder ล้วน ไม่มีข้อความให้แปล ถูกต้อง
- **`GPU` / `FPS`** — ตัวย่อสากลที่ใช้ทับศัพท์ EN ทั่วไปในเมนูกราฟิกไทย ถูกต้อง
- **4 คีย์ขยะไบนารี (`-9\`9@k/...` ฯลฯ)** — เป็น garbage/placeholder data ของ `effect_body_damage.bin` (ตรงกับ
  ค่า `data` ใน bin เดียวกับ `blood`) ไม่ใช่ข้อความ ถูกต้องที่คง

**สรุป**: คง EN 29/29 ถูกต้องทั้งหมด ไม่มีคีย์ไหนควรแปลแต่ถูกคง EN ผิด และไม่มีคีย์ไหนที่ควรคง EN แต่ถูกแปลไปแล้ว

## ข้อสรุปเรื่อง `Chase Action / Catch`

**"Catch" ในคีย์นี้คือระบบเดียวกับ "Capture" ที่ glossary ล็อกไว้ (`Capture → จับกุม`) — ยืนยันด้วยไฟล์เกมจริง**:
`input_action.bin` idx 309 row name **`Chase_Action_Maru`** (ปุ่ม ○) มี `name = "Chase Action / Catch"` ส่วน
`controller_guide.bin` idx 36 row name **`chase`** มี `message = "Chase and Capture"` — คนละคีย์แต่ผูกกับระบบ Chase
เดียวกันชัดเจน (แถวเดียวกันมี `Chase_Action_Sankaku/Shikaku/Batsu`, `Chase_Move_Right/Left` ครบชุด และ
`input_game_state.bin` row `chase` name `"Chases"` ก็อยู่ในกลุ่มเดียวกัน) — เป็นแค่คำละคำในไฟล์เกมสำหรับกลไกเดียวกัน
(ไล่ระยะแล้วเข้าจับ) นักแปลแปล `จับกุม` ถูกต้องแล้ว ไม่ต้องแก้ — **ไม่มีจุดให้ lead ตัดสินในข้อนี้** เพราะหลักฐานชัดพอ

## ตระกูลงัดกุญแจ — ตรวจความนิ่งแล้ว ไม่พบปัญหา

`Keys→กุญแจ · Picking→งัดกุญแจ · Thumb Turn Bypass→เลี่ยงกลอนบิด (ตรงกับ §sprint 21 ส.ค. "ป้ายสั้นคู่กับ Lock Picking")
· Choose Key 1-7→เลือกกุญแจ 1-7` ตรงกับ batch_117 ทุกคำ

**หมายเหตุ (ไม่ต้องแก้ แต่แจ้ง lead ไว้)**: `Move Pick Left/Right` (row name `Picking_PickL`/`Picking_PickR` ใน
`input_action.bin` — ยืนยันเป็นระบบงัดกุญแจแน่นอน) แปลว่า `เลื่อนปิ๊กไปทางซ้าย/ขวา` (ทับศัพท์ "ปิ๊ก" = เครื่องมืองัดกุญแจ)
— คำนี้ **ไม่ใช่คีย์เดียวกับ** `"Move Pick (Left/Right)　/"` และ `"Move Pick (Up/Down)"` ที่ ship แล้วใน master_th
(`เลื่อนเลือก (ซ้าย/ขวา)　/` และ `เลื่อนตัวคีบ (ขึ้น/ลง)`) — สองคีย์นั้นมาจาก `ui_text.bin` idx 888-889 ซึ่งผู้ตรวจ
batch_110 ยืนยันแล้วว่าอยู่ในเมนู Settings/Controls ของมินิเกม (ไม่ใช่งัดกุญแจ) จึงเป็นคนละระบบกันจริง ไม่ผิดกฎ
"ต้องแปลตรงกัน" — แต่**คำว่า "Pick" ถูกแปล 3 แบบต่างกันในเกม** (`เลือก` / `ตัวคีบ` / `ปิ๊ก`) คนละระบบ อาจสร้างความสับสน
ให้นักแปล/ผู้ตรวจชุดถัดไปที่เจอคำว่า "Pick" ลอย ๆ — เสนอเพิ่มบรรทัดแยกระบบให้ชัดใน glossary (เช่น "Pick (งัดกุญแจ) → ปิ๊ก
· Pick (เคอร์เซอร์เลือกในมินิเกม) → เลือก/ตัวคีบ แล้วแต่บริบท ห้ามปนกัน")

## `gamer_stat.bin` — ตรวจสถิติจริงครบ 4 คีย์

`Furthest Chapter Played→บทที่เล่นไกลที่สุด · Enemies Defeated→ศัตรูที่กำจัด · No. of KamuroGo Missions→จำนวนภารกิจ
KamuroGo (KamuroGo คง EN ตรงกับ §7/sprint lock) · Chapter ${chapter_number}→บทที่ ${chapter_number}` — ยัง
ไม่มีใน master_th.json (batch นี้เป็นครั้งแรกที่แปล) ไม่มีของเดิมให้ชนกัน ทุกคำสมเหตุสมผลและใช้ศัพท์เดียวกับที่เหลือใน batch

## คีย์ที่ชนหลาย bin — ตรวจแล้วอยู่ในขอบเขต batch เดียวกันทั้งคู่ ไม่มีความเสี่ยง

- `Enemies Defeated` → ชนกับ `pause_complete_profile.bin` (อยู่ใน source_bins ของ batch นี้เอง) ไม่ใช่ batch อื่น
- `Drone Shooting` / `Decorating the Office` → ชนกับ `input_game_state.bin` (อยู่ใน source_bins ของ batch นี้เอง)

## ตรวจแล้วไม่พบปัญหา (งานมาตรฐาน)

- **`Cancel Shot`**: ยืนยัน row `batting` (`controller_guide.bin` idx 4/27 `message="Batting Center"`,
  `input_game_state.bin` idx 5 `name="Batting Center"`) คู่กับ `Swing Bat`/`Begin Shot`/`Insert Money` ในกลุ่ม
  เดียวกัน — เป็นศูนย์ฝึกตีจริง แปล `ยกเลิกการตี` ถูกต้อง (เขียนทับ ref_tm `ยกเลิกการยิง` ถูกแล้ว)
- **`Shift Up`/`Shift Down`**: ตรวจแล้วเป็น row `Phone_Camera_Shift_Up/Down` (มุมกล้องโทรศัพท์) ไม่ใช่การเปลี่ยนเกียร์
  รถ (`Change Gears` เป็นคนละ row `Minigame_GearChange`) — แปล `เลื่อนขึ้น/เลื่อนลง` ถูกบริบทแล้ว
  ไม่ต้องแก้เป็น "เปลี่ยนเกียร์ขึ้น/ลง" ตามที่กังวลตอนแรก
- **โครงสร้างไฟล์**: เทียบคีย์ worklist vs done ด้วยสคริปต์ — ตรงกันครบ 250/250 ไม่ขาดไม่เกิน ไม่มีค่าว่าง
- **placeholder/tag**: `<input_device_not=...>`, `<input_device=...>`, `<symbol=mouse_moveint>`, `<color=striking>`,
  `${platform.term.stick}`, `${value}`, `${chapter_number}`, `\n` ในประโยคยาว (Camera Control ×4, Autosave,
  Drone motion sensor ฯลฯ) ครบทุกจุด ไม่มีหลุด
- **ความยาว**: ประโยคยาวทั้งหมด (คำอธิบาย option ต่าง ๆ) แปลได้กระชับไม่ล้น ไม่มีจุดยาวเกิน EN ผิดปกติ
- **โทน/สรรพนาม**: ทั้ง batch เป็นข้อความ UI/ระบบล้วน ไม่มีบทพูดตัวละคร ไม่มีจุดต้องผูกสรรพนาม/เพศ
- **คำราชาศัพท์**: ไม่พบ
- **อักขระต้องห้าม (❤♥♪★ ฯลฯ)**: สแกนแล้ว ไม่พบ

## จุดที่ให้ lead ตัดสิน

- **เสนอเพิ่ม glossary**: แยกบันทึกคำว่า "Pick" ตามระบบ (งัดกุญแจ = ปิ๊ก / มินิเกมกระดาน-เคอร์เซอร์ = เลือก·ตัวคีบ)
  กันสับสนในชุดถัดไป (รายละเอียดในหัวข้อ "ตระกูลงัดกุญแจ" ด้านบน) — ไม่กระทบ merge ของ batch นี้ เป็นข้อเสนอเชิงป้องกัน
  เท่านั้น

## คำที่ควรล็อกเพิ่มเข้า glossary

- **`Drone Shooting` (โหมดต่อสู้โดรน, row `drone_battle`) → ยิงด้วยโดรน** คู่กับ `Drone Photo` (โหมดถ่ายภาพ,
  row `drone_photo`) → ภาพถ่ายโดรน — สองระบบชื่อคล้ายกันมาก เสี่ยงสลับซ้ำถ้าไม่มีในตาราง
