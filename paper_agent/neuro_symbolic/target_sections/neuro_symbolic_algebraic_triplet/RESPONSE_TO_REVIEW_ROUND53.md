# Response to Review: Round 53

Thank you. This is the thirteenth review on a thirteenth rubric, and your two lowest sub-scores (**Generality
6** and **Theoretical 6.5**) are both about *scope*, not about rigour. That is the correct diagnosis, and this
round works only on it.

You state your 7 → 8 lever twice, in §19 and again in §20, and it is conjunctive:

> *"A larger rewrite basis × two architectures × composition-depth generalization experiment, with the same
> byte-identical coverage intervention"* — and *"slightly tighter positioning around the methodological
> contribution."*

**`verify_claims.py` rises from 2486 to 2591 assertions, exit 0, all three shipped copies
byte-identical (md5 `85e77e416b9b89fce4665bff4805348c`).** The standing rule in this correspondence is that the first paragraph
says whether the assertion count had to rise and why. It rose because **this round adds four runs**: the one
arm of your §19 design that the paper says in its own text it did not run, and a round that adds a measurement
without adding assertions would be a round that shipped an unaudited number. Gate coverage also rises:
`check_protected_claims.py --control` goes **20 → 22**, via two new checks aimed at the two defects this round
found in itself; a headline result that named no encoder, and the grid you asked for being reachable from no
body file.

**Three things before the answers. One is about your copy of the paper, and two are defects we are conceding.**

## 1. The build you reviewed predates every source file in the paper, including the bibliography

You name it: `iclr2027_conference(20260904-061008).pdf`. That timestamp, `2026-09-04 06:10:08`, is older than
**all ten** sources, the first round in this correspondence where not even the abstract predates the reviewed
build:

| source | last edited before this round | vs your build |
|---|---|---|
| `iclr2027_conference.bib` | 2026-09-07 18:09:53 | **after** |
| `iclr2027_conference.tex` | 2026-09-10 18:25:16 | **after** |
| `abstract.tex` | 2026-09-11 09:10:00 | **after** |
| `introduction.tex` | 2026-09-12 10:46:36 | **after** |
| `conclusion.tex` | 2026-09-12 12:25:23 | **after** |
| `statements.tex` | 2026-09-12 13:00:19 | **after** |
| `appendix_domain_guards.tex` | 2026-09-13 09:36:04 | **after** |
| `methodology.tex` | 2026-09-12 19:38:31 | **after** |
| `related_work.tex` | 2026-09-12 20:11:54 | **after** |
| `experiments.tex` | 2026-09-13 09:14:04 | **after** |

Four consequences, each measured rather than asserted:

- **`four-tier` occurs nowhere in the current paper.** The tier system your §5 describes as four-tier is S0–S3
  plus the admissibility ceiling, and it is stated as an object in §3, not as a tier count.
- **Your "Proposition 3"** (the resolution–retrieval tradeoff) is our **Proposition 5**, and it is
  **appendix-only**, on p69 inside the proofs appendix AN. It is not a body proposition and carries no body
  claim.
- **Your LOSO numbers `+0.061` / `+0.054`** are the 10-seed `r59` values. They have a **25-seed replication at
  `+0.094 [0.031, 0.139]`** in Appendix AQ, which is the number the body now reads against.
- **Your *"0.517 strongest non-learned baseline"*** is superseded. The catalogued bag is `0.517`; the paper's
  margin is now read against the **best of 706 searched composites, `0.676`** (§4.2, Appendix BB), which is a
  strictly harder comparator and shrinks our own headline ratio from `1.7×` to `1.3×`.

## 2. Your §19 figure is Table 29 on p57, and we print it for three corpora, but §4.3 never said which encoder its result belongs to

This is the round's real finding, and the concession is ours, not yours.

Your sketch is *"rows = training exposure (primitives only / 2-compositions / 3-compositions / full library),
columns = Depth 1–5; then repeat it for Tree-LSTM and one other architecture."*

