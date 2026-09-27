# ตรวจคำลงท้ายบอกเพศในบทคัตซีน (`auth.bin`)

> สร้างด้วย `python scripts/audit_cinema_gender.py --write` — ห้ามแก้ด้วยมือ

`cinema_telop` ไม่มีคอลัมน์ผู้พูด → เพศต้องตัดสินจากบริบทฉากเท่านั้น

| ฉาก | หญิง | ชาย | บรรทัดทั้งฉาก |
|---|---|---|---|
| a01_010 | 20 | 7 | 134 |
| a05_040 | 13 | 0 | 52 |
| a05_020 | 7 | 22 | 84 |
| a13_190 | 6 | 11 | 102 |
| a01_060 | 3 | 14 | 64 |
| a01_090 | 2 | 21 | 92 |
| a01_020 | 0 | 1 | 70 |
| a01_025 | 0 | 1 | 18 |
| a01_040 | 0 | 4 | 40 |
| a01_050 | 0 | 1 | 36 |
| a01_085 | 0 | 5 | 26 |
| a01_110 | 0 | 31 | 63 |
| a01_120 | 0 | 2 | 72 |
| a02_020 | 0 | 11 | 67 |
| a02_030 | 0 | 1 | 50 |
| a02_035 | 0 | 1 | 24 |
| a02_040 | 0 | 1 | 72 |
| a03_010 | 0 | 15 | 116 |
| a03_020 | 0 | 1 | 72 |
| a03_030 | 0 | 5 | 76 |
| a04_010 | 0 | 4 | 24 |
| a04_017 | 0 | 12 | 52 |
| a04_040 | 0 | 3 | 32 |
| a05_010 | 0 | 5 | 42 |
| a05_030 | 0 | 5 | 20 |
| a07_010 | 0 | 19 | 40 |
| a08_010 | 0 | 14 | 88 |
| a08_020 | 0 | 8 | 103 |
| a08_025 | 0 | 6 | 75 |
| a08_040 | 0 | 1 | 90 |
| a09_005 | 0 | 3 | 46 |
| a09_010 | 0 | 25 | 52 |
| a09_015 | 0 | 6 | 48 |
| a09_060 | 0 | 4 | 36 |
| a11_005 | 0 | 39 | 112 |
| a11_010 | 0 | 8 | 64 |
| a11_020 | 0 | 5 | 94 |
| a11_030 | 0 | 14 | 86 |
| a11_040 | 0 | 1 | 40 |
| a12_020 | 0 | 12 | 108 |
| a12_030 | 0 | 13 | 146 |
| a12_040 | 0 | 10 | 52 |
| a12_050 | 0 | 9 | 32 |
| a12_070 | 0 | 3 | 24 |
| a13_030 | 0 | 4 | 50 |
| a13_040 | 0 | 4 | 66 |
| a13_060 | 0 | 2 | 68 |
| a13_090 | 0 | 10 | 116 |
| a13_120 | 0 | 1 | 50 |
| a13_130 | 0 | 7 | 16 |
| a13_140 | 0 | 3 | 50 |
| a13_160 | 0 | 17 | 106 |
| a13_170 | 0 | 6 | 142 |
| a13_180 | 0 | 12 | 36 |
| a13_185 | 0 | 5 | 50 |

## a01_010 (หญิง 20 · ชาย 7)

