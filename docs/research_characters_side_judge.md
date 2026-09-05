# รายงาน — ตัวละครสมทบ/NPC เกม Judgment (characters_side.json)

สถานะ: จัดกลุ่มครบ 473/473 ชื่อจาก `extracted/facts/speakers.json` แล้ว (14 ส.ค. 2026 batch)
ผลลัพธ์: `translations/characters_side.part1.json` + `.part2.json` + `.part3.json` (แตกไฟล์เพราะรวมกัน ~87KB เกิน ~40KB/ไฟล์ — แต่ละ part `json.load` ผ่านเดี่ยว ๆ ได้จริง, merge ด้วย `dict.update()` ตามลำดับ part1→part2→part3 เพื่อรวมกลับเป็นออบเจกต์เดียว)

## 1. ตัวเลขสรุป

- **473** ชื่อทั้งหมดใน `speakers.json`
- **8** ชื่อตรงกับตัวละครหลัก 27 ตัว (พบเป็น `talk_talker` ในไฟล์จริง — อีก 19 ตัวไม่มี entry พูดในไฟล์นี้เลย ไม่ต้องข้ามเพราะไม่ปรากฏ):
  `八神`→Yagami · `judge_星野`→Hoshino · `judge_さおり`→Saori · `judge_源田`→Genda ·
  `judge_海藤`→Kaito · `judge_真冬`→Mafuyu · `judge_ツクモ`→Tsukumo · `judge_新谷`→Shintani
- **465** ชื่อที่เหลือ = ตัวละครสมทบ/NPC ที่จัดกลุ่มในงานนี้ทั้งหมด
- **68 กลุ่ม** ทั้งหมด แบ่งเป็น:
  - **52 กลุ่มเพื่อน (friend_*)** — แยกรายคน 1 คน/กลุ่ม ตามระบบ Friend ของเกม (54 คนในเกม ลบ Tsukumo ที่เป็นตัวหลักไปแล้ว ลบ "Yoshida" ผู้จัดการสนามตีลูกที่ไม่มี `talk_talker` เป็นของตัวเองในไฟล์ 473 ชื่อ)
  - **16 กลุ่มตามหมวดหมู่/บทบาท** ครอบคลุมชื่อที่เหลือ 411 ชื่อ

## 2. การพิสูจน์ความครบถ้วน

รันสคริปต์ Python เทียบ `talk_talker` ทุกแถวใน `speakers.json` (473 แถว) กับ:
1. เซตชื่อตัวละครหลัก 27 ตัว (คัดลอกจาก `translations/characters_main.json` ที่ทีมหลักส่งมาแล้ว — ตรวจแล้วว่าตรงกับ 27 ชื่อในบรีฟเป๊ะ)
2. เซต `members` รวมของทั้ง 68 กลุ่มใน 3 part files

ผลลัพธ์:
```
speakers total: 473
excluded (main-27): 8
covered (อยู่ในกลุ่มใดกลุ่มหนึ่ง): 465
missing: 0
8 + 465 = 473  ✅ ครบ
```
`json.load()` ผ่านทั้ง 3 part files แยกกัน — ตรวจแล้ว

## 3. ระเบียบวิธี

1. โหลด `speakers.json` (473 แถว) → แยกแถวที่ `talk_talker` ตรงกับนามสกุล/ชื่อเต็มของ 27 ตัวหลัก
2. จับคู่ 465 ชื่อที่เหลือกับ `friends.json` (54 คน) ผ่าน `talk_talker` (ตรงกับชื่อเต็ม/ชื่อ/นามสกุลใน friends.json) — ได้ 52 คน (อัตโนมัติ 50 + เติมมือ 2 คนที่ระบบจับไม่เจอเพราะรูปแบบชื่อต่างกัน: `Tashiro`→"Tashiro-kun", `President of Ikinari Steak`→"Kunio Ichinose")
3. ชื่อที่เหลือ 411 ชื่อ จัดกลุ่มด้วย regex ตาม keyword ทั้งฝั่งคันจิ/ฮิรางานะใน `id` และฝั่งอังกฤษใน `talk_talker` (ตำรวจ/ยากูซ่า/พนักงานร้าน/คนไร้บ้าน/นักเรียน/ฝูงชนทั่วไป ฯลฯ) แล้วตรวจด้วยตาทีละกลุ่มเพื่อแก้ false positive (เช่น ชื่อฮิรางานะล้วนที่จริงเป็นชื่อคน ไม่ใช่คำคุณศัพท์บรรยาย — ย้ายจาก flavor_npc ไป named_individual_npc)
4. เขียนสคริปต์ตรวจสอบครบ 1 รอบสุดท้ายก่อนส่งงาน (ผลอยู่ข้อ 2)

