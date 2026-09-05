# ข้อเท็จจริงจากไฟล์เกม Judgment — สำหรับทีมวิจัย/นักแปล

> สร้างด้วย `python scripts/make_translator_facts.py` จาก JSON ที่แตกไว้แล้ว
> (`extracted/db_en/en/*.bin.json`) · ข้อมูลดิบรายหมวดอยู่ที่ `extracted/facts/*.json`

**กติกาการใช้**: ข้อมูลในไฟล์นี้คือ *ของจริงจากเกม* — ถ้าขัดกับ wiki ให้เชื่อไฟล์นี้
และจดความขัดแย้งไว้ในรายงาน (บทเรียน K3: wiki ผิดเรื่องชื่อบท/สังกัด/บทบาทบ่อย)

## หมวดข้อมูลที่ดึงมาแล้ว

| หมวด | ไฟล์ต้นทาง | รายการ | คำอธิบาย |
|---|---|---|---|
| `speakers` | `talk_talker.bin` | 473 | ชื่อผู้พูดทั้งหมด (key = ชื่อญี่ปุ่นในไฟล์ · `talk_talker` = ชื่อที่โชว์บนจอ EN) |
| `chapters` | `title_movie_chapter.bin` | 13 | ชื่อบท (main story + Majima Saga) |
| `missions` | `mission_mission_kind.bin` | 550 | ภารกิจ/คดี — ทั้ง Main Case, Side Case และงานย่อย |
| `friends` | `character_friend_list.bin` | 54 | ระบบเพื่อน (Friends) — ชื่อ + คำอธิบายของแต่ละคน |
| `skills` | `player_skill.bin` | 126 | สกิลของยากามิ (ชื่อ + คำอธิบาย + เงื่อนไขปลดล็อก) |
| `items` | `item.bin` | 1071 | ไอเทม/แฟ้มคดี/ของสะสม (ชื่อ + คำอธิบาย) |
| `evidence` | `evidence_item_to_update.bin` | 103 | ประวัติบุคคล/หลักฐานที่อัปเดตตามเนื้อเรื่อง |
| `complete` | `complete.bin` | 499 | รายการ completion (ชี้ว่ามี side content อะไรบ้าง) |
| `complete_checklist` | `complete_checklist.bin` | 20 | หมวดของ completion list |
| `popup_names` | `character_npc_popup_text.bin` | 369 | ป้ายชื่อ NPC ที่เด้งขึ้นบนจอ |
| `npc_names` | `character_npc_soldier_name_group.bin` | 8 | ชื่อกลุ่ม NPC ทั่วเมือง |
| `scenario_summary` | `scene_scenario_explanation.bin` | 62 | สรุปเนื้อเรื่องย่อของแต่ละตอน (ในเกม) |
| `help` | `help.bin` | 153 | หัวข้อ help — ชี้ระบบทั้งหมดที่เกมมี |
| `manual` | `manual.bin` | 200 | คู่มือในเกม (กติกามินิเกมทั้งหมด) |
| `ui_text` | `ui_text.bin` | 1164 | ข้อความ UI รวม |
| `talk_select` | `talk_select_select.bin` | 535 | ตัวเลือกบทสนทนา |
| `trophy` | `trophy.bin` | 47 | ถ้วยรางวัล (สปอยล์โครงเรื่องระดับหยาบ) |
| `places` | `map_place.bin` | 182 | สถานที่ในเมือง (ชื่อ + คำบรรยาย) |
| `complete_group` | `complete_group.bin` | 34 | หมวดของ completion list |
| `shops` | `shop.bin` | 46 | ร้านค้าในเมือง |

## รายชื่อผู้พูดที่มีชื่อแสดงผลภาษาอังกฤษ (473 จาก 473 แถว)

ครบทุกชื่อ — ทีมตัวละครต้องครอบคลุมให้หมด (หลักเดียวกับ K3: main + side ต้องรวมกันได้เท่านี้)

