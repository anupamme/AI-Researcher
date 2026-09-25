# Response to the NeurIPS 2026 workshop TAE review

**Review:** Quality 3 · Clarity 3 · Significance 3 · Originality 3 · **Rating 4 (Borderline Accept)** ·
Confidence 4
**Applied to:** the ICLR 2027 main-track submission, source revision **38**, built 24 September 2026 from
parent commit `8f18687`
**Harness:** `python3 verification/run.py` → **ALL 2,877 CHECKS PASSED**

**Reading order.** §§1–7 are the **round-37** record, written against revision 37 (`ea6faf9`, 2,765 checks,
93 pages) and left as written, except for two corrections marked in place: Part D now says which table its
intervals landed on, and Part E now states W3 as a **decline with reason** rather than as the requested
experiment. **§8 is round 38**, which closes the two items round 37 left genuinely open.

---

## 1. Provenance, stated first because it bounds everything below

**This review is of an earlier, workshop-length version of the same project, not of the build it is being
applied to.** The review describes Claims **A/B/C** and **three diagnostics**. The current paper has Claims
**1–5**, **five requirements (i)–(v)**, the **ECCP** and a **five-rung epistemic ladder**, after 36 revision
rounds and at 93 pages (9 main text).

Same research, so every item in the review is measurable against this tree, and we measured all eight
against it before writing a word. **Two were already closed** (§2). **Six were open and are now
addressed** (§3). We did not reopen Claims 1–5, the five requirements, the ECCP or the ladder to match the
review's A/B/C-and-three-diagnostics structure; that structure is the workshop paper's and was superseded by
rounds 23–36. This paragraph is the only place we say so.

One number in the review we did **not** take on trust: the Pacchiardi et al. correlation range. It was
re-read out of arXiv:2309.15840 (§5.4–5.5, their Appendix D.5) before any prose was written, and only the
part that checked out was used. That verification is itself pinned in the harness (check 37c).

---

## 2. Two items were already closed, and are quoted back rather than re-answered

**W4: "the factorial is V×E, not C×E, and the T/D cell is not human-verified deception."** Correct, and the
paper already says so, in a stronger form than the review asks for. `sections/experiments.tex`: *"Crossing
truth-value with the instruction."* `sections/appendix.tex`: the T/D-vs-F/D contrast *"does **not**
establish that latent D is fixed: D is never observed"*, and *"it does not identify which of the two the
detectors read."* Changed nothing. Pinned as check **37j** so a later round cannot regress it and make this
paragraph false.

**W8: "the recommendation is broader than the evidence."** Also closed. EXP-AF's branch (b) fired and is
reported as having fired: *"no magnitude of the confound is measured outside deception"*, followed by *"no
sentence in this paper may round it up."* `sections/related_work.tex`'s group (e) applies (i)–(v) to four
adjacent constructs explicitly as **decidability, not magnitude**. Changed nothing; pinned as **37j**.

---

## 3. What this round changes: six parts, with measured prices

| Part | Review item | Where | Price |
|---|---|---|---|
| A | W1 · engage Pacchiardi §5.4–5.5 | `related_work.tex`, `app:pacchiardi` | **+21 chars**, 0 main-text rulers |
| B | W6 · name the sense of "confound" | `methodology.tex` (ECCP definition) | **+20 chars**, 0 rulers |
| C | W2 · the two open fidelity gaps | `app:pacchiardi`, `app:r1_protocol` | appendix only |
| D | W5 · claim-clustered intervals, **on the criterion-4 table only** | below `tab:crit4b_h1` + `PREREG_EXP_C4B` §12 | appendix only |
| E | W3 · the missing un-instructed test: **declined with reason**, plus a census | **EXP-XP**, new appendix subsection + table | appendix only |
| F | W7 · no code link | `main.tex` Reproducibility statement | p11, free |

**Total: appendix `+17,390` chars, `main.tex` `+576`, main-text sections `+41`.** The abstract,
introduction, experiments, discussion and conclusion are **byte-identical** to `ea6faf9` (check 37i).

### Part A: W1 is the review's most valuable item, and it is corroboration, not a concession

