# Response to the review (round 12)

*Not part of the paper. Text for the response form.*

## First, a correction that is ours to make: you reviewed a two-round-old file

The review states it was made against `iclr2027_conference(10).pdf`, **61 pages, updated
Sept. 3**. 61 pages is the round-10 build. The current file is **63 pages**, and two
rounds of revision sit between them. That is not a complaint about the review; it is a
failure of ours to make the version legible, and we would rather say so than let the
response read as if we were contradicting a careful reader.

The practical consequence is that two of the review's asks were already met in the file
we should have put in front of you, and we can show it rather than assert it:

| Ask | Status in the current build | Evidence |
|---|---|---|
| §10: replace *"training-library membership is a **causal determinant**"* with a formulation scoped to the intervention | Done in round 11, at all four sites | `pdftotext iclr2027_conference.pdf - \| grep -c "causal determinant"` → **0**. The four surviving sites read *"under this leave-one-schema-out intervention, including the generating schema in the training library **causally changes** identification accuracy, structural distance held exactly fixed"*, which is your formulation. |
| §15: audit whether *"control-complete through tier 3"* is used where the family, not a member, was cleared | Done in round 11 | Every verdict now travels as **`F_3`-complete**, defined in the boxed contract under Definition 1 so the family is named in the shorthand: *"we write **F_3-complete** for the tier-3 verdict so the family travels in the name; it never means exhaustive structural completeness."* |

Three further round-11 additions the review does not mention, and which bear on its
concerns, are the **5×4 wrong-schema transfer matrix** (Appendix AP: the control for
whether the coverage effect is specific to the generating schema or merely to
out-of-library exposure), the **boxed epistemic contract** under Definition 1, and the
assertion suite reaching **1663** live assertions.

We have not changed the paper in response to §10 or §15, because there is nothing left to
change. Everything below is new work in this round.

---

## §13: Figure 1 is now the centerpiece, on page 3

This was the review's strongest presentational ask and we agree with it completely. The
ASCII flowchart the review supplies is, almost line for line, what panel B of Figure 1
already drew: tier-1 screen → tier-2 screen → skyline → renaming → twin and the φ_d
family → coverage → *"only now interpret learned performance."* The content was right and
the **placement** was wrong: the figure was `\input` inside §3, landing on **page 6**,
after the reader had already been asked to hold four tiers, two propositions and a
definition in their head.

- Moved to immediately after the contributions paragraph of §1. It now lands on **page 3**.
- Enlarged ~1.25×. The lever was not `\resizebox`: the tikzpicture already filled the
  text width, so resizing bought nothing. Panel A's italic note column was folded into the
  tier boxes as second lines, which narrowed the natural bounding box and let the resize
  actually take effect.
- Panel B's header now states the criterion outright rather than labelling a diagram:
  *"The criterion, as a procedure: fail at **any** stage ⇒ the reading is unsupported."*
- The caption leads with the review's own sentence.

## §20.2, §20.3: the central claim, stated precisely once, then not repeated

The review asks for the claim to be made brutally precise, and separately observes that
the *"what we do not claim"* material recurs. Those are the same fix: state it once,
exactly, and delete the restatements.

Added as the closing line of the boxed contract under Definition 1, in substance verbatim
from the review:

> **A held-out-form score is evidence for composition only relative to an explicitly
> specified family of alternative explanations; outperforming a single baseline, however
> structurally sophisticated, is insufficient.**

Then the repetitions went. *"never certify"* appeared at **4** sites (abstract, §1 twice,
§5); it now appears at **2**. `conclusion`'s `Not established` block stays in full; it is
scope, not self-flagellation, and previous rounds credited it explicitly.

## §14: self-correction cut from five sites to one

The review is right that this crossed from honesty into a tic. The rhetorical sites were:
the abstract's *"costs us four claims so far, two of them moving against us"*; §1's *"the
first thing it falsified was our own work"*; §1's validation sentence; §3's *"apply it to
our own positive results too"*; and Table 1's caption clause *"four of the six are our
own"*. Four of the five are gone. What survives is **one sentence** in §1's validation
paragraph, plus **Table 1**, which carries the same history as data rather than as a claim
about our character. `grep -c 'our own\|ourselves\|against us'` over the six main-text
files returns **1**.

## §12: the abstract, restructured around three findings

It was five packed paragraphs carrying 14 two-and-three-decimal numbers. It is now the
framework and the criterion, then:

- **Finding 1: a held-out-form score can be a lookup task.**
- **Finding 2: one architecture survives the criterion.**
- **Finding 3: what generalizes is library coverage, not composition.**
- **What we do not claim.**

Same length: page 1 has literally zero slack, the abstract exactly fills it and §1 starts
on page 2, and 10 numbers instead of 14. The framing sentence is yours: *a stronger
baseline is not necessarily a stronger control*, which is also the paper's one measured
methodological result (M(φ_d) is non-monotone in d), so the abstract now opens on the
contribution rather than on the setting.

