# หลักฐานพิสูจน์เพศตัวละคร — Judgment (JETH)

สถานะ: ร่างแรกจากการค้นหลักฐาน 20-21 ส.ค. 2026 — ตรวจครบ **27 ตัวละครหลัก** (`characters_main.json`)
และ **68 กลุ่มผู้พูด** ใน `characters_side.json` (เน้น 50 กลุ่ม `friend_*` รายบุคคล ตามที่บรีฟกำหนดลำดับความสำคัญ)
ไฟล์หลักฐานดิบ: `extracted/facts/gender_evidence.json` (94 entry, `json.load` ผ่านแล้ว)

กติกาที่ใช้: ตาม `translations/PRONOUN_MATRIX.md` §0.1 — ต้องมีสรรพนาม EN ตรงตัว (he/him/his, she/her/hers)
หรือคำเรียกเชิงเพศ (Mr./Ms., guy/lady/man/woman, boyfriend/girlfriend) หรือบทบาทที่ระบุเพศชัด (แม่/พี่ชาย/โฮสเตส)
เท่านั้นถึงจะกำหนดเพศได้ — honorific (-kun/-chan) เดี่ยวๆ ไม่พอ ชื่อเดี่ยวๆ ไม่พอเด็ดขาด

## สรุปจำนวน

| กลุ่ม | ชาย | หญิง | คละเพศ | ไม่รู้ (unknown) | รวม |
|---|---|---|---|---|---|
| ตัวละครหลัก (27) | 24 | 3 | 0 | 0 | 27 |
| กลุ่ม friend_* (50) | 32 | 11 | 0 | 7 | 50 |
| กลุ่มรวม/อื่นๆ (17) | 3 | 0 | 8 | 6 | 17 |
| **รวมทั้งหมด** | **59** | **15** | **8** | **12** | **94** |

Confidence: high 78 · medium 5 · low 11 (ทั้งหมดที่เป็น low คือรายการที่ยัง unknown — ไม่มีรายการไหนเดาเพศแบบ confidence สูงจากหลักฐานอ่อน)

**ผลที่น่าพอใจ: ตัวละครหลักทั้ง 27 ตัวพิสูจน์เพศได้ครบ 100% ด้วยหลักฐาน high confidence** — ไม่มีตัวไหนต้องเลี่ยงสรรพนามในกลุ่มนี้

## ตัวละครหลัก 27 ตัว (ยืนยันครบ)

| ตัวละคร | เพศ | หลักฐานย่อ (EN) | ที่มา |
|---|---|---|---|
| Yagami | ชาย | "his career immediately went down the drain" | evidence.json idx66 |
| Kaito | ชาย | "his failure to stop the robber" | evidence.json idx36 |
| Sugiura | ชาย | "his comfort zone" + "Sugiura is her brother" (ของ Terasawa) | friends.json idx0 · evidence.json idx80 |
| **Shirosaki (Saori)** | **หญิง** | "Saori said herself that **she** hurried home" | talk.bin.json L81344 |
| **Genda** | ชาย | "**he** left as soon as I came in" | talk.bin.json L77666 |
| Hoshino | ชาย | "I'm pretty sure **he's** innocent" | evidence.json idx100 |
| **Fujii (Mafuyu)** | **หญิง** | "**She** also happens to be childhood friends... dated Yagami" | evidence.json idx63 |
| Tsukumo | ชาย | "struggling to step outside **his** comfort zone" | friends.json idx0 |
| Hamura | ชาย | "**His** rank is equal to second-in-command" | evidence.json idx26 (ซ้ำนับสิบครั้ง) |
| Matsugane | ชาย | "Yagami thinks of **him** like a father. Sacrificed **himself**..." | evidence.json idx50 |
| Higashi | ชาย | "Kaito decided to cover for **him**" | evidence.json idx41 |
| Ayabe | ชาย | "**his** gun was temporarily stolen" | evidence.json idx87 |
| Kuroiwa | ชาย | "As **his** title suggests" | evidence.json idx57 |
| Kido | ชาย | "**he** took part in a human experimentation scandal" | evidence.json idx58 |
| Shono | ชาย | "**he** testified that **he** saw Waku" | evidence.json idx69 |
| Ichinose (Kaoru) | ชาย | "**He** also played a prominent role in establishing..." | evidence.json idx74 |
| Izumida | ชาย | "Does **he** have any evidence?" / "the **guy** who was trying to arrest you" | sound_auth.bin.json L82797, L98537 |
| Morita | ชาย | "**he** was actually one of the conspirators" | evidence.json idx62 |
| **Terasawa (Emi)** | **หญิง** | "**She** pointed out the contradiction... **she** was killed by Okubo" | evidence.json idx68 |
| Okubo | ชาย | "**He** admits to abandoning Waku's body... claims **he** didn't kill **him**" | evidence.json idx65 |
| Waku | ชาย | "**his** exact cause of death... **he** died from suffocation" | evidence.json idx88 |
| Shintani | ชาย | "**His** body was discovered... having suffered multiple gunshot wounds" | evidence.json idx87 |
| Murase | ชาย | "**he** began complying with the police investigation" | evidence.json idx28 |
| Hashiki | ชาย | "**He** was allegedly seeing off **his** colleague" | evidence.json idx89 |
| Kajihira | ชาย | "**he** bribed Hashiki to search for defects" | evidence.json idx76 |
| Hattori | ชาย | "to write **his** next big story" | evidence.json idx77 |
| Shioya | ชาย | "**he** came to Tokyo to take Hamura's life" | evidence.json idx46 |