| piece of your ask | where it already is in the copy you read |
|---|---|
| rows = training exposure × columns = test depth | **Table 29, rendered p57** (`poly8`, `K=200`, 5 seeds, tag `r81`): rows `1: composition never seen` / `2: depth-2 composites in library` / `3` / `4`, columns `d=1..4`, **plus** the paired cost-of-never-composing row (`+0.011 / +0.035 / +0.069`), the length-identical alternate-order row, and four control rows |
| *"the same byte-identical coverage intervention"* | the same table's above-diagonal cells, all `≥0.993`; that is the intervention, and it is what licenses reading the depth-4 deficit as one of **coverage** rather than of depth |
| the same grid on further corpora | **Appendix AM, p64**: the identical design on `oneVarPoly13` (same algebra, different anchors) and `boolean8` (**a different algebra**, four new primitives), with nothing changed but `--corpus` |
| *"repeat it for one other architecture"* | **Appendix AK, pp61–63**: its **first row** (the never-composed arm) for **GIN and a Transformer**, in **two replicates each** |
| the arm that was genuinely missing | rows 2–4 for GIN and the Transformer. **The reviewed build discloses this itself**, at the end of Appendix AK: *"We did not run the composites-in-library arm for these two encoders, so this table carries no upper bound and no paired cost-of-never-composing, and the log records that omission rather than leaving it to be inferred."* That sentence is **gone from the current build**; this round ran the arm, so both AK and the near-identical disclosure in AJ now report the result instead (see §9). |

**Why you could not find any of it: §4.3's body paragraph named no architecture.** Its closing clause routed to
Appendix AK as the **fourth of four bare parenthetical `\ref`s**, and `conclusion.tex` contains **zero**
architecture words. Table 29 was referenced from **no body file at all**. Comment-stripped body counts:
`experiments.tex` had 5 × `Tree-LSTM`, 4 × `GIN`, 3 × `Transformer`, but the only body sentence that *compares*
encoders is about the boolean twin protocol, not about the composition curve.

**And it was worse than "not cited from the body", which we found only on the last read of the round.** Table 29
sits in Appendix AH, whose first sentence is **"Superseded, and kept only for continuity"** and whose banner ends
**"a reader checking the current claims can skip to AU"**. That banner is true of the two-schema table above
it, and false of Table 29, which is the current four-primitive design (tag `r81`) and was placed there for
space. So if you did reach the appendix holding your grid, the paper told you to skip it. Three repairs, all
measured: Figure 3's caption on **p8** now ends *"exposure × depth in full: AH"* (the caption's last line carried
`146.76pt` of tail, the addition renders as 30 characters, and p8's line count is unchanged at 124); AH's banner
now carries the exception by name, **"One table here is current and is not superseded"**; and AH's title lists
`r81` alongside `r76` and `r79`, so the grid is findable by its own tag. This is also the one thing here no gate
could see: `check_protected_claims.py` asks whether a float is cited *at all*, and Table 29 is cited five
times, every one of them from another appendix. **Citedness is not reachability**, and the new
`check_grid_route()` now checks the second thing.

This is the **fourth occurrence** of the same defect class in this correspondence (rounds 40, 47, 52), and the
first with a measurable price: it is costing the two lowest sub-scores on your rubric. All three halves are
fixed this round: the missing arm is run (§3 below), §4.3 now says whose result it is (§4 below), and the grid
is reachable from the body and no longer disclaimed where it lives.

## 3. Barrier 1: the paper's own answer is harder on the paper than your ask is

You write that *"the positive result is too dependent on the Tree-LSTM."* Appendix AK's measurement agrees with
you and goes further. Depth-1-minus-depth-4 decay on the never-composed arm, same corpus, same 200 classes,
same libraries, same held-out chains, same 5 seeds, same 10 epochs, only the encoder differing:

| encoder | `d=1` − `d=4` | vs Tree-LSTM |
|---|---|---|
| Tree-LSTM | `+0.079 [0.063, 0.097]` | — |
| GIN | `+0.258` and `+0.260` (two replicates) | **3.3×** |
| Transformer | `+0.481` and `+0.519` | **6.1–6.6×** |

