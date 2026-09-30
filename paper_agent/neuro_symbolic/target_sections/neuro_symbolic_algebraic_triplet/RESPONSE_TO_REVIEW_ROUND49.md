# Response to Review: Round 49

Thank you. This is the ninth review on a ninth rubric, and the third in a row to leave correctness alone
and name a single remaining axis:

> §19: *"The biggest remaining risk is not correctness. It is whether reviewers view the contribution as a
> sufficiently substantial methodological advance rather than a very careful, elaborate audit framework
> whose central theorem is close to a formalization of an intuitive principle."*

**Four things stated before anything else, because three of them go against the grain of your advice and
one is a defect in our own work.**

**First, this round adds a run, and its own pre-registered stop rule then refused to let it train.** Your
§7 asks for *"a much larger transformation library than four primitives"* and adds *"you don't necessarily
need this before submission if compute is expensive."* We took the ask rather than the escape clause. But
compute was never the constraint: **the corpus is**, and we measured that before writing the training
code, not after. Two censuses (Appendix~BD, Table~38) establish that the largest *inventory-preserving*
rewrite library available anywhere in the 15-corpus survey is **five**, attained on `poly8`, the corpus
the paper already uses; the largest *repeatable* library is **four**, everywhere; **seven of the thirteen
shipped poly-side schemas fire on zero of `poly8`'s 1102 anchors**. Then the feasibility census showed
depth-8 delta-matched retention falls from `987/1102` at four members to `175/1102` at five, and that the
collapse is **structural, not a search budget** (`step_tries` `200/600/2000` → `175/212/198`, a plateau).
The pre-registration's stop rule (written before any of this) says fewer than `120` paired classes means
**do not train**. The run retained `89`; re-run at the census's own budget it retained `97`. **Nothing was
trained.** `run_r103_library_size.py` reports `0` encoders trained in both invocations, all nine
construction guarantees `true`, and the drop table settles which kind of shortfall it is: the bucket a
larger budget can empty (`depth_ladder`) *fell* `55 → 42` while the structural one
(`no_distribute_site`) *rose* `662 → 682`.

So §7's answer is a **measurement, not an apology, and not an accuracy claim in either direction**. The
paper's most-quoted concession (the abstract's closing sentence, *"four primitives are not a library"*)
is now a **measured** statement about the field's standard benchmark suite rather than a hedge: no corpus
in it offers a sixth admissible primitive, and nowhere does a fifth one repeat.

**Second, `verify_claims.py` rises 2438 → 2486 assertions**, all three shipped copies byte-identical
(md5 `5fa64467ef226550c86145934245bc85`), exit 0. Rounds 44 and 46 used the count *holding still* as
evidence that a presentation round stayed one; the converse obligation is that when a round adds a run,
the count has to rise and the first paragraph has to say so. The 48 new assertions are Table 38's
census row by row (including the `agree` flag per grouped row), both feasibility censuses, the nine
construction guarantees, the stop rule's own decision and threshold, and the two retention counts:
pinned **together**, so a future edit cannot separate the stop from the numbers that caused it.

**Third, the gate count rose too: `check_protected_claims.py --control` now fires 13, up from 12.** The
new check is this round's own near-miss turned into an assertion, and §G says what it caught.

**Fourth, and this is the defect: our own restructuring silently mis-routed 24 cross-references, and no
gate in the repository could see it.** Details in §G. Twenty-three were found by reading the rendered
page, which is now twenty of the last twenty-one rounds; the **24th** was found by the gate written to
close the first twenty-three, after that gate's own blind spot was widened; it had a vocabulary for the
two subsections the split created and none for the third subsection one reference should have named.

---

## A. The build you reviewed predates five of our six body files

You name the file you read: `iclr2027_conference(20260911-150511).pdf`. The build on disk when your review
arrived was 20:10:35 the same day. Source mtimes at that moment:

