#!/usr/bin/env python3
"""Build /tmp/verify_r36.py from /tmp/verify_r35.py.

Round 36 replaced every prose em dash in the paper with ordinary punctuation.
Under the standing rule, ALL 2230 round-35 checks are retained; the ones this
round deliberately changes are UPDATED with the round-36 reason in a comment,
never deleted.

Pass 1 (mechanical, this file's whole point): 84 retained checks pin prose
strings that contained `---`. Rather than hand-editing 84 literals -- which is
exactly how a near-miss substitution defect gets in -- every affected Python
string literal is re-derived by SPAN ALIGNMENT: locate the literal in the
pre-conversion snapshot of the file it pins, map its character span through the
conversion, and read the replacement out of the live file. A literal is only
touched when it occurs exactly once in exactly one pre-conversion file AND is
absent from the live tree, i.e. only when the conversion actually broke it.

Pass 2 (hand-written, below): the checks whose *logic*, not whose literal, this
round changes -- the historical edit ledgers, the abstract word ratchet, the
byte-identity assertions, and the float-pin table.
"""
import difflib
import io
import json
import os
import re
import sys
import tokenize

D = "/Users/mediratta/code/paper_writing/AI-Researcher-align/output/adaptive_lie_detector_paper"
PRE = "/tmp/r36_snapshots/PRE"
SRC = "/tmp/verify_r35.py"
OUT = "/tmp/verify_r36.py"
FILES = ["main.tex", "sections/abstract.tex", "sections/introduction.tex",
         "sections/related_work.tex", "sections/methodology.tex",
         "sections/experiments.tex", "sections/discussion.tex",
         "sections/conclusion.tex", "sections/appendix.tex"]


def char_opcodes(a, b):
    """Character opcodes for large texts: align lines first, refine blocks."""
    al, bl = a.splitlines(keepends=True), b.splitlines(keepends=True)
    ao, off = [], 0
    for ln in al:
        ao.append(off)
        off += len(ln)
    ao.append(off)
    bo, off = [], 0
    for ln in bl:
        bo.append(off)
        off += len(ln)
    bo.append(off)
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, al, bl,
                                                       autojunk=False).get_opcodes():
        sa, ea, sb, eb = ao[i1], ao[i2], bo[j1], bo[j2]
        if tag == "equal":
            out.append(("equal", sa, ea, sb, eb))
            continue
        for t2, x1, x2, y1, y2 in difflib.SequenceMatcher(
                None, a[sa:ea], b[sb:eb], autojunk=False).get_opcodes():
            out.append((t2, sa + x1, sa + x2, sb + y1, sb + y2))
    return out


print("loading pre/post pairs and building alignments ...")
PAIR = {}
for rel in FILES:
    pre = io.open(os.path.join(PRE, rel.replace("sections/", "")), encoding="utf-8").read()
    post = io.open(os.path.join(D, rel), encoding="utf-8").read()
    PAIR[rel] = (pre, post, char_opcodes(pre, post))
    print("  %-28s %d opcodes" % (rel, len(PAIR[rel][2])))


def map_span(rel, x, y):
    """Map pre-conversion span [x,y) to the live file; None if not clean."""
    pre, post, ops = PAIR[rel]
    lo = hi = None
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            if i1 <= x < i2 and lo is None:
                lo = j1 + (x - i1)
            if i1 < y <= i2:
                hi = j1 + (y - i1)
        else:
            # a span must not START or END inside a changed region, or the
            # mapped boundary would be arbitrary; nudge outward to the block edge
            if i1 <= x < i2 and lo is None:
                lo = j1
            if i1 < y <= i2:
                hi = j2
    if lo is None or hi is None or hi < lo:
        return None
    return post[lo:hi]


src = io.open(SRC, encoding="utf-8").read()

# ---- lines that belong to a HISTORICAL edit ledger, which pass 1 must NOT touch.
# A ledger entry is (old, new) text from the round that made it; it is replayed
# against the round-22 baseline to rebuild the word bag. Converting its em dashes
# would rewrite history and -- measured -- breaks the replay chain for every later
# round: 2 corrupted R23_EDITS literals cascaded into 5 round-28..34 failures.
# The live-tree side of those replays is handled in pass 2 by UNCONVERT instead.
_sl = src.split("\n")
LEDGER_LINES = set()
for _i, _l in enumerate(_sl, 1):
    if re.match(r"R\d+_EDITS\s*=", _l):
        _j, _d = _i, 0
        while _j <= len(_sl):
            _d += _sl[_j - 1].count("[") - _sl[_j - 1].count("]")
            LEDGER_LINES.add(_j)
            if _j > _i and _d <= 0:
                break
            _j += 1
