# Glossary — JETH (Judgment)

> §0 กติกา · §1 ชื่อเฉพาะยืมจากซีรีส์ · §2 ตัวละครหลักที่ล็อกแล้ว · §3 ศัพท์กฎหมาย/สืบสวน ·
> §4 องค์กร/สถานที่เฉพาะ Judgment · §5 ศัพท์ระบบเกม · §6 ยาเสพติด/คดี · §7 ชื่อตัวละครหลัก ·
> §8 ข้อขัดแย้งที่ต้อง lead ตัดสิน · §📇 ตารางเทอมอ่านโดยเครื่อง
> (lead merge สอง part เป็นไฟล์เดียวแล้ว 20 ส.ค. 2026)

สถานะ: **ร่างแรก** (20 ส.ค. 2026) — ยังไม่ freeze รอ lead ตัดสินรายการที่ทำเครื่องหมาย ⏳ และข้อขัดแย้งใน §8
ลำดับความสำคัญเมื่อภาคเก่าขัดกัน: **K3 > Gaiden > Y8 > Y7 > Pirate > K2R** (ใหม่กว่าชนะ)
ไฟล์อ้างอิงเต็ม: `D:/Projects/yakuza-kiwami-3/translations/glossary.md` +
`D:/Projects/yakuza-kiwami-3/docs/reference/glossary_{gaiden,y8,y7,pirate,k2}.md` +
`D:/Projects/yakuza-kiwami-3/docs/reference/glossary_honorifics_y5.json` (ศัพท์ยากูซ่า/honorific อธิบายละเอียด)

ที่มาข้อเท็จจริงของ Judgment เอง: `docs/reference/judge_extract_facts.md` +
`extracted/facts/{evidence,missions,places,chapters,friends,help,skills}.json`
(ทุกชื่อ/องค์กรในไฟล์นี้ verify กับไฟล์เกมจริงแล้ว เว้นแต่ทำเครื่องหมาย ⏳)

## §0 กติกา (สืบทอดจาก K3 ทั้งชุด)
- tag/placeholder ต้องตรงเป๊ะ: `${...}`, `<color=...>`, `<symbol=...>`, `%s/%d`, จำนวน `\n`
- ชื่อเฉพาะทับศัพท์ตามหลักที่ล็อกในภาคเก่า — เจอชื่อใหม่ห้ามตั้งเอง จดลง new_names ให้ lead ตัดสิน
- honorifics ตาม EN ตรงตัวสองทาง: EN มี `-san` → ซัง / ไม่มี → ไม่เติม · `-chan` → จัง · `-kun` → คุง · `-sama` → ท่าน/ซามะ
- หลักทับศัพท์สืบทอด: **g กลางคำ = ก** (ยากามิ, เก็นดะ, มัตสึกาเนะ) · **-ei ท้ายพยางค์ = เ-ย์** (เคียวเฮย์, อิสเซย์, เรย์) · **ki ท้ายชื่อ = กิ** · **zu = ซึ** · ชินเป/ชิเงรุ/ฟุยุฮิโกะ/เคโกะ เป็นรูปที่ล็อกแล้วจากภาคอื่น ใช้ตรงกันเมื่อพยางค์เหมือนกัน
- **ห้าม Cyrillic ในคำแปล** (ชน donor slot ฟอนต์ไทย) — Latin-1 (é ü) ใช้ได้ปกติแต่ระวังชน donor pool (ดู `docs/research.md` §5)
- license/EULA/credits คงอังกฤษ · เลขอารบิกเท่านั้น
- คำตัดสินใหม่ให้จดพร้อมวันที่+เหตุผลก่อนย้ายขึ้นตารางหลัก (โครงเดียวกับ K3 §คำตัดสิน — ยังไม่เปิดใช้เพราะยังไม่ freeze)

---

## §1 ชื่อเฉพาะยืมจากซีรีส์ (LOCKED — สืบทอดจากภาคก่อน ห้ามตั้งใหม่)

### สถานที่ในคามุโรโจ (ยืนยันซ้ำว่ามีจริงใน `places.json`/`missions.json` ของ Judgment)
| EN | ไทย | ที่มา | หมายเหตุ |
|---|---|---|---|
| Kamurocho | คามุโรโจ | ซีรีส์ (K3 §1) | เมืองหลักของเกม |
| Tojo Clan | ตระกูลโทโจ | K3 §1 (Y7) | Matsugane Family เป็นตระกูลลูก (subsidiary) ของโทโจ — ยืนยันจาก evidence.json |
| Tenkaichi Street | ถนนเทนไคจิ | K3 §📇 | places.json: "Tenkaichi First Building" ฯลฯ |
| Millennium Tower | มิลเลนเนียมทาวเวอร์ | K3 §📇 | places.json ยืนยันชื่อเดียวกันเป๊ะ |
| New Serena | นิวเซเรน่า | K3 §📇 | places.json ยืนยันชื่อเดียวกันเป๊ะ |
| Poppo | ป๊อปโป | K3 wave9 (กวาด ป็อปโป้→ป๊อปโป) | ร้านสะดวกซื้อ — Judgment มีหลายสาขา (Showa St./Tenkaichi St./E,W Shichifuku St.) |
| Don Quijote | คง EN | K3 wave10 | ร้านดิสเคานต์ — ห้ามทับศัพท์ "ดอนกิโฮเต้" |
| Café Alps / Caf​é Alps | คาเฟ่อัลป์ส | K3 (TALK_028-048) / Y7 | ตัด é ตามกฎอักษรชน donor slot |
| Theater Square | เธียเตอร์สแควร์ | K2R/Y7/K3 | Judgment: "Club SEGA (Theater Square)" |
| Bantam | แบนตัม | K3 wave10 | ผับไอริช — Judgment: "Bantam" (บาร์) + "DARTSLIVE (Bantam)" |
| Pink Street | ถนนพิงก์สตรีท | K3 §1 / Y7 | ⚠ Judgment มี "Pink Alley" (ตรอก/ซอยพิงค์) — คนละชื่อที่ตั้ง ดู §8 |

### ศัพท์ยากูซ่า (ตารางเต็ม+อธิบาย: `glossary_honorifics_y5.json`)
| EN | ไทย | ที่มา | หมายเหตุ |
|---|---|---|---|
| Aniki (คำเรียก) | ลูกพี่ | เจ้าของสั่ง 27 ก.ย. 2026 (เดิม อานิกิ ตาม K3 §1) | ห้ามทับศัพท์ "อานิกิ" อีก · ติดชื่อ = ลูกพี่+ชื่อ (Kaito-aniki → ลูกพี่ไคโตะ · Higashi-aniki → ลูกพี่ฮิงาชิ) · ติดอ่าง A-Aniki → ล-ลูกพี่ · กวาดด้วย `scripts/fix_owner_terms.py` |
| Kyodai | เคียวได | Pirate/K3 §1 | พี่น้องร่วมสาบาน (ศักดิ์เท่ากัน ต่างจาก aniki/kobun) |
| Kumicho | คุมิโช (ทับศัพท์) / ประธานตระกูล | glossary_honorifics_y5 | ตำแหน่งประธานสูงสุดระดับสมาพันธ์ |
| Oyabun | โอยาบุน (ทับศัพท์) / หัวหน้าครอบครัว | glossary_honorifics_y5 | หัวหน้าครอบครัวย่อย |
| Wakagashira | วากางาชิระ / รองประธาน | glossary_honorifics_y5 | มือขวาอันดับหนึ่ง |
| Kobun | โคบุน / ลูกน้อง | glossary_honorifics_y5 | ลูกน้องทั่วไป |
| Shatei | ชาเท / น้องเล็ก | glossary_honorifics_y5 | คู่ตรงข้าม aniki |
| Family (ตระกูลยากูซ่า) | ตระกูล | K3/Y7 ทั้งชุด | ใช้กับ Matsugane Family, Kyorei Clan ฯลฯ — "Clan" แปล "ตระกูล" เหมือนกัน (Kyorei Clan ก็ใช้ "ตระกูล" ไม่ใช่ "แคลน") |

### ระบบต่อสู้ที่ล็อกข้ามภาค
| EN | ไทย | ที่มา | หมายเหตุ |
|---|---|---|---|
| Style (ต่อท้ายชื่อสไตล์ต่อสู้) | **ท่า** (เฉพาะสไตล์ต่อสู้ของยากามิ) | lead ตัดสิน 20 ส.ค. 2026 | Crane/Snake/Tiger Style → **ท่ากระเรียน / ท่างู / ท่าเสือ** · ⚠ ต่างจากคำล็อก Y7 (`glossary_y7.md:298` ใช้ "สไตล์") — lead เลือกคำไทยล้วนสำหรับภาคนี้ ดู §8 ข้อ 6 |
| EX Gauge | เกจ EX | Y7 (ถอนคง EN แล้ว 6 ส.ค. 2026 — 9/9 จุดใช้ "เกจ EX") | Judgment ใช้ EX Gauge จริง (ไม่มีระบบ Heat — engine ยุคนี้เปลี่ยนมาใช้ EX แทน Heat ทั้งหมด ยืนยันจาก skills.json ไม่พบคำว่า "Heat" เลย) |
| Tiger Drop | ไทเกอร์ดรอป | K3 wave12 (ตาม Y7 "โคมากิ ไทเกอร์ดรอป") | Judgment มีสกิลชื่อ "Tiger Drop" ตรงตัว (skills.json idx 50) — ท่าเคาน์เตอร์ในตำนาน |

---

## §2 ตัวละครหลักที่มีคำล็อกข้ามภาคแล้ว (สำคัญที่สุด — freeze แล้วโดยคำตัดสิน lead 20 ส.ค. 2026)

**Judgment มีคาแรกเตอร์ที่เคยรับเชิญทั้งใน Like a Dragon Gaiden (ฉากโคลอสเซียม) และใน Yakuza 7
(tranche 18/20) — คำเหล่านี้ "ล็อกจริง" ไม่ใช่แค่ข้อเสนอ เพราะ ship ไปแล้วในทั้งสองภาค
เมื่อ Gaiden กับ Y7 สะกดต่างกัน lead ตัดสินให้ใช้รูปไหนไว้ในคอลัมน์ที่มา (คำตัดสิน 20 ส.ค. 2026)**

| EN | ไทย | ที่มา | หมายเหตุ |
|---|---|---|---|
| Yagami (นามสกุล) | **ยากามิ** | **glossary_gaiden.md:80,256** (ship แล้ว — lead Gaiden เคยแก้ "ยากามิ"→"ยากามิ" มาแล้ว 2 จุด ตามกฎ g กลางคำ=ก) | ⚠⚠ ดู §8 — ขัดกับ "ยากามิ" ที่ปรากฏใน CLAUDE.md/บรีฟของโปรเจกต์นี้เอง — **ยากามิ (ก) คือรูปที่ freeze แล้ว** ยืนยันซ้ำโดยคำตัดสิน lead 20 ส.ค. 2026 |
| Takayuki Yagami | ทาคายูกิ ยากามิ | ประกอบจากล็อก + หลักทับศัพท์มาตรฐาน | ตัวเอก อดีตทนาย ผันตัวเป็นนักสืบเอกชน — evidence.json idx 52 |
| Yagami Detective Agency | สำนักงานนักสืบยากามิ | **glossary_gaiden.md:257** (ship แล้วในบท Gaiden 10+ จุด) | help.json ก็มีหัวข้อนี้ตรงตัว |
| Masaharu Kaito | มาซาฮารุ ไคโตะ | **glossary_gaiden.md:143** (ship แล้ว) | หุ้นส่วนนักสืบของยากามิ — evidence.json idx 36 ยืนยันแบ็กกราวนด์ตรงกับ Gaiden (อดีตยากูซ่าตระกูลมัตสึกาเนะ ถูกไล่ออกเพราะทำเงิน 100 ล้านเยนหาย) |
| Toru Higashi | โทรุ ฮิงาชิ | **glossary_gaiden.md:21794** (ship แล้ว: "Toru Higashi": "โทรุ ฮิงาชิ") | ⚠ CLAUDE.md เดิมของโปรเจกต์นี้เข้าใจผิดว่ายังไม่ถูกล็อก — ที่จริงล็อกแล้วจาก Gaiden (ฉาก "Kaito. And this here's Higashi." = ไคโตะ แล้วนี่คือฮิงาชิ) — สมาชิกตระกูลมัตสึกาเนะ, evidence.json idx 41 |
| Higashi (เรียกลอย) | ฮิงาชิ | glossary_gaiden.md:8962 | ใช้ทับศัพท์ตรงเป๊ะกับ Gaiden |
| Matsugane (นามสกุล/ตระกูล) | **มัตสึกาเนะ** (ไม่มี ะ ท้าย) | **glossary_y7.md:812 — คำตัดสิน lead 20 ส.ค. 2026** ("Matsugane Family→ตระกูลมัตสึกาเนะ" tranche 20) | ⚠⚠ **แก้จากรูปเดิม "มัตสึกาเนะ" ที่อ้าง Gaiden** — Gaiden ship ไว้ว่า "มัตสึกาเนะ" (ก+ะ) แต่ lead ตัดสินให้ใช้รูป Y7 "มัตสึกาเนะ" (ง ไม่มี ะ) แทนทั้งชุด ดู §8 |
| Matsugane Family | **ตระกูลมัตสึกาเนะ** | **glossary_y7.md:812 — คำตัดสิน lead 20 ส.ค. 2026** | ตระกูลลูกของโทโจ — องค์กรหลักของเนื้อเรื่อง Judgment |
| Kyorei Clan | ตระกูลเคียวเรอิ | **glossary_gaiden.md** ("Kyorei Clan Hand-Clap Boss"→"หัวหน้าปรบมือตระกูลเคียวเรอิ") + **glossary_y7.md:445 tranche 18** ("Kyorei Clan→ตระกูลเคียวเรอิ") — สองภาคสะกดตรงกัน ไม่มีข้อขัดแย้ง | แก๊งสายคันไซที่ตั้งฐานในคามุโรโจ (evidence.json: Satoshi Shioya เป็นกัปตัน/captain) |
| Mafuyu (ชื่อตัว) | มาฟุยุ | **glossary_y7.md:445 tranche 18** ("Mafuyu→มาฟุยุ") | ตรงกับที่เสนอไว้ใน §7 พอดี (Mafuyu Fujii) — ยืนยันเป็นคำล็อกแล้ว ไม่ใช่แค่ข้อเสนอ |
| Kuroiwa (นามสกุล) | คุโรอิวะ | **glossary_y7.md:445 tranche 18** ("Kuroiwa→คุโรอิวะ") | ตรงกับที่เสนอไว้ใน §7 พอดี (Mitsuru Kuroiwa) — ยืนยันเป็นคำล็อกแล้ว ไม่ใช่แค่ข้อเสนอ |
| Genda-sensei | อาจารย์เก็นดะ (เดิม เก็นดะเซนเซ — เจ้าของโปรเจกต์สั่งเปลี่ยน 5 ก.ย. 2026) | **glossary_y7.md:446 tranche 18** ("Genda-sensei→เก็นดะเซนเซ") | คนละตัวละครกับ Ryuzo Genda ของ Judgment แต่ยืนยันการอ่านนามสกุล "Genda"→เก็นดะ ตรงกัน (ใช้ต่อใน §4) |
| "the Mole" (โค้ดเนม) | **ไอ้ตัวตุ่น** (เดิม ไส้ศึก ตาม glossary_y7 tranche 18) | เจ้าของสั่ง 28 ก.ย. 2026 | ชื่อ JA คือ モグラ (ตัวตุ่น) — ยากามิตั้งเพราะคนร้าย "หายลับไปในความมืด" เหมือนตุ่นมุดดิน ไม่ใช่ความหมาย "สายลับ" ของ mole ใน EN · ไส้ศึก ยังชี้นำว่าคนร้ายเป็นคนใน = สปอยล์คุโรอิวะ · "หาตัว/จับตัว the Mole" = หา/จับไอ้ตัวตุ่น (ไม่ใช่ ตัวไอ้ตัวตุ่น) · กวาดด้วย `scripts/fix_owner_terms.py` |

---

## §3 ศัพท์กฎหมาย/สืบสวน — จุดเด่นเฉพาะภาคนี้ (⏳ เสนอใหม่ทั้งหมด ยังไม่เคยมีภาคไหนต้องแปล)

ยืนยันจากไฟล์เกมจริงว่ามีบริบทเหล่านี้: `evidence.json`, `missions.json`, `items.json`
(ดูคำพูดต้นฉบับที่อ้างอิงในคอลัมน์หมายเหตุ)