| file | mtime | vs 15:05:11 |
|---|---|---|
| `conclusion.tex` | 08:50:14 | before |
| `abstract.tex` | 09:10:00 | before |
| `introduction.tex` | **16:47:26** | **after** |
| `methodology.tex` | **17:28:48** | **after** |
| `related_work.tex` | **17:51:52** | **after** |
| `experiments.tex` | **19:53:47** | **after** |
| `appendix_domain_guards.tex` | **20:09:17** | **after** |

No copy of the 15:05:11 PDF survives locally, so a byte diff is impossible and the mtimes are the
evidence. **Every part of round 48's novelty-routing work is invisible to this reading**: Table 1 placed
on §1's six-object critical path, §3.3's retitle and re-gloss, Table 1's seventh `readout closure?`
column, the five-versus-three axis-count correction, §10's Transformer sourcing, Appendix F's retitle,
the AF citation fix, Table 37's precision, and r102's one body clause, which is exactly what your §12
asks for (see §F). Your §12 discusses Appendix BC in detail, so BC itself was present; the body clause
was not yet.

This is not an objection to your reading. It is a request that the version be pinned when you re-read, and
a note that two of your asks were already satisfied in source at the time you wrote.

---

## B. §7: the library ceiling, and the run that stopped itself

**The census (Appendix~BD, Table 38).** All 15 released corpora, three properties each, every property
thresholded at 20% of that corpus's anchor classes:

| corpus | classes | usable | inventory-safe | repeatable |
|---|---|---|---|---|
| `simplepoly5 / 8 / 10` | 47 / 104 / 195 | 4 | 3 | 3 |
| `poly5` | 150 | 5 | 4 | 4 |
| **`poly8`** | **1102** | **6** | **5** | **4** |
| `oneVarPoly10 / oneVarPoly13` | 83 / 677 | 6 | 5 | 4 |
| all eight boolean corpora | 95–7312 | 4 | 4 | 3–4 |

*Inventory-safe* is a tier condition, not a technicality: a rewrite that introduces an operator the corpus
never uses makes the held-out form separable by a **token multiset**, which is an **S1** cue by this
paper's own definitions, so a library that grows by such a schema does not measure composition at all.
That is what disqualifies `poly8`'s sixth *usable* schema, **`_rw_power_to_explog`** (`a*a → exp(2·log(a))`):
it fires on `313` of `1102` anchors with a site-independent token delta of `+6`, it is mechanically the
cleanest schema in the file, **it appears nowhere in any earlier draft of this paper**, and `poly8`'s
operator inventory is exactly `{+, -, *}`, so it introduces `exp` and `log`. Naming it and disqualifying it
is a stronger answer than quietly not having it: a primitive the corpus admits and the paper never
measured is a gap you could have found, and it is now closed in print with the reason.

**Two design decisions this census forced, both before code was written.**

1. **`|L|=6` is not available; `|L|=5` is.** The plan for this round assumed six. The kill clause would
   have fired *by construction* on the sixth member. Dropped from the library, kept as a finding.
2. **An inverse-rewrite library would have been degenerate by construction.**
   `_rw_remove_add_identity` and `_rw_remove_mul_identity` fire on **zero** of 1102 anchors, because
   EQNET's released forms are minimal: an inverse rewrite has no site until its forward partner creates
   one, at which point the pair **cancels** and a nominal depth-8 chain is really depth 6. That is round
   48's lesson (*write the design out in prose and ask what holds by construction before coding it*)
   applied in the right order for once.

