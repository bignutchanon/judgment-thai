# บริบทเนื้อหาเสริม — Judgment (JETH)

> เอกสารนี้ทำหน้าที่เดียวกับ `side_content_context_k3.md` / `side_content_context_y6.md` — สรุประบบ
> เนื้อหานอกเรื่องหลักทั้งหมดของ Judgment ให้นักแปลรู้ที่มา/โทน/ศัพท์ก่อนแปลจริง
> **ทุกข้อเท็จจริงมาจาก `extracted/facts/*.json` เท่านั้น** (ระบุชื่อไฟล์ต่อท้ายทุกจุด) —
> ไม่มีการเดาเนื้อหาจากชื่อคดี/มินิเกมอย่างเดียว ที่ไม่มีข้อมูลยืนยันจะทำเครื่องหมาย **⏳** ไว้ชัดเจน
> ชื่อเฉพาะทั้งหมดคง EN ตามนโยบาย — เอกสารนี้ไม่ตัดสินชื่อไทยเด็ดขาด เสนอเป็น `proposal` ให้ lead เท่านั้น
>
> ไฟล์นี้แบ่งเป็น 2 ส่วน: **part1** (ไฟล์นี้) = Side Cases + Friends + Girlfriends ·
> **part2** (`side_content_context_judge.md.part2`) = มินิเกม + KamuroGo/ระบบภารกิจ + ร้าน/สถานที่ +
> Completion + สกิล/ระบบต่อสู้ + ตารางศัพท์ยืม/ศัพท์ใหม่ + สิ่งที่ค้าง

---

## 0. โครงสร้างช่องทางรับ Side Case (จาก `manual.json`)

Side Case ทั้ง 50 คดีรับผ่าน 3 จุดหลักในเกม (ยืนยันจาก `manual.json` id `judge_base1`/`judge_base2`):
- **Yagami Detective Agency** (บ้าน/ออฟฟิศยากามิ) — คดีเริ่มต้น/คดีที่ผูกกับเนื้อเรื่องหลัก
- **Bar Tender** — คุยกับ **Jo Masuda** (เจ้าของร้าน) เพื่อดูคดีที่เปิดใหม่ ต้องสร้างสัมพันธ์กับคนในพื้นที่ก่อนคดีจะปลดล็อกเพิ่ม
- **Genda Law Office** — คุยกับ **Saori Shirosaki** (ทนายในสำนักงาน) เพื่อดูคดี ผูกกับผู้อำนวยการ **Ryuzo Genda** (อดีตเจ้านายยากามิ)

ที่มา: `extracted/facts/manual.json` id `judge_base1`, `judge_base2`

---

## 1. Side Cases (50 คดี)

**ที่มาหลัก:** `extracted/facts/scenario_summary.json` (บทสรุปคดีที่เกมเขียนเอง — มี `context` ก่อนคดีจบ +
`update_list.1..4` = สรุปหลังคดีจบ ให้สปอยล์เต็ม) และชื่อคดีทางการจาก `extracted/facts/complete_checklist.json`
(id `judge_clear_side_case`, ใช้ตอนปลดล็อกความสำเร็จ)

**⚠ ข้อขัดแย้งชื่อคดีที่พบ (รายงาน lead):**
- **A29**: journal (`scenario_summary.json`) ใช้ชื่อ **"Master and Pupil"** แต่ป้ายความสำเร็จ (`complete_checklist.json`)
  ใช้ **"The Circle of Law"** — คนละชื่อกันแม้เป็นคดีเดียวกัน (Genda ปกป้องลูกความในคดีแย่งลูก)
- **A30**: journal ใช้ **"The Pigeon Takes Flight"** แต่ป้ายความสำเร็จใช้ **"The Bird Takes Flight"**
- ทั้งสองจุดต้อง verify กับ string ตอนคดีเริ่ม/จบจริงในเกม (case file UI) ก่อน freeze ชื่อไทย — อาจเป็นไปได้ว่า
  journal string เป็นชื่อคนละช่วง (ก่อน/หลังคดี) ของคดีเดียวกัน ไม่ใช่บั๊ก

**โทน:** จัดตามอ่านเนื้อหาจริง (ตลก / ดราม่า / ลามก-ทะลึ่ง / แอ็กชัน-ระทึกขวัญ / อบอุ่น-เบา) — คดีจำนวนมากผสมโทน
("ตลก/ดราม่า" = เปิดเรื่องตลกแต่จบเศร้า หรือกลับกัน) ระบุคอลัมน์ "จุดต้องระวัง" เฉพาะคดีที่มีประเด็นอ่อนไหว
(ล่วงละเมิดทางเพศ, พยายามฆ่าตัวตาย, หลอกขายบริการทางเพศ) เพราะเป็นจุดที่โทนภาษาไทยพลาดง่ายที่สุด

### 1.1 ซีรีส์ "Twisted Trio" — 3 คดีโรคจิตชุดแรก (A01–A03) + คดีต่อยอด (A04)

| # | ชื่อคดี (EN) | ผู้ขอ/ตัวละครหลัก | โทน | เรื่องย่อ |
|---|---|---|---|---|
| A01 | The Twisted Trio: Panty Professor | Yosuke Saotome (ขอแทน Tsukino น้องสาว) | ตลกทะลึ่ง | โรคจิตขโมยกางเกงในด้วยโดรน ยากามิล่อด้วยกางเกงในเหยื่อ พบว่าคนร้ายแต่งตัวเป็น "ศาสตราจารย์" |
| A02 | The Twisted Trio: Ass Catchem | Yosuke Saotome | ตลกทะลึ่ง | อดีตนักกีฬาชอบลวนลามก้น Tsukino อาสาล่อเอง แต่โดนจับผิดตัว (Yosuke ผมสั้นโดนลวนลามแทน) |
| A03 | The Twisted Trio: Judge Creep 'n Peep | Yosuke Saotome | ตลกทะลึ่ง | โรคจิตถ่ายภาพคู่รักอัปโหลดเน็ต ไต่กำแพงได้ ปลายเรื่องเฉลย Yosuke โกหกเรื่องแฟนของ Tsukino |
| A04 | The Pervert King | (ต่อยอดจาก Twisted Trio) | ตลกทะลึ่งจัด | "Giant Impact" โชว์อวัยวะเพศใหญ่ใส่ผู้หญิง สุดท้ายเฉลยเป็นชายบริสุทธิ์วัย 78 ปี |

ที่มา: `scenario_summary.json` id `sidA01`,`sidA02`,`sidA03`,`sidA04`

### 1.2 ซีรีส์ "Mad Bomber" — ระเบิดปริศนา 3 ตอน (A05–A07)

| # | ชื่อคดี | โทน | เรื่องย่อ |
|---|---|---|---|
| A05 | Kamurocho's Mad Bomber | ระทึกขวัญ/จับเวลา | ระเบิดลูกแรก ปริศนา "นางฟ้าในเขาวงกตนักรบ" ต้องหาให้ทันเวลา |
| A06 | The Mad Bomber Strikes Again | ระทึกขวัญ/จับเวลา | ระเบิดลูกสอง ปริศนา "วัวในโรงเตี๊ยม" จำกัด 5 นาที |
| A07 | Return of the Mad Bomber | ระทึกขวัญ/จับเวลา | ระเบิดลูกสาม ปริศนา "นกพิราบร้องท่ามกลางซากุระ" Tsukumo (เพื่อนแฮกเกอร์) ช่วยปลดชนวน |

ที่มา: `scenario_summary.json` id `sidA05`,`sidA06`,`sidA07` · หมายเหตุ: Tsukumo = friend_001 (ดูหัวข้อ 2)

### 1.3 ซีรีส์ "Mystery Writer" — ปมปริศนานักเขียน 3 ตอน (A08–A10)

| # | ชื่อคดี | ตัวละครหลัก | โทน | เรื่องย่อ |
|---|---|---|---|---|
| A08 | The Mystery Writer's Stratagem | Kawada (สนพ. Cloudy Skies), Takumi Katagiri (นักเขียน) | ตลกเบา/ปริศนา | ไขปริศนาในงานอีเวนต์เพื่อแย่งลิขสิทธิ์หนังสือให้ Kawada |
| A09 | The Mystery Writer's Gambit | เหมือนบน | ตลกเบา/ปริศนา | ปริศนารอบสอง เพื่อลิขสิทธิ์เล่ม 2 |
| A10 | The Mystery Writer's Masterstroke | เหมือนบน | ตลกเบา/ปริศนา | ปริศนารอบสุดท้ายของไตรภาค Katagiri (จบซีรีส์นักเขียน) |

ที่มา: `scenario_summary.json` id `sidA08`,`sidA09`,`sidA10` · Katagiri = friend_020 (นักเขียนซีรีส์ "Edison")

### 1.4 คดีเดี่ยว — ดราม่า/สืบสวนครอบครัว-คู่รัก