print("ledger lines excluded from pass 1: %d" % len(LEDGER_LINES))

toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
lines = src.splitlines(keepends=True)
loff, off = [], 0
for ln in lines:
    loff.append(off)
    off += len(ln)


def abspos(row, col):
    return loff[row - 1] + col


edits = []          # (start, end, new_source_text, rel)
skipped = []
for t in toks:
    if t.type != tokenize.STRING:
        continue
    try:
        val = eval(t.string, {"__builtins__": {}}, {})
    except Exception:
        continue
    if not isinstance(val, str) or "---" not in val:
        continue
    if t.start[0] in LEDGER_LINES:
        continue
    hits = []
    for rel in FILES:
        pre, post, _ = PAIR[rel]
        if pre.count(val) == 1 and post.count(val) == 0:
            hits.append(rel)
    if len(hits) != 1:
        if hits:
            skipped.append((t.start, "ambiguous across %s" % hits, val))
        continue
    rel = hits[0]
    pre = PAIR[rel][0]
    x = pre.index(val)
    new = map_span(rel, x, x + len(val))
    if new is None or new == val:
        skipped.append((t.start, "span did not map cleanly", val))
        continue
    a, b = abspos(*t.start), abspos(*t.end)
    prefix = re.match(r"[a-zA-Z]*", t.string).group(0)
    quote = '"""' if t.string[len(prefix):].startswith(('"""', "'''")) else None
    if quote:
        skipped.append((t.start, "triple-quoted, updated by hand in pass 2", val))
        continue
    edits.append((a, b, prefix + repr(new) if prefix else repr(new), rel))

print("\nliterals to re-derive: %d   skipped: %d" % (len(edits), len(skipped)))
for st, why, val in skipped:
    print("  SKIP line %d: %-38s %r" % (st[0], why, val[:60]))

out = src
for a, b, new, rel in sorted(edits, reverse=True):
    out = out[:a] + new + out[b:]

# ======================================================================= PASS 2
# The checks whose LOGIC round 36 changes. Same discipline as every earlier
# mk_verify_r*.py: each substitution must match exactly once, or nothing is
# written. Every one carries the round-36 reason as a comment in the output.
pass2 = []


def sub(old, new, label):
    pass2.append((old, new, label))


# ---- (a) the UNCONVERT helper -------------------------------------------------
# Rounds 30-35 each replay their own edit ledger against the LIVE appendix.tex /
# related_work.tex, asserting the post-edit text is present exactly once. Round 36
# rewrote that text, so the assertion must be made against the pre-conversion
# form. UNCONVERT inverts round 36 on a file's text using the same 538-entry
# ledger that produced the conversion (/tmp/r36_edits.json, round-tripped against
# every pre-conversion snapshot by /tmp/gen_r36_edits.py). This keeps all 55
# historical assertions intact and byte-exact instead of restating them.
sub('''def read(f):
    return io.open(SEC + f, encoding="utf-8").read()
''',
    '''def read(f):
    return io.open(SEC + f, encoding="utf-8").read()


# ROUND-36: the em-dash conversion. Every prose `---` in the paper became ordinary
# punctuation (445 sites in appendix.tex/related_work.tex applied by offset, 87 in
# the main text applied as a string ledger). R36_EDITS is the unified (file, old,
# new) ledger; gen_r36_edits.py asserts that replaying it on the pre-conversion
# snapshot of each of the 9 files reproduces the live file byte-for-byte.
R36_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r36_edits.json",
                                                 encoding="utf-8"))]
R36_BY_FILE = {}
for _r, _o, _n in R36_EDITS:
    R36_BY_FILE.setdefault(_r.replace("sections/", "").replace(".tex", ""),
                           []).append((_o, _n))


def UNCONVERT(text, name):
    """Map live text back to its pre-round-36 form, for historical replays.

    Rounds 30-35 pin their own ledger's post-edit text against the live appendix
    and related_work. Round 36 rewrote that prose, so those pins are asserted
    against the un-converted text rather than restated -- the historical
    assertion is preserved exactly, and round 36 is the documented reason.
    """
    for _o, _n in R36_BY_FILE.get(name, []):
        text = text.replace(_n, _o)
    return text
''',
    "inject UNCONVERT")