| # | ชุด | เพศ | EN | TH |
|---|---|---|---|---|
| 1 | A | - | Yes. | ใช่ |
| 1 | B | - | I see.　 | เข้าใจแล้ว |
| 2 | A | F | Yes, I understand completely. | เข้าใจดีค่ะ ไม่มีปัญหาเลย |
| 2 | B | F | Oh, is that so? | อ้อ งั้นเหรอคะ? |
| 3 | A | F | We'll absolutely be able / to help you out with that. | เราสามารถช่วยเหลือคุณ / ได้อย่างแน่นอนค่ะ |
| 3 | B | F | Yes, of course we can / help you with that. | ได้ค่ะ แน่นอน เราช่วย / คุณได้แน่นอนค่ะ |
| 4 | A | F | I guarantee you. | รับประกันได้เลยค่ะ |
| 4 | B | F | Don't you worry. | ไม่ต้องเป็นห่วงค่ะ |
| 5 | A | F | Oh, you must be / talking about Yagami. | อ๋อ คุณคงหมายถึง / ยากามิสินะคะ |
| 5 | B | F | Hm? Oh... You mean Yagami? | หือ? อ๋อ... หมายถึงยากามิเหรอคะ? |
| 7 | A | F | Absolutely. We appreciate any interest / you might have, but it's just, uh... | แน่นอนค่ะ เราขอบคุณที่คุณสนใจ / แต่ว่า เอ่อ... |
| 7 | B | F | I'm terribly sorry, but I'm afraid / he's all tied up for a while. | ต้องขออภัยจริงๆ ค่ะ แต่ตอนนี้ / เขาติดงานยุ่งอยู่พักหนึ่งค่ะ |
| 8 | A | - | Wow, you know, it must be / so niiice to be a rockstar. | โห นี่สินะ ความเป็นร็อกสตาร์ / คงฟินน่าดูเลยเนอะ |
| 8 | B | - | Come on, how long is / Yagami fever going to last? | ไม่เอาน่า ไข้ยากามิเนี่ย / จะฮิตไปถึงเมื่อไหร่กันเนี่ย |
| 9 | A | - | Right, Saori-chan? | ใช่ไหมล่ะ ซาโอริจัง? |
| 9 | B | - | Right, Saori-chan? | ใช่ไหมล่ะ ซาโอริจัง? |
| 10 | A | F | Genda Law, Saori speaking. | สำนักงานกฎหมายเก็นดะ ซาโอริรับสายค่ะ |
| 10 | B | F | Genda Law Office. | สำนักงานกฎหมายเก็นดะค่ะ |
| 11 | A | F | Yes. Yagami is currently / employed by our firm. | ค่ะ ยากามิเป็นพนักงาน / ของสำนักงานเราอยู่ค่ะ |
| 11 | B | F | Yes. Yagami is on our staff here. | ค่ะ ยากามิเป็นทีมงานที่นี่ค่ะ |
| 12 | A | - | Same bullshit all day. | วันๆ ก็เจอแต่เรื่องบ้าๆ แบบนี้ |
| 12 | B | - | Another one? | อีกแล้วเหรอ? |
| 13 | A | - | Guess everyone wants a lawyer / who can win, huh. | คงเพราะทุกคนอยากได้ทนาย / ที่ชนะคดีได้สินะ |
| 13 | B | - | Everyone wants a lawyer / who can win a defense, huh? | ใครๆ ก็อยากได้ทนาย / ที่แก้ต่างชนะได้ใช่ไหมล่ะ |
| 14 | A | - | Yagami-sensei? | ยากามิเซนเซ? |
| 14 | B | - | Yagami-sensei? | ยากามิเซนเซ? |
| 15 | A | - | Hey, throw me a bone. | เฮ้ย ปราณีกันบ้างสิ |
| 15 | B | - | Gimme a break. | หยุดเหอะน่า |
| 16 | A | - | I never would've won without / a hand from these two. | ผมคงไม่มีทางชนะได้เลย / ถ้าไม่มีสองคนนี้ช่วย |
| 16 | B | M | I just had a lot of luck / on my side on that one. | แค่ผมโชคดีมากๆ / ในครั้งนั้นแหละครับ |
| 17 | A | - | Of course you wouldn't have. | แหงอยู่แล้วละ นายจะชนะเองได้ไง |
| 17 | B | - | Ha. 'Course you did. | ฮึ่ม ก็บอกว่าใช่ไง |
| 18 | A | - | 99 percent of these cases / end up in convictions. | คดีแบบนี้ร้อยละ 99 / จบที่การตัดสินว่าผิด |
| 18 | B | - | Especially considering 99% / of trials end in convictions. | ยิ่งคิดว่า 99% ของการพิจารณาคดี / จบที่การตัดสินว่าผิดด้วยแล้ว |
| 19 | A | - | It makes an acquittal a big deal, / even if it was just luck. | การพ้นผิดเลยเป็นเรื่องใหญ่มาก / ถึงจะเป็นแค่โชคช่วยก็ตาม |
| 19 | B | - | So an acquittal's huge, / even if it's just dumb luck. | การพ้นผิดถึงเป็นเรื่องใหญ่ขนาดนั้น / ถึงจะเป็นแค่โชคช่วยเฉยๆ |
| 20 | A | - | Talk about a lawyer being a hero. | พูดได้เลยว่าทนายคนนั้นคือฮีโร่ |
| 20 | B | - | Any lawyer who pulls / that off is a hero. | ทนายคนไหนทำแบบนั้นได้ / ก็เป็นฮีโร่ทั้งนั้น |
| 21 | A | - | Makes even a former gangster / look good. | ทำให้แม้แต่อดีตนักเลง / ยังดูดีขึ้นมาได้ |
| 21 | B | - | Even ones who used to be thugs. | แม้แต่พวกที่เคยเป็นอันธพาลก็ตาม |
| 22 | A | - | Guess so. | ก็คงงั้นแหละ |
| 22 | B | - | You're right. | นายพูดถูก |
| 23 | A | - | Wipe that grin off your face. / You think you're better than us? | เลิกยิ้มแบบนั้นซะที / คิดว่าตัวเองเก่งกว่าพวกเราเหรอ |
| 23 | B | - | "You're right"!? / Don't get cocky! | "นายพูดถูก" งั้นเหรอ!? / อย่าเหิมเกริมไปหน่อยเลย! |
| 24 | A | M | I'm no saint. | ผมไม่ใช่คนดีเลิศอะไรหรอกครับ |
| 24 | B | M | I wouldn't say I am. | ผมไม่กล้าพูดแบบนั้นหรอกครับ |
| 25 | A | - | Could've fooled me. | ดูไม่ออกเลยนะ |
| 25 | B | - | Sure looks like it from / where I'm sitting. | จากมุมที่ผมมองอยู่ / มันก็ดูเป็นแบบนั้นแหละนะ |
| 26 | A | - | You know, / you're not gonna win all of 'em. | รู้ไว้นะ / นายจะชนะทุกคดีไม่ได้หรอก |
| 26 | B | - | Y'know, you're not / gonna win every time. | รู้ไว้ด้วยนะ นายจะ / ชนะได้ทุกครั้งซะเมื่อไหร่ |
| 27 | A | - | Trust me pal, / my record's not... | เชื่อผมเถอะน่า / สถิติของผมมันไม่ได้... |
| 27 | B | - | As your senpai, I'm warning you. | ในฐานะรุ่นพี่ ผมเตือนไว้ก่อนนะ |
| 28 | A | - | Are you listening? | ฟังอยู่รึเปล่าเนี่ย? |
| 28 | B | - | You even listening!? | นายฟังอยู่รึเปล่าเนี่ย!? |
| 29 | A | M | Of course. / I get the message. | แน่นอนครับ / ผมเก็ตแล้วครับ |
| 29 | B | M | Warning received, thank you. | รับทราบคำเตือนแล้วครับ ขอบคุณครับ |
| 30 | A | - | Hmph. | ฮึ่ม |
| 30 | B | - | Hmph. | ฮึ่ม |
| 31 | A | - | Well, Shintani's available right now. | เอาล่ะ ตอนนี้ชินทานิว่างอยู่นะ |
| 31 | B | F | If you need someone right now, / Shintani is available. | ถ้าต้องการคนตอนนี้เลย / ชินทานิว่างอยู่ค่ะ |
| 32 | A | F | Yes! You bet. / He's more experienced. | ใช่เลยค่ะ! / เขามีประสบการณ์มากกว่าด้วยนะคะ |
| 32 | B | F | Yes, he's more experienced than Yagami. | ค่ะ เขามีประสบการณ์มากกว่ายากามิด้วย |
| 33 | A | - | Are you hearing that? / Now I'm getting tossed your goddamn leftovers. | ได้ยินป่ะเนี่ย / ตอนนี้ฉันโดนป้ายเดนๆ ของนายมาแทนแล้วนะ |
| 33 | B | - | You hearing this? / Looks like I'm getting your scraps. | ได้ยินนี่ป่ะ / ดูเหมือนฉันจะได้แต่เดนๆ ของนาย |
| 34 | A | - | Shut up, man... | หยุดพูดได้แล้วน่า... |
| 34 | B | - | Chill out, would you? | ใจเย็นๆ หน่อยได้ไหม? |
| 35 | A | - | Okay. / And you're sure? | โอเค / แล้วแน่ใจนะ? |
| 35 | B | - | Oh no... You're sure? | ไม่นะ... แน่ใจเหรอ? |
| 36 | A | - | But that just can't be right. | แต่มันเป็นไปไม่ได้หรอก |
| 36 | B | F | Yes, it's just hard to believe... | ค่ะ มันแค่เชื่อยากไปหน่อย... |
| 37 | A | - | He's as skilled as they come. / Trust me. | เขาฝีมือดีที่สุดเท่าที่จะหาได้แล้ว / เชื่อผมสิ |
| 37 | B | - | No, he's never gotten an acquittal. / They're quite rare, you know. | ไม่นะ เขาไม่เคยชนะคดีจนพ้นผิดเลย / รู้ไหมว่ามันหายากแค่ไหน |
| 38 | A | - | Well no, he hasn't won any cases. / You know how rare that is? | เปล่าเลย เขาไม่เคยชนะคดีสักคดี / รู้ไหมว่ามันหายากแค่ไหน |
| 38 | B | - | Don't you know? / In Japan, 99.9% of court cases end in convictions. | ไม่รู้เหรอ / ในญี่ปุ่น คดีในศาล 99.9% จบที่ตัดสินว่าผิด |
| 39 | A | - | Haven't you heard? 99.9% of criminal court / cases end with the defendant behind bars. | ไม่เคยได้ยินเหรอ คดีอาญาในศาล 99.9% / จบด้วยการที่จำเลยติดคุก |
| 39 | B | - | Kind of ridiculous, isn't it? | มันไร้สาระไปหน่อยเนอะ? |
| 40 | A | - | Pretty ridiculous, right? / What? Oh... | ไร้สาระใช่ไหมล่ะ / หา? อ้อ... |
| 40 | B | - | Huh? Oh... | หือ? อ้อ... |
| 41 | A | F | You still want Yagami, though. | แต่คุณก็ยังอยากได้ยากามิอยู่ดีสินะคะ |
| 41 | B | F | You'll only take Yagami? | คุณจะเอาแต่ยากามิเท่านั้นเหรอคะ? |
| 42 | A | - | Man I am so done. | พอกันทีเถอะ |
| 42 | B | - | For crying out loud, / to hell with this! | ให้ตายสิวะ / ช่างหัวมันเถอะ! |
| 43 | A | - | Hey! Can it! | เฮ้ย! หุบปากซะที! |
| 43 | B | - | Everyone, shut up! | ทุกคน หุบปากซะที! |
| 44 | A | - | Yes. Yes. | ใช่ ใช่ |
| 44 | B | - | Yes. Okay. | ใช่ โอเค |
| 45 | A | - | And you're absolutely sure? | แล้วแน่ใจแบบร้อยเปอร์เซ็นต์นะ? |
| 45 | B | - | There's no doubt about it? | ไม่มีข้อสงสัยเลยใช่ไหม? |
| 46 | A | - | I understand. | เข้าใจแล้วล่ะ |
| 46 | B | - | Understood. | รับทราบ |
| 47 | A | - | I'll tell him. | เดี๋ยวจะบอกเขาให้ |
| 47 | B | - | I'll tell him. | เดี๋ยวจะบอกเขาให้ |
| 48 | A | - | Who was that? | ใครเหรอ? |
| 48 | B | - | What's up? | เป็นไงบ้าง? |
| 49 | A | - | Another call for Yagami-sensei. | โทรมาหายากามิเซนเซอีกแล้ว |
| 49 | B | - | It's a job for Yagami-sensei. | เป็นงานของยากามิเซนเซนะ |
| 50 | A | - | Big whoop. | ก็แล้วไง |
| 50 | B | - | Big surprise. | แหงอยู่แล้ว |
| 51 | A | - | But the client is... Shinpei Okubo. | แต่ลูกความคือ... ชินเป โอคุโบะ |
| 51 | B | - | The client is Shinpei Okubo. | ลูกความคือชินเป โอคุโบะ |
| 52 | A | - | Hrm... | อืม... |
| 52 | B | - | Hmmm... | อืมมม... |
| 53 | A | - | Huh!? | หา!? |
| 53 | B | - | Say what!? | ว่าไงนะ!? |
| 54 | A | - | Not sure I believe that. / Okubo's a free man now. | ไม่ค่อยเชื่อเท่าไหร่ / โอคุโบะเป็นอิสระแล้วนี่นา |
| 54 | B | - | Shinpei Okubo... / You mean the guy he just got acquitted? | ชินเป โอคุโบะ... / หมายถึงคนที่เพิ่งพ้นผิดไปเหรอ? |
| 55 | A | - | Not anymore. / He's been arrested for murder. | ไม่ใช่แล้วล่ะ / เขาถูกจับข้อหาฆาตกรรม |
| 55 | B | - | He's been arrested on murder charges. | เขาถูกจับในข้อหาฆาตกรรม |
| 56 | A | - | Come on. / We already proved he was innocent, right? | ไม่เอาน่า / เราเพิ่งพิสูจน์ว่าเขาบริสุทธิ์ไปไม่ใช่เหรอ? |
| 56 | B | - | Wait, but I already— | เดี๋ยวนะ แต่ผมเพิ่ง— |
| 57 | A | - | It's a new case. / He's being processed right now. | เป็นคดีใหม่ / ตอนนี้กำลังดำเนินการอยู่ |
| 57 | B | - | It's a new charge.　 | เป็นข้อหาใหม่ |
| 58 | A | - | What they told me is that... He stabbed his girlfriend, / Emi, to death. Set the apartment on fire. | สิ่งที่เขาบอกผมคือ... เขาแทงแฟนสาวตัวเอง / เอมิ จนตาย แล้วจุดไฟเผาอพาร์ตเมนต์ |
| 58 | B | - | Just now, Okubo stabbed his girlfriend / and set her place on fire with gasoline. | เมื่อกี้นี้ โอคุโบะแทงแฟนสาวตัวเอง / แล้วราดน้ำมันจุดไฟเผาห้องเธอ |
| 59 | A | - | Okubo would never do that! | โอคุโบะไม่มีทางทำแบบนั้น! |
| 59 | B | - | You've gotta be kidding me! | ล้อเล่นใช่ไหมเนี่ย! |
| 60 | A | - | Stabbing Emi-chan... | แทงเอมิจัง... |
| 60 | B | - | When you say he / stabbed his girlfriend... | ที่บอกว่าเขา / แทงแฟนสาวตัวเอง... |
| 61 | A | - | I just don't understand it. | ผมไม่เข้าใจเลยจริงๆ |
| 61 | B | - | You mean he killed Emi-chan? | หมายความว่าเขาฆ่าเอมิจังเหรอ? |
| 62 | A | - | Okubo... | โอคุโบะ... |
| 62 | B | - | No way... | ไม่จริงน่า... |
| 63 | A | - | How could he... | ทำไมเขาถึง... |
| 63 | B | - | Why would he... | ทำไมเขาถึงทำแบบนั้น... |
| 64 | A | M | Suspect secured, sir! | คุมตัวผู้ต้องสงสัยได้แล้วครับ! |
| 64 | B | - | Keep the suspect secure! | คุมตัวผู้ต้องสงสัยไว้ให้ดี! |
| 65 | A | M | Move aside. It's not safe for you here. / Now everyone clear out! | หลีกไปครับ ตรงนี้ไม่ปลอดภัย / ทุกคนถอยไปเดี๋ยวนี้! |
| 65 | B | - | Move it! / Get away from the building! Move! | ถอยไป! / ออกห่างจากตึกด้วย! ถอย! |
| 66 | A | - | That day... | วันนั้น... |
| 66 | B | - | That day... | วันนั้น... |
| 67 | A | - | My career as a lawyer died / alongside Emi-chan... | อาชีพทนายของผมตายไปพร้อมกับ / เอมิจัง... |
| 67 | B | - | My life as a lawyer died / alongside Emi-chan... | ชีวิตทนายความของผมตายไปพร้อมกับ / เอมิจัง... |
| 68 | A | - | Both murdered by Shinpei Okubo. | ทั้งคู่ถูกฆ่าโดยชินเป โอคุโบะ |
| 68 | B | - | Both murdered by Shinpei Okubo, / the serial killer. | ทั้งคู่ถูกฆ่าโดยชินเป โอคุโบะ / ฆาตกรต่อเนื่อง |