The reviewer is right that their §5.4–5.5 anticipated the mechanism, and right that the paper had left it
unengaged. Verified against arXiv:2309.15840: their detector's signal *"strongly correlates with the
probability that the LLM will output a lie in subsequent responses"* (**r from 0.84 to 0.96**, their
Appendix D.5), which their §5.5 reads as *"identifying a latent intention or disposition of the model to
lie"*; their §5.4 separately raises the compliance worry and bounds it **by argument**.

That is **prior work independently reaching this paper's central finding from the other direction**, and the
paper now says so. In the main line, word-neutral: *"Their own §5.5 reads that signal as a disposition to
lie (r = 0.84–0.96 with lying next), and their §5.4 bounds by argument the confound we test by
intervention."* The three "we differ" clauses were **compressed, not deleted**, which is where the words
came from; net **+21 characters**.

The appendix gives the full treatment, including what the disposition reading does **not** license: *"A
disposition correlate is still not τ_D"*, and *"it lifts neither their evaluation nor ours above rung 4."* We
gained a corroboration and did not let it inflate a claim.

### Part B: W6 was a real terminological defect

The paper used "confound" in the **design-of-experiments aliasing** sense (two effects not separately
estimable under the design) inside causal-graph language where deception is a **mediator**, while
*separately and correctly* using the common-cause sense for the residual latent U. Each usage was right; the
reader was never told which was which. A causal-inference reviewer reads the second and trips, exactly as
this one did.

Fixed at the definition site, in **+20 characters**: *"The ECCP names a benchmark-design instance of
standard pathway non-identifiability (**aliasing**, not common causation), not a new theoretical result."*
The 41 characters that paid for it came from *"stated in full in Appendix"* → *"are in Appendix"* and one
*"thus"*. The U→D / U→S common-cause sentence is byte-unchanged (check 37d), which is the point: the paper
makes both claims and now distinguishes them.

**We declined to rename the ECCP.** The stronger reading of W6 would retitle it; that is a multi-site
rewrite across pinned text in the introduction, methodology and conclusion for a gain the one-clause gloss
delivers at ~0 characters. Check 37d pins the name at all three sites so the decline stays a decline.

### Part C: W2's two remaining gaps, disclosed

Both cut against us, which is why they belong in the paper: it is this paper that insists instructed
accuracy is uninterpretable, so being exact about what its reimplementation does and does not reproduce is
on-message.

1. **Bank width, now stated.** *"Their published battery is **48** probes (24 lie-related, 10 factual, 14
   ambiguous), ours is **16** (5, 6, 5), one third of the width."* Plus what that cannot show: *"It cannot
   show that the original detector at full width would collapse by the same margin."* The ratio was
   previously invisible: we gave our 16 and never theirs.
2. **Frozen-weights transfer, now named as untested.** Every EXP-R1/R1b/R1c cell is a per-target refit;
   prior work's headline property was **one classifier fit once and transferred**. *"No cell of
   EXP-R1/R1b/R1c tests that property."* The gap is **bounded**, not open-ended: we point at the two places
   the paper does run that estimator, the transferred pipeline (50.5% and 45.0%, against 84.8%/83.0% for
   the parameter-free rule) and the leave-one-target-out battery transfer (*2 of 5 transferring, 2
   uninformative by construction, 1 genuine null*).

The pre-existing W2 disclosures are byte-unchanged and were extended, not replaced (check 37e).

### Part D: W5, on the criterion-4 table; the equalisation panel waits for round 38

**Correction to an earlier draft of this letter.** W5's sentence names *"Table 2"*, the **equalisation
panel**, `tab:r1_faithful` and `tab:r1c_v2`. This part does **not** put intervals there. It puts them on
`tab:crit4b_h1`, the **criterion-4** contrast, which is a different table answering a different question.
That half of W5 stayed open until **round 38**, which adds Wilson and claim-pair-clustered intervals to all
28 cells of both equalisation panels; see §8. Round 37's contribution to W5 is what follows, and it is the
criterion-4 half only.

The intervals are now computed and reported, and **they are wide**. That is the finding, not a problem with
it: the unit of evidence in EXP-C4B's H1 is the **paired claim (12 to 23 per target), not the 231–400
trials**, so a cluster bootstrap over claims (2,000 draws, seed 42) is the estimator the table was always
implicitly about.