| EN | ไทย (เสนอ) | หมายเหตุ |
|---|---|---|
| lawyer / attorney | ทนายความ (สั้น: ทนาย) | evidence.json: "Yagami was a proper lawyer who worked at the Genda Law Office" |
| defense attorney | ทนายฝ่ายจำเลย / ทนายแก้ต่าง | "Ayabe requests Yagami to be his attorney" |
| prosecutor | อัยการ | "A public prosecutor from the Tokyo Public Prosecutor's Office" |
| Chief Prosecutor | หัวหน้าอัยการ | ตำแหน่งของ Kunihiko Morita — "Chief Prosecutor Morita" |
| Public Prosecutor's Office | สำนักงานอัยการ | — |
| Tokyo Public Prosecutor's Office | สำนักงานอัยการโตเกียว | evidence.json ใช้คำนี้ตรงตัวหลายจุด |
| indictment | การฟ้องร้อง / คำฟ้อง | ⏳ ยังไม่เจอบริบทตรงในไฟล์ที่ extract แล้ว — คำสำรองตามหลักกฎหมายไทยทั่วไป |
| verdict | คำตัดสิน / คำพิพากษา | "not long after the verdict, Okubo was arrested..." |
| acquittal / found innocent | พ้นผิด / ได้รับการยกฟ้อง | "he was later found innocent" |
| conviction | การตัดสินว่ามีความผิด | — |
| conviction rate 99.9% | อัตราการตัดสินลงโทษ 99.9% | ⏳ ยังไม่เจอบริบทตรงในไฟล์ที่ extract แล้ว — ทีมต้อง grep talk.bin.json/sound_auth.bin.json ต่อตอนแปลจริง (คำขึ้นชื่อของระบบยุติธรรมญี่ปุ่นที่เกมอาจพูดถึง) |
| retrial | การไต่สวนใหม่ / การพิจารณาคดีใหม่ | "he once again pleaded innocent throughout this second trial" (Okubo) |
| trial | การพิจารณาคดี / การไต่สวน | "won the trial", "his previous trial" |
| detective (ตำรวจ) | นักสืบ | **locked จาก glossary_y8.md:303** |
| private investigator / PI | นักสืบเอกชน | ยากามิ+ไคโตะเป็นนักสืบเอกชน |
| investigator | นักสืบ / ผู้สืบสวน | evidence.json: Kaito "working as an investigator at the Yagami Detective Agency" |
| client (ลูกความทนาย) | ลูกความ | items.json: "Genda's client. She's battling her husband for custody..." |
| client (ลูกค้าทั่วไป) | ลูกค้า | ตามบริบท — ระวังสับสนกับ client ด้านกฎหมาย |
| evidence | หลักฐาน | ชื่อระบบเกมด้วย (ดู §5 Case File) |
| testimony | คำให้การ / คำเบิกความ | "Shono's testimony was a lie" (talk_select.json) |
| alibi | **พยานที่อยู่** | lead ตัดสิน 20 ส.ค. 2026 — ศัพท์กฎหมายไทยจริง เข้ากับบทอัยการ/ทนายซึ่งเป็นแกนของเกม · ห้ามใช้ทับศัพท์ "อาลิไบ" |
| warrant | หมายจับ / หมายค้น | ตามบริบท (ยังไม่เจอบรรทัดตรงในไฟล์ที่ extract แล้ว) |
| custody (ควบคุมตัวผู้ต้องสงสัย) | การควบคุมตัว | ตามบริบท |
| custody (สิทธิ์เลี้ยงดูบุตร) | สิทธิ์ปกครองบุตร | items.json: "battling her husband for custody over their daughter" — **คนละความหมายกับข้างบน ห้ามปนกัน** |
| Bar Association | เนติบัณฑิตยสภา / สภาทนายความ | ⏳ ยังไม่เจอบริบทตรง — เตรียมไว้เผื่อพูดถึงใบอนุญาตว่าความของยากามิ |
| disbarred / disbarment | ถูกเพิกถอนใบอนุญาตว่าความ | ⏳ เผื่อพูดถึงสาเหตุที่ยากามิเลิกเป็นทนาย |
| suspect | ผู้ต้องสงสัย | evidence.json ใช้เป็น tag ทุกคดี "(Suspect)" |
| culprit | ผู้ก่อเหตุ / ตัวการ | ใช้บ่อยในบทสนทนาสืบสวน |
| "The Mole" (โค้ดเนมผู้ร้ายลับที่ยังไม่เผยตัว) | ไอ้ตัวตุ่น | เจ้าของสั่ง 28 ก.ย. 2026 (ดูแถว "the Mole" ข้างบน) · evidence.json idx 34/48 "The Mole (Suspect)" = ไอ้ตัวตุ่น (ผู้ต้องสงสัย) |
| innocent | บริสุทธิ์ / พ้นผิด | — |
| guilty | มีความผิด | — |

---

## §4 องค์กร/สถานที่เฉพาะ Judgment (ยืนยันจากไฟล์เกมจริง — ทั้งหมด ⏳ เสนอใหม่)

| EN | ไทย (เสนอ) | ที่มา/หมายเหตุ |
|---|---|---|
| Genda Law Office | สำนักงานกฎหมายเก็นดะ | help.json มีหัวข้อนี้ตรงตัว · Genda→เก็นดะ ใช้ตามรูปที่ล็อกไว้แล้วใน Y7 ("Genda-sensei"→"เก็นดะเซนเซ" — คนละตัวละคร แต่นามสกุลอ่านเสียงเดียวกัน) |
| Ryuzo Genda | ริวโซ เก็นดะ | อดีตนายจ้างของยากามิ, evidence.json idx 54 |
| Matsugane Family Office | สำนักงานตระกูลมัตสึกาเนะ | evidence.json: "100 million yen that was stolen from the Matsugane Family Office" |
| Advanced Drug Development Center (ADDC) | ศูนย์พัฒนายาขั้นสูง (ตัวย่อคง ADDC) | evidence.json/places.json ยืนยันชื่อเต็ม+คำย่อ ADDC ใช้สลับกันตลอดเกม — เสนอแปลชื่อเต็มครั้งแรกแล้วใช้ตัวย่อ ADDC ต่อ (คง EN ตามด้วยเกมเองก็ใช้ตัวย่อ) |
| AD-9 | AD-9 (คง EN) | ชื่อยา/รหัสสูตร — คงเป็นรหัสตัวเลขเหมือนชื่อสินค้าทั่วไป |
| Medical Institute | สถาบันการแพทย์ | evidence.json: กลุ่มโรงพยาบาล/สถาบันที่ ADDC สังกัด — "Vice Minister of Health...established a vast medical complex known as the Medical Institute" |
| Tokyo Public Prosecutor's Office | สำนักงานอัยการโตเกียว | ดู §3 |
| Tokyo Police Department, Organized Crime Division / Kamuro(cho) Police, Organized Crime Division | กรมตำรวจ แผนกปราบปรามองค์กรอาชญากรรม (สาขาคามุโรโจ) | ⚠ EN เองสะกดไม่นิ่ง 3 แบบในไฟล์เกม (Kamuro Police / Tokyo Metropolitan Police Department / Tokyo Police Department — ทั้งหมด "Organized Crime Division" เดียวกัน) → **แปลไทยให้นิ่งคำเดียวไม่ว่า EN ต้นฉบับสะกดแบบไหน** — คาซึยะ อายาเบะ + มิตสึรุ คุโรอิวะ สังกัดนี้ |
| Kamurocho PD Station | สถานีตำรวจคามุโรโจ | missions.json: "Head to the Kamurocho PD Station" |
| Bayside Hospital | ❌ ไม่พบในไฟล์เกม — อย่าใช้ | grep ทั้ง `extracted/facts/*.json` และ `extracted/db_en/**` ไม่เจอคำนี้เลยสักครั้ง — ชื่อนี้อยู่ใน CLAUDE.md เดิมของโปรเจกต์ (คาดว่ามาจาก wiki) แต่ไม่ตรงกับไฟล์เกมจริง ดู §8 |
| Tender (บาร์) | เทนเดอร์ | missions.json: "Head to Tender...I'll meet Shintani at Tender" — บาร์ที่ยากามิ/ชินทานิไปพบกัน (speakers.json มี "Jo Masuda"=เจ้าของบาร์ Tender) |
| KJ Art | KJ Art (คง EN) | missions.json — สำนักงาน/แกลเลอรีที่เชื่อมกับสาย Kansai |
| Sauna Goten | ซาวน่าโกเท็น | evidence.json/missions.json — พยานที่อยู่ของฮามุระ |
| Club Amour | คลับอามูร์ | evidence.json — ที่เกิดเหตุฆาตกรรมคุเมะ |
| Honmaruen | ฮนมารุเอ็น | missions.json Chapter 6: "Raid Honmaruen" |

---

## §5 ศัพท์ระบบเกม (ยืนยันจาก `help.json`/`skills.json`/`missions.json` — ⏳ เสนอใหม่ทั้งหมด)

| EN | ไทย (เสนอ) | หมายเหตุ |
|---|---|---|
| Case File | แฟ้มคดี | help.json มีหัวข้อนี้ตรงตัว |
| Main Case | คดีหลัก | คู่กับ Side Case |
| Side Case(s) | คดีเสริม | help.json: "Side Cases" |
| Mortal Wound(s) / Deadly Attack | บาดแผลสาหัส / การโจมตีร้ายแรง | help.json: "Deadly Attacks / Mortal Wounds" |
| SP / Skill Point(s) | แต้มทักษะ (SP) | help.json: "Earning SP" |
| EX Gauge | เกจ EX | ล็อกแล้ว (§1) |
| Tailing | การสะกดรอย | help.json: "Tailing → Basic Rules / Taking Cover" |
| Chase(s) / Chasing | การไล่ล่า | help.json: "Chasing" |
| Search Mode (Active/Quick/Drone/Tailing) | โหมดค้นหา (แบบล่าเป้า/ด่วน/โดรน/สะกดรอย) | help.json มี 4 โหมดแยก: Active Search Mode, Quick Search Mode, Drone Search Mode, Tailing Search Mode |
| Drone | โดรน | ทับศัพท์ตรง — help.json มี Drone/Drone League/Drone Lab |
| Drone League | ลีกโดรน | — |
| Drone Lab | แล็บโดรน | — |
| KamuroGo | คง EN | ล้อชื่อแอปจับ NPC สไตล์ Pokémon GO — ชื่อเฉพาะแอปในเกม ไม่แปล |
| Friends (ระบบ) | เพื่อน | help.json: "Friends" — ระบบผูกมิตร NPC 54 คน (`friends.json`) |
| Girlfriend(s) | แฟนสาว | help.json: "Girlfriends", "Girlfriends → Dates" |
| Disguises | ชุดปลอมตัว | help.json — ใช้คู่กับระบบ Tailing |
| Crane Style | **ท่ากระเรียน** | lead ตัดสิน 20 ส.ค. 2026 (แปลความหมาย ไม่ทับศัพท์) |
| Tiger Style | **ท่าเสือ** | lead ตัดสิน 20 ส.ค. 2026 · เห็นในบริบท "Ferocity of the Tiger" ด้วย (skills.json) |
| Snake Style | **ท่างู** | ⏳ ยังไม่เจอบริบทละเอียด รอยืนยันตอนแปลจริง |
| Quickstep(s) | ควิกสเต็ป | ล็อกสืบทอด Pirate/K3 — skills.json มี "Quickstep Strike", "Double Quickstep" |
| Wall Jump | การกระโดดกำแพง | skills.json |
| Leapfrog | การกระโดดข้าม | skills.json |
| Guard / Guarding | การ์ด | ล็อกสืบทอด K3 (Pirate) |
| Fighting Stance | ท่าเตรียมพร้อม / สแตนซ์ต่อสู้ | help.json |
| Photo Mission(s) | ภารกิจถ่ายภาพ | help.json: "Photo Missions" |
| Selfie | เซลฟี่ | ทับศัพท์ทั่วไป |

---

## §6 ยาเสพติด/คดีในเนื้อเรื่อง

| EN | ไทย | หมายเหตุ |
|---|---|---|
| AD-9 | AD-9 (คง EN) | ยา/สูตรยารักษาอัลไซเมอร์ที่กลายเป็นยาทดลองมนุษย์ผิดกฎหมาย — ศูนย์กลางของคดีทั้งเกม |
| Alzheimer's disease | โรคอัลไซเมอร์ | evidence.json อ้างถึงตรงตัว |
| human experimentation | การทดลองในมนุษย์ | evidence.json: "human experimentation scandal involving AD-9" |

---

## §7 ชื่อตัวละครหลัก (⏳ เสนอใหม่ — รอทีมตัวละครยืนยัน/ทำ characters_main.json)

**ขอบเขต**: กันชนกับทีมแฟ้มตัวละครที่กำลังทำคู่ขนาน — ตารางนี้ให้แค่ **การทับศัพท์ชื่อ** (ไม่ใส่บทบาท/บุคลิก/สรรพนามละเอียด)
เพื่อให้นักแปล batch แรกมีคำอ้างอิงใช้ก่อน ทีมตัวละครทำไฟล์ `characters_main.json`/`characters_side.json` แยกเต็มรูปแบบ
ยึดตามหลักทับศัพท์ §0 + รูปที่ล็อกแล้วจากภาคอื่นเมื่อพยางค์ตรงกัน (ระบุในคอลัมน์ที่มา)

รายชื่อจาก `evidence.json` (idx 25-82 = คดีหลัก, idx 91-102 = ตัวละครฝั่ง side)

| EN | ไทย (เสนอ) | ที่มา/หมายเหตุ |
|---|---|---|
| Takayuki Yagami | ทาคายูกิ ยากามิ | ตัวเอก — Yagami ล็อกจาก Gaiden (§2) |
| Masaharu Kaito | มาซาฮารุ ไคโตะ | ล็อกจาก Gaiden (§2) |
| Toru Higashi | โทรุ ฮิงาชิ | ล็อกจาก Gaiden (§2) |
| Ryuzo Genda | ริวโซ เก็นดะ | Genda อ่านตามรูปล็อก Y7 (§4) |
| Issei Hoshino | อิสเซย์ โฮชิโนะ | ⚠ Hoshino(นามสกุล) ล็อกอ่านจาก Y7/Y8 "ริวเฮ โฮชิโนะ" — **คนละตัวละคร** (Y7 Hoshino=ประธานตระกูลเซริว, Judgment Hoshino=ทนายรุ่นใหม่ Genda Law Office) ทีม K3 เคยตั้งธงเรื่องนี้ไว้แล้วว่าอย่าสับสน |
| Kyohei Hamura | เคียวเฮย์ ฮามุระ | Kyohei อ่านตามรูปล็อก K3 "เคียวเฮย์ จิงงุ" — ผู้ต้องสงสัยหลักคดีที่ 1 (กัปตันตระกูลมัตสึกาเนะ) |
| Akira Murase | อากิระ มุราเสะ | ลูกพี่ของคุเมะ, สมาชิกตระกูลเคียวเรอิ |
| Mitsugu Matsugane | มิตสึกุ มัตสึกาเนะ | หัวหน้าตระกูลมัตสึกาเนะ — Matsugane สะกดตามคำตัดสิน lead (glossary_y7.md §2) |
| Kazuya Ayabe | คาซึยะ อายาเบะ | ตำรวจแผนกปราบปรามองค์กรอาชญากรรม (สายทุจริต) |
| Masakazu Kurimoto | มาซาคาซึ คุริโมโตะ | เหยื่อรายที่ 3 |
| Satoshi Shioya | ซาโตชิ ชิโอยะ | กัปตันตระกูลเคียวเรอิ |
| Masamichi Shintani | มาซามิจิ ชินทานิ | เพื่อนร่วมงาน Genda Law Office ผู้ถูกฆาตกรรม (จุดเริ่มเรื่อง) |
| Mitsuru Kuroiwa | มิตสึรุ คุโรอิวะ | ตำรวจแผนกปราบปรามองค์กรอาชญากรรม — **Kuroiwa ล็อกแล้วจาก glossary_y7.md tranche 18 (ดู §2)** |
| Ryusuke Kido | ริวสึเกะ คิโดะ | ผู้อำนวยการ ADDC |
| Yoji Shono | โยจิ โชโนะ | นักวิจัย ADDC ผู้อยู่เบื้องหลังสูตร AD-9 ตัวจริง |
| Kaoru Ichinose | คาโอรุ อิจิโนเสะ | **รองปลัดกระทรวงสาธารณสุข (ชาย)** | ⚠ lead แก้ 21 ส.ค. 2026 — เดิมเขียนว่า "อัยการ" ผิด · คนละคนกับ Kunio Ichinose เจ้าของร้านสเต๊ก |
| Keigo Izumida | เคโกะ อิซุมิดะ | Keigo อ่านตามรูปล็อก K3 wave9 "เคโกะ" |
| Kunihiko Morita | คุนิฮิโกะ โมริตะ | หัวหน้าอัยการ (Chief Prosecutor) — ตัวร้ายเบื้องหลัง |
| Mafuyu Fujii | มาฟุยุ ฟูจิอิ | อัยการ, เพื่อนสมัยเด็กของ Saori — **Mafuyu ล็อกแล้วจาก glossary_y7.md tranche 18 (ดู §2)** |
| Koichi Waku | โคอิจิ วาคุ | เหยื่อผู้ป่วยสูงอายุที่ ADDC |
| Shinpei Okubo | ชินเป โอคุโบะ | Shinpei อ่านตามรูปล็อก K3 "ชินเป อิคาริ" — ผู้ต้องสงสัยคดี ADDC |
| Emi Terasawa | เอมิ เทราซาวะ | พยาบาล ADDC, แฟนของ Okubo |
| Toru Hashiki | โทรุ ฮาชิกิ | เหยื่ออีกราย |
| Ishimatsu | อิชิมัตสึ | — |
| Shigeru Kajihira | ชิเงรุ คาจิฮิระ | Shigeru อ่านตามรูปล็อก K3 "ชิเงรุ นากาฮาระ" |
| Ko Hattori | โค ฮัตโตริ | — |
| Mika | มิกะ | — |
| Saori Shirosaki | **ซาโอริ ชิโรซากิ** | lead ตัดสิน 20 ส.ค. 2026 — นับในไฟล์เกมจริง: `Shirosaki` 22 ครั้งใน 6 bin vs `Shiosaki` 1 ครั้ง (typo ใน `evidence_item_to_update.bin` จุดเดียว) |
| Yosuke Saotome | โยสึเกะ ซาโอโตเมะ | ฝาแฝดพี่ (บารเกอร์พาร์ทไทม์) |
| Tsukino Saotome | สึกิโนะ ซาโอโตเมะ | ฝาแฝดน้อง |
| Rei Miyamoto | เรย์ มิยาโมโตะ | — |
| Hideaki Deguchi | ฮิเดอากิ เดกุจิ | — |
| Fuyuhiko Tanaka | ฟุยุฮิโกะ ทานากะ | Fuyuhiko อ่านตามรูปล็อก K3 wave4 |
| Asami Morimiya | อาซามิ โมริมิยะ | — |
| Asuka Hachitani | อาสึกะ ฮาจิทานิ | — |
| Kiriko Kuwayama | คิริโกะ คุวายามะ | — |

**ยังไม่ครอบคลุม**: 473 speakers เต็ม (`speakers.json`) — ทีมนี้ทำเฉพาะตัวละครที่มีบทในคดีหลัก (evidence.json)
ตัวละครฝั่ง Friends/side content (54 คน `friends.json`) และ NPC ทั่วไป **ปล่อยให้ทีมแฟ้มตัวละครทำต่อ**

---

## §8 ข้อขัดแย้ง/สิ่งที่ต้องให้ lead ตัดสิน

1. **✅ RESOLVED (คำตัดสิน lead 20 ส.ค. 2026) — "ยากามิ" vs "ยากามิ"** — CLAUDE.md และ
   DATA_COLLECTOR_BRIEF.md ของโปรเจกต์นี้เองสะกดชื่อตัวเอกว่า "ยากามิ" (ทาคายูกิ ยากามิ, ง)
   ตลอดทั้งไฟล์ แต่คำที่ **ล็อกจริงและ ship แล้ว** ใน `yakuza-gaiden/translations/master_th.json`
   (ฉากรับเชิญที่โคลอสเซียม, glossary_gaiden.md บรรทัด 80+256) สะกดว่า **"ยากามิ"** (ก ไม่ใช่ ง)
   ตรงตามหลัก "g กลางคำ = ก" ของทีมเอง — lead ยืนยันแล้วว่า **ใช้ "ยากามิ" (ก)** เป็นทางการ
   (glossary_gaiden.md บรรทัด 80 บันทึกไว้ด้วยว่า lead เคยแก้ "ยากามิ"→"ยากามิ" มาแล้ว 2 จุดในบทนั้น) —
   ตารางในไฟล์นี้แก้ตามแล้วทั้งหมด **เหลือแจ้งทีมเอกสาร CLAUDE.md/บรีฟให้แก้ตาม** (เป็นไปได้ว่าเป็น typo ตอนร่างเอกสารเริ่มโปรเจกต์)