# ---- (b) route the five historical side-bags through it ------------------------
for _line, _old, _new in [
    (1675, '    appx_led = read("appendix.tex")',
           '    # ROUND-36: un-convert before replaying a round-30 pin (see UNCONVERT)\n'
           '    appx_led = UNCONVERT(read("appendix.tex"), "appendix")'),
    (1714, '    r31_side = {"appendix": read("appendix.tex"),\n'
           '                "related_work": read("related_work.tex")}',
           '    # ROUND-36: un-convert before replaying round-31 pins (see UNCONVERT)\n'
           '    r31_side = {"appendix": UNCONVERT(read("appendix.tex"), "appendix"),\n'
           '                "related_work": UNCONVERT(read("related_work.tex"),\n'
           '                                          "related_work")}'),
    (1746, '    r32_side = {"appendix": read("appendix.tex")}',
           '    # ROUND-36: un-convert before replaying a round-32 pin (see UNCONVERT)\n'
           '    r32_side = {"appendix": UNCONVERT(read("appendix.tex"), "appendix")}'),
    (1794, '    r34_side = {"appendix": read("appendix.tex")}',
           '    # ROUND-36: un-convert before replaying round-34 pins (see UNCONVERT)\n'
           '    r34_side = {"appendix": UNCONVERT(read("appendix.tex"), "appendix")}'),
    (1835, '    r35_side = {"appendix": read("appendix.tex"),\n'
           '                "related_work": read("related_work.tex")}',
           '    # ROUND-36: un-convert before replaying round-35 pins (see UNCONVERT)\n'
           '    r35_side = {"appendix": UNCONVERT(read("appendix.tex"), "appendix"),\n'
           '                "related_work": UNCONVERT(read("related_work.tex"),\n'
           '                                          "related_work")}'),
]:
    sub(_old, _new, "side-bag at L%d" % _line)

# ---- (c) the three remaining word-bag / float replays that read the live tree ----
# Same reason as the five side-bags: these compare the LIVE text against a
# pre-round-36 baseline, so the live side is un-converted rather than the historical
# assertion being weakened.
sub(r'''    _p1flat = re.sub(r"\s+", " ",
                     " ".join(re.sub(r"^\s*\d{3}\s", " ", l) for l in p1))
    ck(_p1flat.count("operational identification audit for behavioral LLM") == 1,
       "T9's thesis sentence is not on p1 exactly once")''',
    r'''    _p1flat = re.sub(r"\s+", " ",
                     " ".join(re.sub(r"^\s*\d{3}\s", " ", l) for l in p1))
    # ROUND-36 SUBSTITUTION (the em-dash conversion): the abstract is four
    # whitespace-tokens longer -- `X---Y` became `X, Y` at four sites -- so p1
    # reflows and TeX now hyphenates "identifica-tion" INSIDE this very phrase.
    # Exactly as round 29 absorbed a line BREAK by whitespace-normalising, absorb a
    # line-break HYPHEN by allowing "- " between any two letters of the phrase. The
    # measurement is unchanged (the thesis phrase on p1 exactly once) and nothing
    # else can match: the phrase carries no real hyphen.
    _t9txt = "operational identification audit for behavioral LLM"
    _t9re = re.compile("".join(re.escape(_c) + (r"(?:- )?" if _c.isalpha() else "")
                               for _c in _t9txt))
    ck(len(_t9re.findall(_p1flat)) == 1,
       "T9's thesis sentence is not on p1 exactly once")''',
    "T9 thesis phrase, hyphen-tolerant")

sub('''    for name in ["introduction", "experiments"]:
        cur = io.open(SEC + name + ".tex", encoding="utf-8").read()''',
    '''    for name in ["introduction", "experiments"]:
        # ROUND-36: un-convert before comparing float internals with the round-22
        # baseline (see UNCONVERT). The conversion repunctuated fig:r1c_collapse's
        # caption; these arms pin each edited float's diff EXACTLY rather than
        # skipping it, so the comparison is made on the pre-conversion text and the
        # exact-diff property is preserved instead of being relaxed to a skip.
        cur = UNCONVERT(io.open(SEC + name + ".tex", encoding="utf-8").read(), name)''',
    "float-internal baseline compare")

sub('''    cur_cat = "\\n".join(io.open(SEC + n + ".tex", encoding="utf-8").read()
                        for n in BOLDED)''',
    '''    # ROUND-36: un-convert each file before the round-23..35 replay (see UNCONVERT).
    # The conversion splits `X---Y` into two whitespace tokens, so the word bag would
    # otherwise report 12 lost and 12 gained tokens that are punctuation, not prose.
    #
    # WHY THERE IS NO FORWARD `for old, new in R36_EDITS` STAGE HERE, unlike every
    # round from 23 to 35: those ledgers are paragraph-level rewrites whose `old`
    # strings are disjoint, so replaying them in order is order-independent. The
    # round-36 pairs are NOT -- each was widened with surrounding context until it
    # was two-way unique (gen_r36_edits.py), and that context frequently contains
    # text a LATER round-23..35 replacement also edits, so a forward R36 stage
    # appended after R35 fails `rebuilt.count(old) == 1` on the widened context.
    # Un-converting the LIVE text instead puts both sides of the comparison in
    # pre-round-36 punctuation and leaves the R23..R35 replay untouched, which is
    # the same "compare on the pre-conversion text" remedy used for `cur` above.
    # The round-36 ledger is not thereby unverified: 36d asserts it applies once
    # and inverts once against the live tree on its own.
    cur_cat = "\\n".join(UNCONVERT(io.open(SEC + n + ".tex", encoding="utf-8").read(),
                                  n) for n in BOLDED)''',
    "cur_cat word bag")