## a05_040 (หญิง 13 · ชาย 0)

| # | ชุด | เพศ | EN | TH |
|---|---|---|---|---|
| 1 | A | - | Terasawa-san? | เทราซาวะซัง? |
| 1 | B | - | Terasawa-san? | เทราซาวะซัง? |
| 2 | A | F | Okubo-san's not / a violent person. | โอคุโบะซังไม่ใช่คน / ที่ใช้ความรุนแรงเลยค่ะ |
| 2 | B | F | Okubo-san isn't some / kind of violent criminal. | โอคุโบะซังไม่ใช่อาชญากร / ที่ใช้ความรุนแรงแบบนั้นเลยค่ะ |
| 3 | A | - | And he hasn't even had a drink in over six years. / Not a single drop since the incident! | แล้วเขาก็ไม่แตะเหล้าเลยมากว่าหกปีแล้ว / ไม่แม้แต่หยดเดียวนับตั้งแต่เหตุการณ์นั้น! |
| 3 | B | - | He hasn't touched a drop of alcohol / since his outburst six years ago. | เขาไม่แตะเหล้าแม้แต่หยดเดียว / นับตั้งแต่ที่เขาระเบิดอารมณ์เมื่อหกปีก่อน |
| 4 | A | - | My court will not stand / for this commotion. | ศาลนี้จะไม่ยอมให้ / มีความวุ่นวายแบบนี้เกิดขึ้น |
| 4 | B | - | I'm afraid you're out of order. | เกรงว่าคุณจะพูดนอกลู่นอกทางแล้ว |
| 5 | A | - | He didn't blame Waku-san at all. He knew that / the outburst was just caused by his dementia. | เขาไม่เคยโทษวาคุซังเลยสักนิด เขารู้ดีว่า / การระเบิดอารมณ์นั้นเกิดจากโรคสมองเสื่อมของวาคุซังเอง |
| 5 | B | - | He understood Waku-san was only / lashing out because of his dementia. | เขาเข้าใจดีว่าวาคุซังแค่ / ทำร้ายคนอื่นเพราะโรคสมองเสื่อมเท่านั้น |
| 6 | A | - | That it was all the sickness's fault. | ทั้งหมดเป็นความผิดของโรคร้ายต่างหาก |
| 6 | B | - | So it's not like he held it against him! | เขาไม่เคยผูกใจเจ็บกับวาคุซังเลยสักนิด! |
| 7 | A | - | So there was no reason for him / to resort to murder! | เขาจึงไม่มีเหตุผลอะไร / ที่จะต้องลงมือฆ่าเลย! |
| 7 | B | - | There's no way that would / drive him to murder! | เรื่องแบบนั้นไม่มีทาง / ผลักดันให้เขาต้องฆ่าคนได้เลย! |
| 8 | A | - | Terasawa-san. Please. | เทราซาวะซัง ขอร้องล่ะ |
| 8 | B | - | Terasawa-san, please. | เทราซาวะซัง ใจเย็นๆ ก่อนนะ |
| 9 | A | F | Okubo-san really is / an incredible, caring person! | โอคุโบะซังเป็นคนที่ / น่าทึ่งและใส่ใจคนอื่นจริงๆ นะคะ! |
| 9 | B | F | Okubo-san has lots of positive traits too! | โอคุโบะซังก็มีข้อดีตั้งเยอะแยะนะคะ! |
| 10 | A | - | Please leave this courtroom at once. | กรุณาออกจากห้องพิจารณาคดีนี้ในทันที |
| 10 | B | - | Leave this courtroom before / I have you removed! | ออกไปจากห้องพิจารณาคดีนี้ซะ / ก่อนที่จะให้คนมาพาตัวออกไป! |
| 11 | A | F | You're right that he may be hard / to approach, but he's a kind soul. | ก็จริงที่เขาอาจจะดูเข้าถึงยาก / แต่ลึกๆ แล้วเขาใจดีมากนะคะ |
| 11 | B | - | He's not the most approachable guy, / but he works hard... | เขาอาจจะไม่ใช่คนที่เข้าหาง่ายนัก / แต่เขาก็ตั้งใจทำงานหนักมาก... |
| 12 | A | - | ...And he always keeps his promises! | ...แล้วเขาก็รักษาสัญญาเสมอ! |
| 12 | B | - | And he keeps his promises! | แล้วเขาก็เป็นคนรักษาคำพูดด้วย! |
| 13 | A | F | Okubo-san's not the only person in this courtroom / who would be affected by a guilty verdict, either. | โอคุโบะซังไม่ใช่คนเดียวในห้องนี้ / ที่จะได้รับผลกระทบถ้าถูกตัดสินว่ามีความผิดนะคะ |
| 13 | B | F | If you find him guilty, / my life is basically over too. | ถ้าตัดสินว่าเขามีความผิด / ชีวิตดิฉันก็คงจบสิ้นไปด้วยเหมือนกัน |
| 14 | A | F | As a matter of fact, / it would break my heart. | อันที่จริง / มันคงทำให้ดิฉันใจสลายเลยค่ะ |
| 14 | B | F | That's why he didn't want me to testify. | นั่นแหละค่ะเหตุผลที่เขาไม่อยากให้ดิฉันขึ้นให้การ |
| 15 | A | - | And even through it all... | แล้วถึงแม้จะเจอเรื่องแบบนั้นมาทั้งหมด... |
| 15 | B | F | I couldn't even tell / his own lawyer... | ดิฉันไม่เคยบอกแม้แต่ / ทนายความของเขาเองเลย... |
| 16 | A | F | He wanted me to keep this a secret! Not to tell anyone, / not even his lawyer, that we were dating! | เขาอยากให้ดิฉันเก็บเรื่องนี้เป็นความลับ! ไม่ให้บอกใครเลย / แม้แต่ทนายของเขาเอง ว่าเราคบกันอยู่! |
| 16 | B | - | That the two of us / are seeing each other! | ว่าเราสองคน / คบหาดูใจกันอยู่! |
| 17 | A | F | Even though he knew he could have ended up in prison, / making sure I was safe was the only thing in the world he cared about! | ถึงแม้เขาจะรู้ว่าอาจต้องติดคุก / แต่สิ่งเดียวที่เขาใส่ใจในโลกนี้ก็คือความปลอดภัยของดิฉัน! |
| 17 | B | F | Even though he knew he might go to jail, / he was only thinking of my future. | ถึงแม้เขาจะรู้ว่าอาจต้องติดคุก / แต่เขาคิดถึงแต่อนาคตของดิฉันเท่านั้น |
| 18 | A | - | That's just who he is! | นั่นแหละคือตัวตนที่แท้จริงของเขา! |
| 18 | B | - | That's the kind of guy he is! | เขาเป็นคนแบบนั้นแหละ! |
| 19 | A | - | But when the prosecution has / already decided he's a criminal... | แต่ในเมื่อฝ่ายอัยการ / ตัดสินไปแล้วว่าเขาคืออาชญากร... |
| 19 | B | - | So is a prosecutor who / paints him as some kind of bully... | แล้วอัยการที่พยายามป้ายสี / ให้เขาดูเป็นคนพาลรังแกคนอื่น... |
| 20 | A | - | How could he possibly / be given a fair trial!? | แล้วเขาจะได้รับการพิจารณาคดี / อย่างเป็นธรรมได้ยังไงกัน!? |
| 20 | B | - | ...Really giving him / the benefit of the doubt!? | ...จะยกประโยชน์แห่งความสงสัย / ให้เขาจริงๆ เหรอ!? |
| 22 | A | - | Her little outburst wasn't technically admissable, / but as the trial dragged on, it hung over the jury like a stone. | แม้การระเบิดอารมณ์เล็กๆ ของเธอจะรับฟังเป็นหลักฐานไม่ได้ตามหลักกฎหมาย / แต่พอการพิจารณาคดียืดเยื้อไป มันก็ถ่วงใจคณะลูกขุนเหมือนก้อนหินหนักอึ้ง |
| 22 | B | - | The trial resumed after that, but I think her / parting remarks helped sway the verdict. | หลังจากนั้นการพิจารณาคดีก็ดำเนินต่อไป แต่ผมคิดว่าคำพูดทิ้งท้าย / ของเธอมีส่วนโน้มน้าวคำตัดสินไม่น้อย |
| 23 | A | - | And in the end, / Shinpei Okubo was found not guilty. | และในที่สุด / ชินเป โอคุโบะ ก็ถูกตัดสินว่าไม่มีความผิด |
| 23 | B | - | Shinpei Okubo was found innocent. | ชินเป โอคุโบะ พ้นผิดในที่สุด |
| 24 | A | - | But only a month after his release... | แต่เพียงเดือนเดียวหลังจากที่เขาได้รับการปล่อยตัว... |
| 24 | B | - | But... | แต่... |
| 25 | A | - | Everything changed. | ทุกอย่างก็เปลี่ยนไป |
| 25 | B | - | Not more than a month later...　 | ไม่ถึงเดือนหลังจากนั้น...  |
| 26 | A | - | The same girl who had so bravely / proclaimed Okubo's innocence... | ผู้หญิงคนเดียวกันที่เคยกล้าหาญ / ยืนยันความบริสุทธิ์ของโอคุโบะ... |
| 26 | B | - | Okubo took it upon himself... | โอคุโบะตัดสินใจด้วยตัวเอง... |
| 27 | A | - | ...Died by the man's own hand. | ...ต้องตายด้วยน้ำมือของชายคนนั้นเอง |
| 27 | B | - | ...To render his own cruel verdict / for Emi Terasawa. | ...ในการตัดสินโทษอันโหดร้ายของตัวเอง / ให้กับเอมิ เทราซาวะ |

## a05_020 (หญิง 7 · ชาย 22)

