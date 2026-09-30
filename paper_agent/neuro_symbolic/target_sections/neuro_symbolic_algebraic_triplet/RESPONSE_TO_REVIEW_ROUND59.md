# Response to Review, Round 59

Thank you; this is the most actionable review the paper has had, because §18 asks for
three specific things and says of the first one *"This is already in the paper; it just
needs to be made more rhetorically central."* That diagnosis is exactly right, and it is
the diagnosis we have now acted on: **every object your §18 asks for was already in the
paper**, and the three that most needed routing were nowhere near the pages you were
reading them for, the control ladder on **p6**, the reason trained readouts must be
included on **p5**, and the `boolean8` comparison on **p8**. The round is therefore almost
entirely routing, not writing.

Below: what shipped, then what we measured (including two places where the measurement
contradicts the ask), then what we declined and why, with the arithmetic in each case.

---

## 1. What shipped

Your §18's three items, your §17, your §12 and your §13, in the objects you named.

| your ask | what shipped | where |
|---|---|---|
| §18.1: the anti-tautology argument, then *immediately* the empirical example | the **number** now sits on p2: `+0.874 or +0.22 by control choice` | `introduction.tex:172`, p2 |
| §17 / §18.2: three claims, everything maps to one | §1's three items now labelled `(i) Empirical`, `(ii) A consequence`, `(iii) Positive` | `introduction.tex:326`, p2 |
| §12: make the frozen-family / unseen-partition protection prominent | `\textbf{frozen}, on \emph{partitions it never saw}` | `introduction.tex:326`, p2 |
| §18.2: the arc *shortcut → framework → twin → positive result* | the prevalence survey no longer sits between the twin and the results; it now follows Figure 1 | `introduction.tex`, p1–p2 |
| §18.3: make the positive result's scope painfully explicit | the depth-8 number now names its corpus: `at depth~8 on \texttt{poly8} ($0.736$)` | `abstract.tex:137`, p1 |
| §13: release the exact final artifact, one command per headline experiment | a missing runner shipped, three wrong command cells corrected, **ten** new one-command wrappers | `artifact/iclr-supplementary` |

**§18.1, in full.** The paragraph that ends *"Only the third is the audit statistic, and
no published evaluation reports it"* now continues *"— one cell, $+0.874$ or $+0.22$ by
control choice."* That is the whole tautology answer in one clause: the same encoder, the
same cell, and a margin that moves by **0.654** depending on which control you are willing
to call *"the invariant baseline."* Pages 1–2 previously asserted the distance from *"use a
strong control"* four times and **measured it zero times**; the number came from
`methodology.tex:332` on p6, where the ladder is printed in full. See §2 below for it.

**§17, and one deliberate exception.** Items (i) and (iii) now carry your words verbatim.
Item (ii) is labelled `A consequence` rather than `Methodological`, and that is a decision
rather than an oversight: `(ii) now reads "A consequence."` is the answer we gave the
round-50 reviewer, and (more importantly) **your methodological claim is the criterion,
which is that paragraph's lead sentence, not item (ii).** Relabelling (ii) would file the
consequence as the contribution and demote the criterion to an unlabelled preamble. Your
three words map on as: *Methodological* = the lead sentence, *Empirical* = (i),
*Positive* = (iii), with (ii) the consequence that follows from the first.

Worth knowing, since it is the same routing story again: **§3 already carries your exact
taxonomy on p5**; `methodology.tex:271` reads *"(i) Necessary … (ii) Methodological, and
ours … (iii) Empirical … (iv) Proved, not open."* Your §17 asks for a three-way split the
paper already makes, one page after the place you were reading.

**§13, and the two defects measuring it found.** `REPRODUCE.md` already had a section
headed literally *"One command per headline object."* Measuring your ask against the
shipped tree found that the manual and the artifact disagreed in two ways:

1. **`run_r102_composition_lattice.py` was in no shipped copy.** Row R47 tells the reader
   to run it, its log *is* shipped, and `verify_claims.py` asserts against that log in all
   three copies, so §4.4's `arrangement` row and Appendix BC were **verifiable and not
   reproducible.** The supplement shipped 96 runners against the project copy's 97; it now ships 97.
2. **Three command cells named files that exist under those names in no copy**:
   `run_r11_feynman_trained.py`, `run_r21_feynman_trained_perequation.py`,
   `run_r28_external_audit.py`. The real runners are `run_feynman_trained.py`,
   `run_feynman_trained_perequation.py`, `run_external_audit.py`, each proved by its own
   `default="<tag>"`, because the tag in those rows is a **log stem**, not a filename. A
   reader following three rows of our own manual got `No such file or directory`.

Neither was visible to any assertion we had: the logs were indexed, the programs that
produce them were not. Both are fixed, and a new gate now compares the manual to the file
list (§5 below).

**Ten wrappers, and which of them we actually ran.** `reproduce/` goes from 5 wrappers to
15, plus the `all.sh` driver, each a thin shell over the `REPRODUCE.md` command in the same
row and each ending in `python3 verify_claims.py`, so a green run is an assertion pass and
not a claim of one. **A wrapper nobody has executed is a claim, so `REPRODUCE.md` now
separates them:**

- **Executed end-to-end, exit 0, each ending in a full 2591/2591 pass:**
  `r98_family_robustness.sh` (21.8 s including the verifier), `r95_code_audit.sh` (23.4 s),
  `r90_external_audit_lample.sh` (26.6 s, on its checkpoint-absent branch), and
  `r96_scan_audit.sh` (4 min 52 s, *including* the SHA-256-pinned SCAN download). For the
  three that rewrite a shipped log, the re-run JSON was compared leaf by leaf against the
  shipped one: **26 of 28, 360 of 363 and 293 of 295 leaves identical**, the only
  differences being the run timestamp and the path we redact for anonymity. Every
  scientific value reproduced exactly.
- **Not executed here, and the reason is not the same for all six:** five need the EQNET
  corpora this tree does not redistribute (`r92_family_stress` ~72 s,
  `r91_nonlocal_composition` ~43.9 min, `r94_order_diversity` ~49.6 min,
  `r93_deep_composition` ~183.5 min, `r102_composition_lattice` ~2 h 58 min): `r92` is
  72 s of CPU with no training, so the corpora are its entire cost;
  `r97_scan_composition` (~33 min) fetches its own SCAN split and is blocked instead by GPU
  time, 10 epochs × 3 seeds. `r90`'s checkpoint-present branch cannot run from this tree at
  all: the ~1 GB published checkpoint is the original authors' to distribute.

---

## 2. §15's tautology attack, answered with the ladder

You name this as the harshest-reviewer paragraph, and you are right that it is the paper's
one real battle. Here is the whole of it, from `methodology.tex:332`, at `poly8` `K=500`:

| control | score | apparent margin against the encoder's `0.894` |
|---|---|---|
| Laplacian spectrum | `0.020` | `+0.874` |
| `F₃`'s best single member, one fixed readout | `0.276` | `+0.618` |
| that same member, readout **fitted** | `0.284` | — |
| the bound over **every** readout, nothing trained | `0.296` | `+0.598` |
| the full-token bag, order-blind and identity-anonymised | `0.517` | `+0.377` |
| such bags **composed** | `0.676` | `+0.22` |

The paper prints **five** margins for those six rows: `+0.874, +0.618, +0.598, +0.377 or
+0.22` — *"according to which control is called the invariant baseline"*, which is why the
statistic must be a supremum and not a member. The fitted-readout row (`0.284`) is there for
a different purpose: it is the step that shows *fitting* moves the number at all.

