"""Reviewer audit: join talk_speaker.json with TALK_001..005 done batches.
Outputs a human-readable report per batch to scratchpad, grouped by table,
in original worklist order (dict insertion order == file order).
Read-only script; does not modify anything.
"""
import sys, json, os

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\Projects\judgment-thai"
OUT_DIR = r"C:\Users\BigNut\AppData\Local\Temp\claude\d--Projects-judgment-thai\f5dbcdab-1a9d-478d-8989-18ff83ce58da\scratchpad"

speak = json.load(open(os.path.join(ROOT, "extracted/facts/talk_speaker.json"), encoding="utf-8"))

for n in range(1, 6):
    tag = f"TALK_{n:03d}"
    wl = json.load(open(os.path.join(ROOT, f"translations/worklist/batch_{tag}.json"), encoding="utf-8"))
    done = json.load(open(os.path.join(ROOT, f"translations/done/batch_{tag}.done.json"), encoding="utf-8"))

    order = list(wl["strings"].keys())
    ref_tm = wl.get("ref_tm", {})
    strings = done["strings"]

    # group by table, preserving original order within each table
    by_table = {}
    for en in order:
        info = speak.get(en)
        table = info["table"] if info else "UNKNOWN"
        by_table.setdefault(table, []).append(en)

    lines = []
    lines.append(f"# {tag} speaker audit join\n")
    for table, ens in by_table.items():
        lines.append(f"\n## table = {table}  ({len(ens)} lines)\n")
        for en in ens:
            info = speak.get(en, {})
            speaker = info.get("speaker", "?")
            speaker_ja = info.get("speaker_ja", "")
            gender = info.get("gender", "?")
            th = strings.get(en, "")
            lines.append(f"- EN: {en}")
            lines.append(f"  SPEAKER: {speaker} (ja={speaker_ja}, gender={gender})")
            lines.append(f"  TH: {th}")
    out_path = os.path.join(OUT_DIR, f"audit_{tag}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"wrote {out_path}  ({len(order)} lines, {len(by_table)} tables)")
