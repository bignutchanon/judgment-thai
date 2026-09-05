# Judgment / Lost Judgment — สำรวจข้อมูล modding สาธารณะ (web research, 20 ส.ค. 2026)

สโคป: เฉพาะสิ่งที่หาได้จากอินเทอร์เน็ตสาธารณะเกี่ยวกับการม็อด Judgment (2022 PC) และ Lost Judgment (2021 PC) — ไม่ได้แตะไฟล์เกมจริง ไม่ได้โหลดม็อดใดๆ ทุกข้อมูลมาจาก WebSearch/WebFetch (ผ่าน r.jina.ai proxy สำหรับหน้า nexusmods/pcgamingwiki ที่บล็อก WebFetch ตรง) และ `gh` CLI สำหรับ GitHub

หมายเหตุคุณภาพแหล่งข้อมูล: หน้า nexusmods หลายหน้าถูกอ่านผ่าน r.jina.ai แล้วสรุปโดยโมเดลตัวช่วยของ WebFetch เอง (ไม่ใช่ raw HTML) — ถือว่า VERIFIED ในระดับ "อ่านเนื้อหาหน้าเพจจริงแล้ว" แต่รายละเอียดปลีกย่อยบางจุดอาจถูกย่อหาย ควรเปิดหน้าเพจจริงอีกทีตอนจะใช้งานจริง

---

## 1. ม็อดแปล/localization ที่มีอยู่แล้ว

### 1.1 Judgment MOD2SUB TH EN (Thai)
- URL: https://www.nexusmods.com/judgment/mods/228 — **VERIFIED** (อ่านผ่าน r.jina.ai)
- ผู้ทำ: Maimaomaiplae (เพจ FB "ไม่เมาไม่แปล") ใช้ Google Translate เป็นฐาน — **ตรงกับที่ CLAUDE.md เตือนไว้แล้วว่าห้ามใช้เป็น TM**
- เวอร์ชันล่าสุดที่เห็น: V1.12 (ไฟล์ชื่อ `JusgmentModThaiV1.2.zip` — สังเกตเลขเวอร์ชันในชื่อไฟล์กับหน้าเพจไม่ตรงกันเป๊ะ อาจเป็น typo ของผู้เขียน)
- ติดตั้ง: copy ทั้งโฟลเดอร์ไปที่ `...\Judgment\runtime\media` แล้วรัน `RyuUpdater.exe` → `RyuModManager.exe` → `RyuModManagerGUI.exe` → Install → เลือกไฟล์ zip → กดยืนยัน (checkmark) → เข้าเกม
- **ยืนยันว่าใช้ RyuModManager/SRMM family เป็นตัวติดตั้ง** ไม่ใช่ replace ไฟล์ตรงๆ ใน par
- ไม่มีข้อมูลเรื่องฟอนต์/glyph ใหม่/spacing บนหน้าเพจ (คำอธิบายไม่ลงลึกเทคนิค) — มีรายงานบั๊ก 2 รายการแต่ไม่ระบุรายละเอียด
- **ไม่มีข้อมูลว่าม็อดนี้แก้ฟอนต์เพิ่มกลุ่มอักษรไทยหรือไม่** — เป็นไปได้สูงว่าใช้ฟอนต์เดิมของเกม (EN) เพราะ Google Translate เป็น MT ภาษาไทยที่พิมพ์ด้วยอักษรไทยจริง แปลว่าต้องมีการเพิ่ม glyph ไทยเข้าไปในฟอนต์เกมไม่ทางใดก็ทางหนึ่ง — จุดนี้ควร verify โดยโหลดม็อดมาแกะเนื้อไฟล์ (ไม่ใช่แค่ติดตั้งเข้าเกม) ถ้าต้องการรายละเอียดฟอนต์จริง

### 1.2 Lost Judgment V1.12 MOD2SUB TH EN
- URL: https://www.nexusmods.com/lostjudgment/mods/472 — **VERIFIED** (อ่านผ่าน r.jina.ai)
- ผู้ทำคนเดียวกัน (Maimaomaiplae) วิธีติดตั้งเหมือนกันทุกประการ (copy → RyuUpdater → RyuModManager → RyuModManagerGUI → เลือก `LJMMODTH.zip`)
- ให้เครดิต Veerayut Niranwattanadacha (ผู้ให้เกม) — ไม่มีรายละเอียดฟอนต์/spacing เช่นกัน

