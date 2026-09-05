#!/usr/bin/env python3
"""สร้าง worklist ให้ทีมแปล Judgment — port จาก K3 (21 ส.ค. 2026)

input:
  extracted/unique_strings.json   ({EN: {count, bins[]}} จาก extract_all_en.py)
  extracted/strings_by_bin.json   ({bin: [EN,...]})
  translations/master.json        (คำแปล v1.2 เดิม — ใช้เป็น "ร่างอ้างอิง" เท่านั้น ไม่ auto-fill)

output:
  translations/worklist/batch_NNN.json       (<=250 strings/batch)
  translations/worklist/batch_TALK_NNN.json  (talk.bin-only)
  translations/worklist_report.md

ต่างจาก K2R tm_match:
  - **ไม่ auto-fill master_th จาก TM** — user สั่งแปลใหม่ทั้งเกม ทุก string ต้องผ่านคู่
    ผู้แปล+ผู้ตรวจ; คำแปล v1.2 ใส่มากับ batch ในช่อง "ref_tm" เป็นร่างให้ผู้แปลพิจารณา
    (ดี=เก็บ, เพี้ยน=เขียนใหม่) — ผู้แปลต้องกรอก "strings" เองทุก key เสมอ
  - string ที่อยู่ใน master_th.json แล้ว (ผ่าน merge_qc จาก sprint ก่อน) จะไม่ถูกจัดเข้า batch ใหม่

รันซ้ำได้ (idempotent): ก่อน re-chunk เก็บเกี่ยวคำแปลที่กรอกไว้ใน batch เดิมเข้า master_th ก่อน
แล้วลบ batch เก่าทิ้งค่อยจัดใหม่ (เลข batch เลื่อนได้ — อย่าอ้างเลข batch ข้าม sprint)
"""
import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")  # กัน cp1252
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import EXTRACTED, MASTER_TH, TRANSLATIONS, WORKLIST  # noqa: E402

# ใช้ TM จากโปรเจกต์เก่า (อ่านอย่างเดียว) เป็นร่าง ref — ไม่ auto-fill
# ลำดับความน่าเชื่อ: Gaiden (ใหม่สุด + Kiryu เป็นตัวเอกเหมือนกัน) > Y8 > Y7 > Pirate > K2R
TM_SOURCES = [  # ตัวแรกในลิสต์ที่มี key ชนะ (ลำดับตาม glossary priority ของ CLAUDE.md)
    (Path("D:/Projects/yakuza-kiwami-3/translations/master_th.json"), "k3"),
    (Path("D:/Projects/yakuza-gaiden/translations/master_th.json"), "gaiden"),
    (Path("D:/Projects/yakuza-6-thai/translations/master_th.json"), "y6"),
    (Path("D:/Projects/y8-infinite-wealth/translations/master_th.json"), "y8"),
    (Path("D:/Projects/yakuza-7-like-a-dragon-thai/translations/master_th.json"), "y7"),
    (Path("D:/Projects/pirate-yakuza-hawaii-thai/translations/master_th.json"), "pirate"),
    (Path("D:/Projects/yakuza-kiwami-2-mod/translations/master_th.json"), "k2r"),
]


def load_tm():
    tm = {}
    for p, label in TM_SOURCES:
        if not p.exists():
            print(f"!! TM ไม่พบ: {label} ({p})")
            continue
        d = json.load(open(p, encoding="utf-8"))
        added = 0
        for en, th in d.items():
            if en not in tm and isinstance(th, str) and th.strip():
                tm[en] = th
                added += 1
        print(f"TM {label}: +{added:,} (รวม {len(tm):,})")
    return tm

UNIQUE_JSON = EXTRACTED / "unique_strings.json"
BY_BIN_JSON = EXTRACTED / "strings_by_bin.json"
REPORT_MD = TRANSLATIONS / "worklist_report.md"

BATCH_SIZE = 250

# tier ต่ำ = ทำก่อน (credits คง EN ทั้ง bin ตามบทเรียน K2R — ดันท้ายคิว)
TIER6_DEFER = {"credits.bin"}