## 4. รายชื่อ 68 กลุ่ม

### กลุ่มเพื่อน (friend_*) — 52 กลุ่ม
แต่ละคนมี `description` แปลจากคำบรรยายจริงใน `friends.json`, เพศเดาจากคำสรรพนาม/ชื่อในคำบรรยาย EN (มี ⏳ กำกับให้ยืนยันซ้ำตอนแปลบทแรกของตัวละครนั้น), `pronoun_to_others` ใส่ "คุณยากามิ/ยากามิซัง ⏳" ไว้ก่อนเพราะยังไม่ได้อ่านบท dialogue จริงว่าเพื่อนแต่ละคนเรียกยากามิว่าอะไร

รายชื่อ: onodera, inose, hatano, ryan_acosta, mari, kyushu_no1_star_owner, tomioka, furuya, sagara, amamiya, bantam_owner, matsuzaki, ryo_suzaki, kim, tashiro_kun, nekomiya, katagiri, hutton, xiu, voluptuous_woman, uozumi, mami, nasugawa, tanago, ida, alice, sota, kiyoshiro, dwayne, hiranuma, tateyama, kaede, terahara, moroboshi, takemitsu_owner, fujimori, norimoto, miharu, isaka, fukutsu, koizuka, iyama, yosuke, madoka, kamaguchi, deguchi, ichinose_kunio, tachibana, sana, tsukino, amane, nanami

⏳ เพศไม่ชัวร์ (ไม่มีคำสรรพนามระบุตรง ๆ ใน bio EN): **Xiu (20), Takemitsu Owner (36), Fukutsu (41), Amane (52)**, และอีกหลายคนที่เดาจากชื่อ/บทบาทเท่านั้น (ทำเครื่องหมาย ⏳ ไว้ในฟิลด์ `notes` ของทุกกลุ่มเพื่อนแล้ว)

### กลุ่มตามหมวดหมู่ — 16 กลุ่ม
| กลุ่ม | จำนวนสมาชิก (talk_talker unique) | หมายเหตุ |
|---|---|---|
| meta_system | รวม Everyone/All/Fans | Test/Player/???/Everyone/All/Fans |
| police | 4 | น้อยกว่า K3 มาก เพราะยากามิไม่ใช่ยากูซ่า |
| yakuza_thug_generic | 35 | รวมสมาชิก Keihin Gang (京浜同盟) |
| shop_restaurant_staff | 71 | กลุ่มใหญ่ที่สุด — มีร้านเชนจริงมีลิขสิทธิ์เพียบ |
| homeless | 10 | 5 คนมีชื่อ (Kondo/Hamanaka/Murao/Teraoka/Fukuhara) |
| children_students | 15 | |
| generic_crowd_passerby | 19 | รวมผู้สูงอายุทั่วไปเข้าด้วย |
| mystery_placeholder | 11 | ⚠ สปอยล์ — ตัวตนจริงเฉลยทีหลัง |
| tanaka_imposter_case | 4 | ปมทานากะปลอม/จริง |
| animal_mascot | 3 | แมว, Koro-nyan, มาสคอตทั่วไป |
| media_press | 2 | |
| foreign_gang | 3 | Wang, Zhuang Shi, G.I. |
| smoking_area_regulars | 10 | คาสต์ตายตัวมุมสูบบุหรี่ (id ขึ้นต้น 喫煙_) |
| masked_heist_team | 4 | Crow/Fox/Mascara/Man in Noh Mask — ⏳ บทบาทไม่ยืนยัน |
| flavor_npc_with_trait | 101 | บรรยายด้วยคำคุณศัพท์ ไม่มีชื่อจริง |
| named_individual_npc | 114 | catch-all ชื่อเฉพาะที่ข้อมูลไม่พอจัดเป็นตัวหลัก |

