#!/usr/bin/env python3
"""Caption-vs-row gate: a float's caption may not print a value its own tabular contradicts.

WHY THIS EXISTS.  Round 41 found the caption of Table tab:stronger_baselines printing tree-edit
distance at 0.733 while the row directly beneath it printed 0.723 -- a value the paper's own defect
log (Appendix K) records as RETRACTED, corrected, and corrected in this paper's favour.  A retracted
number survived for rounds in the caption of the table that refutes it.

check_figure_provenance.py asserts a figure's printed values against their appendix source ROWS; it
says nothing about captions, and nothing at all about tables other than Figure 1's sources.  This gate
is the generalisation: for every float, every three-decimal literal in the caption must appear
somewhere in that float's own tabular body, or be declared here with a reason.  It is deliberately
mechanical -- it does not try to parse which baseline a caption sentence attributes a number to,
because the defect it exists to catch does not need that: 0.733 appeared NOWHERE in the tabular.

Usage:  python3 check_caption_rows.py            # gate
        python3 check_caption_rows.py --control  # positive control: must FAIL
"""
import glob
import os
import re
import sys

#: Three-decimal literals.  The paper writes the same value as $0.997$ in prose and $.997$ in a
#: narrow cell, so both forms must read as one number or the gate would fire on typography.
NUM = re.compile(r"(?<![\d.])(\d*\.\d{3})(?![\d])")


def canon(v):
    return v[1:] if v.startswith("0.") else v

#: Caption literals that are legitimately not cells, keyed by "<file>:<label>".  Every entry carries
#: its reason: this list is the gate's only loophole, so an entry added without one is a defect too.
#: Four legitimate kinds, and they are the only four -- a fifth kind is a finding, not an allowance.
#: (i) a CHANCE or null rate, fixed by the design rather than measured;
#: (ii) a DERIVED quantity: a difference, ratio or metric maximum computed from cells;
#: (iii) a value belonging to ANOTHER table or run family, cited as a contrast and attributed there;
#: (iv) a REPRODUCIBILITY tolerance about the cells rather than a value among them.
ALLOW = {
    "appendix_domain_guards.tex:tab:alpha_rename":
        {"0.125": "(i) chance, 1/8, stated as such in the caption"},
    "appendix_domain_guards.tex:tab:triplet_factorial":
        {"0.098": "(iii) tab:overlap's std for the same condition, cited to reconcile two "
                  "independent run families"},
    "appendix_domain_guards.tex:tab:diversity_sweep":
        {"0.125": "(i) chance at K=8"},
    "appendix_domain_guards.tex:tab:held_out_form":
        {"0.932": "(iii) tag r69's replication draw, attributed to it",
         "0.748": "(iii) tag r69's random arm, same replication"},
    "appendix_domain_guards.tex:tab:probe_ladder":
        {"0.500": "(i) the twin's chance rate; this table's cells are pinned-bag COUNTS"},
    "appendix_domain_guards.tex:tab:stronger_baselines":
        {"0.206": "(ii) derived: trained 0.994 minus untrained-depth-4 0.788, both cells"},
    "appendix_domain_guards.tex:tab:poly8_structural":
        {"0.030": "(iv) the carried-over cells' reproduction tolerance"},
    "appendix_domain_guards.tex:tab:composition_depth":
        {"0.005": "(i) chance at K=200, and (iv) the tie-rule re-score's cell movement",
         "0.993": "(iii) tag r76's depth-2 schema pair, on its own easier anchor sample",
         "0.997": "(iii) the same r76 pair's second value"},
    "appendix_domain_guards.tex:tab:k_sweep":
        {"0.969": "(ii) the metric's own maximum at k=3, min(m-1,k) over the class sizes",
         "0.908": "(ii) the same maximum at k=5",
         "0.723": "(ii) the same maximum at k=10 -- NOT tree-edit distance's twin score, which "
                  "shares the value by coincidence"},
    "appendix_domain_guards.tex:tab:deep_composition":
        {"0.500": "(i) the twin's chance rate"},
    "appendix_domain_guards.tex:tab:order_diversity":
        {"0.048": "(ii) a library-change delta on the forward column",
         "0.078": "(ii) the same delta on the second ladder",
         "0.204": "(iii) tab:nonlocal_swap's coverage effect, cited as the sensitivity anchor",
         "0.468": "(iii) the same table's second coverage effect"},
}