| # | ชื่อคดี | ผู้ขอ | โทน | เรื่องย่อ | จุดต้องระวัง |
|---|---|---|---|---|---|
| A11 | The Darkest Place | Noriko Taguchi (เจ้าของคาเฟ่) | ดราม่าเบา/ประชด | สืบสามีนอกใจ พบว่านอกใจกับเจ้าของบาร์ชั้นบนร้านตัวเอง | — |
| A13 | Way of the Detective | Megumi Hashimoto | ดราม่า | สืบสามีนอกใจรอบสอง นักสืบคนก่อนโกงขายข้อมูลกลับให้สามี | เสียดสีวงการนักสืบ |
| A16 | Reckless Aspirations | Fumie Taniyama | ตลกเบา/ครอบครัว | ตามหลานที่หนีไปเป็นโฮสต์ พบว่าปล้นร้านสะดวกซื้อเพื่อใช้หนี้ป้า | — |
| A17 | Queen of Hearts | Fuyuhiko Tanaka (ปลอมตัว) | ดราม่า/สืบสวน | ตามหาผู้หญิงที่ถูกสตอล์ก ผู้ขอจริงคือสตอล์กเกอร์เอง (Inamoto) | หลอกลวง — ต้องเผยพลิกผัน |
| A21 | The Ghost Tenant | Mamoru Shimazu | ตลกผี | สืบบ้านผีสิงเพื่อต่อรองค่าเช่า สุดท้ายแฟนสาวปลอมเป็นผีเอง | — |
| A26 | Underneath the Mask | Crow (หัวโจรกรรม) | ดราม่า/อาชญากรรม | ตามหา Jester สมาชิกแก๊งขโมย เฉลยเป็นกับดักดึงตัวกลับแก๊ง | — |
| A29 | Master and Pupil / "The Circle of Law" | Genda-sensei | ดราม่าซีเรียส | คดีแย่งสิทธิ์ลูกหลังหย่า Genda ใช้ความเมตตาชนะคดีแทนกลโกง | ชื่อคดีขัดแย้ง — ดูหมายเหตุด้านบน |
| A32 | Revenge of the Keihin Gang | Obayashi (กับดัก) | แอ็กชัน/ดราม่า | แก๊ง Keihin ตั้งค่าหัว 10 ล้านเยน ยากามิบุกทลายฐาน | — |
| A34 | Partners | Adachi (เพื่อนเก่า Kaito) | ดราม่า | Adachi หลอกใช้ Kaito เข้าบริษัทอสังหาฯ สุดท้ายร่วมมือกันจัดการ | — |
| A45 | The Devil Wife | Shizue Kuwayama | ดราม่า/สืบสวน | สงสัยลูกสะใภ้วางแผนฆ่าลูกชาย แท้จริงเป็นเพื่อนร่วมงานหึงหวง | — |
| A46 | Smart Watching | (Nanami ถูกลักพา) | ระทึกขวัญ | Nanami Matsuoka ถูกสตอล์กเกอร์ลักพาตัว ต้องตามรถให้ทัน | ลักพาตัว/สตอล์กเกอร์ |
| A49 | Love and Madness | Sunada | ดราม่าหนัก | แฟนสาวนอกใจจริง ผู้ขอขู่ฆ่าตัวตายถ้าเป็นจริง จบด้วยช่วยจับนักต้มตุ๋น | ⚠ พูดถึงการฆ่าตัวตายตรง ๆ ต้องคุมโทนละเอียดอ่อน |

ที่มา: `scenario_summary.json` id ตามคีย์ที่ตรงกับแต่ละคดี (sidA11, sidA13, sidA16, sidA17, sidA21, sidA26, sidA29, sidA32, sidA34, sidA45, sidA46, sidA49)

### 1.5 ซีรีส์ "Calamity" — หมอดู Amane (A18–A20)

| # | ชื่อคดี | โทน | เรื่องย่อ |
|---|---|---|---|
| A18 | The Black Calamity | ตลก/เหนือธรรมชาติแบบล้อ | Amane ทำนาย "ภัยดำ" จะเกิดกับ Meguro สุดท้ายคือบาร์ชื่อ "Black Alice" (มุกเล่นคำ) |
| A19 | The Black and White Calamity | ตลก/ดราม่าเบา | ทำนายรอบสอง "ภัยขาวดำ" = รถตำรวจ Meguro เข้าใจผิดว่า Amane เป็นต้นเหตุจึงทำร้ายเธอ |
| A20 | The Fire Calamity | ระทึกขวัญ/ดราม่า | ทำนาย "ภัยไฟ" ครั้งใหญ่สุด — Hiyama ผู้ถูกทำนายกลับเป็นวางเพลิงตัวจริงที่จะเผาคามุโรโจ |

ที่มา: `scenario_summary.json` id `sidA18`,`sidA19`,`sidA20` · Amane = friend_052/girl_003 (ระบบเพื่อน+แฟนสาว)

### 1.6 ซีรีส์ "วิกผมทองุนากะ" (A22–A25) + งานวันเกิด

| # | ชื่อคดี | โทน | เรื่องย่อ |
|---|---|---|---|
| A22 | Gone in 20 Minutes | ตลกอบอุ่น | Yukako สงสัยแฟนหาย แท้จริงกำลังเตรียมงานเซอร์ไพรส์วันเกิดพร้อมไอดอล Toya Tokunaga |
| A23 | Gone with the Breeze | ตลกล้วน | วิกผมของไอดอล Tokunaga ปลิวหาย ต้องไล่ตาม |
| A24 | Gone with the Gust | ตลกล้วน | วิกปลิวรอบสอง |
| A25 | Gone with the Gale | ตลกล้วน | วิกปลิวรอบสาม ยากูซ่าเข้าใจผิดคิดว่ายากามิใส่วิกด้วย |
| A33 | Worst Birthday Ever | ตลกฮาเธอ | Tatsuro ขอให้เอ็นเตอร์เทนภรรยาเมาที่คิดว่ายากามิเป็นสามี จบด้วยภรรยาเป็นลม |

ที่มา: `scenario_summary.json` id `sidA22`,`sidA23`,`sidA24`,`sidA25`,`sidA33` · Tokunaga = talk_talker "Tokunaga"/"徳永"

### 1.7 ซีรีส์ตามหาลูก "Hide-and-seek" (A38–A40) + คดีเดี่ยวอื่น

| # | ชื่อคดี | ผู้ขอ | โทน | เรื่องย่อ |
|---|---|---|---|---|
| A38 | Dangerous Hide-and-seek | Shoji Ohata | อบอุ่น/เศร้าเล็กน้อย | ตามหาลูกชาย Ayumu ที่ชอบเล่นซ่อนหา จากรูปถ่ายเป็นเบาะแส |
| A39 | Perilous Hide-and-seek | Shoji Ohata | อบอุ่น/เศร้าเล็กน้อย | ตามหารอบสอง ลูกซ่อนที่อันตรายขึ้นเรื่อย ๆ |
| A40 | Treacherous Hide-and-seek | Shoji Ohata | อบอุ่น/สะเทือนใจ | รอบสาม พ่อในที่สุดวิ่งมาเองเพราะห่วงลูกจริง ๆ |
| A12 | Under the Table Politics | (นักข่าวปลอมตัว) | ตลก | สวมรอยนักข่าวถ่ายภาพนักการเมืองอดีตนักมวยปล้ำรับสินบน |
| A14 | Morale and Morals | Rei Miyamoto | ดราม่า/ประเด็นสังคม | สืบคดีล่วงละเมิดทางเพศในที่ทำงาน สุดท้ายเฉลยเป็นกับดักของผู้ขอเอง | ⚠ พลิกผัน sensitive — ระวังโทนไม่ให้ล้อเลียนประเด็น #MeToo |
| A15 | Amidst a Dream | (Sana Mihama) | ดราม่าหนัก | นักร้องสาวเกือบถูกโปรดิวเซอร์บังคับขายบริการทางเพศแล้วถ่ายคลิปขาย ยากามิช่วยทัน | ⚠ เนื้อหาล่วงละเมิดทางเพศตรง ๆ ห้ามแปลตลก |
| A35 | Interview with a Detective | Hayama (เอเจนซี่) | ตลก/แฟนตาซีเบา | ปลอมตัวเป็นนักดนตรีแวมไพร์ "Bram-sama" หนีสื่อ | ตัวละคร Shijima โผล่ร่วม |
| A36 | Entrapment | (คู่สามีภรรยาต้มตุ๋น) | ตลก | Tatsuo/Maki ต้มตุ๋นยากามิ 100,000 เยน ต้องทวงคืน |
| A37 | Justice is Sweet | Hoshino | ตลกในศาล | ศาลจำลองสอบสวนคดีเค้กหาย (Genda โยนเค้กทิ้งเพราะไฟดับ) |
| A41 | Honey Trap | Hyuga Kotaro ("Horny Hinata") | ดราม่า/ผู้ใหญ่ | ตลกหลุดข่าวมีเซ็กซ์กับเด็กไม่บรรลุนิติภาวะ (ข้อกล่าวหาเท็จ) พิสูจน์บริสุทธิ์ | ⚠ กล่าวหาเรื่อง sex กับผู้เยาว์ — ต้องคุมคำระวังสูง แม้จบด้วยพิสูจน์ว่าเท็จ |
| A42 | Sashimi of the Fallen / The Missing Diamond | เจ้าของ Koi Bride / Taeko Nakahara | สืบสวนเบา/ปริศนา | ปลาคาร์ปกลายเป็นซาชิมิข้ามคืน เชื่อมกับแหวนเพชรที่ถูกขโมย (แหวนอยู่ในท้องปลา) | 2 คดีรวมเป็นเนื้อเรื่องเดียว |
| A43 | A Final Request | Shin Amon | แอ็กชัน (บอสไฟต์) | ชายลึกลับท้าดวลเพื่อเป็นคนแกร่งที่สุดในเมือง |
| A44 | Secrets of Cats | Wang | ตลกเบา/องค์กรลับ | ตามหาแมว "Zhuang Shi" ที่แท้เป็นกุญแจนำไปสู่ขุมทรัพย์หัวหน้าองค์กรที่ตายไป |
| A47 | Tiger Jacket | Akagawa | อบอุ่นเบา | ตามหาแจ็กเก็ตที่พี่ชายให้ ถูกขโมยแล้วคนไร้บ้านเก็บได้ |
| A48 | The Ono Michio Bandit | Hironaka (โปรดิวเซอร์มาสคอต) | ตลก | ชุดมาสคอต "Ono Michio" ถูกขโมยไปใช้ปล้น |
| A50 | Burger Fugitive | (ตำรวจ/รางวัลนำจับ) | แอ็กชัน/ตลกปิดท้าย | นักโทษหนีคุก Tatsuya Gamo ซ่อนตัวในคามุโรโจ ยากามิจับได้ |

