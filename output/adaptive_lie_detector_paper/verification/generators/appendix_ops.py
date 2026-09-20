#!/usr/bin/env python3
"""Apply the reviewed appendix em-dash conversion.

Every one of the 329 machine proposals in /tmp/appendix_props.json was read in
context; this file records the review verdict. Three classes of correction were
needed, all recorded below with the reason:

  DROP      the site is the table "not applicable" mark, not punctuation
  OVERRIDE  the rule's replacement was wrong for that site
  INSERT    a parenthesis pair needs its closer somewhere other than at a dash

Ops are (file, pos, length, replacement); a dash op consumes the whitespace on
either side so no " ," or "( " artifacts appear. Applied right-to-left per file,
so no offset depends on another edit. --check is a dry run.
"""
import io, json, os, re, sys, collections

D = "/Users/mediratta/code/paper_writing/AI-Researcher-align/output/adaptive_lie_detector_paper"

# --- DROP: `\multicolumn{2}{c}{---}` is the same "not applicable" mark as `& --- &`;
# --- the proposal generator's PLACEHOLDER_SEG test only caught the bare-cell form.
DROP = {290, 291, 292}

# --- OVERRIDE: rule verdict corrected after reading the site. rep list per dash.
OVERRIDE = {
    # a LaTeX command after the dash hid a coordinator from the first-word test
    18:  [", "],          # ...asymmetry---\textbf{not instruction-following...}: contrastive
    199: [", "],          # ...interpretable---\textbf{but it clears...}: coordinator
    # "segment already has a colon" fired on a colon that is a run-in label or
    # that sits *after* the dash, where the label/gloss colon is still correct
    21:  [": "],          # \textbf{(1)~equalization}: siblings (2),(3),(5) all take a colon
    14:  [", "],          # B. Construct-validity test (4), different in kind: <gloss>
    # a semicolon needs a clause on both sides; these glosses are noun phrases
    38:  [", "], 39:  [", "], 46:  [", "], 57:  [", "], 69:  [", "],
    101: [", "], 139: [", "], 183: [", "], 190: [", "], 220: [", "],
    252: [", "], 257: [", "], 263: [", "], 270: [", "], 283: [", "],
    9:   [", "],          # appositive, matching the sibling items' own commas
    129: [", "],          # table cell: "complies with the deception instruction, sincerely"
    254: [", "],          # run-in title: "...is met here, the first time anywhere..."
    # a comma here would be the THIRD in a row: the site already reads
    # "---and, by EXP-R1c below, on six of six", whose inner commas are the
    # author's. A semicolon is the standard remedy for a series whose members
    # carry their own commas, and it is the same two characters, so the price is 0.
    109: ["; "],          # "...under the v1 bank; and, by EXP-R1c below, on six of six"
    268: [", "],          # "...pushes alpha down, against the claim being tested"
    # a semicolon needs a clause on both sides; inside a parenthetical the rule
    # also has to keep ONE separator level. This paren is a name followed by two
    # noun-phrase notes, and its first separator is already a comma, so a
    # semicolon for the second inverts the hierarchy. Same two characters, price 0.
    50:  [", "],          # "(\texttt{EQUALIZED\_CLAIMS\_V2}, zero shared claim strings, the same set EXP-R1c uses)"
    # a colon or semicolon would be the second one in the sentence; restructure
    25:  [" "],           # "(4) deception at fixed elicitation requires trials..."
    120: [" is "],        # "\item \textbf{UNKNOWN} is anything else: ..."
    192: [". This is "],  # "...survives. This is criterion 4, not the rung above it."
    # the three parallel Tier definitions in one caption segment (was REVIEW)
    42:  [" is "], 43: [" is "], 44: [" is "],
    # EXP-C4 summary row: a genuine pair, then a "so" consequence (was REVIEW)
    239: [" ("], 240: [") "], 241: [", "],
    # not a pair at all: the two dashes bracket a sentence boundary
    167: [", ", ". We give it "],
    # a pair whose parens would nest around competing prose, or would leave a splice
    200: [", ", ", "],    # long appositive on "Dim~2", set off by commas instead
    294: [": ", ", "],    # colon introduces the list, comma before the summative
    299: [": ", ", "],    # same, for the (a)--(e) grouping
    300: ["; ", ", "],    # "...is not new; X's organisms have it..., but no entry..."
    301: [" (", "); "],   # the closing dash carries adversative force: keep a clause break
    4:   [" (", " ("],    # a ;-list of `X---gloss` items: parenthesize each gloss
    8:   [", ", " ("],    # (iii) takes the comma its siblings (iv)/(v) use
    6:   [" ("], 166: [" ("], 243: [" ("], 251: [" ("], 262: [" ("],
}

# --- OVERRIDE, closing side only: ") " leaves an introductory adverbial, a
# --- non-restrictive relative, or a participial without its comma.
CLOSE_COMMA = {27, 72, 86, 93, 147, 153, 157, 197, 212, 218, 272, 284, 285, 320}