2. **✅ RESOLVED (คำตัดสิน lead 20 ส.ค. 2026) — "มัตสึกาเนะ" vs "มัตสึกาเนะ" vs "มัตสึกาเนะ"** —
   สามรูปสะกดชนกัน: CLAUDE.md สะกด "ตระกูลมัตสึกาเนะ" (ง + มี ะ ท้าย) · Gaiden ship ไว้ว่า "มัตสึกาเนะ"
   (ก + มี ะ ท้าย) · ส่วน Y7 (glossary_y7.md บรรทัด 812, tranche 20) ship ไว้ว่า "ตระกูลมัตสึกาเนะ" (ง ไม่มี ะ ท้าย)
   — lead ตัดสินให้ใช้รูปของ **Y7 "มัตสึกาเนะ"** เป็นทางการ (override ลำดับความสำคัญปกติ Gaiden>Y7 เพราะเป็นคำตัดสิน
   lead ตรง ๆ) — ตารางในไฟล์นี้แก้ตามแล้วทั้งหมด (13 จุดใน glossary.md + 3 จุดใน PRONOUN_MATRIX.md)
   **เหลือแจ้งทีมเอกสาร CLAUDE.md/บรีฟให้แก้ ะ ท้ายคำออก**
3. **Bayside Hospital ไม่มีในไฟล์เกม** — CLAUDE.md ระบุชื่อนี้ไว้ (น่าจะมาจากการ research เว็บ) แต่
   grep ทั้ง `extracted/facts/*.json` และ `extracted/db_en/**/*.json` ไม่เจอคำนี้เลย — องค์กรที่มีจริงคือ
   ADDC (Advanced Drug Development Center) ซึ่งมี "hospital wing"/"hospital ward" เป็นส่วนหนึ่งของศูนย์
   ไม่ใช่โรงพยาบาลแยกชื่อ "Bayside" → ต้องตัดคำนี้ออกจากเอกสาร reference หรือยืนยันว่าอยู่ในไฟล์ที่ยังไม่ extract (เช่น `ui.judge.en.par` ที่ยังไม่แตก)
4. ~~**Saori "Shirosaki" vs "Shiosaki"**~~ **ปิดแล้ว → ชิโรซากิ** (นับได้ 22:1 ในไฟล์เกม)
   เดิม: — evidence.json idx 53 สะกด "Saori Shirosaki" แต่ idx 494
   (คำอธิบายของ Mafuyu Fujii) สะกด "childhood friends with Saori Shiosaki" — สะกดไม่ตรงกันในไฟล์เกมเอง
   (อาจเป็น typo ต้นฉบับของ SEGA) → รอ lead ตัดสินว่าใช้สะกดไหนเป็นทางการ (เสนอ "Shirosaki" เพราะเป็นชื่อที่ evidence.json
   ใช้ตอนแนะนำตัวละครครั้งแรก idx 53)
5. **Pink Street (ล็อก K3/Y7) vs Pink Alley (ที่เกิดเหตุใน Judgment)** — ต้องยืนยันว่าเป็นถนนเดียวกันหรือคนละจุด
   ก่อนตัดสินว่าจะใช้ "ถนนพิงก์สตรีท" ต่อหรือแยกชื่อใหม่ "ตรอกพิงก์"/"ซอยพิงค์"
6. ~~**Crane/Snake/Tiger Style**~~ **ปิดแล้ว → ท่ากระเรียน / ท่างู / ท่าเสือ** (แปลความหมาย · ยอมต่างจากคำล็อก "สไตล์" ของ Y7 โดยตั้งใจ)
   เดิม: — เสนอแปลความหมาย (สไตล์เสือ/งู/นกกระเรียน)
   ตามธรรมเนียมชื่อท่ามวยจีน/มวยไทยที่คนไทยคุ้น แต่ยังไม่มีบรรทัดต้นฉบับที่อธิบายที่มาของชื่อสไตล์ในไฟล์ที่ extract แล้ว
   — รอทีมเก็บข้อมูล mission/skill รอบถัดไปยืนยัน lore ก่อน freeze
7. ~~**อาลิไบ vs คำแปล**~~ **ปิดแล้ว → พยานที่อยู่**
   เดิม: — คำนี้ปรากฏถี่มากในคดีหลักทุกคดี ต้อง freeze
   ก่อนเปิด sprint เพราะกระทบความยาวประโยคจำนวนมาก
8. **Tokyo Police Department vs Kamuro(cho) Police vs Tokyo Metropolitan Police Department** — ไฟล์เกมเองสะกดไม่นิ่ง
   3 แบบสำหรับหน่วยงานเดียวกัน (ตำแหน่ง Ayabe/Kuroiwa) — ต้องเลือกคำไทยคำเดียวให้ครอบคลุมทุกกรณี (เสนอไว้ใน §4)

---

## §📇 ตารางเทอมอ่านโดยเครื่อง (เผื่อทำ `make_batch_brief.py` แบบเดียวกับ K3 ในอนาคต)
รูปแบบ: `EN → ไทย` บรรทัดละคู่ — กรอกเฉพาะคำที่ล็อกแน่นอนแล้ว (§1 + §2)

