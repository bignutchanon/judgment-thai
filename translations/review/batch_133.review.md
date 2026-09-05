# QC Review — batch_133 (verification_survey / verification_survey_3d / verification_todo_item / verification_verification / trophy.bin / character_npc_soldier_name_group.bin)

**ผลตรวจ**: แก้ 2 จุด · dry-run สุดท้าย = ผ่าน 239 · คง EN 14 · ตก 0

## จุดที่แก้

1. **`Security Camera for Hyper Win Game`** / **`Security Camera for Bar Ozakeyo`** — นักแปลคง EN
   ไว้ทั้งคำ ("กล้องวงจรปิดของเกม Hyper Win" / "กล้องวงจรปิดของบาร์ Ozakeyo") ตรวจแล้วทั้งสองเป็นชื่อ
   ร้านค้าพื้นหลังในฉากสืบสวน (`verification_survey_3d.bin.json` object `M01_03830_camera_dummy02/03`)
   ไม่ใช่ชื่อเกมอาร์เคดจริงของ SEGA และไม่ใช่มุกสองภาษาแบบ Konban Wife — เข้าเกณฑ์ทับศัพท์ตาม §11
   → แก้เป็น **"กล้องวงจรปิดของไฮเปอร์วินเกม"** / **"กล้องวงจรปิดของบาร์โอซาเคโย"**

## G.I. / Hyper Win Game / Bar Ozakeyo — ข้อสรุปที่ขอให้ lead ยืนยัน