## 5. จุดที่ยังไม่ชัวร์ ⏳ (ให้ lead/นักแปลตรวจก่อนใช้)

1. **masked_heist_team** (Crow/Fox/Mascara/Man in Noh Mask) — จัดกลุ่มจาก idx เรียงติดกันในไฟล์ดิบเท่านั้น ยังไม่ได้อ่านบทพูดจริงว่าเป็นทีมเดียวกันจริงหรือปรากฏคนละบริบท
2. **mystery_placeholder** ทั้ง 11 รายการ — ต้องเทียบสรรพนามกับตัวตนจริงหลังเกมเฉลย ห้ามใช้โทนกลางทั้งบท (ใส่ ⚠ ไว้ในไฟล์แล้ว)
3. **smoking_area_regulars** — สันนิษฐานว่าเป็นเควสเสริม "มุมสูบบุหรี่" (แอบฟังบทสนทนา) จาก pattern id เท่านั้น ยังไม่ได้ยืนยันจาก talk.bin จริง
4. เพศของเพื่อน 4 คน (Xiu, Takemitsu Owner, Fukutsu, Amane) ไม่มีหลักฐาน EN ชัดเจน — ⏳ ทั้งหมด

## 6. ชื่อที่สงสัยว่าอาจสำคัญกว่าที่คิด (ไม่อยู่ใน 27 ตัวหลัก)

- **Hayama (葉山, idx624)** และ **Shijima (志島, idx625)** — ปรากฏใน `speakers.json` อยู่ติดกับกลุ่มตัวละครหลัก (Mass Media, Fan, Hoshino, Saori, Genda ตามลำดับถัดมา idx626-630) ทำให้น่าสงสัยว่าอาจมีบทบาทมากกว่า NPC ทั่วไป — **ตรวจแล้ว**: ไม่พบชื่อทั้งสองใน `extracted/facts/evidence.json` (แฟ้มประวัติ/หลักฐาน 103 รายการ) เลย ซึ่งเป็นสัญญาณว่าน่าจะเป็น NPC รองจริง ๆ ไม่ใช่ตัวละครหลักที่ตกหล่น — แต่ยังไม่ได้เช็ค `talk.bin.json` เต็ม (ไฟล์ใหญ่มาก) จึงจัดไว้ใน `named_individual_npc` เป็นการชั่วคราว พร้อมข้อสังเกตนี้ให้ lead ตัดสินอีกที
- ไม่พบชื่ออื่นที่ overlap กับ 27 ตัวหลักนอกเหนือจากนี้

## 7. คำล็อกจากภาคอื่นที่เกี่ยวข้อง (ส่งต่อให้ทีม glossary)

- **Ono Michio** (小野ミチオ, idx823, ร้านราเมงล้อเลียนเชนดัง) — มีคำล็อกแล้วจาก `yakuza-kiwami-3/translations/glossary.md`: **"โอโนะ มิชิโอะ / มิชิโกะ"** (new_names wave 5) — ใช้คำเดิม ไม่ตั้งใหม่
- **Ass Catchem** (本山, idx795) — ตัวละครโรคจิตลวนลามที่ปรากฏซ้ำข้ามหลายภาคของซีรีส์ Yakuza — ยังไม่พบคำแปลไทยล็อกตรง ๆ ในโปรเจกต์พี่น้อง (เจอแค่ชื่ออังกฤษในรายชื่อ NPC ของ K3) ให้ทีม glossary ตรวจอีกทีก่อนตั้งชื่อใหม่
- ⚠ **กับดักชื่อพ้องนามสกุล**: มีเพื่อน **"Kunio Ichinose"** (friend idx48, ประธานร้าน Ikinari Steak) ซึ่งคนละคนกับตัวละครหลัก **"Kaoru Ichinose"** (นามสกุลเดียวกัน แต่คนละคนคนละบทบาท) — โชคดีที่ `speakers.json` ไม่มี `talk_talker` ตรง "Ichinose" เฉย ๆ (ใช้ "President of Ikinari Steak" แทน) จึงไม่ชนกันในไฟล์นี้ แต่ทีมแปล/glossary ควรรู้ไว้ว่านามสกุลนี้มี 2 คนไม่เกี่ยวข้องกัน

## 8. กับดักอื่นที่พบระหว่างจัดกลุ่ม (บันทึกไว้ใน `notes` ของแต่ละกลุ่มในไฟล์ JSON แล้ว)