95% accuracy intervals, in table order: **[0.827, 0.936] · [0.794, 0.918] · [0.525, 0.795] ·
[0.793, 0.924] · [0.692, 0.843]**. Because resampling claims moves the base rate, we also report the margin
over each cell's own majority baseline: **[+0.172, +0.400]** and **[+0.181, +0.382]** on the two replicated
positives, against **[−0.078, +0.105]**, **[−0.011, +0.095]** and **[−0.031, +0.089]** on the other three.
Family E behaves the same way.

Two things we insist on. **It is descriptive and not a second test**: the pre-registered inference remains
the within-claim permutation test, Holm-corrected within family. And **the margin excludes zero on exactly
the three cells committed as positive and on no other cell**, so the interval arm *agrees with* the
pre-registered test rather than substituting for it.

**Not one published cell moved.** `tab:crit4b_h1` and `tab:crit4b_h1_e` are asserted **byte-identical to
`ea6faf9`** (check 37f). Had a verdict, count, accuracy, p-value or MDE changed, that would have been a
defect to report, not a result to publish. The post-hoc addition is logged in `PREREG_EXP_C4B.md` **§12, the
append-only adjudication log**; the harness pins the file as differing from its last commit by exactly one
contiguous 2,300-character insertion.

To the skimming reader this makes the standing **1 of 5** look thinner. We think reporting it is the paper
doing to itself what it asks of everyone else.

### Part E · W3: a decline with reason, and the census that justifies it

**Stated plainly, because an earlier draft of this letter counted it as closed and it is not.** W3 asks that
the two audited detectors be **run** on the release's un-instructed role-play and fine-tuned-liar rollouts.
**We did not run them, and we decline to.** What we ran instead is EXP-XP, a census of what the release can
express, and the census is the reason for the decline, not a substitute for the experiment.

**The reason.** The role-play design's `label` equals **the row's index parity in every row of all three
files**, so D is recoverable without reading any text: requirement (ii) fails by definition and (v) with it.
Under the only item key the release provides, **0 items carry both outcomes**; under a hand-supplied
adjacent-pair key, **0 of the 69 pairs shares a byte-identical prompt**: the honest cell drops the reward
sentences *and* flips the fact, so the release's un-instructed design **still varies the elicitation between
the two cells it contrasts**. That is the same aliasing the paper is about, in a design that never issues an
instruction to lie. A detection score on such a design would be uninterpretable for exactly the reason this
paper argues, so reporting one would undercut the argument it was meant to support.

**What the decline does not license.** Requirement (iv) *does* hold (the channel is transcript plus
per-probe logprob differences), so the detectors *could* be scored there, and the obstacle is
interpretability, not access. And a negative census is not a negative finding about the corpus:
`sections/appendix.tex` states that *"a negative census does not say the release contains no deception."*
A reviewer who disagrees with this judgment is disagreeing with a stated reason, which is the point of
writing it down.

The reviewer named the gap correctly: the paper audits `pacchiardi2024catch`, declines their
code and data, then runs its criterion-4 census over **Apollo's** release and **Liars' Bench**, never over
the audit target's own. The census below closes that gap.

Pre-registered as `docs/PREREG_EXP_XP.md`, the **17th** such file, frozen with its requirement predicates,
eligibility gates, verdict rule and **all five reporting branches** before the census script existed. The
release is pinned by commit (`c5689fa`, 19 June 2024), fetched to a git-ignored directory, and committed as
a sha256 manifest; a public repository is still not ours to redistribute. **No model call, no detector fit,
no network access after the fetch.**

**Disclosed up front: this arm is exploratory by construction.** A feasibility gate ran before the
pre-registration existed, to decide whether an experiment was possible at all, so the structural facts were
seen before the decision rule was frozen. That is recorded as the pre-registration's DEVIATION 1 and travels
with every number. What the pre-registration buys is that the branches were fixed in advance, not that the
material was unseen.

**Result: the release contains three designs, which the paper previously scored as one row, and no design
supplies all five. Claim 4 survives a test it had not faced.**

