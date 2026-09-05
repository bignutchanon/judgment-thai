# Vietnamese fan-translation leads for Judgment / Lost Judgment (Dragon Engine)

Research date: 2026-08-20. Goal: find a Vietnamese Judgment/Lost Judgment mod and evidence of
how they render Vietnamese glyphs (proportional spacing? diacritic stacking?), since this
engine lays out non-Latin glyphs at fixed full-cell pitch and we need to know whether anyone
has already beaten the spacing problem. No mod files were downloaded or executed; only web
pages and forum-hosted screenshot attachments (images, not game files) were fetched for
visual inspection.

## 1. Best evidence found: Lost Judgment, "The Red Team" — VERIFIED screenshots

**The Red Team** (theredteam.vn) is an active Vietnamese fan-translation group with its own
forum. They have a released/announced Lost Judgment Vietnamese patch:

- Forum release thread: https://forum.theredteam.vn/threads/pc-lost-judgment-viet-hoa-truy-tim-cong-ly.1835/
  (posted 2026-05-12, by user "L.M", in the "Dự Án Đã Phát Hành" / Released Projects section)
- Landing/download page: https://theredteam.vn/lost-judgment-viet-hoa — lists platform
  "STEAM, PS5", last updated 15/07/2026, credits "DỊCH GIẢ THE RED TEAM" (translators) and
  "KỸ THUẬT THE RED TEAM" (technical/engineering) as separate roles, install instructions
  are a simple installer ("ấn vào logo chữ R để chọn đường dẫn ... ấn Cài Đặt"), and a
  PS5 variant is mentioned as "có hướng dẫn kèm theo" (guide included in the archive).
  **At fetch time the page literally said "Game này không có bản Việt Hoá"** (no download
  currently live) — the file is distributed through "Thinkmay Cloud PC", a Vietnamese
  cloud-PC/file service, and download count shown was 0, so the public download is either
  gated, cloud-only, or not actually live yet despite the announcement. CLAIMED that a patch
  exists; VERIFIED that the release post and screenshots are real.

**Screenshots (VERIFIED — downloaded the actual JPEG attachments from
forum.theredteam.vn/attachments/... and viewed them directly, not just search snippets):**

6 real 1920x1080 gameplay/cutscene screenshots were attached to the release thread. All show
the game's bottom-of-screen subtitle captions translated into Vietnamese with full diacritics
(ả, ầ, ố, ệ, ữ, ẳ, etc.). Key observations:

- **Letter spacing is normal/proportional**, not widely spaced or monospaced — it reads like
  ordinary subtitle text, comparable in density to the English subtitle overlays in the same
  UI style. This is the opposite of the "fixed full-cell pitch" problem we're worried about
  for Thai.
- **Diacritics stack correctly** — tone/vowel marks sit properly over/under the base letter
  in every screenshot (e.g. "thất vọng", "chỗ đứng", "gặp lại", "Lần này... đứng ra bảo vệ").
  No visible misalignment.
- **One screenshot (attachment 4237) shows a rendering bug**: the line "Rồi tới lúc có
  chuyện▯ tao cũng có người chống lưng." has a **blank/tofu placeholder glyph** (a plain
  white box) where a punctuation mark (likely a comma or dash) should be. This is concrete
  evidence that their font-slot remap did not cover every punctuation character, even though
  the Latin+diacritic letters themselves render fine.