**No replicate's interval touches another architecture's**, so the ordering is resolved over classes rather
than read off point values. And the criterion bites: **the Transformer passes the `F_3` audit at depths 1 and 2
only.** At `d=3` the strongest non-learned baseline lies *inside* its class-level interval in both replicates;
at `d=4` both point values fall *below* it, and in the second replicate a zero-parameter bag of tokens beats a
trained Transformer resolvedly. By Definition 1 (p5) those results do not pass the audit, and by Proposition 2
no axis-C claim follows from them.

That is also the answer to your §20: *"position this as benchmark-evaluation methodology"*, and it is the
sharpest instance in the paper: at `d=3` a point-value audit would have licensed the Transformer on the first
replicate (`0.270 > 0.250`) and refused it on the second (`0.231 < 0.250`). **The same experiment, run twice,
opposite verdicts.** It is the one place where the paper's own criterion declines to license a result we ran.
Your point is that this belongs closer to the front; it was 53 pages from where you would look for it.

## 4. We ran the one arm the paper said it had not run, and it moved a verdict we had stated too broadly

Your §19 asks for the grid "repeated for Tree-LSTM and one other architecture". The grid existed for three
corpora and its **first row** existed for two further encoders; what did not exist was the rest of the grid for
those encoders, which the paper disclosed itself. We ran it: **four invocations, two replicates each for GIN and
a Transformer.**

**It is the same experiment, not a new one.** The invocation is the Tree-LSTM run's own recorded argument dict
with `--arch` changed and `--primitives_only` dropped. **No rewrite schema was written**, so `equivalence.py` is
untouched and no number already in the paper can move, which is also our answer to your Barrier 2, in §5 below.
The recorded args differ from the Tree-LSTM run's in exactly `{arch, corpus, tag}`.

**It was pre-registered before it was run**, in `PREREGISTRATION_r105_composites_arch.md`, which fixes four
preflight abort conditions and states which of four outcomes licenses which sentence. That document earned its
keep twice, and both times against us; see the two withdrawals below. All four preflight conditions passed, two
more strongly than they were stated: `construction` and `closure_guard` are equal to the Tree-LSTM run's **as
whole dictionaries** (zero differing fields, not a field-by-field spot check), the untrained control matches the
published one **per seed** rather than on the mean, and every non-learned bag agrees to `0.000000`.

### The completed grid, read as the paper reads it

`closes` is the fraction of that encoder's **own** `d=1`−`d=4` deficit that its best library recovers, so each
encoder is measured against its own ceiling rather than the Tree-LSTM's. `pays` counts how many of the six
above-diagonal cells (training deeper than test) fall below row 1 **at their own test depth**: accuracy given
up at shallow depths to buy deep ones.

| encoder, corpus | paired `d=1`−`d=4` | `d=4` gain from composites | closes | pays |
|---|---|---|---|---|
| **Tree-LSTM, `poly8`** | `+0.079 [0.063,0.097]` | `+0.069 [0.052,0.087]` | **87%** | **0 of 6** |
| Tree-LSTM, `boolean8` (different algebra) | `+0.230` | `+0.030 [0.002,0.058]` | 13% | 5 of 6 |
| GIN, `poly8`, rep 1 | `+0.293 [0.262,0.324]` | `+0.065 [0.029,0.102]` | 22% | 3 of 6 |
| GIN, `poly8`, rep 2 | `+0.248 [0.220,0.277]` | `+0.032 [−0.004,0.066]` | 13% | 4 of 6 |
| Transformer, `poly8`, rep 1 | `+0.483 [0.450,0.516]` | `+0.320 [0.288,0.353]` | 66% | 4 of 6 |
| Transformer, `poly8`, rep 2 | `+0.463 [0.428,0.498]` | `+0.292 [0.258,0.326]` | 63% | 3 of 6 |

**The finding is the `pays` column, not the `closes` column.** Composites in the library recover part of the
depth-4 deficit for *every* encoder; only for the Tree-LSTM on `poly8` is the recovery **free**. That is the one
signature stable across both replicates of both new encoders, and it separates one cell of that table from the
other five: `0 of 6` against `3`, `4`, `4` and `5`.