| # | ชุด | เพศ | EN | TH |
|---|---|---|---|---|
| 1 | A | M | Well... Could I at least talk / to Director Kido instead? | เอ่อ... ผมขอคุยกับ / ผู้อำนวยการคิโดะแทนได้ไหมครับ? |
| 1 | B | M | Then, can we talk with Director Kido? | งั้นเราขอคุยกับผู้อำนวยการคิโดะได้ไหมครับ? |
| 2 | A | - | He's an old friend of mine. | เขาเป็นเพื่อนเก่าของผมน่ะ |
| 2 | B | - | We've met before. | เราเคยเจอกันมาก่อน |
| 3 | A | - | Just let him know Yagami / stopped by to say hello. | แค่บอกเขาว่ายากามิ / แวะมาทักทายก็พอ |
| 3 | B | - | Tell him I'm a lawyer named Yagami. | บอกเขาว่าผมเป็นทนายชื่อยากามิ |
| 4 | A | - | I don't think that'll / be necessary. | คงไม่จำเป็น / ขนาดนั้นหรอก |
| 4 | B | - | Hey, Yagami-san. Look. | เฮ้ ยากามิซัง ดูนั่นสิ |
| 5 | A | - | Look over there... | ดูตรงนั้นสิ... |
| 5 | B | - | Isn't that Kido-san right there? | นั่นคิโดะซังใช่ไหมนั่น? |
| 6 | A | - | Gentlemen. I really don't know / what else you want from me. | คุณผู้ชายทั้งสอง ผมไม่รู้จริงๆ / ว่าพวกคุณยังต้องการอะไรจากผมอีก |
| 6 | B | - | You again? / Can't you handle the rest on your end? | มาอีกแล้วเหรอ? / ช่วยจัดการส่วนที่เหลือทางฝั่งคุณเองไม่ได้หรือไง? |
| 7 | A | - | I have nothing more to say. / I've told the police all that I know. | ไม่มีอะไรจะพูดเพิ่มแล้ว / บอกตำรวจไปหมดทุกอย่างที่รู้แล้ว |
| 7 | B | - | I've already told the police / everything I know. | บอกตำรวจไปหมดแล้ว / ทุกอย่างที่รู้ |
| 8 | A | M | Yeah, I know. / Sorry about all this, Director. | ครับ ผมรู้ / ขอโทษด้วยจริงๆ ท่านผู้อำนวยการ |
| 8 | B | M | Apologies, sir, / you're absolutely right, but... | ต้องขออภัยด้วยครับ / ท่านพูดถูกทุกอย่างเลย แต่ว่า... |
| 9 | A | - | Problem is, my partner here won't give / it a rest 'til he sees the scene of the crime. | ปัญหาคือเพื่อนร่วมงานผมคนนี้ / ไม่ยอมเลิกจนกว่าจะได้เห็นที่เกิดเหตุด้วยตาตัวเอง |
| 9 | B | M | This guy wants to see the crime scene, / and he won't take no for an answer. | เพื่อนคนนี้อยากไปดูที่เกิดเหตุ / แล้วไม่ยอมรับคำว่า 'ไม่' เด็ดขาดครับ |
| 10 | A | M | But... / I'm sure we'll be leaving soon. | แต่... / ผมมั่นใจว่าเดี๋ยวเราก็ไปกันแล้วครับ |
| 10 | B | M | We won't be long. | ไม่นานหรอกครับ |
| 11 | A | - | That's not what we agreed upon. | นั่นไม่ใช่สิ่งที่เราตกลงกันไว้นะ |
| 11 | B | - | Don't make promises we can't keep. | อย่าไปรับปากอะไรที่ทำไม่ได้สิ |
| 12 | A | - | You know this isn't about / how long it takes. | คุณก็รู้ว่ามันไม่ใช่เรื่อง / ที่ว่าจะใช้เวลานานแค่ไหนหรอกนะ |
| 12 | B | - | I'll be here until I'm satisfied. | ผมจะอยู่ตรงนี้จนกว่าจะพอใจ |
| 13 | A | - | And what about Okubo? / I take it he's still not fessed up. | แล้วเรื่องโอคุโบะล่ะ? / คงยังไม่ยอมรับสารภาพใช่ไหม |
| 13 | B | - | So Okubo still hasn't admitted to the crime? | หมายความว่าโอคุโบะยังไม่ยอมรับว่าเป็นคนก่อเหตุใช่ไหม? |
| 14 | A | - | Uh... No, not quite as of yet, sir. | เอ่อ...ยังเลย ยังไม่ยอมรับ |
| 14 | B | - | Right, he's really digging his heels in. | ใช่ เขายังดื้อแพ่งอยู่เลย |
| 15 | A | - | But we all saw where the body was. / Exactly where he said it would be. | แต่เราก็เห็นกันหมดแล้วว่าศพอยู่ตรงไหน / ตรงกับที่เขาบอกไว้เป๊ะ |
| 15 | B | - | The body turned up where / he said he buried it and all. | ศพก็โผล่ตรงจุดที่ / เขาบอกว่าฝังไว้เป๊ะเลย |
| 16 | A | - | Quite true. / Not much point in fighting this now. | ก็จริงอยู่ / ตอนนี้จะสู้คดีต่อไปก็คงไม่มีประโยชน์อะไรแล้ว |
| 16 | B | - | Right? Then hurry up / and put this trial to bed. | ใช่ไหมล่ะ? งั้นก็รีบๆ / ปิดคดีนี้ให้จบๆ ไปซะที |
| 17 | A | - | The minister has made it clear that he wants / it resolved soon, as well. *sigh* | ท่านรัฐมนตรีก็บอกชัดเจนว่าอยากให้ / เรื่องนี้จบเร็วๆ เหมือนกัน *ถอนหายใจ* |
| 17 | B | - | Goddamn, how did a single contractor / stir up this much trouble? | ให้ตายสิ พนักงานเหมาช่วงคนเดียว / ก่อเรื่องวุ่นวายได้ขนาดนี้ได้ยังไง |
| 18 | A | - | Just look at how much trouble one / contractor has caused. | ดูสิ พนักงานเหมาช่วงคนเดียว / สร้างปัญหาไว้มากแค่ไหน |
| 18 | B | - | The minister wants this cleared up / as quickly as possible. | ท่านรัฐมนตรีอยากให้เคลียร์เรื่องนี้ / ให้เร็วที่สุดเท่าที่จะทำได้ |
| 19 | A | M | Sorry... Which minister? | ขอโทษนะครับ...ท่านรัฐมนตรีคนไหนครับ |
| 19 | B | - | By "the minister..." | ที่บอกว่า "ท่านรัฐมนตรี"... |
| 20 | A | M | I didn't know about this, sir. | ผมไม่ทราบเรื่องนี้มาก่อนเลยครับ |
| 20 | B | M | You mean the Minister of Health? | หมายถึงท่านรัฐมนตรีสาธารณสุขใช่ไหมครับ? |
| 21 | A | - | The Health Minister. / It's all his call how much funding we get. | ท่านรัฐมนตรีสาธารณสุขน่ะแหละ / งบประมาณที่เราจะได้มากแค่ไหนก็ขึ้นอยู่กับท่านทั้งนั้น |
| 21 | B | - | Obviously. Our budget falls / under the Health Ministry. | ก็แน่นอนอยู่แล้ว งบของเรา / อยู่ภายใต้กระทรวงสาธารณสุขทั้งหมด |
| 22 | A | M | Director. If I may. | ท่านผู้อำนวยการครับ ขออนุญาตนะครับ |
| 22 | B | M | Um, Director... | เอ่อ ท่านผู้อำนวยการครับ... |
| 23 | A | M | If you would just direct me to the scene / of the crime, I could head over there myself. | ถ้าท่านช่วยบอกทางไปยังที่เกิดเหตุ / ผมจะไปดูเองก็ได้ครับ |
| 23 | B | M | If you could point me in the right direction, / I'd be happy to examine it myself. | ถ้าท่านช่วยชี้ทางที่ถูกต้องให้ / ผมยินดีไปตรวจดูด้วยตัวเองครับ |
| 24 | A | M | I'll be out of your hair in no time, / I assure you. | ผมจะรีบไปให้พ้นทางโดยเร็วที่สุด / รับรองได้เลยครับ |
| 24 | B | - | I'll be discreet. | ผมจะเก็บเป็นความลับให้ |
| 25 | A | - | I'd rather you didn't / wander on your own. | ผมไม่อยากให้คุณ / เดินไปมาคนเดียวตามลำพัง |
| 25 | B | - | I can't let you just wander around. | ผมปล่อยให้คุณเดินเพ่นพ่านเองแบบนั้นไม่ได้หรอก |
| 26 | A | - | So instead... / She can show you. | งั้น... / ให้เธอพาคุณไปดีกว่า |
| 26 | B | - | She can be your chaperone. | เธอจะเป็นคนพาคุณไปเอง |
| 27 | A | - | Terasawa-kun. These gentlemen here / are Shintani-sensei, and... | เทราซาวะคุง คุณสุภาพบุรุษสองท่านนี้ / คือชินทานิเซนเซ กับ... |
| 27 | B | - | Terasawa-kun. / This is Shintani-sensei and... | เทราซาวะคุง / นี่คือชินทานิเซนเซ กับ... |
| 28 | A | - | Uh... | เอ่อ... |
| 28 | B | - | Uh... | เอ่อ... |
| 29 | A | M | Yagami. | ยากามิครับ |
| 29 | B | M | Yagami. | ยากามิครับ |
| 30 | A | F | It's a pleasure. I hope I can help / you find what you need. | ยินดีที่ได้รู้จักค่ะ หวังว่าดิฉันจะช่วย / คุณหาสิ่งที่ต้องการได้นะคะ |
| 30 | B | F | I'm Terasawa. / Pleased to meet you. | ดิฉันเทราซาวะค่ะ / ยินดีที่ได้รู้จักค่ะ |
| 31 | A | - | Well... / With that I'll be taking my leave. | เอาล่ะ... / งั้นผมขอตัวก่อนนะ |
| 31 | B | - | I'll take my leave, then. | ถ้างั้นผมขอตัวก่อนละกัน |
| 32 | A | M | Thank you again, Director. / Apologies for all the trouble. | ขอบคุณอีกครั้งนะครับ ท่านผู้อำนวยการ / ขออภัยที่รบกวนด้วยครับ |
| 32 | B | M | Thank you, Director. / Apologies for the trouble. | ขอบคุณครับ ท่านผู้อำนวยการ / ขออภัยที่ทำให้ลำบากด้วยครับ |
| 33 | A | F | This way. I can show you how to get / to Waku-san's room. | ทางนี้ค่ะ ดิฉันจะพาไปที่ห้อง / ของวาคุซังเองนะคะ |
| 33 | B | F | Well, then... / Should we start with Waku-san's room? | เอาล่ะ... / เริ่มจากห้องของวาคุซังก่อนดีไหมคะ |
| 34 | A | - | ...Who's Waku-san? | ...วาคุซังคือใครนะ |
| 34 | B | - | Waku-san? | วาคุซังเหรอ? |
| 35 | A | M | The guy who died in his room? | คนที่ตายในห้องนั่นไงครับ |
| 35 | B | M | The victim, remember? | ก็เหยื่อไงครับ จำได้ไหม |
| 36 | A | - | Uhhh. Oh yeah. | อ๋อ...เออ นึกออกแล้ว |
| 36 | B | - | O-Oh, right. Yeah. | อ๋อ เออ...ใช่สิ |
| 37 | A | - | And you are... | แล้วคุณคือ... |
| 37 | B | - | And you were... | แล้วคุณคือใครนะ |
| 38 | A | - | Terasawa-san, huh? | เทราซาวะซังเหรอ? |
| 38 | B | M | Terasawa-san, right? | เทราซาวะซังใช่ไหมครับ? |
| 39 | A | - |  Wooow, you're young. / And a looker to boot. |  ว้าว คุณอายุยังน้อยจัง / แถมยังสวยอีกด้วย |
| 39 | B | - | You're so young! / I didn't catch your first name? | คุณยังเด็กจังเลยนะ / ยังไม่ทันได้ถามชื่อจริงเลย |
| 40 | A | F | Umm... / Can we keep this professional? | เอ่อ... / ขอคุยกันแบบมืออาชีพได้ไหมคะ |
| 40 | B | F | Uh, I'm kind of busy here, so... | เอ่อ ตอนนี้ดิฉันค่อนข้างยุ่งน่ะค่ะ... |
| 41 | A | - | Huh? | หา? |
| 41 | B | - | Huh? | หา? |
| 42 | A | F | Nice try, Shintani-sensei. | พยายามได้ดีค่ะ ชินทานิเซนเซ |
| 42 | B | - | Come on, Shintani-sensei. | ไม่เอาน่า ชินทานิเซนเซ |