| Design | (i) | (ii) | (iii) | (iv) | (v) | Verdict |
|---|---|---|---|---|---|---|
| Prompted instructed lying (the design we audit) | ✗ | ✗ | *undec.* | *undec.* | ✗ | inapplicable |
| Instrumental role-play, **un-instructed** | ✗ | ✗ | ✗ | ✓ | ✗ | inapplicable |
| **Fine-tuned liars**, the strongest near-miss | ✓ | ✗ | ✓ | ✓ | ✗ | inapplicable |

What decided them, all mechanical: the instructed design ships as a **200-cell rate table over 11 datasets
and 26 instruction texts** with no rollout, prompt or response text at all, and (iii)/(iv) are recorded
**UNDECIDABLE_FROM_RELEASE**, a first-class verdict, never rounded to ✗. The role-play design's `label`
equals **the row's index parity in every row of all three files** (138 rollouts), so D is recoverable
without reading any text. The fine-tuned design has **1,109 byte-identical prompts across the two
conditions**, hashed over the whole prompt and never over a system message, so (i) and (iii) hold, but D is
which file the row came from, i.e. the fine-tuning target.

**What we decline to claim, having measured it.** Branch 3 licensed calling the near-miss *"closer to
criterion 4 than any Apollo set"* **only if the numbers said so. They do not**: Apollo's on-policy
insider-trading corpus clears (i)–(iv) and fails only (v), while the fine-tuned design clears three of five.
So the reported statement is the weaker true one: strongest near-miss **within the audit target's own
release**. The harness pins that the superlative appears **only** inside the sentence that declines it
(check 37g).

Branch 2's split test returned **no split**: all three verdicts agree, and the branch was conditioned on
their differing, so `tab:prior_work_criteria`'s single row is not split, and the per-design patterns (0, 1
and 3 requirements cleared) are reported in the appendix instead. Branch 5 did not fire: the script's
re-derivation agreed with the gate's hand measurement on both structural facts.

One incidental finding, reported because it corroborates a separate appendix claim from a second source:
each role-play rollout carries its elicitation battery as per-probe logprob differences, with group widths
**24 / 14 / 10 = 48** under the release's own field names, matching the count Part C attributes to their
published battery.

### Part F · W7: an availability statement, no URL

The paper forward-referenced "the code" at eight or more sites and named no release. One sentence now sits
in the Reproducibility statement naming **what** will be released: codebase, raw transcripts, per-trial
result files, a table-reproduction script, the **17 pre-registrations** (each frozen before its analysis code
existed, each with an append-only deviations log), the per-experiment analysis scripts, the committed result
files, the citation-verification script, and the **2,765-check verification harness**.

**No URL**: the anonymized repository does not exist yet, and inventing one would be worse than the gap.
The harness asserts the sentence carries no `http`, no `github`, no author name, and that **none of it
renders inside pages 1–9** (check 37h), so it is free.

---

## 4. Declines, each with its receipt

- **Running the two detectors on the release's un-instructed rollouts (W3)**: the role-play design fails
  requirements (i) and (ii); its `label` is the row's index parity, and no pair of contrasted cells shares a
  prompt. A score there measures the design, not detection. Receipt: Part E and `sections/appendix.tex`'s
  census.
- **Renaming the ECCP to an aliasing term**: multi-site rewrite across pinned text in three sections;
  Part B's gloss delivers the precision at +20 characters.
- **A main-text CI table**: page slack is exactly 0, and Part D's intervals belong beside the table they
  qualify.
- **Compressing EXP-AD for space**: standing decision from an earlier round; it stays at 12 rendered lines.
- **Abstract edits**: 403 words with 10 of 13 sentences and 7 numeric tokens pinned; untouched this round.
- **Restructuring to A/B/C-and-three-diagnostics**: that is the workshop paper's structure (§1).

## 5. Carried-forward bounds, unchanged

The generality claim is still bounded, *"the magnitude we measure only for behavioral deception
detection"*; EXP-AF's branch (b) still fired, so **no magnitude is measured outside deception**; EXP-C4B's
H1 still stands at **1 of 5** targets; and the whole paper still stops at **rung 4, not rung 5**: τ_D needs
D manipulated, and nothing in this round changes that. EXP-XP does not move it either: a design clearing all
five would have reached rung 4, as ours does.

