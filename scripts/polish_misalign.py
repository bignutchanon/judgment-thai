"""Flag findings whose th_new looks unrelated to the line (possible id shift): low char-similarity to the TH seen in the chunk."""
import difflib, glob, json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_sweep_findings import unesc

TAG = re.compile(r"<[^<>]*>")
for n in [int(x) for x in sys.argv[1].split(",")]:
    d = str(Path(__file__).resolve().parents[1] / "translations" / "review" / "polish" / ("ch%02d" % n))
    th = {}
    for cp in sorted(glob.glob(d + r"\chunk_*.tsv")):
        rows = open(cp, encoding="utf-8").read().splitlines()
        h = rows[0].split("\t")
        for r in rows[1:]:
            f = r.split("\t")
            th[f[h.index("id")]] = (unesc(f[h.index("TH")]), f[h.index("EN")])
    for fp in sorted(glob.glob(d + r"\findings_*.json")):
        if not re.search(r"findings_\d\d", fp):
            continue
        for it in json.load(open(fp, encoding="utf-8-sig")):
            new = it.get("th_new")
            if not new or it["id"] not in th:
                continue
            if "\\n" in new and "\n" not in new:
                new = unesc(new)
            old, en = th[it["id"]]
            r = difflib.SequenceMatcher(None, TAG.sub("", old), TAG.sub("", new)).ratio()
            if r < float(sys.argv[2] if len(sys.argv) > 2 else 0.35):
                print("%s %s %.2f [%s]\n   EN: %s\n   OLD: %s\n   NEW: %s" % (fp.split("\\")[-1], it["id"], r, it.get("cat"), en[:110], old.replace("\n", "⏎")[:110], new.replace("\n", "⏎")[:110]))
