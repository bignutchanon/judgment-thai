# ตารางเพศผู้พูดทั้งเกม — Judgment

> สร้างด้วย `python scripts/make_dialogue_gender.py --write` — ห้ามแก้ด้วยมือ ·
> ข้อมูลเต็มอยู่ `extracted/facts/dialogue_gender.json` (ข้อความ EN → เพศ + แหล่งหลักฐาน)

| ตัวชี้วัด | ค่า |
|---|---|
| ข้อความ EN ที่รู้เพศผู้พูด (ทุกแหล่ง) | 41,342 |
| ในจำนวนนี้อยู่ใน master_th | 41,247 |
| master_th ที่แปลระบุเพศไว้ (ครับ/ค่ะ/ผม/ฉัน) | 14,526 |
| บรรทัดที่คำแปลขัดกับหลักฐาน (ต้องแก้) | **23** |
| ฉากคัตซีนที่ทีมระบุผู้พูดแล้ว | 102 / 102 (2,374 แถว) |

## แยกตามเพศ (ข้อความในเกมที่รู้ผู้พูด)

| เพศ | จำนวน |
|---|---|
| ชาย | 34,985 |
| หญิง | 5,635 |
| ใช้ร่วมสองเพศ (ต้องกลาง) | 263 |
| บรรยาย/ป้าย | 132 |
| ไม่ยืนยัน | 232 |

## แยกตามแหล่งหลักฐาน

| แหล่ง | ข้อความ |
|---|---|
| talk | 16,350 |
| cue | 15,283 |
| cinema | 4,174 |
| pov | 4,121 |
| speech | 3,489 |
| chat | 1,516 |
| popup | 369 |
| mahjong | 257 |

## บรรทัดที่แปลระบุเพศไว้ แยกตาม bin

| bin | ตรง | ขัดกัน | ไม่มีหลักฐาน |
|---|---|---|---|
| talk.bin | 7317 | 9 | 122 |
| sound_auth.bin | 4514 | 8 | 25 |
| auth.bin | 992 | 0 | 0 |
| pause_message.bin | 838 | 6 | 0 |
| mission_mission_kind.bin | 286 | 0 | 0 |
| scene_scenario_explanation.bin | 105 | 0 | 0 |
| talk_select_select.bin | 90 | 0 | 0 |
| character_npc_popup_text.bin | 67 | 0 | 0 |
| item.bin | 38 | 0 | 0 |
| pause_crowdfunding.bin | 28 | 0 | 0 |
| side_case_side_case_request.bin | 0 | 0 | 21 |
| sound_auth_subtitles_speech_list_sub_a14.bin | 0 | 0 | 13 |
| minigame_poker_com_high_5.bin | 0 | 0 | 8 |
| evidence_item_to_update.bin | 6 | 0 | 0 |
| minigame_poker_com_high_4.bin | 0 | 0 | 5 |
| sound_auth_subtitles_speech_list_sub_a13.bin | 0 | 0 | 5 |
| minigame_poker_com_high_6.bin | 0 | 0 | 4 |
| talk_question_text.bin | 4 | 0 | 0 |
| minigame_cabaret_island_coordinate_accessory_hair.bin | 0 | 0 | 3 |
| character_friend_list.bin | 0 | 0 | 3 |
| minigame_cabaret_island_coordinate_accessory_category.bin | 0 | 0 | 2 |
| minigame_cabaret_island_coordinate_hair_style.bin | 0 | 0 | 2 |
| minigame_cabaret_island_coordinate_makeup_category.bin | 0 | 0 | 2 |
| title_movie.bin | 0 | 0 | 1 |
| talk_popup_popup.bin | 0 | 0 | 1 |
| verification_survey_3d.bin | 0 | 0 | 1 |

## บรรทัดที่ขัดกัน (23) — แก้ด้วย `python scripts/fix_dialogue_gender.py --write`