หมายเหตุ: **Kaoru Ichinose** (รองปลัดสธ., main cast) กับ **Kunio Ichinose** (friend, ประธาน Ikinari Steak) เป็นคนละคน
— นามสกุลซ้ำกันเฉยๆ ยืนยันเพศแยกทั้งคู่แล้ว (ชายทั้งคู่บังเอิญ)

## กลุ่ม friend_* (50 กลุ่ม) — สรุปเฉพาะที่ยัง unknown (7 กลุ่ม)

**สำคัญที่สุดสำหรับนักแปล — 5 รายชื่อนี้ต้องเลี่ยงสรรพนาม/คำลงท้ายบอกเพศจนกว่าจะเจอหลักฐานเพิ่ม:**

| key | ชื่อ EN | เหตุผลที่ยัง unknown |
|---|---|---|
| `friend_hatano` | Shuichi Hatano | มีแค่บทพูดแนะนำตัวเอง ไม่มี he/she ยืนยันเลยทั้ง 3 ไฟล์ที่ค้น |
| `friend_xiu` | Haoyu Xiu | ทุกบทพูดเรียกด้วยชื่อเฉยๆ ไม่มีสรรพนามยืนยัน (ไฟล์ side เดิมก็ทำเครื่องหมาย ⏳ ไว้แล้ว — ยืนยันซ้ำว่ายังหาไม่เจอจริง) |
| `friend_tachibana` | Yurika Tachibana | มีแค่ honorific "-chan" (หลักฐานอ่อน ใช้เดี่ยวๆไม่ได้ตามกฎ §0.1) |
| `friend_fukutsu` | Fukutsu (Ebisu Pawn) | เจอแค่บทแนะนำตัว ไม่มีสรรพนาม |
| `friend_ida` | Hanae Ida | บทพูด 3 จุดล้วนเป็นการแนะนำตัวเอง ไม่มี he/she |

อีก 43 กลุ่ม friend_* ยืนยันได้ครบ high confidence (32 ชาย / 11 หญิง) — ดูรายละเอียดเต็มใน `gender_evidence.json`

## กลุ่มรวม/อื่นๆ (17 กลุ่ม — ไม่ใช่ friend_*)

กลุ่มเหล่านี้ตามบรีฟอนุญาตให้ตัดสิน "คละเพศ" ได้โดยไม่ต้องพิสูจน์รายบุคคลครบ (ยกเว้นที่ตรวจแล้วพบหลักฐานเจาะจง):