Kamurocho → คามุโรโจ
Tojo Clan → ตระกูลโทโจ
Tenkaichi Street → ถนนเทนไคจิ
Millennium Tower → มิลเลนเนียมทาวเวอร์
New Serena → นิวเซเรน่า
Poppo → ป๊อปโป
Don Quijote → Don Quijote
Cafe Alps → คาเฟ่อัลป์ส
Theater Square → เธียเตอร์สแควร์
Bantam → แบนตัม
Aniki → ลูกพี่ (เดิม อานิกิ — เปลี่ยนตามคำสั่งเจ้าของ 27 ก.ย. 2026)
Kyodai → เคียวได
EX Gauge → เกจ EX
Tiger Drop → ไทเกอร์ดรอป
Crane Style → ท่ากระเรียน
Snake Style → ท่างู
Tiger Style → ท่าเสือ
alibi → พยานที่อยู่
Saori Shirosaki → ซาโอริ ชิโรซากิ
Yagami → ยากามิ
Takayuki Yagami → ทาคายูกิ ยากามิ
Yagami Detective Agency → สำนักงานนักสืบยากามิ
Masaharu Kaito → มาซาฮารุ ไคโตะ
Toru Higashi → โทรุ ฮิงาชิ
Higashi → ฮิงาชิ
Matsugane → มัตสึกาเนะ
Matsugane Family → ตระกูลมัตสึกาเนะ
Kyorei Clan → ตระกูลเคียวเรอิ
Genda Law Office → สำนักงานกฎหมายเก็นดะ
Ryuzo Genda → ริวโซ เก็นดะ
Advanced Drug Development Center → ศูนย์พัฒนายาขั้นสูง
AD-9 → AD-9
Kamurocho PD Station → สถานีตำรวจคามุโรโจ
Case File → แฟ้มคดี
Main Case → คดีหลัก
Side Case → คดีเสริม
KamuroGo → KamuroGo
Quickstep → ควิกสเต็ป
Guard → การ์ด
Style → สไตล์
Ozaki → โอซากิ
Kengo → เค็นโกะ
Seiya → เซยะ
patriarch → หัวหน้าตระกูล
senpai → รุ่นพี่
Kajihira Group → Kajihira Group
Tak (ชื่อเล่นของยากามิ — ไคโตะ/ฮามุระ/**มัตสึกาเนะ** ใช้เรียก · ยืนยันเพิ่มจาก batch_032) → ทาคุ
Dr. Shono → ดร.โชโนะ
Kaoru Ichinose → คาโอรุ อิจิโนเสะ (รองปลัดกระทรวงสาธารณสุข ชาย)
Kamurocho PD (หน่วยงาน) → ตำรวจคามุโรโจ
Kamurocho PD Station (สถานที่) → สถานีตำรวจคามุโรโจ
Genda Law (รูปย่อ ไม่มี Office) → สำนักงานเก็นดะ
Captain (กำกวม — ดูบริบท) → "กัปตัน" เมื่อเป็นยศทางการของฮามุระ · "หัวหน้า/กัปตัน" เมื่อลูกน้องเก่าเรียกไคโตะแบบไม่เป็นทางการ (ยืนยันจาก auth.bin ฉาก Ready Tak?)
human guinea pig(s) → หนูทดลองมนุษย์
Champion District → ย่านแชมเปี้ยน (คำล็อก K1/K2)
Pigeon (โค้ดเนมโดรน) → นกพิราบ
Dayroom → เดย์รูม
Sugiura → ซุกิอุระ
Kuroiwa = ตัว "ไอ้ตัวตุ่น" (the Mole) — อย่าสับสนกับ Morita ที่พัวพัน AD-9 คนละบทบาท
Toshiro Kume → โทชิโร คุเมะ (เหยื่อคดีหลัก · สระสั้นตามเสียง クメ)
Suppon Street → ถนนซุปปอน
Taihei Boulevard → ถนนไทเฮ (คำล็อกเดิม glossary_k2.md §3.2)
swiss cheese alibi → พยานที่อยู่ที่โหว่เป็นรูพรุน
Shintani-sensei → อาจารย์ชินทานิ
ice pick → เหล็กเจาะน้ำแข็ง (อาวุธในคดีคุเมะ)
Kamuro Maintenance (บริษัทปลอมที่ยากามิอ้างตอนแฝงตัว) → คามุโร เมนเทนแนนซ์
Club Stardust → คลับสตาร์ดัสต์
Kyushu No. 1 Star (ร้านราเมง) → คง EN
`-shi` (氏) เช่น Yagami-shi → **ไม่เติมคำต่อท้าย** ใช้ชื่อเปล่า "ยากามิ" (ไทยไม่มีคำเทียบ · ยืนยันเป็นกฎถาวร 21 ส.ค. 2026)
Masuda → มาสึดะ (su = สึ · ไม่ใช่ มาสึดะ)
L'Amant (คาสิโนลับ) → ลามองต์ (ทับศัพท์ตามแนว Club Amour → คลับอามูร์ · lead ตัดสิน 21 ส.ค. 2026)
Konban Wife (ซ่อง) → **คง EN** — เป็นมุกสองภาษา (konbanwa + wife) ทับศัพท์แล้วมุกตาย และเป็นชื่อป้ายร้าน
Charles (ร้านเกมของฮิงาชิ) → ชาร์ลส์ · Hills Garden → ฮิลส์การ์เดน · Park Boulevard → ถนนปาร์คบูเลอวาร์ด
Kenkichi Mashiba → เค็นคิจิ มาชิบะ (เหยื่อรายแรก)
Shichifuku Street → ถนนชิจิฟุกุ (ตรงกับคำล็อก glossary_k2 §3.2)
Moroboshi-sensei → อาจารย์โมโรโบชิ
Koi Bride (ร้าน) → โคอิไบรด์
Red Nose → จมูกแดง (แปลความหมาย ไม่ทับศัพท์ — บทเล่นมุกกับสีแดงโดยตรง)
Theater Alley → เธียเตอร์อัลเลย์ (คนละที่กับ Theater Square = เธียเตอร์สแควร์)
Children's Park → สวนเด็ก
Play Pass → เพลย์พาส · Suguroku → ซุโกโรกุ · Dice & Cube / Paradise VR คง EN
the boss (เรียกมัตสึกาเนะแบบไม่เป็นทางการ) → โอยาบุน · second-in-command → มือขวา
swore up (พิธีเข้าตระกูลยากูซ่า) → สาบานเข้าตระกูล
Keihin Gang → แก๊งเคฮิน · Keihin Four → สี่เทพเคฮิน
Kasai → คาไซ · Renji Honda → เรนจิ ฮอนดะ · Sakakiba → ซากากิบะ · Koga → โคกะ · Kim → คิม
Medical Device Development Institute → สถาบันพัฒนาอุปกรณ์การแพทย์ (หน่วยงานที่ดูแล ADDC)
Minister Kazami (รมต.สาธารณสุข ผู้หนุนหลัง) → รัฐมนตรีคาซามิ (คนละคนกับ Kaoru Ichinose รองปลัดฯ)
Hashimoto (เจ้าหน้าที่วิจัย ADDC · **หญิง** ยืนยัน 21 ส.ค. 2026 จากบทพูด "She was just about to return to the lab" + voicer_gender) → ฮาชิโมโตะ
Director (ตำแหน่งคิโดะที่ ADDC) → **ผู้อำนวยการ** (ห้าม "ผู้กำกับ" ซึ่งเป็นศัพท์หนัง/ตำรวจ)
break room → ห้องพักผ่อน (คนละคำกับ day room = เดย์รูม ที่ล็อกไว้ · EN ใช้สองคำเรียกห้องเดียวกัน)
groper / molester → คนลวนลาม
Theater Avenue → เธียเตอร์อเวนิว (คนละที่กับ Theater Square = เธียเตอร์สแควร์ · Theater Alley = เธียเตอร์อัลเลย์)
Keigo Izumida (อัยการ ไม่ใช่ตำรวจ — ยืนยันจากบท "Objection!/Your Honor!") → เคโกะ อิซุมิดะ
Queen Rouge (คลับคาบาเรต์) → ควีนรูจ
Le Marche (ร้านชุด) → เลอมาร์เช่ · Sumire (ฮอสเตสควีนรูจ) → สุมิเระ · Takemitsu (ร้าน/เจ้าของร้านขนม) → ทาเคมิตสึ
Chatter (แอป SNS ในเกม) → **คง EN** (แนวเดียวกับ Dice & Cube / Paradise VR — ชื่อแอป/แบรนด์คงรูปละติน)
Kamuro Kikunoya (ร้านอาหารที่มัตสึกาเนะนัดเจอ) → คามุโรคิคุโนยะ (Kamuro = คามุโร ให้ตรงกับคำล็อก คามุโรโจ ห้ามเขียน "คามุโร")
Tashiro / Tashiro-kun (ลูกน้องตระกูลมัตสึกาเนะที่ยากามิปลอมตัวเป็น) → ทาชิโระ / ทาชิโระคุง
Emerald Hills (คลับคาบาเรต์ ถนนชิจิฟุกุ) → เอเมอรัลด์ฮิลส์ (ฮิลส์ ตรงกับคำล็อก Hills Garden = ฮิลส์การ์เดน)
cho-han (เกมทอยลูกเต๋าดั้งเดิมของยากูซ่า) → **โจฮัง** (คำล็อกจาก K3 glossary บรรทัด 123 + glossary_k2 §4 ตาม PIRATE — lead เคยล็อกผิดเป็น "โจฮัง" 21 ส.ค. 2026 แล้วแก้ตาม priority K3 > ทุกโปรเจกต์)
death row → แดนประหาร · death row inmate → นักโทษประหาร (ล็อก 21 ส.ค. 2026 — จะซ้ำในฉากเยี่ยมเรือนจำบทที่ 9 เป็นต้นไป)
Alvin (ร้านตระกูลมัตสึกาเนะ) → อัลวิน · Sweet Billow → สวีทบิลโลว์ · Fantastic Romance → แฟนตาสติกโรแมนซ์
Romance of the Three Kinkdoms (ร้าน) → **คง EN** — เป็นมุกเล่นคำ Kingdoms/Kinkdoms แปลแล้วมุกตาย (แนวเดียวกับ Konban Wife)
Soleil Building (ตึกที่ไคโตะถูกขังในบทที่ 10) → ตึกโซเลย์ (ล็อกใหม่ 21 ส.ค. 2026 — ไม่มีคำล็อกเดิมในโปรเจกต์พี่น้อง)
Yasuo Kunimura → ยาสึโอะ คุนิมุระ (ล็อก 21 ส.ค. 2026 จาก batch_066 — su=สึ ตามกฎทีม)
entrapment (ศัพท์กฎหมาย) → การล่อให้กระทำความผิด (ล็อก 21 ส.ค. 2026 จาก batch_068)
blackmail → แบล็กเมล์ (ล็อก 21 ส.ค. 2026 — คำยืมที่ใช้ทั่วไป เข้ากับทะเบียนบทพูด) · sexual harassment → การคุกคามทางเพศ
Health Ministry thugs → นักเลงกระทรวงสาธารณสุข (ล็อก 21 ส.ค. 2026 — กลุ่มที่ตามคุ้มกันคิโดะ)
Monsieur Lee (ธุรกิจบังหน้าห้องแล็บลับ ใกล้มิลเลนเนียมทาวเวอร์) → มองซิเออร์ลี (ทับศัพท์แนวเดียวกับ L'Amant → ลามองต์)
Uzawa (อดีตนักสืบ · คนที่มาฟุยุเรียกว่า "sort of my boyfriend") → อุซาวะ (ล็อกใหม่ 21 ส.ค. 2026 จาก batch_073)
caretaker murder → คดีฆาตกรรมโดยผู้ดูแล · dementia → ภาวะสมองเสื่อม (คนละคำกับ Alzheimer's = โรคอัลไซเมอร์ · EN แยกใช้จริง)
Mijore (ร้านที่ยากามิเจออิซุมิดะ) → มิโจเระ (รูปที่ ship แล้วใน master_th — ห้ามเขียน "มิโจเร")
on the force (สำนวน EN ที่ใช้กับตำรวจเสมอในเกมนี้) → เมื่อ EN ใช้กับ**อัยการ** ให้แปล "ในแวดวงกฎหมาย" ไม่ใช่ "กองปราบ/กรมตำรวจ"
Tokyo PD / Tokyo Metropolitan Police → **ตำรวจนครบาลโตเกียว** (ตามรูปที่ ship แล้วใน K3 + Gaiden) · "Kamurocho cop" (พูดถึงคุโรอิวะแบบไม่ทางการ) → ตำรวจคามุโรโจ — ใช้ตาม EN รายบรรทัด ไม่รวบเป็นคำเดียว
Fumiya (ชื่อจริงของซุกิอุระ · น้องชายเอมิ เทราซาวะ · เฉลยบทที่ 13) → ฟูมิยะ / Fumiya-kun → ฟูมิยะคุง
⚠ คำด่า AD-9 ("that damn drug" ฯลฯ) → ใช้คำกลางเช่น "ไอ้ยาเวรนี่" · **ห้ามใช้ "ยาบ้า"** ซึ่งแปลว่าเมทแอมเฟตามีนของจริง (ผู้ตรวจ batch_075 เจอหลุด 2 จุด — AD-9 เป็นยารักษาอัลไซเมอร์ในเรื่องแต่ง ไม่ใช่ยาเสพติดข้างถนน)

## §9 ศัพท์ห้องพิจารณาคดี (ล็อก 21 ส.ค. 2026 — เริ่มใช้ตั้งแต่ batch_077 ฉากคดีอายาเบะ)
Your Honor → ศาลที่เคารพ · Objection! → ขอคัดค้าน! · defendant → จำเลย · the prosecution → ฝ่ายโจทก์ (พูดถึงตัวอัยการใช้ "อัยการ")
defense / defense attorney → ฝ่ายจำเลย / ทนายฝ่ายจำเลย · witness → พยาน · witness stand → คอกพยาน · testimony → คำเบิกความ
to testify → เบิกความ · cross-examination → การถามค้าน · direct examination → การถามติง · subpoena → หมายเรียก
verdict → คำพิพากษา · acquittal → ยกฟ้อง · plead not guilty → ให้การปฏิเสธ · court is in session → เปิดการพิจารณาคดี
**โทนศาล**: ผู้พิพากษา/อัยการในห้องพิจารณาใช้ภาษาราชการ ไม่ผูกสรรพนามรายบุคคล (ใช้ "ศาล"/"ฝ่ายโจทก์"/"ฝ่ายจำเลย" แทนคำแทนตัว) · **ห้ามใช้คำราชาศัพท์**

## §10 ศัพท์ UI/ระบบ (ล็อก 21 ส.ค. 2026 — ผู้ตรวจ batch_080 เสนอ · lead รับ)
Cancel → ยกเลิก · Quit → ออก · OK → ตกลง · Yes/No → ใช่/ไม่ · Back → ย้อนกลับ · Next → ถัดไป · Close → ปิด
Help → ช่วยเหลือ · Select → เลือก · Settings → ตั้งค่า · Saving... → กำลังบันทึก... · Loading... → กำลังโหลด...
Save completed. → บันทึกเสร็จสิ้น · Load completed. → โหลดเสร็จสิ้น · yen → เยน · EX Gauge → เกจ EX · SP → คง EN
**Reset to default X settings?** ใช้แพทเทิร์นเดียวกันทุกหมวด (เกม/เสียง/ความสว่าง/กราฟิก) ห้ามสลับโครงสร้างระหว่างหมวด
**ลำดับ placeholder วันที่**: `${month}/${day}/${year}` → สลับเป็น **`${day}/${month}/${year}`** ได้ (ธรรมเนียมไทย) เพราะเป็น token ตั้งชื่อ ไม่ใช่ตำแหน่ง — **แต่ `%s/%d` ที่เป็น positional ห้ามสลับเด็ดขาด**
**แท็ก `<platform=...>` / `<platform_not=...>`**: มีข้อความ user-facing อยู่ทั้งสองฝั่ง — **ต้องแปลทั้งคู่** ห้ามปล่อย EN (ผู้ตรวจ batch_080 เจอ ref_tm เก่าปล่อยไว้ทั้งค่า)
**legacy string**: บางสตริงมาจากเอนจิ้นร่วม ไม่ได้ใช้จริงใน Judgment (เช่น "Clan Creator" · "Majima Saga" · "Yagami is too full to gain SP") — **แปลตรงตัวไปตามปกติ** ไม่ต้องดัดแปลง
Rie Tomioka → รี โทมิโอกะ · Sakura Amamiya → ซากุระ อามามิยะ · Sana Mihama → ซานะ มิฮามะ · Nanami Matsuoka → นานามิ มัตสึโอกะ
Tatsuro → ทัตสึโร · Yukko → ยุกโกะ · Junichi Fujinaga → จุนอิจิ ฟูจินากะ · Ohata → โอฮาตะ · Ayumu → อายุมุ (ล็อก 21 ส.ค. 2026 จาก batch_081)
Sana → ซานะ · Kabata(-san) → คาบาตะ(ซัง) · Kitamura(-san) → คิตามุระ(ซัง) · Kamuro Theater → โรงละครคามุโร (คนละที่กับ Theater Square = เธียเตอร์สแควร์)
Nanami → นานามิ · Yukko → **ยุกโกะ** (ไม่ใช่ "ยุกโกะ" — ッ ก่อน k สะกดด้วย ก แบบ Nikko = นิกโก) · arcade → ร้านเกม
"lol" (ข้อความมือถือ) → 5555 · "Haha/Ahaha" → ฮ่าๆ / อ้าฮ่าๆ (ล็อก 21 ส.ค. 2026 — ระบบแชทในเกมใช้บ่อย)
Koro-nyan (Mode) → โคโระเนียง · Kuro-nyan → คุโระเนียง
**SP** → คง EN เปล่า ๆ ทุกจุด (ห้ามขยายเป็น "แต้มทักษะ (SP)" — lead ตัดสิน 21 ส.ค. 2026 เพื่อให้ UI สั้นและตรงกันทั้งเกม)
Makoto Tsukumo → **มาโคโตะ สึคุโมะ** (ช่างเทคนิค เพื่อนของยากามิ · ชาย T1) · Wette Kitchen / Jungle Boy → คง EN (ชื่อร้าน ไม่มีคำล็อกเดิม)
Tenkaichi Alley → ซอยเทนไคจิ (แนวเดียวกับ Theater Alley = เธียเตอร์อัลเลย์ · คนละที่กับ Tenkaichi Street = ถนนเทนไคจิ)
⚠ อักขระที่ **ห้ามใช้ในคำแปล**: ❤ ♥ ♪ ★ และสัญลักษณ์นอก ASCII อื่น ๆ — ฟอนต์ไทยที่ inject ไม่มีเซลล์ให้ (จะขึ้น tofu) · ถ่ายความหมายด้วยคำหรือ "..." แทน
Amane → อามาเนะ (หมอดู · หญิง T1) · Tsumugi → สึมุกิ · Nasugawa → **นาสึกาวะ** (su = สึ · ไม่ใช่ "นาสึกาวะ")
M Side Cafe → เอ็ม ไซด์ คาเฟ่ · Batting Center → **ศูนย์ฝึกตี** (รูปที่ ship แล้วใน master_th — ยกเลิกคำเสนอ "ศูนย์ฝึกตี" 21 ส.ค. 2026) · Mantai → มันไท
"sign of the blades" (คำทำนายของอามาเนะ) → ลางแห่งใบมีด · "cow calamity" → ลางร้ายรูปวัว · "Kamurocho Calamity Busters" → หน่วยปราบลางร้ายคามุโรโจ

## §11 ชื่อร้านอาหาร/ร้านค้า + ศัพท์มินิเกม (ล็อก 21 ส.ค. 2026)
**หลักการ**: ชื่อร้านในเกม → **ทับศัพท์ไทย** ตามบรรทัดฐานที่ ship แล้ว (คาเฟ่อัลป์ส · คิวชูนัมเบอร์วันสตาร์ · คลับอามูร์ · เลอมาร์เช่ · ชาร์ลส์ · โคอิไบรด์)
· **ยกเว้น** ชื่อที่เป็นมุกสองภาษา (Konban Wife · Romance of the Three Kinkdoms) และชื่อเกมอาร์เคดจริงของ SEGA → คง EN
**ชื่อเกมที่คง EN**: Virtua Fighter 2/5 · Fighting Vipers · Fantasy Zone · Space Harrier · Kamuro of the Dead · Championship Motor Raid · UFO Catcher · Koi-koi
**mahjong → มาจอง** (รูปที่ ship แล้วใน K3/Gaiden 109 จุด · ไม่ใช่ "มาจอง") · ชื่อร้านมาจองทับศัพท์ทั้งหมด: ลัลลาบายมาจอง · โมเดิร์นมาจอง · ทาชิบานะมาจอง
**ศัพท์มาจอง (ทับศัพท์ ไม่แปลความหมาย)**: ron → รอน · tsumo → สึโม · mangan → มังกัง · haneman → ฮาเนมัง · riichi → **รีช** (คำล็อกเดิม) · riichi ippatsu → รีชอิปปัตสึ · Three Color Straight → ซันโชกุโดจุง
**ศัพท์ดาร์ท**: Bullseye → บูลส์อาย · Hat Trick → แฮตทริก · Cricket → คริกเก็ต · Triple Twenties → ทริปเปิล 20 · Low/High Ton · Ton 80 · Three in a Bed · White Horse → คง EN
**ศัพท์ต่อสู้**: Tiger Style → ท่าเสือ · Crane Style → ท่ากระเรียน · Wall Jump → การกระโดดกำแพง · EX Action / EX Boost → คง EN
**Club SEGA** → คง EN (ชื่อแบรนด์จริงของ SEGA เหมือนชื่อเกมอาร์เคด) · **Crazy Taxi · Crazy Taxi 2/3 · Streets of Rage** → คง EN (แฟรนไชส์จริง)
**ชื่อร้านมาจอง**: ทาชิบานะมาจอง (ไม่ใช่ "ทาชิบานะมาจอง") · ลัลลาบายมาจอง · โมเดิร์นมาจอง
**ร้านอาหารที่ทับศัพท์แล้ว (ผู้ตรวจ batch_088)**: คาเฟ่มิโจเระ · สไมล์เบอร์เกอร์ · อากาอุชิมารุ · เอ็ม ไซด์ คาเฟ่ · คันไร · คิวชูนัมเบอร์วันสตาร์ · ซูชิกิน · ควอดราการ์เดน · ฟูจิโซบะ · ไวลด์แจ็คสัน · โยโรโนทากิ · กินดาโกะ ไฮบอล ทาเวิร์น · ริงเกอร์ฮัท · ซูชิซันไม · อิคินาริสเต๊ก · คาเฟ่อัลป์ส

Earth Angel → เอิร์ธแองเจิล · Shellac → เชลแล็ก · Gyu-Kaku → กิวคาคุ · Beef Zone → บีฟโซน · Decor-oceans → เดคอร์-โอเชียนส์ · G.A. Labs → จีเอ แล็บส์ · Bantam → แบนตัม (ล็อก 21 ส.ค. 2026 — ชื่อพวกนี้ซ้ำใน batch 096/101/104/107/108/120/121 + TALK_*)
wareme → **วาเระเมะ** (wa=วา · re=เระ · me=เมะ) · waryori → วาเรียวริ
EX Bond → **สายสัมพันธ์ EX** (Bond → สายสัมพันธ์ ตามที่ ship ใน master_th) · Investigation Action (หมวด survey) → การสืบสวน · On the Side (หมวด subevent · คนละตัวกับ Side Case) → กิจกรรมเสริม
Extracts → สารสกัด · Creating Extracts → การทำสารสกัด · Extract Ingredients → วัตถุดิบสารสกัด
ชื่อ EX Bond (ยังไม่เจอบทพูด · ทับศัพท์ไว้ก่อน): Takeo Inose → ทาเคโอะ อิโนเสะ · Alice Ino → อลิซ อิโนะ · Sota Nonomura → โซตะ โนโนมุระ · Kiyoshiro Asamura → คิโยชิโร อาซามุระ · Dwayne Cruise → ดเวย์น ครูซ · Hanae Ida → ฮานาเอะ อิดะ · Meguro → เมกุโระ · Wakahara → วาคาฮาระ
⚠ **ชื่อร้าน vs ชื่อสินค้า**: ชื่อร้านที่ล็อกให้คง EN (Wette Kitchen ฯลฯ) ให้คง EN ในประโยคไทยด้วย · แต่ **ชื่อเมนู/สินค้าที่ตั้งจากชื่อร้าน ให้ทับศัพท์** (Wette Burger → เว็ตเทเบอร์เกอร์)

## §12 ศัพท์นิติเวช/แฟ้มคดี (ล็อก 21 ส.ค. 2026 — ผู้ตรวจ batch_090 เสนอ)
cause of death → สาเหตุการเสียชีวิต (direct → สาเหตุการเสียชีวิตโดยตรง) · time of death → เวลาเสียชีวิต · autopsy report → รายงานชันสูตรพลิกศพ
murder weapon → อาวุธสังหาร · crime scene → สถานที่เกิดเหตุ · modus operandi → วิธีการก่อเหตุ · stab wound through the eye → บาดแผลแทงทะลุดวงตา
"relocated from the actual scene of the crime" → ศพถูกเคลื่อนย้ายมาจากสถานที่เกิดเหตุจริง · **alibi → พยานที่อยู่ เท่านั้น** (ห้าม "พยานที่อยู่" — มีกฎกวาดแล้ว)
**แพทเทิร์นรายงานชันสูตร**: "สาเหตุการเสียชีวิตโดยตรงของ [ชื่อ] คือ..." ใช้เหมือนกันทุกแฟ้ม ห้ามถอดความเป็นสำนวนอื่น
**ข้อยกเว้นความยาว**: ชื่อเควส/achievement ย่อได้ (เช่น entrapment → "การล่อกระทำผิด" แทน "การล่อให้กระทำความผิด" เพื่อไม่ให้ล้นกล่อง) แต่ในเนื้อความให้ใช้รูปเต็ม
Hatano (เพื่อนใน Friend system ขายอุปกรณ์เบสบอล) → ฮาตาโนะ · ootoro/chuutoro/akami (ส่วนเนื้อปลาทูน่า) → โอโทโระ/ชูโทโระ/อากามิ · CAB Angus → คง EN (เครื่องหมายการค้า)
⚠ **ref_tm มีช่องว่างแทรกกลางคำไทย** (wrap artifact จากไฟล์เก่า เช่น "อากาอุชิมารุ" · "จัดเรียง อย่างประณีต") — ตรวจทุกครั้งก่อนใช้ ref_tm แล้วลบช่องว่างที่แทรกผิดตำแหน่งออก
⚠ เมนูของ Wette Kitchen → ใช้คำนำหน้า **"เว็ตเท"** เท่านั้น ห้ามเติม "คิทเช่น/คิตเชน" เข้าไปเอง (เช่น Wette Original Coffee → กาแฟต้นตำรับเว็ตเท) · ชื่อร้านในประโยคยังคง EN "Wette Kitchen"
champon → จัมปง (ไม่ใช่ "จัมปง") · steak → **สเต๊ก** (ไม่ใช่ "สเต๊ก" — ล็อก 21 ส.ค. 2026)
Isetani Trading Company → บริษัทการค้าอิเซทานิ (ซ้ำใน batch 103/121/TALK_031/032) · Fuka Shiranui → ฟุกะ ชิรานุย · Bram Sylvania III → แบรม ซิลเวเนียที่ 3 · Toughness Light → ทัฟเนส ไลต์ · Kopi Luwak → โกปี ลูวัก
oicho-kabu → โออิโช-คาบุ (ไม่ใช่ "โออิโช-คาบุ") · karaage → คาราอาเกะ (ไม่ใช่ "คาราอาเกะ") · mahjong ในชื่อไอเทม → มาจอง (ห้าม "มาจอง")
Prepaid Card (1.5K/3K/5K/10K JPY) → บัตรเติมเงิน (1.5K เยน) ฯลฯ — คงรูปตัวเลข K ตามต้นฉบับ เปลี่ยนแค่ JPY → เยน
ชื่อไซด์เคส (ล็อก 21 ส.ค. 2026): Twisted Trio → สามโรคจิต · Judge Creep 'n Peep → ผู้พิพากษาจอมถ้ำมอง · Panty Professor → ศาสตราจารย์กางเกงใน · Giant Impact → ไจแอนต์อิมแพ็กต์ · Crow → โครว์ · Cloudy Skies Publishing → สำนักพิมพ์คลาวดีสกายส์ · Heavy Coffee → เฮฟวี่คอฟฟี่
ตัวละครไซด์เคส: ฮายาโตะ อาดาจิ · ชุนเอย์ โออิคาวะ · อาซึสะ/คาริน/จิน โอทากิ · โคจิโร คุวายามะ · ทาเคฟุมิ/เมกุมิ ฮาชิโมโตะ · ทาโร อิเซยะ · ฮารุอากิ ไซโตะ · ยูกาโกะ โอกิ · มาโมรุ ชิมาซึ · โทยะ โทคุนางะ · ฮาจิเมะ โอบายาชิ · มาคิฮาระ · โทโมคาซึ คาวาดะ · เก็นโกโร มิกิ
ชื่อจีนในเกม (ทับศัพท์แบบจีน ไม่ใช่ญี่ปุ่น): Ruan Wang → หรวน หวัง · Zhuang Shi (แมว) → จวง ซือ
cerebral contusion → สมองฟกช้ำ · Waku's Hospital Room → ห้องผู้ป่วยของวาคุ · Kume → **คุเมะ** (ไม่ใช่ "คุเมะ")
**รูปแบบสาเหตุการเสียชีวิต 2 แบบ ใช้ตาม EN**: ถ้า EN เป็นประโยคเต็ม → "สาเหตุการเสียชีวิตโดยตรงของ [ชื่อ] คือ..." · ถ้า EN เป็นป้ายกำกับ (label) → "สาเหตุการเสียชีวิต: ..." (lead รับรอง 21 ส.ค. 2026)
The Pervert King → ราชาลามก (รูปที่ ship แล้ว — ห้าม "ราชาลามก")
ตัวละคร/สถานที่จาก batch_096: โอโตยะ ชิจิมะ (ชื่อจริงของแบรม ซิลเวเนีย) · อาดาจิ(ซัง) · มากิ · ทัตสึโอะ ทานากะ · โชจิ/อายุมุ โอฮาตะ · โคทาโระ ฮิวกะ ("Horny Hinata" → ฮินาตะจอมกำหนัด) · ทาเอโกะ นากาฮาระ · เค็นจิ ซุนาดะ · คาเนดะ · คุมะคุระ · **นิชิมุระ** · มาซาตากะ ทาเคสึรุ · **ริตา** · โอโนะมิจิ จังหวัดฮิโรชิมะ · โยอิจิ · เซนได
The Fisherman (โค้ดเนม) → นักตกปลา (แปลความหมาย แนวเดียวกับ Red Nose → จมูกแดง · the Mole → ไอ้ตัวตุ่น)
หมากโชกิ: Lance → แลนซ์ · Bishop → บิชอป · Knight → ไนต์ · Rook → รุค · Pawn → เบี้ย · Silver/Gold General → นายพลเงิน/นายพลทอง · Champion/Challenger King → ราชาแชมป์/ราชาผู้ท้าชิง
**เครื่องหมายการค้าเหล้า/เครื่องดื่ม → คง EN เสมอ** (Jack Daniel's · Bushmills · Bunnahabhain · Early Times · Asahi · Wonda · Mitsuya Cider · Bireley's Orange · Wilkinson Soda · Dodekamin · Kinkuro · Camus · Jose Cuervo · Nikka) — คำบรรยายแปลไทยตามปกติ
Skill App → แอปทักษะ (ซ้ำในทุก batch ที่มีข้อความ "Learn how to use it on the Skill App.") · Extract Recipe → สูตรสารสกัด · Deadly Attacks → การโจมตีร้ายแรง
Iyama → อิยามะ · Akatsuki → อาคัตสึกิ · Mugwort → โกฐจุฬาลัมพา · "VR Ethlete" (มุกผสม athlete+VR) → นักกีฬา VR ผู้ประกาศตนเอง (มุกแปลไม่ได้ ยอมสูญ)
Poppo (มาสคอตร้านสะดวกซื้อ) → ป๊อปโป · MFLP → คง EN
**ข้อความที่สลักบนวัตถุ** (เช่น "Charles" บนส้นรองเท้า Charles Sandals) → **ทับศัพท์ตามคำล็อกของชื่อนั้น** (ชาร์ลส์) ไม่คง EN — lead ตัดสิน 21 ส.ค. 2026
amusement center → ศูนย์รวมเครื่องเล่น (ล็อก 21 ส.ค. 2026 — ซ้ำในไอเทมรางวัลร้านเกม)
Yusuke (คดีลักพาตัว · คนละคนกับ Yosuke Saotome) → **ยูซึเกะ** · Haruka Sawamura → ฮารุกะ ซาวามุระ · Ono Michio → โอโนะ มิชิโอะ · King Koro-nyan → **ราชาโคโระเนียง** (แก้ 7 ก.ย. 2026 — บรรทัดนี้เคยเขียน "คิงโคโระเนียง" ขัดกับกฎใน `normalize_terms.py` ที่ตัดสินให้ใช้ ราชา และ master ใช้ ราชา ทั้ง 22 จุด · ทีม register ชิ้น 06 ชี้)
[Launch Edition] → [รุ่นวางจำหน่าย] · [Bonus Code] → [โค้ดโบนัส] · [Bonus] → [โบนัส]
ศัพท์มาจอง (เพิ่ม): จุนซึ · โคะสึ · เมนสึ · จันโตะ · โทอิสึ · ปง · ชี่ · คัง
ศัพท์โป๊กเกอร์ (ทับศัพท์): วันแพร์ · ทูแพร์ · ทรีออฟอะไคนด์ · ฟลัช · ฟูลเฮาส์ · สเตรทฟลัช · รอยัลฟลัช · ไฮการ์ด
ศัพท์โป๊กเกอร์ ฝั่งการเดิมพัน (ล็อก 21 ส.ค. 2026 — นักแปล batch_110 เสนอ · lead รับ): Call → คอล · Fold → โฟลด์ · Raise → เรส · Big Blind → บิ๊กบลายด์ · Little Blind → ลิตเทิลบลายด์ · Total Bet → เดิมพันรวม · Round (โป๊กเกอร์) → ยก (ห้ามใช้ "รอบ" ซึ่งสงวนให้ Lap ของมินิเกมแข่ง)
ศัพท์โออิโช-คาบุ: โฟร์-วัน · ไนน์-วัน · เท็น-เท็น-วัน · โฟร์-ซิกซ์
ชื่อสินค้า/เครื่องดื่มในเกม → คง EN: Staminan X · Hug Bomb · Toughness Z · Tauriner
"Anytime." / "No problem." (ตอบรับคำขอบคุณ) → **ยินดีเสมอ** (ห้าม "เมื่อไหร่ก็ได้" ซึ่งแปลว่านัดเวลา — ผู้ตรวจ batch_079 เจอ ref_tm แปลผิดความหมาย)
**Mad Bomber → มือระเบิดบ้าคลั่ง** (ล็อกรูปเดียว 21 ส.ค. 2026 — เดิมมี 5 รูปในเกม) · The Mad Bomber Strikes Again / Return of the Mad Bomber → มือระเบิดบ้าคลั่งหวนคืน · Kamurocho's Mad Bomber → มือระเบิดบ้าคลั่งแห่งคามุโรโจ
Horumon → โฮรุมง · Yakumaru Loans → ยาคุมารุโลนส์
คำตัดสิน lead รอบ sprint 21 ส.ค. 2026 (จากรายงานผู้ตรวจ batch_106/107/108/109/115/116 — normalize_terms.py กวาดให้อัตโนมัติทุกคำที่เป็นข้อความไทย):
· **Rei / Rei Miyamoto → เรย์** รูปเดียวทั้งเกม (ยืนยันแล้วว่า Rei ในภารกิจ Rescue Rei from the Boss คือคนเดียวกับ Rei Miyamoto) — ปิดข้อขัดแย้งที่ค้างมาตั้งแต่ batch_105
· **Kyushu No. 1 Star → คิวชูนัมเบอร์วันสตาร์** (ทับศัพท์ไทยล้วนทุกจุด รวมในบทพูด — เดิม master ปนกันระหว่างคง EN 10 จุด กับไทย 7 จุด · แก้ย้อนหลังแล้ว)
· **Ass Catchem → จอมจับตูด** (ห้าม "จอมจับตูด")
· **thumb turn bypass → การเลี่ยงสลักล็อกแบบบิดนิ้วโป้ง** (ห้าม "การเลี่ยงสลักล็อกแบบบิดนิ้วโป้ง")
· **ตระกูลสกิล Quickstep: ชื่อสกิลที่เป็นหัวข้อ → คง EN ทั้งตระกูล** (Double Quickstep · Quickstep Strike · Quickstep Cancel) ส่วนคำว่า quickstep ที่อยู่กลางประโยคอธิบาย → ทับศัพท์ "ควิกสเต็ป" ตามที่ ship แล้ว
· นามสกุลลงท้าย -guchi → **กูจิ** (Kamaguchi = คามากูจิ · Taguchi = ทากูจิ) · Katagiri → คาตากิริ · Kitamura → คิตามุระ · Quadra Garden → ควอดราการ์เดน
· ศัพท์มาจอง/ฮานะฟุดะที่ ref_tm ชอบลากรูปเก่ามา: yakuman → **ยากุมัง** (ไม่ใช่ ยากุมัง) · riichi → **รีช** (ไม่ใช่ รีช) · tsumo → **สึโม** (ไม่มี ะ) · no-points hand → มือไร้แต้ม (ไม่ใช่ มือไร้แต้ม) · seven pairs → คู่เจ็ดคู่ (ไม่ใช่ คู่เจ็ดคู่) · all simples → ไพ่ธรรมดาล้วน (ไม่ใช่ ไพ่ธรรมดาล้วน)
· `Iron Plate` กับ `Steel Plate` มาจากคันจิ 鉄 ตัวเดียวกัน → **ต้องแปลเหมือนกัน (เหล็ก)** แม้ EN จะเขียนต่างกัน · King (ร้าน Ohsho) → คิง
· Taihei Boulevard → ถนนไทเฮ (ตัดคำ boulevard ทิ้ง ต่างจาก Park Boulevard ที่ทับศัพท์เต็ม — ยืนยันตามที่ ship แล้ว 26 จุด)
· **ชื่อ NPC ที่ EN ไม่ได้บอกเพศ (Youth / Young X / Host ฯลฯ) ห้ามแปลเป็น "หนุ่ม"** ให้ใช้ วัยรุ่น / อายุน้อย หรือคำกลาง ๆ (ผู้ตรวจ batch_108 เจอพลาดซ้ำ 4 จุดใน batch เดียว)
· `Naisu Daisu` (六角彩) → ไนสึ ไดสึ (ทับศัพท์ตามที่นักแปลเสนอ — ไม่คง EN)
· **แคตตาล็อกชิ้นส่วนโดรน (batch 112/113)**: รหัสแบรนด์ `S-ONE:` `SMZ:` `Mako Mods:` → คง EN · **ทุกอย่างหลัง colon แปล/ทับศัพท์ไทย** (Alloy → อัลลอย · Adamant → อดาแมนต์ · Kaleidoscope → **คาไลโดสโคป** ห้าม "ไคลิโดสโคป" · Clover → ลายใบโคลเวอร์ · Digital/Desert Camo → ลายพรางดิจิทัล/ทะเลทราย) · ชื่อรุ่นที่ไม่มีแบรนด์นำหน้า (Thunder God Motor ฯลฯ) → แปลไทยทั้งชื่อ · คำชนิดชิ้นส่วน: Motor → มอเตอร์ · Propeller → ใบพัด · Turbo → เทอร์โบ · ESC → ESC
· **ลำดับคำไทยของชื่อสินค้า/ชิ้นส่วน**: ภาษาไทยวางคำหลักไว้หน้า คำขยายไว้หลัง — `White Alloy` → **อัลลอยขาว** (ไม่ใช่ "ขาว อัลลอย") · `Black Chariot` → ชาริออตดำ · `S Motor` → มอเตอร์ S (เว้นวรรคเฉพาะตอนคำขยายเป็นอักษรละติน/ตัวเลข) · `Adamant Clover` → อดาแมนต์ลายใบโคลเวอร์ (ซีรีส์นำหน้า ไม่เว้นวรรค) — lead แก้ย้อนหลังใน batch 112/113 แล้ว 94 คีย์
· **thumb turn bypass มีสองรูปตามตำแหน่ง**: ป้ายสั้น (คีย์เดี่ยว ๆ คู่กับ Lock Picking → งัดกุญแจ) → **เลี่ยงกลอนบิด** · ในประโยคอธิบายสกิล → การเลี่ยงสลักล็อกแบบบิดนิ้วโป้ง (ผู้ตรวจ batch_117)
· ⚠ ไฟล์นี้ถูกกันออกจาก `normalize_terms.py` แล้ว (21 ส.ค. 2026) เพราะการกวาดคำเคยเปลี่ยน "ตัวอย่างคำที่ห้ามใช้" ให้กลายเป็นคำถูก จนบรรทัดเตือนอ่านไม่รู้เรื่อง — เขียนตัวอย่างคำผิดในไฟล์นี้ได้ตามปกติ
· **คีย์ที่ใช้ซ้ำหลาย bin**: ก่อนแก้คำแปลของคีย์สั้น ๆ ให้เช็ค `python scripts/make_multibin_index.py --key "<คีย์>"` (รายชื่อเต็ม `docs/reference/multibin_keys.md` 1,650 คีย์) — เช่น `Medium` เป็นทั้งทรงผมคาบาเรต์และระดับกราฟิก · `Up` เป็นทั้งทรงผมและปุ่มทิศทาง → ต้องใช้คำกลาง ๆ ที่ใช้ได้ทุกบริบท
· **นามสกุลลงท้าย -guchi → กูจิ เสมอ** (Kamaguchi = คามากูจิ · Taguchi = ทากูจิ · Iguchi = อิกูจิ · Kawaguchi = คาวากูจิ) — ผู้ตรวจ batch_118 เจอหลุดซ้ำ
· **มาโคโตะ (ชาวเมือง/คู่แข่งโป๊กเกอร์) ใช้ทะเบียน T3 (กู/มึง)** ตามคำที่ ship แล้ว — lead ยืนยัน 21 ส.ค. 2026 ให้คงทะเบียนเดิมทั้งตัวละคร ห้ามลดระดับเป็นราย ๆ (สลับทะเบียนกลางคันแย่กว่า)
· **Shoot (ชนิดลูกขว้างเบสบอล judge_shuuto) → ชูต** ห้ามแปลว่า "ยิง" (ref_tm ต้นทางผิด · สอดคล้องกับ Shootball → ชูตบอล ที่ K3 ship แล้ว)
· `ESC` + คำขยายไทย **ต้องเว้นวรรคเสมอ** (ESC ความเร็วแสง · ESC ต้นทุนต่ำ) · `Cartoon` → การ์ตูน แยกจาก `Anime` → อนิเมะ (ต้นฉบับใช้คนละคำ ไทยต้องแยกตาม — lead ตัดสิน 21 ส.ค. 2026)
· **Chatter (แอป SNS) คง EN ยืนยัน 21 ส.ค. 2026** — เคยมีรูปทับศัพท์ "แชตเตอร์" ship ไป 5 จุด lead แก้ย้อนหลังเป็น EN แล้ว (แนวเดียวกับ Dice & Cube · Paradise VR · KamuroGo · Quickstarter)
· **Stijl (ชื่อบาร์) → สติล** — K3 และ Gaiden ล็อกรูปนี้ไว้แล้วทั้งคู่ จึงชนะตามลำดับความสำคัญ glossary (K3 > Gaiden > …) · (lead เคยตัดสินให้คง EN ตอนบ่าย 21 ส.ค. 2026 เพราะกลัวชนคำว่า "สไตล์" — ยกเลิกคำตัดสินนั้น ผู้ตรวจ batch_120 หา precedent เจอทีหลัง)
· Honmaruen → **ฮนมารุเอ็น** (ไม่ใช่ ฮอนมารุเอ็น) · blackjack → **แบล็กแจ็ก** (ก ไม่ใช่ ค)
· ฝาแฝดของ Ryo = **พี่ชายฝาแฝด** (ตาม characters_side.json — ผู้ตรวจ batch_120 เจอแปลเป็นน้องชาย)
· **คำว่า "Pick" แยกตามระบบ** (ผู้ตรวจ batch_123 เสนอ): เครื่องมืองัดกุญแจ → **ปิ๊ก** (`Move Pick Left/Right` = เลื่อนปิ๊กซ้าย/ขวา) · เคอร์เซอร์ตู้คีบตุ๊กตา → เลื่อนตัวคีบ · เคอร์เซอร์เมนู → เลื่อนเลือก
· `Drone Shooting` = โหมด **ยิง** ด้วยโดรน (ไม่ใช่ถ่ายภาพ) แยกจาก `Drone Photo` → ภาพถ่ายโดรน · `Chase Action / Catch` = ปุ่มเดียวกับ `Chase and Capture` → **จับกุม**
· ศัพท์ไพ่ที่ล็อกเพิ่ม (ผู้ตรวจ batch_099): Yakuhai → ยากุไห · Kazehai → คาเซไห · Renpuuhai → เรนปูไห · Double Riichi → **รีชคู่** · Open Riichi → **รีชเปิด** · Insurance → อินชัวรันส์ · Six-Card Charlie → ซิกซ์การ์ดชาร์ลี · Green Card → กรีนการ์ด · Little Blind → ลิตเทิลบลายด์ (ห้าม "สมอลบลายด์")
· หมายเหตุ Round: **โป๊กเกอร์/มินิเกมไพ่ = ยก** (`End the round.` → จบยกนี้) ส่วน "รอบ" ที่เห็นใน master มาจากบทพูดคัตซีน (`auth.bin`) คนละบริบท ไม่ขัดกัน — ตรวจแล้ว 21 ส.ค. 2026
· **ฟีดโซเชียลในเกม (`popup_frame.bin` · `qsearch_*` · โพสต์ในมือถือ)**: แปล display name เป็นไทย แต่ **คง `@handle` เป็นอักษรละตินเดิม** · เวลาแบบ "4h ago" → "4 ชม.ที่แล้ว" (บรรทัดฐานจาก batch_125 · lead รับ 21 ส.ค. 2026)
· **สถานีตำรวจคามุโร**: EN แยกทะเบียนเอง — `Kamuro Police Station` (ทางการ) → สถานีตำรวจคามุโร · `Kamuro police station` ในบทพูด (ภาษาปาก) → โรงพักคามุโร · **คงความต่างไว้ ไม่ต้องยุบ** (lead ตัดสิน 21 ส.ค. 2026)
· Cover Spot → **จุดกำบัง** (ห้าม "จุดหลบซ่อน") · Caution Gauge → **เกจระวังตัว** (ล็อกรูปเดียว จากเดิม master มี 3 รูป)
· `Valhalla Land` → **วัลฮัลลาแลนด์** (ไม่มี precedent ที่ไหนเลย — lead ตัดสินตามกฎ §11 ให้ทับศัพท์ 21 ส.ค. 2026) · `Wife Eye` **คง EN** (มุกเล่นคำ wife≈wifi) · `UFO Catcher` คง EN · Goto → โกโต้ (K3/Gaiden ล็อก)
· **Quickstarter คง EN ทุกจุด** รวมคีย์เดี่ยว (เดิม batch_091 แปลว่า "เริ่มต้นด่วน" จุดเดียว ขัดกับทุกประโยคที่ ship แล้ว — lead แก้ย้อนหลัง 21 ส.ค. 2026)
· ⚠ แก้ข้อมูลเก่าใน §13: **Hug Bomb → ระเบิดกอด** (ตามที่ ship จริงใน master_th) ไม่ใช่ "คง EN" ตามที่เคยเขียนไว้
· `L'Amant` (เคาน์เตอร์แลกของ Dragon's Palace) → **ลามองต์** · **`caba_sora` / `caba_hikaru` (ซับจีนอ้าง 桐生先生 = คิริว) = เนื้อหาค้างจากเอนจิ้นร่วม คงต้นฉบับจีนเป๊ะ ห้ามแปล** — ผู้ตรวจ batch_114/127 ยืนยันจากไฟล์เกมทั้งสองรอบ (ref_tm มีคำแปลไทยให้ก็ห้ามใช้)
· ⚠ แก้ข้อมูลเก่าใน §📇: **Kajihira Group → กลุ่มคาจิฮิระ** (เดิมเขียนว่าคง EN) — ที่ ship จริงเป็นไทย 130 จุด vs EN 22 จุด · lead แก้ย้อนหลังให้เป็นไทยทั้งหมด 21 ส.ค. 2026
· **เนื้อหาค้างจากภาคอื่นในตารางเดียวกัน (ยืนยัน 21 ส.ค. 2026)**: `sub_a13`/`sub_a14` มีตาราง speaker ชื่อ `paul` = เควสต์ปาเป้า "Legendary Paul Lim" ของ **Yakuza Kiwami 2** (บทเรียกตัวเอกว่า 桐生/คิริว) · `caba_sora`/`caba_hikaru` = ซับจีนของ Y6 · ทั้งหมดไม่มีใน `speech_speaker_map.json` (ดัชนีบทพูดมีเสียง 15,054 บรรทัด) = **เกมไม่เรียกใช้ ผู้เล่นไม่เห็น** → บทจีนคงต้นฉบับ · บท EN แปลตรงตัวไปตามปกติ ไม่ต้องแก้ชื่อคิริวเป็นยากามิ
· Kaoru Ichinose → **อิจิโนเสะ** (ไม่มี ะ กลาง) · Ren/Ren-chan → เหริน/เหรินจัง (คนละคำกับ เร็น ของ Gaiden) · Kon-chan → คอนจัง · Madonkadonk → มาดองกาดองก์
· Kaede → **คาเอเดะ** · Cipher Secrets → **ปริศนารหัสลับ** · Mind over Matter → จิตเหนือกาย · Brains over Brawn → ปัญญาเหนือพลัง (ship แล้วจาก batch_124 แต่ไม่มีในตาราง จน batch_126 พลาดซ้ำ)
· **`save_data_detail.bin` มีป้ายเดียวกัน 5 ภาษา (EN/DE/FR/ES/IT)** — แปลเป็นไทยข้อความเดียวกันทุกภาษาได้ ปลอดภัย (เป็น label ตามค่า ไม่ใช่ตำแหน่ง) · หมายเหตุ: ไฟล์เกมเองสลับคอลัมน์ `text_for_fr` กับ `text_for_de` ทุกแถว จะแปลตามคอลัมน์ภาษาไม่ได้อยู่แล้ว (ผู้ตรวจ batch_126 ยืนยัน)
· **Play Pass → เพลย์พาส** ล็อกรูปเดียว (เดิม master มี 3 รูป) · D-League → ลีกโดรน · LEGEND (ระดับความยาก) → เลเจนด์ · Twisted Trio → คดีสามโรคจิต
· ชื่อร้าน/เกมอาร์เคดสมมติ **ทับศัพท์ตามกฎ §11** (lead รับข้อเสนอผู้ตรวจ batch_133): Hyper Win Game → ไฮเปอร์วินเกม · Bar Ozakeyo → บาร์โอซาเคโย · แต่ `G.I.` **คง EN** เพราะบทพูดอ่านเป็นตัวอักษรทีละตัว
· ชื่อล็อกเพิ่ม: Ishimatsu → อิชิมัตสึ · Mari → มาริ · Asuka Hachitani → อาซึกะ ฮาจิทานิ · Hideaki Deguchi → ฮิเดอากิ เดกุจิ · Hoshino(-kun) → โฮชิโนะ(คุง)
· **คำเรียกผู้ฟังหญิงใช้ "คุณ" ห้าม "นาย"** (ผู้ตรวจ batch_132 เจอยากามิใช้ "นาย" กับนานามิ/สึคิโนะ 3 จุด)
· **ปุ่มคาสิโน (ต้องตรงกันระหว่างปุ่มบนจอกับบทพูดที่อ้างถึงปุ่ม)**: Hit → ตี · Stand → อยู่ · Fold → โฟลด์ · Call → คอล · Raise → เรส · Bet → เดิมพัน · **Check → เช็ก** (แก้จาก "เช็กบิล" ซึ่งเป็นบริบทร้านอาหาร — ไฟล์เกมวางคีย์นี้ไว้ข้าง Call/Fold/Raise = แอ็กชันโป๊กเกอร์) · Double Down → เพิ่มเดิมพันเท่าตัว · Split → แยกไพ่ · Surrender → ยอมแพ้ · Total → รวม
· **Ryan Acosta (เพื่อน #5 คอสเพลย์นินจา) ใช้ทะเบียนโบราณ ข้า/เจ้า** — บท EN เล่นมุกซามูไร/อนิเมะ ('Twould · thy · "Believe it!") lead รับข้อเสนอ 21 ส.ค. 2026 · เป็นข้อยกเว้นเฉพาะตัวละครนี้ (เหมือนบทคาเฟ่แวมไพร์) ห้ามลามไปตัวอื่น
· `Kasho Zoku` (บาร์เหนือ Heavy Coffee) → **คาโชโซกุ** · `Heavy Coffee` → **เฮฟวี่คอฟฟี่** (ตรงกับที่ ship แล้ว 4 จุด) · ชื่อคาเฟ่/บาร์ทับศัพท์เสมอ ต่างจากแบรนด์จริงอย่าง Don Quijote ที่คง EN
· ⏳ **`friend_hatano` (คนขายถุงมือเบสบอล) ยังพิสูจน์เพศไม่ได้** — `characters_side.json` ร่างไว้ว่า "ผม" แต่ `gender_evidence_judge.md` ระบุ unknown · บทของเขาใน TALK_001 ไม่มีหลักฐานเพศเพิ่ม → **ให้เลี่ยงสรรพนามต่อไป** จนกว่าจะเจอหลักฐาน
· Free Pass Voucher → **บัตรผ่านฟรี** (ล็อกรูปเดียว) · Shinano → ชินาโนะ · Ota → โอตะ · Tsunawatari → สึนาวาตาริ · เพลง "Amidst a Dream" → ท่ามกลางความฝัน · มุก `nice dice` (ล้อชื่อ Naisu Daisu) คง EN ยอมสูญมุกไทย
· ชื่อไซด์เคสที่ล็อกเพิ่ม (ผู้ตรวจ TALK_005/006): Mamoru Shimazu → มาโมรุ ชิมาซึ · Yukako (Oki) → ยูกาโกะ (โอกิ) · Naoko → **นาโอโกะ** (ตรงกับที่ ship แล้ว) · Kotaro Hyuga → โคทาโระ ฮิวกะ · "Hinata" เดี่ยว ๆ → ฮินาตะ (ใส่ฉายาเต็มเฉพาะตอน EN เขียนเต็ม) · Hasegawa (เจ้าของหอ A21) ⏳ เพศ unknown (voicer=0) ให้เลี่ยงสรรพนามต่อไป
· **Sotenbori → โซเท็นโบริ** (ย่านโอซากะจากภาคอื่น — รูปที่ ship แล้วใน K3/Gaiden 737 จุด) · Building One → บิลดิ้งวัน · Steel Plate = Iron Plate = **เพลทเหล็ก** (คันจิ 鉄 ตัวเดียวกัน)
· `Kamuro of the Dead` (ตู้ยิงซอมบี้) คง EN — ชุดคำ UI ของตู้นี้ (Combo · Head Shot! · Reload! · Normal hit: · Critical hit: · Shake them off!!) เป็นคนละระบบกับ Chase/Capture ห้ามเอาคำล็อกไล่ล่ามาใช้
คำล็อกเพิ่ม 21 ส.ค. 2026 (ผู้ตรวจ batch_109 เสนอ · lead รับ): Majima Saga → **มาจิม่าซากะ** (ห้าม "มาจิม่าซากะ") · Emerge (ระบบสะกดรอย คู่กับ Hide → ซ่อน) → **โผล่ออกมา** ห้ามแปลว่า "ขึ้นผิวน้ำ" · Runs (สถิติเบสบอลศูนย์ฝึกตี คู่กับ Hits → จำนวนฮิต) → **จำนวนรัน** ห้ามแปลว่า "คะแนนวิ่ง"
ระบบไล่ล่า (ล็อก 21 ส.ค. 2026 — ผู้ตรวจ batch_110 เสนอ · lead รับ): Chase / Chasing → **การไล่ล่า** (ห้าม "การไล่ตาม") · **Capture (ปุ่มในระบบ Chase) → จับกุม** ห้ามแปลว่า "ถ่ายภาพ" (คนละระบบกับ Check the photo) · The Chase Begins! → การไล่ล่าเริ่มขึ้น!
คำล็อกเพิ่ม 21 ส.ค. 2026 (ผู้ตรวจ batch_103/104 เสนอ · lead รับ — ทั้งหมด ship แล้วหลายจุดแต่ยังไม่เคยอยู่ในตาราง จึงหลุดซ้ำ): Renji Honda → **ฮอนดะ** (ห้าม "ฮอนดะ") · Wild Jackson → **ไวลด์แจ็คสัน** (ไม่มีช่องว่างกลาง) · Saito → **ไซโตะ** · Karin-chan → คารินจัง · Tenkaichi Alley → **ซอยเทนไคจิ** · Mantai Internet Cafe → **ร้านอินเทอร์เน็ตคาเฟ่มันไท** — normalize_terms.py กวาดให้อัตโนมัติทุกคำ
ชื่อสถานที่ล็อกเพิ่ม 21 ส.ค. 2026 (ผู้ตรวจ batch_102 เสนอ · lead รับ): Senryo Avenue → **ถนนเซ็นเรียว** (รูปที่ ship แล้ว 19 จุด ชนะ "ถนนเซ็นเรียว" ของ glossary_k2 เก่า · normalize_terms กวาดให้อัตโนมัติ) · Showa Street → ถนนโชวะ · Cherry (ร้านทำผม) → เชอร์รี่ · Children's Park → **สวนเด็ก** (ห้าม "สวนเด็ก")
**Koi-koi**: ชื่อเมนู/ชื่อเกม → คง EN · ศัพท์ในตัวกติกา (โคอิ ฯลฯ) → ทับศัพท์ไทยได้ (lead รับรอง 21 ส.ค. 2026)
**ชื่อคดีชุด Mad Bomber (ต้องต่างกันตาม EN — ห้ามยุบเป็นรูปเดียว)**: The Mad Bomber → มือระเบิดบ้าคลั่ง · Kamurocho's Mad Bomber → มือระเบิดบ้าคลั่งแห่งคามุโรโจ · The Mad Bomber Strikes → มือระเบิดบ้าคลั่งลงมือ · The Mad Bomber Strikes Again → มือระเบิดบ้าคลั่งลงมืออีกครั้ง · Return of the Mad Bomber → มือระเบิดบ้าคลั่งหวนคืน

## §13 ศัพท์มาจอง/ระบบเพิ่มเติม (ล็อก 21 ส.ค. 2026 — นักแปล batch_100 เสนอ · lead รับ)
oka → โอกะ · uma → อุมะ · kan → คัง · chi → ชี · pon → ปง · kandora → คังโดระ · dora/uradora → โดระ/อุระโดระ · tenpai → เทนไพ · ippatsu → อิปปัตสึ · yakuman → ยากุมัง · han → ฮัง · kuitan → คุยตัน · atozuke → อาโตซึเกะ · dealer (มาจอง) → เจ้ามือ · seven pairs → คู่เจ็ดคู่ · no-points hand → มือไร้แต้ม · all simples → ไพ่ธรรมดาล้วน
Threat Level → ระดับภัยคุกคาม · Valuables → ไอเทมมีค่า · Hangout Spot(s) → แหล่งพบปะ · Instant Mission(s) → ภารกิจด่วน · Ebisu Pawn → โรงจำนำเอบิสุ · Yoshida Batting Center → ศูนย์ฝึกตีโยชิดะ
**debug string ที่เป็นภาษาจีน/ญี่ปุ่นล้วน** (ยืมจากเอนจิ้นร่วม เช่นบทของ JUSTIS/幸子/SORA · มี prefix `sample_`) → **คงต้นฉบับไว้ ไม่แปล** (ไม่ได้ใช้จริงในเกม และการแปลทำให้ด่าน C ของ QC ตก)
Ari-ari Ruleset → กติกาอาริ-อาริ · sacred discard → ไพ่ศักดิ์สิทธิ์ · NPC บนแมป: โคกะ · ฮอนดะ · คาไซ · ซากากิบะ (⏳ "Sakakiba" อาจเป็นรูปย่อของ Sakakibara — ยืนยันเมื่อเจอบริบทเพิ่ม)
Dragon's Palace → **วังมังกร** (ship แล้ว 6 จุด — ห้าม "วังมังกร") · Dragon's Palace Key → กุญแจวังมังกร · Ebisu Pawn → โรงจำนำเอบิสุ · Bar Tender (ร้านของโจ มาสึดะ) → บาร์เทนเดอร์
2D code → โค้ด 2 มิติ · Skill Book → ตำราทักษะ · Ferocity of the Tiger → ความดุร้ายแห่งเสือ · Leapfrog → กระโดดข้าม · Charging Tiger → เสือสะสมพลัง · Knockdown Reversal → พลิกสถานการณ์จากการล้ม · Dire Determination → ความมุ่งมั่นสุดขีด · Nyan Nyan Café → คาเฟ่เนียนเนียน · Pigeon (โดรน) → พิเจียน · Directory (ป้ายรายชื่อในตึก) → แผนผังอาคาร · material witness → พยานปากสำคัญ
**Quickstep**: ชื่อสกิล (Quickstep Strike · Double Quickstep) → **คง EN** ตามที่ ship แล้ว · ในประโยคอธิบายวิธีเล่น → **ควิกสเต็ป** (lead ตัดสิน 21 ส.ค. 2026)
calamity ของอามาเนะ: black → ลางร้ายรูปดำ · black-and-white → ลางร้ายรูปขาวดำ · fire → ลางร้ายรูปไฟ (แพทเทิร์นเดียวกับ cow → ลางร้ายรูปวัว)
⚠ typo ในไฟล์เกมต้นฉบับ: **"Matsunage-san" = "Matsugane-san"** (มัตสึกาเนะซัง) · **"Naname" = "Nanami"** (นานามิ) — แปลตามเจตนา
Adachi Estates → อาดาจิ เอสเตท · Kiguchi Real Estate → คิกุจิ เรียลเอสเตท · Volcano (ปาจิงโกะ) → โวลเคโน · Higurashi → ฮิกุราชิ · Shin Amon → ชิน อามอน · Ushimata → อุชิมาตะ · -sama → ท่าน (Bram-sama → ท่านแบรม)
Jester (โค้ดเนมคู่กับ Crow) → เจสเตอร์ · Kamuro Hills → คามุโรฮิลส์ · Kamuro Theater Garden → สวนโรงละครคามุโร · Detention Center → ศูนย์กักขัง · Tokyo Detention Facility → ศูนย์กักขังโตเกียว · Taguchi → ทากูจิ
⚠ typo ในไฟล์เกม: **"Kuwada-san" = "Kawada"** (โทโมคาซึ คาวาดะ · ไซด์เคสไขรหัสเซฟที่คาเฟ่มิโจเระ) → แปลเป็น "คาวาดะซัง" ทั้งชุด
Pigeon (โค้ดเนมโดรน) → **นกพิราบ** (ไม่ใช่ "พิเจียน") · "the dealer" ในสาย Keihin Gang → **คนขายปืน** (ไม่ใช่ "คนขายยา" — ยืนยันจาก missions.json idx 1752-1753) · Rei Miyamoto → **เรย์ มิยาโมโตะ** (กฎ -ei = เ-ย์)

### §13.1 ชื่อ yaku มาจองครบชุด (ล็อก 21 ส.ค. 2026 — batch 115/116/117 แปลครบเป็นครั้งแรก · ผู้ตรวจยืนยันความนิ่งทั้งตาราง)

| EN | ไทย |
|---|---|
| `4x Yakuman` | ยากุมัง 4 เท่า |
| `5x Yakuman` | ยากุมัง 5 เท่า |
| `6x Yakuman` | ยากุมัง 6 เท่า |
| `7x Yakuman` | ยากุมัง 7 เท่า |
| `All Green` | ริวอีโซ |
| `All Honors` | สึอีโซ |
| `All Simples` | ไพ่ธรรมดาล้วน |
| `All Terminals` | ชินโรวโท |
| `All Terminals and Honors` | ฮนโรวโท |
| `All Triplet Hand` | โทอิโทอิ |
| `Big Four Winds` | ไดซูชี |
| `Big Three Dragons` | ไดซังเง็น |
| `Big Wheel` | ไดชาริน |
| `Blessing of Man` | เร็งโฮ |
| `Broken Thirteen` | สิบสามพลาด |
| `Dead Wall Draw` | รินชันไคโฮ |
| `Dora` | โดระ |
| `Double East` | ตะวันออกคู่ |
| `Double Identical Sequences` | เรียงเปโค |
| `Double North` | เหนือคู่ |
| `Double Riichi` | รีชคู่ |
| `Double South` | ใต้คู่ |
| `Double West` | ตะวันตกคู่ |
| `Double Yakuman` | ยากุมังคู่ |
| `Earthly Hand` | ชีโฮ |
| `Four Concealed Triplets` | ซูอังโค |
| `Four Concealed Triplets w/ Single Wait` | ซูอังโค รอเดี่ยว |
| `Four Quads` | ซูคันสึ |
| `Full Flush` | ชินอิตสึ |
| `Full Straight` | อิกคิสึคัง |
| `Fully Concealed Hand` | เมนเซ็นสึโม |
| `Green Dragon` | มังกรเขียว |
| `Half Flush` | ฮงอิตสึ |
| `Heavenly Hand` | เท็นโฮ |
| `Higashi` | ฮิงาชิ |
| `Identical Sequences` | อีเปโค |
| `Ippatsu` | อิปปัตสึ |
| `Last Tile Discard - Ron` | ทิ้งไพ่ตัวสุดท้าย - รอน |
| `Last Tile Draw - Tsumo` | จั่วไพ่ตัวสุดท้าย - สึโม |
| `Little Four Winds` | โชวสึชี |
| `Little Three Dragons` | โชซังเง็น |
| `Mixed Outside Hand` | ชานตะ |
| `Nine Gates` | ชูเร็นโปโต |
| `No-Points Hand` | มือไร้แต้ม |
| `North` | เหนือ |
| `Open Riichi` | รีชเปิด |
| `Pure Nine Gates` | ชูเร็นโปโตแท้ |
| `Pure Outside Hand` | จุนจัง |
| `Pure Thirteen Orphans` | โคคุชิมุโซแท้ |
| `Red Dragon` | มังกรแดง |
| `Riichi` | รีช |
| `Robbing a Quad` | ชังกัง |
| `Seven Pairs` | คู่เจ็ดคู่ |
| `South` | ใต้ |
| `Terminal Discard` | ทิ้งไพ่ขอบ |
| `Thirteen Orphans` | โคคุชิมุโซ |
| `Three Color Straight` | ซันโชกุโดจุง |
| `Three Color Triplets` | ซันโชกุโดโค |
| `Three Concealed Triplets` | ซันอังโค |
| `Three Consecutive Pons` | ปงเรียงสามชุด |
| `Three Quads` | ซันคันสึ |
| `Triple Yakuman` | ยากุมังสาม |
| `West` | ตะวันตก |
| `White Dragon` | มังกรขาว |
| `Yakuman` | ยากุมัง |

### §14 ฟิลเตอร์กล้อง + ศัพท์กราฟิก (ล็อก 21 ส.ค. 2026 · batch_124 · ผู้ตรวจรับรอง)

| EN | ไทย |
|---|---|
| `2bit Retro` | เรโทร 2 บิต |
| `Candlelight.cud` | Candlelight.cud |
| `Cheery` | ชีรี |
| `Dawn` | ดอว์น |
| `Emotional` | อีโมชันแนล |
| `Hellscape` | เฮลสเคป |
| `Ice Cold` | ไอซ์โคลด์ |
| `Lemon` | เลมอน |
| `Monochrome` | โมโนโครม |
| `Moody` | มู้ดดี้ |
| `Noir` | นัวร์ |
| `Nostalgic` | นอสแทลจิก |
| `Peridot` | เพอริดอต |
| `Red Blues` | เรดบลูส์ |
| `Ruby` | รูบี้ |
| `Sapphire` | แซฟไฟร์ |
| `Scorching` | สกอร์ชิง |
| `Sepia` | ซีเปีย |
| `Smokey` | สโมกกี้ |
| `Sunset` | ซันเซ็ต |
| `Toy` | ทอย |
| `Verdant` | เวอร์แดนต์ |
| `Real Time Reflection` | การสะท้อนแบบเรียลไทม์ |
| `Volumetric Fog` | หมอกเชิงปริมาตร |
| `Detail Settings` | การตั้งค่ารายละเอียด |
| `Español` | สเปน |

**ยืนยันแล้ว 21 ส.ค. 2026 (ผู้ตรวจ batch_124 เทียบกับ `translations/slotmap.json` โดยตรง)**: อักษรละตินมีเครื่องหมายในข้อความกฎหมาย PSN (à á ã ä ç é ê í ñ ó ö ú ü) อยู่ในตาราง `reserved` ของ slotmap ไม่ได้ถูกจัดสรรให้กลิฟไทย → **ไม่มีความเสี่ยงขึ้นจอเป็นตัวมั่ว** · บล็อกภาษารัสเซียเป็นซีริลลิกล้วน อยู่นอกตาราง 384 เซลล์ของโหมด EN ตั้งแต่ก่อนม็อดอยู่แล้ว

## คำตัดสิน lead — sprint รอบสาม (คิว TALK_007-012) 21 ส.ค. 2026

**คำล็อกใหม่**
- Falco Edison (นักสืบในนิยายของคาตากิริ) → **ฟัลโค เอดิสัน** (ตัวละครในนิยาย = ทับศัพท์ ไม่คง EN)
- Gotoh Gateau (ร้านเค้กในคดี A37) → **โกโต้ กาโต**
- Kotatsu Higurashi → **โคทัตสึ ฮิกุราชิ** · Takumi Katagiri → **ทาคุมิ คาตากิริ** (ยืนยันกับรูปที่ ship แล้ว 10 จุด — ข้อเสนอ "คาทากิริ" ตกไป) · Hayama → **ฮายามะ**
- The Killing Lightbulb (ชื่อหนังสือ) → **ฆาตกรรมหลอดไฟ**
- "Hornata" (มุกผสม Horny + Hinata) → **ฮินาหื่น** (คงรูปผสมชื่อเหมือน EN · ฉายาเต็ม "Horny Hinata" ยังเป็น ฮินาตะจอมกำหนัด ตามที่ ship แล้ว)

**คำที่เคยล็อกแล้วแต่รอบนี้มีคนคิดรูปใหม่ — ใช้รูปเดิมเท่านั้น** (กวาดด้วย `normalize_terms.py` แล้ว)
- Higurashi → ฮิกุราชิ (ไม่ใช่ ฮิงุราชิ) · Horny Hinata → ฮินาตะจอมกำหนัด (ไม่ใช่ จอมหื่น)
- West Taihei Boulevard → ถนนไทเฮฝั่งตะวันตก · Zhuang Shi → จวง ซือ · Ruan Wang → หรวน หวัง
- Cloudy Skies Publishing → สำนักพิมพ์คลาวดีสกายส์ (**ห้ามคง EN** — ship แล้ว 9 จุด)

**คำหยาบ/ความอ่อนไหว**: `sissy` → **หน้าตัวเมีย** ห้ามใช้ "กะเทย" (คำเหยียดอัตลักษณ์ ไม่ใช่คำด่าความไม่แมนแบบที่ EN สื่อ)

**เพศที่ยืนยันเพิ่มรอบนี้**: Sakura Amamiya = หญิง · Manager (A44) = ชาย · Man in Black (A44) = ชาย · Makihara = ชาย · Hayama = ชาย (`scenario_summary.json` "He wants me to…") · Otoya Shijima = ชาย — รายละเอียดใน `docs/reference/gender_evidence_judge.md`

**สรรพนามในบทสวมบทบาท**: ตอนตัวละครเล่นบท "ท่านแบรม" (แวมไพร์) ใช้ "ข้า/เจ้า" ได้เฉพาะตอนชิจิมะพูดในบทจริง — ตอนยากามิปลอมตัวยังใช้ "ผม" ตามคำล็อกตัวเอก แต่ยกระดับคำศัพท์ให้โอ่อ่าแทน (มุกคือยากามิเล่นบทไม่เนียน)
**คำตัดสินเพิ่ม (ผู้ตรวจ TALK_009/010/012 รายงาน)**
- `Champion District` → **ย่านแชมเปี้ยน** เสมอ — **ไม่ได้อยู่ในกลุ่มทับศัพท์ทั้งชื่อ** แบบ Earth Angel/Shellac/Bantam
  (ผู้ตรวจ TALK_012 เจอ "แชมเปี้ยนดิสตริกต์" หลุดมา 3 จุด — สองบล็อกคำล็อกอยู่ใกล้กันจนสับสน)
- `Katagiri` → **คาตากิริ** (ต ไม่ใช่ ท) — ยึดรูปที่ ship แล้ว 10 จุด
- `-sensei` → **อาจารย์+ชื่อ** เสมอ (อาจารย์คาตากิริ · อาจารย์เก็นดะ) · เรียกลอย ๆ "Sensei" = อาจารย์ — **กลับกฎเดิม** ตามคำสั่งเจ้าของโปรเจกต์ 5 ก.ย. 2026 (กวาดทั้ง master แล้ว 342 บรรทัด)
- **ป้ายชื่อผู้พูดที่ระบุเพศในตัวเอง** ("Lost Boy" · "Young Female Customer") ใช้เป็นหลักฐานเพศได้
  → เด็กชายหลงทางในเควสมือระเบิดใช้ "ครับ" ได้ (ไม่ต้องเลี่ยงสรรพนาม)
- `Kenta Uozumi` → **เค็นตะ อุโอซึมิ** · `East Taihei Boulevard` → **ถนนไทเฮฝั่งตะวันออก** (ทั้งคู่ ship แล้ว)
- ข้อยกเว้นที่ยอมรับแล้ว: `Izumida` → **อิซุมิดะ** (ซุ ไม่ใช่ ซึ) — ship ไปแล้ว 60 จุด ไม่รื้อ · กฎ `zu→ซึ` ยังใช้กับชื่อใหม่ตามเดิม
- ล็อกชื่อ NPC เควสเพื่อนเพิ่ม (ใช้ตรงกันข้าม batch อยู่แล้ว แต่ยังไม่เคยล็อกเป็นทางการ): `Norimoto` → **โนริโมโตะ** · `Miharu Shima` → **มิฮารุ ชิมะ** · `Kim` (Beef Zone) → **คิม** · `Kanrai` → **คันไร** · `Beef Zone` → **บีฟโซน** · `Kenta Uozumi` → **เค็นตะ อุโอซึมิ** (มีไม้ไต่คู้ — ตกบ่อย มีกฎกวาดใน `normalize_terms.py` แล้ว)- `Kon-chan` (ชื่อเล่นของคนโดะ) → **คงจัง** ไม่ใช่ "คนจัง" (อ่านพ้องกับคำว่า "คน") · `Goro Moroboshi` → **โกโร โมโรโบชิ** (ชาย อดีตหมอ) · `Takemitsu` → **ทาเคมิตสึ** (ชาย ยืนยันจาก `voicer_gender.json`)
### กฎ honorific — ย้ำอีกครั้งเพราะพลาดบ่อยที่สุด (21 ส.ค. 2026)

**EN เขียน honorific ไว้ = ต้องทับศัพท์ต่อท้ายชื่อ** · "คุณ+ชื่อ" ใช้เฉพาะตอน EN **ไม่มี** honorific

| EN | ไทย |
|---|---|
| `Yagami-san` | **ยากามิซัง** (ship แล้ว 516 จาก 547 จุด) |
| `-kun` / `-chan` | คุง / จัง ต่อท้ายชื่อ |
| `-sensei` | **อาจารย์+ชื่อ** นำหน้า (อาจารย์เก็นดะ) — เปลี่ยน 5 ก.ย. 2026 |
| `Yagami` เปล่า ๆ | คุณยากามิ (หรือชื่อเปล่าตามความสนิท) |

ผู้ตรวจ TALK_017 เจอนักแปลพลาด **7 จาก 7 จุด** ใน batch เดียว เพราะกฎเดิมอยู่แต่ใน `characters_main.json`
กวาดทั้งโปรเจกต์ได้ด้วย `python scripts/fix_honorific_san.py --write` (แก้ตกค้างไปแล้ว 29 จุดใน 11 batch เก่า)
ข้อยกเว้นที่ ship แล้วและไม่รื้อ: `Yagami-sama` → **คุณยากามิ** (2 จุด)
**honorific `-shi` (氏)**: เป็นคำเรียกทางการแบบข่าว/เอกสาร ไทยไม่มีรูปเทียบ → **ตัดทิ้ง ใช้ชื่อเปล่า**
(สึคุโมะเรียก `Yagami-shi` → "ยากามิ" เฉย ๆ) · ตรงข้ามกับ `-san` ที่ต้องทับศัพท์เสมอ
`Meguro-san` → **เมกุโระซัง** (ship แล้ว 6/6 จุด)
- `Suguru` → **ซุกุรุ** (ス = ซุ ตามรูป `Sugiura` → **ซุกิอุระ** ที่ ship แล้ว · สึ สงวนไว้ให้ つ เช่น มัตสึกาเนะ/สึคุโมะ) — master เคยมี 2 รูปขัดกัน แก้แล้ว
- `Suguru Oka` → **ซุกุรุ โอกะ** · `Oka Detective Agency` → **สำนักงานนักสืบโอกะ** · `Judge Creep 'n Peep` → **ผู้พิพากษาจอมถ้ำมอง** (คำล็อกเดิม ห้ามคง EN)
- `Megumi Hashimoto` → **เมกุมิ ฮาชิโมโตะ** (คนละคนกับฮาชิโมโตะนักวิจัย ADDC — นามสกุลพ้องกันเฉย ๆ) · `Takefumi Hashimoto` → **ทาเคฟุมิ ฮาชิโมโตะ**
### กาแฟ Café Alps (ล็อกรวมไว้ที่เดียว — ผู้ตรวจ TALK_023 เจอหลุดเป็น EN 16 จุด)

`Café Alps` → **คาเฟ่อัลป์ส** (ห้ามใช้ `Café` ที่มีสระ é — ฟอนต์เกมเอาช่องนั้นไปวาดกลิฟไทยแล้ว)
`Blue Mountain` → บลูเมาน์เทน · `Jamaican` → จาเมกา · `Mocha` → โมคา · `Blended Coffee` → กาแฟเบลนด์
`Kona` → โคนา · `Toraja` → โตราจา · `Guatemalan` → กัวเตมาลา · `Java Robusta` → ชวาโรบัสต้า
⚠ ข้อความในแท็ก `<color=yellow>…</color>` ก็ต้องแปล — เป็นจุดที่คนลืมบ่อยเพราะดูเหมือนค่าระบบ

`Shun Isaka` → **ชุน อิซากะ** (ชาย · หลักฐาน `gender_evidence.json` คีย์ `friend_isaka`)
`Sagara` (บาริสต้า Café Alps) → **ซาการะ** (ชาย · bio ที่ ship แล้ว "he boasts an extensive knowledge of coffee")
- `Takeo Inose` → **ทาเคโอะ อิโนเสะ** · `Yasuhiro Furuya` → **ยาสึฮิโระ ฟุรุยะ** · `Kaede Sanada` → **คาเอเดะ ซานาดะ** (ชื่อต้นเพิ่งโผล่ครั้งแรกในคิว TALK นามสกุลล็อกไว้ก่อนแล้ว)
- `Top of Ocean` (เลิฟโฮเทล) → **คง EN** ตามที่ ship แล้วใน master (อย่าเพิ่งตั้งรูปทับศัพท์ใหม่)
- `Exhibitionism Emperor` (ฉายา G.I.) → **จักรพรรดิจอมโชว์** (รูปเดียว ห้ามใช้ "จักรพรรดิแห่งการเปลือยกาย")
- `Kamuro Theater` → **โรงละครคามุโร**
- ตระกูลคุวายามะ (คดี A45): `Kojiro Kuwayama` → **โคจิโร คุวายามะ** · `Shizue Kuwayama` → **ชิซึเอะ คุวายามะ** (ซ ไม่ใช่ ส) · `Kiriko Kuwayama` → **คิริโกะ คุวายามะ**
- มินามิ (คนร้ายคดี A45) พูด T1 "ผม" ตอนแฝงตัวเป็นพนักงานคาเฟ่ แล้วสลับเป็น T3 กู/มึง **เฉพาะตอนเปิดเผยตัว** — ห้ามสลับก่อนบรรทัดที่ EN หยาบจริง (สปอยล์)
### ศัพท์ชุด Smile Burger (คดีประกวด friend_a31) — ทับศัพท์ "สไมล์" ทั้งชุด ห้ามแปลเป็น "ยิ้ม"

ตามรูปที่ ship แล้ว `Legendary Smile Set` → **เซ็ตสไมล์ระดับตำนาน**
`Smile Contest` → การประกวดสไมล์ · `Smile Snapshot` → ภาพสแนปช็อตสไมล์ · `Smile Site` → เว็บไซต์สไมล์
`Smile Staff` → พนักงานสไมล์ · `Smile Rival` → คู่แข่งสไมล์ · `Very Best Smile Award` → รางวัลสไมล์ยอดเยี่ยมที่สุด
`Smile Sensei` → เซนเซสไมล์ · `Smile Intern` → เด็กฝึกงานสไมล์ · `Smile Tutoring` → ติวสไมล์
- `Kopi Luwak` → **โกปี ลูวัก** · `Asian palm civet` → **ชะมดเช็ดปาล์มเอเชีย** (มุกของยากามิที่เรียกผิดเป็น "ขี้แมว" คงไว้ตาม EN — ต้นฉบับก็เข้าใจผิดเอง)
- `Captain Cop` → **กัปตันตำรวจ** (ship แล้ว ห้ามทับศัพท์ "กัปตันคอป") · `Public Park Three` → **สวนสาธารณะสาม**
- **ตระกูลอามอน (Amon)**: `Shin Amon` → **ชิน อามอน** · ใช้สรรพนาม **ข้า/เจ้า** ได้ (สืบทอดคำล็อกจาก K3 ที่ `Jo Amon = ข้า/เจ้า`) — เป็นข้อยกเว้นของกฎ "ข้า/เจ้า เฉพาะบทพีเรียด" เพราะตระกูลนี้เป็นบอสลับสายนินจาข้ามภาคที่พูดโบราณทั้งซีรีส์
- ชื่อญี่ปุ่นลงท้าย **-ro ไม่ใส่ไม้เอก**: โทชิโร · ทัตสึโร · โคจิโร · ชินซาบุโร · **ชินทาโร** (ไม่ใช่ ชินทาโร่) · ยกเว้นคำทับศัพท์ทั่วไปอย่าง "ฮีโร่"
- `Jo Masuda` (เจ้าของบาร์เทนเดอร์) = **ชาย** (`voicer_gender.json` คีย์ `tender_master`) — ใส่ตารางเทียบชื่อใน `make_talk_speaker.py` แล้ว
- `Captain Cop transformation stick` → **ไม้แปลงร่างกัปตันตำรวจ**
- `Shintaro Okabayashi` → **ชินทาโร โอคาบายาชิ** · `Hayato Adachi` → **ฮายาโตะ อาดาจิ** · `Adachi Estate` → **อาดาจิ เอสเตท** · `Ushimata Family` → **ตระกูลอุชิมาตะ**
- **ไคโตะใช้ กู/มึง ได้เฉพาะตอนเล่นบทบาท** (เช่น แกล้งเมาเป็นเหยื่อล่อในคดี A28) — ไม่ใช่ทะเบียนปกติของเขา · คามากูจิใช้ **ฉัน/นาย** (T2) ตามบทจริง ไม่ใช่ ผม/ครับ
- `Kotatsu Higurashi` (บาร์กเกอร์ปากเสีย) = **ชาย** · ทะเบียน: **T2 (ฉัน↔แก)** ตอนคุยปกติ · **T3 (กู↔มึง) เฉพาะตอนขู่** — ตามที่ ship แล้วในคดี A41 (batch TALK_007)
- ปริศนาตัวเลขเวลาในเกม (เช่นโจทย์นาฬิกาคดี A10) **ไม่ต้องแปลงเป็น ทุ่ม/โมง** — กฎแปลงเวลาใช้กับเวลาจริงในเนื้อเรื่องที่มี AM/PM เท่านั้น
- `softcloud` (บริการอีเมลสมมติในเกม) → **คง EN** (แนวเดียวกับ Don Quijote/Chatter — ชื่อบริการดิจิทัลที่เขียนด้วยอักษรโรมันบนจอ)
- `M Side Cafe` → **เอ็ม ไซด์ คาเฟ่** (เป็นคีย์ที่ใช้ซ้ำหลาย bin — ห้ามคง EN)
- `Ryo Suzaki` → **เรียว สึซากิ** (ยึดรูปที่ ship แล้ว 6 จุด · ไม่ใช่ "ซุซากิ" แม้กฎ su=ซุ จะชี้อีกทาง — ของที่ ship ชนะเสมอ)
- `Toya` (ชื่อในชุดมาสคอตของโทคุนากะ) → **โทยะ**
- `Kenji Sunada` → **เค็นจิ ซุนาดะ** · `Junichi Fujinaga` → **จุนอิจิ ฟูจินางะ** · `Aoi` → **อาโออิ** (คดี A49)
- `G.A. Labs` (บริษัทของทาเทยามะ) → **จีเอ แล็บส์**
- `Kikunoya` (ร้านในคดี A12) → **คิคุโนยะ** (คนละคำกับ `Kamuro Kikunoya` ที่ล็อกไว้ก่อนหน้า) · `Hohashi` → **โฮฮาชิ** · `Tatsuo` → **ทัตสึโอะ** · `Maki` (คดี A36) → **มากิ** (หญิง · โทนสุภาพแต่น่าขนลุก คง ค่ะ/คะ แม้ตอนข่มขู่)
- `Songstress of Kamurocho` (ฉายาซานะ) → **นักร้องสาวแห่งคามุโรโจ** · `Ota` → **โอตะ** · `Kabata` = ชาย · `Kitamura` = ชาย (หลักฐาน EN ในบท)- `MaiTube` (ล้อ YouTube ในเกม) → **คง EN** (แนวเดียวกับ Chatter/softcloud)
### ชื่อช่องกระดาน Dice & Cube — ต้องตรงกับการ์ดสอนเล่นที่ ship แล้ว

`Dice Plus Space` → **ช่องเพิ่มลูกเต๋า** · `Dice Minus Space` → **ช่องลดลูกเต๋า** · `Battle Space` → **ช่องต่อสู้**
`Warp Space` → **ช่องวาร์ป** · `Gift Space` → **ช่องของขวัญ** · `Safe Space` → **ช่องตู้เซฟ** · `Drone Space` → **ช่องโดรน**
`Destruction Battle` → **ศึกทำลายล้าง** · `Knockout Battle` → **ศึกน็อกเอาต์** · `Bonus Challenge` → **โบนัสชาเลนจ์**
⚠ บทพูดของโคโระเนียงเคยคงชื่อช่องเป็นอังกฤษ ทั้งที่การ์ดสอนเล่นแปลไทยไปแล้ว — ผู้เล่นจะเห็นสองภาษาในหน้าจอเดียวกัน (แก้แล้ว 14 บรรทัด)
`Dice & Cube` (ชื่อเกม) → **คง EN**
- `Tsukino Saotome` → **สึกิโนะ ซาโอโตเมะ** (ก ไม่ใช่ ค — ship แล้ว 86 จุด) · `Daichi Ryuzenji` → **ไดจิ ริวเซนจิ** · `Yukikawa` → **ยูกิกาวะ**
- **ไดจิ ริวเซนจิ ใช้ "ข้า/เจ้า" ได้** — เป็นคนยุคปัจจุบันที่**สวมบทบาท**สุภาพบุรุษอังกฤษ/ขุนนาง (เข้าข่ายข้อยกเว้นเดียวกับท่านแบรม) · `Young Master` (คำที่ยูกิกาวะเรียกเขา) → **คุณชาย** · `my liege` → **นายหญิงของข้า**


### คำตัดสิน lead รอบสปรินต์สี่ 21 ส.ค. 2026 (ตรวจความสอดคล้องข้าม bin)

- **ชื่อทักษะที่ถูกอ้างในประโยคอื่นต้องใช้ชื่อไทยที่ล็อกไว้** — ข้อความแจ้งปลดล็อก
  ("...has unlocked X. Learn how to use it on the Skill App.") มาคนละ bin กับตารางชื่อทักษะ
  (`player_skill.bin`) นักแปลจึงคงชื่ออังกฤษไว้ แต่หน้าแอปทักษะในเกมแสดงชื่อไทย ผู้เล่นหาทักษะไม่เจอ
  แก้แล้ว 6 บรรทัดใน batch_097 (Re-guard → ตั้งการ์ดใหม่ · EX Frontal Beatdown → EX ถล่มด้านหน้า ฯลฯ)
  ตรวจซ้ำด้วย `python scripts/check_skill_name_quotes.py` (ใส่ `--write` เพื่อแก้)
- **Skill App → แอปทักษะ เท่านั้น** (เดิมหลุดเป็น "แอปสกิล" 3 จุดใน batch_096) — เพิ่มกฎใน `normalize_terms.py` แล้ว
- `Serenade` (ร้าน/บาร์ที่ถูกพูดถึงใน Chatter) → **เซเรเนด** (ตาม §11 ชื่อร้านทับศัพท์ไทย)
- `Top of Ocean Hotel` (เลิฟโฮเทลในคดี) → **ท็อปออฟโอเชียนโฮเทล** (บรรทัดฐาน K3: "เรดบริก เลิฟโฮเทล")
- `Clan Creator` → **คง EN** (ยืนยันตรงกับที่ ship แล้วทั้ง Y6 และ Gaiden)
- ⏳ **ค้างให้ lead รอบหน้าตัดสิน**: ตระกูลสกิล Quickstep — glossary บรรทัด 498/560 ล็อกว่า "คง EN
  ตามที่ ship แล้ว" แต่ **Gaiden ship จริงเป็น "ควิกสเต็ปสไตรก์"** (ทับศัพท์) และในเกมนี้ชื่อทักษะ
  156 จาก 159 ตัวเป็นไทย เหลือ EN แค่ 3 ตัวของตระกูลนี้ — ถ้าจะพลิกต้องใช้เครื่องมือที่ไม่แตะคีย์ EN
  (`normalize_terms.py` แทนที่ทั้งไฟล์ ใช้กับคำละตินไม่ได้ จะทำคีย์พัง)
- ⏳ `"Flight"` ในบรรทัด `(I need to pick "Flight" to fly the drone.)` — ปุ่มจริงในแอปโดรน **ไม่มี
  string ใน db par** (ค้นทุก bin แล้ว) จึงยังไม่รู้ว่าบนจอเป็นไทยหรืออังกฤษ · ตอนนี้คงรูป EN ไว้
  แต่ข้อความช่วยเหลือแปลเป็น "การบิน" แล้ว — ต้องให้ผู้ใช้ยืนยันจากจอจริงก่อนเลือกทางใดทางหนึ่ง

### กวาดชื่อที่ล็อกแล้วให้ตรงกันข้าม bin (สปรินต์สี่ 21 ส.ค. 2026 · แก้ 44 จุดใน 6 batch)

**คลาสบั๊ก**: ตารางชื่อ (ไอเทม/ร้าน/คอร์ส) กับประโยคที่อ้างถึงชื่อนั้นอยู่คนละ bin คนละ batch
นักแปลที่ทำประโยคไม่รู้ว่าอีก batch แปลชื่อเป็นไทยไปแล้ว → ผู้เล่นเห็นสองภาษาในหน้าจอเดียวกัน
เครื่องมือ: `python scripts/fix_locked_name_quotes.py` (ใส่ `--write` เพื่อแก้ แล้ว merge ใหม่ทุก batch ที่ถูกแตะ)

- `Lullaby Mahjong` → **ลัลลาบายมาจอง** · `Modern Mahjong` → **โมเดิร์นมาจอง**
  (ตัวตารางเองเคยแปลความหมายเป็น "มาจองกล่อมนอน"/"มาจองสมัยใหม่" ขัด §11 — แก้แล้วทั้งตารางและประโยค)
- `Hug Bomb` → **ระเบิดกอด** (+ สปาร์คอัลฟา/สปาร์คเบตา/เอ็กซ์โพลชันโอเมกา) · `Staminan X` → **สตามินัน X**
  (รูปที่ ship แล้วทั้ง K3 และ Gaiden) · `Amidst a Dream` → **ท่ามกลางความฝัน**
- `Home Run Course` → **คอร์สโฮมรัน** · `Challenge Course` → **คอร์สท้าทาย** · `Koro-nyan` → **โคโระเนียง**
- `Beef Zone` → **บีฟโซน** (master ล็อกไว้ 3 บรรทัดตั้งแต่ batch ก่อน — นักแปล TALK_056 เผลอคง EN)
- **คง EN ทั้งในตารางและในประโยค**: `Wette Kitchen` · `Don Quijote` (สอง batch เคยแปลตัวตารางเป็นไทย
  ขัดคำล็อกเดิม — แก้กลับเป็น EN แล้ว) · `Motor Raid` · `Club SEGA` · `Fighting Vipers` ·
  `Virtua Fighter 5 Final Showdown` (แฟรนไชส์จริงของ SEGA)
- ⚠ **กับดัก multibin**: `Honey` ในตารางไอเทม = "น้ำผึ้ง" แต่ `Honey` ในบรรทัด Fighting Vipers คือ
  ชื่อตัวละครเกมอาร์เคด → **ห้ามแทนที่อัตโนมัติ** ต้องดูบริบทก่อนเสมอ

### เก็บตกจากผู้ตรวจ สปรินต์สี่ 21 ส.ค. 2026

- `Tsumugi` → **สึมุกิ** (ชื่อจริงของอามาเนะ) — พยางค์สลับเป็น "ซึกุมิ" ได้ง่ายมาก · ใส่กฎกวาดใน `normalize_terms.py` แล้ว
- `patriarch` (ยศยากูซ่า) → **หัวหน้าตระกูล** (ไม่ใช่ "ประมุขตระกูล")
- **การลากเสียงใน EN ที่สะกดสระซ้ำ** (`Takayuki-saaaan!`) → ลากด้วยพยัญชนะท้ายไทย **"ทาคายูกิซังงง!"**
  (ผู้ตรวจ TALK_054 รับรองเป็นบรรทัดฐาน — ปลอดภัยกว่าใช้ `~` ที่อาจชนแท็กระบบ)
- **ยากามิห้ามใช้ "แก" เด็ดขาด** แม้ตอนขู่/บลัฟ — ใช้ "นาย" แทน (ผู้ตรวจเจอซ้ำอีก 2 จุดใน TALK_056)

- `Ryuzenji Group` → **กลุ่มบริษัทริวเซนจิ** (ล็อก 21 ส.ค. 2026) — "ตระกูล" สงวนไว้ให้ครอบครัวยากูซ่า
  (มัตสึกาเนะ/เคียวเรอิ) เท่านั้น · ริวเซนจิเป็นทายาทธุรกิจพลเรือน · แนวเดียวกับ `Kajihira Group` → กลุ่มคาจิฮิระ
- `embondagement` (คำที่ริวเซนจิประดิษฐ์เอง bondage+betrothal) → **การจองจำรัก**

### เก็บตกรอบสี่ (ต่อ) — 21 ส.ค. 2026

- `Yukiko Tonegawa` → **ยูกิโกะ โทเนกาวะ** (g กลางคำ = ก ตามกฎ §0 · แนวเดียวกับ นาสึกาวะ)
- `*giggle*` → **\*หัวเราะคิกคัก\*** (รูปที่ ship แล้ว — ไม่ใช่ "\*ฟึฟึ\*")
- `lovebirds` → **สองคู่รัก** (ไม่ใช่ "คู่นกพิราบ" ตามตัวอักษร)
- **ตัวเลขใช้เลขอารบิกเสมอ** — "2 ล้านเยน" ไม่ใช่ "สองล้านเยน" (ผู้ตรวจ TALK_058/061 เจอคนละจุด)
- **คีย์ที่ใช้ทั้งใน `talk.bin` และคัตซีน (`auth.bin`/`sound_auth.bin`) ต้องแปลกลางไม่ผูกเพศ** —
  ผู้พูดคนละคนกันได้ · เคสจริงที่แก้แล้ว 8 จุด: `Excuse me.` → "ขอโทษนะ" · `Indeed.` → "ใช่แล้ว" ·
  `No, not really.` → "เปล่า ไม่คุ้นเลย" · `Lemme think...` → "ขอคิดดูก่อนนะ..." ·
  `You really think so?` → "คิดงั้นจริงๆ เหรอเนี่ย?" · `What about me?` → "แล้วเราล่ะ?" ·
  `Nope. Not at all.` → "เปล่า ไม่ได้เป็นห่วงเลย"
  (ตรวจด้วย `python scripts/check_speaker_gender.py` — ตอนนี้ master ผ่าน 0 จุด)

- `fuck you` (ยุกโกะพูดตอนโมโหแต่ยังเป็นเพื่อน) → **"ไปตายซะ"** (lead ยืนยัน 21 ส.ค. 2026 ตามรูปที่ ship แล้ว)
  — สงวน "ไอ้สัตว์/ไอ้เหี้ย" ไว้กับทะเบียนข่มขู่จริง (ยากูซ่า/อันธพาล) เท่านั้น · ตัวละครสายเพื่อนที่โมโห
  ให้ใช้คำแรงแบบเหน็บ ไม่ใช่คำแรงแบบขู่
- `batting center` → **สนามตีลูก** (ไม่มี "ซ้อม" ต่อท้าย · ship แล้ว 8 จุด)

- `crowdfunding` → **ระดมทุน** · `crowdfunding platform` → **แพลตฟอร์มระดมทุน** (ห้ามทับศัพท์ "คราวด์ฟันดิง")
  · แบรนด์ **`Quickstarter` คง EN** ตามเดิม — ที่ drift เพราะ glossary ล็อกแต่ชื่อแบรนด์ ไม่ได้ล็อกคำสามัญ
- `*cough cough*` (เสียงกระแอมใบ้) → **\*แฮ่ม แฮ่ม\*** (แนวเดียวกับ `*ahem*` → \*อาแฮ่ม\* ที่ ship แล้ว)
- ⏳ ข้อสังเกตตัวละคร: **โทมิโอกะ (เจ้าของตึก) เรียกยากามิว่า "เธอ"** ตลอดฉากโดยตั้งใจ (น้ำเสียงเจ้าของตึกวางท่า)
  — ไม่ใช่การผสมทะเบียน ถ้าจะล็อกให้ใส่ในไฟล์ตัวละคร

- **มาโดกะ (โฮสเตส Apple Pie) = "ฉัน"** ไม่ใช่ "หนู" (lead ล็อก 21 ส.ค. 2026 — โฮสเตสมืออาชีพคุยกับลูกค้า)
- **เรียว สึซากิ คง T1 (ผม/คุณ)** — ข้อเสนอขยับเป็น T2 ตกไป · ความขี้เมาสื่อผ่านถ้อยคำ ไม่ใช่ลดระดับสรรพนาม

- `extract` (ระบบคราฟต์ของอิยามะ) → **สารสกัด** ทุกจุด (ห้ามใช้ "ยาสกัด" — ผู้ตรวจ TALK_064 กวาด 38 จุด)
- `Scavenger Hunt` → **ภารกิจล่าของ** · `tengu` → **เทงงุ** (ล็อกใหม่ 21 ส.ค. 2026 · จะโผล่ซ้ำในเควสอิยามะ)

- `soapland` → **ร้านอาบอบนวด** (รูปที่ ship แล้ว K3/Gaiden · ไม่ใช่ "ซาวน่าหรู" ซึ่งคนละกิจการ)
- **เซยะ (ผู้จัดการโฮสต์คลับสตาร์ดัสต์)** → การ์ดใหม่ `friend_seiya` ใน `characters_side.json` · T2 (ฉัน/นาย) ไม่ใช้ ครับ

- `image club` (อิมเมจคุระบุ — บริการแต่งคอสเพลย์) → **อิมเมจคลับ** (ล็อกใหม่ 21 ส.ค. 2026)
- **ตัวละครที่ "สวมบท" คนอื่นชั่วคราว ใช้สรรพนามของบทที่สวมได้** แล้วสลับกลับตอนเฉลย —
  เคสจริง: "Older-looking Highschool Girl" ใช้ "หนู" ตอนแกล้งเป็นนักเรียน แล้วเปลี่ยนเป็น "ฉัน" ตรงจุดเฉลย
  (แนวเดียวกับข้อยกเว้น ข้า/เจ้า ของไดจิ ริวเซนจิ — ทะเบียนเป็นส่วนหนึ่งของมุก)

- **`Taka` (ฉายาที่ฮัตตันตั้งให้ยากามิ) → ทากะ** — คนละคำกับ **`Tak` ที่ไคโตะเรียก = ทาคุ** ·
  ยืนยันจากบทในเกม "Okay, then I'm gonna call you \"Taka\"!" · ship แล้ว 9 จุด ห้ามกวาดรวมกัน

### ชื่อไพ่มาจองล้อเลียนของยูริกะ ทาชิบานะ (ล็อก 21 ส.ค. 2026)

ยูริกะเรียกยากุผิดเป็นมุกประจำตัว — ต้องเป็นคำไทยที่ "ล้อเสียงยากุที่ ship แล้ว" ไม่ใช่คงอังกฤษ
(ผู้เล่นไทยอ่านอักษรละตินกลางบทจะไม่รู้ว่าเป็นมุก)

| EN (มุก) | ยากุจริง | คำล็อกไทย |
|---|---|---|
| `Toy Toy` | toitoi / โทอิโทอิ | **ต้อยต้อย** |
| `Honey Sue` | honitsu / ฮงอิตสึ | **หงส์อิ๊ด** |
| `Churning Potato` | chuuren poutou / ชูเร็นโปโต | **ชูรินโปเตโต้** |
| `Slew Uncle` | suu ankou / ซูอังโค | **ซูลุงโค** |
| `Pin Who` | pinfu (คำล็อก = มือไร้แต้ม) | **พินอู๊ย** — ยากามิสวนว่า "ผมว่ามันน่าจะ \"อู๊ย\" มากกว่านะ" (รับมุก painful ของ EN) |

- `Rinko` → **รินโกะ** (ไม่ใช่ "ริงโกะ" ซึ่งอ่านเป็น ringo = แอปเปิล) · `Akko` → **อักโกะ** (ก ไม่ใช่ ค)
- ⚠ **มี "Yosuke" สองคนในไฟล์เกม** — `friend_yosuke` = โยสึเกะ ซาโอโตเมะ (T1 ผม/ครับ) กับ NPC สูบบุหรี่
  `speaker_id 735` (`judge_陽介` · เพศ unknown ในไฟล์เกม) ที่บทเรียกว่า "Yosuke-kun" เฉย ๆ
  → ทับศัพท์เหมือนกันแต่ **ห้ามยกทะเบียนของคนแรกมาใช้กับคนหลัง** · NPC ตัวหลังยังต้องเลี่ยงคำลงท้ายบอกเพศ

- `barker` (คนเรียกแขกหน้าร้าน) → **คนเรียกแขก** ทุกบริบท (เลิกสลับกับ "พนักงานเรียกแขก")
- `North Pink Street` → **ถนนพิงก์สตรีทฝั่งเหนือ** · `Little America` → **ลิตเติลอเมริกา**
  · `Drone Gorilla` → **กอริลลาโดรน** · `coin locker` → **ตู้ล็อกเกอร์หยอดเหรียญ**
- `Rinko` → **รินโกะ** · `Akko` → **อักโกะ** · `Chiaki` → **ชิอากิ** · `Yu-kun` → **ยูคุง**
- **โฮมเลส "ยามานามิ" แทนตัวเองว่า "ลุง"** (ship แล้ว 32 บรรทัด) ห้ามเปลี่ยนเป็น "ฉัน"
- การ์ด `smoking_area_regulars` แก้เป็น **ชาย confidence สูง** แล้ว (หลักฐาน EN ในบท: "I was a working man,
  just like you") — เดิมขึ้น low ทำให้ผู้ตรวจเกือบแก้บทที่ถูกอยู่แล้วให้กลายเป็นกลาง

- `Kon-chan` (ชื่อเล่นของคนโดะ) → **คงจัง** ตามคำตัดสินเดิมที่บันทึกไว้แล้วด้านบน (เหตุผล: "คนจัง" อ่านพ้องกับคำว่า "คน")
  ⚠ บันทึกไว้กันพลาดซ้ำ: รอบ 21 ส.ค. 2026 lead เคยกลับด้านคำตัดสินนี้เพราะนับความถี่ในไฟล์อย่างเดียวโดยไม่ค้น glossary ก่อน
  — **นับความถี่ไม่ใช่หลักฐาน ถ้ามีคำตัดสินพร้อมเหตุผลอยู่แล้ว** · `Kondo` เองสะกด **คนโดะ** (ship 14 จุด ไม่ใช่ "คนโด")
- `bombing` (ศัพท์วงการโฮสต์ = แย่งลูกค้าโฮสต์คนอื่น) → **ทิ้งบอมบ์** · `White Tiger` (โฮสต์คลับคู่แข่ง) → **ไวท์ไทเกอร์**
- `Kento Amahara` → **เคนโตะ อามาฮาระ**

- `Esmeralda Special` → **เอสเมอรัลดา สเปเชียล** · `Geisha 1500` → **เกอิชา 1500**
  (ตามแนวกาแฟที่ ship แล้ว: บลูเมาน์เทน · โกปี ลูวัก · กาแฟเกอิชา — ไม่เข้าข่ายกฎคงเครื่องหมายการค้า)
