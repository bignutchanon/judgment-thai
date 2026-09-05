# Precedent: Thai / complex-script readability in fixed-pitch Japanese game engines

> โจทย์: หา precedent การทำให้ไทย (หรือสคริปต์ซับซ้อนอื่นที่มี combining mark) อ่านออกได้ในเอนจิ้นเกม
> ญี่ปุ่นที่วาด glyph ทุกตัวที่ full-width cell คงที่ (~36-39px) และไม่อ่าน per-glyph advance —
> ตรงกับปัญหาที่เจอใน Dragon Engine (Judgment/Y6/K3 ทั้งตระกูล)
>
> ค้นเว็บ 2026-08-20 (WebSearch/WebFetch, บาง URL ผ่าน r.jina.ai ไม่ได้ใช้เพราะ WebFetch พอเข้าถึงได้ตรง)
> ป้ายกำกับ: **VERIFIED** = อ่าน source ตรง (WebFetch ได้เนื้อหาเต็ม) · **CLAIMED** = เห็นแค่ snippet
> จาก search result · **INTERNAL** = จากเอกสารของโปรเจกต์พี่น้องเราเอง (ไม่ใช่เว็บ แต่เป็น precedent
> ที่ตรงประเด็นที่สุดที่หาได้ เพราะเป็นเอนจิ้นตระกูลเดียวกัน)

---

## สรุปสั้นสำหรับคนรีบอ่าน

ไม่พบใครในโลก (Thai หรือชาติอื่น) ที่**แก้ปัญหา full-width pitch ของสคริปต์ซับซ้อนในเอนจิ้น
ระดับ AAA สมัยใหม่ (Dragon Engine, RE Engine, Fox Engine ฯลฯ) ได้จริงด้วยการแก้ exe/hook** — ทุกเคส
ที่เจอเป็นหนึ่งใน 3 แบบ: (1) **ยอมรับ full-width แล้ว ship เลย** (พบมากที่สุด, ทั้ง Yakuza/Judgment/
Persona/Tales of ฯลฯ), (2) **เอนจิ้นนั้นรองรับฟอนต์ TTF/proportional จริงอยู่แล้ว** จึงไม่มีปัญหานี้
ตั้งแต่ต้น (Unity/UE4 เกมส่วนใหญ่ที่มีม็อดไทย — Nier, Spiritfarer, FF7R ฯลฯ), หรือ (3) **เลี่ยงปัญหา
ด้วย subtitle overlay** แทนการฉีดฟอนต์เข้าเอนจิ้นเกม (ยังไม่ยืนยันเจอเคสจริงที่ทำแบบนี้กับ
full-width engine โดยเฉพาะ — ดู §4)

เอกสารรอบ codebase ของเราเอง (`yakuza-6-thai/docs/exe_hook_feasibility.md`) คือ**ความพยายามแก้ปัญหา
นี้ที่ลึกที่สุดเท่าที่หาเจอที่ไหนก็ตาม** (static RE + runtime dump + Frida dynamic RE + DLL hook 5
เวอร์ชัน) บนเอนจิ้นตระกูลเดียวกับ Judgment เป๊ะ — และ**ยังไม่สำเร็จ** แม้จะเจอกลไก half-width จริง
ในโค้ด (ดู §3) เพราะ Denuvo บล็อค static RE เกือบหมด ต้องหันไป dynamic RE ด้วย Frida ซึ่งก็ยังหา
renderer จริงไม่เจอ — ยืนยันสมมติฐานในโจทย์ ("patching exe/DLL — not achieved on this engine") ด้วย
หลักฐานละเอียดกว่าที่โจทย์สมมติไว้มาก

---

## 1. ม็อดแปลไทยเกมญี่ปุ่นที่ใช้เอนจิ้น fixed-pitch — ทำยังไงกับ vowel/tone stacking และ spacing

### Yakuza / Judgment / Like a Dragon (Dragon Engine — เอนจิ้นเดียวกับเป้าหมายเราเป๊ะ)

