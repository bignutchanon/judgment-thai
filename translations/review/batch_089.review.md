# Review — batch_089 (achievement/trophy + เพื่อน 34 คน + ตัวละครยืม VF/Puyo Puyo + ชื่อ Side Case)

**ผล merge_qc.py --dry-run --only 089**: ผ่าน 250 · คง EN 15 · ตก 0

ไม่มีบทสนทนา — ไม่ตรวจสรรพนาม ตามที่ระบุใน brief

## แก้ไปทั้งหมด 16 จุด

### 1) คำล็อกที่เพิ่งประกาศวันนี้แต่นักแปลแปลก่อนคำล็อกออก (13 จุด)

**ชื่อร้าน/สถานที่ที่นักแปลคง EN ไว้ทั้งที่มีคำล็อกอยู่แล้ว/ต้องทับศัพท์ตาม §11**
- `Complete all of the capsule toys in Charles.` — "...ที่ Charles" → **"...ที่ชาร์ลส์"** (Charles ล็อกแล้วใน glossary.md บรรทัด 362)
- `Complete the Decor-oceans Series 1 capsule toy in Charles.` — เปลี่ยน "Decor-oceans"→"เดคอร์-โอเชียนส์" + "Charles"→"ชาร์ลส์" + "Series 1"→"ซีรีส์ 1"
- `Complete the Decor-oceans Series 2 capsule toy in Charles.` — เหมือนบน (Series 2)
- `Decor-oceans S1` → `เดคอร์-โอเชียนส์ S1`
- `Decor-oceans S2` → `เดคอร์-โอเชียนส์ S2`
- `G.A. Building Complete` → `อาคารจีเอครบสมบูรณ์`
- `Invest through Quickstarter to completely fund all G.A. Labs projects.` — "G.A. Labs" → "จีเอ แล็บส์"
- `Order ${item_name} at Earth Angel.` → "...ที่เอิร์ธแองเจิล"
- `Order ${item_name} at Shellac.` → "...ที่เชลแล็ก"
- `Order ${item_name} at Gyu-Kaku.` → "...ที่กิวคาคุ"
- `Order ${item_name} at the Beef Zone.` → "...ที่บีฟโซน"
- `Bantam Owner` — "เจ้าของ Bantam" → **"เจ้าของแบนตัม"** (Bantam ล็อกเป็น "แบนตัม" มาตั้งแต่ K3 — batch นี้เองก็ใช้ "แบนตัม" ถูกแล้วในอีกบรรทัด `Order ${item_name} at Bantam.` เป็นความไม่สม่ำเสมอภายใน batch)
- `Place 1st at Modern Mahjong's hard table` — "Modern Mahjong" → **"โมเดิร์นมาจอง"**
- `Place 1st at Modern Mahjong's medium table` — เหมือนบน

### 2) กติกาสะกด wareme/waryori (2 จุด)

lead ล็อกกฎ wa=วา · re=**เระ** · me=เมะ นักแปลเขียน "วาเรเมะ" (ขาด ะ หลัง เร) แก้เป็น **"วาเระเมะ"** ทั้งสองจุด:
- `Wareme Waryori` → `วาเระเมะวาเรียวริ`
- `Play at Tachibana Mahjong and go out when the wareme is on your side.` → "...ตอนที่**วาเระเมะ**อยู่ฝั่งคุณ"

"waryori" ไม่แตะ — "เรียว" ตรงกับที่ใช้แปล "Ryo Suzaki" → "เรียว สึซากิ" ในบรรทัดอื่นของ batch เดียวกันอยู่แล้ว (wa+ryo+ri = วา+เรียว+ริ) สะกดถูกตามรูปแบบที่ batch ใช้จริง ไม่ต้องแก้

## รายการชื่อร้าน/แบรนด์ที่แปลงจาก EN → ไทย (ตามข้อ 3 ของ brief)

| EN | เดิม (นักแปลคง EN) | แก้เป็น | มีคำล็อกมาก่อนไหม |
|---|---|---|---|
| Beef Zone | Beef Zone | บีฟโซน | ✅ ตรงกับ ref_tm ที่มีอยู่แล้วใน batch_090.json |
| Shellac | Shellac | เชลแล็ก | ✅ ตรงกับ ref_tm ที่มีอยู่แล้วใน batch_090.json |
| Gyu-Kaku | Gyu-Kaku | กิวคาคุ | ✅ ตรงกับ ref_tm ที่มีอยู่แล้วใน batch_090.json |
| Earth Angel | Earth Angel | เอิร์ธแองเจิล | ⚠ **ไม่มี** — ref_tm ใน batch_090.json ก็ยังปล่อย "Earth Angel" ไว้เฉยๆ เป็นข้อเสนอใหม่จาก QC รอบนี้ |
| Decor-oceans | Decor-oceans | เดคอร์-โอเชียนส์ | ⚠ **ไม่มี** — ข้อเสนอใหม่ |
| G.A. Labs / G.A. | G.A. Labs / G.A. | จีเอ แล็บส์ / จีเอ | ⚠ **ไม่มี** — ข้อเสนอใหม่ |

## จุดที่อยากให้ lead ตัดสิน/ยืนยัน