## a13_190 (หญิง 6 · ชาย 11)

| # | ชุด | เพศ | EN | TH |
|---|---|---|---|---|
| 1 | A | - | Y'know, I really wouldn't mind you goin' back. | รู้ไหม ผมไม่ว่าอะไรเลยนะถ้านายจะกลับไป |
| 1 | B | - | Well, you know I wouldn't mind. | ก็นายก็รู้ว่าผมไม่ว่าอะไรหรอก |
| 2 | A | - | I mean back to being an attorney again. | หมายถึงกลับไปเป็นทนายอีกครั้งน่ะ |
| 2 | B | - | You can go back to / the law if you want. | นายจะกลับไปเป็นทนาย / อีกก็ได้นะถ้าอยากกลับ |
| 3 | A | - | It's not like we got work comin' in. / Maybe I could find a job at another agency or somethin'. | ก็ไม่เห็นจะมีงานเข้ามาเลยนี่ / ฉันอาจจะไปหางานที่สำนักงานอื่นก็ได้มั้ง |
| 3 | B | - | I'm sure I could find work out there. / Not like we have any. | ฉันว่าออกไปหางานที่ไหนก็ได้แหละ / ในเมื่อที่นี่ไม่มีงานให้ทำอยู่ดี |
| 4 | A | - | What are you talking about? | นายพูดเรื่องอะไรของนาย? |
| 4 | B | - | What was that now? | ว่าไงนะ? |
| 5 | A | - | I'm not gonna abandon / our business like that, man. | ผมไม่มีทางทิ้ง / กิจการของเราไปแบบนั้นหรอกนะ |
| 5 | B | - | I'm not about to / close up shop anyway. | ยังไงผมก็ไม่คิดจะ / ปิดกิจการหรอก |
| 6 | A | - | But this is your chance / to be an upstanding citizen again. | แต่นี่มันโอกาสของนาย / ที่จะกลับไปเป็นพลเมืองดีอีกครั้งนะ |
| 6 | B | - | Even with an open invitation / back to being respectable? | ต่อให้มีคนเปิดทางให้ / กลับไปเป็นคนน่านับถืออีกครั้งก็ไม่เอาเหรอ? |
| 7 | A | - | C'mon, man. You know how much of a gaping shithole / this city is. Only a dumbass'd be a detective here. | ไม่เอาน่า นายก็รู้ว่าเมืองนี้มันเป็น / รูโสโครกแค่ไหน มีแต่ไอ้โง่เท่านั้นแหละที่จะมาเป็นนักสืบที่นี่ |
| 7 | B | - | What kinda dumbass would choose / a detective's life in this shithole city? | มีไอ้โง่คนไหนบ้างที่จะเลือก / เป็นนักสืบในเมืองรูโสโครกแบบนี้? |
| 8 | A | M | Well, thank you very much. | ก็ขอบคุณมากเลยนะครับ |
| 8 | B | - | Real nice of you. | ใจดีจริงๆ เลยนะ |
| 9 | A | F | Kaito-san's right though, you know. | แต่ไคโตะซังพูดถูกนะคะ |
| 9 | B | F | Kaito-san's right, don't you think?  | ไคโตะซังพูดถูกไม่ใช่เหรอคะ?  |
| 10 | A | F | I mean just think about it. People would line up / just to have you represent them. | ลองคิดดูสิคะ คนคงต่อแถว / เพื่อขอให้คุณเป็นทนายให้เลย |
| 10 | B | - | People would be lining up / for you to represent them now. | ตอนนี้คนคงต่อแถวกัน / เพื่อขอให้คุณเป็นทนายให้แน่ๆ |
| 11 | A | - | It shouldn't even be a question. | มันไม่น่าจะต้องถามด้วยซ้ำ |
| 11 | B | - | Should this even be a question? | เรื่องนี้ต้องมาถามกันด้วยเหรอ? |
| 12 | A | - | You think so? | คุณคิดงั้นจริงๆ เหรอ? |
| 12 | B | - | You really think so? | คิดงั้นจริงๆ เหรอเนี่ย? |
| 13 | A | F | Of course I think so. | แน่นอนอยู่แล้วค่ะ |
| 13 | B | - |  "You really think so?" he says... |  "คิดงั้นจริงๆ เหรอ" เขาว่างั้นแหละ... |
| 14 | A | - | Genda-sensei would love to have / you back at his office! And, um... | เก็นดะเซนเซคงดีใจมาก / ถ้าได้คุณกลับไปที่สำนักงานอีกครั้ง! แล้วก็ เอ่อ... |
| 14 | B | - | Even Genda-sensei would / take you back in a heartbeat. And... | ต่อให้เป็นเก็นดะเซนเซก็คง / รับคุณกลับทันทีแหละ แล้วก็... |
| 15 | A | F | I'm sure Matsugane-san / would agree with him. | ดิฉันมั่นใจว่ามัตสึกาเนะซัง / ก็คงเห็นด้วยกับท่านเหมือนกัน |
| 15 | B | - | It's what Matsugane-san would want. | นั่นคือสิ่งที่มัตสึกาเนะซังต้องการเหมือนกัน |
| 16 | A | - | Yup. | ใช่. |
| 16 | B | - | I have to say... | ต้องบอกเลยว่า... |
| 17 | A | - | She's right, man. | เธอพูดถูกนะเว้ย |
| 17 | B | - | I agree. | เห็นด้วย |
| 18 | A | - | Everything's led up to this point. It's like your story's circling / back around. There's this fancy French word... | ทุกอย่างมันนำมาสู่จุดนี้ เหมือนเรื่องราวของคุณ / วนกลับมาบรรจบกันเลยนะ มีคำฝรั่งเศสหรูๆ คำหนึ่ง... |
| 18 | B | F | Things got a little crazy, / but I think you being a lawyer is God's... | ทุกอย่างมันบ้าไปหน่อย / แต่ดิฉันว่าการที่คุณเป็นทนายมันคือ... |
| 19 | A | - | Uh... Starts with a D... | เอ่อ... ขึ้นต้นด้วยตัว D... |
| 19 | B | - | Uh, what was it again? | เอ่อ คำว่าอะไรนะ? |
| 20 | A | - | This is your... | นี่คือ...ของคุณ... |
| 20 | B | - | God's... | แผนของพระเจ้า... |
| 21 | A | - | Your denouement? | บทสรุปชีวิตของคุณไงล่ะ? |
| 21 | B | - | His plan? | แผนการของท่านไงล่ะ? |
| 22 | A | - | That's it! | ใช่แล้ว! |
| 22 | B | - | That's the word! | นั่นแหละคำนั้น! |
| 23 | A | - | Would you two give it a rest? | จะหยุดกันสักทีได้ไหม? |
| 23 | B | - | Gimme a break... | ขอร้องเถอะ... |
| 24 | A | - | Huh? | หา? |
| 24 | B | - | Huh? | หา? |
| 25 | A | - | I quit. I'm not a lawyer anymore. / I'm a detective. | ผมเลิกแล้ว ผมไม่ใช่ทนายอีกต่อไป / ผมเป็นนักสืบ |
| 25 | B | - | I quit practicing law, / and I'm a detective now. | ผมเลิกว่าความ / ตอนนี้ผมเป็นนักสืบแล้ว |
| 26 | A | - | But funny enough if I hadn't left Genda's... / I never would've proven Okubo-kun innocent. | แต่ตลกดีนะ ถ้าผมไม่ออกจากที่เก็นดะ... / ผมก็คงไม่มีทางพิสูจน์ว่าโอคุโบะคุงบริสุทธิ์ได้ |
| 26 | B | - | Besides, I was only able to prove / Okubo-san's innocence as a detective. | อีกอย่าง ผมพิสูจน์ความบริสุทธิ์ / ของโอคุโบะซังได้ก็เพราะเป็นนักสืบนี่แหละ |
| 27 | A | - | Well, yes. / I suppose that's true. | ก็... ใช่ / คิดว่าอย่างนั้นจริงๆ นั่นแหละ |
| 27 | B | - | I suppose that's kind of true.　 | คิดว่าก็จริงอยู่เหมือนกันนะ　 |
| 28 | A | - | Pretty damn ironic. It's been three years now... / Since I abandoned the truth and left my job as a lawyer. | มันย้อนแย้งชะมัด สามปีผ่านไปแล้ว... / ตั้งแต่ผมทิ้งความจริงแล้วเลิกเป็นทนาย |
| 28 | B | - | Ironic, isn't it? As a lawyer, / I all but ran from the truth... | ย้อนแย้งใช่ไหมล่ะ สมัยเป็นทนาย / ผมแทบจะหนีความจริงตลอดเวลา... |
| 29 | A | M | But it turned out that decision... Led me / straight to the truth I tried to run away from. | แต่กลับกลายเป็นว่าการตัดสินใจนั้น... พาผม / ไปพบความจริงที่พยายามหนีมาตลอดพอดี |
| 29 | B | - | But as a detective, / I'd never seen the truth so clearly. | แต่พอมาเป็นนักสืบ / ผมไม่เคยเห็นความจริงชัดขนาดนี้มาก่อน |
| 30 | A | - | Guess it goes to show... / You never know where your choices'll take you. | เห็นทีจะพิสูจน์ได้ว่า... / ไม่มีใครรู้หรอกว่าทางเลือกจะพาเราไปที่ไหน |
| 30 | B | - | You never know where your / choices will take you in life. | ไม่มีใครรู้หรอกว่าทางเลือก / จะพาชีวิตเราไปที่ไหน |
| 31 | A | - | It's destiny! / That's what you guys were saying just now, right? | มันคือโชคชะตาไงล่ะ! / นั่นแหละที่พวกคุณเพิ่งพูดกันเมื่อกี้ใช่ไหม? |
| 31 | B | - | All part of God's plan, was it? | ทั้งหมดคือแผนของพระเจ้าใช่ไหมล่ะ? |
| 32 | A | - | So... No matter what decisions you might make... / What comes after matters most. | ดังนั้น... ไม่ว่าคุณจะตัดสินใจแบบไหน... / สิ่งที่ตามมาต่างหากที่สำคัญที่สุด |
| 32 | B | - | But it's all about follow-through, / no matter what choice you make. | แต่สุดท้ายมันอยู่ที่การทำต่อให้สำเร็จ / ไม่ว่าจะเลือกทางไหนก็ตาม |
| 33 | A | - | The real important take away from all this... / Is to never give up. | สิ่งสำคัญที่สุดที่ควรจะได้จากเรื่องนี้... / คือการไม่ยอมแพ้ |
| 33 | B | - | Not giving up on it / is the most important part. | การไม่ยอมแพ้ / คือส่วนที่สำคัญที่สุด |
| 34 | A | - | I... guess. | ก็... คงงั้นมั้ง |
| 34 | B | - | Well... I suppose. | ก็... คงอย่างนั้นแหละ |
| 35 | A | - | By the way... | ว่าแต่... |
| 35 | B | - | By the way... | ว่าแต่... |
| 36 | A | - | Hm? What is it? | หืม? อะไรเหรอ? |
| 36 | B | - | What now? | อะไรอีกล่ะ? |
| 37 | A | - | I was just thinking about how I looked in that suit. / I didn't really pull it off, did I? I knew it! | ผมแค่คิดถึงตอนที่ใส่สูทตัวนั้นน่ะ / มันไม่เข้ากับผมเลยใช่ไหม? รู้อยู่แล้วเชียว! |
| 37 | B | - | I hadn't worn a suit in forever, / and it wasn't really working, was it? | ผมไม่ได้ใส่สูทมานานมากแล้ว / มันดูไม่เข้ากับผมเลยใช่ไหมล่ะ? |
| 38 | A | - | That settles it. / I'm never wearing a suit again, no way, no how. | ตกลงตามนั้น / ผมจะไม่ใส่สูทอีกเด็ดขาด ไม่มีทางเลย |
| 38 | B | - | I'm pretty certain that / I'm done with suits for good. Yep. | ผมค่อนข้างมั่นใจเลยว่า / เลิกใส่สูทตลอดกาลแน่นอน ใช่แล้ว |
| 39 | A | - | Hey, y'know! / Now that's another plus of staying a detective! | เฮ้ รู้ไหม! / นี่แหละอีกข้อดีของการเป็นนักสืบต่อไป! |
| 39 | B | - | And to my point, / detectives never have to wear suits. | แล้วก็ตามที่ฉันว่าไว้ / นักสืบไม่ต้องใส่สูทเลยสักครั้ง |
| 40 | A | - | Seriously...? | เอาจริงดิ...? |
| 40 | B | - | Oh grow up... | โตซะทีเถอะ... |
| 41 | A | M | Hello? Yagami Detective Agency. | ฮัลโหล สำนักงานนักสืบยากามิครับ |
| 41 | B | M | Hello? Yagami Detective Agency.  | ฮัลโหล สำนักงานนักสืบยากามิครับ  |
| 42 | A | M | Huh? Your cat ran away / and it still hasn't come home? | หา? แมวของคุณหนีออกจากบ้าน / แล้วยังไม่กลับมาเลยเหรอครับ? |
| 42 | B | M | Huh? / Your cat ran away from home? | หา? / แมวของคุณหนีออกจากบ้านเหรอครับ? |
| 43 | A | - | What do you think this is lady, a pet shop? | คุณคิดว่าที่นี่คือร้านขายสัตว์เลี้ยงหรือไงล่ะคุณลูกค้า? |
| 43 | B | - | We're not exactly a pet shop here... | ที่นี่ไม่ใช่ร้านขายสัตว์เลี้ยงซะหน่อย... |
| 44 | A | M | Oh yeah? We'll do it! / Ask her some more about the cat. | จริงเหรอ? เอาเลยครับ! / ถามรายละเอียดแมวเพิ่มอีกหน่อยสิ |
| 44 | B | M | Hey, that's right up my alley! / Cat got a name and description? | เฮ้ นี่แหละงานถนัดของผมเลย! / แมวมีชื่อกับลักษณะเป็นยังไงครับ? |
| 45 | A | - | But Yagami-kun! | แต่ยากามิคุง! |
| 45 | B | - | Hey, Yagami-kun! | เฮ้ ยากามิคุง! |
| 46 | A | M | Chako. And she's five? | ชาโกะ แล้วอายุห้าขวบใช่ไหมครับ? |
| 46 | B | - | Chako, five-year old female? | ชาโกะ ตัวเมียอายุห้าขวบใช่ไหม? |
| 47 | A | M | Just send us a picture, yeah? | ส่งรูปมาให้เราหน่อยนะครับ? |
| 47 | B | M | Send us pictures, okay? | ส่งรูปมาให้เราหน่อยนะครับ |
| 48 | A | - | All right, / time to get some catnip at Don Quijote! | เอาล่ะ / ได้เวลาไปซื้อต้นแคทนิปที่ Don Quijote แล้ว! |
| 48 | B | - | Nice, I'll pick up some / catnip at Don Quijote! | เยี่ยม ผมจะไปซื้อ / ต้นแคทนิปที่ Don Quijote เลย! |
| 49 | A | - | Kaito-san. | ไคโตะซัง |
| 49 | B | - | Kaito-san... | ไคโตะซัง... |
| 50 | A | - | This is our first job in a while. | นี่เป็นงานแรกในรอบนานเลยนะ |
| 50 | B | - | We haven't had a job in a while... | ไม่มีงานเข้ามานานแล้วแฮะ... |
| 51 | A | - | Now let's go find that lady's cat! | ไปตามหาแมวของคุณลูกค้าคนนั้นกันเถอะ! |
| 51 | B | - | Let's do it right! | มาไล่เรียงเรื่องให้ถูกต้องกันเถอะ! |