One implementation note, since it cost us a page and may save you one: the four
`\paragraph{}` headings we first used to structure the abstract added enough vertical space
to spill it onto page 2. Inline `\textbf{}` labels with blank lines between paragraphs
render the same and cost nothing.

## §11: numeric density

`experiments.tex` carried **115** two-and-three-decimal numbers over four pages; it now
carries **84**. The split matters more than the total, since the complaint is about reading
prose and not about reading tables: **77 of the original 115 were in prose, and 45 are
now**; a 42% cut where it was felt. The largest single win was deleting a sentence that
re-read Table 3's `d=4` column in prose (`0.918 → 0.955 → 0.980 → 0.987`) in favour of
*"rises monotonically in training depth (Table 3, column d=4)"*.

45 is close to the floor. Of those, 8 are the four load-bearing intervals below, and the
rest are the twin's construction guarantees (the bags pinned at exactly `0.500`, which is
the claim) and the non-learned floors each result is measured against, which is the
method, not decoration.

We did **not** strip the intervals on the four load-bearing contrasts (the `+0.079`
composition cost, the `+0.061`/`+0.054` coverage deltas, the `+0.070` wrong-schema
contrast, the `+0.299` boolean twin gap). Those are the claims; removing their uncertainty
would have traded a clarity point for a rigour point.

On §20.3's *"compress by 15–20%"*: we did the compression and **reinvested it rather than
banking it**, because the main text is at the 9-page limit and the material an earlier
round asked to be elevated is in it. The page count is unchanged; the conceptual load is
lower. If you would prefer the shorter paper, the cuts are identified and we can ship it.

## §20.4, §20.5: the four-primitive result as the definitive case study

Table 3 already was the training-depth × test-depth matrix. What it lacked was a title
that said so, so it is retitled to state the design in the title line: **"The paper's
central experiment: 4 rewrite primitives × 24 unseen orders × test depths 1–4"**, and §4.3
now opens by naming it as the paper's central empirical object.

§20.5's skeptic pre-empt existed but with the polarity inverted: claim first, disclaimer
trailing. It now runs in your order:

> **This does not show that Tree-LSTMs reason compositionally in general**, and
> Proposition 1 says no probe of this kind could. **It shows that under a controlled
> rewrite algebra whose primitive transformations are observed but whose compositions are
> not, the encoder systematically generalizes to unseen transformation orders and depths**
> — descriptively over the primitives, orders and depths tested.

One deliberate deviation: we did not bold Table 3's diagonal. Row 1 (*composition never
seen*) is already fully bold and is the actual finding; a bold diagonal would compete with
it.

## §16: architecture dependence, reframed as a finding

The review is right that we reported this as a caveat when it is the thesis. Added to
`Scope.`:

> **We claim no architecture independence, and treat that as a finding**: a GIN that clears
> every bag on unseen boolean classes sits at **chance** on the shape-matched twin, so the
> twin separates two encoders a held-out-form score ranks together.

That is the framework doing exactly what it is for. An architecture-independence claim
would be the weaker paper.

## §4: the family count, conceded in the table's own paragraph

23 corpora, four families, but **15 of the 23 are EQNET variants**. §4.2 now says so
before the table is read: *"The breadth is over corpora, not over benchmark families: 15 of
the 23 are EQNET variants, so the effective family count is four, and a per-family reading
of the table is the honest one."*

## §17: one command per headline object

Purely additive, so there is zero regression risk against the 1663 assertions: no runner
moved, no import changed, `verify_claims.py` untouched.

```
reproduce/figure1.sh   tier screens, all 23 corpora        R6            ~1 min
reproduce/table1.sh    what the audit changed              R1,R2,R3,R5   ~5 min
reproduce/table2.sh    entitlements (no compute)           —             seconds
reproduce/table3.sh    the central experiment              R16,R17       ~57 min
reproduce/table4.sh    training-library coverage           R24,R25       ~11 h
reproduce/all.sh       everything, then the assertions     all           days
configs/{poly8,boolean8,feynman}.yaml
```

Each script is a thin wrapper over the command already in the matching `REPRODUCE.md` row
and **ends in `python3 verify_claims.py`**, so a green run is an assertion pass rather than
a claim of one. A headline-object → script → `REPRODUCE.md`-row map is now at the top of
both `REPRODUCE.md` and `README.md`.

The `configs/*.yaml` files are **documentation of the flags, not a config loader**;
nothing reads them at runtime, and `configs/README.md` says so in its first line, because a
config file the code ignores is worse than none if you do not know that it is ignored.

## §8: what prevents a specialized invariance to these four primitives?

