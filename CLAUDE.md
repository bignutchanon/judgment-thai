# JETH — Judgment ม็อดแปลไทย

Dragon Engine (PC port 2022) · codename ภายใน **`judge`** (✅ ยืนยันจากไฟล์จริง 14 ส.ค. 2026) · โปรเจกต์ที่ `D:\Projects\judgment-thai`

ลูกผสมสองยุค (verify แล้วกับไฟล์จริง):
- **ข้อความ**: ARMP v2 + `db.judge.en.par` (carrier=EN, par เดียว ไม่มี ja) → ใช้ reARMP/สาย K3 ได้
- **ฟอนต์ (แก้ครั้งใหญ่ 22 ส.ค. 2026 รอบ 16 — ล้มข้อสรุปรอบ 3-15 ทั้งชุด)**: **ตาราง advance ไม่ได้อยู่ใน exe** แต่อยู่ใน `db.judge.en.par → en/font.bin → แถว meta_ot_cond_book → คอลัมน์ kerning_table` (ARMP ซ้อน 332 แถว x 6 คอลัมน์ float = 3 คู่ (L,R)) → **เราตั้ง advance เองได้ทุกเซลล์** สูตร `advance = 36 - 18.0 x (L+R)` และ `x_offset = -18.0 x L` (ยืนยัน 2 ทาง: fit กับ probe ของเราเอง 171 จุด คลาดเคลื่อนเฉลี่ย 0.27 px และ fit กับภาพในเกมของม็อด MOD2SUB rms 0.23 px) · เขียนค่าเดียวกันลงทั้ง 3 คู่คอลัมน์เสมอ (เมนูใช้คู่ 5-6 · แถบภารกิจใช้คู่ 3-4) · รายละเอียดครบใน `scripts/font_metrics.py`
- **ฟอนต์ — ผลที่ตามมา**: มาร์ก (สระ/วรรณยุกต์) ตั้ง advance = 0 + เลื่อนซ้ายทับฐานได้ → **เลิก pre-compose ฐาน+มาร์ก หนึ่งตัวอักษรหนึ่งเซลล์** · ฐานตั้ง advance = ink + side bearing (ซ้าย 1 ขวา 3 px) → เพดาน 36 px หายไป · **Latin Ext-B tofu เพราะ kerning_table มีแค่ 332 แถว = ถึง U+016B** ไม่ใช่เพราะ atlas → donor pool ใช้ได้ถึง U+016B เท่านั้น (182 ช่องหลังหักที่ EN ใช้) · `translations/donor_widths.json` (advance เดิมของ donor) ไม่ได้ใช้จัดสรรอีกแล้ว เก็บไว้อ้างอิง/probe
- **ฟอนต์ — โครงไฟล์ (ยืนยันบนจอรอบ 12)**: โหมด EN วาดข้อความ **ทุกชั้น** (ไตเติล/จอโลโก้/UI/ซับบทสนทนา) ด้วย bitmap grid `data/font.judge/en/meta_ot_cond_book.dds` **ตัวเดียว** — ไม่ใช่ `FONT!` · 16 คอลัมน์ · cell 32x64 · **384 เซลล์ ขยายไม่ได้** · ต้อง drop-in `meta_ot_cond_book_italic.dds` ด้วย (ใช้ atlas เดียวกัน) และแก้แถว italic ใน font.bin ด้วย
- **ฟอนต์ — จอที่ไม่ได้ใช้ meta (แก้ 29 ส.ค. 2026 รอบ 17)**: UI บางจอ (หัวข้อเมนูโดรน · ป้ายท่า EX) ตั้งฟอนต์เป็น **`yakuza`** (`data/font.judge/en/yakuza.dds` 256x512 · cell 16x32 · 225 กลิฟ = cp U+0020-U+0100 · ไม่มี `kerning_table` = ตั้ง advance ไม่ได้) ซึ่งมี Latin-1 ครบ → donor U+00C0-U+00FF ของเราโผล่เป็น `À È Ú Á` · เอนจิ้น **สลับไปวาดด้วย `meta_ot_cond_book` ตั้งแต่ codepoint แรกที่ฟอนต์นั้นไม่มี แล้ววาดต่อจนจบสตริง** → แก้ด้วยเซลล์ "ตัวนำ" **U+0165** (กลิฟว่าง advance 0) ที่ `SlotMap.encode()` แทรกหน้าอักษรไทยทุกช่วง — ห้ามเอาออก และห้ามใส่หมึกในเซลล์นี้
- `tbgm_0p_ja` (`FONT!` ยุค Y6, 7,093 glyphs, slot ว่าง 2,157) **โหมด EN ไม่เรียกใช้เลย** — เก็บไว้เผื่อโหมด JA เท่านั้น (`y6_font_tool.py` ใช้กับไฟล์นี้ ห้ามใช้ font_tool ของ K2R)
- การจัดสรรเซลล์ให้ข้อความไทยทั้งเกม = `scripts/slot_alloc.py` → `translations/slotmap.json` (map เดียว ห้ามมีสำเนาที่สอง · แก้แล้วต้องรัน `scripts/test_slot_alloc.py` ให้ผ่าน 12/12) · **สระอำถูกแตกเป็น ํ + า เสมอ** ตอน encode (`decompose_am` — 5 ก.ย. 2026 แก้ "อ ำ" ห่าง) ห้ามจัดเซลล์ให้ ำ ตัวเดียวอีก
- **ฟอนต์สไปรต์ UI** (จอโดรน/คาสิโน เลือกฟอนต์เองจาก `ui.judge.en.par/en/font/*.bin` · 256 แถว = codepoint) มี donor ของเราอยู่ → ต้องล้างแถว donor ด้วย `scripts/strip_ui_sprite_slots.py --write` (วิธี LJ-015) แล้ว `deploy_spoil.py` ส่ง `mods/JudgmentThai/ui.judge.en` ให้ · แตก par ก่อนด้วย `tools/ParTool.exe extract … extracted/ui_en`

