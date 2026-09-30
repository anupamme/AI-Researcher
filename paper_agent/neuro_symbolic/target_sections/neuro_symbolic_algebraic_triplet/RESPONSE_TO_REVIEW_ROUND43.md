# Response to the round-43 review

**No new experiments, per your instruction. The single highest-leverage change in this round is four words in
an appendix: the paper had been telling you to skip the band its own significance evidence sits in. We found
that by taking your significance score literally and measuring where the ledger of changed published
conclusions is filed. 93 pages, body still ends on page 9, `verify_claims.py` `2337 → 2353`: the 16 added
assertions are itemised in §6.**

You wrote that your main reservation is *"not correctness"* but *"scope and significance,"* and that we should
**not** add more random experiments. We took both literally. Nothing below is a new run. Every number in this
response was already in the paper or already in a log the verifier reads; what changed is where a reader
encounters it.

---

## 0. The staleness note, in one sentence

You read `iclr2027_conference(20260910-091424).pdf`; the current build is 16:14 the same day, and the only
changes between them are two readiness fixes described in the round-42 changelog (`+0.218 → +0.22`, and a §1
cross-reference that pointed at §4.4 for a §4.3 result). Neither touches any ask below, and every answer here
is written against the current text.

---

## 1. The measurement that is the answer

Your significance score is 7.5, and your reason is that *adoption is not demonstrated*: the paper does not
show that the community's conclusions change. **The paper contains exactly that object, and it was misfiled
twice over.**

`tab:audit_changes`, *"What running the audit changes"*, is an eight-row ledger in which every row is an
already-published number and **four of the eight are other people's systems and leaderboards**: AI Feynman's
`0.972`, the 14-corpus $\mathrm{score}_5$ leaderboard, the StructEmb ablation, and Lample–Charton's 80M
integration encoder. Its verdict column reads *broken · **upheld** · narrowed · S2-only · restated · narrowed
and corrected · withdrawn · withdrawn*. It lived inside
`\subsection*{F. Reproducibility Details and Revision History}`, and the appendix's own reading path, added
last round to reduce reader fatigue, said:

> (i) is audit trail; (ii)–(iv) are the scientific content, so a reader who wants the science and not the
> bookkeeping can skip A–K entirely: no claim in the body rests on it.

So the paper (a) filed its conclusion-change ledger under *reproducibility*, and (b) **instructed you to skip
the band containing it**, while §1 item (i) cites that very table, which also made *"no claim in the body
rests on it"* false as written. This is our most-repeated failure mode (an appendix-only result does not
exist) with a new mechanism: **a reading path is a routing decision.** Round 42's fatigue fix mis-routed the
paper's own significance evidence, and no gate in this repo can see a routing error.

**Second measurement, same axis.** The appendix reports predictions written into the runners *before* they
ran, several of which held and several of which failed. The body named exactly **two of them, in passing**;
SCAN's, which held (§4.3), and the adversarial-search line, which failed (§4.2), and **never stated the
practice**: that predictions are registered in the runners before the runs, and that the failures are reported
as a set rather than one at a time. Preregistration is the sharpest available answer to your Objection 2 (*you
only rule out the explanations you chose in advance*): in advance, in the runner, where it could and did
fail. So what was missing was not an instance but the discipline itself.

**Third measurement: your clarity blocker, in the one form in which it is measurable.** Comments stripped,
the body's seven most common negative constructions numbered **73** across ~6,100 words: `\emph{not}` 8,
*never* 9, *not a/an* 12, *does not* 12, *is not* 21, *cannot* 9, *certifies nothing* 2. The **conclusion
carried 7 in 112 words.** Round 42's blocker was bold density; this is the same instrument one level up.

---

## 2. What changed, ask by ask

### Significance: the ledger reaches a body-only reader (p1, p2, pp15–16)

**§1 item (i) now prints the ledger's verdict *distribution*, not only its count** (`introduction.tex:14`,
renders p2): *one broken, one **upheld**, two narrowed, one re-scoped to S2, one restated, two withdrawn
against ourselves.* The load-bearing word is **upheld**. An audit that only breaks things is a critic's tool;
one that upholds a 14-corpus leaderboard under its own screens is an instrument. The abstract already carried
*"Four of the audited results are other people's"* and *"a 14-corpus leaderboard audited the same way is
upheld"*, so page 1 and page 2 now agree, and neither requires the appendix.

