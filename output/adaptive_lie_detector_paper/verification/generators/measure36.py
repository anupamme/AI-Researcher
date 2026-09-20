#!/usr/bin/env python3
"""Budget + pin measurement for the em-dash round."""
import io, re, os, subprocess, sys

D = "/Users/mediratta/code/paper_writing/AI-Researcher-align/output/adaptive_lie_detector_paper"
BASE = "c9718cf"

txt = subprocess.run(["pdftotext", "-layout", os.path.join(D, "main.pdf"), "-"],
                     capture_output=True, text=True).stdout
pages = txt.split("\f")
print("pdftotext pages:", len(pages))

p9, p10 = pages[8], pages[9]
flat9 = re.sub(r"\s+", " ", p9)
flat10 = re.sub(r"\s+", " ", p10)
anchor9 = "magnitude we measure only" in flat9
notin10 = "magnitude we measure only" not in flat10
ethics = "THICS STATEMENT" in flat10[:300]
r9 = re.findall(r"^ *(\d{3})", p9, re.M)
r10 = re.findall(r"^ *(\d{3})", p10, re.M)
print("FIT: anchor9=%s notin10=%s ethics=%s p9last=%s p10first=%s"
      % (anchor9, notin10, ethics, r9[-1] if r9 else None, r10[0] if r10 else None))
FIT_OK = anchor9 and notin10 and ethics and r9 and r9[-1] == "485" and r10 and r10[0] == "486"
print("FIT_OK:", FIT_OK)

# ---- all \newlabel page pins, vs the c9718cf build
PIN = re.compile(r"newlabel\{([^}]*)\}\{\{([^}]*)\}\{(\d+)\}")


def pins(aux):
    out = {}
    for lbl, num, pg in PIN.findall(aux):
        if lbl.endswith("@cref"):
            continue
        out[lbl] = pg
    return out


cur = pins(io.open(os.path.join(D, "main.aux"), encoding="utf-8", errors="replace").read())
old_aux = subprocess.run(["git", "-C", D, "show", "%s:output/adaptive_lie_detector_paper/main.aux" % BASE],
                         capture_output=True, text=True).stdout
base = pins(old_aux)
moved = {k: (base[k], cur[k]) for k in base if k in cur and base[k] != cur[k]}
added = [k for k in cur if k not in base]
removed = [k for k in base if k not in cur]
print("pins base=%d cur=%d  moved=%d added=%d removed=%d"
      % (len(base), len(cur), len(moved), len(added), len(removed)))
for k, (a, b) in sorted(moved.items()):
    print("   MOVED %-36s p%s -> p%s" % (k, a, b))
if added:
    print("   ADDED", added)
if removed:
    print("   REMOVED", removed)

MAIN5 = {"fig:dag": "2", "tab:claim_ledger": "5", "fig:ladder": "5",
         "fig:r1c_collapse": "7", "tab:external_audit": "8"}
bad = [(k, v, cur.get(k)) for k, v in MAIN5.items() if cur.get(k) != v]
print("main 5 float pins:", "OK" if not bad else bad)
print("tab:appendix_roadmap:", cur.get("tab:appendix_roadmap"), "(expect 14)")

# ---- per-page last body baseline, to see free space (xMin>100 excludes the margin
# ---- ruler column; yMax<740 excludes the centred page-number footer)