# bin ที่ไม่ส่งเข้าคิวแปลเลย — ข้อความในนั้นเป็น identifier/ชื่อ object ไม่ใช่ข้อความที่ผู้เล่นเห็น
# (ตรวจแล้วจาก docs/research.md §3 — extractor ปล่อยผ่านมาเพราะเป็นคำอังกฤษล้วน)
DENY_BINS = {
    "minigame_rail_shooter_stage_object.bin",
    "minigame_rail_shooter_doll_z_head_node.bin",
    "character_npc_soldier_name_group.bin",   # ชื่อสกุลญี่ปุ่นดิบสำหรับสุ่ม NPC
    "sound_se_name_table.bin", "sound_cuesheet_info.bin", "sound_voice_table.bin",
    "motion_behavior_info.bin", "scene_config.bin", "timeline.bin",
    "ui_animation_all.bin", "ui_layer_all.bin", "ui_crop_all.bin", "ui_scene_property.bin",
    "character_model_model_data.bin", "character_model_model_data_judge.bin",
    # เพิ่ม 21 ส.ค. 2026 (ผู้ตรวจ batch_118 ยืนยัน): ทั้งไฟล์เป็น rig/bone identifier
    # (scratch/grip/hold/punch/standby + face) ไม่มีข้อความแสดงผลปนเลย
    "minigame_picking_job_picking_job.bin",
    # เพิ่ม 21 ส.ค. 2026 (นักแปล batch_123 ยืนยันรายคีย์): พารามิเตอร์เอฟเฟกต์เอนจิ้นล้วน
    # (blob ไบนารี · รหัสเอฟเฟกต์ 3 ตัวอักษร · ค่า weak/normal/strong) ไม่ใช่ข้อความแสดงผล
    "effect_body_damage.bin", "effect_character_use_effect.bin",
    "effect_charge_dust_generator.bin", "effect_splash_liquid_param.bin",
    # เพิ่ม 21 ส.ค. 2026 (ผู้ตรวจ batch_120 ยืนยันรายคีย์): enum/ค่าระบบล้วน
    "access_type.bin", "ai_param.bin", "camera_shake.bin",
    # เพิ่ม 21 ส.ค. 2026 (นักแปล batch_125 ยืนยันรายคีย์): ชื่อรูปทรง/สไตล์กล้อง enum ล้วน
    "post_effect_dof_shapes.bin", "post_effect_glare_shapes.bin",
}

# bin ที่ "คงภาษาอังกฤษ" ตามกติกาเหล็กข้อ 10 (license/EULA/credits/เครื่องหมายการค้า)
KEEP_EN_BINS = {
    "credits.bin", "pause_license.bin", "pause_siea_eula.bin", "pause_siee_eula.bin",
    "platform_term.bin",
    # เพิ่ม 22 ส.ค. 2026: คำสั่งแชตของมินิเกม live chat เป็นโรมาจิญี่ปุ่นล้วน (AIDAYO,
    # AKIRAMENNNAYO ...) ผู้เล่นพิมพ์ตามตัวอักษร — แปลไม่ได้ ต้องคง EN
    "minigame_live_chat_chat_commands.bin",
}

TIER_NAMES = {
    1: "caption (ซับสั้นบนจอ)",
    2: "auth/sound_auth (บทคัตซีน)",
    3: "msg/pause_message/message dialog",
    4: "item/ui/title/help/manual/map/talk_talker",
    5: "minigame/drone",
    6: "rest",
    7: "talk-only (บทสนทนาเดินเมือง)",
}


def bin_tier(bin_name: str) -> int:
    b = bin_name.lower()
    if b == "caption.bin":
        return 1
    if b in ("auth.bin", "sound_auth.bin"):
        return 2
    if b in ("msg.bin", "pause_message.bin") or b.startswith(("message_", "explanation_", "loading_")):
        return 3
    if (b in ("item.bin", "talk_talker.bin", "manual.bin", "help.bin")
            or b.startswith(("item_", "ui", "title_", "help", "tips", "manual", "map_",
                             "evidence", "mission_", "complete", "player_skill"))):
        return 4
    if b.startswith(("minigame_", "drone_")):
        return 5
    if b == "talk.bin":
        return 7
    return 6


def string_tier(bins: list) -> tuple:
    return min((bin_tier(b), b) for b in bins)


def tier6_sort_key(bin_name: str):
    return (1 if bin_name in TIER6_DEFER else 0, bin_name)


def word_count(s: str) -> int:
    return len(re.sub(r"<[^>]*>", " ", s).split())