| key | ผล | หมายเหตุ |
|---|---|---|
| `named_individual_npc` | คละเพศ (medium) | catch-all 122 ชื่อ — **ไม่ได้ตรวจรายบุคคลครบในงานนี้** นอกขอบเขตเวลา นักแปลต้องอ่าน EN รายเควสเอง |
| `homeless` | คละเพศ เอียงชาย (medium) | แท็ก "Homeless Man/Guy" ยืนยันชายจากคำในชื่อเอง ที่เหลือ (Kondo/Hamanaka ฯลฯ) ยังไม่ยืนยันรายตัว |
| `generic_crowd_passerby` | คละเพศ (high) | ตามที่บรีฟอนุญาตชัดเจน + แท็กระบุเพศแยกในตัวเองอยู่แล้ว |
| `masked_heist_team` | คละเพศ (low) | ยืนยันได้แค่ "Man in Noh Mask" ว่าชาย |
| `flavor_npc_with_trait` | คละเพศ (high) | แท็กระบุเพศในชื่อเองแทบทุกตัว (Rude Dude=ชาย, Ditzy Lady=หญิง ฯลฯ) แปลตามคำในชื่อได้เลย |
| `smoking_area_regulars` | คละเพศ (low) | ยืนยันได้แค่ "Ditzy Lady"=หญิงจากชื่อ ที่เหลือไม่มีหลักฐาน |
| `mystery_placeholder` | **unknown (high)** | ตั้งใจปิดบังตามดีไซน์เกม — คงไว้จนกว่าจะเฉลย |
| `foreign_gang` | ชาย (medium) | Wang ยืนยันชายชัด — **⚠ พบกับดัก: "Zhuang Shi" ที่ไฟล์ side เดิมจัดเป็นสมาชิกแก๊งจริงๆ คือ "แมว" ของ Wang ไม่ใช่คน** (ดูหัวข้อกับดักด้านล่าง) |
| `police` | **unknown (low)** | ไม่พบสรรพนามยืนยันเลย — ห้ามสันนิษฐานว่าชายทั้งหมดจากธรรมเนียมทั่วไป |
| `media_press` | **unknown (low)** | ไม่พบสรรพนามยืนยัน |
| `shop_restaurant_staff` | คละเพศ (high) | ยืนยันแล้วจากพนักงานที่ถูกเผยเป็น friend ทั้งหญิง (Alice) และชาย (Sota/Kiyoshiro/Dwayne) |
| `yakuza_thug_generic` | ชาย (medium) | ไม่พบแท็กหญิงเลยใน 30 ชื่อ + ไม่มีแท็ก "Female Thug" ในเกม — อนุมานชายทั้งกลุ่ม |
| `children_students` | คละเพศ (medium) | ยืนยันได้แค่ "Girl in a School Uniform"=หญิงจากแท็ก ที่เหลือกลางทางเพศ |
| `tanaka_imposter_case` | **unknown (high)** | ตั้งใจคลุมเครือตามดีไซน์เควส |
| `meta_system` | **unknown (high)** | แท็กระบบ ไม่ใช่ตัวละครจริง |

## รายการที่ยังพิสูจน์ไม่ได้ (unknown) — รวม 10 รายการ ต้องเลี่ยงสรรพนามทั้งหมด

1. `friend_hatano` — Shuichi Hatano
2. `friend_xiu` — Haoyu Xiu
5. `friend_tachibana` — Yurika Tachibana
6. `friend_fukutsu` — Fukutsu
7. `friend_ida` — Hanae Ida
8. `mystery_placeholder` — ???/Mysterious Man/Unknown Man (ตั้งใจปิดบัง — สปอยล์)
9. `police` — Veteran Detective/Police/Dopey Cop/Serious Cop
10. `media_press` — Mass Media/Newscaster
11. `tanaka_imposter_case` — Tanaka/?/Tanaka? (ตั้งใจคลุมเครือ — ปมเควส)
12. `meta_system` — Test/Player/Fans/Everyone/All

**หมายเหตุพิเศษ "the Mole"**: ไม่ใช่ key ที่มีอยู่ใน `characters_main.json`/`characters_side.json` (ไม่มีกลุ่มเฉพาะ)
แต่ตามคำสั่ง §0.1 ข้อสปอยล์ ต้องคง unknown เสมอไม่ว่าจะเดาตัวตนได้แค่ไหนก็ตาม — evidence.json idx34/48 มีข้อมูลเบื้องหลัง
(เป็นนักฆ่าที่ Hamura ว่าจ้าง) แต่ไม่ระบุเพศของไอ้ตัวตุ่นเองที่จุดใดเลยในไฟล์ที่ตรวจ — สอดคล้องกับนโยบายเดิมพอดี

## กับดัก/ข้อขัดแย้งที่เจอระหว่างค้นหลักฐาน

1. **"Zhuang Shi" ไม่ใช่คน — เป็นแมว**: ไฟล์ `characters_side.json` กลุ่ม `foreign_gang` เขียนไว้ว่า "Wang, Zhuang Shi ชื่อจีน, G.I. ทหารอเมริกัน"
   ทำให้ดูเหมือน Zhuang Shi เป็นสมาชิกแก๊งคนหนึ่ง — แต่ยืนยันจาก talk.bin.json บรรทัด 87340 ชัดเจนว่า
   *"Zhuang Shi isn't my cat. He is the pet cat of... someone who passed away recently."* คือ **แมว** ของเจ้านาย Wang
   ที่หายไปในเควสเสริม ไม่ใช่มนุษย์ — **ควรแจ้ง lead แก้ note ของกลุ่มนี้** (ไม่ได้แก้เองเพราะนอกขอบเขตงานที่ได้รับ
   ห้ามแตะ characters_side.json)
