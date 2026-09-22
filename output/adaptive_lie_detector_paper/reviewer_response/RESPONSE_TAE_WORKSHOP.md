# Response to the NeurIPS 2026 workshop TAE review

**Review:** Quality 3 · Clarity 3 · Significance 3 · Originality 3 · **Rating 4 (Borderline Accept)** ·
Confidence 4
**Applied to:** the ICLR 2027 main-track submission, source revision **37**, built 22 September 2026 from
parent commit `ea6faf9`
**Harness:** `python3 verification/run.py` → **ALL 2,765 CHECKS PASSED**

---

## 1. Provenance, stated first because it bounds everything below

**This review is of an earlier, workshop-length version of the same project, not of the build it is being
applied to.** The review describes Claims **A/B/C** and **three diagnostics**. The current paper has Claims
**1–5**, **five requirements (i)–(v)**, the **ECCP** and a **five-rung epistemic ladder**, after 36 revision
rounds and at 93 pages (9 main text).

Same research, so every item in the review is measurable against this tree — and we measured all eight
against it before writing a word. **Two were already closed** (§2). **Six were open and are now
addressed** (§3). We did not reopen Claims 1–5, the five requirements, the ECCP or the ladder to match the
review's A/B/C-and-three-diagnostics structure; that structure is the workshop paper's and was superseded by
rounds 23–36. This paragraph is the only place we say so.

One number in the review we did **not** take on trust: the Pacchiardi et al. correlation range. It was
re-read out of arXiv:2309.15840 (§5.4–5.5, their Appendix D.5) before any prose was written, and only the
part that checked out was used. That verification is itself pinned in the harness (check 37c).

---

## 2. Two items were already closed, and are quoted back rather than re-answered

**W4 — "the factorial is V×E, not C×E, and the T/D cell is not human-verified deception."** Correct, and the
paper already says so, in a stronger form than the review asks for. `sections/experiments.tex`: *"Crossing
truth-value with the instruction."* `sections/appendix.tex`: the T/D-vs-F/D contrast *"does **not**
establish that latent D is fixed: D is never observed"*, and *"it does not identify which of the two the
detectors read."* Changed nothing. Pinned as check **37j** so a later round cannot regress it and make this
paragraph false.

**W8 — "the recommendation is broader than the evidence."** Also closed. EXP-AF's branch (b) fired and is
reported as having fired: *"no magnitude of the confound is measured outside deception"*, followed by *"no
sentence in this paper may round it up."* `sections/related_work.tex`'s group (e) applies (i)–(v) to four
adjacent constructs explicitly as **decidability, not magnitude**. Changed nothing; pinned as **37j**.

---

## 3. What this round changes — six parts, with measured prices

| Part | Review item | Where | Price |
|---|---|---|---|
| A | W1 · engage Pacchiardi §5.4–5.5 | `related_work.tex`, `app:pacchiardi` | **+21 chars**, 0 main-text rulers |
| B | W6 · name the sense of "confound" | `methodology.tex` (ECCP definition) | **+20 chars**, 0 rulers |
| C | W2 · the two open fidelity gaps | `app:pacchiardi`, `app:r1_protocol` | appendix only |
| D | W5 · claim-clustered intervals | below `tab:crit4b_h1` + `PREREG_EXP_C4B` §12 | appendix only |
| E | W3 · the missing un-instructed test | **EXP-XP**, new appendix subsection + table | appendix only |
| F | W7 · no code link | `main.tex` Reproducibility statement | p11, free |

**Total: appendix `+17,390` chars, `main.tex` `+576`, main-text sections `+41`.** The abstract,
introduction, experiments, discussion and conclusion are **byte-identical** to `ea6faf9` (check 37i).

### Part A — W1 is the review's most valuable item, and it is corroboration, not a concession

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
disposition correlate is still not τ_D"* — *"it lifts neither their evaluation nor ours above rung 4."* We
gained a corroboration and did not let it inflate a claim.

### Part B — W6 was a real terminological defect

