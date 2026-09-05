import json, io, sys
sys.stdout.reconfigure(encoding="utf-8")

with io.open("translations/worklist/batch_TALK_069.json", encoding="utf-8") as f:
    batch = json.load(f)
keys = list(batch["strings"].keys())

with io.open("extracted/facts/talk_speaker.json", encoding="utf-8") as f:
    ts = json.load(f)

found = 0
missing = []
for k in keys:
    if k in ts:
        found += 1
        info = ts[k]
        dupes = info.get("dupes")
        line = f"{info.get('table')} | {info.get('speaker')} | gender={info.get('gender')}"
        if dupes:
            line += f" | DUPES={dupes}"
        print(f"KEY: {k[:70]!r}\n  {line}")
    else:
        missing.append(k)

print(f"\n=== found {found}/{len(keys)}, missing {len(missing)} ===")
for m in missing:
    print("MISSING:", m[:90])