def load_json(p: Path):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def dump_json(obj, p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def main():
    unique = load_json(UNIQUE_JSON)      # {EN: {count, bins[]}}
    by_bin = load_json(BY_BIN_JSON)      # {bin: [EN,...]}
    legacy = load_tm()   # ร่างอ้างอิงจาก Y7/Pirate/K2R — ไม่ใช่คำตอบ ผู้แปลพิจารณาใหม่ทุกตัว

    # ---- master_th (ของ rework) + เก็บเกี่ยวคำแปลที่ค้างใน batch เดิม ------
    master_th = load_json(MASTER_TH) if MASTER_TH.exists() else {}
    harvested = 0
    WORKLIST.mkdir(parents=True, exist_ok=True)
    old_batches = sorted(WORKLIST.glob("batch_*.json"))
    for bf in old_batches:
        try:
            data = load_json(bf)
        except (json.JSONDecodeError, OSError):
            print(f"!! ข้าม batch เสีย: {bf.name}")
            continue
        for en, th in data.get("strings", {}).items():
            if isinstance(th, str) and th.strip() and not master_th.get(en):
                master_th[en] = th
                harvested += 1
    for bf in old_batches:
        bf.unlink()

    # ---- จัด tier ให้ string ที่ยังไม่มีใน master_th ------------------------
    remaining = []  # (tier, primary_bin, orig_index, EN)
    denied = 0
    for idx, (en, meta) in enumerate(unique.items()):
        if master_th.get(en):
            continue
        bins_ok = [b for b in meta["bins"] if b not in DENY_BINS]
        if not bins_ok:          # string นี้อยู่แต่ใน bin ที่ไม่แปล
            denied += 1
            continue
        tier, primary = min((bin_tier(b), b) for b in bins_ok)
        remaining.append((tier, primary, idx, en))

    def sort_key(item):
        tier, primary, idx, _ = item
        if tier == 6:
            return (tier, tier6_sort_key(primary), idx)
        return (tier, (0, primary), idx)

    remaining.sort(key=sort_key)
    normal = [r for r in remaining if r[0] != 7]
    talk = [r for r in remaining if r[0] == 7]

    # ---- เขียน batch (มี ref_tm = คำแปลเดิมให้พิจารณา ไม่ใช่คำตอบ) --------
    ref_hits = 0

    def write_batches(items, name_fmt):
        nonlocal ref_hits
        n_batch, seq = 0, 1
        groups, cur_tier, cur = [], None, []
        for it in items:  # ตัด batch ไม่ให้คร่อม tier
            if it[0] != cur_tier and cur:
                groups.append((cur_tier, cur))
                cur = []
            cur_tier = it[0]
            cur.append(it)
        if cur:
            groups.append((cur_tier, cur))
        for tier, group in groups:
            for i in range(0, len(group), BATCH_SIZE):
                chunk = group[i:i + BATCH_SIZE]
                ens = [en for _, _, _, en in chunk]
                ref = {en: legacy[en] for en in ens if legacy.get(en)}
                ref_hits += len(ref)
                payload = {
                    "priority": tier,
                    "source_bins": sorted({b for en in ens for b in unique[en]["bins"]}),
                    "strings": {en: "" for en in ens},
                    "ref_tm": ref,
                }
                dump_json(payload, WORKLIST / (name_fmt % seq))
                seq += 1
                n_batch += 1
        return n_batch

    n_normal_batches = write_batches(normal, "batch_%03d.json")
    n_talk_batches = write_batches(talk, "batch_TALK_%03d.json")

    dump_json(master_th, MASTER_TH)

    # ---- report -------------------------------------------------------------
    tier_counts = {}
    for tier, _, _, _ in remaining:
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
    words_normal = sum(word_count(en) for _, _, _, en in normal)
    words_talk = sum(word_count(en) for _, _, _, en in talk)

    key_bins = ["caption.bin", "auth.bin", "sound_auth.bin", "message_dialog.bin",
                "msg.bin", "item.bin", "ui_text.bin", "title_root.bin",
                "map_area.bin", "talk.bin", "credits.bin"]
    lines = []
    a = lines.append
    a("# Worklist Report — Pirate Rework (make_worklist.py)")
    a("")
    a(f"- unique strings ทั้งเกม: **{len(unique):,}**")
    a(f"- อยู่ใน master_th แล้ว (ผ่าน QC): {len(unique) - len(remaining):,} "
      f"(เก็บเกี่ยวจาก batch เดิมรอบนี้ {harvested:,})")
    a(f"- เหลือจัดเข้า batch: **{len(remaining):,}** "
      f"(normal {len(normal):,} / talk-only {len(talk):,})")
    a(f"- batch: **{n_normal_batches}** normal + **{n_talk_batches}** TALK "
      f"(≤{BATCH_SIZE} strings/batch)")
    a(f"- มีร่างอ้างอิง v1.2 (`ref_tm`): {ref_hits:,} strings "
      f"— **ไม่ใช่คำตอบ** ผู้แปลต้องพิจารณาใหม่ทุกตัว")
    a(f"- ปริมาณงาน: ~{words_normal + words_talk:,} คำ EN "
      f"(normal {words_normal:,} / talk {words_talk:,})")
    a("")
    a("| priority | ความหมาย | strings |")
    a("|---:|---|---:|")
    for t in sorted(tier_counts):
        a(f"| {t} | {TIER_NAMES[t]} | {tier_counts[t]:,} |")
    a("")
    a("## bin สำคัญ")
    a("")
    a("| bin | strings |")
    a("|---|---:|")
    for b in key_bins:
        if by_bin.get(b):
            a(f"| {b} | {len(by_bin[b]):,} |")
    a("")
    a("สร้างโดย `scripts/make_worklist.py` — รันซ้ำได้ (harvest ก่อน re-chunk)")
    a("")
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"unique={len(unique):,} in_master={len(unique) - len(remaining):,} "
          f"remaining={len(remaining):,} (normal {len(normal):,}/talk {len(talk):,})")
    print(f"batches: {n_normal_batches} normal + {n_talk_batches} TALK | "
          f"ref_tm hits {ref_hits:,}")
    print(f"-> {WORKLIST}")
    print(f"-> {REPORT_MD}")


if __name__ == "__main__":
    main()
