"""After apply+remerge: every accepted fix (first finding per key, lead file 00 first) must equal master."""
import glob, io, json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from apply_sweep_findings import unesc, validate

n = int(sys.argv[1])
rej = set(sys.argv[2].split(",")) if len(sys.argv) > 2 and sys.argv[2] else set()
d = str(Path(__file__).resolve().parents[1] / "translations" / "review" / "polish" / ("ch%02d" % n))
idx = json.load(open(d + r"\index.json", encoding="utf-8"))
master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
first = {}
for fp in sorted(glob.glob(d + r"\findings_*.json")):
    if not re.search(r"findings_\d\d", fp):
        continue
    for it in json.load(open(fp, encoding="utf-8-sig")):
        new = it.get("th_new")
        if not new or it["id"] in rej:
            continue
        if "\\n" in new and "\n" not in new:
            new = unesc(new)
        first.setdefault(idx[it["id"]], (it["id"], new))
same = diff = 0
for en, (sid, new) in first.items():
    if master.get(en) == new:
        same += 1
    else:
        diff += 1
        if diff <= 10:
            print(sid, repr(new)[:100], "|| master:", repr(master.get(en))[:100])
print("same", same, "diff", diff)