## 6. Verification

| Property | Value |
|---|---|
| Harness | **2,765 checks, all passing** (`verification/run.py`) |
| Verifier regeneration | byte-identical on a second run of `mk_verify_r37.py` |
| Build | exit 0 · **0 Overfull** · 107 Underfull (pinned) · 0 `undefined` · `main.blg warning$ -- 0` |
| Pages | **93** (89 + 4 appendix pages; main text still ends on p9) |
| Page budget | p9 last ruler **485**, p10 first ruler **486**, Ethics statement opens p10 |
| Main-text float pins | all **5** unmoved (`fig:dag` p2, `tab:claim_ledger` p5, `fig:ladder` p5, `fig:r1c_collapse` p7, `tab:external_audit` p8) |
| Float pins overall | 225 labels (223 + EXP-XP's 2); **103 appendix pins repaginated**, each by a pinned delta; 120 unmoved; none with a main-text page |
| Byte-identical to `ea6faf9` | abstract, introduction, experiments, discussion, conclusion; `tab:crit4b_h1`; `tab:crit4b_h1_e` |
| Pre-registrations | **17**; the 16 predecessors byte-identical, `PREREG_EXP_C4B.md` additions-only in §12 |
| Structured cautions | **3** `\fbox{\parbox}`, all retained |
| Punctuation | no em dash in any new prose; no sentence with two grammatical colons; no clauseless semicolon |

Three checks were **strengthened** rather than updated: the code-repo cleanliness checks now name an
explicit seven-path allow-set (the old form accepted *any* untracked file), and the float-pin check now
carries 103 exact page deltas plus the assertion that **no** label whose page was inside the main text moved
at all.

## 7. Honest assessment

**Part A is the real gain**: an unengaged attack surface became independent prior corroboration of the
paper's central mechanism, at 21 characters. **Part D is the real risk and the right risk**: wide intervals
on 12–23 claims are the honest denominator. **Part E is the only item that could have moved Significance**,
and it was gated on someone else's release; the gate opened far enough to run a census, and the census came
back negative, which extends claim 4 rather than narrowing it. **Parts B, C and F are correctness and
reproducibility hygiene**: no score moves on any one of them, but each closes something a careful reviewer
would name.

**Still out of reach, and stated as such in the paper:** the ECCP's magnitude outside deception (EXP-AF
branch (b) fired; no pinned corpus supplies it), and τ_D / rung 5, which needs D manipulated.

---

# 8. Round 38: the two items round 37 left open

**Applied to:** source revision **38**, built 24 September 2026 from parent commit `8f18687`
**Harness:** **ALL 2,877 CHECKS PASSED** · **94 pages** (93 + 1) · main text still ends p9

We re-audited this review against the live tree item by item rather than against §§1–7, on the principle
that a response letter is not evidence about a paper. Six of the eight items were closed, one is the decline
now stated as such in Part E, and **two were genuinely open**. This round is those two and nothing else.
The abstract, introduction, methodology, experiments, discussion, conclusion and related-work sections are
**byte-identical to `8f18687`**; `appendix.tex` grew by **7,149 characters** and `main.tex` by zero.

## 8.1 Part A · W5's actual sentence: intervals on the equalisation panel

The reviewer's *"Table 2"* is `tab:r1_faithful` (EXP-R1, v1 bank) and `tab:r1c_v2` (EXP-R1c, v2 bank). Both
reported a point accuracy, a cell size and an exact permutation p, and **no interval on any cell**; the
headline **97.0% → 43.3%** carried none either. Both now carry two, in prose under each table rather than as
a ninth column: both tables are already 8 columns at `\small`, and a CI column goes Overfull.

**Two estimators, and the paper says which is which.** *Wilson 95%* on the out-of-fold correct counts, which
is the interval the rest of the paper reports for an accuracy, so it is the **comparable** one. And a
**claim-pair cluster bootstrap** (2,000 draws, seed 42), because Wilson's exchangeability assumption is false
here and measurably so: each cell's 50 trials come from **25 matched claim pairs**, two rows apiece, which is
why the v2 panel carries a grouped-5-fold column at all. That one is the **honest** one.

