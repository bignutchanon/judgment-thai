# QC Review — batch_105

ผลตรวจ: อ่านทั้ง 250 คู่ (มิชชันเควสไซด์เคส "Revenge of the Keihin Gang" · เควสอื่น ๆ ระดับปกติ · สกิลทรี Boost/EX/Wall Jump/Leapfrog ฯลฯ)
`merge_qc.py --dry-run --only 105` → **ผ่าน 250 · ตก 0**

## แก้แล้ว 3 จุด (ทั้งหมดเป็นข้อ 1 แปลผิดความหมาย/ข้อ 3 คำล็อกไม่ตรง glossary)

1. **"Find the Dealer"** — "If the intel's right, **the dealer** should show up anytime..."
   เดิม: "**คนขายยา**น่าจะโผล่มาได้ทุกเมื่อ" → แก้เป็น "**คนขายปืน**น่าจะโผล่มาได้ทุกเมื่อ"
   เหตุผล: เควสนี้อยู่ใน case "Revenge of the Keihin Gang" ต่อเนื่องกับ "Search for the Gun Smuggler's Base"
   และ "Gather Intel at City Hangouts" ที่พูดถึง "pistol smuggling" ตรง ๆ (`missions.json` idx 1752-1753)
   → "dealer" ในสายนี้คือพ่อค้าปืน ไม่ใช่พ่อค้ายา แปลเป็น "คนขายยา" ผิดความหมายทั้งประโยค (สร้างคดีลักลอบขนยาเสพติดขึ้นมาเองทั้งที่ไม่มีในเกม)

2. **"Search for the Gun Smuggler's Base"** — "**The dealer** disappeared from the Children's Park..."
   เดิม: "**คนขายยา**หายตัวไปจากสวนเด็ก" → แก้เป็น "**คนขายปืน**หายตัวไปจากสวนเด็ก" (เหตุผลเดียวกับข้อ 1 — คำเดียวกัน ต้องแก้คู่กัน)

3. **"Pay 100,000 and Modify the Drone"** — "...install a shooting mechanism on **the Pigeon**..."
   เดิม: "ติดตั้งกลไกยิงบน**พิเจียน**" → แก้เป็น "ติดตั้งกลไกยิงบน**นกพิราบ**"
   เหตุผล: `glossary.md` §📇 ล็อกไว้ชัดเจนว่า "Pigeon (โค้ดเนมโดรน) → นกพิราบ" และ `master_th.json` ใช้ "นกพิราบ" สม่ำเสมอทุกจุดที่เคยแปลมาก่อน (เช่น "Sounds like a job for the Pigeon." → "...งานของนกพิราบเลยนะ") — ทับศัพท์ "พิเจียน" เป็นการหลุดคำล็อก ไม่ใช่แค่สไตล์

## ไม่แก้ แต่ตั้งข้อสังเกตให้ lead ตัดสิน

- **"Rei" (เควส "Rescue Rei from the Boss" / "Rei is being sexually harassed by Iseya!")**
  batch นี้ใช้ **"เรย์"** ตลอด — ตรวจสอบแล้วว่าเป็นตัวละครเดียวกับ "Rei Miyamoto" ที่ถูก Taro Iseya (ทาโร อิเซยะ) คุกคามทางเพศจริง (ยืนยันจาก `evidence.json`/`master_th.json` — "Taro Iseya"/"Rei Miyamoto" อยู่ติดกัน)
  **แต่ `master_th.json` เองสะกดไม่ตรงกันสองที่**: บรรทัด "Rei Miyamoto" → "**เรย์** มิยาโมโตะ" (ชื่อเต็ม) กับอีกบรรทัดหนึ่ง "...คุกคามทางเพศ**เรย์**ได้อย่างลอยนวล" (บทของ Iseya) ใช้ "**เรย์**" — สองรูปสะกดปนกันอยู่แล้วใน master ก่อน batch นี้
  ส่วน `glossary.md` §7 เขียนไว้ว่า "Rei Miyamoto → **เรย์** มิยาโมโตะ" (ตามกฎ "-ei ท้ายพยางค์ = เ-ย์" ที่ยกตัวอย่าง "เรย์" ไว้เอง) ซึ่งขัดกับ master ที่ ship ไปแล้วแบบ "เรย์"
  → batch_105 ใช้ "เรย์" ตรงกับ 1 ใน 2 รูปที่มีอยู่แล้วใน master (ชื่อเต็มตัวละคร) จึงไม่ถือว่า "ผิด" ตามกฎ "ห้ามดัดคำแปลเพื่อหนี QC" + กฎเทียบ master — **ไม่ได้แก้** แต่รายงานไว้ให้ lead ตัดสินว่าจะ freeze เป็น "เรย์" หรือ "เรย์" ตัวเดียว แล้วค่อยไล่กวาดทั้งสามจุด (master 2 จุด + glossary.md §7 1 จุด)