- **`G.I.` → คง EN** (ถูกต้องแล้ว ไม่แก้): ตรวจจาก `talk.bin.json` idx ~191931 พบบทพูดต้นตอ
  `"People are too embarrassed to say his name though, so they call him \"G.I.\""` — เป็นชื่อเล่นที่
  มาจากตัวอักษรย่อล้วน ๆ (ไม่ใช่คำเต็มแบบ Panty Professor/Ass Catchem/Judge Creep 'n Peep ที่แปลได้)
  จึงเข้าข่ายเดียวกับ initialism/โค้ด (AD-9 · SP · ESC) ที่โปรเจกต์คง EN เสมอ → **แนะนำคง EN ต่อไป**
- **`Hyper Win Game` / `Bar Ozakeyo` → ทับศัพท์** (แก้แล้วตามข้างบน): ไม่พบหลักฐานว่าเป็นแบรนด์ SEGA
  จริงหรือมุกสองภาษา จึงใช้กฎ default ของ §11 (ชื่อร้าน/ป้ายส่วนใหญ่ทับศัพท์) — **จุดนี้ยังเป็นการตัดสินของ
  ผู้ตรวจ ไม่ใช่คำล็อกที่ยืนยันจากไฟล์เกม (ไม่มีบทพูดขยายความชื่อสองร้านนี้ที่อื่นในเกม) ขอให้ lead ยืนยัน
  อีกชั้นก่อนล็อกเข้า glossary §11 ถาวร**

## debug string คง EN — ยืนยันครบ 14 คีย์

ตรวจ row key ในไฟล์เกมจริงแล้วยืนยันเป็น debug/test ทั้งหมด: `test_0001;name` … `test_0005;name` (5) ·
`test05 number 1` … `4` (4) · `Investigate Test 01` … `04` (4) · `2D General Purpose Examination Test` (1)
= 14 คีย์ ตรงกับที่ lead รายงานไว้ล่วงหน้า — นักแปลคง EN ถูกต้องทุกจุด ไม่ต้องแก้

## ชื่อ/นามสกุลตัวละคร — ตรวจ precedent แล้วตรงกับ glossary ทุกจุด

- `Daisuke` → **ไดสึเกะ** ("Daisuke's Sandals") ✓ตรงกฎ su=สึ
- `Akagawa-san` → **อาคางาวะซัง** (เติม ซัง ตาม -san ใน EN ตามกฎ honorific §0 ของ PRONOUN_MATRIX) ✓
- `Kuwayama` → **คุวายามะ** ✓ตรงกับ "โคจิโร คุวายามะ" ที่ล็อกไว้แล้วใน glossary §11 (ชื่อตัวละครไซด์เคส)
- `Kaneda`/`Kumakura`/`Nishimura`/`Terasawa`/`Zhuang Shi`/`Ono Michio`/`Azusa Otaki`/`Ayumu-kun` ✓ตรงกับ
  glossary ทั้งหมด (บรรทัด §11 รายชื่อตัวละครจาก batch 096/side case)
- `Ass Catchem` → จอมจับตูด · `Panty Professor` → ศาสตราจารย์กางเกงใน · `Judge Creep 'n Peep` →
  ผู้พิพากษาจอมถ้ำมอง — ทั้งสามคำล็อก ตรงกับ glossary ทุกจุด ไม่มีจุดหลุด

## `verification_*` — ศัพท์ระบบตรวจหลักฐาน

`Verification Mission` → ภารกิจตรวจสอบ · `Search Mission` → ภารกิจค้นหา · `Photo Investigation` →
การสืบสวนภาพถ่าย (คนละคำกับ `Photo Examination` → การตรวจสอบภาพถ่าย ซึ่ง EN ก็แยกคำเองจริง ไม่ใช่ความ
ไม่สม่ำเสมอของนักแปล) — เช็คด้วย `make_multibin_index.py` ครบทุกคีย์สั้นที่มีความเสี่ยง (`Face`·`Key`·`Bed`·
`Entrance`·`Detective`·`Escape`·`Bust`·`Bangs`·`Fridge`·`Sink`·`Glass`·`Punk`·`Current Area`) — **ทุกคีย์อยู่
ใน bin เดียว ไม่มีคีย์ไหนชนกับบริบทอื่น** ปลอดภัยจากปัญหาคีย์ใช้ซ้ำ

## คำที่ควรเพิ่มเข้า glossary

- `Ishimatsu` → อิชิมัตสึ (ตัวละครใหม่ — โผล่ครั้งแรกใน batch นี้ "Find Ishimatsu")
- `Mari` → มาริ (ตัวละครใหม่ — "Figure out Mari's Occupation")
- `Asuka Hachitani` → อาซึกะ ฮาจิทานิ (ตัวละครใหม่ — "Search for Asuka Hachitani")
- `Hideaki Deguchi` → ฮิเดอากิ เดกุจิ (ตัวละครใหม่ — "Find Hideaki Deguchi")
- `Hoshino(-kun)` → โฮชิโนะ(คุง) — มีอยู่ในรายชื่อที่ lead เสนอไว้แล้วใน CLAUDE.md (Kido/Shono/Hoshino ฯลฯ)
  แต่ยังไม่มีในตาราง §📇/§11 ของ glossary — เสนอให้ล็อกเข้าไปตอนตัดสิน batch ที่มีบทพูดของโฮชิโนะเต็ม ๆ

## จุดที่ยังไม่แน่ใจ / อยากให้ lead ตัดสิน

- ทับศัพท์ `Hyper Win Game` → ไฮเปอร์วินเกม และ `Bar Ozakeyo` → บาร์โอซาเคโย (ดูรายละเอียดด้านบน) —
  ไม่มีหลักฐานยืนยันจากไฟล์เกมว่าเป็นแบรนด์จริงหรือมุกคำ จึงใช้กฎ default แทน ขอให้ lead กดยืนยันครั้งเดียว
  แล้วเพิ่มเข้า glossary §11 ให้ครบ (กันหลุดซ้ำถ้าสองชื่อนี้โผล่อีกใน batch หลัง ๆ)

## สรุป dry-run

```
batch_133.done.json              ผ่าน  239  ตก   0  ขาด   0
รวม: ผ่าน 239 · คง EN 14 · ตก 0
```
