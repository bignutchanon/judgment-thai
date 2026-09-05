# JP/TH community sweep — Dragon Engine font modding, title-screen bitmap fonts

Date: 2026-08-20. Scope: Japanese- and Thai-language web (English used as fallback / cross-check).
Method: WebSearch + WebFetch (auto-routed through r.jina.ai reader for JS-heavy/403 pages) + direct
`curl https://r.jina.ai/<url>`. No game files touched, no mods downloaded.

## Bottom line for the open question

**No Japanese-language, Thai-language, or English-language source anywhere documents the Dragon
Engine `FONT!` container format, or explains how a metrics-less title/menu bitmap font (like
`meta_ot_cond_book.dds`, `yakuza.dds`) is addressed.** This is a clean negative result across all
three language communities — nobody has publicly reverse-engineered this specific piece. The only
usable signal is a **structural precedent from the pre-Dragon-Engine RGG font pipeline** (Yakuza 0 /
Yakuza Kiwami, `font.par` → `hd2_hankaku.dds` / `hd_hankaku.dds`), which is VERIFIED in detail below
and is the closest real-world analogue to Judgment's metrics-less textures.

## VERIFIED: the old RGG "grid DDS, no metrics file" font convention

Source: GitHub issue [Kaplas80/TranslationFramework2#20 "Font for Yakuza 0"](https://github.com/Kaplas80/TranslationFramework2/issues/20)
(read via jina reader) + [ZenHAX "Yakuza 0 PC Text Tools!!!"](https://zenhax.com/viewtopic.php@t=9324.html)
+ [ModDB "Yakuza 0: HD Font (Main)" comment thread](https://www.moddb.com/games/yakuza-0/addons/yakuza-0-hd-font-main)
+ Steam guide [HD Font Mod (Yakuza 0)](https://steamcommunity.com/sharedfiles/filedetails/?id=1800436274).

- The font used in-game is a single DDS texture (`hd2_hankaku.dds` in `font.par`) that is a **fixed
  character grid with no companion metrics/index file at all**. Modders edit it directly in
  Photoshop/GIMP, cell by cell.
- **Cell position = codepoint position in the target codepage.** Default is ISO-8859-1 (Latin-1);
  a Spanish translator (Kaplas, the tool author) explicitly "reorder[ed] and add[ed] some characters
  to fit their positions with ISO-8859-1 code." A separate thread (issue #20) confirms someone tried
  swapping to **ISO-8859-11 (Thai)** by editing the tool's `Encoding.cs` — i.e., the community's own
  working model for "how do I get a non-Latin script into this bitmap font" is exactly "point the
  tool at a different single-byte codepage and place glyphs at that codepage's grid offset."
  Quote (paraphrased from the issue): *"the size and position of each character inside the image are
  important"* — replacements must land in-place, same cell, same size.
  - **CLAIMED/needs own verification for non-Latin range**: the issue also states that going beyond
    the codepage's native Latin range may additionally require **patching the game executable**, not
    just the data file — spacing/advance for extended characters was not guaranteed to be exposed in
    any editable data file.
- **Character spacing/kerning is NOT stored in the DDS or in a sidecar file — it lives in a table
  inside the game's `.exe`.** ZenHAX thread, Kaplas: the game exe contains a "char spacing table"
  that can be hand-edited or auto-adjusted by TranslationFramework2's "Auto ajustar" function. This
  is the single most load-bearing fact from this sweep: RGG has documented precedent for a bitmap
  font whose glyph metrics are **hardcoded outside of any font asset**, in the executable.
- This is Yakuza 0/Kiwami's *old engine* `font.par`, not Dragon Engine's `FONT!` container — but the
  filenames in Judgment's loose font folder (`meta_ot_cond_book.dds`, `yakuza.dds`, no `.bin`) look
  exactly like a **carried-over legacy grid font** sitting alongside the newer Y6-style `FONT!`
  metrics format (`tbgm_0p_ja.bin/.dds`), rather than a second instance of the same `FONT!` format.
  Testable hypothesis for this project: dump `meta_ot_cond_book.dds` as a grid, measure cell pitch,
  and try mapping ASCII 0x20–0x7E (then Latin-1 0xA0–0xFF) sequentially into the visible glyph cells
  — this is the exact convention the Yakuza 0-era tooling used, and Judgment shipping alongside
  legacy-style loose DDS with no `.bin` is consistent with it not having been ported to the `FONT!`
  scheme at all.

## Typeface identity: "Meta OT Condensed Book" is a real commercial name, not a made-up filename

CLAIMED only (snippet, not full source — see caveat below):
[Giant Bomb forum, "(UPDATE: Found it. It's called FF Meta) What Is the Subtitle Font Used in the
Yakuza Games Called?"](https://www.giantbomb.com/forums/general-discussion-30/update-found-it-its-called-ff-meta-what-is-the-sub-1868882/).
The search-result snippet states the Yakuza series' subtitle/body font was identified by the
community as **FF Meta** (Erik Spiekermann / FontFont family), and that a separate **"Yakuza Font"**
(named **Edo SZ**) is used for the main logo/title wordmark. I could not read the full thread — the
current Giant Bomb site requires login even through the reader proxy, so this is unverified beyond
the search snippet.
- This corroborates (but does not prove) that `meta_ot_cond_book(_italic).dds` in Judgment's font
  folder is literally an in-house-rasterized instance of **Meta Offc Pro / FF Meta, Condensed
  weight, Book style** — i.e., not a RGG-original font, a licensed commercial typeface baked to a
  bitmap. `yakuza.dds`/`yakuza_italic.dds` are separately named and most likely the game/franchise
  logo font (candidate: Edo SZ per the same claim), distinct from the Meta-based UI font. Both
  pairs are metrics-less textures, consistent with the "old grid convention, no `.bin`" reading above
  rather than two unrelated one-off formats.
- No Japanese-language source discusses either "Meta OT" or "Edo SZ" font choices for any Yakuza/
  Judgment title screen — searches for 龍が如く + フォント + タイトルロゴ / DDS / 解析 only surfaced
  DynaFont's own official case-study pages (which cover in-game dialogue fonts for Ishin Kiwami and
  Yakuza 8, e.g. traditional/simplified Chinese CJK fonts — never the Latin title/UI face, and never
  Judgment).

## Tooling sweep — nothing Dragon-Engine-`FONT!`-aware exists publicly

- **reARMP / LibARMP** (Ret-HZ) — ARMP `.bin` only (text tables), confirmed to list Judgment among
  supported games in its README. reARMP is explicitly marked obsolete, redirecting to LibARMP
  (still WIP). Neither repo, nor the rest of Ret-HZ's repo list (pxdArchiverCE, ParCrypt,
  Lib20070319, DungeonMaster, HEADER-7, etc.), contains anything font-related.
- **ParManager / ParLibrary** (Kaplas80) — generic PAR archive un/repacker (SLLZ compression incl.
  V2 for Kiwami 2), not font-aware.
- **TranslationFramework2** (Kaplas80) — the tool with the grid-font/codepage knowledge above, but
  it targets the **old engine only** (Yakuza 0/Kiwami); no Dragon Engine support was found in any
  issue or doc.
- **RyuModManager / ShinRyuModManager (SRMM)** — wiki confirms it loads "ALL game files, except
  `.usm` movies for all games, and `.cpk`/`.hca`/`.adx` audio for Yakuza 5 only." No documented
  per-file-type exception for fonts. This means the project's own empirical finding (title menu
  glyphs came out blank when a loose font drop-in was tested) is **not a documented/known SRMM
  limitation** — it's more likely an engine-side load-order/caching quirk specific to that asset
  (fonts loading before the mod hook attaches, per this project's own CLAUDE.md note), not something
  the wider community has hit and written up. Full wiki not read page-by-page under this sweep's time
  budget — worth a direct read of `Adding Loose Files` and `Supported Game Files` wiki pages if this
  needs re-litigating.
- No hit anywhere (note.com, Qiita, Zenn, Hatena, 5ch search snippets, GitHub search) for the string
  `FONT!` as a magic/container identifier, in Japanese or English.

## Thai-language community: no font work exists, only text swaps

- **MOD2SUB** (`nexusmods.com/judgment/mods/228`, already known to this project) — read in full via
  jina. It is a pure text replacement (Thai + English via Google MT) installed through
  RyuUpdater.exe → RyuModManager(GUI) → SRMM install flow (i.e., confirms Parless/SRMM is the
  standard install path Thai modders already use for Judgment). **It does not touch fonts at all** —
  it rides on the existing EN glyph set, which is why it can ship without any font work. No technical
  detail about `db.judge.en.par` or ARMP structure was in the description; this remains a
  proof-of-concept file-list reference only, per CLAUDE.md's existing caution.
- Other Thai RGG mods found: "Yakuza 0 Thai Mod Localization" (Nexus), "AzuNyanMoeChan Mod แปลไทย"
  (Steam group, Yakuza 0) — same pattern, text-only, no font injection, no Thai script rendering
  anywhere in the RGG modding scene as far as this sweep could find.
- **Pantip**: searched directly (`แปลไทย Yakuza ฟอนต์ แก้ dds`, `Judgment ฟอนต์ไทย`) — only
  discussion-of-the-game-itself threads turned up (story questions, "is Judgement Remastered worth
  it"). **No modding/technical threads about Yakuza or Judgment fonts exist on Pantip.** Clear
  negative result.
- No Thai Facebook group content was reachable (Facebook requires login; not attempted beyond what
  surfaced in search snippets, which was only the MOD2SUB credit line already captured above).

## Japanese-language community: clear negative on the specific question

- Searches across `龍が如く MOD フォント 差し替え`, `ジャッジアイズ MOD 日本語 フォント 解析`,
  `ロストジャッジメント MOD フォント 差し替え`, `龍が如く6 フォント 解析 DDS`, `FONT! マジックナンバー`,
  and 5ch-targeted queries surfaced **no** blog/note.com/Qiita/Zenn/5ch post that reverse-engineers
  any Dragon Engine font container, and no Japanese modder credited with documenting `FONT!`.
- The only Japanese font-modding content that exists for any Dragon Engine RGG title is a **red
  herring worth flagging for future sweeps**: a Steam guide literally titled
  "日本語フォントの差し替えについて" (id `3154220049`) appears in results for both "Lost Judgment mod"
  and general RGG font queries — but on full read it is a **Unity/TextMeshPro guide for an unrelated
  game, Book of Hours** (Weather Factory), not Lost Judgment. Steam's guide search/snippet matching
  is unreliable for this kind of query; don't trust title+snippet alone for Steam guide hits again.
- Official/commercial font attribution exists only for **in-game dialogue CJK fonts**, not UI/title:
  Dynacomware's own case-study pages confirm specific DynaFont typefaces for 龍が如く維新!極 (Ishin
  Kiwami: Traditional Chinese LiHei-Md/kaiShuW7-B5, Simplified HeiW9-GB/WeBeiW7-GB) and 龍が如く8
  (Japanese 綜藝体, Traditional DFPMingSUBold-B5, Simplified DFSongW9-GB). Nothing for Judgment/Lost
  Judgment, and nothing about the Latin title/menu face in any game.
- One genuinely useful indirect data point: 伊東豊 (RGG Studio technical lead)'s own X/Twitter post
  confirms Yakuza Kiwami-era games expose a **user-facing font-style toggle** (Mincho/明朝体 vs.
  Gothic/ゴシック体) via in-game settings — orthogonal to this project's problem, but confirms RGG's
  font system is generally built to support multiple named font assets switchable at runtime, which
  is at least consistent with a game shipping multiple distinct font containers (`tbgm_0p_ja`,
  `gothic`, `meta_ot_cond_book`, `yakuza`) simultaneously rather than one of them being dead/unused
  data.

## Recommended next step (not web research — direct binary work)

Given the total absence of external documentation, the fastest path is empirical, mirroring the
Yakuza 0-era method that *is* documented: open `meta_ot_cond_book.dds` and `yakuza.dds` as plain grids,
measure cell size against the texture dimensions, and test-fit ASCII/Latin-1 codepage order glyph-by-
glyph the way Kaplas's community did for `hd2_hankaku.dds`. If the game's executable exposes any
readable "char spacing"-style table (the documented old-engine precedent), that is the next place to
look for metrics if the grid-order hypothesis needs precise per-glyph advance values.

## Search log (queries that returned nothing useful, for future reference)

`Dragon Engine FONT container format reverse engineering RGG` (English) — generic RE guides only.
`github Dragon Engine RGG font tool FONT parser python` — unrelated fonttools/font-dev libraries only.
`"font.par" OR "FONT!" 龍が如く 判別 バイナリ 構造` — nothing indexed.
`龍が如く タイトル画面 フォント ビットマップ 差し替え 5ch` — no 5ch results surfaced at all.
`note.com 龍が如く 極 データ解析 par arc ファイル` — no technical note.com posts found.
`龍が如く7 光と闇の行方 フォント par ARMP MOD 解析 ブログ` — nothing.
`modding.wiki Dragon Engine RGG font format documentation` — no such wiki page exists.