# ---- (d) 27c: a pin broken AT A DISTANCE, the only one in the paper -------------
# introduction.tex:54's `\\textbf{(2)~Protocol---an identification audit ...}` became
# a parenthetical, `\\textbf{(2)~Protocol (an identification audit ...)}`, so the
# clause is now followed by ")}" there and still by "}" in related_work.tex. The
# literal itself contains no `---`, so pass 1 could not see it. The measurement is
# unchanged and asserted at FULL strength: the clause must still be present at BOTH
# sites AND must still close its own bold group; only round 36's paren closer is
# tolerated between them.
sub('''    for f, t in [("introduction.tex", intro), ("related_work.tex", relw)]:
        ck("auditor can apply to a benchmark they did not build}" in t,
           f"27c: {f} lost their §9 clause 'a protocol an auditor can apply to a "
           f"benchmark they did not build'")''',
    '''    for f, t in [("introduction.tex", intro), ("related_work.tex", relw)]:
        # ROUND-36 SUBSTITUTION (em-dash conversion): see the note above 27c.
        ck(re.search(r"auditor can apply to a benchmark they did not build\\)?\\}",
                     t) is not None,
           f"27c: {f} lost their §9 clause 'a protocol an auditor can apply to a "
           f"benchmark they did not build', or the clause no longer closes its own "
           f"bold span")''',
    "27c two-site clause")

# ---- (e) the abstract ratchet: 403 -> 407, 383 -> 387, plus a stronger guard -----
sub('''    ck(len(_awords) == 403,
       f"29z: the abstract is {len(_awords)} words, pinned at 403 (401 before "
       "this round, 388 before round 30, 511 before round 29). If this changed "
       "deliberately, re-read 27g and R2 first")''',
    '''    # ROUND-36 SUBSTITUTION (em-dash conversion): 403 -> 407. Every prose `---` in
    # the paper became ordinary punctuation; the abstract has four of them, and
    # `X---Y` is ONE whitespace-delimited token where `X, Y` is two. No prose was
    # added. Updated rather than relaxed, and the ratchet is RESTORED at full
    # strength below by re-counting the un-converted abstract, which must still be
    # exactly the 403 words round 31 pinned.
    ck(len(_awords) == 407,
       f"29z: the abstract is {len(_awords)} words, pinned at 407 (403 before "
       "round 36's em-dash conversion, 401 before round 31, 388 before round 30, "
       "511 before round 29). If this changed deliberately, re-read 27g and R2 "
       "first")''',
    "29z abstract 403 -> 407")

sub('''    ck(len(_abody_words) == 383,
       f"29z: the abstract's non-Scope body is {len(_abody_words)} words, pinned "
       "at 383 -- only A4's tau_E rewording may move it")''',
    '''    # ROUND-36 SUBSTITUTION: 383 -> 387, the same four punctuation artifacts as
    # above. All four are in the BODY, so the Scope sentence is still pinned at 20
    # words by the difference check that follows.
    ck(len(_abody_words) == 387,
       f"29z: the abstract's non-Scope body is {len(_abody_words)} words, pinned "
       "at 387 (383 before round 36's em-dash conversion) -- only A4's tau_E "
       "rewording and round 36's repunctuation may move it")''',
    "29z body 383 -> 387")