เนื้อเรื่อง: ทาคายูกิ ยากามิ ทนายผันตัวเป็นนักสืบ ไขคดีฆาตกรรมต่อเนื่องในคามุโรโจ (ปี 2018 — ก่อนตระกูลโทโจถูกยุบใน Y7 ปี 2019 จึงอยู่เส้นเวลาเดียวกับซีรีส์หลักได้)
คำล็อกที่ยืนยันแล้ว (20 ส.ค. 2026 — Judgment เคยรับเชิญใน Gaiden + Y7 จึงมีคำ ship จริงอยู่แล้ว): Yagami = **ยากามิ** · Yagami Detective Agency = สำนักงานนักสืบยากามิ · Masaharu Kaito = มาซาฮารุ ไคโตะ · Toru Higashi = โทรุ ฮิงาชิ · Matsugane (Family) = มัตสึกาเนะ / ตระกูลมัตสึกาเนะ · Kyorei Clan = ตระกูลเคียวเรอิ · Mafuyu = มาฟุยุ · Kuroiwa = คุโรอิวะ · Genda-sensei = **อาจารย์เก็นดะ** (เปลี่ยนจาก เก็นดะเซนเซ ตามคำสั่งเจ้าของ 5 ก.ย. 2026 — `-sensei` ทุกคน = อาจารย์+ชื่อ) · "the Mole" = ไส้ศึก
⚠ สะกดที่ **ผิด** และเคยหลุดในเอกสารรุ่นแรกของ repo นี้ (Yagami สะกดด้วย ง แทน ก · Matsugane สะกดด้วย ง แทน ก · Kyorei ลงท้าย ย์ แทน อิ) — กวาดทั้งโปรเจกต์ด้วย `python scripts/normalize_terms.py --write` (สคริปต์ข้าม CLAUDE.md/HANDOFF.md ไว้จงใจ เพราะสองไฟล์นี้ต้องเก็บตัวอย่างคำผิดไว้เตือน)

## สถานะยืนยันแล้ว (research เบื้องต้น 14 ส.ค. 2026 จากโปรเจกต์ K3)
- SRMM/RMM (Parless) **รองรับ Judgment อย่างเป็นทางการ** (Steam เท่านั้น) → loose file ผ่าน `mods/` ใช้ได้
- มีม็อดไทย Google MT อยู่แล้ว: MOD2SUB — https://www.nexusmods.com/judgment/mods/228 — ใช้เป็น proof-of-concept + แกะดูรายชื่อไฟล์ที่เขาแตะได้ **ห้ามใช้เป็น TM** (คุณภาพ MT)
- ✅ extract ครบแล้ว 20 ส.ค. 2026: `db.judge.en.par` → 1,358 bin (แปลง JSON ได้ 1,351) · unique string 53,591 · bin ที่มีข้อความ 213 — สรุปทั้งหมดใน `docs/research.md` + `docs/bin_index.md`

## อ่านก่อนทำงานทุก session
1. `HANDOFF.md` — สถานะล่าสุด + งานถัดไป
2. `docs/research.md` — ข้อเท็จจริงจากไฟล์เกมจริงทั้งหมด (โครงไฟล์ · ผล extract · สถาปัตยกรรมฟอนต์ · ระบบ slot allocator · ช่องว่างที่เหลือ) · คู่กับ `docs/bin_index.md` และ `docs/slot_alloc.md`
3. `docs/reference/FONT_PLAYBOOK.md` — อ่านก่อนแตะฟอนต์ทุกครั้ง