**We withdrew two sentences to get there, and this is the more useful half of the answer.**

1. A draft of this round said *"`boolean8`'s coverage ladder is non-monotone, **as is GIN's**"*. GIN's first
   replicate supports it (the `d=4` column turns over, argmax at training depth 3); **its second replicate
   falsifies it** (argmax 4, monotone rising). The clause was cut from §4.3 and an in-source comment now records
   why, so it cannot be re-sharpened. The pre-registration is the only reason it was checked against a second
   replicate before shipping rather than after.
2. A draft framing said the *closure* is the recursive encoder's. **The Transformer's 66% retires it.** Closure
   fraction does not order by encoder recursion at all: `87%`, `66%`, `22%`, `13%`, `13%` across the five
   encoder-algebra pairs. The paper claims the recovery is *free* only for the Tree-LSTM on `poly8`, which is
   what the measurement supports, and not that it is *larger* there.

### The result that matters most is one your ask did not anticipate: the audit verdict moved

Appendix AK reported, in bold, that **the Transformer passes the `F_3` audit at depths 1 and 2 only**: at `d=3`
the strongest non-learned bag lies inside its interval, at `d=4` below it. Our pre-registered outcome (c)
predicted the composites rows would fail the same way. **They do not.** Trained with depth-4 composites in the
library, the same encoder clears the same bag **resolvedly at all four depths**: interval lower bounds
`0.613 / 0.650 / 0.586 / 0.449` against bags `0.245 / 0.255 / 0.255 / 0.185`.

So the same encoder fails the audit past `d=2` on one training exposure and passes at all four depths on
another. **That is not a defect in the criterion; it is the criterion doing exactly what §3 says it does**: it
licenses a claim about a *trained model on a task*, never about an architecture. But it means our own bolded
sentence was stated at the wrong scope, because when it was written only one exposure had been run. It now names
the exposure it was measured on, in the appendix and in §4.3's body clause. **An architecture-level reading of
that verdict was unlicensed, and it was ours.**

This is also, we think, the sharpest available answer to your §15/§20; that the paper is
benchmark-evaluation methodology rather than a discovery about how neuro-symbolic reasoning works. The
methodology's value here is not that it certified something; it is that it **refused** a result we had run, and
then, on a second exposure, refused our summary of its own refusal.

### The free replication, and a bound that widened

Training depth 1 *is* the never-composed arm, so these four runs are a third and fourth invocation of Appendix
AK's rows at no extra cost. The pre-registration committed in advance to widening AK's stated replicate envelope
if a new value fell outside it. It did: GIN's paired `d=1`−`d=4` reads `+0.258 / +0.260 / +0.293 / +0.248` over
the four invocations, and its per-depth row-1 envelope is **`0.047`**, not the `0.010` two invocations gave. The
appendix now states the four-invocation bound **alongside** the two-invocation one rather than in place of it:
that earlier sentence is about *back-to-back* invocations and is true of them, so both stand. AK's architecture
ordering survives the widening with room: `0.047` is under a third of the `0.169` gap to the Tree-LSTM's curve.

**It widened for *both* encoders, which is why we ran the check on both** rather than only on the encoder whose
bound was tighter: the Transformer's four-invocation row-1 envelope is **`0.062`** against the `0.039` two gave,
its paired drops reading `+0.481 / +0.519 / +0.483 / +0.463`. And the composites arm's *own* replicate envelope (
measured on that arm rather than inherited, since a bound on one arm is not a bound on another) is `0.047`
(GIN, coincidentally the same figure) and `0.034` (Transformer) over the 16 matrix cells.

**And the free replication found something in our own published row.** Over all four invocations the
Transformer's never-composed row is refused at `d=4` *unanimously*; that refusal is what the bolded restriction
rests on, but at `d=3` it is **three refusals to one clearance, and the dissenter clears by `0.007`**: lower
bounds `0.239 / 0.204 / 0.230 / 0.262` against a bag of `0.255`, with the nearest refusal missing by `0.016`, so
the split is resolved at the criterion's own resolution and is not an artefact of the tie rule. The appendix
reports *three of four with the margin quoted*, never a universal. This is the paper's own *"same experiment, run
twice, opposite verdicts"* recurring under the **interval** rule at its own boundary, on the row we published,
and a point-value rule would have recorded four passes and seen nothing.