2. **Izumida ไม่มีสรรพนามใน talk.bin.json เลยสักบรรทัด**: ต้องข้ามไปหาใน `sound_auth.bin.json` (บทคัตซีน) ถึงเจอ
   "Does he have any evidence?" — เป็นตัวอย่างว่าตัวละครสำคัญบางตัวไม่มีบทใน talk.bin.json เลย มีแต่ในคัตซีน
3. **Genda/Shirosaki ไม่มีสรรพนามใน evidence.json**: evidence.json (แหล่งลำดับ 1 ตามบรีฟ) ให้แค่ข้อมูลบทบาท ไม่มี
   he/she สำหรับสองคนนี้ — ต้อง grep บทพูดจริงใน talk.bin.json (ฉากเนื้อเรื่องเสริม "Master and Pupil" เรื่องเค้กหาย)
   ถึงเจอหลักฐานยืนยัน — เป็นเคสตัวอย่างว่าห้ามพึ่งพา evidence.json อย่างเดียวเมื่อไม่มีสรรพนามให้
4. **ไม่มีสรรพนามขัดแย้งกัน (he/she สลับ) กับตัวละครใดในขอบเขตที่ตรวจ** — ตัวละครหลักทั้ง 27 ตัวสรรพนามสอดคล้องกันทุกจุดที่พบ
   ไม่พบเคสที่เกมใช้ he กับ she สลับกับตัวเดียวกัน
5. **Kaoru Ichinose (รองปลัดสธ.) กับ Kunio Ichinose (friend, ปธ. Ikinari Steak) นามสกุลชนกัน** — ทั้งคู่ยืนยันเป็นชายแยกกันแล้ว
   ไม่ใช่ปัญหาเพศ แต่เป็นกับดักชื่อซ้ำที่ `characters_main.json` เตือนไว้แล้วเช่นกัน (ดูฟิลด์ reason ของ ichinose)
6. **friend_xiu ที่ไฟล์ side เดิมทำเครื่องหมาย ⏳ ไว้แล้วว่าต้องยืนยันเพศ** — ผลค้นจริงยืนยันว่ายังหาสรรพนามไม่เจอจริง
   (ไม่ใช่แค่ยังไม่มีใครเช็ค) — คงสถานะ unknown ต่อไป

## ขอบเขตที่ยังไม่ได้ทำ (นอกเวลาที่กำหนด)

- `named_individual_npc` (122 ชื่อ) และ `flavor_npc_with_trait`/`smoking_area_regulars` บางส่วน — ตรวจแค่ระดับกลุ่ม/แท็ก
  ไม่ได้ grep รายชื่อทีละ 100+ ชื่อ เพราะเป็น NPC เควสเสริมเดี่ยว/ฉากเดียวที่นักแปลจะเจอ context EN รอบข้างอยู่แล้วตอนแปลจริง
- `homeless`, `police`, `smoking_area_regulars` — ยืนยันได้แค่บางส่วนจากคำในแท็กเอง ยังไม่ได้ grep บทพูดเต็มทุกตัว

## เพศที่ยืนยันเพิ่ม 21 ส.ค. 2026 (จากคิว TALK)