If admissibility auditing were *"a formal restatement of the requirement that the control be
sufficiently strong"*, then all six rows would be interchangeable choices of a strong
control and the margin would not move. It moves by **0.654 at one cell**. And the
restatement reading has no way to produce the two results that follow from the definition
rather than from care: **fitting the readout raised the ceiling at *every* cell we
measured, by up to `+0.107`**, and **closing the family over readouts leaves one of our own
passes unproved by `0.0027`** at `boolean8 K=50` (`0.8706` against a bound of `0.8733`),
a pass we withdraw against ourselves, where that family's strongest *member*, `0.732`,
would have shown `+0.139`. **Hygiene has no theorem.** Good experimental hygiene does not
predict that its own author's result fails by three parts in ten thousand; a supremum over
a declared family does, and did.

That argument lived on p6. It now also lives, as a number, on p2.

---

## 3. Your §18.1's obvious edit is forbidden by our own gate, one round later

This is worth disclosing plainly, because it is the honest reason the *reason* stayed on
p5. The obvious way to serve §18.1 is a new §1 sentence restating the criterion:
supremum, declared family, tested membership, trained readouts. **We cannot write it.**

Round 58's reviewer scored main-text information density at the rubric's low mark, and the
cause we found was *accumulation*: the criterion was stated four times on pages 1–2, each
time because a different reviewer had asked for one more unmistakable statement of it. Each
individual ask was reasonable; the fourth made the first unreadable. So round 58 added
`check_restatement_budget()`, the repository's first **upper**-bound assertion (every
earlier one is a floor) capping `introduction.tex` at **three** sentence segments carrying
both a ceiling token and a family token. A fourth fails the gate.

So §18.1 shipped as a **number**, not a statement. `one cell, $+0.874$ or $+0.22$ by control
choice` carries no ceiling token and no family token, so it is outside the unit that check
counts, and §1 still prints *"3 segments (floor 2, ceiling 3)"*: confirmed by running the
gate, not by reading it. A number is not a fifth assertion of the criterion; it is the
evidence the first four were asserting without.

Worth saying which routes we did **not** take, because the check names them itself. Its
blind-spot note documents two ways past it: insert the fifth statement *inside* a segment
the check already counts, "because the unit is the segment and not the clause", or put it in
the paper's §2 or §3, "because the budget is scoped to §1, where the density was measured".
Both were open to us and both would have reinstated the accumulation the gate exists to
stop: one by hiding a restatement inside a sentence, the other by moving it out of the
section where we measured the accumulation in the first place. We used neither.

The *mechanism* (that trained readouts must be included because post-composition preserves
admissibility) stays at `methodology.tex:277` on p5, and we priced moving it: the
truthful compression is ~40 rendered characters into `introduction.tex:172`, and p2 holds
**6.197pt** of slack against a body line of **11.6pt**, with the number's own clause
already spending most of it. **Declined with the arithmetic** rather than shipped by
pushing a page.

Sixteen consecutive rounds have produced a collision between a reviewer's request and a
standing requirement. This is the first in which the collision is with our own tooling, and
we think that is the correct outcome: the gate exists precisely to stop the fourth
restatement, and it stopped ours.

---

## 4. §11, terminology load, answered by grep

Measured on the flattened `pdftotext` output of pages 1–9: the rendered main text, not the
sources. **Six of your sixteen terms carry no main-text load at all:**

| term | occurrences, p1–p9 | note |
|---|---|---|
| `skyline` | **0** | **round 55's reviewer asked for exactly this replacement, and it was declined on the same measurement**: the word was already at zero in the rendered main text. It survives, deliberately, in the appendix in its own metric sense, in one node of Figure 5 (p16), and in the shipped artifact's identifiers: `run_r67_score5_skyline.py`, `logs/r69_skyline_sweep.json`, `REPRODUCE.md`. Renaming it in the paper would desynchronise the paper from the supplement a reviewer is invited to run. The reasoning is on record at `appendix_domain_guards.tex:6–17` |
| `readout closure` | **0** rendered, anywhere | the phrase is *yours*, not ours: its six occurrences in our sources are all `%` comments. Our gate for the concept deliberately accepts any of `trained readouts`, `readouts included`, `readout-closed` |
| `protocol asymmetry` | **0** | not the paper's phrase anywhere, in text or comment (1 bare `asymmetry`) |
| `coverage axis` | **0** as a phrase | 11 bare `coverage`, and the only occurrence of the phrase tree-wide is a comment; the coverage remainder is scoped to §3.2 |
| `F1` | **1** | |
| `F2` | **1** | `F1` and `F2` occur **once each, in the same clause on p5**: *"F1 variable bags, F2 operator/arity bags, F3 = …"*, one definition line, not a burden |