## ตาราง path
| ชื่อ | ที่อยู่ | กติกา |
|---|---|---|
| PROJECT | `D:\Projects\judgment-thai` | งานทั้งหมดเขียนที่นี่ |
| GAME | `E:\SteamLibrary\steamapps\common\Judgment` (override: env `JUDGE_GAME`) | ห้ามแก้/ลบ/ทับไฟล์ใน `runtime/media/data/` (ยกเว้นฟอนต์ drop-in + backup `.orig`) · ห้ามเปิดเกมเอง (ผู้ใช้ทดสอบ) · เพิ่มไฟล์ได้เฉพาะโฟลเดอร์ mods + ไฟล์ SRMM · SRMM ติดตั้งแล้ว 15 ส.ค. 2026 |
| Y6 | `D:\Projects\yakuza-6-thai` | อ่านอย่างเดียว (**ต้นแบบฟอนต์ FONT!** — y6_font_tool/bc4_codec/slotmap/inject ตัวจริง) |
| LJ (พี่น้อง) | `E:\SteamLibrary\steamapps\common\Lost Judgment` (ติดตั้งแล้ว) + `D:\Projects\lost-judgment-thai` | ทำหลัง Judgment จบ |
| K3 | `D:\Projects\yakuza-kiwami-3` | อ่านอย่างเดียว (สคริปต์ pipeline ชุดล่าสุด + thai_encode donor Cyrillic) |
| GAIDEN | `D:\Projects\yakuza-gaiden` | อ่านอย่างเดียว (TM + glossary ใหม่สุดที่ ship แล้ว) |
| K2R | `D:\Projects\yakuza-kiwami-2-mod` | อ่านอย่างเดียว (**ต้นแบบเอนจิ้นรุ่นเดียวกัน** — ฟอนต์/donor/โครง par) |
| Y7 / Y8 / PIRATE | ตาม path ใน CLAUDE.md ของ K3 | อ่านอย่างเดียว |

## ไฟล์เกมเป้าหมาย (✅ verify กับไฟล์จริงแล้ว 14-20 ส.ค. 2026)
- ข้อความ: `data/db.judge.en.par` (13.7 MB, carrier = EN) → ARMP v2 · 1,358 bin แบนใน `en/` · แก้ด้วย `tools/reARMP_fixed.py` · แตกใหม่ทั้งชุดด้วย `scripts/extract_all_en.py`
- ฟอนต์: **ไม่ใช่ par** — โฟลเดอร์ `data/font.judge/en/` · ตัวที่เกมใช้จริงคือ `meta_ot_cond_book.dds` (ดูหัวข้อบนสุด)
- ภาษาในเกม: EN/JA — db par มีตัวเดียวคือ `db.judge.en.par` (carrier = EN, ยืนยันแล้ว)
- ⚠ แก้ความเข้าใจผิด (research เว็บ 20 ส.ค. 2026): ม็อด **Retrial ไม่ใช่ม็อดแปลภาษา** — เป็นม็อด rebalance การต่อสู้ แต่ changelog ของ Judgment Retrial มีบรรทัดที่ใช้อ้างอิงได้: fix บั๊ก "Simplified Chinese language having squares in the text" ตอนเพิ่มการรองรับ zh-Hant/zh-Hans = เคยมีคนชนปัญหา tofu/กลิฟหายบนเอนจิ้นนี้แล้วแก้ได้

## กติกาเหล็ก (สืบทอดจาก K3 ทั้งชุด)
1. ห้ามแก้ไฟล์ใน `runtime/media/data/` — deploy ผ่านโฟลเดอร์ mods เท่านั้น ยกเว้นฟอนต์ (ข้อ 5)
2. ห้ามเปิดเกมเอง — การทดสอบในเกมเป็นหน้าที่ผู้ใช้
3. โปรเจกต์เก่าทุกตัวอ่านอย่างเดียว — จะแก้อะไรให้ copy เข้า PROJECT ก่อน
4. คำแปลรวมมีที่เดียว: `translations/master_th.json` เขียนผ่าน `scripts/merge_qc.py` เท่านั้น
5. ฟอนต์ loose ผ่าน Parless ใช้ไม่ได้ (เกมโหลดฟอนต์ก่อน hook) — ทดสอบฟอนต์ต้อง drop-in ทับ font par โดย **backup เป็น `.orig` ก่อนเสมอ**
6. console Windows = cp1252 — ทุกสคริปต์ `sys.stdout.reconfigure(encoding="utf-8")` + เปิดไฟล์ `encoding="utf-8"` · ห้ามส่งข้อความไทยผ่าน CLI args
7. reARMP ใช้ `tools/reARMP_fixed.py` เท่านั้น + path forward-slash · ตัวนี้มีแพตช์ "JETH fix (5 Sep 2026)": ตารางที่มีคอลัมน์สตริงแต่ TEXT_COUNT 0 ต้องเขียนพอยน์เตอร์ +0x24 = 0 ตามต้นฉบับ (ไม่งั้นเอนจิ้นวาดสตริงสุ่มบน telop ว่าง เช่น MV เปิดเกม a01_035) — reARMP ของโปรเจกต์พี่น้องยังไม่มีแพตช์นี้
8. ห้ามรันเครื่องมือทีละไฟล์เป็นร้อยรอบ — เขียน loop ลง `scripts/`
9. agent ห้ามเขียนไฟล์ใหญ่ใน Write เดียว — แตก `.part` แล้ว merge
10. license/EULA/credits คงอังกฤษ
11. ห้ามรัน deploy ซ้อนสองตัวพร้อมกัน