**The run.** `run_r103_library_size.py`, two arms on **one** class set so every contrast is paired per
class: `L4` (the paper's four primitives, retrained here because a cross-run reference is not paired) and
`L5` (`L4` + `distribute`, restricted to its delta-`+4` sites by r91's `_apply_matched`). Both arms share
the depth-8 ladder and its twins **byte for byte** and differ only in which schemas their *training*
paraphrases instantiate; this is a library-**composition** contrast, deliberately *not* a
leave-one-primitive-out coverage test, which is r89's and r91's experiment and is what putting
`distribute` in the held-out chain would have measured instead.

**The stop rule fired.** `min_classes` `120`, pre-registered; `paired_classes` `89`; re-run at the
census's own `--step_tries 200 --site_tries 60`, `97`. Still 23 short. No encoder was trained. We report
this as the outcome rather than relaxing the threshold, and we report one further thing against
ourselves: **the pre-registration's feasibility projection was wrong by about a factor of two.** It
projected `~186` paired classes by multiplying two retention rates as though they were independent. That
arithmetic is printed in Appendix~BD rather than repaired, and it is **not** counted among §1's four
failed registered predictions: a projection inside a stop rule's rationale is neither a point prediction
nor a pre-committed branch, and inflating the count would be the same kind of accounting error in the
other direction.

**Body cost: one clause**, inside §4.5's existing axis table, `primitive` row: *"not established; ≤5
inventory-safe anywhere (App.~BD)."* No new row, no new sentence, no page.

**The appendix grew again**, in the band your §19.3 wants cut: Appendix~BD is new, and Table 38 with it.
We are declaring that rather than netting it out against §C's compression, because netting it out is how
a growth becomes invisible.

---

## C. §19.2: depth-8 now has a heading, which is the round's centre

Your §19.2 names the spine *"shortcut audit → twin → surviving composition → failure on novel inventory"*
and asks that depth-8 + twin sit at the absolute centre. **The section order was already that spine. The
third element had no heading.** `experiments.tex`'s depth-8 result was a `\paragraph` (about seven
rendered lines) **inside a subsection titled after the twin**, with no ToC entry and no handle of its
own. A reader scanning headings saw the twin and then the port-out; the result your §4 calls the one that
*"addresses what I previously considered one of the paper's largest weaknesses"* was invisible to that
scan.

It is now its own numbered subsection. The body headings read, in order:

| | heading |
|---|---|
| §4.1 | Only One Family Carries the S1 Flaw, and S2 Is an Entitlement |
| §4.2 | The Shape-Matched Twin: A Ceiling Known by Proof |
| **§4.3** | **Trained on Singles; Tested on Depth-8 Chains It Never Saw** |
| §4.4 | The Audit Ports; Our Own Inversion Does Not |
| §4.5 | The Protocol Changes the Generalization Claim |

That is your spine, recoverable from the headings alone. This was the only structural edit of the round,
and it was funded (measured empty first) out of §3.2, the paper's largest subsection and the one your
§19.3 most over-allocates: the `\paragraph{Terms, once.}` glossary block, whose definitions duplicate the
tier table directly above it, and horizontal tail room at the ends of §3.2's paragraphs. Slack after the
edit is byte-identical to the pre-round baseline on every page.

---

## D. §19.3: your page budget, priced against the rendered line numbers

The PDF carries ICLR line numbers, 54 per page, so the spans are exactly measurable rather than
estimable. **Section numbers in this table are the ones in the build you read**, before §C's split
renumbered §4.3 and §4.4 upward:

| §19.3's item | your budget | **measured** | delta |
|---|---|---|---|
| Introduction / motivation | 1.0 | §1 **1.55** | −0.55 |
| *(no related-work line)* | **0** | §2 **0.76** | −0.76 |
| Admissibility framework | 1.5 | §3 **3.2** | **−1.70** |
| Leakage audit | 1.0 | §3.4 + §4.1 **0.57** | +0.43 |
| Shape-matched twin | 1.0 | §4.2 **1.30** | −0.30 |
| **Depth-8 composition** | **1.5** | **0.13** (a `\paragraph`) | **+1.37** |
| Novelty axes | 1.0 | §4.4 **0.48** | +0.52 |
| External validation | 0.8 | §4.3 **0.31** | +0.49 |
| Limitations + conclusion | 0.7 | **0.40** | +0.30 |
| **total** | **8.5** | **~8.9** | **net −0.2** |

So *"compress aggressively"*, priced, is a **0.2-page cut and a 3.1-page shuffle**, and its largest line
item is the one we just executed: depth-8 from `0.13` toward `1.5`. The over-allocation is in **§3**, at
3.2 pages against your 1.5, which is where §C's funding came from.

**Two declines, with the reason rather than the assertion.** Your budget has **no related-work line**, and
§2 holds Table 1: the novelty table that rounds 47 **and** 48 both demanded be made findable, and that
round 48 wired onto §1's critical path. Cutting §2 to hit a budget would delete two predecessors'
requirements to satisfy a third. §2 and Table 1 stay. And we did not rebuild §3; the restructuring is
bounded to the one heading, because a 3.1-page shuffle executed at speed is how the mis-routed references
in §G happen, and they happened anyway, on a **one**-subsection edit.

---

## E. §19.1: the paper is not theorem-centric where you say it is, and the phrase you object to is a predecessor's requested de-sell

Two greps decide most of this.

**`abstract.tex` contains zero occurrences of *theorem*, *proposition* or *corollary*.** Its P2 already
reads *"admissibility auditing estimates the **ceiling** of a **declared** family … **trained** readouts
included, at three cue levels S1–S3"*, and its P1 is the reversal, which is your §19.1's requested
framing, close to verbatim, already in print. **§1 never cites `thm:necessity` in its body**: the single
occurrence in `introduction.tex` is a source comment recording that fact.
`methodology.tex` bills the numbered results *"as scoping, not as theoretical contributions"*, a clause
pinned `==1` by a gate because an earlier reviewer required it, and Appendix~AN clause (e) pre-concedes
this objection in the terms you use.

**Theorem 1's title stays, and here is why that is not stubbornness.** It reads *"A simple formal
justification for why admissibility ceilings are the appropriate statistic."* That wording is **round
39's reviewer's own requested de-sell**, granted in their words
(`RESPONSE_TO_REVIEW_ROUND39.md`: *"§7 do not oversell Theorem 1 | Retitled in your own words"*), and
round 40's reviewer **quoted the phrase back approvingly**. The lead words *"A simple formal
justification"* **are** the de-sell. Retitling it would be the tenth consecutive round in which one
reviewer's edit deletes a predecessor's requirement, and we have stopped doing that silently.

**What did change is one word, because you are right about the vocabulary.** §1 said *"the contribution is
that **criterion**"*; it now says *"the contribution is that **protocol** — we call it admissibility
auditing — and symbolic-expression encoders are the case study where it revises published conclusions."*
Your §19.1's three selling points (operationalizes invariant controls, estimates their ceiling including
trained readouts, demonstrates that conventional baseline comparisons can reverse the interpretation) are
what that sentence and the abstract's P2 now carry between them.

