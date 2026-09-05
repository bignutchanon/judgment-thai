# Audit: อักษรละตินตกค้าง (Latin Leftovers) — ทั้งโปรเจกต์

วันที่: 21 ส.ค. 2026 · ผู้ตรวจ: audit agent (spawn เดี่ยว ไม่ spawn ต่อ)
เครื่องมือ: `scripts/check_latin_leftovers.py` (แก้บั๊ก substring-matching แล้วโดย lead ก่อนเริ่มงานนี้)

## สรุปผล

| กอง | จำนวนคำที่คัดแล้ว | การกระทำ |
|---|---|---|
| 1. คง EN ถูกต้อง | ~230 คำ (จาก 239 คำตั้งต้น หลังหัก handle/hashtag ของ Chatter ออกไปแล้ว ~103 คำ) | เติมลง `KEEP_EN` ~90 รายการ (จัดกลุ่ม+คอมเมนต์ที่มา) + ปรับ `scan()` ให้ mask `@handle`/`#hashtag` เชิงโครงสร้าง |
| 2. บั๊กจริง (มีคำแปลไทยชิปแล้วที่อื่น) | **43 จุด** ใน 19 term กลุ่ม | แก้ตรงใน `translations/done/batch_*.done.json` ของคีย์นั้น ๆ แล้ว — merge_qc dry-run ผ่าน 0 ตกทุก batch |
| 3. ให้ lead ตัดสิน | 22 คำ (เหลือหลังหัก 2 กองบน) | ยังไม่แตะ — ดูตารางท้ายรายงาน |

รันซ้ำหลังแก้: `python scripts/check_latin_leftovers.py` (สแกน master_th.json) เหลือ **22 คำ** จากเดิม 239 คำ (ก่อนแก้ KEEP_EN และก่อนอัปเดต `scan()`) — บั๊กจริงที่พบและแก้แล้ว (12 กลุ่มชื่อ/สถานที่ + สกิล) บางส่วนถูก merge เข้า master_th.json แล้วระหว่างงาน (เช็กแล้วว่า master_th.json โตจาก 37,224 เป็น 38,224 คู่ กลางงาน แปลว่ามี process อื่น remerge ระหว่างที่ผู้ตรวจทำงานอยู่ — บาง fix ที่ทำทีหลัง เช่น Apple Pie/Cherry/ชื่อสกิล อาจยังไม่ถูก remerge เข้า master_th ขอให้ lead รัน merge_qc ให้ batch ที่ระบุด้านล่างอีกรอบเพื่อความชัวร์)

---

## กองที่ 2: บั๊กจริง — แก้แล้ว 43 จุด (19 term กลุ่ม, 13 ไฟล์ done)

หลักการยืนยัน: คำเดียวกันมีคำแปลไทยที่ **ชิปแล้วหลายจุด** ใน master_th.json (หรือ locked ใน `translations/glossary.md`) แต่สตริงที่เจอยังคง EN ทิ้งไว้ — เป็นความไม่สม่ำเสมอที่ผู้เล่นจะเห็นจริง ไม่ใช่การตัดสินใจใหม่ของผู้ตรวจ

