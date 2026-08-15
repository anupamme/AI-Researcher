#!/usr/bin/env python3
"""Verify every entry in references.bib against clibib's authoritative sources.

For each entry: prefer arXiv ID / DOI lookup (reliable), fall back to title search.
Writes fetched BibTeX to fetched/<key>.bib and a comparison report.
"""
import json
import os
import re
import subprocess
import sys

BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "references.bib")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".bibverify")
FETCHED = os.path.join(OUT, "fetched")
os.makedirs(FETCHED, exist_ok=True)

raw = open(BIB).read()

# Split into entries on lines starting with @
chunks = re.split(r"\n(?=@)", raw.strip())

ARXIV_RE = re.compile(r"arXiv[:\s]*(\d{4}\.\d{4,5})", re.IGNORECASE)
DOI_RE = re.compile(r"doi\s*=\s*[{\"]([^}\"]+)", re.IGNORECASE)
KEY_RE = re.compile(r"^@(\w+)\s*\{\s*([^,]+),")
TITLE_RE = re.compile(r"title\s*=\s*\{(.+?)\}\s*,\s*\n", re.DOTALL | re.IGNORECASE)
AUTHOR_RE = re.compile(r"author\s*=\s*\{(.+?)\}\s*,\s*\n", re.DOTALL | re.IGNORECASE)


def clean(s):
    s = re.sub(r"[{}\\]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def surnames(author_field):
    """Extract lowercase surnames from a BibTeX author field."""
    out = []
    for a in re.split(r"\s+and\s+", clean(author_field)):
        a = a.strip()
        if not a or a.lower() == "others":
            continue
        if "," in a:
            sn = a.split(",")[0]
        else:
            sn = a.split()[-1] if a.split() else ""
        sn = re.sub(r"[^A-Za-zÀ-ÿ\-]", "", sn).lower()
        if sn:
            out.append(sn)
    return out


entries = []
for c in chunks:
    m = KEY_RE.match(c)
    if not m:
        continue
    key = m.group(2).strip()
    tm = TITLE_RE.search(c)
    am = AUTHOR_RE.search(c)
    ax = ARXIV_RE.search(c)
    doi = DOI_RE.search(c)
    entries.append({
        "key": key,
        "type": m.group(1),
        "title": clean(tm.group(1)) if tm else "",
        "authors": clean(am.group(1)) if am else "",
        "arxiv": ax.group(1) if ax else None,
        "doi": doi.group(1) if doi else None,
        "has_others": "and others" in (am.group(1) if am else ""),
    })

print(f"Parsed {len(entries)} entries\n", flush=True)

results = []
for i, e in enumerate(entries, 1):
    # Prefer arXiv > DOI > title
    if e["arxiv"]:
        query, mode = e["arxiv"], "arxiv"
    elif e["doi"]:
        query, mode = e["doi"], "doi"
    else:
        query, mode = e["title"], "title"

    cache = os.path.join(FETCHED, f"{e['key']}.bib")
    if os.path.exists(cache) and os.path.getsize(cache) > 0:
        fetched = open(cache).read()
    else:
        try:
            p = subprocess.run(["clibib", "--first", query], capture_output=True,
                               text=True, timeout=90)
            fetched = p.stdout
        except Exception as ex:
            fetched = f"ERROR: {ex}"
        open(cache, "w").write(fetched)

    fa = AUTHOR_RE.search(fetched)
    ft = TITLE_RE.search(fetched)
    fetched_authors = clean(fa.group(1)) if fa else ""
    fetched_title = clean(ft.group(1)) if ft else ""

    ours = surnames(e["authors"])
    theirs = surnames(fetched_authors)

    status = "NO_DATA" if not fetched_authors else None
    extra = missing = []
    if fetched_authors:
        extra = [s for s in ours if s not in theirs]     # in ours, not in source => suspect
        missing = [s for s in theirs if s not in ours]   # in source, not in ours
        if extra:
            status = "SUSPECT_AUTHORS"
        elif missing and not e["has_others"]:
            status = "INCOMPLETE"
        elif missing:
            status = "OK(et-al)"
        else:
            status = "OK"

    results.append({**e, "mode": mode, "query": query, "status": status,
                    "fetched_title": fetched_title, "fetched_authors": fetched_authors,
                    "extra": extra, "missing": missing})
    print(f"[{i:02d}/{len(entries)}] {status:16s} {e['key']:35s} ({mode})", flush=True)

json.dump(results, open(os.path.join(OUT, "verify_report.json"), "w"), indent=2)

print("\n" + "=" * 72)
print("ENTRIES WITH AUTHORS NOT FOUND IN THE AUTHORITATIVE SOURCE (likely hallucinated)")
print("=" * 72)
for r in results:
    if r["status"] == "SUSPECT_AUTHORS":
        print(f"\n{r['key']}  [{r['mode']}]")
        print(f"  our title   : {r['title'][:90]}")
        print(f"  source title: {r['fetched_title'][:90]}")
        print(f"  NOT IN SOURCE: {', '.join(r['extra'])}")
        if r["missing"]:
            print(f"  source has  : {', '.join(r['missing'])}")

print("\n" + "=" * 72)
print("COULD NOT VERIFY (no data returned) — need manual check")
print("=" * 72)
for r in results:
    if r["status"] == "NO_DATA":
        print(f"  {r['key']:35s} query={r['query'][:60]}")

print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
from collections import Counter
for k, v in Counter(r["status"] for r in results).most_common():
    print(f"  {k:18s} {v}")