**The pooled pairs, which is where the evidence is:**

| Panel | Instructed | Equalised | Nearest-edge gap |
|---|---|---|---|
| v1 (`tab:r1_faithful`, n=300) | **[76.9, 85.6]** | **[48.0, 59.2]** | **17.7 pp** |
| v2 (`tab:r1c_v2`, n=300) | **[94.4, 98.4]** | **[37.8, 49.0]** | **45.4 pp** |

At n=50 a Wilson half-width is about **14 pp**, so **no single equalised cell is individually decisive** and
the pooled pair is where the claim lives: two intervals that do not approach one another, not two point
estimates. Per cell, the intervals **agree with the pre-registered permutation verdicts cell for cell**: in
v1 exactly one instructed interval contains chance (Qwen 2.5 7B, the target the experiment already reports as
never separating its conditions) and exactly one equalised interval excludes it (Qwen 2.5 14B, the exception
EXP-R1b was pre-registered to test); in v2 all six instructed intervals exclude chance and five of six
equalised intervals contain it.

**The sixth, and why the estimator matters.** Llama 3.2 3B's v2 equalised Wilson interval is
**[14.3, 37.4]**, and it excludes chance *from below*, which read alone would suggest inverted
discrimination. The clustered
interval on the same cell is **[34.0, 70.0]** and contains chance. The clustered intervals are on the
**`grp-5f`** column and not on the primary, and **that is forced rather than chosen**: resampling pairs with
replacement duplicates rows, and under stratified folds a duplicated row is trained on and then scored. We
measured that leakage in a first pass: it inflated every draw far enough that an interval failed to contain
its own point estimate, and the grouped estimator is the only one a cluster bootstrap can be run on here.
**Across all 28 cells of both panels, every clustered interval contains its grouped point estimate**, which
is a standing assertion in the emitted result file, not a remark.

**What computing the intervals turned up, reported because it cuts against us.** All **24 per-target cells
recompute to their published literals exactly**. The four **pooled** cells do so only when the six targets
are stacked in the order the publishing script pooled them (alphabetical by checkpoint filename), and
stacking them in the order the tables *print* their rows gives **80.3% and 49.3%** on v1 and **96.7% and
44.3%** on v2 from the same rows under the same estimator. The cause is not an unfixed seed but
`StratifiedKFold(shuffle=True, random_state=0)`, whose fold assignment is a function of a row's position in
the stacked matrix. **Every one of those four swings, 0.3 to 4.3 pp, lies inside the Wilson interval for its
own cell**, which is precisely the argument for printing an interval. **No per-target cell moves, no
permutation p moves, no change-in-pp moves and no verdict moves**, and the collapse survives either ordering
with the instructed and equalised intervals still disjoint. We report it as a precision disclosure rather
than a correction.

**Status:** descriptive and post-hoc, labelled as such in the paper. The pre-registered inference for both
experiments remains the label-permutation test already printed in the tables, and **no frozen
pre-registration was edited**. The arm is `experiments/analyze_r1_intervals.py`: no model call, no network,
and it **asserts every cell's point accuracy equals its published table literal before emitting any
interval**; a mismatch exits non-zero, because that would be a defect rather than a result. It also pins the
six-target roster explicitly, because the upstream `r1b_fresh_*` glob now also matches `ministral-3:8b`, an
EXP-R1d target collected after this panel was published, whose inclusion would silently give n=350.

## 8.2 Part B · W4's second half: a T/D deception grade, prepared but not coded

The reviewer asked that annotators label the T/D cell's outputs deceptive-or-not. **No grade of D exists for
any response in T/D or F/D**, and that is now stated in the paper rather than left as an inference from the
non-identifiability claim. What the paper had was the *argument*: both cells are defined by the instruction
issued, compliance is inferred from it, and the "compliance is graded rather than binary" statement is read
off corrective leakage in the detector's own features, **not** off any per-response judgment.

**The sheet is built and released; the codes are empty.** `make_factorial_coding_sheet.py` emits **144
items**, 12 per (target, cell) at seed 42, globally shuffled, as a CSV carrying only the claim and the
response, with the item-to-condition key in a **separate file**. Withheld from the coder: the target's
identity, the cell, and every detector-side field (refusal count, probe vector), because those are the
detector's reading of the response and not the response.