| คำ EN ที่ตกหล่น | คำแปลที่ใช้ (ตาม precedent ที่ชิปแล้ว) | จุดที่แก้ | batch |
|---|---|---|---|
| Poppo (ชื่อร้านสะดวกซื้อ) | ป๊อปโป | 4 จุด (E/W Shichifuku St., Showa St., Tenkaichi St.) | batch_089 |
| Queen Rouge (คลับคาบาเรต์) | ควีนรูจ | 1 จุด | batch_081 |
| Wild Jackson (ร้านเบอร์เกอร์) | ไวลด์แจ็คสัน | 1 จุด | batch_091 |
| Valhalla Land | วัลฮัลลาแลนด์ (ล็อกใน glossary.md บรรทัด 525 แต่ยังไม่เคยชิปที่ไหนเลย) | 1 จุด | batch_121 |
| Charles (ร้านเกมของฮิงาชิ) | ชาร์ลส์ | 1 จุด ("Charles Employee" → "พนักงานชาร์ลส์") | batch_001 |
| M Side Cafe | เอ็ม ไซด์ คาเฟ่ | 2 จุด | batch_TALK_016, batch_103 |
| Beef Zone | บีฟโซน | 1 จุด | batch_088 |
| Mantai Internet Café | ร้านอินเทอร์เน็ตคาเฟ่มันไท | 1 จุด | batch_127 |
| Smile Burger | สไมล์เบอร์เกอร์ | 1 จุด | batch_089 |
| Nyan Nyan Cat Café | คาเฟ่เนียนเนียน | 1 จุด | batch_121 |
| Akaushimaru | อากาอุชิมารุ | 1 จุด | batch_089 |
| King of Kamurocho / Titan of Tokyo / Ace of Japan / Global Goliath (ชื่อคอร์สตีลูกบอล Yoshida Batting Center) | ราชาแห่งคามุโรโจ / ไททันแห่งโตเกียว / เอซแห่งญี่ปุ่น / โกไลแอธระดับโลก | 16 จุด (achievement description "Clear the X home run/challenge course...") | batch_103 |
| Apple Pie (คลับคาบาเรต์) | แอปเปิลพาย | 2 จุด | batch_101 |
| Heart of a Champion / High Roller / Elevated Roller / Exalted Roller / Code Hunter / Bottomless Stomach / Danger Display (ชื่อสกิล) | หัวใจแชมป์ / นักเสี่ยงตัวยง / นักเสี่ยงระดับสูง / นักเสี่ยงระดับเซียน / นักล่ารหัส / ท้องไม่มีก้นบึ้ง / แสดงจุดอันตราย | 7 จุด (ข้อความ "Reading this guide has unlocked X...") | batch_050, batch_097 |
| Cherry (ร้านทำผม) | เชอร์รี่ | 2 จุด | batch_100 |
| Premium Adventure | พรีเมียมแอดเวนเจอร์ | 1 จุด (ในข้อความ case_file "When It's Time to Take a Break") | batch_100 |

**หมายเหตุสำคัญ**: กลุ่ม "Heart of a Champion ฯลฯ" คือกลุ่มสกิลที่ทั้งหมด 8 ตัวมีรูปแบบข้อความเดียวกัน ("Reading this guide has unlocked X. Learn how to use it on the Skill App.") — พบว่า **7 ใน 8 ตัว** ลืมแปลชื่อสกิลในข้อความนี้ทั้งที่ชื่อสกิลตัวเองแปลแล้ว ยกเว้น **Re-guard** ที่ไม่มีคำแปลไทยชิปที่ไหนเลย (ดูกองที่ 3)

batch ที่แตะทั้งหมด (lead ต้องรัน `merge_qc.py` ให้ใหม่): `001, 050, 081, 088, 089, 091, 097, 100, 101, 103, 121, 127, TALK_016` — ทุก batch รัน `--dry-run` แล้วผ่าน 0 ตก 0 ขาด

---

## กองที่ 1: คง EN ถูกต้อง — สรุปเป็นกลุ่ม (เติมใน KEEP_EN แล้ว)

- **ชื่อเกมอาร์เคด/แบรนด์จริง**: Out Run, Fighting Vipers, Fantasy Zone, Space Harrier, Championship/Motor Raid, UFO (Catcher), Koi-koi, Don Quijote, Jungle Boy, Super Monkey Ball, DARTSLIVE(CARD), Final Showdown, VF/VF2/FS, Kitty Kat, D&C — ตรงกับ glossary.md §"ชื่อเกมที่คง EN"
- **ตัวละครแบรนด์ SEGA ในเกม**: Bahn, Tokio, Raxel, Sanman, Picky, Grace, Honey (Fighting Vipers) · AiAi, GonGon, MeeMee (Super Monkey Ball) — ชื่อคาแรกเตอร์จริงจากเกมต้นฉบับ ไม่มีใครแปล
- **ชื่อคอร์ส VR/มินิเกม**: Simple Road, Wide Way, Northern Canyon, Breakthrough Cafe, Pipeline (Motor Raid) · Lullaby/Modern Mahjong · Koro-nyan · SugorokuHacks · Paradise (VR)
- **ตัวย่อ UI/กราฟิก**: Lv, HP, DNA, QR, GPS, DLC, Mk, Max, Reverse, UI, NPC, CAUTION, AD (AD-9), Challenge/Home Run Course, DLSS, XeSS, GPU, Xe-HPG, FOV, Anti-Aliasing, Screen Space Ambient Occlusion, AI Super Resolution, Intel Xe Super Sampling, Capture Gallery, OPTIONS, New Game(+), VIP, IQ, II/III/IV, ver, KotD (= Kamuro of the Dead)
- **ศัพท์ดาร์ท**: Ton, Three in a Bed, White Horse, Bull — ตรงกับ glossary.md §"ศัพท์ดาร์ท"
- **เพลง/สินค้า Haruka Sawamura + มุกเล่นคำ**: So Much More, DREAMLINE, T-SET, Japan Dome, Amidst a Dream, nice dice, Open Beta Boyz
- **อื่น ๆ**: KJ/KJ Art (บริษัทบังหน้า — คง EN ทุกจุดกว่า 40 ครั้งในเกม), G.I., YAGAMI System, Ryu Ga Gotoku Studio, Un/Deux/Trois (ฝรั่งเศสในบทพูด), a-z/A-Z (rule text), UFO, J-pop, Dice and Cube (เวอร์ชันสะกดเต็มของ Dice & Cube ที่ถูกตัดด้วย font_kind tag)