| # | ชื่อในไฟล์ (JA) | ชื่อที่โชว์บนจอ (EN) |
|---|---|---|
| 1 | テスト | Test |
| 2 | 八神 | Yagami |
| 3 | judge_ガラの悪い男 | Rude Dude |
| 4 | judge_男性客 | Male Customer |
| 5 | judge_女性客 | Female Customer |
| 6 | judge_女 | Woman |
| 7 | player | Player |
| 8 | judge_葉山 | Hayama |
| 9 | judge_志島 | Shijima |
| 10 | judge_マスコミ | Mass Media |
| 11 | judge_ファン | Fan |
| 12 | judge_星野 | Hoshino |
| 13 | judge_さおり | Saori |
| 14 | judge_源田 | Genda |
| 15 | judge_雨宮 | Amamiya |
| 16 | judge_いい年のチンピラ | Grown-ass Thug |
| 17 | judge_寺原 | Terahara |
| 18 | judge_極道風の男 | Yakuza-esque Man |
| 19 | judge_若い女性客 | Young Female Customer |
| 20 | judge_若い男性客 | Young Male Customer |
| 21 | judge_ワン | Wang |
| 22 | judge_黒服の男 | Man in Black |
| 23 | judge_禿頭の男 | Undercut Mafioso |
| 24 | judge_ツァンシィ | Zhuang Shi |
| 25 | judge_店長 | Manager |
| 26 | judge_牧原 | Makihara |
| 27 | judge_むろた | Azuma |
| 28 | judge_イケイケなチンピラ | Exuberant Thug |
| 29 | judge_セクシー美女 | Gorgeous Girl |
| 30 | judge_タクシー運転手 | Taxi Driver |
| 31 | judge_ぷりん | Pudding |
| 32 | judge_解放された男 | Released Man |
| 33 | judge_海藤 | Kaito |
| 34 | judge_強引なチンピラ | Pushy Punk |
| 35 | judge_助けを求める声 | Cry for Help |
| 36 | judge_田口紀子 | Noriko Taguchi |
| 37 | judge_陽気なチンピラ | Peppy Punk |
| 38 | judge_テンダーマスター | Jo Masuda |
| 39 | judge_徳永 | Tokunaga |
| 40 | judge_小学生男子 | Elementary Student |
| 41 | judge_巨漢のヤクザ | Large Yakuza |
| 42 | judge_さな | Sana |
| 43 | judge_西東 | Saito |
| 44 | judge_ガラ悪部下１ | Uncivil Underling |
| 45 | judge_ガラ悪部下２ | Meddling Minion |
| 46 | judge_ガラ悪部下３ | Foul-mannered Flunky |
| 47 | judge_ガラ悪部下４ | Loutish Lackey |
| 48 | judge_太田 | Ota |
| 49 | judge_綱渡 | Tsunawatari |
| 50 | judge_北村 | Kitamura |
| 51 | judge_ファン一同 | Fans |
| 52 | judge_ＯＬ | Office Lady |
| 53 | judge_達郎 | Tatsuro |
| 54 | judge_直子 | Naoko |
| 55 | judge_？？？_真冬 | ??? |
| 56 | judge_？？？_達郎 | ??? |
| 57 | judge_蒲生 | Gamo |
| 58 | judge_金髪の男 | Blonde Man |
| 59 | judge_背の高い男 | Tall Man |
| 60 | judge_不良風の少年 | Uncouth Youth |
| 61 | judge_熟練刑事 | Veteran Detective |
| 62 | judge_ニュースキャスター | Newscaster |
| 63 | judge_島津 | Shimazu |
| 64 | judge_由香子 | Yukako |
| 65 | judge_長谷川 | Hasegawa |
| 66 | judge_黒髪の女 | Black-haired Lady |
| 67 | judge_日向 | Hyuga |
| 68 | judge_平沼 | Hiranuma |
| 69 | judge_ハンチングの男 | Hunting Man |
| 70 | judge_明日香 | Asuka |
| 71 | judge_パンツルックの女性 | Lady with Suave Pants |
| 72 | judge_メガネの女性 | Woman with Glasses |
| 73 | judge_日暮 | Higurashi |
| 74 | judge_真冬 | Mafuyu |
| 75 | judge_川田 | Kawada |
| 76 | judge_片桐 | Katagiri |
| 77 | judge_司会者 | Host |
| 78 | judge_那須川 | Nasugawa |
| 79 | judge_小柄な男 | Small Man |
| 80 | judge_冨岡 | Tomioka |
| 81 | judge_大畑 | Ohata |
| 82 | judge_歩 | Ayumu |
| 83 | judge_強面の男 | Tough Guy |
| 84 | judge_小野寺 | Onodera |
| 85 | judge_金の皿な店員 | Gold Plate Employee |
| 86 | judge_銀の皿な店員 | Silver Plate Employee |
| 87 | judge_銅の皿な店員 | Bronze Plate Employee |
| 88 | judge_鉄の皿な店員 | Steel Plate Employee |
| 89 | judge_コンビニ店員 | Convenience Store Clerk |
| 90 | judge_猫缶店員 | Cat Food Aficionado |
| 91 | judge_爆弾犯 | The Mad Bomber |
| 92 | judge_？？？_爆弾犯 | ??? |
| 93 | judge_コンビニ店員_爆弾犯 | Convenience Store Clerk |
| 94 | judge_迷子の少年 | Lost Boy |
| 95 | judge_迷子の少年の母 | Lost Boy's Mother |
| 96 | judge_サラリーマン風の通行人 | Commuting Businessman |
| 97 | judge_学生風の通行人 | Strolling Student |
| 98 | judge_ホスト風の通行人 | Meandering Host |
| 99 | judge_ツクモ | Tsukumo |
| 100 | judge_目黒 | Meguro |
| 101 | judge_キャッチの若者 | Young Barker |
| 102 | judge_ぼったくりバーの男 | Man from the Rip-off Bar |
| 103 | judge_黒服のチンピラ | Black-suited Hooligan |
| 104 | judge_白服のチンピラ | White-suited Hooligan |
| 105 | judge_魚住 | Uozumi |
| 106 | judge_マミ | Mami |
| 107 | judge_アリス | Alice |
| 108 | judge_若女将 | Young Woman |
| 109 | judge_三木 | Miki |
| 110 | judge_法橋 | Hohashi |
| 111 | judge_給仕係 | Server |
| 112 | judge_陽介 | Yosuke |
| 113 | judge_月乃 | Tsukino |
| 114 | judge_小野上 | Panty Professor |
| 115 | judge_ルマルシェ店員 | Le Marche Employee |
| 116 | judge_警察 | Police |
| 117 | judge_諸星 | Moroboshi |
| 118 | judge_ホームレス近藤 | Homeless Kondo |
| 119 | judge_ホームレス浜中 | Homeless Hamanaka |
| 120 | judge_ホームレス村尾 | Homeless Murao |
| 121 | judge_ホームレス寺岡 | Homeless Teraoka |
| 122 | judge_ホームレス福原 | Homeless Fukuhara |
| 123 | judge_マッチョな男 | Muscular Man |
| 124 | judge_松崎 | Matsuzaki |
| 125 | judge_シュウ | Xiu |
| 126 | judge_食い逃げ犯 | Dine-and-Dasher |
| 127 | judge_竹蜜店長 | Takemitsu Owner |
| 128 | judge_みかじめ兄貴分 | Shakedown Superior |
| 129 | judge_みかじめ弟分 | Shakedown Subordinate |
| 130 | judge_ノリカ | Norika |
| 131 | judge_ノリカの父 | Norika's Dad |
| 132 | judge_ノリカの母 | Norika's Mom |
| 133 | judge_若いチンピラ01 | Young Thug |
| 134 | judge_若いチンピラ02 | Juvenile Delinquent |
| 135 | judge_若いチンピラ03 | Fledgling Hoodlum |
| 136 | judge_九州一番星店長 | Kyushu No. 1 Star Owner |
| 137 | judge_グルメ気取りの大学生 | Self-professed Foodie |
| 138 | judge_小洒落た大学生 | Fancypants Freshman |
| 139 | judge_則本 | Norimoto |
| 140 | judge_美晴 | Miharu |
| 141 | judge_キム | Kim |
| 142 | judge_韓来店長 | Kanrai Owner |
| 143 | judge_赤川 | Akagawa |
| 144 | judge_くたびれた中年 | Weary Middle-aged Man |
| 145 | judge_金髪の若者 | Young Blonde Guy |
| 146 | judge_長髪の若者 | Long-haired Loafer |
| 147 | judge_気さくなキャッチ | Outgoing Barker |
| 148 | judge_背の低いホームレス | Diminutive Vagabond |
| 149 | judge_川崎 | Kawasaki |
| 150 | judge_タクシー強盗 | Taxi Robber |
| 151 | judge_トム | Judge Creep 'n Peep |
| 152 | judge_畑野 | Hatano |
| 153 | judge_吉田支配人 | Yoshida Owner |
| 154 | judge_外国人旅行客 | Tourist from Overseas |
| 155 | judge_バンタムマスター | Bantam Owner |
| 156 | judge_若い男性 | Young Man |
| 157 | judge_若い女性 | Young Women |
| 158 | judge_ハットン | Hutton |
| 159 | judge_古谷 | Furuya |
| 160 | judge_猪瀬 | Inose |
| 161 | judge_稲光 | Shun |
| 162 | judge_めぐみ | Megumi |
| 163 | judge_丘 | Oka |
| 164 | judge_武文 | Takefumi |
| 165 | judge_マリ姉の友達 | Mari's Friend |
| 166 | judge_サラリーマン風の男 | Businessman |
| 167 | judge_マリ姉 | Mari |
| 168 | judge_本山 | Ass Catchem |
| 169 | judge_月乃の声 | Voice of Tsukino |
| 170 | judge_女の悲鳴 | Female Scream |
| 171 | judge_変態 | Pervert |
| 172 | judge_Ｇ．Ｉ | G.I. |
| 173 | judge_石川 | Ishikawa |
| 174 | judge_クロウ | Crow |
| 175 | judge_のろま警官 | Dopey Cop |
| 176 | judge_窃盗団のファン | Burglary Ring Supporter |
| 177 | judge_ノウメン | Man in Noh Mask |
| 178 | judge_フォックス | Fox |
| 179 | judge_マスケラ | Mascara |
| 180 | judge_緋山 | Hiyama |
| 181 | judge_真面目な警官 | Serious Cop |
| 182 | judge_ドウェイン | Dwayne |
| 183 | judge_清四郎 | Kiyoshiro |
| 184 | judge_えびす屋店長・福津 | Fukutsu |
| 185 | judge_相良 | Sagara |
| 186 | judge_志津絵 | Shizue |
| 187 | judge_南 | Minami |
| 188 | judge_平澤 | Hirasawa |
| 189 | judge_幸次郎 | Kojiro |
| 190 | judge_桐子 | Kiriko |
| 191 | judge_文江 | Fumie |
| 192 | judge_出口 | Deguchi |
| 193 | judge_セイヤ | Seiya |
| 194 | judge_パンチパーマの男 | Blond-haired Yakuza |
| 195 | judge_西村 | Nishimura |
| 196 | judge_小野ミチオ | Ono Michio |
| 197 | judge_広中 | Hironaka |
| 198 | judge_稲峰 | Inamine |
| 199 | judge_金田 | Kaneda |
| 200 | judge_大浦 | Daisuke |
| 201 | judge_熊倉 | Kumakura |
| 202 | judge_子供 | Child |
| 203 | judge_男子高校生 | Highschooler |
| 204 | judge_赤牛丸店員 | Akaushimaru Employee |
| 205 | judge_喫茶アルプス店員 | Café Alps Employee |
| 206 | judge_亜天使店員 | Mama |
| 207 | judge_バンタム店員 | Bantam Staff |
| 208 | judge_ドン・キホーテ店員 | Don Quijote Clerk |
| 209 | judge_えびすや店員 | Ebisu Pawn Employee |
| 210 | judge_富士そば店員 | Fuji Soba Employee |
| 211 | judge_銀だこハイボール酒場店員 | Gindaco Highball Tavern Employee |
| 212 | judge_韓来店員 | Kanrai Employee |
| 213 | judge_九州一番星店員 | Kyushu No. 1 Star Owner |
| 214 | judge_いきなり！ステーキ店員 | Ikinari Steak Employee |
| 215 | judge_ＰＯＰＰＯ店員 | Poppo Employee |
| 216 | judge_リンガーハット店員 | Ringer Hut Staff |
| 217 | judge_シェラック店員 | Shellac Employee |
| 218 | judge_スマイルバーガー店員 | Smile Burger Employee |
| 219 | judge_寿司吟店員 | Sushi Gin Owner |
| 220 | judge_すしざんまい店員 | Sushi Zanmai Employee |
| 221 | judge_ヴェッテキッチン店員 | Wette Kitchen Employee |
| 222 | judge_ワイルドジャクソン店員 | Wild Jackson Employee |
| 223 | judge_養老乃瀧店員 | Yoronotaki Staff |
| 224 | judge_早乙女誠也 | Seiya Saotome |
| 225 | judge_ル・マルシェ店員 | Le Marche Employee |
| 226 | judge_田代 | Tashiro |
| 227 | judge_スーツ姿のヤクザ | Dapper Yakuza |
| 228 | judge_エメラルド・ヒルズの黒服 | Emerald Hills Employee |
| 229 | judge_猫宮 | Nekomiya |
| 230 | judge_猫好きＯＬ | Cat-loving Lady |
| 231 | judge_飯田 | Ida |
| 232 | judge_小湊 | Kominato |
| 233 | judge_いい尻の女 | Voluptuous Woman |
| 234 | judge_蒼太 | Sota |
| 235 | judge_王将店員 | King Employee |
| 236 | judge_謎の人物 | Mysterious Man |
| 237 | judge_M SIDE CAFE店員 | M Side Cafe Employee |
| 238 | judge_QUADRA店員 | Quadra Garden Employee |
| 239 | judge_玲 | Rei |
| 240 | judge_清掃員の青年 | Young Janitor |
| 241 | judge_伊勢谷 | Iseya |
| 242 | judge_七海 | Nanami |
| 243 | judge_竹田 | Takeda |
| 244 | judge_竹田の声 | Takeda's Voice |
| 245 | judge_案内役 | Staff |
| 246 | judge_交換役 | Exchanger |
| 247 | judge_カジノ店員 | Casino Employee |
| 248 | judge_カラオケ店員 | Karaoke Employee |
| 249 | judge_将棋好きの男 | Shogi Lover |
| 250 | judge_ディーラー | Dealer |
| 251 | judge_謎の人物_sida45 | Mysterious Man |
| 252 | judge_浅野 | Asano |
| 253 | judge_若い店員 | Young Chef |
| 254 | judge_釣り堀受付 | Koi Bride Owner |
| 255 | judge_小山田 | Oyamada |
| 256 | judge_妙恵子 | Taeko |
| 257 | judge_若原 | Wakahara |
| 258 | judge_シン | Shin |
| 259 | judge_謎の男 | Unknown Man |
| 260 | judge_ユースケ | Yusuke |
| 261 | judge_慎太郎 | Shintaro |
| 262 | judge_石村 | Ishimura |
| 263 | judge_小柄なヤクザ | Thin Yakuza |
| 264 | judge_大柄なヤクザ | Burly Yakuza |
| 265 | judge_足立 | Adachi |
| 266 | judge_若い男 | Young Man |
| 267 | judge_中年の男 | Middle-aged Man |
| 268 | judge_田中（偽） | Tanaka |
| 269 | judge_side17コンビニ店員 | Convenience Store Clerk |
| 270 | judge_？_田中 | ? |
| 271 | judge_田中？ | Tanaka? |
| 272 | judge_稲本 | Inamoto |
| 273 | judge_田中（本物） | Tanaka |
| 274 | judge_森宮 | Morimiya |
| 275 | judge_名も無き棋士 | Nameless Shogi Player |
| 276 | judge_ドローンレース受付 | Drone Race Receptionist |
| 277 | judge_取り巻きA | Trifling Minion |
| 278 | judge_取り巻きB | Nugatory Minion |
| 279 | judge_通行人A | Random Passerby |
| 280 | judge_通行人B | Extraneous Passerby |
| 281 | judge_？？？_ダイヤモンド | ??? |
| 282 | judge_？？？ | ??? |
| 283 | judge_さまよえる老人 | ??? |
| 284 | judge_ライアン | Ryan |
| 285 | judge_ロングヘアの女 | Long-haired Woman |
| 286 | judge_ロンゲのホスト | Blond-haired Host |
| 287 | judge_臆病そうな青年 | Cowardly Youth |
| 288 | judge_怪しい小男 | Suspicious Tiny Man |
| 289 | judge_葛西 | Kasai |
| 290 | judge_飢える少年 | Hungry Boy |
| 291 | judge_京浜同盟のチンピラ | Keihin Gang Thug |
| 292 | judge_怯えた学生 | Scared Student |
| 293 | judge_金髪の女 | Blonde Woman |
| 294 | judge_軽薄そうな若者 | Superficial Stripling |
| 295 | judge_虎牙 | Koga |
| 296 | judge_慌てる男性 | Panicking Man |
| 297 | judge_阪木葉 | Sakakiba |
| 298 | judge_真面目そうな若者 | Determined Young Man |
| 299 | judge_全員 | Everyone |
| 300 | judge_太めのチンピラ | Thick-boned Thug |
| 301 | judge_大林 | Obayashi |
| 302 | judge_短髪の男 | Short-haired Man |
| 303 | judge_地味な大学生 | Unassuming Undergrad |
| 304 | judge_田名後 | Tanago |
| 305 | judge_怒れるＯＬ | Timid Secretary |
| 306 | judge_派手な女 | Ostentatious Woman |
| 307 | judge_博識ぶった学生 | Snobby Student |
| 308 | judge_本田 | Honda |
| 309 | judge_亮 | Ryo |
| 310 | judge_建山 | Tateyama |
| 311 | judge_ダンディな中年男性 | Suave Gentleman |
| 312 | judge_気さくな青年 | Easygoing Youngster |
| 313 | judge_陽気なマダム | Mirthful Madam |
| 314 | judge_チンピラ | Thugs |
| 315 | judge_あおい | Aoi |
| 316 | judge_砂田 | Sunada |
| 317 | judge_藤永 | Fujinaga |
| 318 | judge_気さくな若者 | Friendly Young Guy |
| 319 | judge_一同 | All |
| 320 | judge_辰夫 | Tatsuo |
| 321 | judge_真紀 | Maki |
| 322 | judge_ツバサ | Tsubasa |
| 323 | judge_金髪のホスト | Blonde Host |
| 324 | judge_見物客 | Onlooker |
| 325 | judge_挑戦者 | Challenger |
| 326 | judge_ミジョーレ店員 | Mijore Employee |
| 327 | judge_ららばい店員 | Lullaby Employee |
| 328 | judge_近代麻雀店員 | Modern Mahjong Employee |
| 329 | judge_麻雀客 | Mahjong Customer |
| 330 | judge_楓 | Kaede |
| 331 | judge_クラブセガ店員 | Club Sega Employee |
| 332 | judge_ラ・マン店員 | L'Amant Employee |
| 333 | judge_花梨 | Karin |
| 334 | judge_仁 | Jin |
| 335 | judge_あずさ | Azusa |
| 336 | judge_及川 | Oikawa |
| 337 | judge_受付の老人 | Old Receptionist |
| 338 | judge_ちゃらい若者 | Frivolous Young Man |
| 339 | judge_太めの主婦 | Thick Housewife |
| 340 | judge_新谷 | Shintani |
| 341 | judge_ダイキュー受付 | Dice & Cube Receptionist |
| 342 | judge_加畑 | Kabata |
| 343 | judge_平凡な高校生 | Ordinary Highschooler |
| 344 | judge_凡庸な高校生 | Normal Highschooler |
| 345 | judge_すごろくチンピラ | Thugs |
| 346 | judge_すごろくキャバ嬢 | Hostess |
| 347 | judge_六角彩 | Naisu Daisu |
| 348 | judge_ころにゃん | Koro-nyan |
| 349 | judge_シャルル受付 | Charles Receptionist |
| 350 | judge_？？？_窃盗団のファン | ??? |
| 351 | judge_麻美 | Asami |
| 352 | judge_紀子の旦那 | Noriko's Husband |
| 353 | judge_スナックのママ | Woman |
| 354 | judge_キャッチ | Barker |
| 355 | judge_ホームレス | Homeless Man |
| 356 | judge_あまね | Amane |
| 357 | judge_地味な学生 | Unremarkable Student |
| 358 | judge_怪しい学生 | Suspicious Student |
| 359 | judge_若いチンピラ | Young Thug |
| 360 | judge_牛又 | Ushimata |
| 361 | judge_ゆっこ | Yukko |
| 362 | judge_アキラ | Akira |
| 363 | judge_竜禅寺 | Ryuzenji |
| 364 | judge_幸川 | Yukikawa |
| 365 | judge_ヒヤマ | Hiyama |
| 366 | judge_イヤマ | Iyama |
| 367 | judge_肥塚 | Koizuka |
| 368 | judge_中年キャッチ | Middle-aged Barker |
| 369 | judge_若いキャッチ | Young Barker |
| 370 | judge_あっぷるぱい店員 | Apple Pie Employee |
| 371 | judge_あっこ | Lady in a Fancy Dress |
| 372 | judge_まどか | Madoka |
| 373 | judge_釜口 | Kamaguchi |
| 374 | judge_依頼人 | Client |
| 375 | judge_目出し帽の男 | Man in a Ski Mask |
| 376 | judge_老人 | Old Man |
| 377 | judge_ホームレスオジサン | Homeless Guy |
| 378 | judge_若いヤクザ | Young Yakuza |
| 379 | judge_リン子 | Girl in a School Uniform |
| 380 | judge_京浜同名のチンピラ | Keihin Gang Thug |
| 381 | judge_イライラする女性 | Frustrated Woman |
| 382 | judge_困っている女性 | Troubled Woman |
| 383 | judge_迷子少年 | Lost Boy |
| 384 | judge_老け顔の女子高生 | Older-looking Highschool Girl |
| 385 | judge_金髪のチンピラ | Blonde Thug |
| 386 | judge_焦る女子大生 | Panicking College Girl |
| 387 | judge_スーツ姿の男 | Man in a Suit |
| 388 | judge_店員 | Staff |
| 389 | judge_いきなり！ステーキ社長 | President of Ikinari Steak |
| 390 | judge_本村 | Motomura |
| 391 | judge_京浜同盟のチンピラ１ | Keihin Gang Thug |
| 392 | judge_京浜同盟のチンピラ２ | Keihin Gang Thug |
| 393 | judge_藤森 | Fujimori |
| 394 | judge_セーラー服の女 | Girl in a School Uniform |
| 395 | judge_セクシードレスの女 | Woman in a Sexy Dress |
| 396 | judge_ホームレス高崎 | Homeless Takasaki |
| 397 | judge_ホームレス鳥居 | Homeless Tori |
| 398 | judge_近藤 | Kondo |
| 399 | judge_浜中 | Hamanaka |
| 400 | judge_いい年の店員 | Middle-aged Employee |
| 401 | judge_阪木葉の部下 | Sakakiba's Subordinate |
| 402 | judge_ロン毛のホスト | Long-haired Host |
| 403 | judge_怒れるOL | Furious Secretary |
| 404 | judge_橘ゆりか | Yurika Tachibana |
| 405 | judge_つむぎ | Tsumugi |
| 406 | judge_いちゃつく男 | Lovey-dovey Man |
| 407 | judge_いちゃつく女 | Lovey-dovey Woman |
| 408 | judge_怪しいヤクザ | Suspicious Yakuza |
| 409 | judge_？？？_キャッチ | ??? |
| 410 | judge_板長 | Chef |
| 411 | judge_喫煙_張り切る後輩 | Enthusiastic Kohai |
| 412 | judge_喫煙_疲れた先輩 | Tired Senpai |
| 413 | judge_喫煙_疲れた会社員 | Exhausted Corporate Peon |
| 414 | judge_喫煙_歳をとったチンピラ | Aging Punk |
| 415 | judge_喫煙_黒髪のチンピラ | Black-haired Punk |
| 416 | judge_喫煙_ふわふわした女 | Ditzy Lady |
| 417 | judge_喫煙_燃える少年 | Energetic Youth |
| 418 | judge_喫煙_若手作業員 | Young Worker |
| 419 | judge_真面目そうな店員 | Diligent Worker |
| 420 | judge_レン | Ren |
| 421 | judge_猫 | Cat |
| 422 | judge_喫煙_ホームレス山並 | Homeless Yamanami |
| 423 | judge_喫煙_噂好きの作業員 | Gossipy Worker |
| 424 | judge_ドローンラボ受付 | Drone Lab Receptionist |
| 425 | judge_牛遊宴店員 | Beef Zone Employee |
| 426 | judge_怪しい男 | Suspicious Man |
| 427 | judge_臼井 | Usui |
| 428 | judge_山田 | Yamada |
| 429 | judge_田淵 | Tabuchi |
| 430 | judge_福原 | Fukuhara |
| 431 | judge_ミキヤ | Mikiya |
| 432 | judge_気さくな店員 | Easygoing Employee |
| 433 | judge_牛角店員 | Gyu-Kaku Employee |
| 434 | judge_制服姿の男 | Uniformed Man |
| 435 | judge_酔っぱらい | Drunk Woman |
| 436 | judge_ゆるキャラ | Mascot |
| 437 | judge_ギターの少女 | Guitarist Girl |
| 438 | judge_ジャケット姿のファン | Fan Wearing a Jacket |
| 439 | judge_太ったファン | Portly Fan |
| 440 | judge_チンピラ風のファン | Thuggish Fan |
| 441 | judge_業界関係者？ | Industry Official? |
| 442 | judge_占い師風の女 | Fortune-teller Lady |
| 443 | judge_仮面の男 | Masked Man |
| 444 | judge_元気な少年 | Energetic Boy |
| 445 | judge_ビクビクした男 | Suspicious Man |
| 446 | judge_ニヤニヤ顔の男 | Smiling Man |
| 447 | judge_おばちゃん | Older Lady |
| 448 | judge_泣きぼくろの女 | Woman with a Mole Under Her Eye |
| 449 | judge_死にたがりの男 | Suicidal Man |
| 450 | judge_綺麗な女性 | Pretty Woman |
| 451 | judge_ミリタリー男 | Military Man |
| 452 | judge_忍者？ | Ninja? |
| 453 | judge_スーツの男性 | Man in Suit |
| 454 | judge_関西弁の女性 | Woman with a Kansai Dialect |
| 455 | judge_ステッキ男？ | Cane Man? |
| 456 | judge_金髪の白人男性 | Blond Foreigner |
| 457 | judge_頼りなさげな板前 | Unreliable Chef |
| 458 | judge_威勢のいいチンピラ | Thug with Spunk |
| 459 | judge_ランニング男 | Running Man |
| 460 | judge_借金取り | Debt Collector |
| 461 | judge_怪しいファン | Suspicious Fan |
| 462 | judge_竜禅寺の執事 | Ryuzenji's Butler |
| 463 | judge_品野 | Shinano |
| 464 | judge_赤牛丸天下一通り店員 | Akaushimaru Employee |
| 465 | judge_ＰＯＰＰＯ昭和通り店店員 | Poppo Employee |
| 466 | judge_ＰＯＰＰＯ七福通り 東店店員 | Poppo Employee |
| 467 | judge_ＰＯＰＰＯ七福通り 西店店員 | Poppo Employee |
| 468 | judge_ＰＯＰＰＯ天下一通り店店員 | Poppo Employee |
| 469 | judge_スマイルバーガー劇場前店員 | Smile Burger Employee |
| 470 | judge_ミジョーレ店員2 | Mijore Employee |
| 471 | judge_徳永帽子脱げ | Bald Man |
| 472 | judge_通行人 | Passerby |
| 473 | judge_M SIDE CAFE店員2 | M Side Cafe Employee |