**Why all four cells and not just T/D against F/D.** Within {T/D, F/D} the deception instruction is
**constant**, so blinding on it would be vacuous; and truth-value cannot be blinded at all from a coder who
knows that water boils at 100°C. Interleaving the two **honest** cells in is what hides the thing that
matters (*whether a deception instruction was issued*), and it supplies the control rate a T/D rate needs.
**The blind is measured, not merely designed:** a keyword sweep over all 144 responses for instruction or
pretence language returns **one** hit, and it is the phrase *"genetic instructions"*.

**This part deliberately stops short of a number.** Hand-coding is the protocol's own method, and
substituting a machine grade would be the exact failure this paper names as construct recovery, in the one
place it would matter most. So **no rate from the sheet is reported**, and the harness pins that, gated on
the key's `coded: false` flag, so the pin releases if and when the sheet is actually coded rather than
turning red. If it comes back coded, Krippendorff's α on the D-binary axis runs through the existing
reliability script and the T/D deceptive share becomes a measurement instead of a declaration.

## 8.3 Verification

| Property | Value |
|---|---|
| Harness | **2,877 checks, all passing**; **111** are new |
| Retained | every check the round-37 harness scores against this tree (**2,766**) is retained; the 10 that this round deliberately changes are updated in the generator with the round-38 reason, none deleted |
| Verifier regeneration | byte-identical on a second run of `mk_verify_r38.py` |
| Build | exit 0 · **0 Overfull** · 107 Underfull · 0 `undefined` · `main.blg warning$ -- 0` |
| Pages | **94** (93 + 1, all appendix) |
| Page budget | p9 last ruler **485**, p10 first ruler **486**, Ethics statement opens p10, inspected in the render |
| Main-text float pins | all **5** unmoved and byte-identical to `c9718cf` |
| Labels | **225**, unchanged; round 38 adds no label (all five new paragraphs are `\paragraph{}`) |
| Appendix repagination | 103 moved pins, each by a recorded delta; 120 unmoved; **no** label whose page was in the main text moved |
| Part A integrity | all **28** printed intervals re-derived from the committed result file and compared string-for-string; **both table bodies byte-identical to `8f18687`** |
| Part B integrity | 144 rows, four cells present, **0 codes populated**, 0 target-name leaks, longest same-cell run ≤ 8 |
| Unchanged | **3** `\fbox{\parbox}`; 5 main-text floats; abstract untouched; **42** three-hyphen runs and **0** em dashes; all 17 pre-registrations byte-identical |

**One arithmetic note, because it looks like a discrepancy and is not.** The round-37 harness scores
**2,766** against this tree, not the 2,765 it scored against its own. The extra check is real and it passes:
check 11 raises one check per appendix sentence naming a post-panel model, and Part A's roster-pin sentence
names `ministral-3:8b`. We diagnosed that by instrumenting a throwaway copy of the round-37 verifier to
record every check's call site and diffing the two multisets, rather than assuming. **2,766 + 111 = 2,877**,
and `main.tex`'s advertised count and the check that pins it moved together.

## 8.4 Honest assessment of round 38

**Part A is small, unambiguously right, and it helps.** It answers the review's most concrete sentence, and
once stated as intervals the collapse reads *stronger*, not weaker: 17.7 pp and 45.4 pp of clear air at the
pooled level. It also cost us a disclosure we would not otherwise have found: the pooled digit carries up to
4.3 pp of row-order noise, which is the kind of thing computing an interval is supposed to surface.

**Part B cannot be finished by us, and that is the correct outcome.** What it delivers unilaterally is a
disclosure the paper's own argument wanted and lacked, plus a ready-to-code sheet. A response letter claiming
a human-verified T/D rate we had generated ourselves would be worth less than the admission that none exists.

**After this round the review's substance is addressed**, the one exception being the W3 detector run, which
is declined on a stated and checkable ground (Part E). The items still standing are the two the paper argues
are out of reach on principle: the ECCP's magnitude outside deception, and τ_D / rung 5.