นอกจากนี้ปรับ `scan()` ให้ mask `@handle` และ `#hashtag` ของแอป Chatter (SNS ในเกม) เชิงโครงสร้างก่อนสแกน — ลดจาก ~103 คำเป็น false positive ทันที เพราะชื่อ handle ปลอมของ NPC เกิดใหม่ทุก batch แจกแจงใน KEEP_EN ทีละชื่อไม่ไหว (ตัวอย่างที่หายไป: `@sei_love_sei`, `@AI_chan`, `@Sharkuma`, `@zakiyama` ฯลฯ)

---

## กองที่ 3: ให้ lead ตัดสิน (22 คำ)

| คำ | บริบท | ประเด็นที่ต้องตัดสิน |
|---|---|---|
| cabbage / baggage / luggage / toilet / takeout / "take you out" / "take it to go" | ฉากบทสนทนาเดียว สอนคำศัพท์อังกฤษ (นักเรียนแลกเปลี่ยนเทียบ "baggage" กับ "cabbage" ฯลฯ) | คำอังกฤษเหล่านี้ **ถูกต้องแล้วที่คง EN** เพราะเป็นตัวบทสนทนาที่พูดถึงคำศัพท์อังกฤษเอง ไม่ใช่คำแปลตกหล่น — ผู้ตรวจ **ไม่เติมใน KEEP_EN** เพราะเป็นคำอังกฤษทั่วไปเสี่ยงกลืนบั๊กจริงคำอื่นในอนาคต ขอให้ lead ยืนยันแนวทางนี้ |
| Romance of the Three Kinkdoms x2 | ชื่อเกมมาจอง/บอร์ดเกมที่ร้าน Pink Street | มี typo ในซอร์ส EN เอง ("Kinkdoms" ไม่ใช่ "Kingdoms") — ไม่ชัดว่าเป็นชื่อเฉพาะที่ต้องคง EN ตามซอร์ส หรือควรรายงานเป็นบั๊กฝั่ง EN ต้นทาง |
| Clan Creator | "Clan Creator victory" — ระบบ/ฟีเจอร์ (อาจเป็นชื่อฟีเจอร์ PlayStation) | ไม่มี precedent อื่นในเกม ไม่แน่ใจว่าเป็นฟีเจอร์แพลตฟอร์ม (คง EN) หรือชื่อในเกม (ควรแปล) |
| BBQ | "Tripe BBQ" คง EN แต่ "XL Horumon BBQ" → "โฮรุมงย่าง XL" (แปล BBQ ทิ้งไปเป็น "ย่าง") | **ไม่สม่ำเสมอในของที่ชิปแล้วเอง** สองแนวทางขัดกัน ต้องเลือกมาตรฐานเดียว (คง "BBQ" เสมอ หรือแปลเป็น "ย่าง" เสมอ) |
| Baby | "A plush of Baby from Super Monkey Ball." — ตุ๊กตาคาแรกเตอร์ Super Monkey Ball | ชื่อคาแรกเตอร์จริง (คู่กับ AiAi/GonGon/MeeMee ที่คง EN แล้ว) แต่ "Baby" เป็นคำอังกฤษทั่วไปเกินไป ผู้ตรวจไม่กล้าเติม KEEP_EN แบบ global — ควรคง EN แต่ขอ lead ยืนยัน |
| Re-guard | "...unlocked Re-guard. Learn how to use it..." — สกิลต่อสู้ | ต่างจากสกิลพี่น้องอีก 7 ตัว (Heart of a Champion ฯลฯ) ที่มีคำแปลไทยชิปแล้ว — **Re-guard ไม่มีคำแปลไทยที่ไหนเลย** อาจเป็นสกิลที่ยังไม่เคยแปล ไม่ใช่แค่ตกหล่น ต้องส่งเข้า pipeline แปลใหม่หรือ lead ตัดสินคง EN |
| wild | "...everything has to be \"wild,\" so..." | คำเดี่ยวมีเครื่องหมายคำพูด ไม่แน่ใจบริบทเต็ม (ไม่ได้อ่านคีย์ EN เต็ม) — เสี่ยงต่ำ ให้ lead เช็กเอง |
| OFF | ตัวเลือก Autosave ("If OFF is selected...") | น่าจะคง EN ตามธรรมเนียม toggle ON/OFF แต่เป็นคำทั่วไปเสี่ยงกลืนบั๊กอื่น ไม่เติม KEEP_EN global |
| Judgment | อ้างอิงชื่อเกมตัวเอง ("...เพื่อเสริมประสบการณ์การเล่น Judgment") | ถูกต้องที่คง EN (ชื่อเกม) แต่ "judgment" เป็นคำอังกฤษทั่วไปด้วย (คำพิพากษา ฯลฯ) — ผู้ตรวจไม่กล้าเติม KEEP_EN แบบ global เพราะจะกลืนบั๊กจริงถ้ามีที่อื่นแปล "judgment" (คำทั่วไป) ตกหล่น |
| Serenade | "Well, looks like Serenade's totally gone to shit..." พูดถึงคู่กับ Devil Aragaki | อาจเป็นชื่อวงดนตรี/สถานที่ ไม่มี precedent ที่ไหน ไม่แน่ใจว่าควรทับศัพท์หรือคง EN |
| Devil Aragaki | ทวีต SNS "Devil Aragaki's new album is FIRE" (แฮชแท็ก #devilaragaki ด้านล่างคง EN ถูกต้องแล้ว) | ชื่อศิลปิน/สเตจเนม ไม่มี precedent — อารากากิเฉย ๆ (ไม่มี "Devil") แปลเป็น "อารากากิ" ที่อื่นแล้ว แต่ "Devil Aragaki" ทั้งวลีอาจเป็นชื่อวงดนตรี/ฉายาที่คง EN ตามธรรมเนียมชื่อค่าย/วงดนตรี |
| Wear Me | "What is the \"Wear Me\" thing?" | ชื่อฟีเจอร์แต่งตัว/ไอเทมที่ยกมาเป็นคำพูด ไม่มี precedent |
| Top of Ocean Hotel | "a love hotel called the Top of Ocean Hotel" | ชื่อโรงแรมม่านรูดสมมติ ไม่เคยมีคำแปลไทยที่ไหนมาก่อน (ต่างจาก Queen Rouge/Apple Pie ที่มี precedent) — ถ้าจะทับศัพท์ต้องตั้งคำแปลใหม่ ไม่ใช่แค่แก้ตาม precedent จึงเกินขอบเขตงาน audit นี้ |
| Tiger | "...there's a tiger embroidered on the back. It says \"Tiger\" on it, too." | ข้อความสลัก/ปักบนเสื้อ (ไม่ใช่ชื่อแบรนด์ล็อกแบบ Charles) — ไม่ชัดว่าควรทับศัพท์ตามกฎ "ข้อความสลักบนวัตถุ" (glossary บรรทัด 481) หรือคง EN เพราะเป็นคำสามัญไม่ใช่ชื่อเฉพาะ |

---

## รายการไฟล์ที่แก้

- `scripts/check_latin_leftovers.py` — เติม `KEEP_EN` ~90 รายการ (มีคอมเมนต์บอกที่มา) + เพิ่ม `HANDLE_RE` mask `@handle`/`#hashtag` ใน `scan()` + ยุบช่องว่างซ้ำจาก tag-strip ก่อนเทียบ `KEEP_EN`
- `translations/done/batch_001.done.json`, `batch_050.done.json`, `batch_081.done.json`, `batch_088.done.json`, `batch_089.done.json`, `batch_091.done.json`, `batch_097.done.json`, `batch_100.done.json`, `batch_101.done.json`, `batch_103.done.json`, `batch_121.done.json`, `batch_127.done.json`, `batch_TALK_016.done.json` — แก้เฉพาะคีย์ที่ระบุในตารางกองที่ 2 (43 จุด) ทุกจุดแทนที่เฉพาะคำ EN ที่ตกหล่นด้วยคำแปลไทยที่ชิปแล้ว ไม่แตะส่วนอื่นของสตริง

**ไม่ได้แตะ**: `translations/master_th.json`, `translations/slotmap.json`, worklist ใดๆ (ตามกติกา) — สังเกตว่า master_th.json ถูก remerge โดย process อื่นระหว่างงาน (37,224 → 38,224 คู่) ควร verify ว่า fix ทั้งหมดโดยเฉพาะ Apple Pie/Cherry/ชื่อสกิล (ทำท้ายสุด) ถูก merge เข้าจริงหรือยัง
