#!/usr/bin/env python3
"""Provenance gate for Figure 1's printed numbers.  Round 39.

WHY THIS EXISTS.  Round 38 verified the figure by decoding each bar's TikZ fraction and comparing it
to the number printed beside it.  Both read 0.277 for the bar labelled $\\sup\\mathcal{F}_3$ -- internally
consistent and wrong: 0.277 is the row BELOW the ceiling in Table tab:poly8_unseen, the tree-local bag,
a descriptor Definition~\\ref{def:audit_complete} does not enumerate and which therefore cannot set the
ceiling.  A consistency check is not a provenance check.  This gate asserts each printed value against
the APPENDIX ROW it is supposed to come from, so a value can no longer be self-consistently stale.

Usage:  python3 check_figure_provenance.py            # gate
        python3 check_figure_provenance.py --control  # positive control: must FAIL
"""
import re
import sys

FIG = "figure_framework.tex"
APP = "appendix_domain_guards.tex"

# (printed value, bar-label fragment in FIG, row-name fragment in APP, 1-based column of that row)
# Column indices count "&"-separated cells after the row name.  poly8 tables are
# K = 50 / 100 / 200 / 500 / 1000, so K=500 is column 4.
BARS = [
    ("1.000", "variable bag",              r"Feynman held-out \$0\.972\$",     None),  # inline, see NOTE
    ("0.972", "Tree-LSTM",                 r"Trained Tree-LSTM",               1),
    ("0.941", "operator/arity bag",        r"\\textbf\{Operator/arity bag\}",  2),
    ("0.872", "80M encoder",               r"\\textbf\{Published 80M encoder\}", 2),
    # pinned to the poly8 unseen-class table by its K=50 cell: a bare "^Tree-LSTM " also matches
    # rows in three other tables, which would let a wrong cell satisfy the check.
    ("0.894", "Tree-LSTM",                 r"^Tree-LSTM & \$\\mathbf\{0\.843\}",  4),
    # Round 47.  This slot held ("0.517", "token bag", "Bag (full token), strongest", 4) from round 39
    # until the cold read of pages 1-5 found that round 41 had raised the top of this chain to the
    # SEARCHED composite everywhere except here -- so the gate was pinning the stale, weaker control
    # into the paper's centrepiece figure while the abstract and tab:entitlements printed 0.676.  The
    # source is Appendix BB's own sentence, and the four-decimal value is inside the row pattern, so a
    # change to the searched number fails row lookup rather than passing a loose substring test; the
    # figure rounds to the three decimals the rest of the ladder prints.
    ("0.676", "best composite",             r"The best composite reads \$\\mathbf\{0\.6758\}\$", None),
    ("0.276", r"\\sup\\mathcal\{F\}_3\$\}", r"Bag \(\$\\sup\\mathcal\{F\}_3\$, the audit statistic\)", 4),
    ("0.994", "Tree-LSTM",                 r"\\textbf\{Trained Tree-LSTM\}",   1),
    ("0.723", None,                        r"Tree-edit-distance NN \(order\)", 1),  # caption, not a bar
]

# The value that must NOT appear as this figure's ceiling: the excluded tree-local bag at K=500.
EXCLUDED_AT_CEILING = ("0.277", r"Bag \(tree-local, S3; \$\\notin\\mathcal\{F\}_3\$\)")


def cells(line):
    """The &-separated cells after a row name, with LaTeX decoration stripped.

    Cells arrive as $0.894$, $\\mathbf{0.894}$ or ${0.894}$; strip the macros first, then every
    $ and brace, THEN read the leading number.  (Round 39: stripping braces with .strip("{}")
    left "${0.941}$" intact and the gate reported four false failures on its first run.)
    """
    out = []
    for p in line.split("&")[1:]:
        p = p.replace("\\\\", "").replace("\\mathbf", "").replace("\\textbf", "")
        p = p.replace("$", "").replace("{", "").replace("}", "").strip()
        m = re.match(r"([\d.]+)", p)
        out.append(m.group(1) if m else p)
    return out


def main():
    control = "--control" in sys.argv
    fig = open(FIG).read()
    app_lines = open(APP).read().split("\n")
    fails, checks = [], 0

    if control:
        fig = fig.replace("{$0.276$}", "{$0.277$}")

    # ---- 1. every numeric literal printed in the figure is accounted for by BARS
    printed = set(re.findall(r"\{\$\\?m?a?t?h?b?f?\{?([\d]\.[\d]{3})\}?\$\}", fig))
    printed |= set(re.findall(r"reaches only \$([\d]\.[\d]{3})\$", fig))
    declared = {v for v, _, _, _ in BARS} | {"0.500"}  # 0.500 is chance, fixed by construction
    unaccounted = printed - declared
    if unaccounted:
        fails.append(f"figure prints values with no declared appendix source: {sorted(unaccounted)}")

    # ---- 2. each declared value equals its appendix source row's cell
    for val, barlab, rowpat, col in BARS:
        checks += 1
        if val not in fig:
            fails.append(f"{val}: declared but not printed in {FIG}")
            continue
        hits = [l for l in app_lines if re.search(rowpat, l)]
        if not hits:
            fails.append(f"{val}: source row /{rowpat}/ not found in {APP}")
            continue
        if col is None:                      # inline prose row, substring match is the assertion
            # Round 47: the figure prints three decimals and an appendix sentence may print four
            # ("the best composite reads 0.6758"), so a bare substring test rejects a correctly
            # rounded bar -- 0.676 is not a substring of 0.6758.  Rounding is accepted only from a
            # LONGER literal in the same row, never the other way round, so a genuinely different
            # value still fails.
            def rounds_to(h, val):
                d = len(val.split(".")[1])
                return any(f"%.{d}f" % float(m) == val
                           for m in re.findall(r"\d\.\d{%d,}" % (d + 1), h))
            if not any(val in h or rounds_to(h, val) for h in hits):
                fails.append(f"{val}: not present in source row /{rowpat}/")
            continue
        got = {c[col - 1] for c in (cells(h) for h in hits) if len(c) >= col}
        if val not in got:
            fails.append(f"{val}: source row /{rowpat}/ col {col} reads {sorted(got)}, "
                         f"figure prints {val}")

    # ---- 3. the ceiling bar must not carry the EXCLUDED non-member's value
    bad, badrow = EXCLUDED_AT_CEILING
    checks += 1
    ceil_block = fig.split(r"\sup\mathcal{F}_3$};")
    if len(ceil_block) > 1 and bad in ceil_block[1][:200]:
        src = [l for l in app_lines if re.search(badrow, l)]
        fails.append(f"ceiling bar prints {bad}, which is the EXCLUDED tree-local bag "
                     f"(source row present: {bool(src)}) -- not $\\sup\\mathcal{{F}}_3$")

    print(f"checked {checks} figure values against {APP} source rows")
    for f in fails:
        print(f"  FAIL  {f}")
    if control:
        print("CONTROL: expected at least one FAIL above" if fails
              else "CONTROL DID NOT FIRE -- the gate is inert")
        return 0 if fails else 1
    print("PASS" if not fails else "FAIL")
    return 0 if not fails else 1


sys.exit(main())