The paper used "confound" in the **design-of-experiments aliasing** sense (two effects not separately
estimable under the design) inside causal-graph language where deception is a **mediator** — while
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

### Part C — W2's two remaining gaps, disclosed

Both cut against us, which is why they belong in the paper: it is this paper that insists instructed
accuracy is uninterpretable, so being exact about what its reimplementation does and does not reproduce is
on-message.

1. **Bank width, now stated.** *"Their published battery is **48** probes (24 lie-related, 10 factual, 14
   ambiguous), ours is **16** (5, 6, 5), one third of the width."* Plus what that cannot show: *"It cannot
   show that the original detector at full width would collapse by the same margin."* The ratio was
   previously invisible — we gave our 16 and never theirs.
2. **Frozen-weights transfer, now named as untested.** Every EXP-R1/R1b/R1c cell is a per-target refit;
   prior work's headline property was **one classifier fit once and transferred**. *"No cell of
   EXP-R1/R1b/R1c tests that property."* The gap is **bounded**, not open-ended: we point at the two places
   the paper does run that estimator — the transferred pipeline (50.5% and 45.0%, against 84.8%/83.0% for
   the parameter-free rule) and the leave-one-target-out battery transfer (*2 of 5 transferring, 2
   uninformative by construction, 1 genuine null*).

The pre-existing W2 disclosures are byte-unchanged and were extended, not replaced (check 37e).

### Part D — W5, and this is the round's honest risk

The intervals are now computed and reported, and **they are wide**. That is the finding, not a problem with
it: the unit of evidence in EXP-C4B's H1 is the **paired claim — 12 to 23 per target — not the 231–400
trials**, so a cluster bootstrap over claims (2,000 draws, seed 42) is the estimator the table was always
implicitly about.

95% accuracy intervals, in table order: **[0.827, 0.936] · [0.794, 0.918] · [0.525, 0.795] ·
[0.793, 0.924] · [0.692, 0.843]**. Because resampling claims moves the base rate, we also report the margin
over each cell's own majority baseline: **[+0.172, +0.400]** and **[+0.181, +0.382]** on the two replicated
positives, against **[−0.078, +0.105]**, **[−0.011, +0.095]** and **[−0.031, +0.089]** on the other three.
Family E behaves the same way.

Two things we insist on. **It is descriptive and not a second test** — the pre-registered inference remains
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

### Part E — W3: EXP-XP, the only genuine experiment in this round

The reviewer named the missing experiment correctly: the paper audits `pacchiardi2024catch`, declines their
code and data, then runs its criterion-4 census over **Apollo's** release and **Liars' Bench** — never over
the audit target's own. We ran it.

Pre-registered as `docs/PREREG_EXP_XP.md`, the **17th** such file, frozen with its requirement predicates,
eligibility gates, verdict rule and **all five reporting branches** before the census script existed. The
release is pinned by commit (`c5689fa`, 19 June 2024), fetched to a git-ignored directory, and committed as
a sha256 manifest — a public repository is still not ours to redistribute. **No model call, no detector fit,
no network access after the fetch.**

**Disclosed up front: this arm is exploratory by construction.** A feasibility gate ran before the
pre-registration existed, to decide whether an experiment was possible at all, so the structural facts were
seen before the decision rule was frozen. That is recorded as the pre-registration's DEVIATION 1 and travels
with every number. What the pre-registration buys is that the branches were fixed in advance — not that the
material was unseen.

**Result: the release contains three designs, which the paper previously scored as one row, and no design
supplies all five. Claim 4 survives a test it had not faced.**

| Design | (i) | (ii) | (iii) | (iv) | (v) | Verdict |
|---|---|---|---|---|---|---|
| Prompted instructed lying (the design we audit) | ✗ | ✗ | *undec.* | *undec.* | ✗ | inapplicable |
| Instrumental role-play, **un-instructed** | ✗ | ✗ | ✗ | ✓ | ✗ | inapplicable |
| **Fine-tuned liars** — the strongest near-miss | ✓ | ✗ | ✓ | ✓ | ✗ | inapplicable |