The distribution is **read back out of the table's own Verdict column** by a new gate function
(`check_protected_claims.py: check_ledger_distribution()`), because two representations of the same eight rows
are exactly what drifts silently here. Its `--control` corrupts one cell and the check fails.

**The appendix front matter is re-routed** (`appendix_domain_guards.tex:62,78`, renders pp15–16). The ledger
is now the **fifth critical-path object** (*"every published number the audit revised, and in which
direction"*) beside Figure 1, Table 2, §4.2 and §3.3. And the skip instruction now reads *"can skip **A–K**
*except* Table 10, which §1 cites and which is where the audit's effect on published conclusions is
tabulated."* The false clause is gone. No float moved and no `\subsection*` was added or reordered: 54
appendix letters are gated and hand-written.

### Objection 2: the preregistration discipline, in the body (p2)

`introduction.tex:14` now reads: *"Predictions were registered in the runners before the runs; four failed,
and all four are printed."* Each of the four is pinned individually in the verifier by a new census function,
and each is printed in the paper: r89's two point predictions (appendix, in full, with the `0.002` separation
that sank them), r96's non-replication reported **as a domain boundary**, and r101's operational line, which
an adversarial search beat by `+0.1584`.

**Why a failure count and not a total.** We drafted *"Four predictions were registered before their runs: two
held, two failed, all four reported"* and then withdrew it, because it is not defensible. The runs register
different *objects*, two point predictions in r89, a directional one with a named domain-boundary branch in
r96, single claims in r97/r99, a compound one in r100, and multi-branch decision rules in r89/r101, so a
printed total depends on how a reader individuates them: **eight under one reading, ten under another.** The
four failures are airtight one at a time, and a discipline is evidenced by its failures anyway. The reasoning
is recorded in the gate beside the pinned literal so a later round cannot "improve" it back.

### Your #4 and #16: one line telling an ML researcher what to do (p9)

The object you ask for twice already existed and had been exiled: `figure_procedure.tex`, a seven-stage
checklist that the released `audit-symbolic-benchmark` implements, was moved out of the main text in round 15
as *"largely redundant with Figure 1."* Rather than bring the figure back into a nine-page body with zero
slack, we mirrored **one line** of it into the conclusion (`conclusion.tex:6`):

> **To audit your own claim** (Figure 4): name the property, declare the invariant family that must be
> beaten, test each member *per instance*, estimate its ceiling, report the margin.

That is your spine in our vocabulary, with one addition: **test membership per instance.** Yours omits it,
and it is the step that distinguishes this from "use an invariant control"; it is why a strong baseline that
reads the property cannot enter, and it is why Table 1's last column is `×` on every row including ours. The
conclusion still ends where it did: *the audit falsifies; it certifies nothing; Table 2 is the ledger.*

Funded on p9 itself by converting takeaways (1) and (2) to positive voice, so the page is net zero lines.

### Your #3: the caveat pass is a voice conversion, and **zero caveats were removed**

**73 → 54 on the census above (−26%)**, with no caveat deleted and none relocated. Two operations only:

1. **Voice conversion**: `X is not Y, it is Z` → `X is Z`, and only where Z excludes Y on its face. *does not*
   fell 12 → 2 and `\emph{not}` 8 → 5; *never* rose 9 → 10, because a single positive *never* often replaces a
   two-clause denial. Same content, positive register.
2. **Exact restatements only.** One duplicate of *certifies nothing* went. The stance is still stated five
   times in the body and all three of its pinned forms survive verbatim and at count 1:
   `falsification tools, not certification tools` (`methodology.tex:188`), `The audit falsifies; it certifies
   nothing` (`conclusion.tex:6`), `no admissible family can turn it into a certificate` (`abstract.tex:4`).
   Counting the exact literals, the stance is stated **seven** times across the six body files.

