#!/usr/bin/env python3
"""Propose a replacement for every prose --- in the appendix, for human review.

Offset-based: each proposal is (file, pos, 3, replacement), applied right-to-left,
so nothing depends on string matching being unique.

Rules PROPOSE; every proposal is reviewed in context before it is applied.
  R1  ---<coordinator>      -> ", "
  R2  ---<relative pronoun> -> ", "
  R3  ---<contrastive>      -> ", "
  R4  a PAIR in one segment -> " ("  +  ") " / "), "
  R5  lone dash, no ':' in segment -> ": "
  R6  lone dash, ':' already there  -> "; "
Skipped: verbatim, `& --- &` placeholder cells, `\textbf{---}` legend symbols.
>=3 dashes in one segment -> REVIEW, no proposal.
"""
import io, os, re, json, collections

D = "/Users/mediratta/code/paper_writing/AI-Researcher-align/output/adaptive_lie_detector_paper"
FILES = ["sections/appendix.tex", "sections/related_work.tex"]

ABBR = ("vs.", "e.g.", "i.e.", "cf.", "Fig.", "Tab.", "Eq.", "No.", "approx.",
        "pre-reg.", "maj.", "underp.", "resp.", "etc.", "al.", "sec.", "reg.",
        "corr.", "est.", "obs.", "ref.", "Inc.", "Ltd.", "St.", "Dr.", "Prof.")
COORD = {"and", "but", "so", "or", "yet", "while", "whereas", "though",
         "although", "because", "since", "then", "nor", "plus", "hence", "thus"}
RELAT = {"which", "who", "whose", "where", "whom", "when"}
CONTRA = {"not", "never", "no", "none", "neither", "rather"}


def is_boundary(s, i):
    j = i - 1
    while j >= 0 and s[j] in "\"')}]":
        j -= 1
    if j < 0 or s[j] not in ".!?":
        return False
    if s[j] == ".":
        if j >= 1 and s[j - 1].isdigit():
            return False
        if j >= 1 and s[j - 1].isupper() and (j < 2 or not s[j - 2].isalpha()):
            return False
        for a in ABBR:
            if s[:j + 1].endswith(a):
                return False
    k = i
    while k < len(s) and s[k] in " \t\n":
        k += 1
    return k >= len(s) or s[k].isupper() or s[k] in "\\$([\u201c`"


def segments(s):
    cuts = {0, len(s)}
    for m in re.finditer(r"[.!?][\"')}\]]*\s", s):
        if is_boundary(s, m.end() - 1):
            cuts.add(m.end())
    for m in re.finditer(r"(?<!\\)&|\\\\|\n\n|\\item\b|\\paragraph\{|\\subsection\{"
                         r"|\\subsubsection\{|\\caption\{", s):
        cuts.add(m.start())
        cuts.add(m.end())
    c = sorted(cuts)
    return list(zip(c, c[1:]))


def strip_math(t):
    t = re.sub(r"\$[^$]*\$", "", t)
    return re.sub(r"\\(ref|citep|citet|citealp|label|texttt|url)\{[^}]*\}", "", t)


PLACEHOLDER_SEG = re.compile(r"\A[\s$]*---[\s$]*\Z")
props, stats = [], collections.Counter()

for rel in FILES:
    src = io.open(os.path.join(D, rel), encoding="utf-8").read()
    verb, inv = [], None
    for m in re.finditer(r"\\(begin|end)\{(verbatim|lstlisting|comment|Verbatim)\}", src):
        if m.group(1) == "begin" and inv is None:
            inv = m.start()
        elif m.group(1) == "end" and inv is not None:
            verb.append((inv, m.end()))
            inv = None

    for a, b in segments(src):
        seg = src[a:b]
        ds = [m.start() for m in re.finditer(r"(?<!-)---(?!-)", seg)]
        if not ds:
            continue
        # whole segment is just the "not applicable" mark, or a legend symbol
        if PLACEHOLDER_SEG.match(seg):
            stats["PLACEHOLDER"] += len(ds)
            continue
        keep = []
        for d in ds:
            p = a + d
            if any(x <= p < y for x, y in verb):
                stats["VERBATIM"] += 1
                continue
            if re.search(r"\\textbf\{\Z", seg[:d]) and seg[d + 3:].startswith("}"):
                stats["LEGEND"] += 1
                continue
            keep.append(d)
        if not keep:
            continue

        def ctx(d, w=60):
            return (re.sub(r"\s+", " ", src[max(0, a + d - w):a + d]),
                    re.sub(r"\s+", " ", src[a + d + 3:a + d + 3 + w]))

        if len(keep) == 2:
            d1, d2 = keep
            m = re.match(r"([A-Za-z]+)", seg[d2 + 3:])
            close = "), " if (m and m.group(1).lower() in COORD) else ") "
            pre1, _ = ctx(d1)
            _, post2 = ctx(d2)
            props.append(dict(file=rel, rule="R4-pair",
                              pos=[a + d1, a + d2], rep=[" (", close],
                              pre=pre1, inner=re.sub(r"\s+", " ", seg[d1 + 3:d2]),
                              post=post2))
            stats["R4-pair"] += 2
            continue
        if len(keep) == 1:
            d = keep[0]
            w = re.match(r"([A-Za-z]+)", seg[d + 3:])
            w = w.group(1).lower() if w else ""
            if w in COORD:
                rule, rep = "R1-coord", ", "
            elif w in RELAT:
                rule, rep = "R2-rel", ", "
            elif w in CONTRA:
                rule, rep = "R3-contra", ", "
            elif ":" in strip_math(seg):
                rule, rep = "R6-semi", "; "
            else:
                rule, rep = "R5-colon", ": "
            pre, post = ctx(d, 70)
            props.append(dict(file=rel, rule=rule, pos=[a + d], rep=[rep],
                              pre=pre, inner=None, post=post))
            stats[rule] += 1
            continue
        for d in keep:
            pre, post = ctx(d, 70)
            props.append(dict(file=rel, rule="REVIEW", pos=[a + d], rep=[None],
                              pre=pre, inner=None, post=post))
        stats["REVIEW"] += len(keep)

for p in props:
    src = io.open(os.path.join(D, p["file"]), encoding="utf-8").read()
    p["line"] = src.count("\n", 0, p["pos"][0]) + 1

print("=== dash occurrences by disposition ===")
tot = 0
for k, v in sorted(stats.items()):
    print("  %-14s %4d" % (k, v))
    tot += v
print("  %-14s %4d   (expect 476)" % ("TOTAL", tot))
json.dump(props, io.open("/tmp/appendix_props.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nwrote /tmp/appendix_props.json (%d proposals)" % len(props))