The eight that are genuinely load-bearing, and that we accept are a real cost:
`S1` 16 · `S2` 19 · `S3` 20 · `F3` 14 · `admissib*` 26 · `ceiling` 36 · `twin` 18 ·
`family-relative` 7 · `ϕ` 13 · `cue` 18 · `certif*` 8 · `resolution` 5. `resolution`'s five
uses are all the content of `prop:resolution`/`cor:supremum`: a named result rather than
jargon.

We would rather you check this than take it from us: `pdftotext -f 1 -l 9`, strip the
line-number gutter, and grep.

Your own four-sentence compression of the framework is excellent, and we note it is almost
entirely already in the paper: `introduction.tex:172` (*"could the best such control have,
over trained readouts as well as feature maps?"*), the twin paragraph, and
`abstract.tex:92`'s *"the best score any control strong on the task yet blind to the claimed
property can reach, trained readouts included."*

---

## 5. §12, the forking-paths protection: prominence, not absence

Measured on the render. The protection is not missing; it was in the **last clause** of a
long item: word **71** of a **76**-word item, inside a **245**-word paragraph. (Counted on
`pdftotext` output of p2, not on the source: the source count is inflated by macro tokens.)

- **p2**: *"a bound we try to break three ways: by hand, by adversarial search, and by
  re-scoring that search's winner, frozen, on partitions it never saw."* `frozen` is now
  **bold** and `partitions it never saw` *italic*; both spans were unmarked before this
  round. Bold on both was built and reverted: it cost a rendered line, taking p2 from
  **+6.197pt to −0.695pt**. Italic is width-neutral where bold is not, so the shipped pair
  costs nothing on a page that has 6.197pt to lose.
- **p2**: *"Predictions were registered in the runners before the runs; four failed, and
  all four are printed."*
- **p8**, the same protection in full, with numbers: *"that winner frozen, re-scored on
  four partitions it never saw, +0.16 to +0.27."*
- **p9**, `experiments.tex:401`: *"One frozen pipeline throughout; inferential claims are
  restricted to the contrasts prespecified in §…, so every exploratory appendix test is
  descriptive."*
- the supplement ships **`PREREGISTRATION_r101_holdout_sweep.md`** and
  **`PREREGISTRATION_r103_library_size.md`**, written before those runs.

Your list (architectures, depths, K values, families, protocols, partitions, corpora,
heads) is answered by p8's sweep, p9's frozen pipeline and those two files. We did not
restate the defence, because restating it is the defect §3 above describes. The one funding
edit we designed for this promotion (`that search's winner` → `that winner`) was declined:
round 51's response letter quotes that phrase verbatim to a reviewer as proof the
five-partition protection is in the main paper twice, so shortening it would have falsified
a letter we had already sent.

---

## 6. §18.3: your scope sentence attaches the partiality to the wrong claim

You propose *"…on poly8, with partial replication on Boolean8."* We shipped the corpus name
(`abstract.tex:137` now reads *"at depth 8 on `poly8` (0.736)"*) and we did **not** ship
that sentence, because measured against `experiments.tex:218` it is the wrong way round:

- on `boolean8` the encoder clears the criterion **more** decisively, not less:
  **`7.6×` against `poly8`'s `5.0×`**;
- the **twin margin widens** to **`+0.299`**;
- what fails on `boolean8` is the **coverage mechanism**: its coverage ladder is
  non-monotone, so *"the coverage-closure **mechanism** is polynomial- **and**
  encoder-specific."*

So *"partial replication"* would concede the wrong half. The paper's own version is the
stricter one: *"as composition-of-known-transformations generalization, scoped to K≥200
here. That is not compositional reasoning: four primitives are not a library"*
(`abstract.tex:137`), and *"on `poly8` and two further EQNET corpora, one a different
algebra … up to unseen compositions of known rewrites"* (`introduction.tex:326`). The
positive result is scoped by *which claim*, not by *how much replicated*.

We take your §18.3 as a diagnosis: the scope was not painfully explicit enough, and
answered it in the place the number is, rather than by adopting the sentence.

---

## 7. §19: your epigram is declined, with the arithmetic, and that is the finding

You ask for *"The framework ports; the conclusion need not"* and explicitly forbid a section
claiming the framework applies to NLP, code or symbolic regression. **We added no such
section**, and we did not add the epigram either, because we priced it in all four places
its content already lives and **no truthful swap exists in any of them**:

1. **`abstract.tex`'s third paragraph** already closes *"the audit ports to language and to
   code, where **our own** inversion fails to replicate."* The shortest truthful insertion
   is +23 rendered characters with 41 in `\textbf`; at the 4.64 pt/char we measured for
   *extending* a bold run in this abstract, that is ~107pt against 56.81pt of tail. It buys
   a line on p1, which holds **0.561pt**.
2. **`introduction.tex`'s third paragraph, p2** already says *"language and code two ports
   of the same code."* Only your second half is needed there: +24 characters ≈
   89–106pt against 73.17pt of tail, over by 16–32pt, and the clause it would extend is
   quoted in two earlier response letters.
3. **`experiments.tex:230`** has 186.85pt of tail and *would* hold it, but that sentence
   already ends *"portability, not general validation, never prevalence"*, which is a
   protected needle and is quoted in **ten** of our earlier response letters. Appending your epigram beside a
   pinned clause that already says it is round 58's accumulation defect at one clause'
   distance instead of two pages'.
4. **§4.4's title is already *"The Audit Ports; Our Own Inversion Does Not"*** (`experiments.tex:221`, p8): your
   epigram's exact grammatical shape, with our nouns and a **stronger** second half: a
   named failure to replicate rather than a hedge. Swapping in your wording would weaken
   it.

`experiments.tex:401` carries the same boundary as a limitation: *"What we cannot yet show
is a **reversal** on a non-symbolic benchmark built by others: the code corpus we settle is
ours."* We would rather say that than say *the conclusion need not port*, which is the
weaker claim.

---

## 8. §7 and §10: how we market it, and why several asks shipped as swaps

**§7.** We agree, and the paper says so on p2 in bold: *"So this is a paper about
evaluation, not about encoders: the contribution is that protocol — we call it
admissibility auditing — and symbolic-expression encoders are the **case study** where it
revises published conclusions"* (`introduction.tex:80`). The abstract closes
*"The audit is the deliverable; the findings are its test."* If that framing is not reaching
you, the failure is placement, not intent, which is this round's theme.

**§10.** The main text is 9 pages; `E THICS S TATEMENT` is the first body line of p10.
The page budget is why this round is a swap round rather than an addition round, and the
numbers are: total slack across eleven pages **17.552pt**, distributed p1 **+0.561** ·
p2 **+6.197** · p3 **+9.463** · **p4 0.000** · p5 **−0.695** · p6 **−1.927** ·
p7–p10 **0.000** · p11 **+0.687**, against a body line of **11.6pt**. The largest single
pocket is 9.463pt on p3, so **17.552pt is not one spendable line anywhere**, and p4 (
Table 1's page) is at zero. Every insertion this round was funded inside its own page by a
deletion or an emphasis demotion; where no funding existed we declined and showed the
arithmetic (§3 and §7 above).

---

## 9. The build you read, and one thing that is still unreviewed

You read `iclr2027_conference(20260914-122739).pdf`. `figure_audit.tex` on disk is dated
**15:11:55** the same day, **2 h 44 min after** your build, so **round 58's Figure 1 fix
was not in the PDF you read.**

That matters because of what it fixed. Three consecutive reviewers (rounds 55, 57 and 58)
reported Figure 1's graded verdict band as **absent**, and one of them quoted its caption in
the same review. The cause was not naming: a band drawn beneath a numbered strip **inherits
the axis of the object above it** and reads as a fifth step, so it was skipped as a step
rather than read as a grading. Round 58 fixed it on the drawing: a hairline plus the words
*"a grading, not a fifth step"*. **You are the first reviewer in four not to report the band
as missing, and we are explicitly not claiming that as evidence the fix worked**, because
your build predates it. Figure 1's band remains, as far as review goes, unread.

---

## 10. What this round added to the tooling, and one defect it caught in its own prose

`check_reproduce_manifest()` is new, and it is the first assertion here that compares
`REPRODUCE.md` to the **file list** of the shipped artifact. (Not, we should be precise, the
first to read the artifact at all: another check has read the supplement's `verify_claims.py`
since round 51, and `verify_claims.py`'s own block [24] checks `REPRODUCE.md` against the 85
logs it asserts. What nothing compared was the manual against the programs.) Five halves:
every runner named in a command cell exists; wrapper cells and `reproduce/*.sh` agree **in
both directions**, since one direction alone is satisfiable by deletion; every wrapper
sources `_common.sh`, ends at `verify` and names only existing runners; the three
deliberately unshipped inputs are allowlisted **by name with a reason** and each one's
disclosure must still be in `REPRODUCE.md`; and every wrapper is **named in the
executed-versus-untested list.**

That fifth half exists because it caught us. Asking *"is it ready?"* of this round's own new
artifact prose found that nine of the ten new wrappers were listed as executed or untested
and **`r92_family_stress` was in neither**, while the same sentence asserted *"all five need
the EQNET corpora"* of a set one of whose members (`r97`, which fetches its own SCAN split)
does not. Four halves of the gate passed on that text, because a wrapper can be in the
table, on disk and `bash -n`-clean while being named nowhere in the prose that says whether
anyone has ever run it. Both are fixed and both are now gated. **A count in a disclosure is
a universal quantifier wearing a numeral**, and the fix is to require the population rather
than the number.

Board after the round: 0 LaTeX errors · 0 undefined references or citations · 0 floats too
large · exactly the 2 pre-existing overfull boxes at unchanged sizes (`\vbox` 6.4211pt,
`\hbox` 3.509pt) · **101 pages** · the eleven-page slack profile byte-identical to the
pre-round baseline on **every** page, p1 +0.561 · p2 +6.197 · p3 +9.463 · p4 0.000 ·
p5 −0.695 · p6 −1.927 · p7–p10 0.000 · p11 +0.687 · four gate scripts pass, and the
deliberate-corruption
control fails on all **49** of them (41 before this round) · assertion suite
**2591/2591**, unchanged, md5 identical across all three copies · both artifact copies
`__pycache__`-free and clean of author-identifying paths.

---

## 11. One question back

Scope/generalization at 6.5 is now the low mark, and the low mark has moved three rounds
running (Significance, then Clarity, now Scope), while **six consecutive reviewers have
told us not to run more experiments.** Round 57's jump (Novelty 6.5 → 8.5 on
positioning-only work, no new evidence) suggests those two facts are related: the score is
tracking where claims are stated, not what is proved.

So: **is Scope 6.5 a verdict on what we claim, or on where we say it?** Every object your
§18 asks for was already in the paper, three of them on pages 5–9, and your own §18.1
says so. If the answer is *where*, we would rather be told which page a reader stops on than be
given another axis, because we can fix placement inside a zero-sum page budget and we
cannot fix scope without claiming more than we proved.