**A sentence whose content is a refusal is not surplus prose**, and this is the constraint that shaped the
whole pass: five of the caveats a "compact Scope-of-claims paragraph" would gather up are pinned at `==1` in
our own gate *because earlier reviewers required them there.*

### Your §6: `K≥200` is now justified rather than conceded (p7)

We replaced the hedge in §4.2 with the argument, derived from the log rather than from the paper's printed
decimals:

| K | unseen classes | Tree-LSTM unseen | class-level CI95 width | strongest control's CI upper | chance |
|---|---|---|---|---|---|
| 50 | 10 | 0.8426 | **0.333** | 0.900 | 0.100 |
| 100 | 20 | 0.8818 | 0.182 | 0.875 | 0.050 |
| 200 | 40 | 0.8720 | 0.120 | 0.769 | 0.025 |
| 500 | 100 | 0.8943 | **0.066** | 0.593 | 0.010 |

The encoder is **flat across a 10× range of K** (`0.843 → 0.894`, a move of `0.05`) while the class-level
interval **narrows by more than five times that**, `0.333 → 0.066`, as the unseen pool goes 10 → 100 classes.
`K=200` is therefore where the *instrument* acquires resolution, not where the effect begins, which is what
the body now says, and it converts a caveat into a positive statement in the same edit.

**One scoping note we owe you.** There are *two* instrument-side drivers of that threshold and the body names
one. The second is that the strongest control's own interval upper bound collapses `0.900 → 0.593` as chance
falls `0.100 → 0.010`. Both are properties of the instrument at small K, so the body's account is **partial in
the conservative direction, not wrong**: naming only the encoder-side driver understates how much of the
overlap at `K=50` is the control's imprecision. The second driver is recorded in the verifier with that
reasoning rather than spent on page 7, which has zero slack. `K=1000` is deliberately not printed: its unseen
pool *falls* to 81 classes and its interval widens, which opens a question the body does not carry.

### Your §11: the easy positives, second direction (p4)

`methodology.tex:57` now closes with what the disclosure implies for **our own** positive results, not only
for the audit's validity: *"It bounds our own positives too: a pass establishes recognition of single-rewrite
equivalence."*

### Your §13: GIN/MPS turned into an argument (p9)

`experiments.tex:66` now reads: *"Neither GIN number is reproducible on MPS; the gap of `.370` is `5.7×` the
largest per-seed GIN drift measured here, `.065`."*

**This one corrected a draft of our own.** The first version quoted `±.03`, and `±.03` is the flattering
number: it is a *carried-cell* envelope from the poly8 both-protocols caption, not from the appendix the
sentence cites, and the verifier's own note at that check already warned that *"quoting only the mean would
flatter the argument."* The binding envelope is the **per-seed** `0.065` in Appendix AJ. Replaced, and pinned.

### Your §20: the two directions separated in print (p5)

Two independent reviewers have now merged them, which is the signal to fix the print rather than the reader.
`methodology.tex:84`'s `twin` entry now says both in one clause: *"admissible by a declared family's
per-instance test, never by proof of global invariance — a ceiling, though, can be (Prop. 4)."* Membership is
family-relative; the twin's **ceiling** is a deduction over *every* arrangement-invariant representation,
which is the stronger claim §1 already makes.

---

## 3. Already present, with line numbers, so you can check rather than take our word

| your ask | where it already is |
|---|---|
| #1, a sharper contribution sentence | `introduction.tex:4`, the sentence you quote back to us as the memorable one; the method is **named** *admissibility auditing* in the abstract, §1 and §2 (×2) |
| #2, the twin as centrepiece | abstract's **first** result (p1) · a titled §1 paragraph (p2) · rung 4 of Figure 1 (p3) · the **title of §4.2**, the first results subsection |
| Objection 1, the theorem is tautological | pre-conceded **and** counterweighted in place, `methodology.tex:102`: *"billed as scoping, not as theoretical contributions"* (a `==1` pinned literal) followed by what is *not* definitional: trained-readout closure (Prop. 1) and the measured non-monotone ceiling (Cor. 2) |
| the ceiling checked rather than asserted | Prop. 4 attains `sup F_3 = 0.500` at the twin; the widened family (Appendix AT); the adversarial search (Appendix BB) that **beat us** by `+0.1584` and is printed in the body |

