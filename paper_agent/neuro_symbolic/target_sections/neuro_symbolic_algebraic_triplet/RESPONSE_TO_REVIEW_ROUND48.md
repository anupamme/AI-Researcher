# Response to Review: Round 48

Thank you. This is the eighth review on an eighth rubric, and it is the second in a row to leave
correctness alone and name one remaining axis:

> §1: *"The main remaining risk is whether reviewers view the central methodological contribution as
> sufficiently novel and general for ICLR, rather than as a carefully systematized version of an already
> familiar principle… That is now the key battle."*
> §17.1: *"Make the novelty of admissibility unmistakable. This is the biggest one."*
> §17, closing: *"the final push should not be another 20 experiments."*

**Two things stated before anything else, because both go against the grain of that advice.**

**First, this round adds a run.** You asked for no more experiments and so did round 47
(*"I would not add another encoder, another symbolic dataset, another 20 baselines, another 50 seeds"*).
We mapped your §17.2's seven requested conditions against what already runs and **six of the seven
already existed**, with run tags. The seventh (**unseen TRIPLE**) did not, and the paper's own
appendix already disclosed the gap in its own words (`appendix_domain_guards.tex`, disclosure (iii)):
*"Three bigrams, not twelve. The arrangement result rests on the three most frequent adjacent pairs… it
is not a sweep of all ordered pairs, and all three involve `commute`."* So one run was added, `r102`,
pre-registered in writing before training started, on the paired class set, closing both halves of that
disclosure. No new dataset, no new encoder, no new architecture. It is reported in §B below, including
which pre-registered branch fired, **and it fired against its own label**, which is the part of §B we
would rather not have had to write. **`verify_claims.py` therefore goes 2398 → 2438 assertions**, all
three shipped copies byte-identical, exit 0. Rounds 44 and 46 both used the count *holding still* as
evidence that a presentation round stayed one; the converse obligation is that when a round adds a run,
the count has to rise and the first paragraph has to say so. The 40 new assertions are the 39 numbers
Appendix BC's Table 37 prints, its construction and certification properties, and (deliberately pinned
**together**) the fired branch, the magnitude that contradicts its label, the statistic's grid step, and
the larger number §4.4 calls *free*, so those four cannot silently drift apart.

**Second, the biggest finding this round is that the object your §15 asks us to build is already in the
paper, and we had it on a list of sections to DELETE.** Your §11 asks us to cut ~30–40%; the approved
plan for this round named three uncited appendix sections to cut. One of them, **Appendix U**, turned out
to be tag `r69`, the sweep that re-scores *every* protocol under which this paper reports an
identification number against all three bag representations *and* an untrained encoder under that same
protocol, n=25 seeds, and it opens:

> *"Four times in this revision, supplying a non-learned baseline we had not measured reversed a
> conclusion we had drawn."*

That sentence is the empirical answer to your §6's *"can look partially definitional"*: a definitional
criterion cannot reverse four of your own conclusions. Its table then shows **our own trained encoder at
or below a zero-parameter variable-token bag on three of six protocols**. It was referenced **nowhere in
94 pages** (not by `\ref`, not by a hand-typed letter), which is exactly why a page census could put it
on a cut list. **It is now cited from page 6, in the lead-in to the table your §15 asked for, and it was
not cut.**

---

## Findings

### Finding 1: §15's table exists, in §3.3, and this is the *second* reviewer to miss it for a cause our own source recorded

Your §15 hands over an eight-row *"Existing idea | This paper"* table. `methodology.tex` already carried
six of those rows as a tabular in §3.3, in your own left/right form. It was missed because it has **no
caption, no float number and no list-of-tables entry**, and we know that is the cause because
**round 40's source comment says so**, about a *different* reviewer:

> *"The table below already carried SIX of the seven rows he asked for, and he missed it and credited
> `Table~\ref{tab:novelty}` on page 4 instead — because it has no caption, no float number and no
> list-of-tables entry… Kept inline deliberately: a caption is ~3 lines and a float here lands on the
> bistable §4.3 boundary above."*

Round 40 diagnosed it, declined the fix for a measured page reason, and did not route around it. Two
reviewers have now independently failed to find the object. **A diagnosed-but-unfixed routing defect is
rediscovered.** Fixed as routing, in four places, at zero page cost:

| what changed | where |
|---|---|
| §1's critical path: **five objects → six**, Table 1 added with a gloss no other entry gives | `introduction.tex` |
| the appendix front matter's mirror: *"Five objects carry the argument"* → **Six** | `appendix_domain_guards.tex` |
| §3.3's critical-path gloss: *"why one invariant baseline is not enough"* → the practice ⇒ requirement contrast | both lists |
| **§3.3's own title**: *"Why a Single Invariant Baseline Is Not Enough"* → **"A Baseline's Strength Bounds Nothing; the Family's Ceiling Does"** | `methodology.tex` |

The last of those was found only on the render and was not in the plan: **the section's own title was the
caveat the gloss was copying**; the last "why X is not enough" heading in the body, in the section your
§17.1 calls the biggest ask. The lead-in was also restating `abstract.tex` three pages earlier, so it now
names what the object *is* instead. **Fourteenth consecutive round in which we have declined to paste a
reviewer's wording**; the rows are ours, and they were already there.

### Finding 2: Table 1 was missing exactly the axis your §6 uses to rescue the novelty claim

Your §6 concedes the obvious version (*"A P-blind baseline cannot prove P — that's too obvious"*) and
locates the novelty in a conjunction of seven items. Checked one by one against `tab:novelty`'s six
columns, items 1, 2 and 5 **were** columns. Item **3 (trained readouts included in the ceiling) had no
column at all**, though it is **Proposition 1** (p6) and it is measured: the bound over every readout is
`0.296`, against the best declared member's `0.276`.

**Table 1 now has a seventh column, `readout closure?`**, set **bold**, so it is one of *three* bold
columns, the ones that test blindness rather than describe a device. A column is a *width* edit where a
row is *height*, which is why this was affordable on a page carrying `0.000pt` of vertical slack; measured
after, with p4 read at 320 dpi for collisions.

Two details that are the honest part of it:

- Every prior device is `×` in the new column **except `learned invariant control`, scored `partly`**:
  the `r100` arm does train a comparator, it just does not bound over the class of them. Scoring it `×`
  would have made the column unanimous and the table self-flattering.
- The caption carries two counts that both had to move: *"`×` in all **six**"* → **seven**, and *"the
  **two** bold columns"* → **three**. It cost **4 rendered characters**, not a clause, only because round
  47 had already made the caption *point at* the bold headers instead of transcribing them.

Your §6's item 4, **non-monotonicity**, deliberately gets no column: it is a property of the ceiling
(**Corollary 2**, p6: *"a family is not audited by its strongest member"*), not of a prior device, so
there is no cell to tick.

This was also a **correctness** fix, not an addition: `methodology.tex` claimed Table 1 *"runs the first
five [rows of §3.3] across eight prior devices"*, and before the new column that was true of **four**.
The same gap existed in two independent representations of the same argument.

### Finding 3: the section on the cut list was the significance evidence (and only one of the three candidates was even unreachable)

The plan's premise was that Q, U and V carry no `\applabel`, *"so nothing in 94 pages can `\ref` them."*
That was true of `\ref` and **false of reachability**, because appendix letters here are hand-typed:

| candidate | referenced from | verdict |
|---|---|---|
| **Q** *(Domain Guards and Sampling)* | `methodology.tex:72`, hand-typed, **rendered on p4: the body** | cutting it breaks a page-4 sentence |
| **V** *(the score₅ leaderboard floor)* | `appendix_domain_guards.tex:1041`, from Appendix T | reachable |
| **U** *(Every Claim Against Its Strongest Skyline)* | **nothing, anywhere** | the `r69` sweep; see above |

So the cut was **declined**, and the reasons are measurable rather than rhetorical:

- **The three candidates are ~1.5 pages of 94**: Q is 7 source lines, V is 5, U is 34; Q renders inside
  p41 and U and V share p44 with their neighbours. Against a 30–40% ask, that is **1.6%**.
- **Cutting even U alone re-letters ~30 sections**, across 54 `\subsection*{<L>. …}` titles, 37
  `\applabel{<L>}` arguments and 50 hand-typed `Appendix~<L>` prose references in five files.
- **The residual risk is undetectable by any mechanical check**: a hand-typed letter that names a real
  but *wrong* section. Round 33 shipped two of those in a *smaller* re-lettering.

We would rather state that bound than perform a cut whose only measurable effect is risk. See §C for the
full page census.

### Finding 4: writing the gate for Finding 3 found a live wrong-target citation

