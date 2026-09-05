# คีย์ที่ใช้ซ้ำหลาย bin — ห้ามแปลให้เข้าบริบทเดียว

สร้างด้วย `python scripts/make_multibin_index.py --write` (ที่มา `extracted/unique_strings.json`) · เกณฑ์: คีย์ยาวไม่เกิน 40 ตัวอักษร และปรากฏใน 2 bin ขึ้นไป

**กติกา**: คำแปลของคีย์พวกนี้ต้องใช้ได้กับ *ทุก* บริบทที่มันโผล่ ถ้าเลี่ยงไม่ได้ให้เลือกคำกลาง ๆ แล้วรายงาน lead — ห้ามแปลให้เข้ากับ bin เดียว (ไฟล์คำแปลเป็น map แบน EN→TH ตัวเดียวทั้งเกม)

รวม 1650 คีย์

| คีย์ EN | จำนวน bin | bin ที่ใช้ |
|---|---|---|
| `Amane` | 11 | character_friend_list.bin · complete_checklist.bin · item.bin · minigame_darts_rival_info_judge.bin · minigame_poker_com_special_2.bin · minigame_shogi_menu.bin · … |
| `Takayuki Yagami` | 11 | caption.bin · drone_enemy_division1.bin · drone_enemy_division2.bin · drone_enemy_division3.bin · drone_enemy_division4.bin · drone_enemy_division5.bin · … |
| `Mari` | 9 | character_friend_list.bin · complete_checklist.bin · evidence_item_to_update.bin · item.bin · minigame_stalking_mission.bin · pause_message.bin · … |
| `not-yet-localized` | 9 | asset_asset_name.bin · minigame_cabaret_island_ability.bin · minigame_cabaret_island_condition.bin · minigame_cabaret_island_coordinate_hair_color.bin · minigame_cabaret_island_evaluation.bin · minigame_cabaret_island_looks.bin · … |
| `Tsukino Saotome` | 9 | character_friend_list.bin · complete_checklist.bin · evidence_item_to_update.bin · item.bin · minigame_darts_rival_info_judge.bin · minigame_poker_com_special_3.bin · … |
| `On` | 8 | minigame_cabaret_island_coordinate_makeup_cheek.bin · minigame_cabaret_island_coordinate_makeup_eyeshadow.bin · minigame_cabaret_island_coordinate_makeup_lip.bin · minigame_oichokabu_string_oichokabu.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · … |
| `Yosuke Saotome` | 8 | character_friend_list.bin · complete_checklist.bin · evidence_item_to_update.bin · item.bin · pause_message.bin · pause_message_person.bin · … |
| `Nanami Matsuoka` | 7 | character_friend_list.bin · complete_checklist.bin · item.bin · minigame_darts_rival_info_judge.bin · pause_message.bin · pause_message_person.bin · … |
| `No` | 7 | character_npc_soldier_name_group.bin · minigame_hanafuda_string_hanafuda.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · msg.bin · talk_select_select.bin · … |
| `Normal` | 7 | map_icon.bin · minigame_cabaret_island_coordinate_dress.bin · msg.bin · option.bin · save_data_detail.bin · talk_select_select.bin · … |
| `Quit` | 7 | controller_guide.bin · minigame_hanafuda_string_hanafuda.bin · minigame_mahjong_string_common.bin · minigame_oichokabu_string_oichokabu.bin · msg.bin · talk_select_select.bin · … |
| `View Rules` | 7 | controller_guide.bin · minigame_hanafuda_string_hanafuda.bin · minigame_hanafuda_string_mainmenu.bin · minigame_mahjong_string_common.bin · minigame_oichokabu_string_oichokabu.bin · talk_select_select.bin · … |
| `Yes` | 7 | minigame_hanafuda_string_hanafuda.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · msg.bin · pause_message.bin · talk_select_select.bin · … |
| `Batting Center` | 6 | complete_group.bin · controller_guide.bin · input_game_state.bin · manual.bin · pause_message.bin · talk_select_select.bin |
| `Beginner` | 6 | minigame_cabaret_cabaret.bin · minigame_hanafuda_string_hanafuda.bin · minigame_oichokabu_string_oichokabu.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · talk_select_select.bin |
| `Captain Cop` | 6 | character_npc_soldier_name_group.bin · complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Drone Lab` | 6 | complete_group.bin · help.bin · manual.bin · map_place.bin · shop.bin · ui_text.bin |
| `Judge Creep 'n Peep` | 6 | caption.bin · character_npc_soldier_name_group.bin · drone_enemy_etc.bin · evidence_item_to_update.bin · item.bin · talk_talker.bin |
| `Sana Mihama` | 6 | character_friend_list.bin · item.bin · minigame_darts_rival_info_judge.bin · pause_message.bin · pause_message_person.bin · talk_category_title.bin |
| `View Controls` | 6 | controller_guide.bin · input_action.bin · msg.bin · pause_others.bin · pause_trial_root.bin · ui_text.bin |
| `${value} pts.` | 5 | minigame_mahjong_string_common.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · msg.bin · player_point.bin |
| `A Final Request` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `All right.` | 5 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `Amidst a Dream` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Ass Catchem` | 5 | caption.bin · character_npc_soldier_name_group.bin · item.bin · minigame_chase_mission.bin · talk_talker.bin |
| `Battle` | 5 | help_category.bin · input_game_state.bin · map_icon.bin · player_skill_category.bin · ui_text.bin |
| `Blackjack` | 5 | access_type.bin · asset_asset_name_judge.bin · controller_guide.bin · input_game_state.bin · manual.bin |
| `Burger Fugitive` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Cancel` | 5 | controller_guide.bin · input_action.bin · msg.bin · talk_select_select.bin · ui_text.bin |
| `Close` | 5 | minigame_hanafuda_string_hanafuda.bin · minigame_hanafuda_string_mainmenu.bin · minigame_picking_job_picking_job.bin · msg.bin · ui_text.bin |
| `Dangerous Hide-and-seek` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Darts` | 5 | controller_guide.bin · input_game_state.bin · manual.bin · pause_message.bin · talk_select_select.bin |
| `Drone` | 5 | help.bin · manual.bin · map_icon.bin · ui_text.bin · verification_survey_3d.bin |
| `Drone Race` | 5 | controller_guide.bin · input_game_state.bin · map_place.bin · pause_message.bin · talk_select_select.bin |
| `Easy` | 5 | access_type.bin · option.bin · save_data_detail.bin · talk_select_select.bin · ui_text.bin |
| `Entrapment` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `EX Boost` | 5 | controller_guide.bin · input_action.bin · manual.bin · pause_tutorial.bin · tips.bin |
| `Gone in 20 Minutes` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Gone with the Breeze` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Gone with the Gale` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Gone with the Gust` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Hands` | 5 | controller_guide.bin · input_action.bin · minigame_hanafuda_string_hanafuda.bin · minigame_mahjong_string_common.bin · ui_text.bin |
| `Help` | 5 | controller_guide.bin · input_action.bin · msg.bin · pause_tutorial.bin · ui_text.bin |
| `Hideaki Deguchi` | 5 | character_friend_list.bin · complete_checklist.bin · evidence_item_to_update.bin · item.bin · talk_category_title.bin |
| `Honey Trap` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Huh?` | 5 | auth.bin · minigame_mahjong_string_npc.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Interview with a Detective` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Love and Madness` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Mafuyu Fujii` | 5 | caption.bin · evidence_item_to_update.bin · item.bin · pause_message.bin · pause_message_person.bin |
| `Makoto Tsukumo` | 5 | character_friend_list.bin · complete_checklist.bin · pause_message.bin · pause_message_person.bin · talk_category_title.bin |
| `Morale and Morals` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Of course.` | 5 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `Off` | 5 | minigame_oichokabu_string_oichokabu.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · option.bin · ui_text.bin |
| `Partners` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Perilous Hide-and-seek` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Photo Missions` | 5 | controller_guide.bin · help.bin · input_game_state.bin · manual.bin · minigame_photo_shooting_mission_mission_data.bin |
| `Queen of Hearts` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Reckless Aspirations` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Return of the Mad Bomber` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Revenge of the Keihin Gang` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Rie Tomioka` | 5 | character_friend_list.bin · complete_checklist.bin · pause_message.bin · pause_message_person.bin · talk_category_title.bin |
| `Ryan Acosta` | 5 | caption.bin · character_friend_list.bin · character_npc_soldier_name_group.bin · complete_checklist.bin · talk_category_title.bin |
| `Sakura Amamiya` | 5 | character_friend_list.bin · complete_checklist.bin · pause_message.bin · pause_message_person.bin · talk_category_title.bin |
| `Sashimi of the Fallen` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Secrets of Cats` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Smart Watching` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Sure.` | 5 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `The Black and White Calamity` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Black Calamity` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Darkest Place` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Devil Wife` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Fire Calamity` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Mad Bomber Strikes Again` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Mystery Writer's Gambit` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Mystery Writer's Masterstroke` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Mystery Writer's Stratagem` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Ono Michio Bandit` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Pervert King` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Tiger Jacket` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Treacherous Hide-and-seek` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Under the Table Politics` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Underneath the Mask` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Voluptuous Woman` | 5 | character_friend_list.bin · complete_checklist.bin · minigame_poker_com_special_1.bin · talk_category_title.bin · talk_talker.bin |
| `Way of the Detective` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Worst Birthday Ever` | 5 | complete_checklist.bin · item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Yagami Detective Agency` | 5 | help.bin · manual.bin · map_icon.bin · map_place.bin · ui_text.bin |
| `Yeah.` | 5 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `Yes.` | 5 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `${value}` | 4 | complete.bin · pause_complete_profile.bin · player_point.bin · reward_judge_clear_achievement.bin |
| `Active Search Mode` | 4 | help.bin · input_game_state.bin · manual.bin · verification_verification.bin |
| `Back` | 4 | msg.bin · option.bin · talk_select_select.bin · ui_text.bin |
| `Balanced` | 4 | minigame_cabaret_island_coordinate_makeup_eyebrows.bin · minigame_shogi_menu.bin · minigame_shogi_shogi.bin · option.bin |
| `Bantam Owner` | 4 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin · talk_talker.bin |
| `Bar Tender` | 4 | help.bin · manual.bin · map_place.bin · ui_text.bin |
| `Crow` | 4 | caption.bin · character_npc_soldier_name_group.bin · item.bin · talk_talker.bin |
| `Deguchi` | 4 | character_npc_soldier_name_group.bin · minigame_stalking_mission.bin · talk_talker.bin · verification_survey_3d.bin |
| `Difficulty` | 4 | minigame_hanafuda_string_hanafuda.bin · option.bin · pause_complete_profile.bin · ui_text.bin |
| `Dragon's Palace` | 4 | complete_group.bin · help.bin · manual.bin · map_place.bin |
| `Drone Search Mode` | 4 | help.bin · input_game_state.bin · manual.bin · verification_verification.bin |
| `Earth Angel` | 4 | complete_group.bin · map_place.bin · shop.bin · talk_select_select.bin |
| `EX Actions` | 4 | help_category.bin · manual.bin · pause_tutorial.bin · tips.bin |
| `Examine` | 4 | access_type.bin · controller_guide.bin · input_action.bin · ui_text.bin |
| `Genda Law Office` | 4 | help.bin · manual.bin · map_place.bin · ui_text.bin |
| `Hard` | 4 | option.bin · save_data_detail.bin · talk_select_select.bin · ui_text.bin |
| `Hey.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Hiroto Nasugawa` | 4 | character_friend_list.bin · complete_checklist.bin · pause_message_person.bin · talk_category_title.bin |
| `Hiyama` | 4 | character_npc_soldier_name_group.bin · item.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Hm?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `I see.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `I understand.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Ishimatsu` | 4 | evidence_item_to_update.bin · item.bin · minigame_stalking_mission.bin · verification_survey_3d.bin |
| `Justice is Sweet` | 4 | complete_checklist.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Kaito` | 4 | character_npc_soldier_name_group.bin · talk_select_select.bin · talk_talker.bin · verification_survey_3d.bin |
| `Kanrai` | 4 | complete_group.bin · map_place.bin · shop.bin · talk_select_select.bin |
| `Kenji Tanago` | 4 | caption.bin · character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kim` | 4 | character_npc_soldier_name_group.bin · pause_message.bin · pause_message_person.bin · talk_talker.bin |
| `Kyushu No. 1 Star Owner` | 4 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin · talk_talker.bin |
| `L'Amant` | 4 | help.bin · manual.bin · map_place.bin · shop.bin |
| `Lullaby Mahjong` | 4 | complete_group.bin · help.bin · manual.bin · map_place.bin |
| `Masaharu Kaito` | 4 | caption.bin · item.bin · pause_message.bin · pause_message_person.bin |
| `Meguro` | 4 | character_npc_soldier_name_group.bin · item.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Modern Mahjong` | 4 | complete_group.bin · help.bin · manual.bin · map_place.bin |
| `Noboru Hiranuma` | 4 | character_friend_list.bin · complete_checklist.bin · item.bin · talk_category_title.bin |
| `None` | 4 | input_action.bin · minigame_vf5_key_set.bin · msg.bin · ui_text.bin |
| `Nope.` | 4 | pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `Oh yeah?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Okay!` | 4 | auth.bin · pause_message.bin · talk.bin · talk_select_select.bin |
| `Onodera's Wares` | 4 | help.bin · manual.bin · map_place.bin · shop.bin |
| `Outdoor Shogi` | 4 | complete_group.bin · help.bin · manual.bin · map_place.bin |
| `Panty Professor` | 4 | caption.bin · character_npc_soldier_name_group.bin · item.bin · talk_talker.bin |
| `Paradise VR` | 4 | complete_group.bin · help.bin · manual.bin · map_place.bin |
| `Poker` | 4 | access_type.bin · controller_guide.bin · input_game_state.bin · manual.bin |
| `Raise Camera` | 4 | access_type.bin · controller_guide.bin · input_action.bin · ui_text.bin |
| `Right...` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Ryan` | 4 | character_npc_soldier_name_group.bin · minigame_darts_rival_info_judge.bin · talk_select_select.bin · talk_talker.bin |
| `Ryo Suzaki` | 4 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin · talk_select_select.bin |
| `Shellac` | 4 | complete_group.bin · map_place.bin · shop.bin · talk_select_select.bin |
| `Shit!` | 4 | auth.bin · minigame_mahjong_string_npc.bin · sound_auth.bin · talk.bin |
| `Shogi` | 4 | controller_guide.bin · input_game_state.bin · manual.bin · talk_select_select.bin |
| `Side Cases` | 4 | help.bin · item.bin · manual.bin · map_icon.bin |
| `Sorry.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Sprint` | 4 | controller_guide.bin · input_action.bin · pause_tutorial.bin · ui_text.bin |
| `Stand` | 4 | access_type.bin · minigame_oichokabu_string_oichokabu.bin · msg.bin · ui_text.bin |
| `Standard` | 4 | minigame_cabaret_island_coordinate_makeup_eyebrows.bin · minigame_cabaret_island_coordinate_makeup_eyelashes.bin · minigame_cabaret_island_coordinate_makeup_eyeline.bin · option.bin |
| `Start Game` | 4 | minigame_hanafuda_string_hanafuda.bin · minigame_hanafuda_string_mainmenu.bin · minigame_mahjong_string_mainmenu.bin · minigame_oichokabu_string_oichokabu.bin |
| `Sure thing.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Suspicious Man` | 4 | caption.bin · minigame_stalking_mission.bin · talk_talker.bin · verification_survey_3d.bin |
| `Tachibana Mahjong` | 4 | complete_group.bin · help.bin · manual.bin · map_place.bin |
| `Tailing Search Mode` | 4 | controller_guide.bin · help.bin · manual.bin · verification_verification.bin |
| `Takumi Katagiri` | 4 | character_friend_list.bin · complete_checklist.bin · item.bin · talk_category_title.bin |
| `Tashiro-kun` | 4 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin · talk_select_select.bin |
| `Tatsuro` | 4 | item.bin · pause_message.bin · pause_message_person.bin · talk_talker.bin |
| `Taxi` | 4 | help.bin · manual.bin · map_icon.bin · ui_text.bin |
| `test` | 4 | manual.bin · minigame_chase_mission.bin · minigame_stalking_mission.bin · talk_select_select.bin |
| `Thank you.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Thanks.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `That's right.` | 4 | auth.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `The Ghost Tenant` | 4 | complete_checklist.bin · item.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Missing Diamond` | 4 | item.bin · mission_mission_kind.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `The Socialite's Secret` | 4 | complete_checklist.bin · item.bin · scene_scenario_explanation.bin · talk_category_title.bin |
| `Threat Level` | 4 | help.bin · manual.bin · pause_tutorial.bin · tips.bin |
| `Toru Higashi` | 4 | caption.bin · evidence_item_to_update.bin · item.bin · minigame_stalking_mission.bin |
| `UFO Catcher` | 4 | complete.bin · controller_guide.bin · input_game_state.bin · manual.bin |
| `Wakahara` | 4 | character_npc_soldier_name_group.bin · item.bin · minigame_chase_mission.bin · talk_talker.bin |
| `Well...` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `What do you mean?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `What!?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `What's up?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Why?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Yeah, sure.` | 4 | pause_message.bin · sound_auth.bin · talk.bin · talk_select_select.bin |
| `Yoshida` | 4 | character_friend_list.bin · character_npc_soldier_name_group.bin · complete_checklist.bin · talk_category_title.bin |
| `You sure?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `You think so?` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `You're right.` | 4 | auth.bin · pause_message.bin · sound_auth.bin · talk.bin |
| `Yukko` | 4 | minigame_stalking_mission.bin · pause_message.bin · pause_message_person.bin · talk_talker.bin |
| `Yurika Tachibana` | 4 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin · talk_talker.bin |
| `...Huh?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `...Right.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `...Yes.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `A job?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `About what?` | 3 | auth.bin · pause_message.bin · sound_auth.bin |
| `AD-9 Research Paper` | 3 | evidence_item_to_update.bin · item.bin · talk_select_select.bin |
| `Advanced` | 3 | minigame_hanafuda_string_hanafuda.bin · minigame_oichokabu_string_oichokabu.bin · talk_select_select.bin |
| `Akira Murase` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Alice Ino` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `All` | 3 | qsearch_search.bin · talk_talker.bin · ui_text.bin |
| `All right!` | 3 | minigame_mahjong_string_npc.bin · sound_auth.bin · talk.bin |
| `Am I wrong?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `And you are?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Aoi` | 3 | item.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Are you sure?` | 3 | msg.bin · sound_auth.bin · talk.bin |
| `Asuka Hachitani` | 3 | evidence_item_to_update.bin · item.bin · minigame_stalking_mission.bin |
| `Attack` | 3 | pause_tutorial.bin · player_point.bin · ui_text.bin |
| `Bantam` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Bat` | 3 | asset_asset_name_judge.bin · minigame_batting_center_message.bin · verification_survey_3d.bin |
| `Beef Zone` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `But...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Café Alps` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Café Mijore` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Camera` | 3 | asset_asset_name_judge.bin · input_action.bin · ui_text.bin |
| `Case File` | 3 | help.bin · manual.bin · ui_text.bin |
| `Change Controls` | 3 | drone_message.bin · pause_others.bin · ui_text.bin |
| `Change Settings` | 3 | minigame_hanafuda_string_hanafuda.bin · minigame_hanafuda_string_mainmenu.bin · minigame_oichokabu_string_oichokabu.bin |
| `Chapter 10: Chumming the Water` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 11: Curtain Call` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 12: Behind Closed Doors` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 1: Three Blind Mice` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 2: Beneath the Surface` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 3: The Stickup` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 4: Skeletons in the Closet` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 5: Days Gone By` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 6: Collusion` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 7: Limelight` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 8: A Broken Bond` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chapter 9: The Miracle Drug` | 3 | caption.bin · mission_mission_kind.bin · title_movie_chapter.bin |
| `Chase` | 3 | input_game_state.bin · manual.bin · title_movie.bin |
| `Check Bonus Rewards` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Child` | 3 | minigame_chase_mission.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Confirm` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Daichi Ryuzenji` | 3 | caption.bin · minigame_darts_rival_info_judge.bin · minigame_poker_com_special_4.bin |
| `Dice & Cube` | 3 | controller_guide.bin · input_game_state.bin · manual.bin |
| `Disguises` | 3 | help.bin · manual.bin · ui_text.bin |
| `Don't worry.` | 3 | auth.bin · sound_auth.bin · talk_select_select.bin |
| `Dora` | 3 | minigame_mahjong_string_common.bin · minigame_mahjong_string_yaku.bin · ui_text.bin |
| `Drone League` | 3 | complete_group.bin · help.bin · manual.bin |
| `Dwayne Cruise` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Ebisu Pawn Owner, Fukutsu` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Eh?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `End` | 3 | input_action.bin · msg.bin · ui_text.bin |
| `Evade` | 3 | controller_guide.bin · manual.bin · ui_text.bin |
| `EX Airborne Assault` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Bat Appropriation` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Bind Reversal` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Blasting Kick` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Drunken Fist` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Finishing Blow` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Flowing Kick` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Flying Blow` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Frontal Beatdown` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Infuriating Counter` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Leapfrog Destruction` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Light Bullet` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Mounting Punch` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Playground Panic` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Reverse Beatdown` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Running Assault` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Running Palm Strike` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Running Wall Smash` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Tiger Dances With Crane` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Waking Wrath` | 3 | help.bin · manual.bin · player_skill.bin |
| `EX Wall Acrobatics` | 3 | help.bin · manual.bin · player_skill.bin |
| `Excuse me.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Fair enough.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Fighting Stance` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Fighting Vipers` | 3 | manual.bin · title_root.bin · ui_text.bin |
| `Focus` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `For real?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Friends` | 3 | help.bin · manual.bin · pause_complete_profile.bin |
| `Fuji Soba` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Fuyuhiko Tanaka` | 3 | evidence_item_to_update.bin · item.bin · side_case_side_case_request.bin |
| `Gindaco Highball Tavern` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Girlfriends` | 3 | help.bin · manual.bin · pause_complete_profile.bin |
| `Good question.` | 3 | auth.bin · pause_message.bin · sound_auth.bin |
| `Goro Moroboshi` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Got it.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Gotcha.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `Grabbing Enemies and Picking Up Weapons` | 3 | manual.bin · pause_tutorial.bin · tips.bin |
| `Guard` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Gyu-Kaku` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Hanae Ida` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Haoyu Xiu` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Hello?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Here we go!` | 3 | auth.bin · minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Here you go.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Hey there.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `Hey!` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Hi.` | 3 | auth.bin · pause_message.bin · sound_auth.bin |
| `Higashi` | 3 | character_npc_soldier_name_group.bin · minigame_chase_mission.bin · minigame_mahjong_string_yaku.bin |
| `Hint` | 3 | continue_info_tips_condition.bin · input_action.bin · ui_text.bin |
| `Hit` | 3 | minigame_batting_center_message.bin · msg.bin · ui_text.bin |
| `Hmm...` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `Hmph.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Honda` | 3 | character_npc_soldier_name_group.bin · map_icon.bin · talk_talker.bin |
| `Horseplayer Detective` | 3 | caption.bin · character_npc_soldier_name_group.bin · minigame_chase_mission.bin |
| `Huh!?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `I did.` | 3 | auth.bin · pause_message.bin · talk.bin |
| `I figured as much.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `I think so.` | 3 | pause_message.bin · sound_auth.bin · talk_popup_popup.bin |
| `I'd honestly rather not trick her.` | 3 | pause_message.bin · talk.bin · talk_select_select.bin |
| `Ikinari Steak` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `In that case...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Interesting.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Intermediate` | 3 | minigame_hanafuda_string_hanafuda.bin · minigame_oichokabu_string_oichokabu.bin · talk_select_select.bin |
| `Is something wrong?` | 3 | auth.bin · sound_auth.bin · talk_select_select.bin |
| `Is that so?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Issei Hoshino` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `It's Yagami.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Jo Masuda` | 3 | pause_message.bin · pause_message_person.bin · talk_talker.bin |
| `Kaede Sanada` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kaito-san.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Kamurocho's Mad Bomber` | 3 | complete_checklist.bin · mission_mission_kind.bin · scene_scenario_explanation.bin |
| `KamuroGo` | 3 | help.bin · manual.bin · ui_text.bin |
| `Kaneda` | 3 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Kaoru Ichinose` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Kasai` | 3 | character_npc_soldier_name_group.bin · map_icon.bin · talk_talker.bin |
| `Kawada` | 3 | character_npc_soldier_name_group.bin · side_case_side_case_request.bin · talk_talker.bin |
| `Kazufumi Kamaguchi` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kazuhisa Norimoto` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kazuya Ayabe` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Keigo Izumida` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Kenta Uozumi` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kick` | 3 | controller_guide.bin · input_action.bin · pause_tutorial.bin |
| `Kim Won-soon` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kiyoshiro Asamura` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Ko Hattori` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Koga` | 3 | character_npc_soldier_name_group.bin · map_icon.bin · talk_talker.bin |
| `Koi-koi` | 3 | controller_guide.bin · input_game_state.bin · manual.bin |
| `Kume's Autopsy Report` | 3 | evidence_item_to_update.bin · item.bin · talk_select_select.bin |
| `Kunihiko Morita` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Kunimura's Autopsy Report` | 3 | evidence_item_to_update.bin · item.bin · talk_select_select.bin |
| `Kunio Ichinose` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Kyohei Hamura` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Kyushu No. 1 Star` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Large Yakuza` | 3 | character_npc_soldier_name_group.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Legend` | 3 | option.bin · save_data_detail.bin · ui_text.bin |
| `Lock Picking` | 3 | controller_guide.bin · input_game_state.bin · minigame_picking_job_picking_job.bin |
| `Lower Camera` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `M Side Cafe` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Mahjong` | 3 | controller_guide.bin · input_game_state.bin · manual.bin |
| `Maki` | 3 | item.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Mami Sakuma` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Man in Black` | 3 | character_npc_soldier_name_group.bin · item.bin · talk_talker.bin |
| `Map` | 3 | help.bin · manual.bin · ui_text.bin |
| `Map Display` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Masakazu Nekomiya` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Mashiba's Autopsy Report` | 3 | evidence_item_to_update.bin · item.bin · talk_select_select.bin |
| `Masked Man` | 3 | character_npc_soldier_name_group.bin · minigame_chase_mission.bin · talk_talker.bin |
| `Menu` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Miharu Shima` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Mika` | 3 | evidence_item_to_update.bin · item.bin · minigame_picking_job_picking_job.bin |
| `Minami` | 3 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Miracle Darts` | 3 | item.bin · minigame_darts_dart_kind.bin · pause_crowdfunding.bin |
| `Mitsugu Matsugane` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Mitsuru Kuroiwa` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Morio Onodera` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Move` | 3 | access_type.bin · controller_guide.bin · ui_text.bin |
| `Naoko` | 3 | item.bin · minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Naotaro Terahara` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Next` | 3 | msg.bin · talk_select_select.bin · ui_text.bin |
| `No problem.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `No way...` | 3 | auth.bin · minigame_mahjong_string_npc.bin · talk.bin |
| `No!` | 3 | auth.bin · pause_message.bin · sound_auth.bin |
| `No, not really.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `No...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Noboru Tateyama` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Noriko Taguchi` | 3 | item.bin · side_case_side_case_request.bin · talk_talker.bin |
| `Noriko's Husband` | 3 | minigame_photo_shooting_mission_todo_item.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Not yet.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `Oh no...` | 3 | sound_auth.bin · talk.bin · talk_popup_popup.bin |
| `Oh yeah!` | 3 | minigame_mahjong_string_npc.bin · sound_auth.bin · talk.bin |
| `Oh, right.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Ohata` | 3 | pause_message.bin · pause_message_person.bin · talk_talker.bin |
| `Oicho-kabu` | 3 | controller_guide.bin · input_game_state.bin · manual.bin |
| `Okay.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `Old Man` | 3 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin · talk_talker.bin |
| `Open Riichi` | 3 | complete.bin · minigame_mahjong_string_command.bin · minigame_mahjong_string_yaku.bin |
| `Order` | 3 | access_type.bin · msg.bin · ui_text.bin |
| `Pink Street` | 3 | map_place.bin · position_stage_warp.bin · talk_select_select.bin |
| `Premier Darts` | 3 | item.bin · minigame_darts_dart_kind.bin · pause_crowdfunding.bin |
| `Premium Adventure` | 3 | caption.bin · reward_judge_clear_achievement.bin · ui_text.bin |
| `Previously...` | 3 | caption.bin · title_movie.bin · ui_text.bin |
| `Probably.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Put Away` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Quadra Garden` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Quick Search Mode` | 3 | help.bin · input_game_state.bin · manual.bin |
| `Quickstarter` | 3 | help.bin · manual.bin · ui_text.bin |
| `Really?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Rei Miyamoto` | 3 | evidence_item_to_update.bin · item.bin · side_case_side_case_request.bin |
| `Reset Camera` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Return to Title` | 3 | msg.bin · pause_others.bin · pause_trial_root.bin |
| `Right.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Right?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Ringer Hut` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Ryo` | 3 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Ryusuke Kido` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Saito` | 3 | character_npc_soldier_name_group.bin · minigame_stalking_mission.bin · talk_talker.bin |
| `Sakakiba` | 3 | character_npc_soldier_name_group.bin · map_icon.bin · talk_talker.bin |
| `Saori Shirosaki` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Satoshi Shioya` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Save` | 3 | help.bin · manual.bin · ui_text.bin |
| `Sebastian Hutton` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Seiya` | 3 | evidence_item_to_update.bin · item.bin · talk_talker.bin |
| `Select Item` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Settings` | 3 | msg.bin · pause_trial_root.bin · ui_text.bin |
| `Shigeru Kajihira` | 3 | caption.bin · evidence_item_to_update.bin · item.bin |
| `Shin Amon` | 3 | caption.bin · character_npc_soldier_name_group.bin · item.bin |
| `Shin Fujimori` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Shinzato Madoka` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Shoot` | 3 | controller_guide.bin · input_action.bin · minigame_batting_center_type_of_pitch.bin |
| `Shortcuts` | 3 | help.bin · manual.bin · ui_text.bin |
| `Showdown` | 3 | minigame_oichokabu_string_oichokabu.bin · title_movie.bin · ui_text.bin |
| `Shuichi Hatano` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Shun Isaka` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Simple` | 3 | minigame_cabaret_island_coordinate_accessory_bracelet.bin · msg.bin · save_data_detail.bin |
| `Skills` | 3 | help_category.bin · manual.bin · ui_text.bin |
| `So what?` | 3 | auth.bin · minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Sota Nonomura` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Sounds good.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Start` | 3 | input_action.bin · map_icon.bin · ui_text.bin |
| `Stop!` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Super Take Back` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Sushi Gin` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Sushi Zanmai` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Take Back` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Take Picture` | 3 | access_type.bin · input_action.bin · talk_select_select.bin |
| `Takeda` | 3 | character_npc_soldier_name_group.bin · item.bin · talk_talker.bin |
| `Takemitsu Owner` | 3 | character_friend_list.bin · complete_checklist.bin · talk_talker.bin |
| `Takeo Inose` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Tanago` | 3 | character_npc_soldier_name_group.bin · talk_select_select.bin · talk_talker.bin |
| `Test 1` | 3 | mission_mission_kind.bin · search_param.bin · talk_select_select.bin |
| `Test 3` | 3 | mission_mission_kind.bin · search_param.bin · talk_select_select.bin |
| `Thank you so much!` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Thank you very much.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Thank you!` | 3 | auth.bin · pause_message.bin · talk.bin |
| `The Mad Bomber` | 3 | evidence_item_to_update.bin · item.bin · talk_talker.bin |
| `The Twisted Trio: Ass Catchem` | 3 | complete_checklist.bin · mission_mission_kind.bin · scene_scenario_explanation.bin |
| `The Twisted Trio: Judge Creep 'n Peep` | 3 | complete_checklist.bin · mission_mission_kind.bin · scene_scenario_explanation.bin |
| `The Twisted Trio: Panty Professor` | 3 | complete_checklist.bin · mission_mission_kind.bin · scene_scenario_explanation.bin |
| `Toshikazu Sagara` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Toshiro Koizuka` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Uh...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Um...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Understood.` | 3 | auth.bin · pause_message.bin · talk.bin |
| `Upgrade Abilities` | 3 | help.bin · manual.bin · pause_tutorial.bin |
| `Use Item` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Valuables` | 3 | help.bin · manual.bin · ui_text.bin |
| `Very well.` | 3 | auth.bin · pause_message.bin · talk.bin |
| `View Piece Details` | 3 | controller_guide.bin · manual.bin · ui_text.bin |
| `Wait, what?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Wall Jump / Wall Strike` | 3 | manual.bin · pause_tutorial.bin · tips.bin |
| `Wang` | 3 | character_npc_soldier_name_group.bin · side_case_side_case_request.bin · talk_talker.bin |
| `What is it?` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `What the hell!?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `What the hell...` | 3 | minigame_mahjong_string_npc.bin · sound_auth.bin · talk.bin |
| `What the hell?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `What's going on?` | 3 | auth.bin · pause_message.bin · talk.bin |
| `What's that?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `What...?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `What?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Where is he?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Who are you?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Will do.` | 3 | pause_message.bin · sound_auth.bin · talk.bin |
| `Yagami-kun!` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yagami-san!` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yagami-san.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yagami-san...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yagami-san?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yasuhiro Furuya` | 3 | character_friend_list.bin · complete_checklist.bin · talk_category_title.bin |
| `Yeah, of course.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yeah...` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yeah?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yes?` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yoronotaki` | 3 | complete_group.bin · map_place.bin · shop.bin |
| `Yoshida Batting Center` | 3 | help.bin · manual.bin · map_place.bin |
| `You're telling me.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `You've gotta be kidding me!` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Yup.` | 3 | auth.bin · sound_auth.bin · talk.bin |
| `Zhuang Shi` | 3 | item.bin · talk_talker.bin · verification_survey_3d.bin |
| `Zoom` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Zoom In` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `Zoom Out` | 3 | controller_guide.bin · input_action.bin · ui_text.bin |
| `${value} Han` | 2 | minigame_mahjong_string_common.bin · msg.bin |
| `(...And there's my way up.)` | 2 | sound_auth.bin · talk.bin |
| `(1370. Time to give it a try.)` | 2 | sound_auth.bin · talk.bin |
| `(Bingo.)` | 2 | sound_auth.bin · talk.bin |
| `(Dammit, I need a code to get in.)` | 2 | sound_auth.bin · talk.bin |
| `(Doesn't look like anyone's in here.)` | 2 | sound_auth.bin · talk.bin |
| `(Doesn't look like this door'll open.)` | 2 | sound_auth.bin · talk.bin |
| `(Guess I'll just have to pick the lock.)` | 2 | sound_auth.bin · talk.bin |
| `(I bet Le Marche has some good stuff.)` | 2 | pause_message.bin · talk.bin |
| `(I can get out on the roof from here.)` | 2 | sound_auth.bin · talk.bin |
| `(I can't believe I'm doing this...)` | 2 | sound_auth.bin · talk.bin |
| `(I can't give up now. One more try!)` | 2 | sound_auth.bin · talk.bin |
| `(I need to find a way up to Murase!)` | 2 | sound_auth.bin · talk.bin |
| `(I should probably follow him.)` | 2 | sound_auth.bin · talk.bin |
| `(It's the reception room...)` | 2 | sound_auth.bin · talk.bin |
| `(Looks like it's locked...)` | 2 | sound_auth.bin · talk.bin |
| `(Nah. Now's not a good time.)` | 2 | pause_message.bin · talk.bin |
| `(No choice now but to go all in!)` | 2 | sound_auth.bin · talk.bin |
| `(No, maybe not right now.)` | 2 | pause_message.bin · talk.bin |
| `(Now where should we go today?)` | 2 | pause_message.bin · talk.bin |
| `(Okay, now to climb this fence.)` | 2 | sound_auth.bin · talk.bin |
| `(Okay. Let's see what she says.)` | 2 | pause_message.bin · talk.bin |
| `(Phew, tricked him.)` | 2 | sound_auth.bin · talk.bin |
| `(Phew. That was a close one.)` | 2 | sound_auth.bin · talk.bin |
| `(She might be on this floor...)` | 2 | sound_auth.bin · talk.bin |
| `(Shoot. I don't have a choice.)` | 2 | sound_auth.bin · talk.bin |
| `(Should I invite Sana-chan out?)` | 2 | pause_message.bin · talk.bin |
| `(Sturdy door for a reception room.)` | 2 | sound_auth.bin · talk.bin |
| `(That just might do the trick.)` | 2 | sound_auth.bin · talk.bin |
| `(Wait... Did I put the code in wrong?)` | 2 | sound_auth.bin · talk.bin |
| `(Where could Giant Impact appear next?)` | 2 | talk.bin · talk_question_text.bin |
| `(Yes, got it open.)` | 2 | sound_auth.bin · talk.bin |
| `*sigh*` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `...All right.` | 2 | sound_auth.bin · talk.bin |
| `...And?` | 2 | sound_auth.bin · talk.bin |
| `...Got it.` | 2 | sound_auth.bin · talk.bin |
| `...Guess so.` | 2 | sound_auth.bin · talk.bin |
| `...Hello?` | 2 | sound_auth.bin · talk.bin |
| `...Hm?` | 2 | sound_auth.bin · talk.bin |
| `...Hmm, okay then...` | 2 | pause_message.bin · talk.bin |
| `...I figured as much.` | 2 | pause_message.bin · talk.bin |
| `...I knew it.` | 2 | pause_message.bin · talk.bin |
| `...I see.` | 2 | pause_message.bin · talk.bin |
| `...If you say so.` | 2 | sound_auth.bin · talk.bin |
| `...My eyes hurt just thinking about it.` | 2 | sound_auth.bin · talk.bin |
| `...Okay.` | 2 | sound_auth.bin · talk.bin |
| `...Seriously?` | 2 | sound_auth.bin · talk.bin |
| `...Tch!` | 2 | sound_auth.bin · talk.bin |
| `...Well, I'm fucked.` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `...What is it?` | 2 | sound_auth.bin · talk.bin |
| `...What?` | 2 | sound_auth.bin · talk.bin |
| `...With you there.` | 2 | sound_auth.bin · talk.bin |
| `...Yeah.` | 2 | auth.bin · sound_auth.bin |
| `10th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `10th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `1st Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `1st Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `2nd Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `2nd Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `3rd Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `3rd Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `4th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `4th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `5th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `5th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `6th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `6th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `7th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `7th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `8th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `8th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `9th Dan` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `9th Kyu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `<Sign:4>` | 2 | minigame_cabaret_cabaret.bin · pad_button.bin |
| `<symbol=vf5_key_g>` | 2 | input_action.bin · minigame_vf5_key_set.bin |
| `<symbol=vf5_key_k>` | 2 | input_action.bin · minigame_vf5_key_set.bin |
| `<symbol=vf5_key_k> + <symbol=vf5_key_g>` | 2 | input_action.bin · minigame_vf5_key_set.bin |
| `<symbol=vf5_key_p>` | 2 | input_action.bin · minigame_vf5_key_set.bin |
| `<symbol=vf5_key_p> + <symbol=vf5_key_g>` | 2 | input_action.bin · minigame_vf5_key_set.bin |
| `<symbol=vf5_key_p> + <symbol=vf5_key_k>` | 2 | input_action.bin · minigame_vf5_key_set.bin |
| `A Challenge` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `A Final Event` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `A Golden Mouse` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `A VR Pair of Dice` | 2 | complete_checklist.bin · talk_category_title.bin |
| `About Skills` | 2 | help.bin · manual.bin |
| `About?` | 2 | auth.bin · sound_auth.bin |
| `Action` | 2 | input_action.bin · ui_text.bin |
| `Actually...` | 2 | sound_auth.bin · talk.bin |
| `Adachi` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Adaptable` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Ah!` | 2 | sound_auth.bin · talk.bin |
| `Ah.` | 2 | sound_auth.bin · talk.bin |
| `Ah. Neat.` | 2 | talk.bin · talk_select_select.bin |
| `akahana` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Akaushimaru` | 2 | complete_group.bin · talk_select_select.bin |
| `Akaushimaru (Hotel District)` | 2 | map_place.bin · shop.bin |
| `Akaushimaru (Tenkaichi St.)` | 2 | map_place.bin · shop.bin |
| `Akira Kai` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Akira Kawakami` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `All right. I'll hold you to that, then.` | 2 | pause_message.bin · talk.bin |
| `All right. I'll see what I can do.` | 2 | pause_message.bin · talk.bin |
| `Amane-san?` | 2 | pause_message.bin · talk.bin |
| `An error has occurred.` | 2 | message_dialog.bin · msg.bin |
| `An excuse...?` | 2 | pause_message.bin · talk.bin |
| `And also...` | 2 | sound_auth.bin · talk.bin |
| `And if I may be so forward...` | 2 | sound_auth.bin · talk.bin |
| `And if I refuse?` | 2 | auth.bin · sound_auth.bin |
| `And why's that?` | 2 | sound_auth.bin · talk.bin |
| `And?` | 2 | auth.bin · sound_auth.bin |
| `Aniki...` | 2 | auth.bin · sound_auth.bin |
| `Anonymous` | 2 | drone_enemy_division5.bin · side_case_side_case_request.bin |
| `Anything else?` | 2 | sound_auth.bin · talk.bin |
| `Are you in your thirties?` | 2 | talk.bin · talk_select_select.bin |
| `Are you not feeling well?` | 2 | talk.bin · talk_select_select.bin |
| `Are you okay?` | 2 | pause_message.bin · sound_auth.bin |
| `Are you saying...` | 2 | pause_message.bin · talk.bin |
| `Are you serious?` | 2 | pause_message.bin · sound_auth.bin |
| `Are you sure...?` | 2 | sound_auth.bin · talk.bin |
| `Are you talking to me?` | 2 | sound_auth.bin · talk.bin |
| `Armed Robber (Suspect)` | 2 | evidence_item_to_update.bin · item.bin |
| `Asami Morimiya` | 2 | evidence_item_to_update.bin · item.bin |
| `Asano` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Ashtray` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Assist Mode` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Autosave` | 2 | option.bin · ui_text.bin |
| `ayabe` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Azusa Otaki` | 2 | item.bin · verification_survey.bin |
| `barten` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Base` | 2 | access_type.bin · help_category.bin |
| `Basically...` | 2 | auth.bin · sound_auth.bin |
| `Beautiful Eyes…` | 2 | minigame_cabaret_cabaret.bin · sound_auth_subtitles_speech_list_caba_hikaru.bin |
| `Beginner Darts` | 2 | item.bin · minigame_darts_dart_kind.bin |
| `Believe it!` | 2 | talk.bin · talk_popup_popup.bin |
| `Berserker` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Bet` | 2 | msg.bin · ui_text.bin |
| `Better get your game face on!` | 2 | pause_message.bin · talk.bin |
| `Blade Resist` | 2 | player_point.bin · ui_text.bin |
| `Blended Coffee` | 2 | item.bin · talk_select_random_ls.bin |
| `Blocking Attacks` | 2 | pause_tutorial.bin · tips.bin |
| `Blonde looks way better.` | 2 | talk.bin · talk_select_select.bin |
| `Blonde Woman` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `Blowfish` | 2 | complete_checklist.bin · item.bin |
| `Blue Mountain` | 2 | item.bin · talk_select_random_ls.bin |
| `Bomber` | 2 | caption.bin · character_npc_soldier_name_group.bin |
| `Bonus Content` | 2 | help.bin · manual.bin |
| `Boss` | 2 | character_npc_soldier_name_group.bin · map_icon.bin |
| `Boss!` | 2 | auth.bin · sound_auth.bin |
| `Boss...` | 2 | auth.bin · sound_auth.bin |
| `Brake` | 2 | controller_guide.bin · input_action.bin |
| `Breakthrough Center` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Brightness Level` | 2 | option.bin · ui_text.bin |
| `Broken Security Camera` | 2 | evidence_item_to_update.bin · talk_select_select.bin |
| `Bungo Bando` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Businessman` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `But can you see me as a love interest?` | 2 | talk.bin · talk_select_select.bin |
| `But how?` | 2 | sound_auth.bin · talk.bin |
| `But you just didn't want to admit it?` | 2 | talk.bin · talk_select_select.bin |
| `But?` | 2 | auth.bin · talk.bin |
| `By the way...` | 2 | auth.bin · sound_auth.bin |
| `Call Koi` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Can I talk to Moon?` | 2 | sound_auth.bin · talk_select_select.bin |
| `Can't believe it.` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Captain Hamura.` | 2 | auth.bin · sound_auth.bin |
| `Captain Hamura...?` | 2 | auth.bin · sound_auth.bin |
| `Capture the Horseplayer Detective` | 2 | mission_mission_kind.bin · ui_text.bin |
| `Card Type` | 2 | minigame_oichokabu_string_oichokabu.bin · ui_text.bin |
| `CCC` | 2 | minigame_live_chat_chat_commands.bin · talk_select_select.bin |
| `Central Rook User` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Chair` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Chairman Shigeru Kajihira.` | 2 | auth.bin · sound_auth.bin |
| `Challenge [Eighth]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Fifth]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [First]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Fourth]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Ninth]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Second]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Seventh]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Sixth]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Tenth]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge [Third]` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Challenge Course` | 2 | minigame_batting_center_message.bin · talk_select_select.bin |
| `Challenge Rule: Long Course` | 2 | complete_checklist.bin · pause_crowdfunding.bin |
| `Challenge Rule: Middle Course` | 2 | complete_checklist.bin · pause_crowdfunding.bin |
| `Champion District` | 2 | map_place.bin · talk_select_select.bin |
| `Change contact color.` | 2 | minigame_cabaret_island_coordinate_makeup_category.bin · minigame_cabaret_island_coordinate_makeup_color_contact.bin |
| `Change lip color.` | 2 | minigame_cabaret_island_coordinate_makeup_category.bin · minigame_cabaret_island_coordinate_makeup_lip.bin |
| `Change Minimap Size` | 2 | controller_guide.bin · input_action.bin |
| `Changing Styles` | 2 | manual.bin · tips.bin |
| `Chaotic Challenge Course` | 2 | complete_checklist.bin · talk_select_select.bin |
| `Charles Employee` | 2 | caption.bin · character_npc_soldier_name_group.bin |
| `Charles Receptionist` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `Chase and Capture` | 2 | controller_guide.bin · manual.bin |
| `Chateaubriand, blue.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Check Discard` | 2 | controller_guide.bin · input_action.bin |
| `Check Items Obtained` | 2 | controller_guide.bin · input_action.bin |
| `Check Settings` | 2 | minigame_hanafuda_string_hanafuda.bin · minigame_hanafuda_string_mainmenu.bin |
| `Checkmate. Use a Take Back?` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Chef` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Chips Left:` | 2 | player_point.bin · ui_text.bin |
| `City Missions:` | 2 | msg.bin · save_data_detail.bin |
| `Clear` | 2 | minigame_batting_center_message.bin · ui_text.bin |
| `Client` | 2 | talk_talker.bin · ui_text.bin |
| `Club SEGA` | 2 | help.bin · manual.bin |
| `Club SEGA (Nakamichi St.)` | 2 | complete_group.bin · map_place.bin |
| `Club SEGA (Theater Square)` | 2 | complete_group.bin · map_place.bin |
| `Coelacanth` | 2 | complete_checklist.bin · item.bin |
| `Coffee Maker` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Come in.` | 2 | auth.bin · sound_auth.bin |
| `Come on.` | 2 | auth.bin · sound_auth.bin |
| `Come on...` | 2 | sound_auth.bin · talk.bin |
| `console` | 2 | platform_term.bin · sound_cuesheet_info.bin |
| `Controller` | 2 | msg.bin · platform_term.bin |
| `Controls` | 2 | option.bin · ui_text.bin |
| `Conversation: Chaining Correct Choices` | 2 | help.bin · manual.bin |
| `Cooperative EX Action` | 2 | help.bin · manual.bin |
| `Cost` | 2 | drone_message.bin · ui_text.bin |
| `Cost Limit` | 2 | drone_message.bin · ui_text.bin |
| `Could he be a businessman?` | 2 | talk.bin · talk_select_select.bin |
| `Could you ever see me as your boyfriend?` | 2 | talk.bin · talk_select_select.bin |
| `Could've fooled me.` | 2 | auth.bin · sound_auth.bin |
| `Count-Up` | 2 | complete_checklist.bin · manual.bin |
| `Counterattacker` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Course` | 2 | minigame_batting_center_message.bin · ui_text.bin |
| `Crab` | 2 | complete_checklist.bin · item.bin |
| `Crap.` | 2 | pause_message.bin · talk.bin |
| `Crap...` | 2 | sound_auth.bin · talk.bin |
| `Creating Extracts` | 2 | help.bin · manual.bin |
| `Cricket` | 2 | complete_checklist.bin · manual.bin |
| `Crime Scene Diagram` | 2 | evidence_item_to_update.bin · item.bin |
| `Customers who don't order alcohol?` | 2 | talk.bin · talk_select_select.bin |
| `Daichi Ogata` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Daisuke` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `Daisuke Koshimizu` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Dammit!` | 2 | auth.bin · sound_auth.bin |
| `Dammit...` | 2 | sound_auth.bin · talk.bin |
| `Damn it!` | 2 | auth.bin · talk.bin |
| `Damn right.` | 2 | auth.bin · sound_auth.bin |
| `Damn you, Yagami!` | 2 | auth.bin · talk.bin |
| `Damn, I can't freakin' win...` | 2 | talk.bin · talk_popup_popup.bin |
| `Damn. That's heavy.` | 2 | sound_auth.bin · talk.bin |
| `Damn...` | 2 | sound_auth.bin · talk.bin |
| `Dealer` | 2 | talk_talker.bin · ui_text.bin |
| `Decorating the Office` | 2 | controller_guide.bin · input_game_state.bin |
| `Default` | 2 | option.bin · ui_text.bin |
| `Defense` | 2 | player_point.bin · ui_text.bin |
| `Defensive` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Defensive Demon` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Defensive Master` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Defined` | 2 | minigame_cabaret_island_coordinate_makeup_eyelashes.bin · minigame_cabaret_island_coordinate_makeup_eyeline.bin |
| `Definitely!` | 2 | pause_message.bin · talk.bin |
| `Didn't you mean baggage?` | 2 | talk.bin · talk_select_select.bin |
| `Didn't you mean crab legs?` | 2 | talk.bin · talk_select_select.bin |
| `Didn't you mean grab bag?` | 2 | talk.bin · talk_select_select.bin |
| `Die!` | 2 | auth.bin · sound_auth.bin |
| `Dine-and-Dasher` | 2 | minigame_chase_mission.bin · talk_talker.bin |
| `Do you eat at home a lot?` | 2 | talk.bin · talk_select_select.bin |
| `Do you have a boyfriend?` | 2 | talk.bin · talk_select_select.bin |
| `Do you know who he was calling?` | 2 | auth.bin · sound_auth.bin |
| `Do you not like the concept of dating?` | 2 | talk.bin · talk_select_select.bin |
| `Don Quijote` | 2 | map_place.bin · shop.bin |
| `Don't be like that.` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Don't be ridiculous.` | 2 | auth.bin · sound_auth.bin |
| `Don't Call Koi` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Don't Promote` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Don't tell me...` | 2 | auth.bin · talk.bin |
| `Don't you feel a little out of place?` | 2 | talk.bin · talk_select_select.bin |
| `Double Down` | 2 | msg.bin · ui_text.bin |
| `Double pts. for 7+` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Dr. Shono.` | 2 | auth.bin · sound_auth.bin |
| `Drawn-out` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Drone Champion` | 2 | complete.bin · trophy.bin |
| `Drone Shooting` | 2 | controller_guide.bin · input_game_state.bin |
| `Earrings` | 2 | minigame_cabaret_island_coordinate_accessory_category.bin · verification_survey_3d.bin |
| `East Shichifuku Street` | 2 | map_place.bin · position_stage_warp.bin |
| `East Taihei Boulevard` | 2 | map_place.bin · position_stage_warp.bin |
| `Ebisu Pawn` | 2 | map_place.bin · shop.bin |
| `emi` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Emi Terasawa` | 2 | evidence_item_to_update.bin · item.bin |
| `Emi Terasawa (Victim)` | 2 | evidence_item_to_update.bin · item.bin |
| `Encountering the Keihin Gang` | 2 | help.bin · manual.bin |
| `End game and return to the desktop.` | 2 | pause_others.bin · title_root.bin |
| `Enemies Defeated` | 2 | gamer_stat.bin · pause_complete_profile.bin |
| `English` | 2 | option_audio_language.bin · option_text_language.bin |
| `Evasion` | 2 | player_point.bin · ui_text.bin |
| `Everything okay?` | 2 | sound_auth.bin · talk.bin |
| `EX Barrier Bash` | 2 | help.bin · manual.bin |
| `EX Battering Ram` | 2 | help.bin · manual.bin |
| `EX Bond: Alice Ino` | 2 | help.bin · manual.bin |
| `EX Bond: Dwayne Cruise` | 2 | help.bin · manual.bin |
| `EX Bond: Hanae Ida` | 2 | help.bin · manual.bin |
| `EX Bond: Haoyu Xiu` | 2 | help.bin · manual.bin |
| `EX Bond: Hiroto Nasugawa` | 2 | help.bin · manual.bin |
| `EX Bond: Kenta Uozumi` | 2 | help.bin · manual.bin |
| `EX Bond: Kim Won-soon` | 2 | help.bin · manual.bin |
| `EX Bond: Kiyoshiro Asamura` | 2 | help.bin · manual.bin |
| `EX Bond: Kyushu No. 1 Star Owner` | 2 | help.bin · manual.bin |
| `EX Bond: Manager Yoshida` | 2 | help.bin · manual.bin |
| `EX Bond: Sota Nonomura` | 2 | help.bin · manual.bin |
| `EX Bond: Takeo Inose` | 2 | help.bin · manual.bin |
| `EX Bond: Yasuhiro Furuya` | 2 | help.bin · manual.bin |
| `EX Bowling Strike` | 2 | help.bin · manual.bin |
| `EX Chopstick Mastery` | 2 | help.bin · manual.bin |
| `EX Cooperative Jump Kick` | 2 | help.bin · manual.bin |
| `EX Cooperative Knee Bash` | 2 | help.bin · manual.bin |
| `EX Cooperative Knee Kick` | 2 | help.bin · manual.bin |
| `EX Cooperative Power Surge` | 2 | help.bin · manual.bin |
| `EX Cooperative Powerbomb` | 2 | help.bin · manual.bin |
| `EX Cooperative Sucker Kick` | 2 | help.bin · manual.bin |
| `EX Cooperative Sucker Punch` | 2 | help.bin · manual.bin |
| `EX Dislocation` | 2 | help.bin · manual.bin |
| `EX Disposal` | 2 | help.bin · manual.bin |
| `EX Electromagnetic Torture` | 2 | help.bin · manual.bin |
| `EX Face Smash` | 2 | help.bin · manual.bin |
| `EX Feeding Frenzy` | 2 | help.bin · manual.bin |
| `EX Flying Press` | 2 | help.bin · manual.bin |
| `EX Frontal Wall Crush` | 2 | help.bin · manual.bin |
| `EX Gauge` | 2 | player_point.bin · ui_text.bin |
| `EX Guts Piercer` | 2 | help.bin · manual.bin |
| `EX Hammer Fall` | 2 | help.bin · manual.bin |
| `EX Hammer Head` | 2 | help.bin · manual.bin |
| `EX Heavyweight Drop` | 2 | help.bin · manual.bin |
| `EX Home Run Spiral` | 2 | help.bin · manual.bin |
| `EX Impulse Blade` | 2 | help.bin · manual.bin |
| `EX Knockout` | 2 | help.bin · manual.bin |
| `EX Meteor Drop` | 2 | help.bin · manual.bin |
| `EX Nunchaku Flurry` | 2 | help.bin · manual.bin |
| `EX Pendulum Kick` | 2 | help.bin · manual.bin |
| `EX Pole Slam` | 2 | help.bin · manual.bin |
| `EX Poleway to Heaven` | 2 | help.bin · manual.bin |
| `EX Reverse Wall Crush` | 2 | help.bin · manual.bin |
| `EX Salt Shaker` | 2 | help.bin · manual.bin |
| `EX Solid Smash` | 2 | help.bin · manual.bin |
| `EX Stand Crush` | 2 | help.bin · manual.bin |
| `EX Sucks to Be You` | 2 | help.bin · manual.bin |
| `EX Sweeping Strike` | 2 | help.bin · manual.bin |
| `EX Tera Charge Shot` | 2 | help.bin · manual.bin |
| `EX Tonfa Flurry` | 2 | help.bin · manual.bin |
| `EX Traffic Safety` | 2 | help.bin · manual.bin |
| `EX Tragic Downfall` | 2 | help.bin · manual.bin |
| `Exactly.` | 2 | pause_message.bin · sound_auth.bin |
| `Excuse me?` | 2 | sound_auth.bin · talk.bin |
| `Exit` | 2 | access_type.bin · controller_guide.bin |
| `Exit minigame?` | 2 | drone_message.bin · msg.bin |
| `Expert` | 2 | minigame_hanafuda_string_hanafuda.bin · talk_select_select.bin |
| `Exquisite Screw` | 2 | item.bin · verification_survey_3d.bin |
| `Extract Ingredients` | 2 | help.bin · manual.bin |
| `Extracts` | 2 | help.bin · pause_tutorial.bin |
| `Fair enough. What do you need me to do?` | 2 | pause_message.bin · talk.bin |
| `Fan` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Fantasy Zone` | 2 | input_game_state.bin · manual.bin |
| `Farewell.` | 2 | minigame_poker_com_special_2.bin · sound_auth.bin |
| `Figures.` | 2 | sound_auth.bin · talk.bin |
| `Final Challenge` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Finale: Down Came the Rain` | 2 | caption.bin · mission_mission_kind.bin |
| `Find Shono` | 2 | mission_mission_kind.bin · verification_todo_item.bin |
| `Fine, I swear.` | 2 | pause_message.bin · talk.bin |
| `Fixed Camera` | 2 | controller_guide.bin · ui_text.bin |
| `Flounder` | 2 | complete_checklist.bin · item.bin |
| `Foooooood!` | 2 | sound_auth.bin · talk.bin |
| `Fortress` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Four Riichi Draw` | 2 | minigame_mahjong_string_agari.bin · minigame_mahjong_string_mangan.bin |
| `Four-Six` | 2 | minigame_oichokabu_string_oichokabu.bin · ui_text.bin |
| `Fugu` | 2 | complete_checklist.bin · item.bin |
| `Fukuhara` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Fumie Taniyama` | 2 | item.bin · side_case_side_case_request.bin |
| `Fumio Matsuzaki` | 2 | character_friend_list.bin · complete_checklist.bin |
| `Furuya` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Gah...! Shit!` | 2 | sound_auth.bin · talk.bin |
| `Game Style` | 2 | minigame_mahjong_string_setting.bin · ui_text.bin |
| `Gamo` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `genda` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Genda` | 2 | talk_select_select.bin · talk_talker.bin |
| `Genda Law Office.` | 2 | auth.bin · sound_auth.bin |
| `Genda-sensei.` | 2 | sound_auth.bin · talk.bin |
| `Genius` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Get back here!` | 2 | auth.bin · sound_auth.bin |
| `Get the fuck outta here!` | 2 | auth.bin · minigame_poker_com_high_3.bin |
| `Glasses` | 2 | minigame_cabaret_island_coordinate_accessory_category.bin · search_characteristic.bin |
| `Go on.` | 2 | sound_auth.bin · talk.bin |
| `Go!` | 2 | auth.bin · talk.bin |
| `Goby` | 2 | complete_checklist.bin · item.bin |
| `Gold Keycard` | 2 | item.bin · verification_survey_3d.bin |
| `Good idea!` | 2 | pause_message.bin · talk.bin |
| `Good idea.` | 2 | pause_message.bin · sound_auth.bin |
| `Good luck on your interview.` | 2 | pause_message.bin · talk.bin |
| `Good luck.` | 2 | sound_auth.bin · talk.bin |
| `Good point.` | 2 | auth.bin · sound_auth.bin |
| `Got it!` | 2 | sound_auth.bin · talk.bin |
| `Grab` | 2 | access_type.bin · ui_text.bin |
| `Grab / Throw` | 2 | controller_guide.bin · input_action.bin |
| `Great!` | 2 | minigame_poker_com_special_4.bin · talk.bin |
| `Great. I'll go check it out now.` | 2 | sound_auth.bin · talk.bin |
| `Guess not.` | 2 | auth.bin · sound_auth.bin |
| `Guess so.` | 2 | auth.bin · sound_auth.bin |
| `Gun Resist` | 2 | player_point.bin · ui_text.bin |
| `Hah!` | 2 | sound_auth.bin · talk.bin |
| `Hair` | 2 | minigame_cabaret_island_coordinate_makeup_category.bin · verification_survey_3d.bin |
| `Hajime Obayashi` | 2 | item.bin · side_case_side_case_request.bin |
| `hamura` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Hamura and Ichinose's Missing Link` | 2 | evidence_item_to_update.bin · item.bin |
| `Hamura-san.` | 2 | auth.bin · sound_auth.bin |
| `Hanafuda` | 2 | minigame_oichokabu_string_oichokabu.bin · ui_text.bin |
| `Hand Guide` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Hangout Spots` | 2 | help.bin · manual.bin |
| `Hasegawa` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `hashiki` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Hashiki's Autopsy Report` | 2 | evidence_item_to_update.bin · item.bin |
| `hattori` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Have it your way.` | 2 | auth.bin · talk.bin |
| `Have you written anything new lately?` | 2 | talk.bin · talk_select_select.bin |
| `He'll go after one more drink.` | 2 | talk.bin · talk_select_select.bin |
| `He'll go after two more drinks.` | 2 | talk.bin · talk_select_select.bin |
| `Health` | 2 | player_point.bin · ui_text.bin |
| `Heh.` | 2 | auth.bin · sound_auth.bin |
| `Heh...` | 2 | sound_auth.bin · talk.bin |
| `Hehe. You tell me.` | 2 | pause_message.bin · talk.bin |
| `Hell no!` | 2 | sound_auth.bin · talk.bin |
| `Hell yeah!` | 2 | auth.bin · sound_auth.bin |
| `Here I go!` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `Here.` | 2 | sound_auth.bin · talk.bin |
| `Hey, as long as you're happy.` | 2 | talk.bin · talk_select_select.bin |
| `Hey, wait!` | 2 | auth.bin · talk.bin |
| `Hey, Yagami-san!` | 2 | pause_message.bin · talk.bin |
| `Hey, you have a sec?` | 2 | sound_auth.bin · talk.bin |
| `Hey, you okay?` | 2 | auth.bin · talk.bin |
| `Hey, you!` | 2 | auth.bin · talk.bin |
| `Hey...` | 2 | auth.bin · talk.bin |
| `Hide` | 2 | option.bin · ui_text.bin |
| `Hide / Emerge` | 2 | controller_guide.bin · input_action.bin |
| `higashi` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Higashi.` | 2 | auth.bin · sound_auth.bin |
| `Higurashi` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Hiranuma` | 2 | side_case_side_case_request.bin · talk_talker.bin |
| `Hironaka` | 2 | item.bin · talk_talker.bin |
| `Hiroshi Tsurugami` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Hiroyuki Tsuji` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Hm? What is it?` | 2 | auth.bin · talk.bin |
| `Hmm.` | 2 | pause_message.bin · talk.bin |
| `Hmm. Not sure I can do that.` | 2 | pause_message.bin · talk.bin |
| `Hmmm...` | 2 | auth.bin · sound_auth.bin |
| `Hold on.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Hold up.` | 2 | auth.bin · talk.bin |
| `Home Run Competition` | 2 | manual.bin · minigame_batting_center_message.bin |
| `Home Run Course` | 2 | minigame_batting_center_message.bin · talk_select_select.bin |
| `Home Run Hell Course` | 2 | complete_checklist.bin · talk_select_select.bin |
| `Home Runs` | 2 | minigame_batting_center_message.bin · ui_text.bin |
| `Homeless Man` | 2 | caption.bin · talk_talker.bin |
| `Homewrecker` | 2 | minigame_photo_shooting_mission_todo_item.bin · minigame_stalking_mission.bin |
| `Hooded parka` | 2 | search_characteristic.bin · verification_todo_item.bin |
| `hoshino` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Hoshino` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Hoshino!` | 2 | auth.bin · talk_select_select.bin |
| `Hoshino-kun.` | 2 | auth.bin · sound_auth.bin |
| `Hoshino-kun?` | 2 | auth.bin · sound_auth.bin |
| `Hostess` | 2 | minigame_cabaret_island_coordinate_hair_style.bin · talk_talker.bin |
| `Hotel District` | 2 | map_place.bin · talk_select_select.bin |
| `How about a little kiss?` | 2 | talk.bin · talk_select_select.bin |
| `How much?` | 2 | sound_auth.bin · talk.bin |
| `How to Learn Skills` | 2 | help.bin · manual.bin |
| `How's that?` | 2 | sound_auth.bin · talk.bin |
| `How's your love life going?` | 2 | talk.bin · talk_select_select.bin |
| `Hug Bomb Explosion Omega` | 2 | item.bin · pause_crowdfunding.bin |
| `Hug Bomb Spark Alpha` | 2 | item.bin · pause_crowdfunding.bin |
| `Hug Bomb Spark Beta` | 2 | item.bin · pause_crowdfunding.bin |
| `Huh? But...` | 2 | sound_auth.bin · talk.bin |
| `Huh? Oh...` | 2 | auth.bin · sound_auth.bin |
| `Huh? Really?` | 2 | sound_auth.bin · talk.bin |
| `Huh? What is it?` | 2 | auth.bin · talk.bin |
| `Huh? Who the hell are you!?` | 2 | sound_auth.bin · talk.bin |
| `Huh? Who're you?` | 2 | sound_auth.bin · talk.bin |
| `Huh? Why do you ask?` | 2 | pause_message.bin · talk.bin |
| `Huh? Why?` | 2 | sound_auth.bin · talk.bin |
| `Hyper Propeller H` | 2 | drone_parts.bin · pause_crowdfunding.bin |
| `I agree.` | 2 | auth.bin · pause_message.bin |
| `I am.` | 2 | pause_message.bin · talk.bin |
| `I appreciate it.` | 2 | sound_auth.bin · talk.bin |
| `I bet that keeps you pretty busy.` | 2 | talk.bin · talk_select_select.bin |
| `I do.` | 2 | sound_auth.bin · talk.bin |
| `I don't get it...` | 2 | auth.bin · minigame_mahjong_string_npc.bin |
| `I dunno...` | 2 | sound_auth.bin · talk.bin |
| `I get it.` | 2 | auth.bin · sound_auth.bin |
| `I guess so.` | 2 | sound_auth.bin · talk.bin |
| `I have.` | 2 | pause_message.bin · talk.bin |
| `I know what you're thinking.` | 2 | auth.bin · sound_auth.bin |
| `I see. That's too bad.` | 2 | pause_message.bin · talk.bin |
| `I see...` | 2 | auth.bin · talk.bin |
| `I think I get it.` | 2 | sound_auth.bin · talk_select_select.bin |
| `I think you look fabulous.` | 2 | talk.bin · talk_select_select.bin |
| `I think you'll be just fine.` | 2 | talk.bin · talk_select_select.bin |
| `I thought you might be around that age.` | 2 | talk.bin · talk_select_select.bin |
| `I want to show you my love.` | 2 | sound_auth.bin · talk.bin |
| `I want to suck your blood!` | 2 | talk.bin · talk_select_select.bin |
| `I wanted to say I love you!` | 2 | sound_auth.bin · talk.bin |
| `I won't forget.` | 2 | sound_auth.bin · talk.bin |
| `I wonder if he's still lost...` | 2 | talk.bin · talk_popup_popup.bin |
| `I wonder if that boy's lost...` | 2 | talk.bin · talk_popup_popup.bin |
| `I'd like you to be my special partner. ❤` | 2 | sound_auth.bin · talk.bin |
| `I'll do what I can.` | 2 | sound_auth.bin · talk.bin |
| `I'll take it!` | 2 | talk.bin · talk_select_select.bin |
| `I'll walk you back to the office.` | 2 | sound_auth.bin · talk.bin |
| `I'm actually pretty big on curry.` | 2 | talk.bin · talk_select_select.bin |
| `I'm fine.` | 2 | talk.bin · talk_select_select.bin |
| `I'm glad to hear that.` | 2 | pause_message.bin · talk.bin |
| `I'm her boyfriend.` | 2 | talk.bin · talk_select_select.bin |
| `I'm her friend.` | 2 | talk.bin · talk_select_select.bin |
| `I'm just glad you're safe.` | 2 | pause_message.bin · talk.bin |
| `I'm listening.` | 2 | sound_auth.bin · talk.bin |
| `I'm looking for a guy named Moon.` | 2 | sound_auth.bin · talk_select_select.bin |
| `I'm not letting you get away!` | 2 | sound_auth.bin · talk.bin |
| `I'm only kind to the ladies.` | 2 | talk.bin · talk_select_select.bin |
| `I'm so sorry!` | 2 | sound_auth.bin · talk.bin |
| `I'm sorry you had that experience.` | 2 | talk.bin · talk_select_select.bin |
| `I'm sorry.` | 2 | auth.bin · talk.bin |
| `I'm sorry...` | 2 | auth.bin · sound_auth.bin |
| `I'm taken.` | 2 | pause_message.bin · talk_select_select.bin |
| `I'm very interested in you.` | 2 | talk.bin · talk_select_select.bin |
| `I've become quite enamored with you.` | 2 | sound_auth.bin · talk.bin |
| `I've never seen you in a skirt before.` | 2 | pause_message.bin · talk.bin |
| `I, uh...` | 2 | auth.bin · talk.bin |
| `I, um...` | 2 | auth.bin · sound_auth.bin |
| `I... I...` | 2 | sound_auth.bin · talk.bin |
| `ichinose` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Ichinose from the Ministry of Health.` | 2 | sound_auth.bin · talk_select_select.bin |
| `If that's a challenge, then I accept!` | 2 | pause_message.bin · talk.bin |
| `If you say so.` | 2 | auth.bin · sound_auth.bin |
| `If you say so...` | 2 | pause_message.bin · talk.bin |
| `Inamoto` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Indeed.` | 2 | sound_auth.bin · talk.bin |
| `Inverted` | 2 | msg.bin · option.bin |
| `Investigate the Crime Scene` | 2 | mission_mission_kind.bin · verification_verification.bin |
| `Investigate the Room` | 2 | mission_mission_kind.bin · verification_verification.bin |
| `Is everything okay?` | 2 | pause_message.bin · talk.bin |
| `Is he now?` | 2 | auth.bin · talk.bin |
| `Is something the matter?` | 2 | auth.bin · sound_auth.bin |
| `Is there a problem?` | 2 | sound_auth.bin · talk.bin |
| `Ishikawa` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Ishimura` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Isn't that right?` | 2 | auth.bin · sound_auth.bin |
| `It is.` | 2 | auth.bin · sound_auth.bin |
| `It's exactly what I'm saying!` | 2 | pause_message.bin · talk.bin |
| `It's over.` | 2 | auth.bin · minigame_poker_com_special_3.bin |
| `It's Yagami!` | 2 | sound_auth.bin · talk.bin |
| `izumida` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Jin` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Junk Modifier` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Kabata` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Kabufuda` | 2 | minigame_oichokabu_string_oichokabu.bin · ui_text.bin |
| `Kaede` | 2 | minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Kai` | 2 | character_npc_soldier_name_group.bin · item.bin |
| `kaito` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Kaito-san!` | 2 | auth.bin · sound_auth.bin |
| `Kaito-san...?` | 2 | auth.bin · sound_auth.bin |
| `Kaito-san?` | 2 | auth.bin · sound_auth.bin |
| `kajihira` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Kajiwara` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Kamuro of the Dead` | 2 | controller_guide.bin · manual.bin |
| `KAMURO OF THE DEAD` | 2 | input_game_state.bin · title_root.bin |
| `kanryo` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Karin` | 2 | minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Katagiri` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Kataoka` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Kawakami` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Kawamoto` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Kawasaki` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Kazuki Koto` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Kazuya Ayabe (Suspect)` | 2 | evidence_item_to_update.bin · item.bin |
| `Keep going.` | 2 | sound_auth.bin · talk.bin |
| `Keihin Gang Thug` | 2 | caption.bin · talk_talker.bin |
| `kengo` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Kenji Kato` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Kenta Someya` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `kido` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Kido` | 2 | character_npc_soldier_name_group.bin · verification_survey_3d.bin |
| `King Koro-nyan` | 2 | item.bin · map_icon.bin |
| `Kiriko Kuwayama` | 2 | evidence_item_to_update.bin · item.bin |
| `Kitajima` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Kitamura` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Kitchen Knife` | 2 | evidence_item_to_update.bin · item.bin |
| `Knife` | 2 | character_npc_soldier_name_group.bin · verification_survey_3d.bin |
| `Konban Wife` | 2 | map_place.bin · title_movie.bin |
| `Kondo` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Koro-nyan` | 2 | map_icon.bin · talk_talker.bin |
| `Kouichi Inada` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Kuitan` | 2 | minigame_mahjong_string_setting.bin · ui_text.bin |
| `Kumakura` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Kumakura's Bag` | 2 | item.bin · verification_survey_3d.bin |
| `kuroiwa` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Kuroiwa` | 2 | character_npc_soldier_name_group.bin · talk_select_select.bin |
| `Kuroiwa!` | 2 | auth.bin · sound_auth.bin |
| `Kuroiwa.` | 2 | auth.bin · sound_auth.bin |
| `Kuroiwa...` | 2 | auth.bin · sound_auth.bin |
| `Kyohei Hamura (Suspect)` | 2 | evidence_item_to_update.bin · item.bin |
| `Laundry Cart` | 2 | evidence_item_to_update.bin · item.bin |
| `Le Marche` | 2 | map_place.bin · shop.bin |
| `Left / Right Controls` | 2 | option.bin · ui_text.bin |
| `Lemme think...` | 2 | sound_auth.bin · talk.bin |
| `Let me go!` | 2 | auth.bin · sound_auth.bin |
| `Let's Chat About a Pervert` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `Let's do this!` | 2 | auth.bin · talk_select_select.bin |
| `Let's go!` | 2 | auth.bin · talk.bin |
| `Let's go, Yagami-san!` | 2 | auth.bin · talk.bin |
| `Like what?` | 2 | sound_auth.bin · talk.bin |
| `Listen` | 2 | access_type.bin · talk_select_select.bin |
| `Little Asia` | 2 | map_place.bin · talk_select_select.bin |
| `Loading...` | 2 | msg.bin · ui_text.bin |
| `Long time no see.` | 2 | auth.bin · sound_auth.bin |
| `Look` | 2 | access_type.bin · ui_text.bin |
| `Look Around` | 2 | access_type.bin · controller_guide.bin |
| `Looking forward to it.` | 2 | sound_auth.bin · talk.bin |
| `Low-Cost ESC` | 2 | drone_parts.bin · pause_crowdfunding.bin |
| `Low-Cost Turbo` | 2 | drone_parts.bin · pause_crowdfunding.bin |
| `madam` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Maeda` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `mafuyu` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Mafuyu` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Mafuyu!` | 2 | sound_auth.bin · talk_select_select.bin |
| `Major Piece Lover` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Makihara` | 2 | item.bin · talk_talker.bin |
| `Mamoru Shimazu` | 2 | item.bin · side_case_side_case_request.bin |
| `Man in Noh Mask` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Manabu Kubota` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Mao` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Marlin` | 2 | complete_checklist.bin · item.bin |
| `Masaharu Kaito (Victim)` | 2 | evidence_item_to_update.bin · item.bin |
| `Masakazu Kurimoto (Victim)` | 2 | evidence_item_to_update.bin · item.bin |
| `Masamichi Shintani (Victim)` | 2 | evidence_item_to_update.bin · item.bin |
| `Mask` | 2 | search_characteristic.bin · verification_todo_item.bin |
| `Master and Pupil` | 2 | item.bin · scene_scenario_explanation.bin |
| `matsugane` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Matsugane Family Member` | 2 | minigame_chase_mission.bin · verification_survey_3d.bin |
| `Matsugane-san!` | 2 | auth.bin · sound_auth.bin |
| `Matsugane-san.` | 2 | auth.bin · sound_auth.bin |
| `Matsugane-san...` | 2 | auth.bin · sound_auth.bin |
| `Matsuzaki` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Maximum Threat Level` | 2 | help.bin · manual.bin |
| `Maybe.` | 2 | pause_message.bin · sound_auth.bin |
| `Me too!` | 2 | pause_message.bin · talk.bin |
| `Me too.` | 2 | pause_message.bin · sound_auth.bin |
| `Me?` | 2 | sound_auth.bin · talk.bin |
| `Meaning...` | 2 | auth.bin · sound_auth.bin |
| `Medium` | 2 | minigame_cabaret_island_coordinate_hair_style.bin · option.bin |
| `Megalodon` | 2 | complete_checklist.bin · item.bin |
| `Megumi Hashimoto` | 2 | item.bin · side_case_side_case_request.bin |
| `Mhm.` | 2 | sound_auth.bin · talk.bin |
| `Michio Inoue` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Miki` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Millennium Tower` | 2 | map_place.bin · position_stage_warp.bin |
| `Minigames` | 2 | help_category.bin · map_icon.bin |
| `Misaki Hayama` | 2 | item.bin · side_case_side_case_request.bin |
| `Mmhm.` | 2 | auth.bin · sound_auth.bin |
| `Mocha` | 2 | item.bin · talk_select_random_ls.bin |
| `Money` | 2 | player_point.bin · ui_text.bin |
| `Moon sure is bright tonight.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Moon Viewing/Cherry Blossom Viewing` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `More Details` | 2 | input_action.bin · ui_text.bin |
| `morita` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Moroboshi Clinic` | 2 | map_place.bin · shop.bin |
| `Moroboshi's calling for you.` | 2 | talk.bin · talk_select_select.bin |
| `Mortal Wounds` | 2 | pause_tutorial.bin · tips.bin |
| `Motor Raid` | 2 | input_game_state.bin · manual.bin |
| `Move Camera` | 2 | controller_guide.bin · ui_text.bin |
| `Move Crane` | 2 | controller_guide.bin · input_action.bin |
| `Move Cursor` | 2 | controller_guide.bin · ui_text.bin |
| `Move Pick (Up/Down)` | 2 | controller_guide.bin · ui_text.bin |
| `Much appreciated.` | 2 | sound_auth.bin · talk.bin |
| `murase` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Murase` | 2 | character_npc_soldier_name_group.bin · verification_survey_3d.bin |
| `Must've been hard to deal with.` | 2 | talk.bin · talk_select_select.bin |
| `My humble apologies...` | 2 | auth.bin · sound_auth.bin |
| `My Subordinate is Missing` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `Mysterious Attacker` | 2 | caption.bin · character_npc_soldier_name_group.bin |
| `N Senryo Ave.` | 2 | map_place.bin · pause_message.bin |
| `Nah, it's fine.` | 2 | sound_auth.bin · talk.bin |
| `Nah.` | 2 | auth.bin · sound_auth.bin |
| `Nasugawa` | 2 | pause_message.bin · talk_talker.bin |
| `Never mind.` | 2 | pause_message.bin · talk_select_select.bin |
| `Next Page` | 2 | talk_select_select.bin · ui_text.bin |
| `Ngh!` | 2 | sound_auth.bin · talk.bin |
| `Ngh...` | 2 | sound_auth.bin · talk.bin |
| `Nice!` | 2 | pause_message.bin · talk.bin |
| `Nice.` | 2 | sound_auth.bin · talk.bin |
| `Niiice.` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Nine Terminal Draw` | 2 | minigame_mahjong_string_agari.bin · minigame_mahjong_string_mangan.bin |
| `Nishimura` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Nishimura's Bag` | 2 | item.bin · verification_survey_3d.bin |
| `No can do.` | 2 | auth.bin · pause_message.bin |
| `No doubt about it.` | 2 | auth.bin · talk_select_select.bin |
| `No thanks.` | 2 | talk.bin · talk_select_select.bin |
| `No way!` | 2 | minigame_poker_com_special_3.bin · talk.bin |
| `No, not yet.` | 2 | sound_auth.bin · talk_select_select.bin |
| `No.` | 2 | auth.bin · sound_auth.bin |
| `Nobuyuki Kobayashi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Nope. Not at all.` | 2 | sound_auth.bin · talk.bin |
| `Not Achieved` | 2 | msg.bin · ui_text.bin |
| `Not so fast.` | 2 | auth.bin · sound_auth.bin |
| `Not sure.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Nothing.` | 2 | talk.bin · talk_select_select.bin |
| `Now that's what I'm talking about!` | 2 | pause_message.bin · talk.bin |
| `Now we're talking.` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `Now!` | 2 | auth.bin · sound_auth.bin |
| `Obayashi` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Objection!` | 2 | talk.bin · talk_select_select.bin |
| `Of course!` | 2 | sound_auth.bin · talk.bin |
| `Offensive Demon` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Offensive Master` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Offer unto me your pulsing blood!` | 2 | talk.bin · talk_select_select.bin |
| `Offer unto me your purest blood!` | 2 | talk.bin · talk_select_select.bin |
| `Oh shit!` | 2 | auth.bin · sound_auth.bin |
| `Oh shit...` | 2 | auth.bin · sound_auth.bin |
| `Oh yeah.` | 2 | sound_auth.bin · talk.bin |
| `Oh!` | 2 | sound_auth.bin · talk.bin |
| `Oh, damn.` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Oh, I see!` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `Oh, okay...` | 2 | pause_message.bin · talk.bin |
| `Oh, that?` | 2 | auth.bin · sound_auth.bin |
| `Oh, Yagami-san...` | 2 | sound_auth.bin · talk.bin |
| `Oh.` | 2 | sound_auth.bin · talk.bin |
| `Oh. Damn.` | 2 | pause_message.bin · talk.bin |
| `Oh...` | 2 | sound_auth.bin · talk.bin |
| `Oh... But...` | 2 | sound_auth.bin · talk.bin |
| `Oh?` | 2 | sound_auth.bin · talk.bin |
| `Oh? Why's that?` | 2 | pause_message.bin · talk.bin |
| `Ohhhh! Hey, what about this!?` | 2 | pause_message.bin · talk.bin |
| `Oikawa` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `OK` | 2 | msg.bin · ui_text.bin |
| `Oka` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Okay then.` | 2 | pause_message.bin · talk.bin |
| `Okay then. Let's do this.` | 2 | pause_message.bin · talk.bin |
| `Okay then...` | 2 | auth.bin · talk.bin |
| `Okay! Be right there!` | 2 | pause_message.bin · talk.bin |
| `Okay, got it.` | 2 | sound_auth.bin · talk.bin |
| `Okay, here's what happened.` | 2 | pause_message.bin · talk.bin |
| `Okay, how about...` | 2 | sound_auth.bin · talk.bin |
| `Okay, I'll be waiting.` | 2 | pause_message.bin · talk.bin |
| `Okay, okay...` | 2 | sound_auth.bin · talk.bin |
| `Okay. Here goes.` | 2 | sound_auth.bin · talk.bin |
| `Okay. Let's go.` | 2 | auth.bin · talk.bin |
| `Okay...` | 2 | auth.bin · talk.bin |
| `On it!` | 2 | auth.bin · sound_auth.bin |
| `On the Side` | 2 | help_category.bin · ui_text.bin |
| `Online Ranking` | 2 | talk_select_select.bin · ui_text.bin |
| `Ono Michio` | 2 | item.bin · talk_talker.bin |
| `Onodera` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `ookubo` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Open` | 2 | minigame_cabaret_island_coordinate_makeup_eyelashes.bin · talk_select_select.bin |
| `Opponent goes <color=blue>first</color>.` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Osamu Kikuchi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Ota` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Ow!` | 2 | sound_auth.bin · talk.bin |
| `Oyamada` | 2 | minigame_picking_job_picking_job.bin · talk_talker.bin |
| `ozaki` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Ozaki` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Pardon me.` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Pause` | 2 | input_action.bin · ui_text.bin |
| `Payout` | 2 | msg.bin · ui_text.bin |
| `Perfect.` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `Photo of Kurimoto's Corpse` | 2 | evidence_item_to_update.bin · item.bin |
| `Photojournalist Job` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `Pink Street Entrance` | 2 | map_place.bin · position_stage_warp.bin |
| `Play` | 2 | access_type.bin · talk_select_select.bin |
| `Play Time` | 2 | pause_complete_profile.bin · ui_text.bin |
| `Player` | 2 | map_icon.bin · talk_talker.bin |
| `PlayStation™Store` | 2 | platform_term.bin · title_root.bin |
| `Please don't.` | 2 | auth.bin · talk.bin |
| `Please Find My Son` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `Please Find My Son (Again)` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `Please Find My Son Again` | 2 | mission_mission_kind.bin · side_case_side_case_request.bin |
| `Pocket Tissues` | 2 | item.bin · verification_survey_3d.bin |
| `Police` | 2 | caption.bin · talk_talker.bin |
| `Poppo (E Shichifuku St.)` | 2 | map_place.bin · shop.bin |
| `Poppo (Showa St.)` | 2 | map_place.bin · shop.bin |
| `Poppo (Tenkaichi St.)` | 2 | map_place.bin · shop.bin |
| `Poppo (W Shichifuku St.)` | 2 | map_place.bin · shop.bin |
| `Potted Plant` | 2 | item.bin · verification_survey_3d.bin |
| `Probably fighting.` | 2 | talk.bin · talk_select_select.bin |
| `Promote` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Promote this piece?` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Pull the fuckin' trigger!` | 2 | auth.bin · sound_auth.bin |
| `Punch` | 2 | controller_guide.bin · input_action.bin |
| `Purchase` | 2 | msg.bin · ui_text.bin |
| `Puyo Puyo` | 2 | manual.bin · ui_text.bin |
| `Puzzle Shogi 1 (One Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 10 (Three Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 2 (One Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 3 (One Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 4 (One Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 5 (One Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 6 (Three Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 7 (Three Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 8 (Three Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Puzzle Shogi 9 (Three Move Mate)` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Quit?` | 2 | drone_message.bin · minigame_decorating_office_message.bin |
| `Rank` | 2 | minigame_mahjong_string_common.bin · ui_text.bin |
| `Re-bet` | 2 | msg.bin · ui_text.bin |
| `Really now...` | 2 | pause_message.bin · talk.bin |
| `Really!?` | 2 | pause_message.bin · talk.bin |
| `Rear View` | 2 | controller_guide.bin · input_action.bin |
| `Reckless` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Red Dora` | 2 | minigame_mahjong_string_setting.bin · ui_text.bin |
| `Red Nose (Suspect)` | 2 | evidence_item_to_update.bin · item.bin |
| `Red Snapper` | 2 | complete_checklist.bin · item.bin |
| `Relentless` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Reload` | 2 | controller_guide.bin · input_action.bin |
| `Ren` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Reset` | 2 | input_action.bin · ui_text.bin |
| `Reset Camera / Disable EX Actions` | 2 | controller_guide.bin · input_action.bin |
| `Rest` | 2 | access_type.bin · talk_select_select.bin |
| `Result` | 2 | msg.bin · ui_text.bin |
| `Results` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Resume` | 2 | talk_select_select.bin · ui_text.bin |
| `Retry` | 2 | continue_info_root.bin · ui_text.bin |
| `Return to Title Screen` | 2 | continue_info_root.bin · ui_text.bin |
| `Ribeye, well done.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Right this way.` | 2 | auth.bin · sound_auth.bin |
| `Riichi` | 2 | minigame_mahjong_string_command.bin · minigame_mahjong_string_yaku.bin |
| `Rival 100` | 2 | drone_message.bin · ui_text.bin |
| `Roll Dice` | 2 | controller_guide.bin · input_action.bin |
| `Rook User` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Rotate` | 2 | controller_guide.bin · ui_text.bin |
| `Rounds` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Rules` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Ryuzenji` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Ryuzo Genda` | 2 | caption.bin · evidence_item_to_update.bin |
| `Safe` | 2 | map_icon.bin · verification_survey_3d.bin |
| `saibancho` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `sakuraba` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Salmon` | 2 | complete_checklist.bin · item.bin |
| `sample_事件遇敵戰鬥` | 2 | instant_mission_kind.bin · mission_kind.bin |
| `sample_交談` | 2 | instant_mission_kind.bin · mission_kind.bin |
| `Sana-chan, are you free right now?` | 2 | pause_message.bin · talk.bin |
| `saori` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Saori` | 2 | talk_select_select.bin · talk_talker.bin |
| `Satoshi Yano` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Sauna Goten Employee` | 2 | evidence_item_to_update.bin · item.bin |
| `Say what!?` | 2 | auth.bin · talk.bin |
| `Say what?` | 2 | sound_auth.bin · talk.bin |
| `Scout the Matsugane Family Office` | 2 | mission_mission_kind.bin · verification_todo_item.bin |
| `Seasons` | 2 | minigame_hanafuda_string_hanafuda.bin · ui_text.bin |
| `Security Camera Footage: Pink Alley` | 2 | evidence_item_to_update.bin · item.bin |
| `See ya around.` | 2 | auth.bin · talk.bin |
| `Sega Taro` | 2 | minigame_chase_mission.bin · minigame_stalking_mission.bin |
| `Seichou Kawaguchi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `seiya` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Select` | 2 | msg.bin · ui_text.bin |
| `Sell` | 2 | msg.bin · ui_text.bin |
| `Seriously!?` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `Seriously?` | 2 | sound_auth.bin · talk.bin |
| `sharuru` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Shaven head` | 2 | search_characteristic.bin · verification_todo_item.bin |
| `Shigeru Kajihira.` | 2 | auth.bin · sound_auth.bin |
| `Shin` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Shinoda` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Shinpei Okubo (Suspect)` | 2 | evidence_item_to_update.bin · item.bin |
| `Shinryu Utsunomiya` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `shintani` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Shintani's Call History` | 2 | evidence_item_to_update.bin · talk_select_select.bin |
| `shioya` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Shit...` | 2 | auth.bin · talk.bin |
| `Shizue Kuwayama` | 2 | item.bin · side_case_side_case_request.bin |
| `Shogi King` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Shogi Points` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Shoji Ohata` | 2 | item.bin · side_case_side_case_request.bin |
| `shono` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Shono.` | 2 | auth.bin · sound_auth.bin |
| `Shop Missions:` | 2 | msg.bin · save_data_detail.bin |
| `Shopping` | 2 | help.bin · manual.bin |
| `Should I be happy about that?` | 2 | pause_message.bin · talk.bin |
| `Show` | 2 | minigame_cabaret_island_coordinate_makeup_color_contact.bin · option.bin |
| `Shun` | 2 | minigame_chase_mission.bin · talk_talker.bin |
| `Shut up!` | 2 | auth.bin · sound_auth.bin |
| `Shut up.` | 2 | pause_message.bin · sound_auth.bin |
| `Sirloin, medium rare.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Slow Defense` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Slow Starter` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Smile Burger` | 2 | complete_group.bin · item.bin |
| `Smile Burger (Nakamichi St.)` | 2 | map_place.bin · shop.bin |
| `Smile Burger (NW Theater Square)` | 2 | map_place.bin · shop.bin |
| `Snap a Photo` | 2 | minigame_photo_shooting_mission_mission_data.bin · mission_mission_kind.bin |
| `So he's the guy...` | 2 | auth.bin · sound_auth.bin |
| `So you don't automatically hate me then?` | 2 | talk.bin · talk_select_select.bin |
| `So you're a workaholic, then?` | 2 | talk.bin · talk_select_select.bin |
| `So you're not sure.` | 2 | talk.bin · talk_select_select.bin |
| `So you're volunteering, then?` | 2 | talk.bin · talk_select_select.bin |
| `So, about Nanami-san...` | 2 | pause_message.bin · talk.bin |
| `So, if you'll have me...` | 2 | sound_auth.bin · talk.bin |
| `So...` | 2 | sound_auth.bin · talk.bin |
| `Soccer Ball` | 2 | asset_asset_name_judge.bin · item.bin |
| `Sofa` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Something like that.` | 2 | talk.bin · talk_select_select.bin |
| `Something wrong?` | 2 | auth.bin · sound_auth.bin |
| `Sorry...` | 2 | sound_auth.bin · talk.bin |
| `Sorry?` | 2 | auth.bin · talk.bin |
| `Sounds like a real bastard.` | 2 | pause_message.bin · talk.bin |
| `Space Harrier` | 2 | input_game_state.bin · manual.bin |
| `Speaker Type` | 2 | option.bin · ui_text.bin |
| `Special` | 2 | player_skill_category.bin · ui_text.bin |
| `Speed Demon` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Split` | 2 | msg.bin · ui_text.bin |
| `Squid` | 2 | complete_checklist.bin · item.bin |
| `Stamina` | 2 | player_point.bin · ui_text.bin |
| `Standard Darts` | 2 | item.bin · minigame_darts_dart_kind.bin |
| `Start / Change Perspective` | 2 | controller_guide.bin · input_action.bin |
| `Steel Knuckles` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Stereo` | 2 | option.bin · ui_text.bin |
| `Stop right there!` | 2 | auth.bin · sound_auth.bin |
| `Style Switch` | 2 | controller_guide.bin · input_action.bin |
| `sugiura` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Sugiura!` | 2 | auth.bin · sound_auth.bin |
| `Sugiura.` | 2 | auth.bin · sound_auth.bin |
| `Suguru Hanatani` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Sunglasses` | 2 | search_characteristic.bin · verification_todo_item.bin |
| `Sure, why not.` | 2 | sound_auth.bin · talk.bin |
| `Sure?` | 2 | pause_message.bin · talk.bin |
| `Surrender` | 2 | msg.bin · ui_text.bin |
| `Surround` | 2 | option.bin · ui_text.bin |
| `Suspicious Tiny Man` | 2 | minigame_stalking_mission.bin · talk_talker.bin |
| `Table` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Tactician` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Tadahisa Yoshida` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Tailing` | 2 | controller_guide.bin · input_game_state.bin |
| `Tak!` | 2 | auth.bin · sound_auth.bin |
| `Tak.` | 2 | auth.bin · sound_auth.bin |
| `Takahiko Shiomura` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Takefumi Hashimoto` | 2 | item.bin · minigame_stalking_mission.bin |
| `Takeshi Akagawa` | 2 | item.bin · side_case_side_case_request.bin |
| `Takeshi Hayashi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Talk` | 2 | access_type.bin · talk_select_select.bin |
| `Tanaka` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Tashiro` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Tatsuya Gamo` | 2 | caption.bin · item.bin |
| `Tatsuya Iguchi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Taunt / Discard Weapon` | 2 | controller_guide.bin · input_action.bin |
| `Taxi Robber` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Tell me.` | 2 | auth.bin · talk.bin |
| `Temperamental` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Tenderloin, medium.` | 2 | sound_auth.bin · talk_select_select.bin |
| `Tenkaichi Street` | 2 | map_place.bin · position_stage_warp.bin |
| `Tenkaichi Street Entrance` | 2 | map_place.bin · position_stage_warp.bin |
| `Teruichi Yuki` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Test 2` | 2 | mission_mission_kind.bin · search_param.bin |
| `Thanks again.` | 2 | sound_auth.bin · talk.bin |
| `Thanks for waiting, Yukko-san.` | 2 | pause_message.bin · talk.bin |
| `Thanks!` | 2 | sound_auth.bin · talk.bin |
| `Thanks. But how?` | 2 | pause_message.bin · talk.bin |
| `That is a problem indeed.` | 2 | talk.bin · talk_select_select.bin |
| `That sound about right?` | 2 | auth.bin · sound_auth.bin |
| `That was close...` | 2 | minigame_mahjong_string_npc.bin · sound_auth.bin |
| `That would be Aragaki.` | 2 | sound_auth.bin · talk.bin |
| `That would be problematic.` | 2 | talk.bin · talk_select_select.bin |
| `That's correct.` | 2 | auth.bin · sound_auth.bin |
| `That's terrible...` | 2 | pause_message.bin · talk.bin |
| `That's the plan.` | 2 | sound_auth.bin · talk.bin |
| `That's true...` | 2 | sound_auth.bin · talk.bin |
| `That's what I'm talking about!` | 2 | pause_message.bin · sound_auth.bin |
| `That's...` | 2 | auth.bin · talk.bin |
| `The Bird Takes Flight` | 2 | complete_checklist.bin · talk_category_title.bin |
| `The Circle of Law` | 2 | complete_checklist.bin · talk_category_title.bin |
| `The condor has left the nest.` | 2 | talk.bin · talk_select_select.bin |
| `The dealer wins.` | 2 | minigame_oichokabu_string_oichokabu.bin · talk.bin |
| `The fuck!?` | 2 | auth.bin · sound_auth.bin |
| `The hell?` | 2 | auth.bin · sound_auth.bin |
| `The Hermit of the Dragon's Palace, Iyama` | 2 | complete_checklist.bin · talk_category_title.bin |
| `The Mad Bomber Strikes` | 2 | item.bin · talk_category_title.bin |
| `The Mole (Suspect)` | 2 | evidence_item_to_update.bin · item.bin |
| `The Twisted Groper` | 2 | item.bin · talk_category_title.bin |
| `The Twisted Judge` | 2 | item.bin · talk_category_title.bin |
| `The Twisted Professor` | 2 | item.bin · talk_category_title.bin |
| `Theater Alley` | 2 | map_place.bin · position_stage_warp.bin |
| `Theater Avenue` | 2 | map_place.bin · position_stage_warp.bin |
| `Then my lips are sealed.` | 2 | pause_message.bin · talk.bin |
| `There he is.` | 2 | auth.bin · sound_auth.bin |
| `There we go.` | 2 | sound_auth.bin · talk.bin |
| `There's no doubt.` | 2 | auth.bin · sound_auth.bin |
| `There... I said it...` | 2 | sound_auth.bin · talk.bin |
| `Thick stubble` | 2 | search_characteristic.bin · verification_todo_item.bin |
| `This is the standard difficulty level.` | 2 | option.bin · title_root.bin |
| `Three Color Straight` | 2 | complete.bin · minigame_mahjong_string_yaku.bin |
| `Throw` | 2 | input_action.bin · ui_text.bin |
| `Thugs` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Thumb turn bypass` | 2 | controller_guide.bin · minigame_picking_job_picking_job.bin |
| `Tiara` | 2 | minigame_cabaret_island_coordinate_accessory_hair.bin · minigame_cabaret_island_coordinate_hair_style.bin |
| `To 1F` | 2 | access_type.bin · talk_select_select.bin |
| `To 2F` | 2 | access_type.bin · talk_select_select.bin |
| `To the rooftop` | 2 | access_type.bin · talk_select_select.bin |
| `Toggle Camera Height` | 2 | controller_guide.bin · input_action.bin |
| `Toggle Command Display` | 2 | controller_guide.bin · input_action.bin |
| `Toggle Street Names` | 2 | input_action.bin · ui_text.bin |
| `Tokunaga` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Tomioka` | 2 | minigame_picking_job_picking_job.bin · talk_talker.bin |
| `Tomioka-san, I tried your okonomiyaki.` | 2 | pause_message.bin · talk.bin |
| `Tonfa` | 2 | asset_asset_name_judge.bin · character_npc_soldier_name_group.bin |
| `Took you long enough.` | 2 | sound_auth.bin · talk.bin |
| `Top 100 Friends` | 2 | drone_message.bin · ui_text.bin |
| `Torahiko Hyodo` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Toru Hashiki (Victim)` | 2 | evidence_item_to_update.bin · item.bin |
| `Toshiaki Murakami` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Toshiro Kume (Victim)` | 2 | evidence_item_to_update.bin · item.bin |
| `Toshiyuki Iwama` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Toss pieces to determine who goes first.` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Total` | 2 | msg.bin · ui_text.bin |
| `Total Play Time:` | 2 | msg.bin · save_data_detail.bin |
| `Trash Can` | 2 | asset_asset_name_judge.bin · verification_survey_3d.bin |
| `Triple Ron` | 2 | minigame_mahjong_string_agari.bin · minigame_mahjong_string_mangan.bin |
| `True.` | 2 | auth.bin · sound_auth.bin |
| `Tsubasa` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Tsukino` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `Tsukumo` | 2 | talk_select_select.bin · talk_talker.bin |
| `Tuna` | 2 | complete_checklist.bin · item.bin |
| `Turn: ${num}` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Two Han Minimum` | 2 | minigame_mahjong_string_setting.bin · ui_text.bin |
| `Ueki` | 2 | character_npc_soldier_name_group.bin · minigame_picking_job_picking_job.bin |
| `Ugh...` | 2 | sound_auth.bin · talk.bin |
| `Uh huh.` | 2 | auth.bin · sound_auth.bin |
| `Uh-huh.` | 2 | sound_auth.bin · talk.bin |
| `Uh-huh...` | 2 | sound_auth.bin · talk.bin |
| `uketuke` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Um, excuse me.` | 2 | sound_auth.bin · talk.bin |
| `umazuki` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Unlocking Skills` | 2 | help.bin · manual.bin |
| `Unused Super Take Backs` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Up` | 2 | input_action.bin · minigame_cabaret_island_coordinate_hair_style.bin |
| `Up / Down Controls` | 2 | option.bin · ui_text.bin |
| `Ura-Dora` | 2 | minigame_mahjong_string_common.bin · ui_text.bin |
| `Use` | 2 | access_type.bin · talk_select_select.bin |
| `Use a Super Take Back?` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Use a Take Back?` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Use the 10-10-1 Charm?` | 2 | talk.bin · talk_select_select.bin |
| `Use The Basics of Shogi?` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Use the Lucky Hanafuda Card?` | 2 | talk.bin · talk_select_select.bin |
| `Use the Trips Yokan?` | 2 | talk.bin · talk_select_select.bin |
| `Use Turbo` | 2 | controller_guide.bin · input_action.bin |
| `Usui` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `View Hands` | 2 | minigame_hanafuda_string_hanafuda.bin · minigame_hanafuda_string_mainmenu.bin |
| `View Tutorial` | 2 | controller_guide.bin · input_action.bin |
| `Virtua Fighter 5 Final Showdown` | 2 | title_root.bin · ui_text.bin |
| `W-Wait!` | 2 | sound_auth.bin · talk.bin |
| `W-Well...` | 2 | auth.bin · talk.bin |
| `Wager` | 2 | minigame_hanafuda_string_hanafuda.bin · player_point.bin |
| `Wait` | 2 | access_type.bin · talk_select_select.bin |
| `Wait until the turn order is decided.` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Wait!` | 2 | auth.bin · sound_auth.bin |
| `Wait, really?` | 2 | sound_auth.bin · talk.bin |
| `Wait, what!?` | 2 | sound_auth.bin · talk.bin |
| `Wait...` | 2 | sound_auth.bin · talk.bin |
| `Waku's Autopsy Report` | 2 | evidence_item_to_update.bin · item.bin |
| `Waku's Hospital Room: Window` | 2 | evidence_item_to_update.bin · item.bin |
| `Want me to call you a taxi?` | 2 | talk.bin · talk_select_select.bin |
| `Was I wrong?` | 2 | pause_message.bin · talk.bin |
| `We should see how this plays out.` | 2 | talk.bin · talk_select_select.bin |
| `Weak Attack / Rush Combo` | 2 | controller_guide.bin · input_action.bin |
| `Weak Point Striker` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Welcome, sir.` | 2 | sound_auth.bin · talk.bin |
| `Well then, I'll be off now.` | 2 | sound_auth.bin · talk.bin |
| `Well-rounded` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Well... I suppose.` | 2 | auth.bin · talk.bin |
| `Were you quiet as a child?` | 2 | talk.bin · talk_select_select.bin |
| `West Shichifuku Street` | 2 | map_place.bin · position_stage_warp.bin |
| `Wette Kitchen (W Taihei Blvd.)` | 2 | map_place.bin · shop.bin |
| `What a bunch of jerks.` | 2 | talk.bin · talk_select_select.bin |
| `What about me?` | 2 | talk.bin · talk_select_select.bin |
| `What about the last guy you dated?` | 2 | talk.bin · talk_select_select.bin |
| `What are you doing here?` | 2 | auth.bin · talk.bin |
| `What are you doing?` | 2 | auth.bin · talk.bin |
| `What are you talking about?` | 2 | auth.bin · talk.bin |
| `What can you contribute to our company?` | 2 | talk.bin · talk_select_select.bin |
| `What do you mean...?` | 2 | sound_auth.bin · talk.bin |
| `What does that have to do with anything?` | 2 | pause_message.bin · talk.bin |
| `What happened to her?` | 2 | pause_message.bin · talk.bin |
| `What happened?` | 2 | sound_auth.bin · talk.bin |
| `What kind of men do you like?` | 2 | talk.bin · talk_select_select.bin |
| `What makes you say that?` | 2 | sound_auth.bin · talk.bin |
| `What should I do?` | 2 | talk.bin · talk_popup_popup.bin |
| `What the!?` | 2 | sound_auth.bin · talk.bin |
| `What the...` | 2 | auth.bin · sound_auth.bin |
| `What! Really!?` | 2 | pause_message.bin · talk.bin |
| `What! Really?` | 2 | pause_message.bin · talk.bin |
| `What's going on, Amane-san?` | 2 | pause_message.bin · talk.bin |
| `What's wrong?` | 2 | sound_auth.bin · talk.bin |
| `What's your name?` | 2 | auth.bin · sound_auth.bin |
| `What? I can't do that...` | 2 | pause_message.bin · talk.bin |
| `What? Why?` | 2 | sound_auth.bin · talk.bin |
| `Where's Murase?` | 2 | sound_auth.bin · talk_select_select.bin |
| `Where's the girl?` | 2 | sound_auth.bin · talk_select_select.bin |
| `Which is what?` | 2 | auth.bin · sound_auth.bin |
| `Which means...` | 2 | sound_auth.bin · talk.bin |
| `Who is he?` | 2 | sound_auth.bin · talk.bin |
| `Who the hell are you!?` | 2 | sound_auth.bin · talk.bin |
| `Who the hell are you?` | 2 | auth.bin · sound_auth.bin |
| `Who?` | 2 | auth.bin · sound_auth.bin |
| `Whoa!` | 2 | sound_auth.bin · talk.bin |
| `Whoa.` | 2 | sound_auth.bin · talk.bin |
| `Whoa. You're gonna tell me after all?` | 2 | pause_message.bin · talk.bin |
| `Why didn't you tell me?` | 2 | talk.bin · talk_select_select.bin |
| `Why don't we play some darts?` | 2 | pause_message.bin · talk.bin |
| `Why thank you.` | 2 | pause_message.bin · talk.bin |
| `Why wouldn't I be?` | 2 | talk.bin · talk_select_select.bin |
| `Why!?` | 2 | auth.bin · sound_auth.bin |
| `Wild Jackson` | 2 | complete_group.bin · qsearch_search.bin |
| `Wild Jackson (E Millennium Tower St.)` | 2 | map_place.bin · shop.bin |
| `Wild Jackson (Tenkaichi St.)` | 2 | map_place.bin · shop.bin |
| `Will do!` | 2 | sound_auth.bin · talk.bin |
| `Will you feed me something?` | 2 | talk.bin · talk_select_select.bin |
| `Wind Discard Draw` | 2 | minigame_mahjong_string_agari.bin · minigame_mahjong_string_mangan.bin |
| `Woman with Glasses` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `World Rank Top 100` | 2 | drone_message.bin · ui_text.bin |
| `Would you be comfortable dating her?` | 2 | pause_message.bin · talk.bin |
| `Wow.` | 2 | sound_auth.bin · talk.bin |
| `Wow...` | 2 | sound_auth.bin · talk.bin |
| `Wristwatch` | 2 | minigame_cabaret_island_coordinate_accessory_category.bin · verification_survey_3d.bin |
| `x ${value}` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `yagami` | 2 | character_character_data.bin · character_character_data_judge.bin |
| `Yagami` | 2 | player.bin · talk_talker.bin |
| `Yagami Detective Agency: Out Run` | 2 | help.bin · manual.bin |
| `Yagami Detective Agency: Records` | 2 | help.bin · manual.bin |
| `Yagami Detective Agency: Side Cases` | 2 | help.bin · manual.bin |
| `Yagami-san! Are you okay!?` | 2 | sound_auth.bin · talk.bin |
| `Yagami-san. Do you really like Nanami?` | 2 | pause_message.bin · talk.bin |
| `Yagami-sensei.` | 2 | auth.bin · sound_auth.bin |
| `Yagami.` | 2 | auth.bin · sound_auth.bin |
| `Yakuman` | 2 | minigame_mahjong_string_mangan.bin · minigame_mahjong_string_yakuman.bin |
| `Yamada` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Yao` | 2 | character_npc_soldier_name_group.bin · drone_enemy_division2.bin |
| `Yasuaki Onishi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Yasumitsu Izumi` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Yeah!` | 2 | sound_auth.bin · talk.bin |
| `Yeah, but...` | 2 | sound_auth.bin · talk.bin |
| `Yeah, I did.` | 2 | pause_message.bin · talk.bin |
| `Yeah, I do.` | 2 | talk.bin · talk_select_select.bin |
| `Yeah, I guess so.` | 2 | talk.bin · talk_select_select.bin |
| `Yeah, I promise.` | 2 | talk.bin · talk_select_select.bin |
| `Yeah, I would say so.` | 2 | pause_message.bin · talk.bin |
| `Yeah, I'll be careful.` | 2 | pause_message.bin · talk.bin |
| `Yeah, I'm good.` | 2 | auth.bin · talk_select_select.bin |
| `Yeah, let's do it.` | 2 | pause_message.bin · sound_auth.bin |
| `Yeah, what about it?` | 2 | sound_auth.bin · talk.bin |
| `Yeah, you got that right.` | 2 | auth.bin · sound_auth.bin |
| `Yeah, you look cute.` | 2 | talk.bin · talk_select_select.bin |
| `Yellow Wristwatch` | 2 | verification_survey_3d.bin · verification_todo_item.bin |
| `Yes!` | 2 | minigame_mahjong_string_npc.bin · talk.bin |
| `Yes, sir!` | 2 | auth.bin · sound_auth.bin |
| `Yes. Please do.` | 2 | pause_message.bin · talk.bin |
| `Yo.` | 2 | auth.bin · sound_auth.bin |
| `Yoji Shono` | 2 | caption.bin · evidence_item_to_update.bin |
| `Yoshikazu Saito` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `Yosuke` | 2 | talk_talker.bin · verification_survey_3d.bin |
| `You are the dealer.` | 2 | minigame_hanafuda_string_hanafuda.bin · minigame_oichokabu_string_oichokabu.bin |
| `You bastard...` | 2 | sound_auth.bin · talk.bin |
| `You don't say...` | 2 | sound_auth.bin · talk.bin |
| `You don't think so?` | 2 | pause_message.bin · talk.bin |
| `You ever been mooned?` | 2 | sound_auth.bin · talk_select_select.bin |
| `You go <color=red>first</color>.` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |
| `You got a minute?` | 2 | sound_auth.bin · talk.bin |
| `You little!` | 2 | auth.bin · sound_auth.bin |
| `You okay?` | 2 | sound_auth.bin · talk.bin |
| `You really are creative, aren't you...` | 2 | pause_message.bin · talk.bin |
| `You really don't want to know?` | 2 | pause_message.bin · talk.bin |
| `You really think so?` | 2 | auth.bin · talk.bin |
| `You sure about that?` | 2 | pause_message.bin · talk.bin |
| `You think?` | 2 | auth.bin · sound_auth.bin |
| `You thought up something else?` | 2 | pause_message.bin · talk.bin |
| `You want to just call it a day?` | 2 | talk.bin · talk_select_select.bin |
| `You were gonna complain about work.` | 2 | sound_auth.bin · talk_select_select.bin |
| `You were gonna confess, right?` | 2 | sound_auth.bin · talk_select_select.bin |
| `You'd do that?` | 2 | auth.bin · talk.bin |
| `You're in your twenties, right?` | 2 | talk.bin · talk_select_select.bin |
| `You're never gonna find the Mole.` | 2 | auth.bin · sound_auth.bin |
| `You're not getting away!` | 2 | auth.bin · sound_auth.bin |
| `You're not saying...` | 2 | pause_message.bin · talk.bin |
| `You're serious?` | 2 | pause_message.bin · talk.bin |
| `You're wrong!` | 2 | auth.bin · sound_auth.bin |
| `You're...` | 2 | auth.bin · talk.bin |
| `Young Janitor` | 2 | character_npc_soldier_name_group.bin · talk_talker.bin |
| `Your homeboy's calling for you.` | 2 | talk.bin · talk_select_select.bin |
| `Your inventory is full.` | 2 | msg.bin · ui_text.bin |
| `Your point being?` | 2 | auth.bin · sound_auth.bin |
| `Your Points` | 2 | minigame_hanafuda_string_hanafuda.bin · player_point.bin |
| `Your Total Points` | 2 | minigame_mahjong_string_common.bin · ui_text.bin |
| `Yusuke` | 2 | item.bin · talk_talker.bin |
| `Zenji Watanabe` | 2 | minigame_shogi_menu.bin · minigame_shogi_shogi.bin |

## คีย์สั้นในคิว TALK ที่ผู้พูดไม่ใช่คนเดียว (เพิ่ม 21 ส.ค. 2026)

คีย์เหล่านี้อยู่ bin เดียว (`talk.bin`) จึงไม่ติดตะแกรง multibin ปกติ แต่ **ถูกพูดโดยหลายคนในตารางเดียวกัน**
(ฟิลด์ `dupes` ของ `extracted/facts/talk_speaker.json`) → คำแปลต้อง **ไม่ผูกเพศ** ใช้ได้ทุกฝั่ง

| คีย์ | ตาราง | ใครพูดบ้าง | รูปที่ใช้ |
|---|---|---|---|
| `R-Right.` | `judge_friend_g04` | นานามิ · ยากามิ | **ถ-ถูกต้อง** (ตามรูปที่ ship แล้วของ `R-Right...`) |
| `...Hmm.` | `judge_friend_g04` / `judge_friend_a49` | นานามิ · Ryo (เพศ unknown) | **...อืม** |