# --- INSERT: the closer for a parenthesis pair whose opener replaced a dash.
INSERT = [
    ("sections/appendix.tex",
     "the claim's truth-value, the condition label, and the detector's output;",
     "the claim's truth-value, the condition label, and the detector's output);"),
    ("sections/appendix.tex",
     "no observable is a child of exactly one $M_i$; and \\textbf{(A5)}",
     "no observable is a child of exactly one $M_i$); and \\textbf{(A5)}"),
    ("sections/appendix.tex",
     "this costs generation time and nothing else;",
     "this costs generation time and nothing else);"),
    ("sections/appendix.tex",
     "not to the identification of $\\tau_D$.",
     "not to the identification of $\\tau_D$)."),
    ("sections/appendix.tex",
     "not by evidence. mistral:7b's",
     "not by evidence). mistral:7b's"),
    ("sections/appendix.tex",
     "not a paired counterfactual on a single item.",
     "not a paired counterfactual on a single item)."),
    ("sections/appendix.tex",
     "plus fourteen LoRA and persona variants of them.",
     "plus fourteen LoRA and persona variants of them)."),
    ("sections/appendix.tex",
     "and now with requirement~(iii) actually satisfied.",
     "and now with requirement~(iii) actually satisfied)."),
]

WS = re.compile(r"[ \t]*\n?[ \t]*\Z")          # trailing space, at most one newline
props = json.load(io.open("/tmp/appendix_props.json", encoding="utf-8"))
ops = collections.defaultdict(list)
tally = collections.Counter()

# --- DECLINE: keep the em dash at sites at or after this source line in
# --- appendix.tex. Set by --decline-after=N; used to re-fund the appendix float
# --- pins (pp86-89) when the conversion's cumulative shrink moves them.
DECLINE_AFTER = None
for a in sys.argv:
    if a.startswith("--decline-after="):
        DECLINE_AFTER = int(a.split("=")[1])

for i, p in enumerate(props):
    if i in DROP:
        tally["DROP (kept as the not-applicable mark)"] += len(p["pos"])
        continue
    if (DECLINE_AFTER and p["file"] == "sections/appendix.tex"
            and p["line"] >= DECLINE_AFTER):
        tally["DECLINED (re-funds the pp86-89 float pins)"] += len(p["pos"])
        continue
    reps = list(OVERRIDE[i]) if i in OVERRIDE else list(p["rep"])
    if i in CLOSE_COMMA:
        assert reps[1] == ") ", (i, reps)
        reps[1] = "), "
    assert len(reps) == len(p["pos"]), (i, reps, p["pos"])
    for pos, rep in zip(p["pos"], reps):
        assert rep is not None, "unreviewed site %d" % i
        ops[p["file"]].append((pos, rep, i))
        tally["OVERRIDE" if i in OVERRIDE or i in CLOSE_COMMA else "as proposed"] += 1

print("=== review verdicts ===")
for k, v in sorted(tally.items()):
    print("  %-38s %4d" % (k, v))

changed = {}
for rel, lst in ops.items():
    path = os.path.join(D, rel)
    s = io.open(path, encoding="utf-8").read()
    lst.sort(reverse=True)
    seen = set()
    for pos, rep, i in lst:
        assert s[pos:pos + 3] == "---", (rel, pos, i, repr(s[pos - 20:pos + 20]))
        assert pos not in seen, (rel, pos)
        seen.add(pos)
        a = pos - len(WS.search(s[:pos]).group(0))          # absorb space before
        b = pos + 3
        while b < len(s) and s[b] in " \t":
            b += 1
        if b < len(s) and s[b] == "\n":                     # at most one newline
            b += 1
            while b < len(s) and s[b] in " \t":
                b += 1
        assert "\n\n" not in s[a:b], (rel, pos, "blank line")
        s = s[:a] + rep + s[b:]
    changed[rel] = s

for rel, old, new in INSERT:
    s = changed.get(rel) or io.open(os.path.join(D, rel), encoding="utf-8").read()
    n = s.count(old)
    if n != 1:
        print("INSERT anchor count %d (need 1): %r" % (n, old[:60]))
        sys.exit(2)
    changed[rel] = s.replace(old, new)

for rel, s in sorted(changed.items()):
    left = len(re.findall(r"(?<!-)---(?!-)", s))
    print("  %-28s remaining --- = %d" % (rel, left))

if "--check" in sys.argv:
    print("\ndry run, nothing written")
else:
    for rel, s in changed.items():
        io.open(os.path.join(D, rel), "w", encoding="utf-8").write(s)
    print("\nwrote %d files" % len(changed))
json.dump({r: [[p, rep, i] for p, rep, i in sorted(l)] for r, l in ops.items()},
          io.open("/tmp/r36_appendix_ops.json", "w", encoding="utf-8"), indent=1)