sub('''    ck(len(_awords) < 511,
       f"29z: the abstract grew back past its pre-round-29 length ({len(_awords)})")''',
    '''    # ROUND-36: the ratchet at FULL pre-conversion strength. Inverting round 36 must
    # give back exactly the 403/383 words round 31 pinned -- which proves the four
    # extra tokens are punctuation artifacts and that NO prose entered the abstract,
    # the property this ratchet exists to hold. Any real word added to the abstract
    # fires here even though the live counts moved.
    _abs36 = UNCONVERT(absr, "abstract")
    _body36 = _abs36[_abs36.index("\\\\begin{abstract}") + 16:
                     _abs36.index("\\\\end{abstract}")]

    def _w36(_s):
        return [_t for _t in re.sub(r"\\\\[a-zA-Z]+\\*?|[{}$~\\\\]", " ", _s).split()
                if re.search(r"[A-Za-z0-9]", _t)]

    _n36 = len(_w36(_body36))
    _nb36 = len(_w36(_body36[:_body36.index("\\\\textbf{Scope:")]))
    ck(_n36 == 403,
       f"29z: un-converting round 36 leaves the abstract at {_n36} words, not "
       f"the 403 round 31 pinned -- so round 36 did more to the abstract than "
       f"repunctuate it")
    ck(_nb36 == 383,
       f"29z: un-converting round 36 leaves the non-Scope body at {_nb36} "
       f"words, not the 383 round 31 pinned")
    ck(_n36 - _nb36 == 20,
       f"29z: un-converted, the Scope sentence is {_n36 - _nb36} words, not 20")
    # and the conversion's size is itself pinned: -6 characters, four `---` sites
    # traded for four shorter marks.
    ck(len(absr) == 3248,
       f"abstract.tex is {len(absr)} chars, expected 3,248 (3,254 before round "
       f"36's four repunctuations)")
    ck(len(_awords) < 511,
       f"29z: the abstract grew back past its pre-round-29 length ({len(_awords)})")''',
    "29z un-converted ratchet + char pin")

# ---- (f) methodology.tex's character pin ----------------------------------------
sub('''    ck(len(meth35) == 15_687,
       f"35a: methodology.tex is {len(meth35)} chars, expected 15,687 "
       f"(c9718cf's 15,696 less Part A's 9) -- Part C is a pure move and Part A "
       f"is confined to five \\\\rungrow column-1 arguments, so any other value "
       f"means an unledgered edit entered §2")''',
    '''    # ROUND-36 SUBSTITUTION (em-dash conversion): 15,687 -> 15,669. §2 carries
    # three prose em dashes; repunctuating them costs 18 characters. Updated rather
    # than relaxed, and restored at full strength on the next line: un-converting
    # round 36 must give back exactly 15,687, so round 35's "Part C is a pure move"
    # claim is still asserted against the same number it was measured at.
    ck(len(meth35) == 15_669,
       f"35a: methodology.tex is {len(meth35)} chars, expected 15,669 (15,687 "
       f"before round 36's three repunctuations) -- Part C is a pure move and Part "
       f"A is confined to five \\\\rungrow column-1 arguments, so any other value "
       f"means an unledgered edit entered §2")
    ck(len(UNCONVERT(meth35, "methodology")) == 15_687,
       f"35a: un-converting round 36 leaves methodology.tex at "
       f"{len(UNCONVERT(meth35, 'methodology'))} chars, not the 15,687 round 35 "
       f"pinned -- so round 36 did more to §2 than repunctuate it")''',
    "35a methodology char pin")

# ---- (g) fig:ladder's caption: the one pass-1 group left hybrid ------------------
# Pass 1 works token by token, and this pin is four implicitly-concatenated tokens.
# It re-derived the third correctly ("elicitation---necessary for," -> "elicitation
# (necessary for,") but the parenthesis CLOSER falls in the fourth token, which
# contains no `---` and was therefore skipped -- leaving the group matching neither
# the pre-conversion nor the live caption. Audited: this is the only one of the 17
# pass-1 groups that does not occur exactly once in the file it pins.
sub(r'''       "$\\tau_D$." in meth35,''',
    r'''       "$\\tau_D$)." in meth35,      # ROUND-36: the paren closer, see above''',
    "35b ladder caption closer")

# ---- (h) the byte-identity assertions against c9718cf ---------------------------
sub('''        ck(read(_f35 + ".tex") == _rename35(_was35),''',
    '''        # ROUND-36: un-convert before the byte-identity assertion (see UNCONVERT).
        # Round 36 repunctuated all six of these files; asserting on the
        # un-converted text keeps round 35's claim -- that nothing but the two key
        # renames and the two Gemma cites touched them -- byte-exact rather than
        # restating it more loosely.
        ck(UNCONVERT(read(_f35 + ".tex"), _f35) == _rename35(_was35),''',
    "35f rename-tolerant identity")

sub('''            ck(read(_f35 + ".tex") == _was35,
               f"35f: {_f35}.tex is not byte-identical to c9718cf; it cites "
               f"neither renamed key, so nothing this round may touch it")''',
    '''            # ROUND-36: un-convert first (see UNCONVERT) -- the assertion is that
            # no ROUND-35 edit touched these two files, and it is preserved exactly.
            ck(UNCONVERT(read(_f35 + ".tex"), _f35) == _was35,
               f"35f: {_f35}.tex is not byte-identical to c9718cf once round 36's "
               f"repunctuation is inverted; it cites neither renamed key, so "
               f"nothing but round 36 may touch it")''',
    "35f strict identity")