### 1.3 Judgment "Retrial" (mod 203) — **ไม่ใช่ม็อดแปลภาษา**
- URL: https://www.nexusmods.com/judgment/mods/203 — **VERIFIED**
- แก้ไข **gameplay/combat rebalance** (ความเร็ว combo, quickstep cancel, hit bounce, ports skills จาก Lost Judgment มา ฯลฯ) — ไม่ใช่ม็อดแปลอย่างที่ CLAUDE.md สรุปไว้ตอนต้น (ต้อง correct ความเข้าใจตรงนี้)
- **สิ่งที่เกี่ยวกับข้อความ**: หน้าเพจระบุว่า mod "compatible with English, Traditional Chinese, Simplified Chinese, and Korean text language settings" — และ **changelog มี entry แก้บั๊ก "Simplified Chinese language having squares in the text"** (ตัวสี่เหลี่ยม/tofu) — เครดิตให้ YohaneShiro ที่ช่วยเพิ่ม Traditional/Simplified Chinese support ตั้งแต่ v1.0b
- **นี่คือหลักฐานเชิงประจักษ์ชิ้นสำคัญที่สุดที่เจอในรอบนี้**: ยืนยันว่า **การเปลี่ยนภาษา/เพิ่มการรองรับภาษาใหม่ในเกมตระกูลนี้เคยเจอบั๊ก glyph-หาย/tofu จริง** และมีคนแก้ได้สำเร็จ (แต่หน้าเพจไม่ได้ลงรายละเอียดทางเทคนิคว่าแก้ยังไง — CLAUDED, ต้องขุด comments/posts เพิ่มถ้าต้องการ how-to)
- ติดตั้งด้วย Shin Ryu Mod Manager, เวอร์ชันล่าสุด 1.0e (ต.ค. 2024), เครดิตเครื่องมือ Kaplas80, HeartlessSeph และอื่นๆ

### 1.4 Lost Judgment "Retrial" (mod 641)
- URL: https://www.nexusmods.com/lostjudgment/mods/641 — **VERIFIED**
- เป็น combat/gameplay rebalance เช่นกัน (ครอบคลุมทั้งเกมหลักและ DLC "The Kaito Files")
- ระบุชัดว่า **"Only compatible with English and Korean text language setting"** — ต่างจากฝั่ง Judgment Retrial ที่รองรับ zh-Hant/zh-Hans ด้วย — บ่งชี้ว่าการทำให้ mod เข้ากันได้กับแต่ละภาษาต้องทำทีละภาษา (ไม่ auto-compatible) เพราะ mod นี้อาจแก้ ARMP/ข้อความบางไฟล์ที่ผูกกับ carrier ภาษา
- v1.1c ล่าสุด (เม.ย. 2026)

### 1.5 Judgment "4K Font" (mod 192) — ม็อดฟอนต์ (ไม่ใช่แปลภาษา แต่เกี่ยวกับฟอนต์โดยตรง)
- URL: https://www.nexusmods.com/judgment/mods/192 — **VERIFIED**
- โดย Asterra (ต.ค. 2023) — เพิ่มความละเอียดฟอนต์หลักของเกมเป็น "4K" แทนต้นฉบับ 1080p เพื่อลด aliasing
- ติดตั้งได้สองทาง: ผ่าน RyuModManager `\Judgment\runtime\media\mods` **หรือ replace ไฟล์เกมตรงๆ** — ยืนยันว่า **ฟอนต์ของ Judgment สามารถ drop-in ทับได้ทั้งสองทาง** (สอดคล้องกับที่ CLAUDE.md บอกว่า Parless โหลดฟอนต์ไม่ทัน ต้อง drop-in ทับไฟล์จริงเท่านั้น)
- ข้อจำกัดที่ผู้ทำระบุ: ตัวเลข/ตัวอักษรบางตัวใน "minigame" บางตัวเป็นภาพกราฟิกแยก ไม่ใช่ font glyph เลยแก้ผ่านฟอนต์ไม่ได้ (ยังคง 1080p แม้ทั้งเกมจะ 4K) — เป็นข้อควรระวังสำหรับทีมแปล: ป้าย/asset ในบาง minigame ไม่ใช่ text glyph
- ไม่มีรายละเอียด format ไฟล์ฟอนต์ (dds/FONT! ฯลฯ) หรือเครื่องมือที่ใช้สร้างบนหน้าเพจ — ต้อง reverse-engineer เอง (ตรงกับสถานะที่ CLAUDE.md ระบุไว้แล้วว่ายังไม่มีใคร document พับลิกเรื่องนี้)