---

## F. The remaining points

| your point | the answer |
|---|---|
| **§10, elevate the adversarial search** | It has been **drawn on page 3** since round 47: Figure 2's rung S3 is three ascending bars, `\sup\mathcal{F}_3` `0.276` → best composite `0.676` → Tree-LSTM `0.894`, i.e. *"search finds increasingly strong controls but fails to close the gap"*, already a figure. What was missing was its **provenance**, so the bar is now labelled **`best of 706`**: the search's own size (`r101`'s `n_distinct_candidates_scored`; 28 primitives, 46 ladder calls). The four independent optima that make *"asymptotically"* true (`0.6523 / 0.6577 / 0.6635` against `0.676`) stay in Appendix~BB band (iii): that clause was this round's lowest-priority body edit and it was **dropped for space**, which we say rather than leave you to notice. |
| **§11, effect sizes more prominently** | Reported in a **stronger** form than you ask for, and now first in its paragraph: *"**A margin of $+0.22$**, $0.181$ clear of the encoder's bootstrap lower bound, over the strongest non-learned baseline an adversarial search over 28 primitives finds."* The `0.181` is the gap from the **lower end** of the encoder's bootstrap CI `[0.8572, 0.9232]` to the searched ceiling: more conservative than your `+0.218`, which is a subtraction of two rounded point estimates. **We do not print `+0.218`**: the log-derived margins are `+0.2208` and `+0.2202`, and the appendix already records that a per-$K$ margin computed from the printed three-decimal values and one computed from the logs *disagree in the last digit*. `+0.22` is the precision both derivations agree on. The fix you asked for was adjacency and ordering; that is what changed. |
| **§12, keep the lattice in the appendix, one body sentence** | **Already exactly one clause**, and more restrained than you ask: `experiments.tex`'s `arrangement` row carries *"also, unseen pair/triple ≤ +0.010 (App.~BC)"* and nothing else. Added at **19:53 on 2026-09-11, 4 h 48 m after the build you read** (§A). No edit this round. |
| **§13, simplify §1's first paragraph** | §1 opens on a **concrete measured example** (AI Feynman, `1.000` against `0.972`) in four sentences, then the boxed criterion. That is the structure your §13 prefers; it was already there in the source you did not have. **Fourteenth consecutive round in which we decline to paste a reviewer's own wording into the paper**, for the reason we have given each time: a reviewer writes the strong version of a claim, and pasting it ships an overclaim in their voice. |
| **§14, retitle** | **Declined, and this is the third consecutive round with a different proposed title.** Yours drops *Admissibility*, the coined term you elsewhere call the paper's real concept, in favour of *Invariant Controls*: the prior device that Table 1 scores `×` on every axis. Dropping *Stronger* deletes the thesis, which is that a stronger baseline can mislead. Rounds 47, 48 and 49 each named a **different** substitute; when three reviewers want three different titles, the title is not the defect. Unchanged: *When Stronger Baselines Mislead: Admissibility Auditing for Representation-Level Claims.* |
| **§16, AI disclosure** | Untouched, and named as untouched: round 37 required a precise one and it is still precise. It remains to be reconciled with the OpenReview form at submission time **without softening**. |
| **§3/§4/§5, the praise** | Named so the next reader can find the objects: `fig:framework`'s rung 4 (the ceiling ladder), §4.2 (the twin), and; now that it has a heading, **§4.3 by name**. |

---

## G. The defect this round found in its own work: 24 references pointing at the wrong subsection

Splitting depth-8 out of §4.2 (§C) left the label `sec:structural_scale` on the twin, which is correct and
was planned. But **23 prose references written before the split still named `sec:structural_scale` while
describing content that had moved into §4.3**: two in `experiments.tex`, 21 in
`appendix_domain_guards.tex`. Every one of them rendered a **wrong section number** in a sentence about
composition, coverage ordering, primitive sets or depth-8 cost.

**Why nothing caught it, stated precisely, because the reason is the lesson.** The label still resolves,
so LaTeX raises no undefined-reference warning. Round 45's rule (*resolve every rewritten `\ref` against
the `.aux`*) does not apply: **nothing was rewritten.** The references were untouched; the subsection
moved out from under them. The two references a gate pins by section were repointed inside the split edit
itself, so that gate passed. It was found by rendering page 9 as an image and reading it.