## a01_060 (หญิง 3 · ชาย 14)

| # | ชุด | เพศ | EN | TH |
|---|---|---|---|---|
| 1 | A | - | Hey there, Saori-san. | ไง ซาโอริซัง |
| 1 | B | - | Yo, Saori-san.　 | เฮ้ ซาโอริซัง |
| 2 | A | - | Look, dorayaki. / Extra fancy. | ดูนี่สิ โดรายากิ / รุ่นพิเศษเลยนะ |
| 2 | B | - | I brought dorayaki. / Limited edition... | ผมเอาโดรายากิมาฝาก / รุ่นลิมิเต็ดเอดิชั่นด้วยนะ... |
| 3 | A | - | Genda Law Office, / where I used to work. | สำนักงานกฎหมายเก็นดะ / ที่ที่ผมเคยทำงานอยู่ |
| 3 | B | - | This is Genda Law Office, / where I used to work. | นี่คือสำนักงานกฎหมายเก็นดะ / ที่ที่ผมเคยทำงาน |
| 4 | A | - | Things haven't changed / much these past three years. | อะไร ๆ ก็ไม่ค่อยเปลี่ยนไป / มากนักตลอดสามปีที่ผ่านมา |
| 4 | B | - | I left three years ago, / so the staff's changed a bit. | ผมออกมาตั้งแต่สามปีก่อน / พนักงานเลยเปลี่ยนไปบ้าง |
| 5 | A | M | Hello, Yagami-san. | สวัสดีครับ ยากามิซัง |
| 5 | B | M | Hi, Yagami-san. | หวัดดีครับ ยากามิซัง |
| 6 | A | - | Oh, I didn't see you there. / You getting situated?  | โอ้ ไม่เห็นคุณอยู่ตรงนั้นเลย / เข้าที่เข้าทางกันดีไหม? |
| 6 | B | - | Hoshino-kun, hey. / Getting situated? | โฮชิโนะคุง ไง / เข้าที่เข้าทางกันดีไหม? |
| 7 | A | M | Yes. / Everyone here is just great. | ครับ / ทุกคนที่นี่ดีมากเลยครับ |
| 7 | B | M | Yeah, everyone here's great. | ครับ ทุกคนที่นี่ดีมากเลยครับ |
| 8 | A | F | So I hear you're good. / Passed the bar with top marks and everything. | ได้ยินมาว่าคุณเก่งนี่ / สอบเนติบัณฑิตได้คะแนนอันดับต้น ๆ เลยด้วย |
| 8 | B | - | Heard you're pretty good? / Top of your class on the bar? | ได้ยินว่าฝีมือดีนี่? / สอบเนติบัณฑิตได้ที่หนึ่งของรุ่นเลยเหรอ? |
| 9 | A | - | How'd you end up in this dump / and not in a bigger office, huh? | แล้วมาลงเอยที่ออฟฟิศกระจอก ๆ นี่ได้ไง / ทำไมไม่ไปสำนักงานใหญ่ ๆ ล่ะ? |
| 9 | B | - | So why didn't you join a bigger firm? | แล้วทำไมไม่ไปเข้าสำนักงานใหญ่ ๆ ล่ะ? |
| 10 | A | - | Huh? Well you see, that's, uh... | หา? เอ่อ ก็คือว่า...นั่นมัน... |
| 10 | B | M | Oh, well, you know... | อ้อ ก็คือ...รู้ไหมครับ... |
| 11 | A | - | I hear you over there, Yagami. | ได้ยินอยู่นะ ยากามิ |
| 11 | B | - | I can hear you, Yagami. | ผมได้ยินอยู่นะ ยากามิ |
| 12 | A | M | Evening, Genda-sensei. | สวัสดีครับ เก็นดะเซนเซ |
| 12 | B | M | Genda-sensei! Hello! | เก็นดะเซนเซ! สวัสดีครับ! |
| 13 | A | - | Other than my real dad, there's / two people I look up to like a father. | นอกจากพ่อแท้ ๆ ของผมแล้ว / ยังมีอีกสองคนที่ผมนับถือเหมือนพ่อ |
| 13 | B | - | I've got three people I look up to / like a father. My actual dad being one. | ผมมีคนที่นับถือเหมือนพ่อ / อยู่สามคน พ่อแท้ ๆ ของผมเป็นหนึ่งในนั้น |
| 14 | A | - | Genda-sensei's one of those people. | เก็นดะเซนเซเป็นหนึ่งในนั้น |
| 14 | B | - | Genda-sensei is another. | เก็นดะเซนเซก็เป็นอีกคนหนึ่ง |
| 15 | A | - | He gave me a job here before I'd / even gotten outta law school. | อาจารย์ให้งานผมทำที่นี่ / ตั้งแต่ผมยังไม่จบโรงเรียนกฎหมายด้วยซ้ำ |
| 15 | B | - | He let me work here / before I even became a lawyer. | อาจารย์ให้ผมทำงานที่นี่ / ก่อนที่ผมจะเป็นทนายความด้วยซ้ำ |
| 16 | A | M | Shintani-sensei out for the night? | ชินทานิเซนเซออกไปแล้วเหรอครับคืนนี้? |
| 16 | B | M | Where's Shintani-sensei? | ชินทานิเซนเซอยู่ไหนครับ? |
| 17 | A | - | I can't keep track of that boy. | ผมตามเด็กคนนั้นไม่ทันจริง ๆ |
| 17 | B | - | Haven't seen him in a bit. | ไม่เห็นเขาอยู่พักหนึ่งแล้วนะ |
| 18 | A | - | I'm sure you're happy, though. / You don't have to deal with him. | แต่ผมว่าคุณคงดีใจอยู่นะ / ที่ไม่ต้องเจอกับเขา |
| 18 | B | - | Works out for you though, right? / You dodged him. | ก็ดีสำหรับคุณแล้วนี่ ใช่ไหม / รอดตัวไปเลย |
| 19 | A | - | Huh? | หา? |
| 19 | B | - | Huh? | หา? |
| 20 | A | - | You two can't stand each other. | สองคนนั้นทนกันไม่ได้เลยนะ |
| 20 | B | - | Don't you hate each other's guts? | เกลียดขี้หน้ากันสุด ๆ เลยไม่ใช่เหรอ? |
| 21 | A | - | You hate each other's guts. / Be honest with me here. | เกลียดขี้หน้ากันชะมัด / พูดตรง ๆ กับผมมาเถอะน่า |
| 21 | B | - | Both of you think the other's an idiot. | ทั้งคู่คิดว่าอีกฝ่ายมันโง่ทั้งนั้นแหละ |
| 22 | A | M | Hold on now. / Shintani's like a mentor to me. | เดี๋ยวก่อนนะครับ / ชินทานิเหมือนอาจารย์ของผมเลยนะ |
| 22 | B | - | C'mon, I respect the guy like a mentor. | ไม่เอาน่า ผมนับถือเขาเหมือนอาจารย์เลยนะ |
| 23 | A | M | So... About that job you have. | งั้น...เรื่องตำแหน่งที่อาจารย์ทำอยู่น่ะครับ |
| 23 | B | - | I don't think he's an idiot. | ผมไม่คิดว่าเขาโง่หรอกนะ |
| 24 | A | - | If you really want that job, / you're gonna have to get along. | ถ้าอยากได้ตำแหน่งนั้นจริง ๆ / คุณต้องเข้ากับเขาให้ได้ก่อนนะ |
| 24 | B | - | You ever want my job, / you need to get along with him. | ถ้าอยากได้ตำแหน่งของผมสักวัน / คุณต้องเข้ากับเขาให้ได้ |
| 25 | A | - | So show your senpai / a little more respect. | งั้นก็ให้เกียรติรุ่นพี่ / ของคุณสักหน่อยสิ |
| 25 | B | - | Show some respect to your sensei. | ให้ความเคารพอาจารย์ของคุณหน่อยสิ |
| 26 | A | - | Oh, Genda-sensei. | อ้าว เก็นดะเซนเซ |
| 26 | B | - | Whoa, Genda-sensei. | โห เก็นดะเซนเซ |
| 27 | A | M | I got you some dorayaki. | ผมเอาโดรายากิมาฝากด้วยนะครับ |
| 27 | B | M | How does dorayaki sound? | โดรายากิเป็นไงครับ? |
| 28 | A | M | Just sit right there. / I'll grab you one. | นั่งตรงนั้นก่อนนะครับ / เดี๋ยวผมหยิบให้ |
| 28 | B | - | I think you'll really / like 'em, they're... | ผมว่าอาจารย์ต้องชอบแน่ ๆ / มันคือ... |
| 29 | A | - | Huh? | หา? |
| 29 | B | - | Huh? | หา? |
| 30 | A | - | Saori? | ซาโอริ? |
| 30 | B | - | Really? | จริงเหรอ? |
| 31 | A | - | Did you... eat them all? | คุณ...กินหมดเลยเหรอ? |
| 31 | B | - | Are they all... gone? | หมดไปแล้ว...เหรอเนี่ย? |
| 32 | A | F | All but half. / Hope you don't mind. | เหลืออยู่ครึ่งเดียวค่ะ / หวังว่าคงไม่ว่ากันนะคะ |
| 32 | B | F | There's a... half left. | เหลืออยู่...ครึ่งหนึ่งค่ะ |