1. **Earth Angel / Decor-oceans / G.A. Labs ยังไม่เคย ship ที่ไหนมาก่อน** — ทั้งสามชื่อนี้ยังปรากฏซ้ำอีกหลาย batch ที่ยังไม่แปล (Decor-oceans: batch_096, batch_TALK_031 · G.A. Labs: batch_121, batch_124, batch_TALK_040 · Earth Angel: batch_120, batch_121, batch_TALK_012, batch_TALK_069) — ควร lock สะกดที่ใช้ในรายงานนี้ก่อนแตะ batch พวกนั้น เพื่อกันสะกดเพี้ยนข้าม batch
2. **Captain Cop** — ตรวจแล้วจาก `extracted/facts/scenario_summary.json` (id `sidA28`) และ `complete_checklist.json` (`table.28.judge_side_A28.1`): "Captain Cop" คือ**ชื่อทางการของ Side Case A28** ไม่ใช่คำที่ตัวละครในเกมเรียก Kaito จริง — เนื้อคดีเรียก Kaito แค่ "some kind of superhero"/"hero of justice" เท่านั้น ไม่มีจุดไหนเรียก Kaito ว่า "Captain Cop" ตรงๆ เพราะฉะนั้นเป็นชื่อคดีที่ต้องแปลเหมือนชื่อคดีอื่นๆ ทั้งหมด (ไม่ใช่ proper noun ที่ต้องคง EN) — คำแปล "กัปตันตำรวจ" ของนักแปลใช้ได้ ไม่แก้ (แม้ Kaito จะไม่ใช่ตำรวจจริง แต่ชื่อคดีอื่นในซีรีส์นี้ก็ใช้ชื่อเชิงประชดแบบนี้เหมือนกัน เช่น "The Pervert King")
3. **Batting Center** — batch_089 **ไม่มี** string "Batting Center" เลย (ตรวจแล้วไม่พบ) จึงไม่มีอะไรต้องแก้ในไฟล์นี้ แต่แจ้งไว้ว่า `translations/glossary.md` §10 (บรรทัด 433, ล็อก 21 ส.ค. 2026) **ตัดสินไปแล้ว** ว่า Batting Center → **"ศูนย์ฝึกตี"** — lead ควรใช้ค่านี้กวาด batch_086/088 ที่ขัดกันให้ตรงกัน
4. **"Time Attack Vol. X"** → นักแปลสร้างคำใหม่ "ไทม์แอททาคุ" (ทับศัพท์เสียงญี่ปุ่นแบบ タイムアタック) ไม่มี precedent จากภาคไหนในโปรเจกต์ — ไม่ได้แก้เพราะไม่อยู่ในขอบเขตงานที่สั่ง แต่ใช้สม่ำเสมอครบทั้ง 10 จุดในไฟล์ (Vol. 1–10) ถ้า lead อยากเปลี่ยนเป็นคำอื่นควรเปลี่ยนพร้อมกันทั้งชุด

## ตรวจแล้วไม่มีปัญหา (ไม่ต้องแก้)

- **mahjong/riichi**: ทุกจุดใน batch สะกด "มาจอง" (ไม่ใช่ "มาจอง") และ "รีช" (ไม่ใช่ "รีช") ถูกต้องอยู่แล้ว หลังแก้ Modern Mahjong ก็ครบทั้ง 3 ร้าน (ลัลลาบายมาจอง/โมเดิร์นมาจอง/ทาชิบานะมาจอง)
- **ชื่อเพื่อน 34 คน**: ตรวจกฎ su=สึ · zu=ซึ · g กลางคำ=ก · ki ท้ายชื่อ=กิ ครบทุกชื่อที่เข้าเงื่อนไข (Suzaki→สึซากิ, Uozumi→อุโอซึมิ, Kazufumi→คาซึฟุมิ, Kamaguchi→คามากูจิ, Katagiri→คาตากิริ, Deguchi→เดกุจิ ฯลฯ) ถูกต้องหมด ไม่พบ ง แทน ก หรือ ผิดกฎที่ระบุ — เทียบกับ `characters_side.json` แล้วไม่พบชื่อขัดแย้งกับ description/เพศที่บันทึกไว้
- **Extract → สารสกัด**: ใช้สม่ำเสมอครบ 4 จุด (Extract Boy/Aficionado/Addict + "Take an extract...")
- **placeholder**: `${need_player_point_value}` `${need_checklist_completed_num}` `${value}` `${item_name}` ครบตรงทุกคู่ (merge_qc ผ่าน 0 ตก ยืนยันด้วย)
- **ความยาวชื่อ achievement**: ทุกชื่อสั้นกระชับ ไม่มีชื่อไหนยาวเกินสังเกต

## คำที่ควรเพิ่มเข้า glossary

- Earth Angel → เอิร์ธแองเจิล
- Decor-oceans → เดคอร์-โอเชียนส์
- G.A. Labs → จีเอ แล็บส์ (ย่อ G.A. → จีเอ)
- wareme → วาเระเมะ (สะกดตามกฎ wa=วา/re=เระ/me=เมะ — กัน batch อื่นสะกดผิดซ้ำแบบที่เจอใน batch นี้)