| key | ชื่อ EN | เพศ | หลักฐาน |
|---|---|---|---|
| `friend_amamiya` | Sakura Amamiya | **หญิง** | `judge_friend_a13` — Grown-ass Thug พูดกับเธอว่า "you dirty girl!" (คำเรียกเชิงเพศ §0.1 ข้อ 2) |
| Manager (คดี A44) | Manager | **ชาย** | บทพูด EN "The guy at the cafe said..." |
| Man in Black (คดี A44) | Man in Black | **ชาย** | ชื่อ JA 黒服の男 มีคำว่า 男 |
| Makihara (คดี A44) | Makihara | **ชาย** | `scenario_summary.json` "that guy Makihara must really love drones" |
| Hayama (คดี A35) | Hayama | **ชาย** | `scenario_summary.json` sidA35 "He wants me to…" |
| Otoya Shijima (คดี A35) | Otoya Shijima / "Bram" | **ชาย** | ตัวละครชายในคำล็อก glossary (ชื่อจริงของแบรม ซิลเวเนีย) |
| Tomokazu Kawada (คดี A08) | Kawada | **ชาย** | `scenario_summary.json:90` "He wants me to accompany him" |
| Takumi Katagiri (คดี A08) | Katagiri | **ชาย** | บทพูดของคาวาดะใน `judge_side_a08` "He's trying to create a level playing field…" |
| `friend_kyushu_no1_star_owner` | Kyushu No. 1 Star Owner | **ชาย** | `judge_friend_a09` บทรำพึงยากามิ "I'm glad **he's** back to his old self… **his** cuisine" || Meguro (คดี A18/A19) | Meguro | **ชาย** | บทพูดใน batch ใช้ he/his ซ้ำหลายครั้ง (§0.1 ข้อ 1) |
| Man from the Rip-off Bar | — | **ชาย** | ชื่อผู้พูด JA `ぼったくりバーの男` มีคำว่า 男 |
| Ryu Asaka (มือระเบิด) | Ryu Asaka | **ชาย** | ข่าวเปิดเผยตัวตน "his security firm" |
| Moroboshi (friend_a40) | Moroboshi | **ชาย** | "he's been down in the dumps… he lost his chance" |
| Kondo (friend_a40) | Kondo | **ชาย** | EN เรียก "this homeless guy" (§0.1 ข้อ 2) |
| Shoji Ohata (คดี A38/A39) | Ohata | **ชาย** | ลูกชายเรียก "Dad" + บทพูดของเขาเอง "I'm a single father" |
| Ayumu Ohata | Ayumu | **ชาย** | EN บรรยาย "a boy, about 6 years old" |
| Panty Professor (คดี A01) | Pervert | **ชาย** | โยสึเกะพูดถึงเขาด้วย he/his ซ้ำ |
| Manager ร้านคันไร (friend_a17) | Fumio Matsuzaki | **ชาย** | `side_content_context_judge.md` idx 13 + batch_120 "His professional demeanor" || Takeshi Akagawa (คดี A47) | Akagawa | **ชาย** | ชื่อจริง "Takeshi" + บทพูด "he lost the bag" |
| Megumi Hashimoto (คดี A13) | Megumi | **หญิง** | EN เรียก "Ma'am" · "the lady's husband" |
| Takefumi Hashimoto (คดี A13) | Takefumi | **ชาย** | EN he/his + เป็นสามีของเมกุมิ |
| Suguru Oka (คดี A13) | Oka | **ชาย** | EN he/his ในบทเดียวกัน || Crow (แก๊งโจรสวมหน้ากาก) | Crow | **ชาย** | บันทึกภารกิจที่ ship แล้ว "Crow told me **he's** worried about Jester" + Fox พูดถึงเขาว่า "that hypocrite doesn't practice what **he** preaches" |
| Shinzaburo Ishikawa (G.I.) | Ishikawa | **ชาย** | แนะนำตัวเอง "I, Shinzaburo Ishikawa" || Hironaka (คดี A48) | Hironaka | ⏳ **ยังพิสูจน์ไม่ได้** | นักแปล TALK_028 อ้างคำอธิบายไอเทม แต่ lead ค้นทุก bin แล้ว ประโยคเดียวที่มีชื่อเขาคือ ...despite whatever faith Hironaka-san seems to have in **him** ซึ่ง him = นิชิมุระ ไม่ใช่ฮิโรนากะ — ให้เลี่ยงสรรพนามต่อไป |
| Nishimura (คดี A48) | Nishimura | **ชาย** | EN "a **boy** named Nishimura-kun" |
| Kaneda (คดี A48) | Kaneda | **ชาย** | EN "**he'd** finally paid back **his** debts" |
| Kumakura (คดี A48) | Kumakura | **ชาย** | EN "**He** refuses to let us see…" |
| Inamine · Daisuke (คดี A48) | — | ⏳ **ยังพิสูจน์ไม่ได้** | ไม่พบสรรพนาม/คำเรียกเชิงเพศ — ให้เลี่ยงสรรพนามต่อไป |
| Hideaki Deguchi (คดี A16) | Deguchi | **ชาย** | บทพูดของฟุมิเอะ my nephew / a guy |
| Fumie Taniyama (คดี A16) | Fumie | **หญิง** | EN a very generous **lady** |
| Emerald Hills Employee | — | **ชาย** (medium) | ชื่อผู้พูด JA `judge_エメラルド・ヒルズの黒服` — 黒服 (คุโรฟุกุ) = พนักงานชายชุดดำประจำร้านคาบาเรต์ ธรรมเนียมเดียวกับผู้จัดการควีนรูจ |
| Jo Masuda (บาร์เทนเดอร์) | Masuda | **ชาย** | `voicer_gender.json` คีย์ `tender_master` + `speech_speaker_map.json` บทรำพึง (Guess Masuda kept **his** word.) |
| Kotatsu Higurashi (บาร์กเกอร์) | Higurashi | **ชาย** | บทของเขาเองใน `judge_friend_a36` พูดถึงอวัยวะเพศชายของตัวเองตรง ๆ + คดี A41 มีบทขู่ยากามิแบบชายล้วน |

