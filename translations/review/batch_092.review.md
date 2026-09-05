# QC batch_092 — ชื่อเมนู/ไอเทม/UI (item.bin, help.bin, ดาร์ต, EX Bond ฯลฯ)

ผลตรวจ: `python scripts/merge_qc.py --dry-run --only 092` → **ผ่าน 250 · คง EN 3 · ตก 0**

## แก้แล้ว 4 จุด

1. **ชื่อ EX Bond ผิด glossary (§11)** — สระผิด (สั้น/ยาว):
   - `EX Bond: Sota Nonomura`: "โซตะ โนโนมุระ" → **"โซตะ โนโนมุระ"** (ล็อก: Sota Nonomura → โซตะ โนโนมุระ)
   - `EX Bond: Kiyoshiro Asamura`: "คิโยชิโร อาซามุระ" → **"คิโยชิโร อาซามุระ"** (ล็อก: Kiyoshiro Asamura → คิโยชิโร อาซามุระ)
   - ชื่อ EX Bond อีก 4 คน (Takeo Inose / Alice Ino / Dwayne Cruise / Hanae Ida) ตรง glossary อยู่แล้ว ไม่ต้องแก้

2. **กฎชื่อร้าน vs ชื่อสินค้า (Wette Kitchen) หลุด 2 จุด**:
   - ชื่อไอเทม `Wette Original Coffee` แปลเป็น "กาแฟต้นตำรับเว็ตเทคิทเช่น" — ผิดสองต่อ: (ก) ต้นฉบับไม่มีคำว่า "Kitchen" เลย เป็นการเติมเข้ามาเอง (ข) ทับศัพท์ "Kitchen" ทั้งที่ชื่อร้าน Wette Kitchen ล็อกให้คง EN → แก้เป็น **"กาแฟต้นตำรับเว็ตเท"** ให้ตรงแพทเทิร์นเดียวกับ Wette Burger/Wette Egg Burger ในชุดเดียวกัน (คำนำหน้า "เว็ตเท" เฉย ๆ ไม่มี Kitchen)
   - คำบรรยาย Iced Lemon Tea ("A popular **Wette Kitchen** soft drink...") แปลเป็น "เครื่องดื่มขายดีของ**เว็ตเทคิตเชน**..." — ทับศัพท์ชื่อร้านทั้งที่อยู่ในประโยค (ไม่ใช่ชื่อเมนู) ต้องคง EN ตามกฎใหม่ + ขัดกับอีก 2 จุดในชุดเดียวกัน (บรรยาย Wette Burger / Wette Original Coffee) ที่คง "Wette Kitchen" เป็น EN ถูกต้องอยู่แล้ว → แก้เป็น **"เครื่องดื่มขายดีของ Wette Kitchen ให้ความสดชื่นด้วยกลิ่นซิตรัสสดใหม่"**

## ตรวจแล้วไม่มีปัญหา

- **ความสม่ำเสมอชุดอิมุระยะ** (5 รายการ) — ทุกตัวใช้แพทเทิร์น "ซาลาเปา[ชนิด]อิมุระยะ" ตรงกันหมด (lead แก้ Imuraya Gold Pizza Bun ไว้ก่อนแล้ว)
- **ไวลด์แจ็คสัน** — ทั้ง 2 จุดที่เหลือในชุด (Wild Jackson's signature hamburger / Wild Jackson's original mayo) สะกดถูกแล้ว ไม่มีตกค้าง "ไวลด์แจ็คสัน"
- **Grade-A prefix** (Salted Beef Tongue / Kalbi / Sirloin / Harami) — รูปแบบ "X เกรดเอ" ตรงกันทั้ง 4 คู่
- **ชื่อร้าน/สินค้าที่เหลือ**: คาเฟ่อัลป์ส, คันไร ทับศัพท์ถูกตามกฎ §11 ไม่มีจุดขัดแย้ง
- **คำล็อกใหม่** (EX Bond → สายสัมพันธ์ EX · Investigation Action → การสืบสวน · On the Side → กิจกรรมเสริม · Extracts/Creating Extracts/Extract Ingredients · Meguro → เมกุโระ · Wakahara → วาคาฮาระ · EX Gauge → เกจ EX) ตรง glossary ทุกจุด
- **คง EN 3 จุด**: Toughness Z, Tauriner (ชื่อแบรนด์เครื่องดื่มพลังงาน — สมเหตุสมผล คงชื่อแบรนด์) · EX Actions (ล็อก glossary §11 ให้คง EN) — ไม่มีจุดที่ควรแก้
- placeholder `${...}`/`%s`/`%d` ครบทุกคู่ (สคริปต์เช็คอัตโนมัติผ่าน) · ไม่พบ ❤ ♥ ♪ ★
- ไม่มีบทสนทนา จึงไม่มีสรรพนามให้ตรวจตามบรีฟ

## เสนอเพิ่ม glossary (สำหรับ lead)

- **"Wette Original Coffee" ไม่ควรทับศัพท์ "Kitchen" เข้าไปเอง** — เตือนไว้เผื่อ batch อื่นที่มีเมนูจากร้าน Wette Kitchen ซ้ำแบบเดียวกัน (ใช้แค่คำนำหน้า "เว็ตเท" พอ อย่าใส่ "Kitchen" เพิ่มโดยไม่มีในต้นฉบับ)
- ไม่มีจุดอื่นที่อยากให้ lead ตัดสินเพิ่มเติม

## สรุป

แก้ 4 จุด (ชื่อเฉพาะผิด glossary 2 · กฎชื่อร้าน-vs-สินค้าหลุด 2) · merge_qc ผ่าน 250/250 ตก 0
