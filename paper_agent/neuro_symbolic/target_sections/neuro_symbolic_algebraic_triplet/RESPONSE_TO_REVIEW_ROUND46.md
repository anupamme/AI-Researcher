# Response to Review: Round 46

Thank you. This review is the sixth on a sixth rubric, and it is the first to separate
*writing/presentation* (6.5) from *empirical rigor* (8.5) so sharply, with an instruction we took as
binding on the whole round:

> *"Do not add more technical detail to improve the writing score. … the rigor is obscuring the idea."*
> *"You do not need another 30 experiments."* · *"The paper needs to become simpler and sharper."*

So **this round adds no run, no claim and no assertion.** `verify_claims.py` reads **2366/2366, exit 0,
in all three copies: the same number as the version you read.** That number not moving is the check
that a presentation round stayed a presentation round; every change below is to how the paper reads.

Your own priority list is the spine of what follows: **#1 abstract · #2 introduction · #3 one-picture
audit workflow · #4 results that open with their findings · #5 one "Scope of inference" section.**

---

## Finding 1: the picture you asked for existed twice, and both copies were routed wrong

You asked for *"a one-picture audit workflow"* (#3) and, separately, for Figure 1 to be simplified so it
answers only *"what does the audit let me conclude?"* (#13). We went looking for what to draw and found
that **we had already drawn it, twice, and neither copy was reachable where you needed it:**

1. **`figure_framework.tex`** (the old Figure 1 on page 3) already contained that exact chain in its
   left column: *the claim* → *can a $P$-invariant control solve the task?* → *declare the family* →
   *measure $\sup\mathcal{F}$, readouts included* → *is the learned score above it?*, with **both**
   dead-end exits and the terminus box. Its caption read *"What a held-out score entitles you to
   conclude."* But it was welded into the same frame as a four-rung **results ladder** carrying bars and
   eight numbers, so a reader scanning page 3 saw a numbers figure and read past the workflow.
2. **`figure_procedure.tex`** (the eight-screen auditor's checklist) existed as a second workflow
   picture and the `.aux` put it on **page 16, behind the references.**

A reviewer who read all 94 pages still asked for the picture. That is not a missing figure; it is a
**consolidation and routing defect**, and it is the same class of defect as round 44's uncited float and
round 45's two appendices that did not cite each other. The fix:

- **New `figure_audit.tex` is Figure 1, and it lands on rendered page 2**: a horizontal four-box strip
  (five stages folded to four, *declare the family* merged into *measure its ceiling*), both exits
  dropping below, the terminus box across the full width. **Content-identical to what the old Figure 1
  already carried**, which is what makes it compatible with *"do not add more technical detail."*
- **`figure_framework.tex` is now Figure 2, the results ladder alone**: four rungs, every bar, every
  number, and the provenance-asserted `0.723` still in the file `check_figure_provenance.py` pins it to.
  Its caption now leads with the finding: *the twin is the one rung whose ceiling is known by proof.*
- **Figure 1's caption cites `fig:procedure`**, so the released auditor's checklist is now reached from
  **page 2** instead of being met on page 16.

**Disclosure, because this partially reverses two predecessors.** Round 15 exiled `fig:procedure` from
the body at a reviewer's request, and round 38 *consolidated* the page-2 chain **into** Figure 1 at
another's. This round undoes half of each, deliberately, and we would rather say so than revert quietly.
It is not the first time: our round-43 response reported the same collision between one reviewer's fix
and a predecessor's requirement. We are not putting an ordinal on it, because our own change log states
one for round 43 and the same one for round 45, so the count we could quote is not a count we trust.

**A geometry note, since it is the lever that made the round fit.** `\resizebox` scales by *width*, so we
built the strip with a **natural width of 16.34cm against a 13.9cm `\textwidth`**: deliberately too
wide, so the box is scaled *down* to ≈0.85 and its rendered height falls with it. That bought the ~2 body
lines that let a new page-2 float exist at all on a page with `+0.000pt` of slack.

---

## #1: the abstract (your top priority)

Measured before rewriting: **the abstract was already your four paragraphs in exactly your order**,
Problem, Method, Result, Scope. So this was a compression, not a restructure, and ¶3 was where it lived.

| | before | after |
|---|---|---|
| ¶1 problem | 61 | **56** |
| ¶2 method | 108 | **95** |
| ¶3 result | **167** | **111** |
| ¶4 scope | 96 | **59** |
| **total** | **432** | **321 (−25.7%)** |

- **Your #15: both GIN numbers are out of the abstract.** You wrote *"neither GIN number is reproducible
  on MPS … do not let the abstract depend on it,"* and you are right. The protocol finding survives in ¶2
  stated architecture-neutrally; **§4.4 keeps the entire disclosure**: the two numbers, the MPS
  irreproducibility, and the argument that the `.370` gap is `5.7×` the largest per-seed GIN drift we
  measured (`.065`).
- **Your #17: the abstract and the conclusion now carry the same three findings in the same order**,
  direction of comparison forced / *"strongest baseline"* is not an evidential principle / what survives
  is narrower than *"compositional generalization."*
- **Your #13/#17: *coverage* leaves the abstract entirely.** You asked for it to be *visibly secondary to
  S1–S3*; not naming it beside the levels is the strongest available form of that, and §3.2's own title
  still announces it.
- The three literals pinned at exactly one document-wide occurrence and living only here: the
  certificate clause, `Four of the audited`, `four primitives are not a library`: are verbatim and were
  grepped by hand as well as gated.

**One defect the render caught, and it was ours.** After rewriting §1's opening onto the AI Feynman
example (your #6), the abstract and §1 carried **the same rhetorical move with the same two numbers about
twenty rendered lines apart on page 1**: *"the better predictor, worthless … for the reason it wins."*
We had relocated the redundancy rather than removing it. The division of labour is now: **the abstract
states the verdict, §1 states the mechanism** (the bag wins *because* it is a function of the variables
alone) and what follows methodologically. Neither number moved.

---

## #2: the introduction, built on your three-term distinction

You asked for §1 to be organised around **baseline ≠ admissible control ≠ admissible ceiling.** The
distinction was real and stated: in abstract ¶2 and in `methodology.tex`'s `Terms, once.` glossary, but
**the three terms were never set side by side**, which is what you actually asked for. They now open the
section, in one sentence, on page 2:

> **Three objects, and only the third is evidence**: a *baseline* answers whether the model scored
> higher; an *admissible control*, whether something blind to $P$ could have scored that; and the
> *family-relative admissible ceiling* $\sup\mathcal{F}$ — the best score attainable by *any* such
> control, over trained readouts as well as feature maps — whether the best such thing could have.

This lands three of your asks with one edit: **#2**, the *"move the glossary much earlier"* ask (the three
core terms are promoted to their first use; *cue*, *twin*, *coverage axis* and $\phi_d$ stay in §3.2), and
**#16**, since the paper's vocabulary is now fixed at the point a reader meets it.

**#12, the *"potentially dangerous sentence."*** §1's criterion now reads *"the **best** representation in
a **declared** family $\mathcal{F}$ invariant to $P$."* We bound the family and left the connective alone:
round 44's boxed display is a **one-way implication** on purpose; a biconditional would assert the
certification the paper spends nine pages refusing, and round 45 gave the ideal-vs-declared gap its own
display in §3.3. This sentence was the last place still reading as though the *ideal* family were
measurable.

**#6, the killer example in the first 30 seconds.** §1 ¶1 now opens on it directly, with the new Figure 1
above it doing the *"boxed conceptual diagram"* half of the same ask.

---

## #4: results that open with their findings, and #12's argumentative titles

Delivered by **reordering existing sentences**, adding nothing, and (this mattered) strictly *inside*
each subsection, because `check_reviewer_map.py` requires each of 17 map Claim cells to be a verbatim
quote **in the section its own row names**, and seven of those live in §4.2 alone.

| | was | now |
|---|---|---|
| §4.1 | *Can a Held-Out-Form Score Be Solved Without Reading Structure?* | **Only One Family Carries the S1 Flaw, and S2 Is an Entitlement** |
| §4.2 | opened on corpus setup | opens **"Here the ceiling is proved, not searched for."** |
| §4.3 | *The Same Audit Outside Symbolic Mathematics* | **The Audit Ports; Our Own Inversion Does Not** |
| §4.4 | *Novelty Is Not a Scalar* (subsection) | **The Protocol Changes the Generalization Claim** |

Every new title is **shorter than the one it replaced** (62→60, 42→42, 45→44 characters): a heading that
wraps to a second line costs a body line, and pages 7–9 carry `0.000pt` of slack. §3.3 is already *"Why a
Single Invariant Baseline Is Not Enough"*: your own suggested title, and is unchanged.

---

## #5 and #14: one "Scope of inference" close, delivered **bounded**, and exactly how far

§4 now ends, immediately before §5, with a single consolidated paragraph carrying the **global** scope:
prespecification (moved out of §4's old standalone preamble, where a reader met it as a hedge before
seeing a single finding), **the equivalence class as the unit of inference**, and what a pass is and is
not. Nothing was deleted; §4's local scopings stay beside the numbers they qualify.

**We are telling you it is bounded rather than claiming ~50%.** Measured before writing it: most of §4's
hedges are pinned to the cell they qualify. **Five are `==1` literals earlier reviewers required**, and
`check_reviewer_map.py` freezes seven Claim quotes inside §4.2 alone, each of which must remain in the
subsection its row names. Hauling those into one place would undo round 45's lesson: *quote the
dispersion figure where the number is*, and would risk exactly the factual drift this apparatus exists
to catch, for a presentational gain. So what gathered here is the global scope only.

**#17, the class as the inferential unit.** Stated in **Table 2's caption**, where it also distinguishes
the two external rows honestly (*"the equivalence class on our corpora and the individual expression on
the two external ones"*: a blanket clause would have been false for AI Feynman and Lample–Charton), and
in the Scope paragraph, which carries it for all of §4 at once. That is why the two §4 tabulars did not
each grow a clause: §4 has `0.000pt` of slack on every page.

---

## #19: Table 2, and one row you named that was missing

**15 claim rows → 13**, in three blocks, on page 5.

- **Demoted to the appendix ledger** (all three already asserted in body prose, so nothing was lost):
  *under every sub-family of it* (§4.2 still says *every cell the union passes is passed by all 8191
  sub-families*), *Type-2 clones as evidence above S3* (§4.3's modality tabular), and *arrangement /
  depth / primitive* (§4.4's axes tabular).
- **Added: the shape-matched twin, as a row of its own.** You call it *"the visual centerpiece"*, and in
  the version you read the twin had **no row in the ledger of claims and verdicts**. It appeared only
  *inside another row's control cell* (`Our poly8, across protocols` · *"matched construction; twin"*),
  whose **Reported** number was the unseen-class `0.894`, so the twin's own result, `0.994` against a
  ceiling of `0.500` **by proof**, had no verdict anywhere in the table. It is now its own row: *pass; the
  ceiling is a theorem*, and the poly8 row it was buried in states its own control (`0.676`) explicitly.
- Both external blocks are kept whole, including round 43's four rows of other people's published claims.
- `\arraystretch` was left at `0.92`: the source note warning that `0.94` pushes §4.3's heading off its
  page was measured at the old row count, and re-measuring said the margin is still not there.

---

## Compression, and three honest near-misses

| | before | after | your target |
|---|---|---|---|
| abstract | 432 w | **321 w (−25.7%)** | −25–35% ✅ |
| body prose | 6228 w | **6093 w (−2.2%)** | — |
| conclusion | 161 w | **142 w (−11.8%)** | *"much shorter"*; see below |
| Related Work prose | 569 w | **532 w (−6.5%)** | **−30–40% ✗** |
| `\textbf` spans | 102 | **102** | round 45's requirement held |
| `\emph` spans | 187 | **186** | round 45's requirement held |
| parentheticals | 123 | **124** | *"reduce"*; see below |

1. **Related Work came down 6.5%, not 30–40%.** What we could cut was the prose that duplicated
   `tab:novelty`; you note the table already does the comparison work, and that ran out. What we
   *would not* cut is the two-nearest-devices contrast (*matched control* / *counterfactual evaluation*),
   which is the novelty argument you scored 7.5 on, and the untrained-encoder disqualification, which
   round 35 added here to fix a contradiction with §3.2 and which a pinned ABSENT literal now guards.
2. **Parentheticals are flat, and we think the ask was mis-measured: by us.** Our plan carried a target
   of *"102 → ~70"*; on inspection **102 was round 45's *bold* count**, not a parenthetical count. The
   real census is 124, and it splits: **66 are cross-references or citations** (dropping one is a routing
   regression, which is the defect this round exists to fix), and of the remaining 58, all but about a
   dozen are **inline mathematics**, `(h)`, `(g)`, `(x{+}y)`, or the `(i)/(ii)/(iii)` enumerators in
   Theorem 1. The dozen left each carry a value (`chance 0.5`, `0.843 to 0.894`) or a definition
   (`whole subtrees, children in order`). We would rather report that than manufacture cuts that lose
   content.
3. **The conclusion is 142 words, not shorter still.** It was merged into one paragraph and lost three
   spans, and it now closes on the recipe line: *name the property, declare the invariant family, test
   each member per instance, estimate its ceiling, report the margin.* Cutting further would take out one
   of the three numbered findings that mirror the abstract, which is your #17.

**We proved the compression removed no content**, rather than asserting it: a markup-stripped,
comment-stripped, sentence-level diff of the six body files against the pre-round snapshot flags 68
changed spans and 67 new ones, and exactly **one** lost content outright, the word *propositional*, a
precision about `xie2019embedding`'s subject matter. **It has been restored.**

---

## What we declined, and why

| your point | our answer |
|---|---|
| **§10's seven-section reorganisation** | **Declined.** Rounds 43–45 converged on this structure; a full re-sectioning would re-point ~50 cross-references and put all 17 map Claim quotes at risk of leaving the sections their rows name: factual-drift risk taken for a presentational gain, which is the failure mode this paper's apparatus exists to prevent. Its *effect* is delivered by the new Figure 1, the three argumentative titles and the Scope close. |
| **§21 blocker 3: one more clean positive benchmark with a nontrivial `F3` ceiling** | **Declined this round, named as future work.** You also wrote *"you do not need another 30 experiments"* and *"the paper needs to become simpler."* Adding a benchmark in the round whose brief is compression would trade the score you asked us to raise for one you did not. |
| **§22: reposition as a framework paper with three case studies** | **Adopted as framing, refused as a restructure.** At nine pages, "framework paper" *is* the new Figure 1 on page 2, the three-term ladder, and section titles that state findings. |
| **§16: do not strengthen the composition claim** | Complied. No wording in §4.2 or §5 got stronger; #4 only reordered. |
| **§9: do not oversell Theorem 1 / Prop 1** | Already pre-conceded twice: `methodology.tex` bills the numbered results *"as scoping, not as theoretical contributions"* (a pinned `==1` literal), and Appendix AN says a reader who finds Theorem 1 close to a restatement *"is not disagreeing with us."* Your positioning (the theorem formalises the boundary, the contribution is making it measurable) is what §3.3's display already says, and §1 says *every part of its distance from "use an invariant control" is **measured***. Stated in our own voice: **eleventh consecutive round we have declined to paste a reviewer's sentence into the paper.** |
| **§10: S1–S3 are researcher-defined** | You call this largely mitigated; the evidence is `≤ +0.038` by hand over 8191 sub-families, `+0.181` clear under adversarial search, and round 45's table re-scoring that search's frozen winner on four partitions it never saw (`+0.16` to `+0.27`). |
| **§14: 94 pages** | The body is **nine pages and self-contained**. The appendix is the audit trail; round 42's reading path and round 44's five-object critical path route it, and round 43's reviewer moved the published-numbers ledger *into* the body. |
| **§23: keep the title** | Agreed, unchanged. |

---

## Build state

`pdflatex → bibtex → pdflatex ×2`: **0 errors · 0 undefined references · 0 floats too large · exactly 2
overfull boxes, both pre-existing · 94 pages · body ends page 9**, with the Ethics Statement the first
body line of page 10.

Float placement, re-baselined because this round renumbered every figure and each was resolved against
the `.aux`: **Figure 1 (`fig:audit`) p2 · Figure 2 (the ladder) p3 · Figure 3 (`fig:novelty_cost`) p8 ·
Table 1 (`tab:novelty`) p4 · Table 2 (`tab:entitlements`) p5 · Figure 4 p15 · Figure 5 (`fig:procedure`)
p16, now cited from page 2.**

**§4.3's heading is on page 9.** That boundary is bistable and has two legal states; round 45 landed on
p8 and this round lands on p9. We name it rather than let a future round discover it as drift.

All four gate scripts **PASS** with every positive control firing (`check_protected_claims.py --control`
= 6 FAILs; `check_figure_provenance.py --control` = 2; `check_caption_rows.py --control` = 1;
`check_reviewer_map.py` runs its two controls inline in every invocation, 17 rows / 286 checks).
`figure_audit.tex` was added to the protected-claims float list: a hardcoded float list rots silently,
which is what that script's check 6 exists to catch.

**`verify_claims.py`: 2366/2366, exit 0, in all three copies; unchanged from the version you read.**