### 1.6 Russian: "Text Localizer" (Judgment)
- URL: https://vgtimes.com/games/judgment/files/78732-text-localizer.html — **VERIFIED** (แต่หน้านี้เป็น mirror/aggregator ไม่ใช่ต้นทาง อาจไม่ครบ)
- โดย rtmrus, อัปโหลด ม.ค. 2025, แปล UI/เนื้อเรื่องเป็นรัสเซีย (ไม่แปล minigame)
- ติดตั้ง: แตกไฟล์ทับ `Judgment\runtime\media\data` ตรงๆ (**ไม่ผ่าน RyuModManager** — เป็นวิธี legacy/replace-in-place ซึ่งขัดกับกติกาเหล็กข้อ 1 ของโปรเจกต์เรา และเสี่ยงกว่า)
- ไม่มีรายละเอียดฟอนต์/technical notes บนหน้า mirror นี้

### 1.7 Chinese/Spanish/Portuguese fan translations
- ไม่พบม็อดแปล Chinese/Spanish/Portuguese แยกเฉพาะสำหรับ Judgment/Lost Judgment ในการค้นรอบนี้ (มีแต่ PCGamingWiki "List of Traditional/Simplified Chinese fan translations" ที่ปรากฏเป็นผลค้นหา — **CLAIMED เท่านั้น** เพราะ pcgamingwiki.com บล็อก WebFetch/proxy ด้วย Cloudflare 403 ทั้งทาง WebFetch ตรงและผ่าน r.jina.ai ไม่สามารถอ่านเนื้อหาจริงได้ในรอบนี้ — ต้องลองใหม่ด้วยวิธีอื่น เช่น archive.org แบบระบุ timestamp เจาะจง หรือดูผ่านเบราว์เซอร์จริง)
- ประเด็น "Simplified Chinese squares in text" ใน Retrial mod (ข้อ 1.3) คือหลักฐานทางอ้อมที่ใกล้เคียงที่สุดที่ยืนยันได้ว่ามีการดัดแปลง/เพิ่มการรองรับภาษาจีนในเกม Judgment มาก่อน

---

## 2. เครื่องมือ (tools)

