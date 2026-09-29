"""Compact lead-review view of a polish chapter: one block per id, A vs B side by side.
usage: python scripts/polish_compare.py N [--only-diff] [--cats MPC] > out.txt
"""
import io, json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths
from apply_sweep_findings import unesc, validate

n = int(sys.argv[1])
folder = ROOT / "translations" / "review" / "polish" / ("ch%02d" % n)
index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
master = json.load(io.open(paths.MASTER_TH, encoding="utf-8"))
cats = None
if "--cats" in sys.argv:
    cats = set(sys.argv[sys.argv.index("--cats") + 1])

by = {}
for fp in sorted(folder.glob("findings_*.json")):
    m = re.match(r"findings_(\d\d)", fp.name)
    if not m:
        continue
    who = {"0": "A", "5": "B", "9": "L"}.get(m.group(1)[0], m.group(1))
    try:
        items = json.loads(fp.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print("JSON BROKEN", fp.name, e)
        continue
    for it in items:
        if not isinstance(it, dict):
            continue
        new = it.get("th_new")
        if isinstance(new, str) and "\\n" in new and "\n" not in new:
            new = unesc(new)
        by.setdefault(str(it.get("id")), []).append((who, str(it.get("cat", "?"))[:1], it.get("sev") or it.get("conf") or "mid", new, it.get("note", "")))


def e(s):
    return "" if s is None else str(s).replace("\n", "⏎")


for sid in sorted(by, key=lambda x: x):
    rows = by[sid]
    if cats and not any(r[1] in cats for r in rows):
        continue
    en = index.get(sid)
    old = master.get(en)
    mt = meta.get(sid, {})
    news = {r[3] for r in rows if r[3]}
    if "--only-diff" in sys.argv and len(news) <= 1:
        continue
    flags = " ".join(mt.get("flags", []))
    print("%s [%s/%s] %s" % (sid, mt.get("speaker", "?"), mt.get("gender", "?"), flags))
    print("  EN: " + e(en))
    print("  TH: " + e(old))
    for who, cat, sev, new, note in rows:
        err = validate(old, new) if new else "-"
        print("  %s %s/%s: %s  ‖ %s%s" % (who, cat, sev, e(new), note[:70], ("  !! " + err) if err and err != "-" else ""))