# ---- (i) the 223-pin table: four appendix labels move, and exactly four ---------
sub('''        ck(not _moved35,
           f"35g: round 35 moved {len(_moved35)} label(s) off their c9718cf "
           f"page: {[(k, _a35[k], _b35[k]) for k in _moved35[:6]]} -- the round "
           f"was costed at zero rulers and this is the check that proves it")''',
    '''        # ROUND-36 SUBSTITUTION (em-dash conversion): the conversion is a net shrink
        # of the appendix (445 dash sites), and the cumulative shrink upstream of
        # p86 reflows the last appendix pages, moving four appendix labels by one
        # page. PRICED, not waved through: bisected over nine builds, holding all
        # 223 pins costs 56 of the 445 dashes (declining every site at or after
        # appendix.tex:2100 holds them; 2110 does not), i.e. 56 em dashes kept in
        # prose to hold four appendix cross-references on the page they were on.
        # The user chose the full conversion and to re-pin the four. Updated rather
        # than deleted, and STRICTER than "not _moved35" was: the moved set must be
        # EXACTLY these four and each must move by exactly the recorded delta, so a
        # fifth label moving -- or any main-text, section or table pin moving --
        # still fires here.
        _R36_MOVED = {"app:causal_probes": (("AQ", "86"), ("AQ", "87")),
                      "app:exp_i_4th_scenario": (("AQ.1", "86"), ("AQ.1", "87")),
                      "app:machine_icc": (("AR", "89"), ("AR", "88")),
                      "tab:td_vs_fd": (("62", "87"), ("62", "86"))}
        ck(set(_moved35) == set(_R36_MOVED),
           f"35g: the labels that moved off their c9718cf page are "
           f"{sorted(_moved35)}, not the four appendix pins round 36's em-dash "
           f"conversion is costed at ({sorted(_R36_MOVED)})")
        for _k36 in sorted(set(_moved35) & set(_R36_MOVED)):
            ck((_a35[_k36], _b35[_k36]) == _R36_MOVED[_k36],
               f"35g: {_k36} moved {_a35[_k36]} -> {_b35[_k36]}, not the "
               f"{_R36_MOVED[_k36][0]} -> {_R36_MOVED[_k36][1]} round 36 is "
               f"costed at")''',
    "35g four re-pinned labels")

