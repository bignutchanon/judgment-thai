# Worklist Report — Pirate Rework (make_worklist.py)

- unique strings ทั้งเกม: **53,591**
- อยู่ใน master_th แล้ว (ผ่าน QC): 3,324 (เก็บเกี่ยวจาก batch เดิมรอบนี้ 0)
- เหลือจัดเข้า batch: **50,267** (normal 32,474 / talk-only 17,793)
- batch: **133** normal + **72** TALK (≤250 strings/batch)
- มีร่างอ้างอิง v1.2 (`ref_tm`): 5,568 strings — **ไม่ใช่คำตอบ** ผู้แปลต้องพิจารณาใหม่ทุกตัว
- ปริมาณงาน: ~487,922 คำ EN (normal 298,260 / talk 189,662)

| priority | ความหมาย | strings |
|---:|---|---:|
| 1 | caption (ซับสั้นบนจอ) | 91 |
| 2 | auth/sound_auth (บทคัตซีน) | 19,382 |
| 3 | msg/pause_message/message dialog | 1,801 |
| 4 | item/ui/title/help/manual/map/talk_talker | 5,804 |
| 5 | minigame/drone | 1,907 |
| 6 | rest | 3,489 |
| 7 | talk-only (บทสนทนาเดินเมือง) | 17,793 |

## bin สำคัญ

| bin | strings |
|---|---:|
| caption.bin | 91 |
| auth.bin | 4,174 |
| sound_auth.bin | 15,404 |
| message_dialog.bin | 23 |
| msg.bin | 301 |
| item.bin | 1,797 |
| ui_text.bin | 556 |
| title_root.bin | 70 |
| talk.bin | 18,391 |

สร้างโดย `scripts/make_worklist.py` — รันซ้ำได้ (harvest ก่อน re-chunk)