def brace_span(s, i):
    """Index just past the '{...}' group starting at s[i] == '{'."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j + 1
    return len(s)


def floats_in(text):
    """(label, caption_text, tabular_text, line_no) per float environment."""
    out = []
    for m in re.finditer(r"\\begin\{(table\*?|figure\*?)\}", text):
        start = m.start()
        endm = re.search(r"\\end\{" + re.escape(m.group(1)) + r"\}", text[start:])
        block = text[start:start + (endm.end() if endm else len(text) - start)]
        cap = ""
        cm = re.search(r"\\caption\{", block)
        if cm:
            cap = block[cm.end():brace_span(block, cm.end() - 1) - 1]
        bodies = []
        for t in re.finditer(r"\\begin\{tabular\}(\[[^\]]*\])?(\{[^}]*\})?", block):
            stop = block.find(r"\end{tabular}", t.end())
            bodies.append(block[t.end():stop if stop != -1 else len(block)])
        tab = "\n".join(bodies)
        lab = re.search(r"\\label\{([^}]*)\}", block)
        out.append((lab.group(1) if lab else "(unlabelled)", cap, tab,
                    text[:start].count("\n") + 1))
    return out


def main():
    control = "--control" in sys.argv
    here = os.path.dirname(os.path.realpath(__file__))
    fails, checked, floats = [], 0, 0
    used = set()
    # the loophole polices itself: an allowance without a reason is a defect of the same kind.
    for k, entries in ALLOW.items():
        for v, why in entries.items():
            if not why.strip().startswith(("(i)", "(ii)", "(iii)", "(iv)")):
                fails.append(f"ALLOW[{k}][{v}] has no reason of a declared kind")
    for path in sorted(glob.glob(os.path.join(here, "*.tex"))):
        text = open(path).read()
        if control and path.endswith("appendix_domain_guards.tex"):
            # reinstate the exact round-41 defect: the retracted value in the caption.
            text = text.replace("tree-edit distance ($0.723$) is the only",
                                "tree-edit distance ($0.733$) is the only")
        for lab, cap, tab, line in floats_in(text):
            if not tab.strip() or not cap.strip():
                continue          # nothing to cross-check
            floats += 1
            cells = {canon(v) for v in NUM.findall(tab)}
            key = f"{os.path.basename(path)}:{lab}"
            for val in sorted(set(NUM.findall(cap))):
                checked += 1
                if canon(val) in cells:
                    continue
                allowed = {canon(a): a for a in ALLOW.get(key, ())}
                if canon(val) in allowed:
                    used.add((key, allowed[canon(val)]))
                    continue
                fails.append(f"{key} (line {line}): caption prints {val}, "
                             f"absent from its own tabular "
                             f"({len(cells)} cell values)")
    # a stale allowance is unverified prose: if a caption no longer needs it, it must go.
    if not control:
        for k, entries in ALLOW.items():
            for v in entries:
                if (k, v) not in used:
                    fails.append(f"ALLOW[{k}][{v}] is never needed -- stale, remove it")
    print(f"checked {checked} caption literals across {floats} floats with tabulars, "
          f"{len(used)} via a declared allowance")
    if checked == 0:
        print("  FAIL  the gate scanned zero caption literals -- it is inert")
        return 1
    for f in fails:
        print(f"  FAIL  {f}")
    if control:
        print("CONTROL: expected at least one FAIL above" if fails
              else "CONTROL DID NOT FIRE -- the gate is inert")
        return 0 if fails else 1
    print("PASS" if not fails else "FAIL")
    return 0 if not fails else 1


sys.exit(main())