**The fix, in two parts.** All 23 repointed (`§4.2` and `§4.3` render at identical width, so the repair
was page-neutral). And a new check, `check_section_topics()` in `check_protected_claims.py`: for every
reference to either of the two split subsections it takes the enclosing sentence, scores it against a
pinned vocabulary for each subsection, and fails when the sentence's topic is the *other* one. It stands
at **27 adjudicated references, 0 mis-routed**, and it **prints the 31 further references it declines to
judge** because they carry no pinned vocabulary either way: a bounded pass should say where it stopped.
Run against a mechanically reverted copy of the source it reports **18** of the 23. The control reverts
**one** occurrence rather than all 18, so the other control lines stay legible: round 48 shipped exactly
that mistake in a new check and this one does not repeat it.

**And then the new check found a 24th, which the first version of the check could not see.** The map it
adjudicates against held only the two subsections the split *created*. But a mis-routed reference's
correct destination can be any sibling, and one of them was `§4.4`: `related_work.tex` bolded **"we audit
SCAN itself, where the ceiling is *monotone*"** and pointed the reader at `sec:structural_scale`, §4.2,
the twin, which mentions SCAN only to point *forward* to §4.4, where that sentence actually appears
(*"there the ceiling is monotone"*). The pointer was **half right**: its appendix half, `app:scan`, was
the SCAN appendix all along, which is exactly what made it read as checked. So the reader following the
paper's own citation for its external-validation claim landed one subsection short of the result the
bolded clause promises.

