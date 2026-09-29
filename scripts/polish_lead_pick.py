"""Write polish/chNN/findings_00.json (lead overrides, sorted first so they win in apply).
usage: python scripts/polish_lead_pick.py N "<B ids comma>" [own.json]
own.json: [{"id":..., "cat":..., "note":..., "th_new": "... real newlines or \\n ..."}]
B ids: pick reader-B (findings_5x) version for these ids.
"""
import glob, io, json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from apply_sweep_findings import unesc, validate

n = int(sys.argv[1])
bids = [x for x in sys.argv[2].split(",") if x]
d = str(Path(__file__).resolve().parents[1] / "translations" / "review" / "polish" / ("ch%02d" % n))
idx = json.load(open(d + r"\index.json", encoding="utf-8"))
master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
B = {}
for fp in sorted(glob.glob(d + r"\findings_5*.json")):
    for it in json.load(open(fp, encoding="utf-8-sig")):
        if it.get("th_new"):
            B.setdefault(it["id"], it)
out = []
for i in bids:
    it = B[i]
    out.append({"id": i, "cat": it.get("cat", "N"), "sev": "high", "note": "(lead เลือกฉบับผู้อ่าน B) " + it.get("note", ""), "th_new": it["th_new"]})
if len(sys.argv) > 3:
    for it in json.load(open(sys.argv[3], encoding="utf-8")):
        it.setdefault("sev", "high")
        it["note"] = "(lead) " + it.get("note", "")
        out.append(it)
bad = 0
for it in out:
    new = it["th_new"]
    if "\\n" in new and "\n" not in new:
        new = unesc(new)
    err = validate(master[idx[it["id"]]], new)
    if err:
        bad += 1
        print("BAD", it["id"], err, repr(master[idx[it["id"]]])[:80], repr(new)[:80])
json.dump(out, open(d + r"\findings_00.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", len(out), "bad", bad)