## a01_090 (หญิง 2 · ชาย 21)

| # | ชุด | เพศ | EN | TH |
|---|---|---|---|---|
| 1 | A | M | Here, right this way. | เชิญทางนี้เลยครับ |
| 1 | B | M | Right this way. | เชิญทางนี้เลยครับ |
| 2 | A | - | The Matsugane are an / offshoot of the Tojo Clan. | ตระกูลมัตสึกาเนะเป็น / สาขาย่อยของตระกูลโทโจ |
| 2 | B | - | The Tojo Clan's Matsugane Family... | ตระกูลมัตสึกาเนะของตระกูลโทโจ... |
| 3 | A | - | Not the biggest yakuza / family on the block. | ไม่ใช่ตระกูลยากูซ่า / ที่ใหญ่ที่สุดในย่านนี้หรอก |
| 3 | B | - | Not exactly the biggest family on the block. | ไม่ใช่ตระกูลที่ใหญ่ที่สุดในย่านนี้ซะทีเดียว |
| 4 | A | - | They're a small branch / that's low on the tree. | เป็นแค่สาขาเล็ก ๆ / ที่อยู่ล่างสุดของตระกูล |
| 4 | B | - | They're bottom rung. / A "branch" family to those in the know. | อยู่ล่างสุดของสายตระกูล / เป็น "ตระกูลสาขา" สำหรับคนที่รู้เรื่องจริง ๆ |
| 5 | A | M | But the family's patriarch, / Mitsugu Matsugane, is like a father to me. | แต่โอยาบุนของตระกูล / มิตสึกุ มัตสึกาเนะ เป็นเหมือนพ่อของผม |
| 5 | B | - | But to me and Kaito-san, / their patriarch, Mitsugu Matsugane... | แต่สำหรับผมกับไคโตะซัง / โอยาบุนของพวกเขา มิตสึกุ มัตสึกาเนะ... |
| 6 | A | - | And Kaito-san. | แล้วก็ไคโตะซัง |
| 6 | B | - | ...is like a father. | ...เป็นเหมือนพ่อ |
| 7 | A | M | Excuse me.  / Yagami-san is here to pay you a visit. | ขออนุญาตครับ / ยากามิซังมาเยี่ยมท่านครับ |
| 7 | B | M | Boss. / Yagami-san is here to see you. | ท่านครับ / ยากามิซังมาพบท่านครับ |
| 8 | A | - | Oh, so good to see / you again, my boy. | โอ้ ดีใจจริง ๆ ที่ได้เจอ / คุณอีกครั้งนะ ไอ้หนุ่ม |
| 8 | B | - | Oh, it's been a while, my boy. | โอ้ ไม่เจอกันนานเลยนะ ไอ้หนุ่ม |
| 9 | A | - | Now then, feels like ages / since you last stopped by. | เอาล่ะ รู้สึกเหมือนผ่านไปนานมาก / ตั้งแต่คุณแวะมาครั้งล่าสุด |
| 9 | B | - | Why don't you ever stop by anymore? | ทำไมไม่ค่อยแวะมาหาผมเลยล่ะ? |
| 10 | A | M | I know. / I wonder why that is, huh? | ก็นั่นสิครับ / สงสัยเหมือนกันว่าทำไมนะ? |
| 10 | B | M | You wanna know why that is? | อยากรู้ไหมครับว่าทำไม? |
| 11 | A | - | Could it be that you're the / only one who's glad to see me? | หรือว่าเป็นเพราะท่าน / คือคนเดียวที่ดีใจที่ได้เจอผมกันแน่? |
| 11 | B | - | Because you're the only one / here who's glad to see me. | เพราะท่านเป็นคนเดียว / ที่นี่ที่ดีใจได้เจอผมไง |
| 12 | A | - | Well, you have a point there. | ก็จริงของคุณอยู่นะ |
| 12 | B | - | Guess you have a point. | ก็คงจริงอย่างที่ว่า |
| 13 | A | - | How's Kaito these days? / Staying out of trouble? | ช่วงนี้ไคโตะเป็นยังไงบ้าง / ไม่หาเรื่องใช่ไหม? |
| 13 | B | - | How's Kaito? Still doing well? | ไคโตะเป็นยังไงบ้าง ยังสบายดีอยู่ไหม? |
| 14 | A | M | He's okay.  | เขาก็สบายดีครับ |
| 14 | B | M | He's fine. | เขาสบายดีครับ |
| 15 | A | - | If not for that incident, / he'd still be part of the family, you know. | ถ้าไม่ใช่เพราะเหตุการณ์นั้น / เขาก็คงยังอยู่กับตระกูลนี้อยู่นะ |
| 15 | B | - | If it hadn't been for that mess, / he'd still be one of us, you know. | ถ้าไม่ใช่เพราะเรื่องยุ่งเหยิงนั้น / เขาก็คงยังเป็นพวกเราอยู่นะ |
| 16 | A | - | Hard to believe it's / already been a year. | ไม่อยากเชื่อเลยว่า / ผ่านมาเป็นปีแล้ว |
| 16 | B | - | Has a whole year really gone by? | ผ่านมาเป็นปีเต็ม ๆ แล้วจริง ๆ เหรอเนี่ย? |
| 17 | A | - | Bah, the both of you were more / or less the sons I never had. | ช่างเถอะ พวกคุณทั้งสองคน / ก็เหมือนลูกชายที่ผมไม่เคยมีนั่นแหละ |
| 17 | B | - | The both of you were like / sons to me, you know. | พวกคุณทั้งคู่เหมือนลูกชาย / ของผมเลยนะ รู้ไหม |
| 18 | A | - | The past is what it is.  | อดีตก็คืออดีต |
| 18 | B | - | What's done is done. | อะไรที่ทำไปแล้วก็แล้วไป |
| 19 | A | - | True. | จริงด้วย |
| 19 | B | - | True... | จริงด้วย... |
| 20 | A | - | But I'm glad to hear / he's doing well... under your watch. | แต่ผมก็ดีใจนะที่ได้ยิน / ว่าเขาสบายดี...ภายใต้การดูแลของคุณ |
| 20 | B | - | But if he's doing well with you... / I'm happy. | แต่ถ้าเขาสบายดีเมื่ออยู่กับคุณ... / ผมก็มีความสุขแล้ว |
| 21 | A | - | I'm sure Kaito-san will / always... feel like my aniki. | ผมมั่นใจว่าไคโตะซัง / จะยังคงเป็นลูกพี่ของผมตลอดไป |
| 21 | B | - | It still feels like Kaito-san is my aniki. | ไคโตะซังก็ยังคงเป็นลูกพี่ของผมอยู่เสมอ |
| 22 | A | M | If not for you, I would have taken another direction / in life. I'd be a very different person I think. | ถ้าไม่มีท่าน ผมคงเลือกเดินไปอีกทาง / ในชีวิต คงเป็นคนละคนกับตอนนี้เลยครับ |
| 22 | B | - | If I hadn't met you two twenty years ago, / I'd be a very different person now. | ถ้าผมไม่ได้เจอทั้งสองคนเมื่อยี่สิบปีก่อน / ตอนนี้ผมคงเป็นคนละคนไปแล้ว |
| 23 | A | - | You'd have turned out / just fine, my boy. | คุณก็คงเติบโตมาดี / อยู่แล้วแหละ ไอ้หนุ่ม |
| 23 | B | - | Except you're still a good kid at heart! | แต่ลึกๆ แล้วนายก็ยังเป็นเด็กดีเหมือนเดิมนั่นแหละ! |
| 24 | A | - | Excuse me. | ขอโทษนะ |
| 24 | B | - | Excuse me. | ขอโทษนะ |
| 25 | A | F | Tea. | ชาค่ะ |
| 25 | B | F | Here you go. | นี่จ้ะ รับไปเลย |
| 26 | A | - | So then... | งั้นก็เลย... |
| 26 | B | - | So? | แล้วไง? |
| 27 | A | - | What would drag you back to an office / where you're not exactly welcome? | อะไรจะทำให้นายยอมกลับมาที่ออฟฟิศ / ที่นายไม่ค่อยเป็นที่ต้อนรับนักล่ะ? |
| 27 | B | - | What drags you into an office / where you're unwelcome? | อะไรทำให้นายมาที่ออฟฟิศ / ที่นายไม่เป็นที่ต้อนรับล่ะ? |
| 28 | A | M | Hamura is giving me some grief. | ฮามุระสร้างปัญหาให้ผมอยู่ครับ |
| 28 | B | M | It's about Captain Hamura.　 | เรื่องของกัปตันฮามุระน่ะครับ |
| 29 | A | - | Is he now? | งั้นเหรอ? |
| 29 | B | - | Oh, that? | อ๋อ เรื่องนั้นเหรอ? |
| 30 | A | - | I was under the assumption / Genda is handling the issue. | ผมนึกว่า / เก็นดะกำลังจัดการเรื่องนี้อยู่ซะอีก |
| 30 | B | - | We asked Genda-san to defend him. | เราขอให้เก็นดะซังช่วยแก้ต่างให้เขาแล้ว |
| 31 | A | - | Are you helping him / out with the case now? | นายกำลังช่วยเขา / ในคดีนี้อยู่ด้วยเหรอ? |
| 31 | B | - | Are you helping out with that, too? | นายช่วยเรื่องนั้นด้วยเหรอ? |
| 32 | A | M | Shintani's got me looking / for the Kyorei Clan. | ชินทานิให้ผมตามหา / ตระกูลเคียวเรอิอยู่ครับ |
| 32 | B | M | The Kyorei Clan has a base / in Kamurocho, right? | ตระกูลเคียวเรอิมีฐานอยู่ / ในคามุโรโจใช่ไหมครับ? |
| 33 | A | M | Just need to find them, / so I can ask them a few things. | แค่ต้องหาตัวพวกเขาให้เจอ / จะได้ถามอะไรสักสองสามอย่างครับ |
| 33 | B | M | I need to find it so I can ask a few things. | ผมต้องหาที่นั่นให้เจอ จะได้ถามอะไรหน่อยครับ |
| 34 | A | - | Not wise, my boy. You do know / they're all up in arms right now. | ไม่ฉลาดเลยนะ ไอ้หนู นายก็รู้ดี / ว่าตอนนี้พวกมันกำลังฮึกเหิมกันสุดขีด |
| 34 | B | - | You know they're all / up in arms right now, right? | นายก็รู้อยู่แล้วนี่ / ว่าตอนนี้พวกมันกำลังฮึกเหิมกันสุดขีด? |
| 35 | A | - | Sure you want this? | แน่ใจเหรอว่าจะทำแบบนี้? |
| 35 | B | - | You sure that's wise? | แน่ใจเหรอว่ามันฉลาด? |
| 36 | A | M | Don't worry. / I just want to have a word. | ไม่ต้องห่วงครับ / ผมแค่อยากคุยด้วยสักหน่อย |
| 36 | B | M | I just want to have a word. | ผมแค่อยากคุยด้วยสักหน่อยครับ |
| 37 | A | - | Does the name the Kajihira Group / mean anything to you? | ชื่อกลุ่มคาจิฮิระ / คุ้นหูนายไหม? |
| 37 | B | - | Heard of a construction company / called the Kajihira Group? | เคยได้ยินชื่อบริษัทก่อสร้าง / ที่ชื่อกลุ่มคาจิฮิระไหม? |
| 38 | A | M | No. Can't say that it does. | ไม่เลยครับ ไม่คุ้นหูเท่าไหร่ |
| 38 | B | - | No, not really. | เปล่า ไม่คุ้นเลย |
| 39 | A | - | They're a Kansai outfit. | เป็นแก๊งจากคันไซน่ะ |
| 39 | B | - | They're big in Kansai. | พวกมันใหญ่โตในคันไซเลยล่ะ |
| 40 | A | - | It's... They've got a front in the city. / The KJ Art office down on Senryo Avenue.  | คือ... พวกมันมีหน้าฉากอยู่ในเมืองด้วย / สำนักงาน KJ Art แถวถนนเซ็นเรียว |
| 40 | B | - | Anyway, they've got an office / called KJ Art on Senryo Avenue. | ยังไงก็เถอะ พวกมันมีสำนักงาน / ชื่อ KJ Art อยู่บนถนนเซ็นเรียว |
| 41 | A | - | Be careful, though. There's Kyorei crawling on every floor. / These are Tojo Clan streets, but that's their turf now. | แต่ระวังตัวไว้ด้วยล่ะ มีพวกเคียวเรอิยั้วเยี้ยอยู่ทุกชั้น / แถวนี้เป็นถนนของตระกูลโทโจ แต่ตอนนี้กลายเป็นเขตของพวกมันไปแล้ว |
| 41 | B | - | That whole building is theirs. / And that's where you'll find the Kyorei Clan. | ตึกทั้งตึกเป็นของพวกมัน / นั่นแหละคือที่ที่นายจะเจอตระกูลเคียวเรอิ |
| 42 | A | - | Senryo Avenue. KJ Art, eh. | ถนนเซ็นเรียว KJ Art สินะ |
| 42 | B | M | Senryo Avenue, KJ Art, right? | ถนนเซ็นเรียว KJ Art ใช่ไหมครับ? |
| 43 | A | M | I'll check it out. | ไปดูให้ครับ |
| 43 | B | - | Got it. | ได้เลย |
| 44 | A | - | I know you're busy... | รู้แหละว่านายยุ่งอยู่... |
| 44 | B | - | Sounds like you're a busy guy. | ท่าทางนายจะยุ่งน่าดูเลยนะ |
| 45 | A | - | Although, you think I could visit your office / some day soon? Keep it on the downlow? | แต่นายว่าสักวันผมจะไปเยี่ยม / ที่ออฟฟิศนายได้ไหม? แบบไม่ให้ใครรู้น่ะ |
| 45 | B | - | You know, I'd like to visit your office / sometime. Our secret, of course. | จริงๆ แล้วผมอยากไปเยี่ยม / ออฟฟิศนายสักครั้งนะ เก็บเป็นความลับกันแค่เราสองคน |
| 46 | A | - | Yeah, of course. | ใช่ แน่นอนอยู่แล้ว |
| 46 | B | - | Yeah, of course. | ใช่ แน่นอนอยู่แล้ว |