What decided them, all mechanical: the instructed design ships as a **200-cell rate table over 11 datasets
and 26 instruction texts** with no rollout, prompt or response text at all — and (iii)/(iv) are recorded
**UNDECIDABLE_FROM_RELEASE**, a first-class verdict, never rounded to ✗. The role-play design's `label`
equals **the row's index parity in every row of all three files** (138 rollouts), so D is recoverable
without reading any text. The fine-tuned design has **1,109 byte-identical prompts across the two
conditions**, hashed over the whole prompt and never over a system message, so (i) and (iii) hold — but D is
which file the row came from, i.e. the fine-tuning target.

**What we decline to claim, having measured it.** Branch 3 licensed calling the near-miss *"closer to
criterion 4 than any Apollo set"* **only if the numbers said so. They do not** — Apollo's on-policy
insider-trading corpus clears (i)–(iv) and fails only (v), while the fine-tuned design clears three of five.
So the reported statement is the weaker true one: strongest near-miss **within the audit target's own
release**. The harness pins that the superlative appears **only** inside the sentence that declines it
(check 37g).

Branch 2's split test returned **no split** — all three verdicts agree, and the branch was conditioned on
their differing — so `tab:prior_work_criteria`'s single row is not split, and the per-design patterns (0, 1
and 3 requirements cleared) are reported in the appendix instead. Branch 5 did not fire: the script's
re-derivation agreed with the gate's hand measurement on both structural facts.

One incidental finding, reported because it corroborates a separate appendix claim from a second source:
each role-play rollout carries its elicitation battery as per-probe logprob differences, with group widths
**24 / 14 / 10 = 48** under the release's own field names — matching the count Part C attributes to their
published battery.

### Part F — W7: an availability statement, no URL

The paper forward-referenced "the code" at eight or more sites and named no release. One sentence now sits
in the Reproducibility statement naming **what** will be released: codebase, raw transcripts, per-trial
result files, a table-reproduction script, the **17 pre-registrations** (each frozen before its analysis code
existed, each with an append-only deviations log), the per-experiment analysis scripts, the committed result
files, the citation-verification script, and the **2,765-check verification harness**.

**No URL** — the anonymized repository does not exist yet, and inventing one would be worse than the gap.
The harness asserts the sentence carries no `http`, no `github`, no author name, and that **none of it
renders inside pages 1–9** (check 37h), so it is free.

---

## 4. Declines, each with its receipt

- **Renaming the ECCP to an aliasing term** — multi-site rewrite across pinned text in three sections;
  Part B's gloss delivers the precision at +20 characters.
- **A main-text CI table** — page slack is exactly 0, and Part D's intervals belong beside the table they
  qualify.
- **Compressing EXP-AD for space** — standing decision from an earlier round; it stays at 12 rendered lines.
- **Abstract edits** — 403 words with 10 of 13 sentences and 7 numeric tokens pinned; untouched this round.
- **Restructuring to A/B/C-and-three-diagnostics** — that is the workshop paper's structure (§1).

## 5. Carried-forward bounds, unchanged

The generality claim is still bounded — *"the magnitude we measure only for behavioral deception
detection"*; EXP-AF's branch (b) still fired, so **no magnitude is measured outside deception**; EXP-C4B's
H1 still stands at **1 of 5** targets; and the whole paper still stops at **rung 4, not rung 5** — τ_D needs
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

**Part A is the real gain** — an unengaged attack surface became independent prior corroboration of the
paper's central mechanism, at 21 characters. **Part D is the real risk and the right risk**: wide intervals
on 12–23 claims are the honest denominator. **Part E is the only item that could have moved Significance**,
and it was gated on someone else's release; the gate opened far enough to run a census, and the census came
back negative, which extends claim 4 rather than narrowing it. **Parts B, C and F are correctness and
reproducibility hygiene** — no score moves on any one of them, but each closes something a careful reviewer
would name.

**Still out of reach, and stated as such in the paper:** the ECCP's magnitude outside deception (EXP-AF
branch (b) fired; no pinned corpus supplies it), and τ_D / rung 5, which needs D manipulated.