---

## 4. Declined, each with its reason

**The nine-page restructure (#2 taken literally).** Your requested order is *problem → counterexample →
admissibility → twin*, and that **is** the current order: §4.1 is the counterexample at scale. What is true
in the complaint is that §4 starts on p7, so six of nine body pages precede the twin *experiment*. Moving a
section moves a claim out of the section its reviewer-map `\ref` names; 17 frozen map rows resolve against
those numbers, eight of them inside this round's edit zones. We spent the round on routing instead, which is
where the measurement said the loss was.

**The compact Scope-of-claims paragraph (#3 taken literally).** Five of those caveats are pinned at `==1`
**because earlier reviewers required them**, and round 40 measured that a caveat gathered away from the number
it caveats stops working. This is the **eighth consecutive round** in which a reviewer-proposed edit would
delete a predecessor's explicit requirement. We answered the register instead of the arrangement.

**Your §10's framing of two of our objects.** The untrained encoder (`0.788`) and tree-edit distance (`0.723`)
are described there as *controls*. They are **extensions**: both fail the twin's per-instance membership test
and are reported as such. If either were a control, Prop. 4 would be false: an arrangement-*sensitive*
representation cannot be pinned at `0.500`. We have not adopted that framing anywhere, and this is the second
round in which it has arisen.

---

## 5. On adoption, plainly

You are right that we cannot demonstrate adoption in a submission. What we can show is that the method, run
on published numbers, changes them in **both** directions: including upholding a leaderboard we expected to
break, and that is now on pages 1 and 2 instead of in an appendix band the paper told you to skip. Your own
suggestion for the most valuable remaining experiment (*an independent preregistered one; you partly have this
with SCAN*) is the shape of the next paper, and the SCAN row is why we think it is the right shape.

---

## 6. Verification

**93 pages · abstract ends p1 · body ends p9 · References p11 · p10's first body line is the Ethics heading**
(the canonical bistable state). Floats unmoved: Fig 1 p3 · Tab 1 p4 · Tab 2 p5 · Fig 2 p8. All 13 body
headings on their pages; §4.2 p7, §4.3/§4.4/§5 p9. 0 errors · 0 undefined references · 0 `Float too large` ·
**exactly 2** overfull boxes, both pre-existing · 0 bibtex warnings. All four gate scripts PASS with every
`--control` firing. Every rewritten `\ref` was resolved against `iclr2027_conference.aux`. Pages 1, 2, 4, 5,
6, 8, 9, 15 and 16 were read as rendered images, which is the gate that has caught the round's real defect in
twelve of the last thirteen rounds.

**`verify_claims.py` exit 0 at `2353/2353` in all three copies** (`2337 + 16`, itemised: **10** for the
K-resolution argument (all four scales present; the four unseen means; the two values the body prints at 3dp;
the `0.05` spread at the 2dp it prints; that the range really is 10×; the two interval widths at 3dp; that the
interval narrows more than 5× faster than the accuracy moves; the unseen-class counts 10→100; **the threshold
itself**) overlap at K=50/100 and separation from K=200 on, failures included; and the control's collapsing
upper bound). **1** for §4.4's `5.7×`. **5** for the preregistration census, one per failure plus the
conjunction. Every new assertion reuses an already-loaded log stem, because the verifier now checks its own
`REPRODUCE.md` index at exactly 44 tags. `statements.tex` prints `2353`.

**Three defects this round's own readiness pass caught after every gate was green**, the `±.03` above, the
withdrawn preregistration total, and one in *this document*: an earlier draft of §1 said the body had mentioned
preregistration *"exactly once — the one that failed."* It had not. §4.3 already stated a preregistered SCAN
prediction that **held**, so the sentence understated the paper and was checkable against it in ten seconds.
Corrected above; the gap the round actually closed was the *discipline*, not an instance. None of the three was
visible to any script here, and that is now the sixth consecutive round in which the last pass before "ready"
found something.
