#!/usr/bin/env python3
"""Gate the Reviewer map at the head of the appendix.

The map is a hand-typed table *about the artifact*, which is exactly the class of
prose that has drifted four times in this paper's revision history (rounds 23, 26,
32, 33 -- a stale run index, a superseded log still cited, a hand-kept tag list, and
two false appendix letters).  Nothing here is derived from a list a human maintains:

  1. every Run cell resolves to exactly ONE ``load_log()`` call site in the
     verifier -- 0 or >=2 both FAIL, because a substring match is a known loophole
     (``r78`` prefixes four tags, ``r86`` and ``r87`` two each);
  2. every resolved tag appears in ``REPRODUCE.md``;
  3. every Code cell names a file that exists in the copy the reviewer receives
     (``artifact/iclr-supplementary``, 94 runners -- NOT ``audit-sym``, 33);
  4. every appendix letter that has a ``\\subsection*`` is reachable from the map or
     from the reading-map prose, so trimming that prose cannot orphan an appendix;
  5. every Claim cell is a verbatim quote from the body, markup stripped;
  6. section and appendix cells are ``\\ref``s, never hand-typed letters or numbers.

Two positive controls run in the same invocation, because a ``0 -> 0`` silent pass
has fired repeatedly here: a deliberately bogus tag must FAIL resolution, and a
sentinel string must be absent from the map.

Usage: python3 check_reviewer_map.py     (from the paper directory)
Exit 0 on PASS, 1 on any failure.  A missing input is a failure, never a skip.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SHIPPED = os.path.join(REPO, "artifact", "iclr-supplementary")

APPENDIX = os.path.join(HERE, "appendix_domain_guards.tex")
BODY_FILES = [
    "abstract.tex", "introduction.tex", "related_work.tex",
    "methodology.tex", "experiments.tex", "conclusion.tex",
]
BEGIN, END = "% BEGIN reviewer-map", "% END reviewer-map"

failures = []
checks = 0


def check(ok, label):
    global checks
    checks += 1
    if not ok:
        failures.append(label)


def must_read(path, label):
    if not os.path.exists(path):
        failures.append("MISSING INPUT (%s): %s" % (label, path))
        return None
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------- normalise
# Same contract as check_protected_claims.py:normalise -- strip markup so a
# claim quoted with \emph{} still matches the body's plain wording.
_MARKUP = re.compile(r"\\(?:textbf|emph|texttt|textit|mathcal|mathrm|text)\b")


def normalise(s):
    s = _MARKUP.sub("", s)
    s = s.replace("~", " ")
    s = re.sub(r"[{}$\\]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


# ---------------------------------------------------------------- inputs
tex = must_read(APPENDIX, "appendix")
verifier = must_read(os.path.join(SHIPPED, "verify_claims.py"), "verifier")
reproduce = must_read(os.path.join(SHIPPED, "REPRODUCE.md"), "REPRODUCE.md")

# Round 47: the body this file reasons about is the RENDERED body, so every
# %-comment comes out before anything is searched. It matters in both
# directions. It fired as a false FAIL first: the round's own in-source note
# recording that `E3b' appears nowhere in the body put the string `E3b' in
# experiments.tex, and the lead-claim loop below read it -- a note about an
# absence became the absence's counterexample. The other direction is the
# latent one and is why the strip is done here rather than inside that loop:
# check 5b requires each Claim cell to be a verbatim quote of the section its
# row names, and until now a quote that survived only in a %-comment would have
# passed a check whose entire purpose is that a reviewer can read the sentence.
# Line structure is preserved so the \label{sec:...} splitting below is unmoved.
_COMMENT = re.compile(r"(?m)(?<!\\)%.*$")

body = []
for name in BODY_FILES:
    src = must_read(os.path.join(HERE, name), name)
    if src is not None:
        body.append(_COMMENT.sub("", src))
if failures:
    print("FAIL check_reviewer_map: unreadable input")
    for f in failures:
        print("  -", f)
    sys.exit(1)

body_norm = normalise(" ".join(body))

# Per-section normalised text, keyed by \label{sec:...}, at the FINEST
# granularity the file provides.  A Claim cell that is somewhere in the body but
# not in the section its own row names is a wrong pointer, and checking the
# concatenated body cannot see that: the readiness pass found four rows whose
# Run/Appendix pair did not correspond while every per-cell check was green.
SEC_TEXT = {}
for src in body:
    parts = re.split(r"(?m)^(\\(?:sub)?section\*?\{)", src)
    segs = [parts[0]] + [parts[i] + parts[i + 1] for i in range(1, len(parts) - 1, 2)]
    for seg in segs:
        for lab in re.findall(r"\\label\{(sec:[^}]+)\}", seg):
            SEC_TEXT[lab] = SEC_TEXT.get(lab, "") + " " + normalise(seg)
check(len(SEC_TEXT) >= 7,
      "only %d sec: labels chunked; the section splitter is broken" % len(SEC_TEXT))

# Derived, never hand-kept: the verifier's own LITERAL load_log() call sites.
# Round 45: this count is deliberately the literal one, because what this file
# needs is to resolve a Run cell's tag to exactly one call site. It is NOT the
# number of logs the verifier asserts against -- families addressed by a
# computed name are invisible to a source regex, which is why verify_claims.py
# now records stems as they are loaded and prints 77 where this prints 46.
# (Round 47 raised both by one, for the same log: r31_hardened_recipe.)
# Same regex as verify_claims.py's check_reproduce_index().
LOG_TAGS = sorted(set(re.findall(r'load_log\(\s*["\']([^"\']+)["\']', verifier)))
check(len(LOG_TAGS) >= 40,
      "expected >=40 literal load_log() call sites, got %d" % len(LOG_TAGS))


def resolve(short):
    """Tags matching `short` as a prefix.  Exactly one is required."""
    return [t for t in LOG_TAGS if t == short or t.startswith(short + "_")]


# ---------------------------------------------------------------- parse map
if BEGIN not in tex or END not in tex:
    print("FAIL check_reviewer_map: map delimiters not found in appendix_domain_guards.tex")
    sys.exit(1)
block = tex.split(BEGIN, 1)[1].split(END, 1)[0]

mid = block.split(r"\midrule", 1)
check(len(mid) == 2, "no \\midrule in map")
rows_src = mid[1].split(r"\bottomrule", 1)[0] if len(mid) == 2 else ""

rows = []
for raw in rows_src.split(r"\\"):
    line = "\n".join(l for l in raw.splitlines() if not l.strip().startswith("%"))
    if not line.strip():
        continue
    # \ub is the table's breakable underscore (see the .tex): expand it before
    # any cell is parsed, so a break hint can never hide a wrong file name.
    line = line.replace("\\ub ", "\\_").replace("\\ub", "\\_")
    cells = [c.strip() for c in line.split("&")]
    check(len(cells) == 5, "row has %d cells, expected 5: %.60s" % (len(cells), line.strip()))
    if len(cells) == 5:
        rows.append(cells)

check(len(rows) >= 10, "map has only %d rows; a map this short is not navigable" % len(rows))

# Appendix letters that exist, and the labels \applabel pins them to.
applabels = dict(re.findall(r"\\applabel\{([A-Z]+)\}\{([^}]+)\}", tex))
letters = re.findall(r"\\subsection\*\{([A-Z]+)\.\s", tex)
check(len(letters) >= 50, "expected >=50 appendix subsections, found %d" % len(letters))

label_to_letter = {v: k for k, v in applabels.items()}
cited_labels = set(re.findall(r"\\ref\{(app:[^}]+)\}", tex))

# ---------------------------------------------------------------- row checks
mapped_letters = set()
for claim, sec, run, app, code in rows:
    tag = "row %.40s" % normalise(claim)

    # 5. the Claim cell is a verbatim body quote
    check(normalise(claim) in body_norm,
          "%s: Claim not found verbatim in the body: %r" % (tag, normalise(claim)))

    # 5b. and it is in the section this row NAMES, not merely somewhere in the body
    m_sec = re.fullmatch(r"\\ref\{(sec:[^}]+)\}", sec)
    if m_sec:
        slab = m_sec.group(1)
        check(slab in SEC_TEXT, "%s: %s is not a section label in the body" % (tag, slab))
        if slab in SEC_TEXT:
            check(normalise(claim) in SEC_TEXT[slab],
                  "%s: Claim is in the body but NOT in %s, the section this row names"
                  % (tag, slab))

    # 6. section and appendix cells are \refs, not hand-typed
    check(re.fullmatch(r"\\ref\{sec:[^}]+\}", sec) is not None,
          "%s: section cell is not a bare \\ref{sec:...}: %r" % (tag, sec))
    check(re.fullmatch(r"\\ref\{app:[^}]+\}", app) is not None,
          "%s: appendix cell is not a bare \\ref{app:...}: %r" % (tag, app))

    m = re.fullmatch(r"\\ref\{(app:[^}]+)\}", app)
    if m:
        lab = m.group(1)
        check(lab in label_to_letter,
              "%s: %s has no \\applabel, so the letter it prints is unverified" % (tag, lab))
        if lab in label_to_letter:
            mapped_letters.add(label_to_letter[lab])

    # 1 + 2. tags resolve uniquely and are indexed
    shorts = re.findall(r"\\texttt\{([A-Za-z0-9\\_]+)\}", run)
    check(len(shorts) >= 1, "%s: no tag in Run cell %r" % (tag, run))
    for short in shorts:
        s = short.replace("\\_", "_")
        hits = resolve(s)
        check(len(hits) == 1,
              "%s: tag %r resolves to %d load_log() call sites %s (need exactly 1)"
              % (tag, s, len(hits), hits))
        if len(hits) == 1:
            check(hits[0] in reproduce,
                  "%s: resolved tag %r is not in REPRODUCE.md" % (tag, hits[0]))

    # 3. every named script exists in the shipped copy
    files = re.findall(r"([A-Za-z0-9\\_]+\.py)", code)
    check(len(files) >= 1, "%s: no script named in Code cell %r" % (tag, code))
    for f in files:
        fn = f.replace("\\_", "_")
        check(os.path.exists(os.path.join(SHIPPED, fn)),
              "%s: %s does not exist in artifact/iclr-supplementary" % (tag, fn))

# ---------------------------------------------------------------- reachability
# 4. No appendix may become unreachable.  Two tiers, because the reading map
# navigates partly by RANGE (`A--K`, `L--Z`, `AA--AZ`) and partly by \ref:
#   tier 1 -- every letter is inside a stated range or has a specific pointer;
#   tier 2 -- every per-run section (the two-letter AA--AZ block) has a
#             SPECIFIC pointer, since a 26-section range is not navigation.
# Specific pointers are counted across the whole document, not just this file:
# an appendix cited from the body is reachable.
prose = tex.split(BEGIN, 1)[0] + tex.split(END, 1)[1]
prose_head = prose.split(r"\subsection*{A.", 1)[0]

order = []
for letter in letters:
    if letter not in order:
        order.append(letter)

ranged = set()
for lo, hi in re.findall(r"\\textbf\{([A-Z]+)--([A-Z]+)\}", prose_head):
    if lo in order and hi in order:
        i, j = order.index(lo), order.index(hi)
        if i <= j:
            ranged.update(order[i:j + 1])

doc_refs = set(cited_labels)
for src in body:
    doc_refs.update(re.findall(r"\\ref\{(app:[^}]+)\}", src))
bare = set(re.findall(r"(?<![A-Za-z])([A-Z]{1,2})(?![A-Za-z])", normalise(prose_head)))

specific = set(mapped_letters)
for letter in order:
    lab = applabels.get(letter)
    if lab and lab in doc_refs:
        specific.add(letter)
    elif letter in bare:
        specific.add(letter)

orphans = [l for l in order if l not in specific and l not in ranged]
check(not orphans,
      "TIER 1: appendices unreachable from the map, the reading map and the body: %s"
      % ", ".join(orphans))

# The reading map states the map's row count in prose.  A count in prose is
# unchecked prose, and this paper has shipped a wrong one before.
stated = re.search(r"Reviewer map above indexes the (\d+)\b", prose_head)
check(stated is not None, "reading map no longer states the map's row count")
if stated:
    check(int(stated.group(1)) == len(rows),
          "reading map says %s rows, map has %d" % (stated.group(1), len(rows)))

per_run = [l for l in order if len(l) == 2]
vague = [l for l in per_run if l not in specific]
check(not vague,
      "TIER 2: per-run appendices with no specific pointer (range only): %s"
      % ", ".join(vague))

# ------------------------------------------------- claims the lead makes
# The lead paragraph asserts two things ABOUT THE BODY.  Both are claims about
# the artifact, which is the class that has drifted four times here, so both are
# measured rather than trusted.  Note the body is the six numbered files only:
# figure_overview.tex is \input AFTER \appendix, so its E3/E3b labels are
# appendix text, not body text.
for tag in ("E3", "E3b", "E3m"):
    hits = [n for n, src in zip(BODY_FILES, body)
            if re.search(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % tag, src)]
    check(not hits, "lead says %s appears nowhere in the body, but it is in %s"
          % (tag, ", ".join(hits)))

for term in ("Johnson", "Lindenstrauss", "linear aggregation", "random projection"):
    hits = [n for n, src in zip(BODY_FILES, body) if term in src]
    check(not hits, "lead says no body claim depends on the JL account, but %r is in %s"
          % (term, ", ".join(hits)))

# -------------------------------------------------- Appendix K's own tag claim
# Appendix K states that every run from r70 onwards is tagged in the appendix
# subsection that reports it.  That is a checkable claim about the artifact, and
# it was FALSE twice: for r72_structure_twin and r73_swap_twin, both reported in
# Appendix AB whose caption named only r75; and the sentence itself said
# "r70--r91", a hardcoded range that eight later runs (r92--r99) had outgrown.
# The range is now derived here rather than read from the prose.  Everything
# below r70 must instead be in K's own table.  Matching is substring-safe: a bare
# `r79` occurs inside the unrelated tag `r78_r79_bag_ties`, so a short form only
# counts when the next character cannot continue a tag name.
apx_sections = {}
_parts = re.split(r"(?m)^(\\subsection\*\{)", tex.replace(block, ""))
for _i in range(1, len(_parts) - 1, 2):
    _seg = _parts[_i] + _parts[_i + 1]
    _m = re.match(r"\\subsection\*\{([A-Z]+)\.", _seg)
    if _m:
        apx_sections[_m.group(1)] = _seg
check(len(apx_sections) >= 50,
      "only %d appendix subsections chunked; the splitter is broken" % len(apx_sections))
k_table = apx_sections.get("K", "")
check(len(k_table) > 2000, "Appendix K's tag table did not chunk (%d chars)" % len(k_table))


def names_tag(text, t):
    """Does `text` name tag `t`, in full or as an unambiguous short form?"""
    if re.search(t.replace("_", r"\\?_"), text):
        return True
    # Round 45.  An appendix subsection may name a whole run FAMILY with a glob --
    # Appendix AL's heading reads `r82\_split*`, `r82\_ladder*`, `r82\_null*` for fifteen
    # logs addressed in the verifier by a computed name.  So the moment one of those stems
    # is loaded LITERALLY (the holdout join reads r82_ladder71 to check that two scripts'
    # intervals agree digit for digit) it appears here and is reported as tagged nowhere,
    # while the appendix does name it.  Same blind spot verify_claims.py's REPRODUCE index
    # had this round, in a second script: a family addressed by a computed name is invisible
    # to a check that greps for literals.  The glob is honoured, not the failure silenced.
    for g in re.findall(r"(r\d+(?:\\?_[A-Za-z0-9]+)*)\*", text):
        if t.startswith(g.replace("\\_", "_")):
            return True
    short = re.match(r"r\d+[a-z]?", t)
    if not short:
        return False
    # reject `r79` inside `r78\_r79\_bag\_ties`: a real short reference is not
    # followed by another name segment.
    return re.search(short.group(0) + r"(?![0-9A-Za-z]|\\?_)", text) is not None


for t in LOG_TAGS:
    n = re.match(r"r(\d+)", t)
    num = int(n.group(1)) if n else -1
    if num >= 70:
        where = [L for L, s in apx_sections.items() if names_tag(s, t)]
        check(bool(where),
              "Appendix K claims every run from r70 onwards is tagged in the "
              "subsection reporting it, but %s is named in no appendix subsection" % t)
    else:
        check(names_tag(k_table, t),
              "%s is below r70, so Appendix K's table must list it, and does not" % t)
# The prose must not re-hardcode a range: that is what drifted.
check("r70}--\\texttt{r91" not in tex and "r70--r91" not in tex,
      "Appendix K states a hardcoded tag range again; eight runs outgrew the last one")

# ---------------------------------------------------------------- controls
# CONTROL: the registration matcher must reject a tag that is genuinely absent,
# and must NOT be fooled by the substring collision it exists to handle.
check(not names_tag(" ".join(apx_sections.values()), "r777_absent_run"),
      "CONTROL: registration matcher matched an absent tag")
check(not names_tag(r"tags \texttt{r78\_r79\_bag\_ties}", "r79_composition_depth"),
      "CONTROL: short form matched inside a longer tag name")
check(names_tag(r"tag \texttt{r79}", "r79_composition_depth"),
      "CONTROL: legitimate short-form reference not matched")
# A bogus tag must fail to resolve -- proves resolve() can say no.
check(len(resolve("r999_not_a_real_run")) == 0, "CONTROL: bogus tag resolved")
# `r87` and `r78` really are ambiguous here, so the uniqueness test must bite:
# `r87` prefixes r87_boolean_tier3 and r87_regression_poly8, which is why the map
# spells that row's tag in full.
check(len(resolve("r87")) >= 2, "CONTROL: prefix 'r87' should be ambiguous but is not")
check(len(resolve("r78")) >= 2, "CONTROL: prefix 'r78' should be ambiguous but is not")
# A truncated prefix must NOT match by substring -- resolve() is segment-aware.
check(len(resolve("r9")) == 0, "CONTROL: prefix 'r9' matched by substring")
# A sentinel must be absent -- proves the map text is actually being read.
check("ZZQQ-map-sentinel" not in block, "CONTROL: sentinel found in map")
check(len(block) > 1500, "CONTROL: map block only %d chars -- parse likely broken" % len(block))

# ---------------------------------------------------------------- report
print("check_reviewer_map: %d rows, %d checks, %d literal load_log() sites, %d appendix letters"
      % (len(rows), checks, len(LOG_TAGS), len(set(letters))))
if failures:
    print("FAIL (%d):" % len(failures))
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("PASS")
sys.exit(0)