## 5. Barrier 2: eight primitives across two algebras, and one of your requested primitives is *inapplicable*, not missing

Your basis: commutativity, associativity, distributivity, identity, cancellation, double negation, De Morgan,
exp/log, power, rational. Measured against the paper:

- **Eight heterogeneous primitives are already run, across two algebras.** Four on `poly8` (`_rw_commute`,
  `_rw_double_negate`, `_rw_add_identity`, `_rw_mul_identity`) and four on `boolean8` (a **different algebra**,
  where the `poly8` primitives are invalid) **including one non-local (De Morgan)**. Each set has its own full
  training-depth × test-depth matrix (Appendix AM).
- **Distributivity is already run**, as the local → non-local swap of Appendix AS (tag `r91`): `_rw_distribute`
  fires on **283 of 1102** anchors; the coverage cost is `+0.204 [0.161, 0.250]` non-local against
  `+0.468 [0.391, 0.540]` local, a difference-in-differences of `−0.263 [−0.344, −0.184]`.
- **Associativity cannot fire on this corpus.** `_rw_reassoc` fires on **0 of 1102** anchors, because EQNET
  forms are already right-nested. This is recorded in `r81`'s own `why_four` provenance field. "Add
  associativity" is therefore a measurement about the corpus, not a gap in the design.
- **28 primitives** already appear, as the adversarial hill-climb family behind §4.2's `0.676`.

**We did not write a new rewrite schema for this round, and that is deliberate.** `equivalence.py` untouched is
what guarantees that no published number in the paper can move while four new runs are added. Appendix AS
states the same discipline for its own run.

## 6. Barrier 3: one more independent domain

Four non-`poly8` external cases already ship: published **SCAN** (Appendices AX, AY), **Type-2 code clones**
(Appendix AW), the **Lample–Charton** integration case, and **`boolean8`** as a different algebra. The first two
are the **last two rows of Table 10 (p26)**, the ledger of what running the audit changed: *"our SCAN
`add_prim_jump` 0.987: **narrowed** — it passes, but `sup F_3 = 0.0005`"* and *"our Type-2 clone S2 0.987:
**settled below S3**."* Note that both are audits turned on **our own** claims.

We are **not** adding a fifth domain this round, and the gap you are pointing at stays disclosed in the paper's
own words in §4.5: no *third party's* headline claim has been overturned by this audit *outside* symbolic math.
Adding a domain that does not have that property would widen the table without widening the evidence, and the
honest version of Barrier 3 is that the disclosure stays.

## 7. Six asks are already satisfied verbatim in the copy you read: measured, with rendered page numbers

**Tenth consecutive round in which a reviewer's proposed edit would have deleted a predecessor's requirement.**
We answer these by measurement rather than by edit:

| your ask | where it already is |
|---|---|
| **§3** *"highlight the non-monotonicity / 'controls are not totally ordered' insight far more aggressively"* | the exact phrase *non-monotone in resolution* occurs **4×**, on **pp1, 2, 5 and 9**; it is the **abstract's closing sentence** (*"the ceiling is non-monotone in resolution, and widening the family can only cost a pass"*), it recurs in §1 and again in §3 where the corollary is stated, and it is numbered finding **(2)** of the conclusion |
| **§6** *"explicitly downgrade confidence in Finding 3"* | §4.3 already reads, **in bold**, *"the coverage-closure mechanism is polynomial-specific"* (p8), and conclusion finding (3) is already scoped *"to the polynomial setting for the coverage mechanism"* (p9). This round **widens** that caveat further; see §4 above |
| **§8** *"stop making 23 corpora sound like the main evidence of generality"* | both body mentions carry their own narrowing. p2: *"a zero-parameter classifier over 23 corpora, **15 of them EQNET variants**"*. p7, §4.1, whose title is *"Only One Family Carries the S1 Flaw"*: *"Over all 23 corpora the S1 flaw is real and **confined to one published family**"*; the survey is used to *localize* the flaw, not to claim breadth |
| **§9** *"move Lample–Charton further into framework-validation"* | already framed as *"an S2 task correctly identified, and evidence of nothing above it"*, under the paper's italics on p8: *"portability, not general validation, never prevalence"* |
| **§13** *"the main paper should revolve around four visual objects"* | it does, and they are on the first five pages: Figure 1 (the audit) **p2**, Figure 2 (the framework) **p3**, Table 1 **p4**, Table 2 **p5** |
| **§15/§20** *"position as benchmark-evaluation methodology, not a discovery of how neuro-symbolic reasoning works"* | the conclusion's final, gate-pinned sentence: *"The audit falsifies; it certifies nothing; Table 2 is the ledger."* |