The fix is the one that restores coverage rather than the one that explains the miss: `§4.4` goes **into
the topic map** as a third destination, and the reference is repointed (`§4.2` → `§4.4`, identical width,
page-neutral, Figure 2, Table 1 and Table 2 all still land on p3, p4 and p5, and p3's slack is unchanged
at `+6.624`). Coverage rises to **29 adjudicated references, 0 mis-routed, 35 declined**. Building it
also produced a **false** positive worth recording, because it bounds what the check can claim: a first
draft included §4.4's rhetorical framing (*"somebody else built"*) in its vocabulary and fired on
`experiments.tex:167`, a sentence *inside* §4.4 reading **"§4.2's inversion replicates in none of 9
cells"**, where the possessive makes §4.2 the correct destination. A cross-reference sentence is
legitimately about two subsections at once; only artifact names discriminate which one a reference must
point *at*. The vocabulary was narrowed to artifact names and that sentence is now **declined**, which is
the honest verdict rather than a convenient one.

`--control` therefore fires **14**, up from 12: **one legible line per map entry**, because the two
entries are independently falsifiable and *an entry no control exercises asserts nothing.*

**Four further stale claims, found in the same pass**, all in the appendix, all attributing a number to a
body section that does not print it:

- a `0.110` said to be quoted by the body, which appears **nowhere** in the body: the appendix now says
  where that number actually lives (an unnumbered ladder, not any numbered table) and what §4.3 prints
  instead (`0.100` at `d=8`, with the strongest non-learned member named as the *variable-only* bag, both
  asserted against the stored log);
- an architecture qualifier said to be stated in the body **twice**, which is stated **once**: the
  appendix now names the one place and notes that §5 scopes the same claim by class count and algebra but
  not by architecture;
- a `+0.079` attributed to the body, which is Appendix~AK's Tree-LSTM row: the body prints the depth
  cost `+0.200` instead;
- a `+0.069` attributed to the body, which is Appendix~AH's `tab:composition_matrix_full`.

One of those four repairs was itself wrong on first attempt: our replacement text cited a numbered table
that does not contain the number. It was caught by checking the table's own line range before shipping,
which is the only reason it is not in the PDF.

---

## H. State

- **Build** `pdflatex → bibtex → pdflatex ×2`: **0** errors · **0** undefined references or citations ·
  **0** `Float too large` · exactly **2** overfull boxes, both pre-existing (`\vbox` 6.4211 pt, `\hbox`
  3.509 pt) · **99 pages**, body ends **p9**, Ethics is p10's first body line.
- **Placements asserted, not assumed**: Figure 1 p2 · Figure 2 p3 · Figure 3 p8 · Table 1 p4 · Table 2 p5.
- **Slack**: p1 `+0.561` · p2 `+0.001` · p3 `+6.624` · p4 `0.000` · **p5 `−0.695`** · p6 `−1.927` ·
  p7–p11 `0.000`. Ten of the eleven are byte-identical to the pre-round baseline; **p5 is not**; it was
  `0.000` and is where the new §4.3 heading spent its headroom. No overfull box resulted (the only two
  are the pre-existing appendix boxes), so this is not a defect, but it is stated rather than rounded to
  "unchanged": **p5 now has no headroom left**, and the next body addition that lands there will overflow.
- **Gates**: four scripts PASS. `check_protected_claims.py` 21 protected claims + 4 absences over 6+6
  files + 3 over all 16, `--control` fires **14** · `check_reviewer_map.py` 17 rows, 291 checks, 50 load
  sites, 56 appendix letters, controls inline · `check_caption_rows.py` 36 caption literals across 38
  floats, `--control` **1** · `check_figure_provenance.py` 10 figure values, `--control` **2**.
- **`verify_claims.py` 2486/2486, exit 0, in all three copies**, md5-identical
  (`5fa64467ef226550c86145934245bc85`).
- **Reproducibility**: `REPRODUCE.md` gains **R48** (the run and its stop rule) and **R49** (the census
  script), each with the exact command, wall clock, hardware, and (for R49) the three false table cells
  the census found in its own first run.