- **MOD2SUB series** (ผู้แปล AI เดียวกัน ทำหลายเกม RGG: Judgment
  [nexusmods.com/judgment/mods/228](https://www.nexusmods.com/judgment/mods/228),
  Lost Judgment [nexusmods.com/lostjudgment/mods/472](https://www.nexusmods.com/lostjudgment/mods/472))
  — **CLAIMED/VERIFIED บางส่วน**: หน้า mod ไม่มีรายละเอียดเทคนิคฟอนต์เลย (อ่านตรงแล้วว่างเปล่า) มีแค่
  ขั้นตอนติดตั้งผ่าน RyuModManager/RyuUpdater — วางเป็น loose file ทับ `runtime/media/mods` ปกติ
  (แปลว่าใช้กลไก par/donor เดียวกับที่โปรเจกต์เราใช้อยู่ ไม่ใช่ overlay ภายนอก) ชื่อ "MOD2SUB" **ไม่ได้
  แปลว่า subtitle overlay** อย่างที่คาดตอนแรก — ชื่อกลุ่มนี้เป็นแค่ชื่อแบรนด์ ("mod → subtitle") ของทีม
  แปล AI ที่ทำเกมนับสิบเกม (Hades II, Metaphor, Summer of '58 ฯลฯ) ไม่ใช่ชื่อ tool overlay เฉพาะทาง
- **Judgment "4K Font" mod** [nexusmods.com/judgment/mods/192](https://www.nexusmods.com/judgment/mods/192)
  — **VERIFIED**: แค่แทนที่ atlas เดิมด้วยความละเอียดสูงขึ้น (ลด aliasing) ไม่แตะ layout/spacing เลย —
  ยืนยันว่าไฟล์ฟอนต์ระดับ atlas แก้ได้ตรงไปตรงมา (ตรงกับ pipeline `y6_font_tool.py`/`inject_thai_sdf.py`
  ที่เราใช้อยู่)
- **Yakuza 0 / Kiwami / Like a Dragon Thai mods** (AzuNyanMoeChan, nexusmods.com/yakuza0/mods/1112,
  /500, nexusmods.com/yakuzakiwami/mods/431, nexusmods.com/yakuzalikeadragon/mods/197) — **VERIFIED
  (หน้า mod อ่านแล้ว)**: ทุกหน้าไม่มีการพูดถึงฟอนต์/spacing เลยสักหน้า มีแค่ credit + วิธีติดตั้ง — เข้า
  ข่าย "ship แบบ full-width โดยไม่พูดถึงปัญหา" (ไม่ใช่ "ไม่มีปัญหา" — แค่ไม่มีใครพูดถึงในหน้า mod)
- **GitHub Kaplas80/TranslationFramework2 issue #20 "Font for Yakuza 0"** — **CLAIMED** (WebFetch โดน
  403, เห็นแค่ snippet): มีรายงานปัญหาฟอนต์ไทยไม่ขึ้นตอนแปล Yakuza 0 แต่ไม่มีรายละเอียดวิธีแก้ที่ดึงมาได้

**สรุปกลุ่ม RGG**: ไม่มีม็อดไทยตัวไหนในตระกูล Dragon Engine ที่ประกาศว่าแก้ full-width pitch ได้ —
สอดคล้องกับหลักฐาน INTERNAL ใน §3 ที่ว่าการแก้ที่ระดับ exe เป็นไปได้ยากมากบนเอนจิ้นนี้ (Denuvo)

### Persona 5 (Royal) — เอนจิ้นละครอบครัว Katana Engine (Persona/SMT)

**VERIFIED** (nexusmods.com/persona5royal/mods/22): ใช้ฟอนต์ **"Sarabun Simibold"** (สะกดแบบนี้จริงใน
หน้า mod — พิมพ์ผิดจาก "Semibold") เป็นฟอนต์ TTF ทดแทนตรง ๆ ไม่มีการพูดถึงปัญหา
vowel-stacking/spacing เลย — เข้าข่าย "เอนจิ้นรองรับ TTF proportional อยู่แล้ว" (Persona 5 ใช้ font
rendering ผ่านระบบที่รองรับ TTF จริง ต่างจาก Dragon Engine ที่ใช้ SDF glyph atlas คงที่)

### Final Fantasy (VII Remake / VIII Remastered / IX / XVI) — Luminous/PS engines ต่าง ๆ

**CLAIMED** (จาก search snippets, ไม่ได้ WebFetch เจาะหน้าเพจ): ทุกภาคใช้ฟอนต์ TTF จริง (TH Sarabun,
Ansana, Boon) วางทับเป็นไฟล์ font ปกติ — FFXVI มีรายละเอียดน่าสนใจ: "เพิ่มขอบสีของฟอนต์เพื่อให้อ่านง่าย
ขึ้นบนพื้นขาว" (outline/border technique เพื่อ readability ไม่เกี่ยวกับ pitch) — ทุกเคสนี้ไม่มีปัญหา
full-width pitch เพราะเอนจิ้นรองรับ proportional font จากโรงงานอยู่แล้ว

### Sekiro / FromSoft — ผ่าน Mod Engine (community font-injection framework)

**CLAIMED**: มีม็อด "Font Replacement" (nexusmods.com/sekiro/mods/56) ที่สลับฟอนต์ EN/JA/KR เป็นฟอนต์
อื่นได้ผ่าน Mod Engine — ไม่พบม็อดไทยที่ประกาศ published ใน Nexus (มี "Thai Translation Patch for Long
May the Shadows Reflect" ซึ่งเป็นชื่อ mod แต่ระบบ FromSoft ใช้ font ระบบมาตรฐานที่รองรับ TTF ผ่าน Mod
Engine ได้อยู่แล้ว — ไม่ใช่ fixed-pitch atlas แบบ Dragon Engine)

### Monster Hunter Rise/World, Nier Automata — RE Engine / Unreal-style proportional

**VERIFIED** (nexusmods.com/monsterhunterrise/mods/2018): "Thai Font Fix" = **font replacement ตรง
ๆ** ผ่าน Fluffy Manager — แก้ปัญหา tofu-box (ไม่ใช่ปัญหา spacing) เพราะฟอนต์เดิมไม่มี glyph ไทยเลย ไม่ใช่
ปัญหา full-width pitch — เอนจิ้นนี้รองรับ proportional font อยู่แล้ว ปัญหามีแค่ "ฟอนต์ไม่มีตัวอักษรไทย"
ไม่ใช่ "มีแต่ห่างเกินไป"

### สรุปข้อ 1

ไม่มีเคสไหนในโลกที่หาเจอ (ทั้ง Thai และเทียบกับสคริปต์ซับซ้อนอื่น) ที่ต้องแก้ปัญหา **fixed
full-width-cell pitch ที่ไม่อ่าน metrics เลย** แบบเดียวกับ Dragon Engine โดยเฉพาะ — เพราะเอนจิ้นเกม
AAA สมัยใหม่ส่วนใหญ่ (Unity/UE4/RE Engine/Luminous ฯลฯ) รองรับ proportional TTF font จากโรงงานอยู่แล้ว
ปัญหาที่ม็อดไทยทั่วไปเจอคือ "ฟอนต์เดิมไม่มีกลิฟไทย" (แก้ด้วยแทนที่ไฟล์ font ตรง ๆ) ไม่ใช่ "มี glyph
แต่ pitch เต็มช่องเสมอ" — Dragon Engine (และรุ่นก่อนหน้าอย่าง PS2/PS3-era JP engines ที่คง SDF-atlas
mono-cell ไว้) เป็นกลุ่มที่หายากกว่ามาก และไม่มีใครประกาศแก้ pitch ได้จริง

---

## 2. คลังเทคนิคที่นักแปลไทยใช้จริง (technique inventory)

จากการอ่านเอกสารทั้ง RPG Maker community และ RGG family:

| เทคนิค | ใช้ที่ไหน | รายละเอียด | ป้ายกำกับ |
|---|---|---|---|
| **Pre-composed cluster glyph** (base+สระ+วรรณยุกต์วาดรวมเป็น 1 เซลล์) | Dragon Engine family (K3/Gaiden/Y8/K2R/Y6 — INTERNAL, เอกสารโปรเจกต์เราเอง) | ยังคง full-pitch ต่อ cluster แต่แก้ปัญหา "ตัวอักษรกระจายเป็นตัว ๆ" เพราะ 1 cell = 1 คำ/พยางค์สมบูรณ์ ไม่ใช่ 1 phoneme | INTERNAL, VERIFIED (ใช้จริงมาแล้ว 3+ เกม) |
| **Donor-slot injection** (ฉีดกลิฟไทยทับ Latin-diacritic codepoint ที่มี "หมึก" อยู่แล้วในฟอนต์) | เดียวกับข้างบน | ไม่ต้องขยาย charmap เพราะ charmap อยู่ใน exe แก้ไม่ได้ — ใช้ slot ที่มีอยู่แล้วเท่านั้น | INTERNAL, VERIFIED |
| **ASCII-class half-width mechanism มีอยู่จริงในโค้ดเกม** (แต่ retarget ไม่สำเร็จ) | Y6 (Dragon Engine) | โค้ดเกมมี `if (codepoint < 0x80) advance *= 0.5` จริง (พิสูจน์จาก decompile) — แต่การ hook ให้ donor ไทย/CJK ได้ path เดียวกันไม่ทำให้ glyph ขยับ เพราะ function ที่ hook ได้เป็นแค่ "measure" ไม่ใช่ "draw" | INTERNAL, VERIFIED (อ่าน source/decompile ตรง) — ดู §3 |
| **Vowel/tone-mark reposition offset (RPG Maker MV/VX/XP)** | RPG Maker family (`irpg.in.th/thread-3699`, `planila.blogspot.com/2017/03/rpg-maker-mv.html`) | เลื่อนตำแหน่ง y ของสระบน/วรรณยุกต์ตามคลาสพยัญชนะ (ป/ฝ/ฟ ต้องเลื่อนสูงกว่าปกติ, ญ/ฐ ชนสระล่าง) ผ่านการแก้ `Window_Base.prototype.convertEscapeCharacters` หรือ script `Font.default_name`/`Window_Message` โดยตรง — แก้ที่ตำแหน่ง glyph ไม่ใช่ pitch | VERIFIED (อ่าน source ตรงทั้งคู่) |
| **Alternate-codepoint duplication ผ่าน FontForge + TextMeshPro SDF** | เกม Unity ทั่วไป (`gist.github.com/rutcreate`) | copy กลิฟสระ/วรรณยุกต์ไปวางที่ตำแหน่ง Unicode สำรอง (Character Sequence กำหนดช่วง codepoint เอง เพราะ TMP ใช้ atlas ของตัวเอง ไม่ผูกกับ charmap เกม) แล้วปรับตำแหน่ง glyph รายตัว (shift ซ้าย/ล่าง/ซ้าย-ล่าง) | VERIFIED (อ่าน gist ตรง) |
| **Font replacement ตรงไปตรงมา (TTF/OTF)** | Persona 5R, FF7R/8/9/16, Monster Hunter, Nier, Spiritfarer | ใช้ได้เฉพาะเอนจิ้นที่รองรับ proportional font จริงอยู่แล้ว — ไม่เกี่ยวกับปัญหา pitch เลย | VERIFIED/CLAIMED (หลายเคส) |
| **ASI hook / Mod Engine loader สำหรับสลับไฟล์ฟอนต์** | Sekiro, MGSV (`FoxEngine.TranslationTool` โดย Atvaark), เกม PC ทั่วไป | ใช้แค่ "โหลดไฟล์ทดแทน" ไม่ใช่ hook logic การวาด glyph — คนละระดับกับที่โจทย์เราต้องการ (patch การคำนวณ advance/pitch) | CLAIMED |

**ชื่อเครื่องมือ/ผู้เขียนที่ยืนยันได้จริง:**
- `RyuModManager` / `SRMM` (ผู้เขียน: **mosamadeeb**, github.com/mosamadeeb/RyuModManager) — mod loader
  มาตรฐานของ RGG family ทั้งหมด รวม Judgment — VERIFIED (อ่าน GitHub release page)
- `FoxEngine.TranslationTool` (ผู้เขียน: **Atvaark**) — เครื่องมือแกะ/แปล string ของ Fox Engine (MGSV)
  — CLAIMED (เจอชื่อใน search แต่ไม่ได้เจาะรายละเอียด)
- `rutcreate` (GitHub gist) — เทคนิค FontForge + TMP character-sequence สำหรับแก้วรรณยุกต์ลอย — VERIFIED
- Planila (blogspot) — เทคนิค RPG Maker MV Thai fix (`Window_Base.prototype.convertEscapeCharacters`) —
  VERIFIED
- **ทีมโปรเจกต์เรา (K3/Gaiden/Y8/K2R/Y6)** — donor-slot + pre-composed cluster pipeline
  (`thai_encode.py`, `inject_thai_sdf.py`, `y6_font_tool.py`) — INTERNAL, VERIFIED (ใช้จริง ship แล้ว)

**ที่ไม่พบเลยในการค้น:** ไม่มีบทความ/เคสไหนพูดถึง "tone-mark tiering" เป็นศัพท์เทคนิคเฉพาะ (คำนี้ดูจะ
เป็นศัพท์ที่ตั้งขึ้นในโจทย์ ไม่ใช่ศัพท์ที่ใช้จริงในคอมมูนิตี้) — สิ่งที่ใกล้เคียงที่สุดคือ "การเลื่อนชั้น
วรรณยุกต์ตามพยัญชนะ" ใน RPG Maker fix ข้างบน ซึ่งเป็นการแก้ตำแหน่ง glyph ไม่ใช่การแบ่ง "ชั้นความสำคัญ"
ของวรรณยุกต์แต่อย่างใด

---

## 3. เคยมีใครยัดสคริปต์ non-Latin ลง ASCII slot (0x20-0x7E) เพื่อรับ proportional spacing ไหม?

**ผลค้นหา: ไม่พบเคสสำเร็จที่ไหนเลยทั้งเว็บอังกฤษและไทย** (negative result ที่มีน้ำหนัก — ค้นด้วย query
หลายแบบทั้ง Thai/Arabic/Vietnamese/Korean × ASCII-slot × half-width) — เคสที่ใกล้เคียงที่สุดที่เจอคือ
ของ**โปรเจกต์พี่น้องเราเอง** (INTERNAL):

`yakuza-6-thai/docs/exe_hook_feasibility.md` (อ่านเต็มไฟล์) บันทึกไว้ว่า:
- **✅ พิสูจน์จาก decompile จริง (runtime dump ผ่าน Denuvo ได้ + Ghidra)**: โค้ดเกม Y6 มีกลไก
  half-width ฝังอยู่จริงในฟังก์ชัน render/advance (`FUN_7ff65adf1a50`) — บรรทัด: `if (param_10 < 0x80)
  { adv *= 0.5; bearing *= 0.5; }` โดย `param_10` คือ codepoint (UTF-8 packed) — แปลว่า **engine เอง
  แยกคลาส ASCII (<0x80) ให้ได้ half-width โดยธรรมชาติอยู่แล้ว** ตรงกับสมมติฐานในคำถามเป๊ะ
- ทีมลองเขียน DLL hook (`dinput8.dll` proxy, เวอร์ชัน v5) เพื่อ retarget ให้ donor cp (Cyrillic
  0x400+, CJK cluster) วิ่งผ่าน path เดียวกับ ASCII (คูณ 0.5) — **ติดตั้ง hook สำเร็จ, log ยืนยันว่า
  donor codepoint ทุกตัว match ถูกต้อง (`srcAdv=20.0` = ครึ่งจาก 40) แต่ glyph บนจอไม่ขยับเลย**
- สาเหตุที่พิสูจน์แล้ว (§0'''' ของเอกสาร): ฟังก์ชันที่ hook ได้ (`FUN_7ff65adf1a50` + walker
  `FUN_7ff65ade7f70`) เป็น **"measure" subsystem** (คำนวณ bounding box สำหรับ layout/wrap) **ไม่ใช่
  "draw" subsystem จริง** — ตัว emit glyph quad จริงยังหาไม่เจอ (สงสัยว่าอยู่ใน D3D11 draw-call
  pipeline คนละ path, ต้องทำ (a) hook `DrawIndexed`/`PSSetShaderResources` ไล่ backtrace หรือ (b) Frida
  Stalker trace ทั้งเฟรม — ทั้งคู่ยังไม่ได้ทำ เพราะเป็น session แยกที่มี risk สูง)
- Frida (dynamic instrumentation) ใช้งานได้จริงบน Y6 ทั้งที่มี Denuvo (breakthrough ของ session นั้น)
  — แต่ backtrace ผ่าน optimized+protected binary ไม่แม่นพอไล่ถึง renderer จริง

**สรุปสำหรับคำถามนี้**: มี "ต้นแบบทางทฤษฎี" ของกลไก half-width ในโค้ดเกมจริง (พิสูจน์แล้วด้วย
decompile) และมีความพยายาม retarget อย่างจริงจัง (DLL hook 5 รุ่น + runtime dump + Frida) แต่**ยังไม่
สำเร็จ** — ไม่ใช่เพราะไม่มีกลไกให้ยัด แต่เพราะหา "จุด hook ที่ถูกต้อง" (draw ไม่ใช่ measure) ไม่เจอ
ภายใต้การป้องกัน Denuvo ส่วนคำถามย่อย "ถ้าจะใช้ ASCII 95 ช่องจะพอไหม/ตัวเลข-control tag จะพังไหม" —
**ไม่เคยไปถึงขั้นทดสอบจริงในเกม** เพราะติดที่ต้นทาง (หา hook site ที่ใช่ก่อน) — เป็นคำถามที่ยังไม่มี
คำตอบเชิงประจักษ์จากใครเลย

---

## 4. ทางเลือกสมัยใหม่: เปลี่ยน atlas เป็น proportional / ใช้ language slot อื่น / ใช้ overlay layer

- **เปลี่ยน atlas ทั้งชุดเป็น proportional**: ไม่พบเคสไหนทำสำเร็จบนเอนจิ้น fixed-pitch จริง (ดู §1, §3)
  — เพราะปัญหาไม่ได้อยู่ที่ atlas (atlas แก้ได้ตรงไปตรงมาอยู่แล้ว ตามที่ทีมเราเองก็ทำได้ — ปัญหาอยู่ที่
  renderer/layout code ไม่อ่าน metrics เลย ซึ่งอยู่นอกไฟล์ atlas)
- **ใช้ language slot อื่นที่ proportional อยู่แล้ว**: ตรวจ `docs/exe_hook_feasibility.md` และ
  `FONT_PLAYBOOK.md` ไม่เจอหลักฐานว่า Dragon Engine มี language mode ไหนที่ layout ต่างกัน (JP/EN ทั้งคู่
  ยืนยันแล้วว่าใช้ full-width สำหรับ wide-class เหมือนกัน — ปัญหาอยู่ที่ "wide-class vs narrow-class"
  ไม่ใช่ "ภาษาไหน") — ไม่มี precedent ว่ามี slot ลับที่ proportional
- **Subtitle overlay layer แยกจากเอนจิ้นเกม** (เช่น ReShade overlay, DirectX hook วาด text ทับ, หรือ
  ImGui overlay): **ไม่พบเคสจริงที่ยืนยันได้ว่าทำแบบนี้กับเกมที่มีปัญหา full-width pitch โดยเฉพาะ** —
  ชื่อ "MOD2SUB" ที่ดูเหมือนจะสื่อถึงเทคนิคนี้ กลับกลายเป็นแค่ชื่อแบรนด์ของทีมแปล AI เท่านั้น (§1) ไม่ใช่
  ชื่อ tool overlay จริง — เกมที่ modder ทำ "mod sub" ในความหมาย overlay จริง ๆ (เช่น XUnity.AutoTranslator,
  Rei Patcher — พบใน GBAtemp/nexusmods) ล้วนเป็นเกม engine ที่มี proportional text UI อยู่แล้ว
  (Unity/RenPy ทั่วไป) — เป็นการแปลสด ไม่ใช่การแก้ font-pitch ของเอนจิ้นที่ fixed-width แต่อย่างใด — จึง
  **ไม่ใช่ precedent ที่ตรงประเด็นกับ Dragon Engine**
- **ข้อสังเกตสำคัญ**: การทำ overlay layer (วาด text ทับเกมด้วย renderer ของ mod เอง ไม่ใช้ font
  engine เดิมเลย) เป็นแนวทางที่ **น่าจะเป็นไปได้ในทางทฤษฎี** (คล้าย ReShade ImGui overlay ที่เกมอื่นใช้
  แปลสด) แต่**ไม่มีใครเคยพิสูจน์ว่าใช้ได้กับ Dragon Engine** และมีข้อเสียที่ทีมงานคงต้องพิจารณาเอง
  (ต้องมี dialogue box positioning/timing sync เอง, เสี่ยง Denuvo เหมือนกับ DLL hook อื่น ๆ) — ไม่มี
  หลักฐานสนับสนุนหรือคัดค้านจากการค้นครั้งนี้ เป็นแค่ direction ที่ยังไม่มีใครลอง (หรือมีคนลองแต่ไม่ได้
  เขียนบันทึกไว้ที่ไหนที่ค้นเจอ)

---

## 5. ตัวอย่างที่ ship ทั้งที่ spacing กว้าง + ปฏิกิริยาผู้เล่น

- **INTERNAL** (`FONT_PLAYBOOK.md`, ทีมเราเอง): "**spacing กว้าง = known-limitation เดียวกับ Y0DC ที่
  ship จริง**" — ยืนยันว่าทีมงานเคย ship เกมตระกูล RGG ด้วย full-width spacing มาแล้วอย่างน้อย 1 ภาค
  (Y0DC = โปรเจกต์ codename ก่อนหน้า) และ**ยอมรับเป็น known-limitation** ไม่ใช่ blocker — เป็นบรรทัดฐาน
  ที่ทีมตั้งไว้เองแล้วสำหรับ Y6/K3/Y8/Gaiden ทั้งหมด (แปลว่า Judgment ก็น่าจะใช้บรรทัดฐานเดียวกันได้)
- **ทุกม็อดไทยของ RGG family ที่ตรวจหน้า Nexus แล้ว** (Yakuza 0/Kiwami/Like a Dragon/Judgment/Lost
  Judgment) — **ไม่มีหน้าไหนพูดถึงปัญหา spacing เลยแม้แต่หน้าเดียว** ทั้งในคำอธิบายและ (เท่าที่ WebFetch
  ดึงได้) ไม่เจอ comment ที่บ่นเรื่องนี้โดยตรง — ตีความได้ 2 ทาง: (a) full-width spacing ไม่ใช่ปัญหาใหญ่
  พอที่ผู้เล่นทั่วไปจะบ่นในหน้า mod (ผู้เล่นไทยที่โหลดม็อดเหล่านี้คุ้นเคยกับสภาพนี้อยู่แล้วเพราะเป็น
  norm ของทั้งตระกูล) หรือ (b) ข้อมูลจำกัดจาก WebFetch summarizer ที่ไม่ได้ดึง comment section เต็ม —
  **ไม่สามารถฟันธงได้ 100% ว่าไม่มีใครบ่นเลย** เพียงแค่ไม่พบหลักฐานการบ่นในสิ่งที่เข้าถึงได้
- **RPG Maker community**: ตรงข้ามกับ RGG — คอมมูนิตี้นี้ถือว่าวรรณยุกต์ลอย/ชนกันเป็นปัญหาที่ต้อง "แก้"
  ไม่ใช่ "ยอมรับ" (มี thread/plugin แก้เฉพาะทางหลายตัว) แต่นั่นเป็นปัญหาคนละแบบ (glyph วางผิดตำแหน่ง ไม่
  ใช่ pitch กว้าง) — บ่งชี้ว่าคอมมูนิตี้ไทยแยกแยะ "อ่านไม่ได้เพราะ glyph ชนกัน/แตก" (severity สูง ต้องแก้)
  ออกจาก "อ่านได้แต่ไม่สวย/ห่างเกิน" (severity ต่ำกว่า ยอมรับได้) อย่างชัดเจน — สอดคล้องกับที่ทีมเรา
  ตัดสินใจ ship full-width spacing ของ RGG family มาตลอด

---

## ข้อสรุปที่ใช้ต่อได้จริงสำหรับ Judgment

1. **Full-width spacing เป็นบรรทัดฐานที่ยอมรับได้ทั้งวงการ** — ไม่มีม็อดไทยเกมไหนในตระกูล fixed-pitch
   engine (RGG หรืออื่น) แก้ปัญหานี้ได้จริง รวมถึงพี่น้องเราเองที่ลงทุนหนักที่สุดในการหา (Y6) ก็ยังไม่
   สำเร็จ — **การวางแผน ship Judgment ด้วย full-width + pre-composed cluster (แบบเดียวกับ K3/Y8) เป็น
   แนวทางที่ปลอดภัยและสอดคล้องกับ precedent ทั้งหมด**
2. **ถ้าอยากลอง exe hook สำหรับ Judgment ในอนาคต** ให้เริ่มจาก lesson ของ Y6 โดยตรง: (a) หา draw-call
   subsystem ผ่าน D3D11 hook ก่อนไล่ measure function (b) ต้อง runtime dump/Frida ผ่าน Denuvo ก่อน
   static RE จะไม่มีความหมาย (c) เตรียมใจว่าเป็นงาน session แยกที่มี risk สูงและไม่การันตีผล
3. **Subtitle-overlay เป็น direction ที่ไม่มีใครพิสูจน์ทั้งด้านบวกและลบ** — ถ้าจะสำรวจต้องเริ่มจากศูนย์
   ไม่มี precedent ให้อ้างอิงได้เลยสำหรับเอนจิ้นตระกูลนี้โดยเฉพาะ
4. **Pre-composed cluster + donor-slot injection ที่ทีมใช้อยู่แล้ว** ยังคงเป็นทางออกที่ verified มาก
   ที่สุดในบรรดาทุกทางเลือกที่สำรวจมา (ship แล้วจริงหลายเกม ไม่ใช่แค่ทฤษฎี)

---

## แหล่งอ้างอิงทั้งหมด

**VERIFIED (WebFetch อ่านเนื้อหาเต็ม):**
- https://www.nexusmods.com/judgment/mods/228 (MOD2SUB Judgment)
- https://www.nexusmods.com/judgment/mods/192 (4K Font)
- https://www.nexusmods.com/persona5royal/mods/22
- https://www.nexusmods.com/monsterhunterrise/mods/2018
- https://www.nexusmods.com/yakuzakiwami/mods/431
- https://www.nexusmods.com/yakuza0/mods/1112
- https://www.nexusmods.com/yakuzalikeadragon/mods/197
- https://gist.github.com/rutcreate/cbc7d3aabeb6983007db7c2d0290719b
- https://irpg.in.th/thread-3699.html
- https://planila.blogspot.com/2017/03/rpg-maker-mv.html
- https://gbatemp.net/threads/translation-and-font-hacking.562889/
- https://xn--o3cfe5a8azf.com/วิธีแก้-spiritfarer-farewell-edition-mod-sub-ไทย-ขึ้นเป/

**CLAIMED (เห็นแค่ snippet จาก search):**
- GitHub Kaplas80/TranslationFramework2 issue #20 (403 บล็อค WebFetch)
- FF7R/FF8/FF9/FF16 Thai mod pages (nexusmods.com/finalfantasy...)
- MGSV Thai mod (nexusmods.com/metalgearsolidvtpp/mods/2178), FoxEngine.TranslationTool by Atvaark
- Sekiro font/translation mods (nexusmods.com/sekiro/mods/56, /1006, /1193)
- Monster Hunter World/Wilds Thai AI localization mods

**INTERNAL (เอกสารโปรเจกต์พี่น้อง ไม่ใช่เว็บ แต่เป็น precedent ตรงประเด็นที่สุด):**
- `D:\Projects\yakuza-6-thai\docs\exe_hook_feasibility.md` (อ่านเต็มไฟล์)
- `D:\Projects\judgment-thai\docs\reference\FONT_PLAYBOOK.md` (อ่านเต็มไฟล์)

**Negative results (ค้นแล้วไม่พบ — บันทึกไว้เพราะมีมูลค่า):**
- ไม่พบเคสสำเร็จของการยัด non-Latin script ลง ASCII codepoint slot (0x20-0x7E) เพื่อรับ
  half-width/proportional spacing ในเกมญี่ปุ่นใด ๆ (ค้นทั้ง Thai/Arabic/Vietnamese/Korean)
- ไม่พบ "tone-mark tiering" เป็นศัพท์เทคนิคที่ใช้จริงในคอมมูนิตี้ไหน
- ไม่พบ subtitle-overlay tool ที่พิสูจน์แล้วว่าใช้แก้ปัญหา full-width pitch บนเอนจิ้นตระกูล Dragon
  Engine หรือเอนจิ้น fixed-pitch อื่นที่เทียบเคียงได้