## 8. §11 and §12: conceptual overload, and "too defensive and qualification-heavy"

We take this as the one criticism we cannot answer by measurement, and we can only tell you what it costs.
§3 spans the paper's **only two negative-slack pages** (p5 `−0.695pt`, p6 `−1.927pt`, against a saturation
height of `732.01pt`), and `placeins [section]` bars those pages from borrowing space. Total body slack across
the nine body pages is **≈7.2pt: 0.6 of one line, and all of it is on p3.** So a simplification here is not a
stylistic choice with a stylistic cost: any sentence added to §3 pushes the conclusion off p9, and a 10-page
body is a desk reject at this venue.

The specific qualifications you would remove were each *asked for* by an earlier reviewer of this paper:
`methodology.tex`'s `Terms, once.` block is a predecessor's requirement and is simultaneously the answer to
your §11; the §1 ordering is already the three-finding structure your §12 requests. We would rather carry the
qualification and say so than delete a predecessor's requirement, which is the failure mode that has now
recurred in ten consecutive rounds.

## 9. What changed in the paper this round

**Body: §4.3 now names the encoder its headline result belongs to.** *"Trained on singles alone the **Tree-LSTM**
identifies them at 0.736"*, where the sentence read *"the encoder"* in the build you have. That two-character
substitution is the round's central repair, and we found it by measurement rather than by reading your review: §4.3
contained **zero** architecture words naming the encoder behind its 0.736, and **exactly one** naming an encoder
that *fails*. So a reader of p8 alone could not say whose result the paper's headline composition number is, which
is your Barrier 1 stated as a property of our typesetting rather than of our evidence. It is also why you could
not find the three-encoder answer in Appendix AK: this paragraph routed to AK as the fourth of four bare
parenthetical refs.

**And two clauses that narrow a claim.** §4.3's closing parenthesis now reads *"a **singles-trained**
Transformer fails the audit past $d{=}2$"*. That qualifier is not a hedge and it is the round's most consequential
single word: the arm in §4 above shows the *same* Transformer clearing the $\mathcal{F}_3$ audit at all four
depths when its library holds composites, so the unqualified sentence (which is what the clause said until this
round) asserted an architecture-level verdict our own criterion never licensed. §4.3's scoping clause likewise
now reads **polynomial- *and* encoder-specific** for the coverage-closure *mechanism*, which is your §6's ask
arriving as a measurement rather than as a concession.