- One screenshot (a character-credits screen, "Takayuki Yagami / English Voice / Takuya
  Kimura") is untouched English UI text — not evidence of anything, included for context.

**Interpretation for our project:** Vietnamese uses the Latin base alphabet with combining
diacritics (mostly precomposed Vietnamese Unicode codepoints), which is a different problem
from injecting a wholly non-Latin script like Thai. It's likely the Dragon Engine's font
system already carries correct per-glyph advance widths for extended-Latin codepoints
(needed for French/German/Portuguese official localizations), so Vietnamese "just works" by
occupying those existing slots — it does not prove the engine can do proportional advance for
newly-injected non-Latin slots (which is our actual Thai problem). It DOES prove the engine's
text renderer is capable of proportional spacing in general (it isn't hard-locked to
monospace), and the tofu-box bug is a useful cautionary data point about incomplete glyph
coverage.

Screenshots were saved locally only to the session scratchpad for inspection (not copied into
the project) since the task says not to add mod files to the repo; if you want them kept,
say so and I'll copy the JPEGs into `docs/research_web/`.

## 2. Judgment (part 1) — no in-game screenshot evidence found

Multiple Vietnamese sites reference a "Judgment Việt Hóa" but none yielded a viewable
in-game screenshot:

- https://meviethoa.com/269/judgment-viet-hoa/ — **404**, page removed/never existed at that
  slug.
- https://thichviethoa.wordpress.com/2026/07/29/judgment-viet-hoa/ — page exists, but the
  only image on it is the official Steam box-art banner (verified — downloaded and viewed
  it, no Vietnamese text). Translation itself is gated: "chỉ có trong vip" (VIP-members
  only). Contact: Discord invite `discord.com/invite/pdwUkwAumB`, VIP-registration link
  `thichviethoa.wordpress.com/gioi-thieu/`.
- https://tamhongame.com/game-detail/judgment-viet-hoa-full/2778 and
  https://ddat14game.com/Home/DetailsProduct/18837 — both are third-party "pre-cracked +
  pre-translated" repack mirror sites (not the translation team's own site); both refused to
  load for inspection (timeout / empty response) and, per rules, we did not attempt to
  download their archives anyway — these repost someone else's translation bundled with a
  pirated game copy, so they're not useful as a technical source and are flagged CLAIMED
  only ("Judgment V1.12 Việt Hoá Sẵn" per search snippet).
- YouTube videos "JUDGMENT (Việt Hóa) - Tập 1" (watch?v=dZBp8w18Arw) and "Judgment Việt Hóa
  Demo" (watch?v=0uQTmWWfI3o) were found by title/search snippet only; the second one's
  uploader account has since been terminated (video gone), and the first could not be
  fetched for description/comments (401 from the metadata scrape). CLAIMED existence only —
  did not get to see either video's actual footage.

## 3. Recruiting thread — the only place technical pipeline details surfaced

https://viethoagame.com/threads/lap-team-dich-cho-nhung-du-an-viet-hoa-game-cua-studio-ryu-ga-gotoku-like-a-dragon-judgment-va-lost-judgment.886/
(posted 2025-03-27, last edited 2026-04-02, viethoagame.com forum) — a recruiting post by one
translator/tech person building a multi-title RGG localization effort (Like a Dragon Infinite
Wealth, Judgment, Lost Judgment, Gaiden, Pirate, Kiwami 2, Y6, Y7, Y0 Director's Cut, Kiwami 3,
Kiwami). This is **CLAIMED/self-reported, not independently verified** since we could not see
the actual font files:

- States they have **"handled font and text"** ("đã xử lý font chữ") for the series and will
  deal with images later — i.e. a self-reported claim of solved font work, with no
  screenshot or file attached in the fetched excerpt to verify it.
- Names tools: **reARMP**, **Reloaded II Mod Loader**, **Ultimate ASI Loader** — reARMP
  matches exactly the tool name our own project/K3 pipeline uses (`tools/reARMP_fixed.py`),
  which is a strong signal this person is working the same ARMP-text angle we are, though
  "Reloaded II" and "Ultimate ASI Loader" are generic/other-game modding tools (not the
  RGG-specific SRMM/Parless loader our CLAUDE.md names), so it's unclear if those two are
  actually used for the RGG titles specifically or just listed as tools this person knows.
- Progress as of the fetch: Judgment had 1 participant, Lost Judgment 2 (recruiting more),
  LaD Infinite Wealth 2 (recruiting more); everything else still "seeking translators" with
  no progress claimed.
- Contact: Discord handle **"kecox15670"** given as the point of contact for joining.
- No download links posted in the thread itself.

Separately, on The Red Team's own forum, a member (DarkGin) asked on 2026-07-03 **"Xin hỏi
các bác là trích xuất text trong các con game nhà RGG dùng dragon engine thì làm thế nào cho
hiệu quả ạ"** ("How do you effectively extract text from RGG's Dragon-Engine games?") in the
technical help section —
https://forum.theredteam.vn/threads/ve-dragon-engine-trong-yakuza-va-judgment.1955/ —
**and got zero replies** (verified by fetching the raw thread; only the original post exists,
followed immediately by the login-to-reply footer). This is useful negative evidence: even
inside the most active Vietnamese translation community we found, Dragon Engine text
extraction is *not* a solved, publicly-documented technique as of this writing — it doesn't
contradict the Red Team's own Lost Judgment release (their "KỸ THUẬT" person presumably knows
it and just hasn't written it up publicly), but no public writeup, guide, or tool-share for
Dragon Engine specifically exists on either forum we checked.

A tangential but real technique thread exists for a different problem (Unity SDF fonts, not
Dragon Engine): https://forum.theredteam.vn/threads/xoa-font-sdf-de-viet-hoa-font.1909/
describes deliberately deleting/corrupting a Unity game's primary SDF font asset so the
engine falls back to a secondary font that already has full Vietnamese glyph coverage — a
"break it to force fallback" trick. Not applicable to Dragon Engine's `FONT!`/ARMP pipeline,
just noted in case the concept (force a fallback font that has full coverage) is useful.

## 4. Other Yakuza/Dragon Engine Vietnamese mods (context, not this game)

- Yakuza: Like a Dragon — VOZ forum thread "Yakuza Like a Dragon Việt hóa - GG dịch"
  (https://voz.vn/t/yakuza-like-a-dragon-viet-hoa-gg-dich.1069810/) explicitly says the
  Vietnamese text is raw Google-Translate output ("GG dịch"), i.e. explicitly a low-quality
  MT pass, not hand-translated — same caveat as our own note about MOD2SUB for Judgment.
  Not RGG Dragon-Engine-font-relevant beyond confirming *a* Vietnamese patch exists for a
  Dragon Engine RGG title.
- meviethoa.com lists "Yakuza: Like a Dragon Việt ngữ" and "Like a Dragon: Ishin! Việt Hóa"
  pages (https://meviethoa.com/tag/yakuza-like-a-dragon-viet-ngu/,
  https://meviethoa.com/964/like-a-dragon-ishin-viet-hoa/) — found by search snippet only,
  not opened in this pass; worth a follow-up fetch since Like a Dragon/Ishin are closer in
  engine vintage to Judgment than the Unreal-Engine-oriented threads on The Red Team.

## 5. Contact channels summary

| Team | Discord | Facebook | Other |
|---|---|---|---|
| The Red Team | discord.com/invite/theredteamvn | facebook.com/TheRedTeam.Viethoa | YouTube @theredteam906, forum.theredteam.vn |
| Thích Việt Hoá | discord.com/invite/pdwUkwAumB | — | thichviethoa.wordpress.com (VIP gate for downloads) |
| Mê Việt Hóa | invite link present on site (not captured) | — | email meviethoa@gmail.com |
| viethoagame.com recruiting thread | handle "kecox15670" | — | viethoagame.com forum account |

## 6. Recommended follow-up if this matters enough to pursue

1. Message The Red Team's Discord/Facebook directly and ask their "KỸ THUẬT" (technical)
   person how they handled font glyph advance for Lost Judgment — they clearly have a
   working, mostly-correct-looking pipeline (per the screenshots) but have not published it.
2. Ask specifically about the tofu-box bug seen in attachment 4237 — confirms whether it's a
   known/ignored gap in their punctuation glyph table.
3. If they respond, request (don't demand) their font tool or a description of how they
   derived per-glyph advance values, and whether they special-cased anything for the
   Dragon-Engine `FONT!`/cell-based glyph sheet vs. relying on default engine metrics.
4. This does not resolve the Thai-specific problem (non-Latin injected glyphs at fixed
   pitch) since Vietnamese didn't need new slots — worth being upfront with them that our
   ask is different in kind, not just degree.