This is the one substantive objection in the review, and the one place we have run new
compute against your advice that no new experiment is needed. We think it earns its keep
because it is not added breadth; it is a direct measurement of the mechanism the objection
names, and §4.4's family result made a falsifiable prediction about the answer that we
pre-registered before the run.

**The design.** `r89_leave_one_primitive_out`, 25 seeds, 125 encoders, ~6.4 h. For each of
the four primitives $h$ we train an encoder whose library holds single applications of the
other **three** only, backfilled from those three so `k_para` stays exactly 6: form count
matched, so the contrast isolates *which primitive is present*, never how much data. The
drawn permutation places $h$ **first**, so every depth-$d$ test form on ladder $h$ contains
$h$ and the whole 1–4 ladder tests unseen-*primitive* generalization at increasing
composition depth. The held-out trees are byte-identical across arms; the fifth arm is the
all-four IN control. Its own curve, over the four ladders and the new seeds, is
$0.991/0.975/0.951/0.911$ against §4.3's published never-composed row of
$0.997/0.983/0.950/0.918$: agreeing to within $0.008$ at every depth, which is what anchors
`r89` to the experiment it is interrogating.

**The answer to your question is: nothing does.** The paired IN-minus-LOPO cost at $d{=}4$ is
$+0.390$ $[0.355,0.425]$ for `commute`, $+0.516$ $[0.484,0.548]$ for $x{+}0$, $+0.556$
$[0.523,0.589]$ for $x{\cdot}1$ and $+0.678$ $[0.647,0.708]$ for double-negate: every
interval excluding zero, pooled $+0.535$. That is an **order of magnitude** above the
$+0.079$ cost of never having *composed*. So the invariance is specialised to the primitives
the library covers, and we now say so in §4.3 and scope the claim accordingly. We concede the
objection and report it as a measurement rather than answering it rhetorically.

**But the collapse has a shape, and the shape is the finding.** At $d{=}1$ the LOPO encoder
sits **on** its own untrained control (max $|{\Delta}|=0.045$ across the four ladders):
training buys *nothing at all* for a primitive it never saw once. Yet across depths 1–4 the
LOPO encoder is nearly **flat** (worst decay $0.041$), while the untrained control it
matches at $d{=}1$ collapses (decays $0.384/0.211/0.215/0.133$). **What training buys here is
invariance to composition *depth*, not to the primitive inventory.** That is a sharper scope
statement than §4.3 could make on its own, and it is the honest form of your objection's
answer: the encoder has not learned "composition"; it has learned depth-robustness over a
covered inventory.

**Both pre-registered predictions failed, and we report them as failures.** We predicted from
§4.4's family result that `commute` (structural, with no family member in the library)
would hurt most and the two identity insertions least. `commute` is in fact the **cheapest**
($+0.390$) and double-negate the costliest ($+0.678$); and the identity/non-identity split
is a **dead tie** ($0.5362$ vs $0.5340$, separated by $0.0022$), with all the variation
*inside* its groups. The honest statement is that the family reading has **no explanatory
power on primitives**, not that it inverts. §4.4's schema-level claim stands where it was
measured, and we do not extend it.

**What does order the cost, labelled post-hoc.** The four costs are ordered by how many
tokens the primitive *adds* ($\Delta$tok $=0,4,4,8$), and the three $\Delta$tok groups' $d{=}4$
intervals are pairwise **disjoint** while the two primitives *sharing* $\Delta$tok $=4$ are
**not** separated, which is what makes it an ordering by $\Delta$tok rather than four
unrelated numbers. Ruled out: ladder difficulty, since the untrained control is flat across
the four ladders at $d{=}4$ ($0.166$–$0.191$, range $0.025$); it is *not* flat at $d{=}1$
($0.317$–$0.550$), which is why the claim is made at $d{=}4$ and not pooled. Not ruled out,
and stated as such in Appendix AQ: $\Delta$tok is confounded with how much of the tree the
primitive rewrites. This is post-hoc and Appendix AQ says so in those words.

**Verification.** Appendix AQ; `REPRODUCE.md` row **R25**; `check_lopo()` is check function
**#22** and takes the verifier to **1717** assertions. It establishes the construction by
**recomputation against an independent reimplementation**, its own parser, serialiser and
rewriter, deliberately *not* importing `equivalence.py`, so agreement is between two
implementations rather than between the log and itself: 9400 serialisations round-trip
byte-for-byte, 0 library-vs-test collisions recomputed over all four ladders, 3200/3200 exact
token-delta triples, and the held-out primitive absent over *every* rewrite site of every
anchor. The pre-registered reading (`specialised_collapse`), both **failed** predictions and
the $\Delta$tok guard are all asserted, so a rerun landing elsewhere fails loudly.
**12 negative controls** fire on their intended assertion, every mutated log `cmp`-checked
byte-for-byte afterwards; **two of them make our claim *stronger***: LOPO matching IN, and
P1 coming true, and both must and do fail.