ที่มา: `scenario_summary.json` id ตามคีย์ตรงคดี (sidA38–A40, A12, A14, A15, A35–A37, A41–A44, A47, A48, A50)

### 1.8 คดีที่ไม่มี synopsis เต็ม (แนะนำระบบ / ไม่มี update_list) — ⏳ อ่านจาก `missions.json` ตอน sprint จริง

| # | ชื่อคดี | หมายเหตุ |
|---|---|---|
| A28 | Captain Cop | มี context เดียว (ไม่มี update_list.1) — Kaito ช่วยลูกชาย Yosuke จากยากูซ่า เด็กคิดว่า Kaito เป็นฮีโร่ |
| A30 | The Pigeon/Bird Takes Flight | มี context เดียว — เปิดระบบแข่งโดรน (Makihara) ไม่มีบทสรุปคดี เป็นคดีแนะนำระบบ |
| A31 | Paradise VR Unlocked | มี context เดียว — คนไร้บ้านให้เพลย์พาส Dice & Cube แลกข้อมูล Red Nose เป็นคดีแนะนำระบบ VR |

ที่มา: `scenario_summary.json` (ไม่มี `update_list.1..4` ในทั้ง 3 รายการนี้)

**สรุปหมวด Side Cases:** 50 คดี มี synopsis เต็ม 47 คดี (A28/A30/A31 มีแค่ context เปิดคดี) · จัดกลุ่มซีรีส์ได้ 6 ชุด
(Twisted Trio, Mad Bomber, Mystery Writer, Calamity, วิกผม Tokunaga, Hide-and-seek) · พบคดีที่มีเนื้อหาละเอียดอ่อนต้อง
ระวังโทนภาษาไทยเป็นพิเศษ 4 คดี (A14, A15, A41, A49 — ล้วนเกี่ยวกับการล่วงละเมิด/หลอกลวงทางเพศหรือฆ่าตัวตาย)

---

## 2. ระบบเพื่อน (Friends) — 54 คน

**ที่มา:** `extracted/facts/friends.json` (มี `description` ให้ครบทุกคน) + `extracted/facts/complete_checklist.json`
id `judge_friend` (ยืนยันชื่อทางการ 50 จาก 54 — บางคนไม่มีในลิสต์ completion เพราะผูกกับเนื้อเรื่องหลักไม่ใช่ระบบเพื่อนแยก)
+ `manual.json` id `judge_friend0` (กติการะบบ) — **manual ไม่มีข้อความอธิบายกติกาละเอียด เกิน 1 บรรทัด (title เท่านั้น
ไม่มี `table.*` ตามด้วยเนื้อหา) → กติการะดับสนิท/ปลดล็อกอะไรบ้างยังไม่มีข้อมูลยืนยันจากไฟล์เกม ⏳**

ระบบนี้คล้าย "Business/Employee" ของภาคอื่นแต่เป็น "คนรู้จัก" ทั่วเมืองที่ยากามิสร้างสัมพันธ์ผ่านเควสเล็ก ๆ — สนิทมากพอ
ปลดล็อก **EX Bond** (ท่าต่อสู้ร่วมพิเศษ ดูหัวข้อ 6 ใน part2) อย่างน้อย 13 คนมี EX Bond ยืนยันจาก `complete.json`
id `judge_hact65`–`judge_hact77` (Yoshida, Kyushu No.1 Star Owner, Xiu, Nasugawa, Kim Won-soon, Uozumi, Furuya,
Inose, Alice Ino, Sota Nonomura, Kiyoshiro Asamura, Dwayne Cruise, Hanae Ida)

### 2.1 รายชื่อเพื่อนครบ 54 คน (จัดตามกลุ่มอาชีพ/ทำเล)

