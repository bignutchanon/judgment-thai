# Runtime patching feasibility — Judgment (2022) / Lost Judgment (2021) PC

Scope: DRM status, existing hook/injection frameworks, and RE precedent for these two
Dragon Engine Steam ports. Researched 2026-08-20 via WebSearch/WebFetch/curl. PCGamingWiki
was unreachable all session (Cloudflare 403 on direct fetch, jina proxy, and Wayback
Machine snapshots alike) — its content below is inferred only from search-result snippets
(marked CLAIMED) and cross-checked against other sources where possible.

## 1. Denuvo status

**Judgment (Steam AppID 2058180)** and **Lost Judgment (AppID 2058190)** both shipped
2022-09-14 with Denuvo Anti-Tamper. CLAIMED, multiple corroborating sources:
- [dsogaming.com](https://www.dsogaming.com/news/judgment-and-lost-officially-released-on-steam-both-of-them-are-using-denuvo/) and [game-news24.com](https://game-news24.com/2022/09/14/judgment-and-lost-officially-released-on-steam-and-they-are-using-denuvo/) — release-day reporting, both games "using Denuvo."
- Steam Community threads on both app IDs discussing Denuvo as late as Feb 2025, no removal reported.
- PCGamingWiki search snippets (page itself unreachable) state "All versions require Steam and Denuvo Anti-Tamper DRM" for both games.

**No official Denuvo removal found for either game as of Aug 2026.** SEGA has removed
Denuvo from some older titles (Yakuza 0 in 2019, per a CLAIMED PCGamingWiki-derived
snippet from a search result) but nothing indicates the same for Judgment/Lost Judgment.
RGG Studio continues shipping Denuvo on its newest titles too — Yakuza Kiwami 3 & Dark
Ties (Feb 2026) requires it, and was reportedly cracked ~11 days post-launch using a
"hypervisor" bypass method rather than a simple patch (CLAIMED, [ixbt.games](https://ixbt.games/en/news/2026/02/22/xaker-spustia-11-dnei-vzlomal-denvuo-v-yakuza-kiwami-3-dark-ties.html)) — implying current-gen Denuvo on this engine family is not trivial to strip, though that is a much newer/harder build than the 2022 Judgment ports.

**Piracy-crack status (does NOT mean Denuvo was removed by the publisher, but is a proxy
for how hardened these specific 2022 builds are):**
- Judgment: cracked by EMPRESS, **2023-08-15** (CLAIMED, [skidrowcodex.net](https://www.skidrowcodex.net/judgment-empress/), corroborated by [cwwatch.net/judgment](https://cwwatch.net/judgment/) page metadata: `articleSection: "Cracked Games"`, `dateModified: 2023-10-25`).
- Lost Judgment: **still listed as uncracked** — [cwwatch.net/lost-judgment](https://cwwatch.net/lost-judgment/) page metadata shows `articleSection: "Uncracked Games"` as of its last edit, `dateModified: 2024-01-01`. No search turned up a later crack announcement. This is the one asymmetry between the two games worth remembering: Judgment's Denuvo has a known public break; Lost Judgment's (as far as public trackers show) does not.

Net for our purposes: Denuvo is present and, per Steam/PCGamingWiki-derived snippets,
still active in the live builds of both games as sold today. This matches the K3/Y6
precedent our team already has (Frida attaches fine despite Denuvo) — see §3 for direct
evidence that third-party tools already inject and hook code in both exes successfully.

## 2. Existing injection/hook frameworks

**Shin Ryu Mod Manager (SRMM) / RyuModManager + YakuzaParless — VERIFIED (read source).**
- `https://github.com/SutandoTsukai181/RyuModManager` (also mirrored as `mosamadeeb/RyuModManager`). README fetched via `raw.githubusercontent.com` confirms it is a loose-file loader: generates an MLO consumed by Parless.
- Supported-Games wiki page (fetched via `raw.githubusercontent.com/wiki/...`) explicitly lists **both Judgment and Lost Judgment** as supported (Steam versions only; tested), alongside Y0 through Y8 and VF eSports.
- `YakuzaParless` README (`SutandoTsukai181/YakuzaParless`, read directly): "**ASI hook that redirects file paths** in Yakuza series PC games to allow loading loose files outside of game archives." Built on CookiePLMonster's SilentPatch/ModUtils patterns and the Ultimate ASI Loader. Known unsupported files: `.usm` (all games), plus `.cpk`/`.hca`/`.adx` for Yakuza 5 only — none of these gaps concern Judgment/Lost Judgment text or font.
- **Important for our purposes: Parless operates purely at the file-path/loader level** (it intercepts file-open calls and redirects to `mods/`), not at the rendering or memory level. It does not touch glyph/text-layout code at all — consistent with our CLAUDE.md rule #5 that loose fonts via Parless don't work because "the game loads fonts before the hook" fires.

**DragonTweak — VERIFIED (read source), the important find of this research.**
- `https://github.com/Lyall/DragonTweak` (archived; active dev moved to Codeberg, same content). This is a genuine runtime **code hook** ASI plugin (not a file-loader), confirmed by reading `src/dllmain.cpp` directly.
- It explicitly supports **both `Judgment.exe` and `LostJudgment.exe`** by name, alongside Yakuza 6, Kiwami 2, Like a Dragon, Gaiden, Infinite Wealth, and Pirate Yakuza. Its internal per-game enum codenames read `Judge` (Judgment) and `Coyote` (Lost Judgment) — the `Judge` codename independently corroborates this project's own CLAUDE.md verified codename for Judgment.
- Technique, read directly from source: **AOB/signature pattern scanning** (`Memory::PatternScan` / `Memory::MultiPatternScan`) to locate functions inside the live `.exe` image, then **`safetyhook::create_mid`** (a proper inline/trampoline hook library, https://github.com/cursey/safetyhook) to install mid-function hooks that read and rewrite CPU register/context state (e.g. rewriting `rsi`/`rdi`/`rbx`/`r8` register contents to change scene-config or launch-arg behavior). Used to: disable pillarboxing/letterboxing, adjust shadow resolution/draw distance, adjust LOD, and skip intro logos.
- Feature matrix confirms full success on Judgment (pillarboxing ✔, shadow quality ✔, intro-skip ✔; LOD adjust ✘ — not yet implemented for that title, not a technical blocker) and on Lost Judgment (all four features ✔, including LOD).
- This is **direct proof that inline/mid-function code hooking via AOB pattern scan works against these exact two Denuvo-protected binaries today**, using a fully public, open-source technique — a materially stronger data point than "Frida attaches" alone, because it demonstrates actual sustained in-process hooking (not just attach/detach) shipping as a released, widely-used mod.
- I grepped the entire `dllmain.cpp` (764 lines) for `font|text|glyph|width|string` — **no font/text/glyph work exists in this project.** It only touches camera/scene/quality code paths. This is a genuine, confirmed negative: DragonTweak is proof the *technique* works, not proof anyone has *used* it on text rendering.

**ReShade / Special K — CLAIMED, cosmetic only.** Both are usable on Lost Judgment
(ReShade has an explicit "Lost Judgement" profile in its installer per Special K wiki
cross-references; several ReShade presets exist on Nexus for Lost Judgment). These operate
at the swapchain/present level for post-processing, not at the draw-call or glyph level —
not useful for locating a text renderer.

**Cheat Engine tables / trainers — CLAIMED, exist but not code-hooking precedent for
text.** Active FearLess Revolution threads for both games (`viewtopic.php?t=21410`
Judgment, `t=21411` Lost Judgment, plus dedicated table threads `t=26885`, `t=32074`,
`t=21533`) with pointers for HP, EX gauge, money, items, minigame values, etc. These are
static memory-address/pointer discoveries via a debugger, not injected code, and none of
the found threads' summaries mention text/font/string-table pointers — cheat tables target
gameplay stats, not rendering internals.

## 3. Public reverse-engineering of Judgment/Lost Judgment internals

No dedicated Ghidra/IDA writeup repo, offset dump, or "judgment.exe internals" blog post
was found (searched directly; results returned only generic RE tooling docs). The state of
the art in public RE of these specific binaries is exactly what's described in §2:
- **DragonTweak**'s AOB patterns for `Judgment.exe`/`LostJudgment.exe` (three pattern
  groups: one shared by Yakuza 6/Kiwami 2, one shared by Lost Judgment/Gaiden, one shared
  by Like a Dragon 7 (Yakuza: Like a Dragon)/Judgment) — evidence that some internal
  engine functions are structurally similar/identical across specific title pairs, which
  narrows where a shared text/font subsystem might also be found by pattern-matching
  across those same pairings.
- Cheat Engine community pointer maps (gameplay stats only, see above).
- `Timo654/kuma` (Dragon Engine karaoke editor) and `HeartlessSeph/BEPEdit` (BEP file
  editor) — both are **file-format** tools (offline archive/asset editors), not runtime
  hook code. Not checked for Judgment-specific support but same genre as `kuma`/`BEPEdit`
  — no indication of memory-hook technique inside either.

No GitHub repo was found with "judgment.exe" or "lostjudgment.exe" function-address
documentation beyond DragonTweak's inline AOB patterns.

## 4. Has anyone hooked text/font rendering in any Dragon Engine title at runtime?

**No. This is a clean, well-searched negative result.** Multiple targeted searches for
D3D11 `DrawIndexed`/`ID3D11DeviceContext` hooking, font/glyph/width-table runtime patching,
and Frida scripts against any Yakuza/RGG/Dragon Engine title turned up nothing beyond:
- The Yakuza 0 PC Text Tools (ZenHAX thread, fetched and summarized) — confirmed this is
  **pure file-format editing**: unpack/repack `.par` archives, replace font `.dds` texture,
  and a one-time **static `.exe` binary patch** to widen an ASCII-range check + extend file
  size for longer strings/char-spacing tables. Explicitly "no runtime memory patching,
  process hooking, or dynamic function interception" per the fetch summary — this is the
  same "K2R-era" static-patch approach your team already has experience with, not a live
  hook.
- DragonTweak, confirmed by direct source grep (§2), touches zero font/text code.

So: the specific gap the team hit on Yakuza 6 — locating the actual glyph-quad
renderer/draw call at runtime — has **no known public solution on any Dragon Engine
title**, Judgment/Lost Judgment included. Nobody has published a `DrawIndexed` hook, a
glyph atlas hook, or a runtime character-spacing/kerning patch for this engine family.
The only "runtime" font-adjacent precedent industry-wide is generic tools like
`ysc3839/FontMod` (Win32 GDI font hooking for arbitrary programs, not games, and not
applicable to a D3D11 custom text renderer) — not evidence for or against Dragon Engine
specifically.

## 5. Config/ini/registry settings affecting text layout or font selection

**`steam_api64.ini` — CLAIMED but reported consistently across independent searches,
not directly read.** Multiple search results (echoing PCGamingWiki-style
"Fix"/"Multiplayer/Language" sections, unreachable directly this session) describe a
`steam_api64.ini` file located at `<Game>\runtime\media\steam_api64.ini` on **Yakuza: Like
a Dragon**, with a `Language = japanese` (etc.) key that overrides the UI/interface
language independent of the in-game menu. One search snippet extends this specifically to
**Judgment**, listing supported text languages (English, French, Italian, German, Spanish,
Japanese, Korean, Simplified/Traditional Chinese) and audio languages (English, Japanese).
This file is very likely present in Judgment/Lost Judgment too given they share the same
Steam localization plumbing as Yakuza: Like a Dragon, but **this was not independently
verified by reading the file or an unambiguous primary source** — flag as CLAIMED, worth a
five-minute check once the game is actually installed (per CLAUDE.md, extraction hasn't
started yet).

No evidence of any ini/registry key controlling font *selection*, glyph rendering, or
per-language spacing — only the interface-language string. This tracks with the
established architecture (per this project's own CLAUDE.md): fonts are loose `FONT!`
files under `data/font.judge/en/`, not something exposed via a config toggle.

## Summary of what actually matters for the mod

1. Denuvo is present and unremoved on both games' live Steam builds; this is the same
   posture the team already cleared on Y6 (Frida/injection still works).
2. A real, working, open-source example of **inline/mid-function code hooking against the
   live `Judgment.exe` and `LostJudgment.exe` processes** exists today (DragonTweak,
   safetyhook + AOB pattern scan) — this is stronger validation than "attaches fine," and
   gives a concrete, reusable technique (pattern-scan → `safetyhook::create_mid`) to try
   against text/font code paths.
3. Parless/SRMM remains file-redirect-only and irrelevant to the glyph-renderer problem,
   confirming CLAUDE.md rule #5.
4. Nobody, on any Dragon Engine title, has published a runtime hook into the actual
   text/glyph rendering path. The Y6 team's blocker (finding the glyph-quad draw call) is
   still an open problem industry-wide — Judgment/Lost Judgment are not "easier" by virtue
   of precedent; they're merely proven-hookable in general (via DragonTweak), which is a
   necessary but not sufficient condition.
5. A `steam_api64.ini` language-override file likely exists (unverified) but only affects
   which language pack loads, not font/glyph behavior.