`check_appendix_letters()` already asserted the printed letter sequence is contiguous A…BB, that each
`\applabel{L}` sits under a section titled `L.`, and that every hand-typed `Appendix~<L>` names a defined
section. Its docstring already stated plainly what it **cannot** see: *a hand-typed letter that names a
real section which is the wrong one.*

Finding 3 needed one clause it did not have, **which appendix sections nothing in the document routes a
reader to**, and the first run of that clause flagged `AF`. Appendix AF is *"The AI Feynman Case Study, Full Controls"*, and its
first sentence is:

> *"§4.1 states the AI Feynman result in one paragraph because it is a case study of the audit, not a
> finding about the field. **The controls behind it are here.**"*

**AF points at §4.1; §4.1 cited `AG`**: *"Auditing EQNET Under Its Own Splits"*, one letter away, the
signature of a past re-lettering. So the exact failure the docstring says no check can see was **live in
the shipped paper**, and an *orphan* check caught it as a side effect. §4.1 now cites AF (AG is kept: it
is the reviewer map's row 1 and the survey spans EQNET corpora too).

The first cut of that clause was **too strict** and reported seven orphans; four of them (G, M, N, R)
hold a table or a `\S`-label that *is* `\ref`'d, so a reader is routed onto those pages. Reachability is
now computed per **section span**, not per `\applabel`. Two sections, **J and L**, remain genuinely
unreferenced; both are robustness sweeps no claim rests on, both were read before being left, and both
are **declared in the check** rather than passing silently.

### Finding 5: §17.3's first named cut target is not in the paper

Your §11 names *"revision history, multiple superseded experiments."* Both are **section titles**:
`F. Reproducibility Details and Revision History` and `T. The Superseded score_5 Comparison, and Why It
Was Wrong`. F's title contradicts the front matter three pages earlier — *"The developmental chronology…
is **not here**: it ships as `REVISION_HISTORY.md`"* — which exists, 149 lines, byte-identical in all
three copies. **The impression came from two words in a heading.** F is retitled
**"What the Audit Changed: the Ledger, and the Defect Log"**, at zero pages, and the front matter's
band-(i) gloss now leads on the ledger instead of on provenance.

### Finding 6: a sentence counted five axes and cited a figure that draws three

Your §17.2 asks for the composition axes to be separated, and §4.4 already separates them: *"'out-of-
distribution' names **five separable axes**, free to fatal"* over a five-row table. But the citation on
that sentence is `Figure~\ref{fig:novelty_cost}`, **whose lower panel draws three bars**, not five:
arrangement, depth, primitive. The figure's own caption explains why: *"Below: paired drops at `d=8`"*, and
schema and inventory are not paired at `d=8`, but the `\ref` was attached to the word **five**.

Same class as round 47's *"three modalities"* against an all-symbolic table, and invisible to all four
gates, which read numbers and labels but not the arithmetic between a count and the object it cites. The
sentence now reads *"… names five separable axes, free to fatal; **the three paired at `d=8` are
drawn**"*: the count and the citation now describe different things, correctly.

### Finding 7: the round's own new comment block cited two theorems that do not exist

Found on the last pass, by hand, and it is the most uncomfortable one because it is **ours, written this
round, in the very comment block justifying Finding 2's new column.** That block cites the two results the
argument rests on as `Prop.~\ref{prop:readout_closure}` and `Cor.~\ref{cor:nonmonotone}`. **Neither label
exists.** The real ones are `prop:ceiling`: **Proposition 1**, p6 (and `cor:supremum`) **Corollary 2**,
p6. An earlier draft of *this response* repeated both errors before they were resolved against the `.aux`.

**Nothing in the project could have caught it, and the reason is structural.** LaTeX never expands a `\ref`
inside a `%`-comment, so no undefined-reference warning can fire and the build stays at 0 undefined. And
every check in the gate scripts **strips comments before reading**, deliberately, so that commented-out
prose cannot fake a pass (round 47 found the mirror-image bug: a gate reading a `%`-comment *as* body
text). So the comment stream (which is where this project keeps its design record, its measured page
costs, and its standing do-not-touch warnings) was **the one part of the source with no reader at all.**

That is worse than a typo. The comment is what the *next* round reads: it believes the number and prints
it. Which is precisely what nearly happened here, in this document.

New `check_comment_refs()`: a comment may say anything, but a `\ref` in it must name a label that exists.
It reads **60** such refs across the 16 files and all 60 now resolve. Its positive control injects the two
original wordings into `related_work.tex` alone and fires exactly 2: a first cut injected into all 16
files, fired 32 near-identical lines, and took `--control` from 10 to 42, burying the other nine checks'
controls. A control has to be legible to be a control.

---

## B. The run you asked us not to add, and why this one condition

Your §17.2's seven conditions against what already ran before this round:

| §17.2 asks for | already run |
|---|---|
| unseen primitive | `r89` leave-one-primitive-out; `r93` branch (2) at depth 8 |
| unseen **pair** | `r93` branch (3), leave-one-bigram-out: `+0.015 / +0.011 / +0.010`, **all intervals cover zero**, but on the *adjacency* reading only; `r102` adds the co-occurrence reading |
| unseen **triple** | **nothing, on either reading** ← the one gap |
| unseen depth | `r93` branch (1), train depth ∈ {1,2,4,8} × test depth 1–8 |
| unseen ordering | `r94`, all 24 orders |
| different algebra | `r83` oneVarPoly13, `r84` boolean8 |
| unrelated rewrite families | `r88` schema-transfer matrix; leave-one-composition-family-out |

Your §5 states the hypothesis `r102` tests, so we quote it as the null: *"the difficult part appears to be
acquiring the primitive invariances, not learning a general compositional operator over arbitrary
transformations."*

**The design changed once, before training, and the reason is worth reporting because it is a defect we
found in our own plan.** Our first design read *pair* and *triple* the way our existing `r93` does, as a
withheld **adjacency**: chains that never place `q` immediately after `p`. Written out, that reading is
**degenerate by construction**: fewer depth-8 orders contain a given trigram than contain a given bigram,
so `cost(triple) ≤ cost(pair)` would have held whatever the encoder did, and the experiment would have
measured **the size of a combinatorial set rather than a capability**. It is also the wrong reading of your
list, which names *depth* and *ordering* as their own separate conditions. The reading that actually
escalates is **co-occurrence**:

| level | withheld | what is still trained | test form |
|---|---|---|---|
| order 1 | a primitive | — | `r89`, already run |
| **order 2** | a pair `{p,q}` | both alone, and each composed with *other* primitives | depth-2 composite of `p,q` |
| **order 3** | a triple `{p,q,r}` | **all six** of its pairs, as pair composites | depth-3 composite of `p,q,r` |

That is a **lattice**, not a list: each level withholds exactly one node of the level above while holding
every node below it. *"Learned a general compositional operator"* and *"learned pairwise composition and
stopped"* make **different predictions at order 3**, and nothing in the paper separated them. **Arrangement
is deliberately held fixed** (within a class, a type's training composite and its test form use the same
drawn order), because arrangement is `r93`'s and `r94`'s axis and is not re-manipulated here.

**Eight trainings per seed × 5 seeds = 40**, one encoder scored on all five test sets (`r89`'s trick), so
two further contrasts come free:

- `covered_pair` (order-2 library, 10 forms) · 3 × `nopair_<P>` · `covered_triple` (order-3, 14 forms) ·
  2 × `notriple_<T>` · **`size_control`**, which matches `covered_triple` in form count *and* total token
  delta while training **no three-way co-occurrence**: a stronger unseen-triple contrast than
  `notriple_<T>`, which still trains the other three triples.
- **Matching is searched, not padded:** every arm at a level holds the same form count and the same total
  token delta as that level's covered arm, the replacement chain being *searched* for that exact delta;
  both arms are scored on the **byte-identical** test form. So a cost cannot be a difference in how much
  data, how many tokens, or which form was scored.
- **The withheld types close disclosure (iii) explicitly:** two of the three pairs and one of the two
  triples **contain no `commute`**, and the two triples differ by exactly one substitution (`commute` for
  `double_negate`), so the pair of triples is itself a controlled contrast.
- **No shape-matched twin, deliberately.** `r93` runs one because it makes absolute-accuracy claims on a
  single arm. Every headline number here is a *paired difference between two arms on the same form*, so
  length, operator multiset and tree-local shape difference out exactly. Building one would have cost
  roughly a quarter of the corpus (`r93` dropped 58 of 305 scanned classes on that guard alone) for a
  guard this contrast does not need. The zero-parameter bag ladder still runs, because the covered arms'
  absolute accuracies are reported.
- **Certification, because construction is not entitlement.** Building a form by applying `p` then `q`
  does not establish that both are *required* to reach it: `commute` has token delta 0. So every test
  form goes through a route search carrying the primitive set used along each route, and the class is
  **rejected** if any route within the test's own depth reaches it without the withheld co-occurrence. The
  search is one-sided by construction (a route found really exists; absence is reported as unverified,
  never as proof), it is seeded differently from construction so it is a second opinion, and its **power
  is logged**: it reached `926/1000` test forms, with a positive control firing on `923/1000`.

**Four branches were pre-registered in the script's own docstring before training started, and the script
selects among them in code from the numbers**; it is not a judgment we make after reading them. They are
emitted into the run's JSON under `preregistered_branches`, so the artifact carries them:

1. **both intervals cover zero** → co-occurrence novelty is free at orders 2 and 3; your §5 hypothesis is
   refuted in the direction that favours the paper.
2. **`pair` covers zero, `triple` excludes it and exceeds it** → the operator is **pairwise-local**. *This
   is a finding against the paper's present framing and confirms your §5.* §4.4's arrangement row is
   re-scoped, §4.2's composition claim narrowed, and Figure 3's bar and its provenance pin move with it.
3. **`pair` excludes zero** → co-occurrence costs even at order 2; both readings printed side by side, and
   nothing in `r93` is withdrawn, because `r93` never claimed the co-occurrence version.
4. **both exclude zero, `triple` ≤ `pair`** → costed but not escalating.

A **confound test** was also fixed in advance: the branch is reported CONFOUNDED if `library_size_effect`
(`size_control` − `covered_pair` on the pair tests) has an interval excluding zero *and* a magnitude at
least half the reported `triple` cost, the one way a cross-level comparison can fail. Note the direction
of any residual: order 3 trains *more* composition than order 2, which if anything makes an unseen-triple
cost look **smaller**, i.e. it works against branch (2) rather than for it.

**Construction, already measured and logged** (this is the `--build_only` feasibility gate the design
needed, and it passed before any training): **200 classes usable in every arm and certified at every
test**, from 209 scanned; the only drop reason was `test_forms` (9); **0 coincidences in the leak check
over 8 arms**; and *"every withholding, matching and level assertion passed."*

### What it found, and the part we would rather not have to report

**40 trainings, 5 seeds × 8 arms, 10702.9 s ≈ 3.0 h. Appendix BC, Table 37, pp94–96.** Every cost below is
a **paired per-class difference between two arms scored on the byte-identical test form**, `n=200`, 95% CI:

| withheld | cost | 95% CI | resolves? |
|---|---|---|---|
| **pair** `commute+double_negate` | **`+0.010`** | **`[+0.001,+0.021]`** | **yes** |
| pair `add_identity+mul_identity` | `-0.002` | `[-0.006,+0.000]` | no |
| pair `add_identity+double_negate` | `+0.000` | `[-0.003,+0.003]` | no |
| **triple** `add_identity+commute+mul_identity` | `-0.002` | `[-0.005,+0.000]` | no |
| **triple** `add_identity+double_negate+mul_identity` | `-0.001` | `[-0.005,+0.002]` | no |
| *no three-way training at all* (`size_control`), on `a+c+m` | `+0.000` | `[-0.003,+0.003]` | no |
| *no three-way training at all* (`size_control`), on `a+n+m` | `-0.002` | `[-0.005,+0.000]` | no |

Mean unseen-pair cost **`+0.0027`**, mean unseen-triple cost **`-0.0015`**. The confound test did **not**
fire: no `library_size_effect` interval clears zero and its largest magnitude is `0.005`, so
`confounded_by_library_size` is `false` in the log.

**The pre-registered rule selected branch (3), and its LABEL is wrong. We are reporting that rather than
repairing it, because the defect is in our pre-registration and not in the numbers.** Branch (3) reads
*"co-occurrence costs even at order 2"*, and it fired for one reason only: one of five intervals excludes
zero. Three things about that one interval, all of which we would have caught had we written a smallest
effect size of interest into the predicate:

1. It clears zero by **`+0.001`, which is exactly one step of the statistic's grid.** Five seeds of binary
   correctness per class averaged over `K=200` classes means a paired class-mean gap **cannot take a value
   between `0` and `0.001`**. A rule keyed on *"the interval excludes zero"* is, at this resolution,
   deciding on one representable step.
2. Its magnitude, `+0.010`, is **smaller than the `+0.012` that §4.4's own axis table prints in the row it
   labels *free*.** So the branch label says *costs* where the paper's own vocabulary, applied to a larger
   number, says *free*. That is not a coincidence to be argued away; it is the vocabulary and the
   pre-registration disagreeing, and the appendix says so in print.
3. **It is a locus on a primitive, not an escalation with order.** It is the only withheld pair containing
   `commute`: the delta-0 primitive that disclosure (iii) already flagged. **Both `commute`-free
   withholdings cost nothing**, at both orders.

So on the substance: **your §5 hypothesis is not refuted, and it is not confirmed either.** Nothing at
order 3 resolves; **both** triple point estimates are *negative*; and the strongest contrast we built (
`size_control`, which trains **no three distinct primitives together at all**, matched to `covered_triple`
in form count *and* total token delta) also resolves nothing. What did resolve is at order 2 and sits on
one primitive. The honest reading is the one the appendix prints: **this design bounds a composition cost
and cannot resolve one.**

**And here is the limit that bounds every sentence above, stated before you have to find it.** All **40**
arm × test cells score between **`0.985` and `1.000`**. The arm that never saw `a+c+m` reads **`1.0000` on
all five test sets in all five seeds.** At that ceiling a null result is *"we could not resolve a cost
against a saturated arm"*, not *"there is no cost."* Two things keep the split from being trivial by the
paper's own instrument: the strongest of 14 zero-parameter bags reaches **`0.115`–`0.260`** and an
untrained encoder of the same architecture reaches **`0.257`–`0.337`**, both against chance `0.005`, so
the ceiling is a property of the *trained* encoder here, and it is an arm the audit admits and the
encoder clears.

**What does not move.** Figure 3's arrangement bar and `check_figure_provenance.py`'s pin are unchanged:
branch (2) did not fire, so §4.4's `arrangement` row is not re-scoped and §4.2's composition claim is not
narrowed. §1's count of **four** failed pre-registered predictions is also unchanged:
`check_preregistration_failures()`'s docstring already excludes multi-branch decision rules from that
count, so a branch selecting itself is not a fifth failed prediction.

**Two process notes, because they are the kind of thing that is easier to omit.**

- **Our own caption gate caught a defect in this table, and following it changed the argument for the
  better.** Every cell was first written to four decimals. `check_caption_rows.py` FAILed; it matches
  three-decimal literals, so it read the tabular as having **zero** cell values and reported the caption's
  own `0.005` as absent. The available fixes were an `ALLOW` entry (gate passes, float becomes permanently
  unverifiable: round 47's trap of a gate passing for the wrong reason) or printing the grid's own
  precision. We did the second: on a `0.001` grid the fourth digit is `0` **by construction in every
  cell**, so it was precision that cannot exist. It also makes point 1 above visible *in the table*:
  `+0.001` as a CI bound against a grid of `0.001` is one step on its face. The two prose means stay at
  four decimals, because they average three and two on-grid values and are legitimately off-grid.
- **The page count rose, and we are not netting it out against §C.** 94 → **96 pages**: Appendix BC is
  three pages in band (iii), the band your §11 wants cut. §C's census is stated against the new number.

`REPRODUCE.md` indexes it as **R47** with a one-command recipe. (Not R46: R46 was taken last round by
`r31_hardened_recipe`, and a *next free* index is not the item count; `check_reproduce_index()`'s pin is
the count, **78**.)

---

## C. The length answer: the census, and the bound

Measured on this build, **96 pages; up from 94, and §B is why**:

| span | pages | what it is |
|---|---|---|
| pp1–9 | **9** | the body: §1 through §5 |
| p10 | 1 | Ethics and Reproducibility statements |
| pp11–13 | 3 | references |
| p14 | 1 | appendix divider |
| pp15–32, band (i) A–K | **18** | provenance and the audit trail (2 of the 18 are full-page figures) |
| pp33–49, band (ii) L–Z | **17** | protocol specifications |
| pp50–96, band (iii) AA–**BC** | **47** | one self-contained section per run tag (AN, the proofs, is 3 of those; **BC, pp94–96, is `r102`**) |
| **appendix total, pp15–96** | **82** | |

**The bound, stated plainly: ~1.5 pages of the 82 are unreferenced, and a 30–40% cut has to come out of
band (iii)**; the 47 pages this same review scores 7/10 under Reproducibility and calls, in its §2, the
biggest improvement over earlier versions. We are not willing to trade that for a page count, and
`r102` **adds three pages to that band**. Netting that out against the pass below would have let the
census read as a cut when the appendix grew, so: **the appendix is two pages longer than the version you
reviewed, and the growth is in the band you asked us to cut.**

**We also did not take the cut the approved plan listed.** Three sections (Q, U, V) were on it as
uncited. **All three are cited in prose**; what they lacked was an `\applabel`, so nothing could `\ref`
them, which is a reachability property and not a citation one, and a census that conflates the two
produces a cut list of live sections (Finding 3: one of the three was the answer to your §6). Cutting
them would also have **re-lettered every section after V**: ~30 hand-typed `Appendix~<L>` prose refs
across three unreconciled registries, and round 33 shipped two false letters that way. The letter is
typed, not counted, so the residual failure mode is a hand-typed letter naming a real but *wrong*
section, which **no check here can see**. The reason is recorded in
`check_protected_claims.py`'s `check_appendix_letters()` docstring rather than in a commit message, and
that check is new this round.

The bounded pass we did take: **F retitled** (Finding 5), the front matter re-routed, **U and AF made
reachable** (Findings 3 and 4), and the census above printed rather than asserted.

---

## D. Two claim-hygiene items

**§10: the ordering claim is now sourced in the body.** You warn against publishing the GIN/Transformer
ordering, and the number your §4 quotes to assemble that ranking (`0.669`) is **appendix-only**: the
abstract has carried no GIN number since round 46. The body's one architectural clause was
*"of the three, only the Tree-LSTM clears both"*: **true, but its basis was in Appendix AO**. GIN's
failure was already printed two sentences above (`.511±.026` against chance `.500`), so the only basis a
reader could not see was the Transformer's interval. It is now in the body:
*"the Transformer's `[.588,.746]` misses `.596`"*, and *"of the three"* is gone, which also de-ranks the
clause you warn about. Both printed numbers were **already asserted at the digits they print**
(`verify_claims.py` pins `[0.588, 0.746]` at `tol=0` and the bound at `0.596`), so the body caught up to
the verifier rather than the other way round.

That clause cost ~46 rendered characters on a page with `0.000pt` of slack, and **widow control then
moved two lines of §5 onto p10**, so Ethics stopped being p10's first body line. It is paid back inside
the same paragraph by six restatements with nothing dropped. One attempted funding edit elsewhere was
**reverted**: it compressed a sentence that `check_reviewer_map.py` pins verbatim *and* to its section,
so the gate failed twice on an edit that changed no meaning.

**§13; no edit, and here is the grep.** `causal determinant` / `causally` appear **nowhere in the whole
`.tex` tree, zero hits**. The paper already states the coverage effect as your preferred intervention
framing: *"inventory: library membership | `.965/.880 → .832/.662` | plain/renamed; held-out tree
**byte-identical**."*

**§14: the framing is already deflationary; the count stays.** Three places, in print before you asked:
*"the audit ports to language and to code, where **our own** inversion fails to replicate"*; *"language
and code two **ports** of the same code"*; *"**portability, not general validation**, never prevalence."*
Your proposed sentence is weaker than what is there. The one clause that reads as ambition is §1's
*"revise ten claims across three modalities"*: a **count**, made true and gated last round by
`check_ledger_modalities()` after round 47 found it false of the table it cites. **Round 47 required the
two non-symbolic ledger rows that make it true.** This is the ninth consecutive round with a live
conflict between reviewers, and as in the previous eight we are resolving it here rather than by deleting
a predecessor's requirement.

---

## E. Answered without an edit

| your point | the answer |
|---|---|
| **§12, claim hierarchy**: *"I would preserve almost exactly"* | untouched, and named as untouched. |
| **§8, non-monotonicity**: *"arguably the most elegant conceptual contribution"* | **Corollary 2** (p6) and **Appendix AC** (p51). It is why Finding 2 adds a **column** and not a row: non-monotonicity is a property of the ceiling, not of a prior device, so it has no cell in a per-device table. |
| **§6, "partially definitional"** | Pre-conceded in the paper's own words; the numbered results are billed *"as scoping, not as theoretical contributions"*, a pinned `==1` literal, and answered twice structurally: Finding 2's new column is **proved**, not definitional, and Finding 3's Appendix U is the **track record** of the criterion reversing our own conclusions. |

---

## Verification

- **Build:** `pdflatex → bibtex → pdflatex ×2`. **96 pages · 0 errors · 0 undefined references or
  citations · 0 `Float too large` · exactly 2 overfull boxes, both pre-existing** (`6.4211pt` vbox,
  `3.509pt` hbox). 94 → 96 is Appendix BC; **no body page moved.**
- **Placement, asserted not assumed:** Figure 1 p2 · Figure 2 p3 · Figure 3 p8 · Table 1 p4 · Table 2 p5
  · §4.3 p8 · §4.4 p9 · §5 p9 · **Ethics the first body line of p10**. Every one identical to the
  pre-round baseline.
- **Slack, in points:** p1 `+0.561` · p2 `+0.001` · p3 `+6.624` · p4–p5 `0.000` · p6 `−1.927` · p7–p11
  `0.000`. **Byte-identical to the pre-round baseline**: every edit this round was width, not height.
- **Four gate scripts PASS**, every positive control firing: `check_protected_claims.py` (**`--control`
  fires 12**, up from 7 last round (the letter checks contribute 3, of which the new reachability clause
  is 1, and `check_comment_refs()` contributes 2) ·
  `check_reviewer_map.py` (17 rows, **288** checks, **47** literal `load_log()` sites, **55** appendix
  letters; controls inline) · `check_caption_rows.py` (control = 1 FAIL; census re-baselined to **36
  caption literals across 37 floats, 19 via a declared allowance**) Table 37 is checked against its own
  cells, **not** via an allowance) · `check_figure_provenance.py` (control = 2 FAILs).
- **`verify_claims.py` exit 0 at 2438/2438** in all three md5-identical copies
  (`c912b2c50dd18a386d470525c75bb809`). `check_reproduce_index()`'s load-stem pin re-baselined
  **77 → 78** at `tol=0`; `REPRODUCE.md` md5-identical across the three copies.
- **`r102`'s log shipped with the home path redacted**, including the one **nested** key that carried it
  (`provenance.args.log_dir` → `<redacted-for-anonymity>`); both artifact copies md5-identical, and an
  overwrite guard was asserted before the sync because `--tag` names the `.json` *and* the `.log` the
  verifier reads.
- **No content was lost** in the compressions: a markup- and comment-stripped sentence-level diff of the
  six body files against the pre-round snapshot shows `abstract.tex` and `conclusion.tex`
  **byte-identical**, and `experiments.tex`, `introduction.tex` and `related_work.tex` unchanged in
  sentence count (37 → 37, 12 → 12, 8 → 8 under this splitter). `methodology.tex` is the only file that
  loses one (47 → 46), and that is the merge described above: two sentences of restated abstract replaced
  by one that names the object. **Absolute sentence counts depend on the splitter**: an earlier pass over
  the same two files with a finer one reported 54 → 54 and 68 → 67, so what is being asserted is the
  **delta**, one merge and nothing else, not the totals.
- **Pages read as images**, not only as text: **p4 at 320 dpi** for the new column (a cell collision is
  invisible to `pdftotext` and to all four gates), **p95 at 300 dpi** for Table 37 after the precision
  change: needed because `pdftotext` **regroups table rows and drops `\texttt{}` underscores**, so the
  cell layout of a new float cannot be read from text at all, and p6 for the new §3.3 title, the boxed criterion and the
  extended lead-in. The p4 read confirms eight columns, no collision, `readout closure?` bold and correctly
  placed between `family ceiling?` and `falsifies only?`, the caption's *"× in all seven columns"* true of
  the `strongest baseline` row, and *"the last column is × on every row, ours included"* true of
  `certifies mechanism?`. It also showed one thing text cannot: **`\textbf{\checkmark}` in the bottom row is
  a no-op**; the glyph has no bold shape, the same silent font-shape fallback as *`\emph` inside a theorem
  renders upright*. Nothing in print depends on it (the caption's *"three bold columns"* points at the
  **header** cells, which are bold), and it is recorded in the source rather than "fixed", since swapping the
  glyph would trade a no-op for a font substitution on a saturated page.
- **The reconstruction gate: pp1–6 read as one unit, not as the pages an edit touched.** The chain a
  reviewer who reads only the front matter now follows: **p2** names six critical-path objects including
  *"Table 1, the axes no prior device attains"* → **p4** is that table, whose caption ends *"(§3.3)"* →
  **p6** is §3.3, retitled *"A Baseline's Strength Bounds Nothing; the Family's Ceiling Does"*, carrying the
  boxed criterion and the practice ⇒ requirement contrast that answers §15. Before this round the chain had
  no second link: nothing in §1 pointed at Table 1, and §3.3's entry was glossed as a caveat.