| bin | เพศจริง | EN | TH ปัจจุบัน |
|---|---|---|---|
| sound_auth.bin | mixed | Um... Yagami-san. | เอ่อ...ยากามิซังคะ |
| sound_auth.bin | male | You got all you need from here, yeah? | ได้ข้อมูลที่ต้องการจากตรงนี้ ครบแล้วใช่ไหมคะ? |
| sound_auth.bin | male | Shintani-sensei, can you / lay on the bed for me? | อาจารย์ชินทานิ ช่วยไป / นอนบนเตียงให้หน่อยได้ไหมคะ? |
| sound_auth.bin | male | The service entrance, right? | ทางเข้าฝ่ายบริการใช่ไหมคะ? |
| sound_auth.bin | male | Saori-san? You good? | คุณซาโอริซัง? ไม่เป็นไรใช่ไหมคะ? |
| sound_auth.bin | male | By Hashiki's estimation, looking at the facts, / it was all too convenient to be | ตามที่ฮาชิกิคาดคะเน จากข้อเท็จจริงที่มี / มันดูสะดวกเกินไปจนไม่น่าจะ เป็นเรื่องบ |
| sound_auth.bin | male | Yagami-san, there he is. / It's Shono. | ยากามิซัง เขาอยู่นั่นไงคะ / คือโชโนะ |
| sound_auth.bin | male | There he is, Yagami-san. / It's Shono. | เขาอยู่นั่นไงคะ ยากามิซัง / คือโชโนะ |
| pause_message.bin | mixed | The name's Takayuki Yagami. Could you come to the Yagami Detective Agency in Nak | ผมชื่อทาคายูกิ ยากามิ มาที่สำนักงานนักสืบยากามิ ในตรอกนากามิจิได้ไหมครับ |
| pause_message.bin | mixed | I'll go as soon as I get the chance. | มีโอกาสเมื่อไหร่ผมจะรีบไปเลย |
| pause_message.bin | mixed | Make me some more next time. | ครั้งหน้าทำให้ผมกินอีกนะ |
| pause_message.bin | mixed | Are you saying she trusts me more than she trusts you? | หมายความว่าเธอไว้ใจผมมากกว่า ไว้ใจนายเหรอ? |
| pause_message.bin | mixed | Maybe I can cheer you up somehow? | ให้ผมช่วยทำให้อารมณ์ดีขึ้น สักหน่อยไหม? |
| pause_message.bin | mixed | Are you asking me out on a date? | นี่คุณกำลังชวนผมไปเดตอยู่เหรอ? |
| talk.bin | female | Of course, sir! Just a moment. | ได้เลยครับ! รอสักครู่นะครับ |
| talk.bin | female | All done! Thanks for your patience. | เสร็จเรียบร้อยครับ! ขอบคุณที่รอนะครับ |
| talk.bin | female | Okay! Let us know if you need any help. | ได้ครับ! ถ้าต้องการความช่วยเหลืออะไรก็ บอกได้เลยนะครับ |
| talk.bin | male | Lovely, you say? Oh, ha ha... You think so? | สวยงามเหรอคะ? โอ้ ฮ่าฮ่า... คิดงั้นจริง ๆ เหรอ? |
| talk.bin | mixed | So you figured it out, huh? Whatever. As long as I have Asami-chan. | อ้อ นายรู้แล้วสินะ ช่างเถอะ ขอแค่มีอาซามิจังอยู่กับผมก็พอ |
| talk.bin | mixed | Hmph. You'll have to excuse my abruptness, but I need to speak with you for a mo | หึ ต้องขออภัยที่มาแบบไม่ทันตั้งตัวนะ แต่ผมมีเรื่องอยากคุยกับคุณสักครู่ |
| talk.bin | mixed | No, I didn't feel that was necessary. I noticed you from outside, so I thought I | เปล่า ผมว่าไม่จำเป็นต้องนัดหรอก เห็นคุณจากข้างนอกก็เลยคิดว่าจะ แวะเข้ามาคุยด้วยส |
| talk.bin | mixed | Then I'll make this as quick and painless as possible... | งั้นผมจะทำให้เรื่องนี้จบไวและ เจ็บน้อยที่สุด... |
| talk.bin | male | Instinct!? | สัญชาตญาณเหรอคะ!? |