| # | ชื่อ | อาชีพ/บทบาท (สรุปจาก description) |
|---|---|---|
| 0 | Makoto Tsukumo | นักเทคนิค แฮกเกอร์ ค้นข้อมูล "Chatter" (โซเชียลเน็ตเวิร์กในเกม) ให้ยากามิ |
| 1 | Morio Onodera | คนไร้บ้านในท่อระบายน้ำ ขายของแปลก ๆ (ร้าน Onodera's Wares) |
| 2 | Takeo Inose | ผู้จัดการร้าน Wild Jackson (ไก่ทอด) |
| 3 | Yoshida | ผู้จัดการสนามตีเบสบอลโยชิดะ |
| 4 | Shuichi Hatano | นักพัฒนาอุปกรณ์เบสบอล |
| 5 | Ryan Acosta | ชาวต่างชาติแต่งตัวเป็นนินจา |
| 6 | Mari | ลูกค้าประจำ Bar Tender ปริศนา (ภายหลังเฉลยเป็นนักพนันมืออาชีพ — A27) |
| 7 | Kyushu No. 1 Star Owner | เจ้าของร้านราเมง |
| 8 | Rie Tomioka | เจ้าของตึกที่ยากามิเช่าออฟฟิศ |
| 9 | Yasuhiro Furuya | ผู้จัดอีเวนต์ร้าน Wette Kitchen |
| 10 | Toshikazu Sagara | บาริสต้า Café Alps |
| 11 | Sakura Amamiya | หมอนวดสำเนียงโอซาก้า |
| 12 | Bantam Owner | เจ้าของบาร์ Bantam |
| 13 | Fumio Matsuzaki | เจ้าของร้านยากินิกุ Kanrai |
| 14 | Ryo Suzaki | คนตกงานติดเหล้า พี่ชายฝาแฝดเป็นยากูซ่าถือไม้เท้า |
| 15 | Kim Won-soon | เจ้าของร้าน Beef Zone |
| 16 | Tashiro-kun | สมาชิกตระกูล Matsugane หน้าตาโฉ่งฉ่าง |
| 17 | Masakazu Nekomiya | ชายให้อาหารแมวจรจัด |
| 18 | Takumi Katagiri | นักเขียนซีรีส์ "Edison" (ดู A08–A10) |
| 19 | Sebastian Hutton | แชมป์โลกแข่งโดรน พูดญี่ปุ่นคล่อง |
| 20 | Haoyu Xiu | นักเรียนแลกเปลี่ยนทำงานร้าน Akaushimaru |
| 21 | Voluptuous Woman (ไม่มีชื่อจริงในระบบ) | นักพนันที่ L'Amant |
| 22 | Kenta Uozumi | เชฟซูชิฝึกหัดที่ Sushi Gin |
| 23 | Mami Sakuma | ปาติซีเยร์ M Side Cafe |
| 24 | Hiroto Nasugawa | ผู้จัดการ Akaushimaru สาขา Hotel District |
| 25 | Kenji Tanago | นักกีฬาลู่วิ่ง ฉายา "Mr. Try and Hit Me" |
| 26 | Hanae Ida | พนักงาน Smile Burger |
| 27 | Alice Ino | พนักงานร้านสะดวกซื้อ Poppo |
| 28 | Sota Nonomura | พนักงาน Poppo |
| 29 | Kiyoshiro Asamura | พนักงาน Poppo |
| 30 | Dwayne Cruise | พนักงาน Poppo |
| 31 | Noboru Hiranuma | นักข่าวอิสระ |
| 32 | Noboru Tateyama | พนักงานบริษัท IT "G.A. Labs" |
| 33 | Kaede Sanada | พนักงาน Quadra Garden |
| 34 | Naotaro Terahara | ช่างตัดเสื้อร้าน Le Marche |
| 35 | Goro Moroboshi | คนไร้บ้านในท่อ อดีตหมอในมหาวิทยาลัยแพทย์ |
| 36 | Takemitsu Owner | เจ้าของร้านขนมสไตล์เกียวโต |
| 37 | Shin Fujimori | นักพัฒนาแอประดมทุน "Quickstarter" |
| 38 | Kazuhisa Norimoto | พนักงาน Café Mijore แอบชอบเพื่อนร่วมงาน |
| 39 | Miharu Shima | พนักงาน Café Mijore |
| 40 | Shun Isaka | นักกรีฑา นิสัยแปลก |
| 41 | Ebisu Pawn Owner, Fukutsu | เจ้าของร้านจำนำ Ebisu Pawn |
| 42 | Toshiro Koizuka | เจ้าของร้านกุญแจ Kamuro Lock & Key |
| 43 | The Hermit of the Dragon's Palace, Iyama | ชายชราสกัดยา "Extract" ใน Dragon's Palace (ดูระบบ Extract ใน part2) |
| 44 | Yosuke Saotome | นักศึกษา/บาร์คเกอร์พาร์ตไทม์ ฝาแฝด Tsukino (ผู้ขอ A01–A03) |
| 45 | Shinzato Madoka | โฮสเตสร้าน Apple Pie หาเงินเรียนมหาลัย |
| 46 | Kazufumi Kamaguchi | ซีอีโอบริษัททวงหนี้ Turtle Financing |
| 47 | Hideaki Deguchi | หนุ่มอยากเป็นโฮสต์อันดับหนึ่ง (ผู้ถูกตาม A16) |
| 48 | Kunio Ichinose | ประธาน Ikinari Steak |
| 49 | Yurika Tachibana | พนักงาน Tachibana Mahjong |
| 50 | Sana Mihama | นักร้อง-นักแต่งเพลงมุ่งมั่น (ดู A15 + girlfriend — ⚠ ดูข้อขัดแย้งนามสกุลหัวข้อ 3) |
| 51 | Tsukino Saotome | หญิงสาวเงียบขรึม ฝาแฝด Yosuke (girlfriend candidate) |
| 52 | Amane | หมอดู "เห็นลางร้าย" (girlfriend candidate, ดู A18–A20) |
| 53 | Nanami Matsuoka | หญิงสาวบุคลิกเฉียบคม (girlfriend candidate, ดู A46) |

ที่มา: `extracted/facts/friends.json` ทุกแถว (idx 0–53)

**สังเกต:** 4 คนสุดท้าย (idx 50–53) คือกลุ่มเดียวกับระบบ Girlfriend (หัวข้อ 3) — ระบบเพื่อนกับระบบแฟนใช้
ตัวละครชุดเดียวกันบางส่วน ไม่ใช่ระบบแยกขาดจากกันโดยสิ้นเชิง

---

## 3. ระบบแฟนสาว (Girlfriends / Dating)

**ที่มา:** `extracted/facts/complete_checklist.json` id `judge_girl_friend` (4 คน) + `manual.json` id
`judge_girlfriend0`/`judge_girlfriend1`/`judge_girlfriend2` (`Girlfriends`, `Dating`, `Topic Talks`) +
`judge_girlfriend3`/`judge_girlfriend4` (`Presents`, `Once It's Official`)

### 3.1 แฟนสาว 4 คน

| # | ชื่อ (ตาม completion) | ชื่อ (ตาม friends.json) | หมายเหตุ |
|---|---|---|---|
| 1 | Sana Omura | Sana Mihama | **⚠ นามสกุลไม่ตรงกัน — ต้อง verify กับ talk/UI string จริงก่อน freeze**: อาจเป็นชื่อเล่นก่อนแต่งงาน/หลังแต่งงานในเนื้อเรื่อง หรือเป็นความคลาดเคลื่อนของข้อมูลเกม |
| 2 | Tsukino Saotome | Tsukino Saotome | ตรงกัน |
| 3 | Amane | Amane | ตรงกัน (ไม่มีนามสกุล) |
| 4 | Nanami Matsuoka | Nanami Matsuoka | ตรงกัน |

ที่มา: `complete_checklist.json` id `judge_girl_friend` เทียบกับ `friends.json` idx 50–53

### 3.2 กติการะบบ (จาก `manual.json`)

- **Girlfriends** (`judge_girlfriend0`): พบผู้หญิงที่มีศักยภาพผ่าน Side Case ก่อน — สนิทมากพอจะเริ่มทักแชทมาเอง แล้วชวนออกเดตผ่านแอปข้อความในเกมได้
- **Dating** (`judge_girlfriend1`): เลือกตัวเลือกบทสนทนาที่คิดว่าเธอจะพอใจเพื่อสร้างความสนิทสนม (intimacy) — ปฏิเสธคำชวนได้โดยไม่เสียโอกาส (ชวนใหม่ทีหลังได้) สนิทมากพอเธออาจ **สารภาพความรู้สึก** (confess feelings)
- **Topic Talks** (`judge_girlfriend2`), **Presents** (`judge_girlfriend3`), **Once It's Official** (`judge_girlfriend4`) — มีอยู่จริงแต่ manual.json ไม่มี `table.*` เนื้อหาละเอียด (มีแค่ title) → กติกาเชิงลึก **⏳ ต้องอ่านจาก UI/talk string จริงตอน sprint**

ที่มา: `manual.json` id ตามที่ระบุแต่ละบรรทัด

**ผูกกับความสำเร็จ:** `trophy.json` id `JUDGE_GIRL_FREND_A/B/C` — "Going Steady" (1 คนสารภาพ), "Ladies, Please" (2 คน),
"Now You're Just Bragging" (4 คน) → ระบบรองรับคบพร้อมกันหลายคน (ธรรมเนียมซีรีส์ Yakuza ทั่วไป ไม่ต้องเลือกคนเดียว)

---

*(ต่อที่ `docs/side_content_context_judge.md.part2` — มินิเกม, KamuroGo/ระบบภารกิจ, ร้าน/สถานที่, Completion, สกิล/ระบบต่อสู้, ตารางศัพท์ยืม/ศัพท์ใหม่, สิ่งที่ค้าง)*
# บริบทเนื้อหาเสริม — Judgment (JETH) — ส่วนที่ 2

> ต่อจาก `docs/side_content_context_judge.md.part1` (Side Cases + Friends + Girlfriends)
> ส่วนนี้ครอบคลุม: มินิเกม · KamuroGo/ระบบภารกิจในแอป · ร้าน/สถานที่ · Completion · สกิล/ระบบต่อสู้ ·
> ตารางศัพท์ยืมจากภาคก่อน/ศัพท์ใหม่ที่ต้องตั้ง · สิ่งที่ยังค้าง

---

## 4. มินิเกม (จาก `manual.json` — 200 รายการคู่มือในเกม)

### 4.1 การพนันในร่ม (Dragon's Palace, L'Amant)

| มินิเกม | สถานที่ | กติกาย่อ (จาก `manual.json`) | ศัพท์ล็อกแล้วจากภาคก่อน |
|---|---|---|---|
| Koi-koi (ไพ่ฮานาฟุดะ) | Dragon's Palace | เล่นไพ่ดอกไม้ 12 เดือน จับคู่เก็บไพ่ ประกาศ "Koi" เพื่อเล่นต่อสะสมคอมโบพิเศษ (Junk, Poetry Ribbons, Boar-Deer-Butterfly, Five Lights ฯลฯ) | **koi-koi → โคอิ-โคอิ** (มีขีด ตามคำตัดสิน K3 14 ส.ค. 2026) |
| Oicho-kabu | Dragon's Palace | ใช้ไพ่ดอกไม้เดือน ม.ค.–ต.ค. รวมแต้มให้ใกล้ 9 ที่สุด มีมือพิเศษ (Four-One, Nine-One, Three of a Kind, Ten-Ten-One) | **oicho-kabu → โออิโช-คาบุ** (ตาม PIRATE, glossary_k2 §4) |
| Blackjack | L'Amant | มาตรฐานสากล | ไม่มีคำล็อกเฉพาะ — ทับศัพท์ "แบล็กแจ็ก" |
| Poker: Omaha Hold'em / Texas Hold'em / Pineapple Hold'em | L'Amant | โป๊กเกอร์ 3 รูปแบบแยกโต๊ะ | ไม่มีคำล็อกเฉพาะ — ทับศัพท์ "โป๊กเกอร์" + คงชื่อรูปแบบ (Texas/Omaha/Pineapple Hold'em) ทับศัพท์ตามธรรมเนียมวงการโป๊กเกอร์ |

ที่มา: `manual.json` id `koikoi`, `kabu`, `poker` (ยาว รวม >900 ตัวอักษรกฎ), ยืนยันสถานที่จาก `places.json`
id `judge_k_playspot_ryugujou`, `judge_k_playspot_laman`

### 4.2 มาจอง (3 ร้าน — ระดับความยากต่างกัน)

3 ร้าน (จาก `shops.json`/`complete_group.json`): **Lullaby Mahjong** (มือใหม่ ค่าเข้าถูก), **Modern Mahjong**
(มืออาชีพ ค่าเข้าแพงกว่า ได้รางวัลสูงกว่า), **Tachibana Mahjong** (ร้านใหม่ กติกาเสี่ยงสูงได้สูง เช่น "wareme")

**กติกา/ศัพท์:** `manual.json` id `mahjong0` (Rules, 84–166), `mahjong1` (Hands, 166–235) — เนื้อหายาวมาก อธิบาย
Chi/Pon/Kan/Riichi/Tsumo/Ron/Dora ครบ **ศัพท์ล็อกแล้วจาก K3:** pon → **ปง** · chii → **ชิ** · kan → **คัง** ·
tsumo → **สึโม/จั่วเอง** (แล้วแต่บริบท) · ron → **รอน** · riichi → **รีช** · dora → **โดระ** · han/fu → **ฮัง/ฟุ**
(คงทับศัพท์) · mangan/haneman/baiman/sanbaiman/yakuman → **มังกัง/ฮาเนมัง/ไบมัง/ซันไบมัง/ยากุมัง**

**⚠ กับดักคำว่า "Draw" (สืบทอดจากบทเรียน Y6):** มีอย่างน้อย 3 ความหมายต่างกันในไฟล์มาจอง — "draw a tile" (จั่วไพ่ปกติ),
"Exhaustive Draw" (ไพ่หมดกอง จบแบบเสมอ), "redraw the hand" (แจกไพ่ใหม่ทั้งกระดาน กรณี kyuushukyuuhai/เก้าเทอร์มินัล)
— ต้องดู context รอบข้างทุกครั้ง ห้ามแปลคำเดียวกันหมดทั้งไฟล์

ที่มา: `manual.json` id `judge_playspot0/1/10`, `mahjong0`, `mahjong1`

### 4.3 เกมตู้อาร์เคด SEGA (Club SEGA 2 สาขา)

**สถานที่:** Club SEGA (Nakamichi St.) และ Club SEGA (Theater Square) — ทั้งสองสาขายืนยันจาก `places.json`
id `judge_k_playspot_sega_nakamichi`/`_gekijomae`

**เกมตู้ที่มีคู่มือยืนยัน** (จาก `manual.json` titles):
- **UFO Catcher** — คีบตุ๊กตา (นำมาตกแต่งออฟฟิศยากามิได้ — ดู `judge_base0`)
- **Virtua Fighter 5** (ชื่อ manual: "Virtua Fighter 5", ตัวย่อ `vf5fs` ในความสำเร็จ) — โรสเตอร์ 19 ตัว: Taka-Arashi,
  Akira Yuki, Pai Chan, Lau Chan, Wolf Hawkfield, Jeffry McWild, Jean Kujo, Eileen, Kage Maru, Sarah Bryant,
  Jacky Bryant, Shun Di, Lion Rafale, El Blaze, Aoi Umenokoji, Lei-Fei, Vanessa Lewis, Brad Burns, Goh Hinogami
- **Virtua Fighter 2** (ตัวย่อ `vf2` ในความสำเร็จ — คนละโรสเตอร์กับ VF5, มี 10 ตัว: Akira, Jacky, Sarah, Kage-Maru,
  Lau, Jeffry, Pai, Wolf, Shun Di, Lion)
- **Fighting Vipers**, **Motor Raid** — ยืนยันชื่อจาก `manual.json` title เท่านั้น เนื้อหากติกา ⏳ ยังไม่ได้อ่านละเอียด
- **Kamuro of the Dead** — เกมยิงซอมบี้ (ผูกกับความสำเร็จ `JUDGE_ZOMBIE_HANTER` "Zombie Apocalypse Survivor")
- **Fantasy Zone**, **Space Harrier** — เกมตู้คลาสสิก SEGA ยุค 80s (ชื่อเดียวกับที่ล็อกไว้แล้วใน Y6/Y7: คงอังกฤษ)
- **Puyo Puyo** — เกมต่อบล็อกสี คู่แข่ง 10 ตัว: Ringo, Maguro, Amitie, Sig, Suketoudara, Klug, Rulue,
  Arle & Carbuncle, Risukuma, Witch

**ศัพท์ล็อกแล้ว:** ชื่อเกมตู้ SEGA ทั้งหมด (Virtua Fighter, Fantasy Zone, Space Harrier, UFO Catcher, Puyo Puyo)
→ **คงอังกฤษ** ตามธรรมเนียมทุกภาคที่อ่านมา (K2/Y7/Y8/Y6) · ชื่อตัวละคร VF/Puyo Puyo → คงอังกฤษเช่นกัน (ไม่มี
precedent แปลชื่อตัวละครเป็นไทยในภาคใดที่อ่านมา)

ที่มา: `extracted/facts/complete_checklist.json` id `judge_vf5fs_win_character`, `judge_vf5fs_clear_stage`,
`judge_vf2_select_all_character`, `judge_vf2_clear_stage`, `judge_puyo_win_rival` · `manual.json` titles
"Fighting Vipers", "Motor Raid", "Kamuro of the Dead", "Fantasy Zone", "Space Harrier", "Virtua Fighter 5"

### 4.4 กีฬา/สันทนาการ

| มินิเกม | สถานที่ | กติกา | ศัพท์ล็อก |
|---|---|---|---|
| Yoshida Batting Center | เจ้าของ: friend_003 "Yoshida" | 2 โหมด: **Home Run Course** (ตี 7/10 ลูกให้ได้โฮมรันเพื่อ A Rank), **Challenge Course** (ทำแต้มตามเป้าใน 10 ลูก) — มีเครื่อง "ลับ" ที่โยชิดะปิดล็อกไว้ | **⚠ พบข้อขัดแย้งข้ามภาค:** K2 glossary ใช้ "ศูนย์ตีเบสบอล" (Yoshida Batting Center → ศูนย์ตีเบสบอลโยชิดะ) แต่ **K3 glossary.md เองใช้ "ศูนย์ฝึกตีโยชิดะ"** (ตรงกับ Y7 "ศูนย์ฝึกตี") — ตามลำดับความสำคัญ K3 ใหม่กว่าชนะ → เสนอ **"ศูนย์ฝึกตี" / "ศูนย์ฝึกตีโยชิดะ"** แต่ควรให้ lead ยืนยันอีกครั้ง |
| Darts (DARTSLIVE) | Bantam, Club SEGA (Theater Square) | ดาร์ทมาตรฐาน DARTSLIVE2 เชื่อมต่อเน็ต บันทึกข้อมูลผู้เล่นด้วย DARTSLIVE CARD | DARTSLIVE → คงอังกฤษ (ชื่อแบรนด์จริง, ล็อกจาก K2) |
| Karaoke | ⏳ ยังไม่ยืนยันสถานที่ในไฟล์ facts | กติกา manual.json id `karaoke0` มีอยู่จริงแต่เนื้อหาย่อ (แค่ title "Karaoke" idx 235 ไม่มี table.* ต่อ) | **karaoke → คาราโอเกะ** (glossary_k2 §4) เพลง/เนื้อร้องคงอังกฤษตามกฎทีม |
| Outdoor Shogi | Outdoor Shogi (เปลี่ยนทำเลตามช่วงเวลาของวัน) | Ranked Match (แข่งตามระดับฝีมือ) + Challenge Match (เงื่อนไขพิเศษ) — คนไร้บ้านในท่อรู้เล่นแต่ไม่มีกระดาน | **shogi → โชกิ** (glossary_k2 §4, ตรงกับ Y7 "โชกิ") |

ที่มา: `manual.json` id `judge_playspot2` (Yoshida Batting Center), `judge_playspot3` (Outdoor Shogi), `darts0`,
`karaoke0` · `places.json` id `judge_k_playspot_DARTSLIVE_bantam`, `_sega`

### 4.5 Paradise VR — Dice & Cube (ระบบเฉพาะ Judgment)

**ระบบคืออะไร:** เกมกระดาน sugoroku เสมือนจริงในตู้ VR ที่ **ผู้เล่นเองเป็นตัวหมากบนกระดาน** — มี 2 กติกา
(Standard Rule, Challenge Rule) × 3 คอร์ส (Short/Middle/Long) รวมถึงโหมด **Battle Mission** และโหมดตัวละคร
**Koro-nyan** (มาสคอตแมว — ยืนยันจาก `friends.json`-adjacent talk_talker "ころにゃん"/"Koro-nyan" และ
`complete_checklist.json` มีรายชื่อด่าน 5 ด่าน: YENDAS, IDO, REEF8, JUNOS, BOWEL — น่าจะเป็นชื่อด่าน/คอร์สแฟนตาซี)

**ที่มา:** ปลดล็อกผ่าน Side Case **A31 "Paradise VR Unlocked"** — คนไร้บ้านขาพิการให้เพลย์พาสแลกข้อมูลเบาะแส
"Red Nose" (ดูเนื้อเรื่องหลัก) · ความสำเร็จ `JUDGE_ALL_SUGOROKU_COURCE_CLEAR` "Yagami Party" (เคลียร์ทุกคอร์ส/กติกา)

**ศัพท์เสนอ:** ชื่อระบบ "Paradise VR" และ "Dice & Cube" → คงอังกฤษ (ชื่อเฉพาะสถานที่/เกม) — ไม่พบ precedent
ระบบนี้ในภาคอื่นที่อ่านมา (K2/Y6/K3 ไม่มี VR sugoroku เหมือนกัน) **เป็นระบบใหม่เฉพาะ Judgment ต้องตั้งศัพท์เอง**

ที่มา: `places.json` id `judge_k_playspot_sugoroku` ("Paradise VR"), `complete_checklist.json` id
`judge_sugoroku_stage_clear`, `judge_mr_all_course_clear` · `manual.json` titles "Dice & Cube", "Dice & Cube:
Kuro-nyan", "Dice & Cube: King Koro-nyan", "Dice & Cube: Battle Mission", "Dice & Cube: Koro-nyan Mode"

### 4.6 โดรน (ระบบเฉพาะ Judgment — ใช้ทั้งสืบสวนและมินิเกม)

โดรนไม่ใช่แค่มินิเกม แต่เป็นกลไกสืบสวนหลักของยากามิ แยกใช้งานได้หลายโหมด (ยืนยันจาก `manual.json` titles):
- **Drone** (`judge_survey3`) — บังคับพื้นฐาน แนะนำครั้งแรกใน Chapter 1
- **Drone League** (`judge_playspot7`) — แข่งแข่งโดรน ปลดล็อกผ่าน Side Case **A30**
- **Drone Lab** (`judge_playspot9`) — ประดิษฐ์/อัปเกรดชิ้นส่วนโดรน (ความสำเร็จ `JUDGE_GET_ALL_DRONE_PARTS`)
- **Drone: Shooting** (`judge_survey12`) — โหมดยิงด้วยโดรน
- **Drone Search Mode** (`judge_survey14`) — โหมดค้นหาเบาะแส/แมวจร (ผูกความสำเร็จ `JUDGE_ALL_CATS_FOUND_IN_SEARCH_MODE`)

ที่มา: `manual.json` titles ตามที่ระบุ, `places.json` id `judge_k_playspot_drone_race`, `judge_k_playspot_drone_lab`,
`trophy.json` id `JUDGE_DRONE_OPERATOR`, `JUDGE_PLAYED_FPS_MODE_BY_DRONE`, `JUDGE_DRONE_RACE_ALL_WIN`,
`JUDGE_GET_ALL_DRONE_PARTS`

### 4.7 ระบบสกัดยา "Extract" + Onodera's Wares (ระบบเฉพาะ Judgment)

**Extract (มินิเกมคราฟต์ไอเทม):** เก็บวัตถุดิบทั่วเมือง (บางอย่างหาได้เฉพาะมุมลับ/จุดที่โดรนบินไปถึงเท่านั้น) แล้วนำไป
ผสมสูตรที่แผงของ **Iyama** ("The Hermit of the Dragon's Palace" — friend idx43) ใน Dragon's Palace — บางสูตร
ต้อง Iyama สั่งของเฉพาะ ("errand") ส่งแล้วปลดล็อกสูตรใหม่ ไม่มี precedent ระบบนี้ในภาคอื่นที่อ่านมา (ใหม่ทั้งหมด)

**Onodera's Wares:** ร้านตลาดมืดใต้ท่อระบายน้ำของ **Morio Onodera** (friend idx01) — แลกไอเทมแปลก ๆ โดยฟัง
ยากามิเล่าอดีต ("listen to me reminisce about my past") ก็เพียงพอ ไม่ใช้เงิน

**ศัพท์เสนอ:** Extract → เสนอทับศัพท์ "เอ็กซ์แทร็กต์" หรือแปล "สารสกัด/ยาลับ" (ให้ lead ตัดสินโทน — "Mystical
Extracts" ในคู่มือสื่อถึงพลังเวทย์มนตร์แฝง) · Onodera's Wares → คงชื่อ "Onodera's Wares" หรือแปล "ของออโนเดระ"

ที่มา: `manual.json` id `judge_secret_medicine0/1/2` (Extracts, Creating Extracts, Extract Ingredients) ·
`places.json` id `judge_hiyaku` ("Iyama's Extract Shop"), `judge_onodera` ("Onodera's Wares"), `judge_yamiisha`
("Moroboshi Clinic") · `friends.json` idx 1, 35, 43

### 4.8 โหมดสืบสวน/ค้นหา (ไม่ใช่มินิเกมแยก แต่เป็นกลไกที่ต้องคุมศัพท์ให้ตรงกันทุกจุด)

จาก `manual.json`/`help.json` titles: **Tailing** (การสะกดรอย — Basic Rules, Taking Cover, Tailing Search Mode),
**Disguises** (การปลอมตัว), **Chase**/**Chasing** (การไล่ล่า), **Active Search Mode**, **Quick Search Mode**,
**Photo Missions** (ภารกิจถ่ายภาพ), **Conversation: Chaining Correct Choices** (สนทนาต่อเนื่องเลือกถูก) —
ทั้งหมดนี้เป็นกลไกที่ปรากฏซ้ำในหลาย Side Case (โดยเฉพาะคดีสืบสวน/นอกใจ) ต้องแปลชื่อโหมดให้ตรงกันทุกจุดที่ปรากฏ

ที่มา: `manual.json` titles `judge_survey0`–`judge_survey16`, `help.json` id `judge_survey0`–`judge_survey16`

---

## 5. KamuroGo / ระบบภารกิจในแอป / Case File

**KamuroGo** เป็นระบบภารกิจ/ธุระย่อยผ่านแอปมือถือในเกม (คีย์ระบบยืนยันจาก `manual.json`/`help.json` id
`judge_system0` title "KamuroGo") แยกเป็น 2 ประเภทตามความสำเร็จ:
- **Shop Missions** (`JUDGE_KAMGO_SHOP_A/B/ALL` — "KamuroGo Shopper"/"Trendsetter"/"Socialite") — ธุระเกี่ยวกับร้านค้า
- **City Missions** (`JUDGE_KAMGO_COMPLETE_A/B/ALL` — "KamuroGo Tourist"/"Local"/"Guide") — ธุระทั่วเมือง

**ระบบที่เกี่ยวข้อง** (จาก `manual.json`/`help.json`):
- **Case File** (`judge_system3`) — สมุดบันทึกคดี/หลักฐาน ใช้ตามคดีหลัก+รอง
- **Map** (`judge_system1`) — ระบบแผนที่
- **Quickstarter** (`judge_system2`) — แอประดมทุน **ชื่อเดียวกับแอปในเกม Yakuza 6** (พัฒนาโดย friend idx37
  Shin Fujimori ในทั้งสองเกม — เป็นไปได้สูงว่าใช้ทรัพยากร/แนวคิดชุดเดียวกันข้ามภาค) — เสนอคงชื่อ "Quickstarter"
  ตามที่ล็อกในทีมอื่น (ยังไม่พบคำแปลไทยที่ล็อกจริงจาก Y6 — ⏳ ต้องเช็คให้แน่ใจกับทีม Y6)
- **Selfie**: How to Change Your Expression / Even More Expressions (`judge_system6`/`7`) — ระบบถ่ายเซลฟี่
- **Valuables** (`judge_system8`) — ของมีค่า/ของสะสมพิเศษ (คนละหมวดกับ item ปกติ)
- **Save** (`judge_system4`), **Bonus Content** (`judge_system5`) — ระบบทั่วไป

**ความสำเร็จสูงสุดของหมวดนี้:** `JUDGE_ALL_COMPLETE` "KamuroGo Master" — "Achieved 100% completion of KamuroGo. Wow!"

ที่มา: `help.json` id `judge_system0`–`judge_system8`, `judge_sidecase0`, `judge_friend0`, `judge_girlfriend0/1/2` ·
`trophy.json` id `JUDGE_KAMGO_*`, `JUDGE_ALL_COMPLETE` · `manual.json` titles ตรงกัน

---

## 6. ร้านค้า (46 ร้าน) และสถานที่สำคัญ

**ที่มา:** `extracted/facts/shops.json` (46 รายการทางการ, id `shop.bin`) + คำบรรยายร้านจากไฟล์ `places.json`
(182 รายการ มี field `explanation` ให้หลายร้าน — บาง id ซ้ำกันคนละ namespace เช่น `judge_k_akaushi_h` ใน shops.json
กับ `judge_k_shop_akaushi_h` ใน places.json คือร้านเดียวกัน)

### 6.1 ร้านอาหาร/เครื่องดื่ม (มีคำบรรยายในเกม)

| ร้าน | คำบรรยายย่อ |
|---|---|
| Akaushimaru (Hotel District / Tenkaichi St.) | ร้านข้าวหน้าเนื้อดั้งเดิมตั้งแต่ปี 1924 |
| Café Alps | คาเฟ่หรูตั้งแต่ปี 1971 |
| Bantam | ผับไอริช มีดาร์ทให้เล่น |
| Fuji Soba | ร้านโซบะยืนกิน แบบเชนทั่วโตเกียว |
| Gindaco Highball Tavern | บาร์ยืนดื่ม highball + ทาโกะยากิ |
| Kanrai | ร้านยากินิกุหรู |
| Kyushu No. 1 Star | ราเมงทงคตสึสไตล์คิวชู |
| Ikinari Steak | สเต๊กชิ้นใหญ่ ตัดสดหน้าออร์เดอร์ |
| M Side Cafe | คาเฟ่กลางแจ้งมี PC/ปลั๊กไฟ |
| Poppo (4 สาขา: E/W Shichifuku St., Showa St., Tenkaichi St.) | ร้านสะดวกซื้อ สินค้าต่างกันไปตามสาขา |
| Quadra Garden | คาเฟ่ในโรงแรม กาแฟบราซิล |
| Ringer Hut | ร้านจัมปงนางาซากิ |
| Smile Burger (Nakamichi St. / NW Theater Square) | เบอร์เกอร์ฟาสต์ฟู้ด |
| Sushi Gin | ซูชิร้านเล็กบน W Showa Street |
| Sushi Zanmai | ซูชินำเข้า มีโชว์แล่ปลาทูน่าสด |
| Wette Kitchen (W Taihei Blvd.) | เบอร์เกอร์แต่งเองได้ |
| Wild Jackson (E Millennium Tower St. / Tenkaichi St.) | ไก่ทอด/แซนด์วิชสไตล์ "wild" |
| Yoronotaki | ร้านยากิโทริตั้งแต่ปี 1956 |
| Don Quijote | ดิสเคาต์สโตร์เชนดัง |
| Ebisu Pawn | ร้านจำนำ |
| Le Marche | บูทีคแฟชั่นหรู |
| Café Mijore | เชนคาเฟ่ทั่วญี่ปุ่น |
| Gyu-Kaku | เชนยากินิกุใหญ่สุดในญี่ปุ่น |
| Beef Zone | ยากินิกุราคาประหยัด นักศึกษานิยม |
| Earth Angel | บาร์รับฟังเรื่องรักลูกค้า |
| Shellac | บาร์หรูสายบันเทิง |

**ศัพท์ล็อกแล้วจากภาคก่อน (glossary_k2 §8):** Poppo → **ป๊อปโป** · Don Quijote → **คงชื่ออังกฤษ "Don Quijote"**
(K3 ตัดสิน 14 ส.ค. 2026 ให้ยกเลิกทับศัพท์เก่า "ดอนกิโฮเต้") · Café Alps → **คาเฟ่อัลป์ส** · Fuji Soba, Gyu-Kaku,
Kanrai, Ikinari Steak, Ebisu Pawn, Shellac → ทับศัพท์ตามเสียงญี่ปุ่น (ยังไม่มีคำไทยแบบเป๊ะจาก K2 — ต้องเสนอใหม่
ตามแนวเดียวกัน)

### 6.2 สถานที่เล่น/ธุรกิจกลางคืน (มีคำบรรยาย)

Club Amour (คลับ+บาร์ Suppon St.), Sauna Goten (ซาวน่า Senryo Ave.), Koi Bride (บ่อตกปลาในร่ม — เชื่อม A42),
Cabaret Honmaruen, The Queen Rouge (คาบาเรต์คลับ 2 แห่ง — **⏳ ไม่พบ manual/minigame bin เฉพาะระบบคาบาเรต์คลับ
แบบ K2R Cabaret Club Grand Prix ในข้อมูลที่สำรวจรอบนี้ — อาจเป็นแค่สถานที่ประกอบฉาก ไม่ใช่ระบบเกมแยก ต้องยืนยันเพิ่ม**),
Cho-han Gambling Hall (ต้องรหัสผ่านเข้า), Game Center Charles (เกมตู้เรโทร), Bar Tender (ร้านของ Jo Masuda —
ฐานรับ Side Case), Matsugane Family Office, Genda Law Office, Yagami Detective Agency, Konban Wife (นวดเชิงอีโรติก),
Kamuro Lock & Key (ร้านกุญแจของ Toshiro Koizuka — friend idx42)

**ศัพท์เสนอ:** cho-han → **โจฮัง** (ล็อกแล้ว glossary_k2 §4 ตาม PIRATE) — ยืนยันมีระบบนี้จริงใน Judgment
(`judge_k_building_toba` "Cho-han Gambling Hall" + `judge_k_playspot_toba` "Gambling Hall (Dragon's Palace)")

ที่มา: `places.json` id ตามที่ระบุ (มี `explanation` ครบทุกรายการที่กล่าวถึง)

### 6.3 ถนน/ย่านหลัก — ตรงกับภาคอื่นในจักรวาลเดียวกันทั้งหมด (ศัพท์ล็อกแล้ว)

| ชื่อ EN | คำไทยล็อกแล้ว (K3 glossary.md) |
|---|---|
| Kamurocho | คามุโรโจ |
| Tenkaichi Street | ถนนเทนไคจิ |
| Senryo Avenue | ถนนเซ็นเรียว |
| Pink Street | ถนนพิงก์สตรีท |
| Champion District | ย่านแชมเปียน |
| Theater Square | เธียเตอร์สแควร์ |
| Millennium Tower | มิลเลนเนียมทาวเวอร์ |
| Bantam | แบนตัม |

ถนน/ย่านอื่นที่มีใน Judgment แต่ยังไม่เจอคำล็อกตรงจากภาคก่อน (ต้องเสนอใหม่ตามแนวทับศัพท์เดียวกัน): Showa St.,
Shichifuku St. (E/W), Nakamichi St., Taihei Blvd. (E/W), Suppon St., Little Asia, Hotel District, Park Boulevard

ที่มา: `places.json` id `judge_k_street_*` (ครบทุกถนนที่ปรากฏ), เทียบกับ `D:/Projects/yakuza-kiwami-3/translations/glossary.md`

---

## 7. ระบบเก็บ Completion (`complete.json` 499 + `complete_group.json` 34)

`complete_group.json` คือสารบัญหมวดของ side content ทั้งเกม (34 หมวด) — ใช้เป็น "แผนที่" ตรวจสอบว่าแปลครบทุกระบบ
หรือยัง รายชื่อหมวดที่ยืนยันจากไฟล์จริง (`complete_group.json`, idx 1–34): Café Mijore, Smile Burger, Akaushimaru,
M Side Cafe, Bantam, Kanrai, Kyushu No. 1 Star, Sushi Gin, Café Alps, Quadra Garden, Fuji Soba, Wild Jackson,
Yoronotaki, Gindaco Highball Tavern, Ringer Hut, Sushi Zanmai, Wette Kitchen, Ikinari Steak, Earth Angel, Shellac,
Gyu-Kaku, Beef Zone, **Batting Center**, Club SEGA (Nakamichi St.), Club SEGA (Theater Square), Lullaby Mahjong,
Modern Mahjong, Tachibana Mahjong, **Drone League**, **Drone Lab**, **Paradise VR**, Charles, **Dragon's Palace**,
**Outdoor Shogi**

**ยอด completion ระดับ 3 ขั้นแบบเดียวกันทุกหมวด** (พบใน `complete.json`): Talk to People (Affable/Popular/Talk of
the Town), Eat at Restaurants (Big Eater/Glutton/Connoisseur), Make Money (Millionaire/Multimillionaire/Triple
Multimillionaire), Walk distance (Mini Marathon Man) — ระบบนี้เป็น "ป้าย 3 ระดับ" มาตรฐานของเกม เหมือนกันทุกหมวด
วัดจากจำนวนครั้งสะสม (`${need_player_point_value}`)

ที่มา: `extracted/facts/complete_group.json` (ครบ 34), `extracted/facts/complete.json` (ตัวอย่าง idx 318–331)

---

## 8. สกิล/ระบบต่อสู้ (126 สกิล จาก `skills.json`)

**สไตล์การต่อสู้ 2 แบบ** (ยืนยันข้อความเต็มจาก `manual.json` id `judge_battle6`, title "Change Styles"):
> "Over the years, Yagami has mastered two distinct combat styles, **Crane** and **Tiger**, which he can switch
> between at any time."
- **Crane Style** (สีน้ำเงินในเกม) — เก่งกับศัตรูหมู่ ท่าเร็ว ครอบคลุมพื้นที่กว้าง มี EX Action สำหรับกลุ่มเยอะ
- **Tiger Style** (สีแดงในเกม) — เก่งกับศัตรูเดี่ยว ท่าหนักทะลวงการ์ด มี EX Action สำหรับดวลตัวต่อตัว

**ศัพท์สกิลที่พบ:** Charging Tiger, Tiger Drop, Balance of the Tiger, Elegance of the Tiger, Ferocity of the
Tiger, Flux Fissure (ทั้งหมดเฉพาะ Tiger Style) · EX Tiger Dances With Crane (ท่าพิเศษรวม 2 สไตล์)

**ระบบ EX Action (Heat Action):** มีมากกว่า 80 ท่า (จาก `help.json` id `judge_hact0`–`judge_hact77` + Heat Action
20–80 ใน `manual.json`) รวมถึง **EX Bond** 13 ท่า ผูกกับเพื่อนสนิทเฉพาะคน (ดูหัวข้อ 2 ใน part1) — ต้องแปลชื่อท่าให้
สอดคล้องกับชื่อเพื่อนที่ผูกท่านั้น (เช่น "EX Bond: Manager Yoshida" ต้องใช้ชื่อ Yoshida เดียวกับระบบเพื่อน)

**ระบบ Threat Level / Keihin Gang:** ผูกกับ Side Case A32 — สู้เยอะเกินจะเจอ "Threat Level"/"Maximum Threat
Level" (ทีมแก๊ง Keihin ไล่ล่า) เป็นกลไกเฉพาะช่วงคดีนั้น

ที่มา: `manual.json` id `judge_battle0`–`judge_battle15`, `judge_skill0`–`3` · `skills.json` (126 รายการเต็ม) ·
`help.json` id `judge_hact0`–`77`, `judge_battle11`–`13`

---

## 9. ศัพท์ที่ยืมจากภาคก่อน (ล็อกแล้ว)

| คำ EN | คำไทยล็อกแล้ว | ที่มา/ลำดับความสำคัญ |
|---|---|---|
| Kamurocho | คามุโรโจ | K3 glossary.md |
| Tenkaichi Street | ถนนเทนไคจิ | K3 glossary.md |
| Senryo Avenue | ถนนเซ็นเรียว | K3 glossary.md |
| Pink Street | ถนนพิงก์สตรีท | K3 glossary.md |
| Champion District | ย่านแชมเปียน | K3 glossary.md |
| Theater Square | เธียเตอร์สแควร์ | K3 glossary.md |
| Millennium Tower | มิลเลนเนียมทาวเวอร์ | K3 glossary.md |
| Bantam | แบนตัม | K3 glossary.md |
| Café Alps | คาเฟ่อัลป์ส | K3 glossary.md |
| Poppo | ป๊อปโป | glossary_k2 §8 |
| Don Quijote | คงอังกฤษ "Don Quijote" | K3 ตัดสิน 14 ส.ค. 2026 (ยกเลิกทับศัพท์เดิม) |
| shogi | โชกิ | glossary_k2 §4 |
| koi-koi | โคอิ-โคอิ (มีขีด) | K3 ตัดสิน 14 ส.ค. 2026 |
| oicho-kabu | โออิโช-คาบุ | glossary_k2 §4 ตาม PIRATE |
| cho-han | โจฮัง | glossary_k2 §4 ตาม PIRATE |
| karaoke | คาราโอเกะ (เพลง/เนื้อร้องคงอังกฤษ) | glossary_k2 §4 |
| pon / chii / kan / tsumo / ron / riichi / dora / han / fu | ปง / ชิ / คัง / สึโม (จั่วเอง) / รอน / รีช / โดระ / ฮัง / ฟุ | K3 side_content_context_k3.md §2.1 |
| mangan / haneman / baiman / sanbaiman / yakuman | มังกัง / ฮาเนมัง / ไบมัง / ซันไบมัง / ยากุมัง | K3 side_content_context_k3.md §2.1 |
| Virtua Fighter (ทุกภาค), Fantasy Zone, Space Harrier, UFO Catcher, Puyo Puyo, Club SEGA | คงอังกฤษ | K2/Y6/Y7/Y8 ทุกภาคตรงกัน |
| DARTSLIVE | คงอังกฤษ | glossary_k2 §0 |
| golf → กอล์ฟ | (ไม่ยืนยันว่า Judgment มีกอล์ฟ — ไม่พบใน manual.json titles) | glossary_k2 §4 (สำรอง ถ้าเจอภายหลัง) |
| Masaharu Kaito | มาซาฮารุ ไคโตะ | glossary_gaiden (ล็อกแล้วก่อนเริ่มโปรเจกต์นี้) |

---

## 10. ศัพท์ใหม่ที่ต้องตั้ง (เสนอ + เหตุผล)

| คำ EN | proposal | เหตุผล |
|---|---|---|
| Extract (ระบบสกัดยา) | "เอ็กซ์แทร็กต์" (ทับศัพท์) หรือ "สารสกัดลับ" | ไม่มี precedent ระบบนี้ในภาคอื่น — ระบบใหม่เฉพาะ Judgment ผูกกับตัวละคร Iyama ผู้ใช้คำว่า "magic"/"mystical" ปนอยู่ในคำอธิบาย จึงเสนอคำที่สื่อถึงเวทมนตร์แฝงเล็กน้อย |
| Onodera's Wares | คงชื่ออังกฤษ หรือ "ร้านของออโนเดระ" | ชื่อร้านเฉพาะตัวละคร friend_001 — ไม่มี precedent ร้านใต้ดินแบบนี้ในภาคอื่นที่ตรงกัน |
| Paradise VR | คงอังกฤษ "Paradise VR" | ชื่อสถานที่เฉพาะ ไม่มีระบบ VR sugoroku ในภาคอื่นที่อ่านมาให้เทียบ |
| Dice & Cube | คงอังกฤษ "Dice & Cube" | ชื่อเกมเฉพาะภายใน Paradise VR — เหตุผลเดียวกับด้านบน |
| Drone League | "ดี-ลีก" (ตามที่ trophy.json ย่อว่า "D-League" ในบาง achievement) หรือ "ลีกโดรน" | ระบบแข่งโดรนใหม่เฉพาะ Judgment — ควรเช็คว่าเกมเรียกย่อว่า "D-League" บ่อยแค่ไหนก่อนเลือกทับศัพท์ |
| Twisted Trio (ชื่อกลุ่มคดี A01–A04) | "สามโรคจิต" หรือคงอังกฤษ "Twisted Trio" | ชื่อกลุ่มคดีที่ผู้เล่นเห็นซ้ำ ๆ ในเมนู Side Case — ควรเลือกให้ฟังดูขบขันสมโทนคดี ไม่ใช่น่ากลัว |
| KamuroGo | คงอังกฤษ "KamuroGo" | ชื่อแอปเฉพาะ Judgment (ล้อคำ "Pokémon GO"/GPS app) แปลจะเสียมุกชื่อ |
| Quickstarter | คงอังกฤษ "Quickstarter" (รอยืนยันกับทีม Y6) | ชื่อแอประดมทุนที่ปรากฏทั้งใน Judgment และ Y6 — ควรใช้คำเดียวกันถ้า Y6 มีคำแปลอยู่แล้ว |

---

## 11. สิ่งที่ยังค้าง ⏳

1. **ชื่อคดี A29/A30 ขัดแย้งกันระหว่าง journal กับป้ายความสำเร็จ** ("Master and Pupil" vs "The Circle of Law",
   "The Pigeon Takes Flight" vs "The Bird Takes Flight") — ต้อง verify กับ case-file UI string จริงตอนเข้าเกม
2. **Sana Omura (girlfriend list) vs Sana Mihama (friends list)** — นามสกุลไม่ตรงกัน ต้อง verify จาก talk/UI string
3. **ระบบคาบาเรต์คลับ** (Cabaret Honmaruen, The Queen Rouge) — พบแค่คำบรรยายสถานที่ใน `places.json` ไม่พบ
   `manual.json`/minigame bin เฉพาะ — ยังไม่ยืนยันว่ามีระบบเกมแยกแบบ K2R Cabaret Club Grand Prix หรือเป็นแค่ฉาก
4. **Fighting Vipers, Motor Raid** — ยืนยันแค่ชื่อจาก manual.json title ยังไม่ได้อ่านเนื้อหากติกาละเอียด
5. **Karaoke, Girlfriend Topic Talks/Presents/Once It's Official** — manual.json มีแค่ title ไม่มี `table.*`
   เนื้อหา กติกาละเอียด ⏳ ต้องอ่านจาก UI/talk string อื่นตอน sprint
6. **กติการะดับสนิทของระบบ Friends** (ปลดล็อกอะไรตามลำดับ, มีกี่ระดับ) — ไม่พบข้อมูลยืนยันจากไฟล์ facts ที่สำรวจ
7. **Quickstarter (แอปเดียวกับ Y6 หรือไม่)** — ต้องให้ทีม Y6 ยืนยันว่ามีคำแปลไทยล็อกไว้แล้วหรือยัง
8. **Drone League ย่อว่า "D-League" ในเกมบ่อยแค่ไหน** — ต้องสำรวจ `ui_text.json`/`talk_select.json` เพิ่มก่อนล็อกศัพท์
9. **ถนน/ย่านที่ยังไม่มีคำแปลล็อกจากภาคก่อน** (Showa St., Shichifuku St., Nakamichi St., Taihei Blvd., Suppon St.
   ฯลฯ) — ต้องเสนอชุดใหม่ให้ lead ตัดสินพร้อมกันในรอบ glossary freeze
10. **ป้ายชื่อร้าน 20 กว่าร้านที่ยังไม่มีคำไทยล็อกจากภาคก่อน** (Fuji Soba, Gyu-Kaku, Kanrai, Ikinari Steak,
    Ebisu Pawn, Shellac, Gindaco Highball Tavern, Ringer Hut, Wette Kitchen, Wild Jackson, Yoronotaki,
    Le Marche, Café Mijore, Quadra Garden, Beef Zone, Earth Angel ฯลฯ) — เสนอทับศัพท์ตามเสียงญี่ปุ่น/อังกฤษต้นฉบับ
    รอ lead ตัดสินพร้อมกันเป็นชุด