All three edits are funded, not free, and one of them nearly cost us the paper. §4.3's paragraph sits on p8, which
carries **`0.000pt`** of vertical slack; the body's total slack is ≈`7.2pt` and all of it is on p3. We measured the
height-free tail on the paragraph's last line (`73.90pt`, ≈19 characters) and spent 16 on *singles-trained*, which
left the line saturated at `−0.00pt`. The **two** further characters of *Tree-LSTM* then cost the paragraph a
rendered line, which pushed seven lines off p8 onto p9 and pushed the conclusion's finding (3) onto p10: a
**ten-page body**, which is a desk reject at this venue. We measured it both ways, against the build as it stood before the clause landed
(p8 `123 → 116` rows, p10's first body line `Ethics Statement → conclusion prose`) and paid for the two characters inside the same paragraph:
*"188 of them realised and none trained on"* → *"188 realised, none trained on"*, `−11` rendered characters,
keeping both the number and the emphasis, and pinned by no gate. **The body ends on p9, `Ethics Statement` is the
first line of p10, all five floats are on their original pages, and the ten body pages of the slack profile are
byte-identical to the pre-round build's.** The eleventh page of that profile is the one number in it that moved,
`+0.000pt → +0.687pt`, and it is back matter, not body: the Reproducibility Statement, which sits after `Ethics
Statement`, gained the clause naming this round's four runs. We report both the near-miss and the one moved
number, because the margin was two characters wide and because "unchanged" is the claim a slack profile is
easiest to overstate.

**Appendix AK gains the arm and loses a disclosure.** The table of §4 above is new, as are four paragraphs: what
the arm shows, why the audit verdict is a verdict about an exposure, the free third and fourth replicate of AK's
own rows, and the envelopes that replication *widened*, `0.010` → `0.047` for GIN and `0.039` → `0.062` for the
Transformer, each stated as the four-invocation bound alongside the two-invocation one, since the earlier bound is
a true statement about back-to-back invocations. AK's closing sentence (*"We did not run the composites-in-library arm
for these two encoders"*) is deleted, because it is no longer true.

**And the same disclosure had a twin one paragraph earlier, which we found by re-reading rather than by any
gate.** Appendix **AJ** (the narrower `r79` two-schema design that AK supersedes) closed with almost the same
sentence, and its *first* clause is still true: AJ's own table has no composites arm and this round did not run
one for that design. Its *second* clause had gone false. It framed *"whether GIN and the Transformer could do
depth-4 composition when trained on composites"* as an open counterfactual, three lines above AK's heading, when
AK now answers exactly that on a harder design. A reader going in order was told the question was open and then
handed its answer. AJ's paragraph now keeps the scoped disclosure and routes to AK: *"…is a different question
from the one asked here, and it is not left open: Appendix AK runs that arm for both encoders on the harder
four-primitive design, so what is missing here is this narrow design's upper bound, not the answer."* (p61 of the
render; `−2 / +2` sentences, no content dropped; page count held at 100.) We report it because the general
lesson is not about this sentence: **when a run makes a disclosure stale, the stale copy is wherever the words
are, not where you remember writing them**, so the grep must be for the disclosure's wording across every file,
and no gate we have can see a sentence that is merely out of date.

**The paper is 100 pages, up from 99, and we chose that deliberately.** The reviewed build's p99 already held 118
rendered lines, i.e. the document ended exactly on a page boundary, so holding 99 pages would have required
adding **zero** rendered lines, which is to say, running the experiment and not reporting it. The appendix has no
page limit at this venue; the limit is on the body, and the body is unchanged at nine pages. We state the page
change rather than let you discover it.

**Bookkeeping.** Four new logs (`r81_matrix_gnn`, `r81_matrix_transformer`, each `×2` replicates), so
`REPRODUCE.md`'s indexed-run count rises `81 → 85` and gains entry **R50**; two of its existing entries were
*amended because this round falsified them*: R18's *"the composites-in-library arm was not run"* and its
two-invocation envelope. `verify_claims.py` rises to **2591** assertions. **Two** new gate assertions in
`check_protected_claims.py` target this round's own defect class: `check_encoder_scope()`, which fails if §4.3
states the composition result while naming no encoder but its own, and `check_grid_route()`, which fails if the
exposure × depth grid is referenced from no body file *or* is left under an unqualified "superseded" banner, so
its `--control` count rises `20 → 22`; the four gate control counts are **22 / 9 / 1 / 2**. `equivalence.py` is
untouched.

## 10. What we did not do

- **No new rewrite schema, and no new corpus.** `equivalence.py` is byte-identical, which is the guarantee that
  no published number moved.
- **No fifth external domain** (§6 above), and the gap stays disclosed.
- **No reorganization of §3** (§8 above), with its page cost stated rather than asserted.
- **No softening of Appendix AK's answer into the shape of the ask.** AK's finding is *against* generality, and
  it stays that way.