# ---- (j) GROUP 36: the round's own checks ---------------------------------------
sub('''    # ---- report -----------------------------------------------------------
    if fails:''',
    r'''    # ==================================================================== 36
    # ROUND 36: every prose em dash in the paper replaced with ordinary
    # punctuation. 602 `---` in the nine source files, 560 converted, 42 kept --
    # and the 42 are not prose: they are table "not applicable" marks, one table
    # legend, and two verbatim transcript separators. This group pins the
    # conversion from four independent directions, so that neither a missed site
    # nor a collateral edit can pass:
    #
    #   36a  scope      per-file dash counts, live AND un-converted
    #   36b  survivors  each of the 42 classified, exhaustively
    #   36c  artifacts  no punctuation artifact the conversion could have made
    #   36d  ledger     the 538-pair ledger applies once and inverts once
    #
    # 36d is what licenses UNCONVERT, which is how ~55 historical assertions from
    # rounds 23-35 are preserved byte-exact rather than restated (see UNCONVERT).

    _EM36 = re.compile(r"(?<!-)---(?!-)")
    _EN36 = re.compile(r"(?<!-)--(?!-)")
    # (file, em dashes now, em dashes before round 36, en dashes -- unchanged)
    _EXP36 = [("main.tex",         0,  14,   5),
              ("abstract.tex",     0,   8,   2),
              ("introduction.tex", 0,  28,  12),
              ("related_work.tex", 0,  43,  11),
              ("methodology.tex",  3,  31,  14),
              ("experiments.tex",  8,  41,  26),
              ("discussion.tex",   0,   2,   3),
              ("conclusion.tex",   0,   2,   5),
              ("appendix.tex",    31, 433, 249)]

    def _txt36(_f):
        return (io.open("main.tex", encoding="utf-8").read()
                if _f == "main.tex" else read(_f))

    _tot36 = _pre36 = 0
    for _f36, _now36, _was36, _en36 in _EXP36:
        _s36 = _txt36(_f36)
        _u36 = UNCONVERT(_s36, _f36[:-4])
        _tot36 += _now36
        _pre36 += _was36
        # ---- 36a. SCOPE, both directions. The live count says the conversion is
        # complete; the un-converted count says which dashes it was accountable
        # for, so a site added later cannot hide behind the same total.
        ck(len(_EM36.findall(_s36)) == _now36,
           f"36a: {_f36} has {len(_EM36.findall(_s36))} em dashes, expected "
           f"{_now36} -- round 36 converted every PROSE dash in the paper, and "
           f"what may remain is only a table's not-applicable mark")
        ck(len(_EM36.findall(_u36)) == _was36,
           f"36a: un-converting round 36 gives {_f36} "
           f"{len(_EM36.findall(_u36))} em dashes, not the {_was36} it had at "
           f"the start of the round -- the ledger no longer accounts for the "
           f"conversion")
        # en dashes are a DIFFERENT mark (ranges, "(1)--(3)", "69--80\%") and the
        # conversion must not have touched one: the count is equal on both sides.
        ck(len(_EN36.findall(_s36)) == _en36 == len(_EN36.findall(_u36)),
           f"36a: {_f36} has {len(_EN36.findall(_s36))} en dashes, expected "
           f"{_en36} both before and after the conversion -- an en dash is a "
           f"range or an enumeration, never punctuation round 36 may touch")
        # and every parenthesis the conversion opened, it closed.
        ck(_s36.count("(") == _s36.count(")"),
           f"36c: {_f36} has {_s36.count('(')} '(' against "
           f"{_s36.count(')')} ')' -- a parenthesis pair replacing a dash pair "
           f"lost one of its two halves")
        ck(_s36.count("(") - _u36.count("(") == _s36.count(")") - _u36.count(")"),
           f"36c: {_f36} gained {_s36.count('(') - _u36.count('(')} '(' but "
           f"{_s36.count(')') - _u36.count(')')} ')' in round 36")
        # ---- 36c. ARTIFACTS. Stated as "no MORE than before the conversion",
        # which is the exact claim (a pre-existing " . " in a verbatim block is
        # not this round's business) and needs no magic number.
        for _pat36 in [r" ,", r" ;", r" :", r",,", r";;", r",;", r";,", r",\.",
                       r"\(,", r",\)", r"\(;", r"\( ", r"::", r"\s\)", r",  ",
                       r", (?:and|but|or|so|yet), ", r"---,", r",---"]:
            ck(len(re.findall(_pat36, _s36)) <= len(re.findall(_pat36, _u36)),
               f"36c: the conversion introduced {_pat36!r} into {_f36} "
               f"({len(re.findall(_pat36, _u36))} -> "
               f"{len(re.findall(_pat36, _s36))})")
    ck(_tot36 == 42 and _pre36 == 602,
       f"36a: the paper carries {_tot36} em dashes against 42 expected, and had "
       f"{_pre36} against 602 -- these two numbers are what the response letter "
       f"states")

    # ---- 36b. THE 42 SURVIVORS, CLASSIFIED EXHAUSTIVELY. Each is a table cell
    # holding the not-applicable mark, a braced mark (\multicolumn or the table
    # legend), or one of two verbatim transcript separators. The partition is
    # asserted to be COMPLETE, so no prose dash can hide inside the allowance.
    for _f36, _cell36, _brace36, _verb36 in [("methodology.tex", 3, 0, 0),
                                             ("experiments.tex", 7, 1, 0),
                                             ("appendix.tex", 26, 3, 2)]:
        _s36 = read(_f36)
        # lookahead, not a consuming match: "& --- & --- &" is TWO cells
        _c36 = len(re.findall(r"&[ \t]*---[ \t]*(?=&|\\\\)", _s36))
        _b36 = len(re.findall(r"\{---\}", _s36))
        ck(_c36 == _cell36 and _b36 == _brace36,
           f"36b: {_f36} has {_c36} cell marks and {_b36} braced marks, "
           f"expected {_cell36} and {_brace36}")
        ck(_c36 + _b36 + _verb36 == len(_EM36.findall(_s36)),
           f"36b: {_f36}'s {len(_EM36.findall(_s36))} surviving em dashes are "
           f"not all accounted for as cell ({_c36}) + braced ({_b36}) + "
           f"verbatim ({_verb36}) -- an unclassified survivor is a PROSE dash "
           f"the conversion missed")
    ck(read("experiments.tex").count("\\textbf{---}~not expressible") == 1,
       "36b: tab:criteria's legend no longer explains the not-applicable mark, "
       "which is the reason those cells may keep their em dash")
    ck(read("appendix.tex").count("\\multicolumn{2}{c}{---}") == 3,
       "36b: the three spanned not-applicable cells changed shape")
    for _v36 in ["\\begin{verbatim}\n--- Transcript C: RLHF Refusal",
                 "Cascade (Claude Haiku 4.5) ---"]:
        ck(read("appendix.tex").count(_v36) == 1,
           f"36b: a verbatim transcript separator moved or was converted, and "
           f"verbatim text is quoted MODEL OUTPUT that may not be repunctuated: "
           f"{_v36[:40]!r}")

    # ---- 36d. THE LEDGER. /tmp/r36_edits.json is the round's single source of
    # truth: the main-text edits as an explicit string ledger, and the 445
    # appendix/related_work sites recovered by aligning the pre-conversion
    # snapshot against the live file (gen_r36_edits.py asserts BOTH directions
    # byte-exact). Here the two properties UNCONVERT depends on are re-asserted
    # against the live tree alone, so the check does not need /tmp to survive:
    # every `old` is gone, and every `new` occurs exactly once.
    ck(len(R36_EDITS) == 538 and len(R36_BY_FILE) == 9,
       f"36d: the round-36 ledger has {len(R36_EDITS)} pairs across "
       f"{len(R36_BY_FILE)} files, expected 538 across 9")
    _lsrc36, _bad36, _dash36 = {}, [], 0
    for _rel36, _o36, _n36 in R36_EDITS:
        _k36 = _rel36.replace("sections/", "").replace(".tex", "")
        if _k36 not in _lsrc36:
            _lsrc36[_k36] = _txt36(_k36 + ".tex")
        if _lsrc36[_k36].count(_o36) or _lsrc36[_k36].count(_n36) != 1:
            _bad36.append((_k36, _o36[:50], _lsrc36[_k36].count(_o36),
                           _lsrc36[_k36].count(_n36)))
        _dash36 += _o36.count("---") - _n36.count("---")
    ck(not _bad36,
       f"36d: {len(_bad36)} ledger pair(s) do not apply-once/invert-once against "
       f"the live tree, so UNCONVERT cannot be trusted and every historical pin "
       f"routed through it is void: {_bad36[:4]}")
    ck(_dash36 == 560,
       f"36d: the ledger accounts for {_dash36} converted em dashes, not the "
       f"602 - 42 = 560 the files actually show")
    ck(sum(1 for _r36, _o36, _n36 in R36_EDITS if "---" not in _o36) == 8,
       "36d: expected exactly 8 ledger pairs that carry no em dash -- the eight "
       "parenthesis CLOSERS that had to be inserted where no dash stood, which "
       "is the one class of edit in this round that is not a substitution")

    # ---- 36e. THE PRICE. 89 pages, the main text still closing on p9 at ruler
    # 485 with the Ethics statement opening p10 at 486. The conversion is a net
    # shrink, so the risk it carried was never overflow -- it was the four
    # appendix float pins that the cumulative shrink moves, priced at 35g.
    _pp36 = subprocess.run(["pdfinfo", "main.pdf"], capture_output=True,
                           text=True).stdout
    ck(re.search(r"Pages:\s+89", _pp36) is not None,
       f"36e: the document is not 89 pages: "
       f"{re.search(r'Pages:.*', _pp36).group(0) if 'Pages:' in _pp36 else '?'}")
    _p9_36 = subprocess.run(["pdftotext", "-layout", "-f", "9", "-l", "9",
                             "main.pdf", "-"], capture_output=True,
                            text=True).stdout
    _p10_36 = subprocess.run(["pdftotext", "-layout", "-f", "10", "-l", "10",
                              "main.pdf", "-"], capture_output=True,
                             text=True).stdout
    _r9_36 = re.findall(r"^ *(\d{3})", _p9_36, re.M)
    _r10_36 = re.findall(r"^ *(\d{3})", _p10_36, re.M)
    ck(_r9_36 and _r9_36[-1] == "485",
       f"36e: p9's last margin ruler is {_r9_36[-1] if _r9_36 else None}, not "
       f"485 -- the main text no longer ends exactly at the 9-page limit")
    ck(_r10_36 and _r10_36[0] == "486",
       f"36e: p10's first margin ruler is {_r10_36[0] if _r10_36 else None}, "
       f"not 486")

    # ---- report -----------------------------------------------------------
    if fails:''',
    "GROUP 36")

for old, new, label in pass2:
    n = out.count(old)
    if n != 1:
        sys.exit("PASS 2 anchor %r matched %d times (need 1): %r" % (label, n, old[:70]))
    out = out.replace(old, new)
print("pass 2 substitutions applied: %d" % len(pass2))

# a machine-readable record of pass 1, so the update is auditable
json.dump([{"line": src[:a].count("\n") + 1, "file": rel, "new": new}
           for a, b, new, rel in sorted(edits)],
          io.open("/tmp/r36_verify_literal_updates.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

io.open(OUT, "w", encoding="utf-8").write(out)
print("\nwrote %s (%d lines)" % (OUT, out.count("\n") + 1))
print("pass 1 record: /tmp/r36_verify_literal_updates.json")