### 2.1 Shin Ryu Mod Manager (SRMM) + Parless
- Repo: https://github.com/SRMM-Studio/ShinRyuModManager — **VERIFIED** (อ่าน README ผ่าน `gh api`)
- ผู้เริ่มโปรเจกต์เดิม: SutandoTsukai181 (ปัจจุบันมูฟไปอยู่ org SRMM-Studio, มี Kaplas80/Pleonex/Kent/CookiePLMonster ร่วมเครดิต)
- โหลดม็อดจากโฟลเดอร์ `/mods/` ในโฟลเดอร์เกม — **ไม่ต้อง repack PAR สำหรับเกม Dragon Engine เป็นต้นไป (รวม Judgment/LJ)** — repack PAR จำเป็นเฉพาะเกม Old Engine (ก่อน Yakuza 6) เท่านั้น
- เวลารันจะ generate ไฟล์ MLO ให้ **Parless** (`YakuzaParless`, ASI hook) ใช้ redirect path ไฟล์ให้โหลดจาก loose file แทนไฟล์ใน PAR
- Parless README (https://github.com/SRMM-Studio/YakuzaParless — VERIFIED): ข้อจำกัดปัจจุบันคือไฟล์ที่โหลดผ่านฟังก์ชันอื่นนอกเหนือจาก path ปกติ redirect ไม่ได้ — ส่วนใหญ่คือ middleware audio/video container (`.usm` ทุกเกม, `.cpk` เฉพาะ Y5) — **ไม่มีการระบุว่าไฟล์ฟอนต์อยู่ในข้อยกเว้นนี้** แต่ CLAUDE.md ของโปรเจกต์เราระบุจากประสบการณ์ตรงจริงว่า "ฟอนต์ loose ผ่าน Parless ใช้ไม่ได้ (เกมโหลดฟอนต์ก่อน hook)" — ข้อมูลนี้จึงเป็น **จากประสบการณ์ตรง/testing ของทีมเรา ไม่ใช่จาก README สาธารณะ** (README ไม่ได้พูดเรื่องนี้ตรงๆ) ควรถือเป็นข้อเท็จจริงเฉพาะโปรเจกต์ ไม่ใช่ spec สาธารณะที่ verify ได้จากภายนอก
- Wiki "Supported Games" (https://github.com/SutandoTsukai181/RyuModManager/wiki/Supported-Games — VERIFIED ผ่าน raw githubusercontent): รายชื่อเกมที่รองรับรวม Judgment, Lost Judgment, Yakuza 0 ถึง Like a Dragon, VF eSports (เฉพาะส่วน Dragon Engine) — **ทดสอบเฉพาะ Steam version เท่านั้น**
- Wiki "Creating A New Mod": โครงสร้างโฟลเดอร์ม็อดต้อง mirror `/data/` ของเกม (ไม่ต้องมี `/data/` เป็นชั้นบนสุด) — ไม่มีเนื้อหาเจาะจงเรื่อง par/loose rules หรือ font/language logic ในหน้านี้ (ลิงก์ไปหน้าอื่นที่ไม่ได้ไล่ดูในรอบนี้)

### 2.2 ParManager / ParLibrary (Kaplas80)
- Repo: https://github.com/Kaplas80/ParManager — **VERIFIED** (README ผ่าน `gh api`)
- .NET library+CLI สำหรับอ่าน/เขียน Yakuza PAR archives รองรับ SLLZ compression (รวม SLLZ V2 ที่ใช้ใน Kiwami 2)
- คำสั่งหลัก: `list`, `extract`, `create`, `remove`, `add` — รองรับ drag&drop ตั้งแต่ v1.2.0
- ใช้ Yarhl (by Pleonex) เป็น base library — SRMM ใช้ ParLibrary ตัวนี้ในการ repack PAR (สำหรับ Old Engine)

### 2.3 reARMP (Ret-HZ, เดิมชื่อ CapitanRetraso)
- Repo: https://github.com/Ret-HZ/reARMP — **VERIFIED**
- **สถานะ: ประกาศเลิกพัฒนา (obsolete) แล้ว** — README มีคำเตือนชัดเจนว่า "will not be updated" ให้ไปใช้ **LibARMP** แทน (https://github.com/Ret-HZ/LibARMP)
- รองรับเกม Dragon Engine: Yakuza Kiwami 2, Yakuza 6, **Judgment**, Yakuza 7/Like a Dragon — ระบุชื่อ Judgment ตรงๆ ใน README ยืนยันว่า community เคยใช้ reARMP กับ Judgment มาก่อนจริง
- วิจัยเดิมของ format โดย SlowpokeVG (repo แยก: `SlowpokeVG/Dragon-Engine-armp-converter`, WIP)
- **นี่คือของเดิมที่โปรเจกต์เราใช้เป็นฐาน (`tools/reARMP_fixed.py` เป็น fork/patch ของตัวนี้)** — ควรพิจารณาย้ายไปดู LibARMP ในอนาคตถ้ามีเวลา แต่ LibARMP เองก็ยัง "not ready for general use" (README ระบุชัดว่า API จะเปลี่ยนแบบ breaking และ wiki "incomplete and obsolete" — **VERIFIED** จาก wiki Home.md)

### 2.4 อื่นๆ ที่เจอ
- **Counta/Yakuzazhfontgen** (https://github.com/Counta/Yakuzazhfontgen — VERIFIED, README ภาษาจีน): สคริปต์ Python 2 ตัวสำหรับ generate ฟอนต์จีน (ตัวเต็ม + ตัวย่อ) ให้ **"kiwami engine"** — workflow คือ unpack `font.par` ด้วย ParTool → ได้ไฟล์ **DDS texture** ของฟอนต์ → แก้/แทนที่ → repack เป็น DDS ด้วย DXT5 compression, single mipmap (ใช้ Microsoft DirectXTex/texconv) → หรือ pack เป็น mod zip ให้ SRMM ใช้ตรงๆ
  - **สำคัญ**: นี่คือ workflow ของฟอนต์ยุค "kiwami engine" (DDS texture atlas แบบ parallel-array/SDF) **ไม่ใช่ยุค Y6/Judgment "FONT!" flat format** ตาม CLAUDE.md ของโปรเจกต์เรา — ยืนยันภายนอกว่ามี **สองสถาปัตยกรรมฟอนต์จริงต่างกัน** ในตระกูลเกมนี้ (สอดคล้องกับที่ CLAUDE.md เตือนห้ามใช้ font_tool ของ K2R กับ Judgment) แต่ไม่มีข้อมูลสาธารณะที่พบเจอเกี่ยวกับ "FONT!" format ของ Y6/Judgment เลย (ดูข้อ 3)
- **Timo654/kuma**: Dragon Engine karaoke editor — ไม่เกี่ยวกับฟอนต์ข้อความ/subtitle โดยตรง (เป็น editor สำหรับ karaoke minigame maps) ไม่ตรง scope
- **Kaplas80/TF3.YakuzaPlugins** และ **Kaplas80/TranslationFramework2** — เจอในผลค้นหาว่ามี plugin อ่าน format Yakuza ทั่วไป และมี GitHub issue "#20 Font for Yakuza 0" — ไม่ได้เปิดอ่านลึกในรอบนี้ (นอก scope Judgment/LJ โดยตรง, เป็น TranslationFramework คนละเครื่องมือจาก ParManager) — ถ้าต้องการรายละเอียดฟอนต์เพิ่มเติมค่อยเปิดดู issue นี้ภายหลัง (**ไม่ verify ในรอบนี้**)

---

## 3. เอกสารชุมชน (community docs) และ format "FONT!"

- **ไม่พบเอกสารสาธารณะที่อธิบาย "FONT!" magic container format โดยตรง** (32-byte-per-glyph flat interleaved record ตามที่ CLAUDE.md อธิบาย) จากการค้นทั้ง WebSearch ทั่วไปและ GitHub code search (`gh search code "FONT!" language:python` ไม่เจอ hit ที่เกี่ยวข้องเลย — ผลลัพธ์ทั้งหมดเป็น false positive จาก comment ปกติในโปรเจกต์อื่น)
- ไม่พบ repo สาธารณะอื่นที่พูดถึง Yakuza 6 font format ("FONT!") หรือมีสคริปต์แบบ `y6_font_tool.py`/`bc4_codec.py` ที่ user มีอยู่แล้วใน `yakuza-6-thai` — **บ่งชี้ว่า research ของโปรเจกต์ Y6 (`docs/recon_font.md`) เป็นงาน reverse-engineer ต้นฉบับของทีมเราเอง ไม่ได้อ้างอิงจากที่อื่นที่ publish เป็น publicอยู่แล้ว** — ควรถือเป็นทรัพย์สินความรู้เฉพาะของทีม ไม่มี fallback ให้ cross-check จากภายนอกได้ในตอนนี้
- **RGG Modding Community Discord** (https://discord.com/invite/yakuzamodding) — มีอยู่จริงและเป็น hub หลักของ community นี้ (**VERIFIED ว่ามีเซิร์ฟเวอร์นี้อยู่จริง** จาก search) แต่เนื้อหา Discord เข้าถึงไม่ได้ผ่าน WebSearch/WebFetch (ต้อง join ด้วยบัญชี Discord จริง) — **นี่คือ gap สำคัญที่สุด**: ข้อมูล format ละเอียด (ARMP string control tags, font format เจาะลึก, "carrier" par logic) น่าจะอยู่ใน pinned messages/docs ของ Discord นี้เป็นหลัก แต่ tool การค้นในเซสชันนี้เข้าไม่ถึง
- **ShrineFox** (shrinefox.com, GitHub: ShrineFox) — ยืนยันว่าเป็นบุคคล/กลุ่มที่ทำงานด้าน Yakuza modding จริง (Vinesauce editor, มี GitHub org) — ไม่พบ index หรือ landing page ที่ list เครื่องมือ/เอกสาร font format ชัดเจนในรอบค้นนี้ (เว็บอาจถูก maintain 2020-2024 แล้วหยุด ตามที่ผลค้นบอก) — **CLAIMED เท่านั้น ยังไม่ verify เนื้อหาเทคนิคใดๆ**
- **PCGamingWiki** หน้า Judgment, Lost Judgment, "List of Traditional/Simplified Chinese fan translations" — **เข้าถึงไม่ได้เลยในรอบนี้** ทั้ง WebFetch ตรงและผ่าน r.jina.ai proxy (Cloudflare 403 ทุกครั้ง) แม้แต่ผ่าน web.archive.org ก็โดน 403 เช่นกัน — ต้องลองใหม่ภายหลังด้วยวิธีอื่น (เช่น เบราว์เซอร์จริงของผู้ใช้)

---

## 4. Text layout / word wrap / control tags / per-language font selection

- **ไม่พบเอกสารสาธารณะเจาะจงเรื่องนี้สำหรับ Judgment/Lost Judgment โดยตรง** — คำค้นเรื่อง ARMP control tags, ruby/furigana tags, "\n" line break format ไม่เจอ hit ที่เป็นเนื้อหาเทคนิคจริงเลย (เจอแต่ผลลัพธ์ทั่วไปเกี่ยวกับ ruby text ใน context อื่น เช่น Ren'Py, Anki)
- ข้อสังเกตทางอ้อมที่มีมูล: หน้า Fandom "Judgment: Apocalypse Survival Simulation Wikia" (เกมคนละเกม คนละบริษัท — Devolver Digital's zombie survival game ไม่ใช่ RGG's detective game) ที่ปรากฏซ้ำในผลค้นหา **ไม่เกี่ยวข้องกับเกมเป้าหมายของเรา แม้ชื่อจะพ้องกัน** — ต้องระวังอย่าใช้ข้อมูลจากวิกินี้โดยเข้าใจผิดว่าเป็นเกม RGG (มี snippet ที่ดูเหมือนเกี่ยวกับ Chinese word-wrap แต่บริบทจริงคือเกมคนละเกม จึงไม่ได้ใช้ในรายงานนี้)
- LibARMP wiki (https://github.com/Ret-HZ/LibARMP/wiki) — **VERIFIED ว่าว่างเปล่า**: หน้า Home ระบุตรงๆ ว่า "The contents of the wiki are currently incomplete and obsolete. They will be properly updated once the project is ready for general use (version 1.0)" — ไม่มีข้อมูล string/text format ให้อ้างอิงตอนนี้
- **สรุป**: เรื่อง word wrap / control tags / per-language font selection ของ Judgment/LJ **ไม่มีแหล่งสาธารณะให้ verify ได้เลยในการค้นรอบนี้** ทีมต้อง reverse-engineer จากไฟล์เกมจริงเหมือนที่ทำกับ Y6 มาก่อน (ตามแผนที่ CLAUDE.md วางไว้อยู่แล้ว)

---

## 5. Gap ที่เหลือ / ควรตามต่อ

1. เข้าไม่ถึง PCGamingWiki เลยทั้งสามช่องทาง (WebFetch ตรง / r.jina.ai / web.archive.org) — ควรลองใหม่ด้วยเบราว์เซอร์จริงหรือ user ช่วยเปิดเอง
2. RGG Modding Discord คือแหล่งข้อมูลที่น่าจะมีรายละเอียดมากที่สุดแต่เข้าไม่ถึงจาก session นี้ — แนะนำให้ user join แล้ว export/สรุปมาให้ ถ้าต้องการข้อมูลเชิงลึกกว่านี้
3. ยังไม่ได้ verify ว่าม็อด MOD2SUB (ไทย) เพิ่ม glyph ไทยลงฟอนต์เกมจริงหรือไม่ — ต้องโหลดไฟล์ม็อดมาแกะดู (เป็น mod file ไม่ใช่ game file จึงไม่ผิดกติกาเหล็ก แต่ผู้ใช้ระบุ "ห้ามใช้เป็น TM" ไม่ได้ห้ามแกะโครงสร้างไฟล์ — ควรถามผู้ใช้ก่อนถ้าจะดาวน์โหลดจริง เพราะ task นี้ระบุห้าม download/install mods)
4. ไม่ได้เปิดอ่าน GitHub issue "Kaplas80/TranslationFramework2#20 (Font for Yakuza 0)" และ TF3.YakuzaPlugins — อาจมีรายละเอียด font format เพิ่มเติมที่เกี่ยวข้องทางอ้อม
5. ไม่พบม็อดแปล Spanish/Portuguese สำหรับเกมเป้าหมายเลยในรอบค้นนี้ — อาจไม่มีอยู่จริง หรือค้นไม่เจอ