## คำที่ควรพิจารณาเพิ่มเข้า glossary

- **"the dealer" ในสาย "Revenge of the Keihin Gang" = คนขายปืน** (ไม่ใช่คำทั่วไปที่แปลว่า "คนขายยา" ได้ตามค่าเริ่มต้น) — ถ้ามี batch อื่นพูดถึงสายนี้ต่อ (Keihin Gang / gun smuggling) ควรเพิ่มลง glossary กันหลุดซ้ำ
- ยืนยันว่า **Pigeon → นกพิราบ** ควรเพิ่มเข้า §📇 ตารางเทอมอ่านโดยเครื่องด้วย (ตอนนี้อยู่แค่ในเนื้อ §11 ข้อความ ไม่มีในตารางท้ายไฟล์ที่เครื่องอ่าน) — เผื่อ batch อื่นหลุดซ้ำแบบเดียวกัน

## จุดที่ตรวจแล้วผ่าน (ไม่มีปัญหา)

- honorific ทั้งหมดตรง EN (-san/-chan/-kun → ซัง/จัง/คุง) ครบทุกจุด (Sana-chan, Ohata-san, Ayumu-kun, Karin-chan, Kim-san, Tokunaga-san, Terasawa-san, Okubo-kun, Makihara-kun, Saori-san)
- ชื่อเฉพาะที่ล็อกแล้วทั้งหมดตรง glossary: Kanrai, Kumakura, Sugiura, Minister Kazami, Keihin Gang, Amane (+ "ลางร้ายรูป X" ทั้ง 3 ตัวแปร), Koi Bride, Smile Burger, Poppo, Club Stardust (Stardust Rooftop), Kim, Charles, Ono Michio, Zhuang Shi, Mantai, Café Mijore, Batting Center (ศูนย์ฝึกตี), Ushimata (ไม่มีคำล็อกเดิม — ทับศัพท์ตามหลักมาตรฐาน), East Taihei Boulevard (ตาม Taihei Boulevard ที่ล็อกแล้ว), Yusuke
- Mad Bomber variants ("serial bomber" ×2) แปลรวมเป็น "มือระเบิดบ้าคลั่ง" ตามกฎล็อกรูปเดียวถูกต้อง
- สรรพนามยากามิ "ผม" ทุกจุด (เป็นมอนอล็อกทั้งหมด ไม่มีบทพูดที่ต้องยืนยันผู้พูดจาก speaker_by_subtable เพราะ source_bins เป็น mission/skill/side_case ไม่ใช่ dialogue table) — ไม่พบ ครับ/ค่ะ/คะ หลุดจุดใด, ไม่พบ กู/มึง/แก
- ref_tm ทั้ง 13 คู่ตรงกับคำแปลใน done ทุกจุด (Boost Health/Attack/Combo Speed series, Dash Attack, Rising Tornado, Re-Guard, Triple Finisher, Please Find My Son ฯลฯ)
- แท็ก `<Sign:N>` ครบจำนวนทุกบรรทัดในหมวดสกิล ไม่มีตกหล่น
- ไม่พบสัญลักษณ์ ❤ ♥ ♪ ★, ไม่พบช่องว่างแทรกกลางคำ, ไม่พบ debug string ภาษาจีน/ญี่ปุ่น