- **Norika (ノリカ, มีพ่อ/แม่)** ≠ **Noriko Taguchi (田口紀子, มีสามี)** — ชื่อพ้องเสียงคล้ายกันมาก แต่คนละครอบครัว คนละ JA id
- **Kondo/Hamanaka** (named_individual_npc) ≠ **Homeless Kondo/Homeless Hamanaka** (กลุ่ม homeless) — JA id ต่างกัน (近藤/浜中 ธรรมดา vs ホームレス近藤/ホームレス浜中) คนละตัวละคร
- **judge_むろた** (id ภาษาญี่ปุ่นอ่านว่า "Murota") แต่ `talk_talker` ที่โชว์จริงคือ **"Azuma"** — id ภายในกับชื่อที่แสดงจริงไม่ตรงกัน (น่าจะเป็นชื่อ codename ตอนพัฒนา) ให้ยึด `talk_talker`/EN เป็นหลักเสมอเวลาแปล ไม่ใช่ความหมายตรงตัวของ JA id
- ชื่อแก๊ง **"Keihin Gang"** สะกดใน JA id ไม่ตรงกัน 2 แบบ (京浜同盟 ปกติ vs 京浜同名 ในบางแถว) — น่าจะเป็นพิมพ์ผิดของทีมพัฒนาเกมเอง ให้ยึด "Keihin Gang" (EN) เป็นชื่อทางการเดียว
- **Voice of Tsukino / Takeda's Voice** — เสียงนอกจอ/โทรศัพท์ของ Tsukino Saotome (เพื่อน) และ Takeda (named_individual_npc) ตามลำดับ ให้ใช้โทนเดียวกับตัวจริงของแต่ละคน

## 9. การแก้ไขตามคำตัดสิน lead (ระหว่างทำงาน)

ได้รับข้อความจาก lead กลางงานให้แก้สะกด — ตรวจสอบและแก้ในไฟล์ที่เขียนแล้วครบถ้วน:
- **Yagami**: แก้ "ยากามิ" → **"ยากามิ"** ทุกจุด (60+56 ครั้งใน part1/part2 เดิม ก่อนแตกเป็น 3 parts)
- **Matsugane Family**: แก้ "ตระกูลมัตสึกาเนะ" → **"ตระกูลมัตสึกาเนะ"** (จุดเดียวที่พบ — ในคำบรรยาย friend_tashiro_kun)
- Kyorei Clan / Mafuyu / Kuroiwa / Genda-sensei / "the Mole" — ตรวจแล้วไม่พบการใช้คำเหล่านี้ในไฟล์ที่เขียน (ไม่เกี่ยวข้องกับตัวละครสมทบในงานนี้โดยตรง)
- ยืนยัน `characters_main.json` (27 ตัว จากทีมหลัก) ตรงกับรายชื่อ 27 ที่ใช้ข้ามในงานนี้ทุกตัว — ไม่มีชื่อซ้ำ/ตกหล่น

## 10. สิ่งที่ค้าง (⏳ งานถัดไปสำหรับทีมอื่น/นักแปล)

- ยืนยันเพศ 4 เพื่อนที่ยัง ⏳ (Xiu, Takemitsu Owner, Fukutsu, Amane)
- ยืนยันบทบาทจริงของ masked_heist_team และ smoking_area_regulars จากบท dialogue จริงใน `talk.bin.json` (ไฟล์ใหญ่ ต้อง Grep เฉพาะจุด)
- ยืนยันว่า Hayama/Shijima (idx624-625) เป็น NPC รองจริงหรือมีบทบาทมากกว่าที่ประเมิน
- ยืนยันคำเรียกยากามิของเพื่อนแต่ละคน (ตอนนี้ใส่ "คุณยากามิ/ยากามิซัง ⏳" เป็นค่าเริ่มต้นทุกคน — ยังไม่ได้เทียบ EN จริงทีละคน)
- ทีม glossary ตัดสินคำทับศัพท์ไทยของชื่อเฉพาะใน `named_individual_npc`/`flavor_npc_with_trait` เป็นรายเควสตอนแปลจริง (งานนี้กำหนดแค่โทน/สรรพนาม ไม่ได้ทับศัพท์ชื่อ)