## ธรรมเนียมทีม + Pipeline + กฎการแปล
ใช้ตาม CLAUDE.md ของ K3 ทุกข้อ (token budget, lead spawn คนเดียว, sonnet translators, merge_qc 7 เกณฑ์, DENY_BINS, DIALOG_TOKEN_RE ฯลฯ) — สคริปต์ port จาก K3 (แทนที่ bis→judge) และ **ค่า game-specific ต้อง verify กับไฟล์ Judgment จริงตอนใช้ครั้งแรก**
- สายบิลด์ของภาคนี้ (ไม่ใช่ `apply_thai.py`/`deploy.py` ของ K3 — ฟอนต์คนละสถาปัตยกรรม) รันตามลำดับ:
  `slot_alloc.py --write` → `inject_thai_title.py --slotmap` (วาด atlas) → คัดลอก atlas เป็น `meta_ot_cond_book_italic.dds` → `build_text.py --clean` (ข้อความทั้งเกม) → `gen_font_bin.py` (ตาราง advance — ต้องรันหลัง `--clean` ทุกครั้ง) → `strip_ui_sprite_slots.py --write` + `patch_drone_menu_titles.py --write` (ui.judge.en loose) → `deploy_spoil.py` (`--restore` ถอน)
  · **กติกาตัดบรรทัดของเอนจิ้น (รอบ 20)**: ช่องว่างใช้ตัดบรรทัดได้เฉพาะเมื่อคำถัดไปยาว ≤ ~40 ตัว (หลัง encode) → `fix_thai_wrap.py` คุมทุก run ไทยไว้ ≤ 36 ตัว (TARGET 30) ก่อน deploy ต้อง `--check` = 0
  ตรวจงานก่อน deploy ด้วย `python scripts/preview_line.py` — จำลองการวาดของเอนจิ้นจาก atlas + ตารางจริง ออกมาเป็น PNG (ผู้ใช้เป็นคนเปิดเกม จึงต้องเห็นผลก่อนส่ง)
  ทั้งฟอนต์และข้อความอ่าน `translations/slotmap.json` ตัวเดียวกัน — แก้การจัดสรรที่เดียวแล้วรันใหม่ทั้งสองฝั่ง
- **เพศผู้พูด (5 ก.ย. 2026 รอบ 19)**: หลักฐานทุกแหล่งรวมที่ `extracted/facts/dialogue_gender.json`
  (`make_dialogue_gender.py --write`) + สรุป `docs/dialogue_gender_table.md` · ก่อน deploy ทุกครั้งรัน
  `fix_dialogue_gender.py` (ต้องเสนอ 0) · คัตซีน `auth.bin` ไม่มีคอลัมน์ผู้พูด → ใช้ `translations/cinema_speakers/`
  (ทีมอ่านบริบทแล้ว 102/102 ฉาก) · ผู้พูด `talk.bin` ที่ไฟล์เกมไม่บอกเพศ → `translations/speaker_gender_overrides.json`
  (รับคีย์ `ชื่อ#speaker_id` เพราะป้ายอย่าง `???` ใช้กับหลายคน)
- glossary ลำดับความสำคัญ: **K3 > Gaiden > Y8 > Y7 > Pirate > K2R** (ใหม่กว่าชนะ) — ตัวละคร/องค์กรฝั่ง Judgment **มีคำล็อกจาก Gaiden + Y7 อยู่แล้วหลายคำ** (ดูรายการบนสุดของไฟล์นี้) เพราะเคยรับเชิญในสองภาคนั้น ที่เหลือ (Sugiura, Saori, Hoshino, Kido, Shono ฯลฯ) เสนอไว้ใน `translations/characters_main.json` + `translations/glossary.md` — lead ตัดสินก่อนเปิด sprint
- บทเรียนที่จ่ายแพงมาแล้ว: ดูหัวข้อเดียวกันใน CLAUDE.md ของ K3 + `docs/reference/FONT_PLAYBOOK.md` (copy มาแล้วในโปรเจกต์นี้)
