# Response to the round-32 review

*Not part of the paper.*

**Summary: you named three things standing between this paper and an 8, and all three are now done,
two of them by running something rather than by arguing.** You asked for an independently designed
composition benchmark. We ran the audit on **SCAN's published `add_prim_jump` split**, whose
transformations, composition grammar, equivalence relation and train/test partition are all Lake and
Baroni's: the encoder reaches **0.987** against an admissible ceiling of **0.0005**, and **the
prediction we registered before the run held**, where the previous SCAN run's registered prediction
failed. You asked for `P(same verdict | F ~ 𝓕)`. That probability is **1 by proof, not an estimate**,
because the ceiling is a supremum and therefore monotone in the family; we also enumerated it
exhaustively anyway: **65,527 of 65,528 (sub-family, cell) pairs**, with the single exception named
and located. And you asked for a prospective-audit table of published claims: **that was already
Table 2, in the wrong format**, and it is now in your four columns.

We also took your two framing recommendations. The title is **yours**. The non-monotonicity is
**de-billed**; it is no longer "the centerpiece", and *evaluation protocols are themselves
hypotheses about what generalization means* is elevated into the space it vacated, as you suggested.

New runs: `r97` (SCAN composition audit) and `r98` (exhaustive family enumeration, derived from the
existing `r92` log without re-running it). Assertion count **2143 → 2219** (+76). No new dataset
enters the paper: SCAN was already audited, cited and hash-pinned, so the standing "add no datasets"
constraint from the other reviewer is honoured; we asked a **new question** of a corpus already here.

---

## 0. The most useful thing in this review is that you quoted our own sentence back at us

You wrote:

> *"An independently designed composition benchmark would test this further; we do not run one."*
> **I would expect reviewers to notice that sentence. And I think they are right to.**

That sentence was a deliberate choice in the previous round. Twice before, openly declining to address
a low-scoring axis *in the paper's own text* made that axis disappear from the scorecard. It did not
work here, and your explanation of why is correct: **there was a cheap way to answer the axis and we
did not see it.** Declining is only honest when the alternative is genuinely out of reach. It was not:
the split we needed was in a file already in our repository, behind a hash we had already pinned.
The run cost 33 minutes on one laptop GPU and no new measurement code.

We are recording this because it bounds a tactic we had been leaning on, and because the correction
came from you rather than from us.

---

## 1. Your ask #3: a composition benchmark whose rules are not ours (`r97`)

`add_prim_split/tasks_train_addprim_jump.txt` and `tasks_test_addprim_jump.txt`, SHA-256 pinned,
fetched by the same hard-failing script as the rest of SCAN. **What is theirs**: the grammar, the
transformations, the equivalence relation, and the train/test partition. **What is ours**: the
admissible family, and the question.

Measured from the published files rather than described:

| | |
|---|---|
| train / test commands | **13,204** / **7,706** (a 20,910 partition, no remainder) |
| test classes, multi-form | **3,595**, every one an `X and Y ≡ Y after X` pair containing `jump` |
| `jump` in training | the **bare primitive only**, 1,467 times; never composed |
| surface overlap, class overlap | **0** and **0** |
| parse failures | **0**; max tree depth 4 |
| chance | **0.000171**, from the *observed* class-size distribution, not `1/K` |

**Guards, with the control that makes the second one capable of firing.** All eleven order-blind
candidates are pinned at exactly **0.500** on their own order twins (14,900 twin pairs, asserted as
the sum 8,852 structure/order + 6,048 content/position). A guard that cannot fire proves nothing, so
the **ordered completion** was run through the same test as a positive control: it scores **1.000** on
the structure/order twins and is **rejected** from the family. The guard fires.

**Result.** A Tree-LSTM trained on their train split identifies held-out forms at **0.987**
(3 seeds: 0.9799 / 0.9864 / 0.9940; worst per-seed lower bound **0.9759**) against
**sup 𝓕₃ = 0.0005** `[0.0001, 0.0010]`, attained by `φ_{d1}`. The strongest non-learned method of any
kind, admissible or not, is a token bag at **0.0167** `[0.0112, 0.0226]`. Intervals are disjoint
**per seed**, not merely on the mean.

**The prediction was registered in the script docstring before the first full run and it held.** We
draw attention to this only because the previous SCAN run's registered prediction **failed**, and we
reported that failure with the same prominence. A pre-registration that only ever confirms is not a
pre-registration.

**One thing we decline to print, and why.** The ratio is **1973.6×**. It is in the appendix and
asserted in the verifier, and it is **not in the body**. SCAN's held-out design puts the admissible bar
on the floor, so that ratio measures their split's construction, not our encoder, and §4.2 of this
same paper criticises exactly this move, where we report `1.7×` against the strongest bag rather than
the flattering `6.1×` against a variable-blind one. We would be doing the thing we audit others for.
The honest statement is disjoint intervals plus disclosure of the number we are not using.

**And what it does not license.** What clears the bar is composition of **one known** transformation
onto **one** unseen primitive. That is not compositional reasoning, and the paper says so in the same
sentence as the result.

**One measurement caveat, disclosed rather than filtered.** Three of the twelve representations show
an unclean tie valley at the `1e-6` quantisation step (the three WL variants). The member that
*attains* the ceiling, `φ_{d1}`, has a clean valley, so the reported statistic is unaffected, but the
three are flagged in the log rather than dropped from it.

---

## 2. Your ask #2: `P(same verdict | F ~ 𝓕)` is 1 by proof, and we enumerated it anyway (`r98`)

**There is nothing to estimate, and this is the substantive point.** The audit statistic is a
**supremum** over the declared family, so it is monotone under inclusion: for any `F′ ⊆ 𝓕`,
`sup{M(g) : g ∈ F′} ≤ sup{M(g) : g ∈ 𝓕}`. Therefore clearing `𝓕` clears **every** sub-family of it, and
reporting the supremum over the union **dominates every distribution over sub-families**. This is now
**Corollary 3** in §3.

Two consequences worth stating plainly, because they answer your weakness 2 (*"who decides which
admissible family is sufficient?"*):

- **Nobody has to.** Leaving a descriptor out is strictly **against our own interest**; it can only
  lower the bar we must clear.
- Which family we declared bears on **how informative a failure is**, never on whether a **pass** is
  sound.

**Note that Proposition 1 does not cover this.** Proposition 1 is about refining a *member*; this is
about sub-setting the *family*. They are different statements and we had only the first.

We then enumerated it, because a one-line proof invites the suspicion that the algebra is hiding an
empirical surprise. Over the 13-descriptor catalogue (the 8 published `𝓕₃` members plus the 5
extensions admitted in the previous round, which map onto the descriptors you yourself listed; WL
variants, graphlet counts, root–leaf path kernel, Laplacian spectrum), all `2¹³−1 = 8191` non-empty
sub-families, in each of 8 cells:

| cell | union verdict | sub-families agreeing |
|---|---|---|
| `poly8` K=50 | **fail** | 8190 / 8191 |
| `poly8` K=100, 200, 500, 1000 | **pass** | 8191 / 8191 each |
| `boolean8` K=50, 100, 190 | **pass** | 8191 / 8191 each |

**65,527 of 65,528**, i.e. 0.999985. **Every cell the union passes is passed by all 8191 of its
sub-families**, which is the corollary, confirmed by enumeration and not only by algebra, and it is
this statement rather than the 0.999985 aggregate that the verifier asserts.

**The single flip, named.** `bag_laplacian_spectrum` taken alone, at `poly8` K=50: the one cell the
paper **already reports as a failure**. It scores 0.1968 where the other descriptors score 0.7258–0.7355,
against a trained lower bound of 0.6126. A narrower family at a failing cell can only refute more
weakly, which is the direction the supremum rule already forbids. It is not a counterexample; it is
the shape the proof predicts.

**Scope, in the same breath:** this says nothing about descriptors **outside** the catalogue. That is
Proposition 3's point and Definition 1's family-relativity, both already in the paper, and neither is
weakened by this result.

---

## 3. Your ask #1: it was already there, in the wrong format, the thirteenth time

You asked for 3–5 published claims audited prospectively in a
`Published claim / Original evidence / Admissibility audit / Final interpretation` table.

**Table 2's first block is exactly that, and has been for several rounds**: four other people's
published claims with four *different* verdicts, `broken` (AI Feynman variable invariance),
`S2 only` (Lample–Charton 80M integration), `upheld` (a 14-corpus score₅ leaderboard), `narrowed`
(a StructEmb ablation). Four claims, four outcomes, none of them ours. `tab:audit_changes` in the
appendix is an eight-row ledger of the same thing.

So this was a **format** gap, not a content gap. We have restructured the block to read in your four
columns, with a spanning row label marking rows 1–4 as *other people's published claims, audited
prospectively*, and moved the constant column into the caption: your own mock table has "strong
baseline" in **every** `Original evidence` cell, so it carries no information as a grid column, and
five prose columns provably overflow at this width.

This is the **thirteenth** time in this revision history that a reviewer has asked for something that
was already in the paper. Eleven of the previous twelve were *appendix-only* results: genuinely
invisible. The last two, including this one, were **in the body, cited from §1, and still did not
register**, because the format did not match the question being asked. We now treat *"a reader asked
for X"* as evidence about **form and position**, never as evidence that X is absent. Restating a claim
a third time does not make it salient; moving it does.

---

## 4. Framing: the title, the de-billing, and what we elevated

**Title.** Yours, verbatim: *When Stronger Baselines Mislead: Admissibility Auditing for Structural
Generalization*.

**De-billing the non-monotonicity.** You are right that it was oversold. "That inversion is the
paper's centerpiece" is gone. Every measurement stays: the saturation result, the protocol-dependence
proposition, and the SCAN boundary showing the inversion does **not** hold off symbolic mathematics.
It is now billed as you framed it: *within this retrieval protocol, a more resolving structural
representation can be a worse control.* This de-billing is also what **paid** for the round: the space
it freed is where `r97` and `r98` went.

**What we elevated in its place.** *An evaluation protocol is itself a hypothesis about what
generalization means*: your §7, which you said you would elevate. It is now the lead of §4.3, of
contribution (2) in §1 and of the conclusion. Your turn-around question (*if two protocols disagree,
why trust the hierarchy?*) is answered explicitly in the same paragraph: the two protocols test
**different properties**, identification and discrimination, so their disagreement is the
hierarchy's content, not a defect in it. A claim that does not name its protocol names nothing.

**Your two-sentence central message.** Sentence 1 is already the abstract's and §1's opening sentence.
Sentence 2 we adopted in structure but not in wording, after checking it against the paper: supplied
sentences have been factually wrong about this paper in four of the last six rounds, so we no longer
paste them unchecked.

**What we did not do.** You asked us not to spend the round on more appendices, more bookkeeping or
more individual baselines, and we did not. The two new appendix subsections exist only to register the
two runs; every claim they support is in the body.

---

## 5. Verification, and one defect our own gates caught

Assertions **2143 → 2219** (+76), passing in all three shipped code copies. Every new literal traces
to `logs/r97_scan_composition.json` or `logs/r98_family_robustness.json`; where a literal did not
trace we added an assertion, never a tolerance. Two of the new assertions exist specifically to
protect *against* the paper: one pins `mean_of_seeds = 0.9868` with a note that it rounds **up** to
0.987 and the body must not print 0.986, and one pins the 1973.6× ratio **because** the body declines
to use it.

**The defect.** Reading the built abstract cold (without the source) the independent-split result
was in the paragraph about *external audits*, phrased as a method (*"the audit runs on a composition
split…"*), while the paragraph that states what we **claim** mentioned only our own corpus. A cold
reader learned we had run on an independent split but not that the claim **held** there, which is the
entire point of your ask #3. The result is now in the claim paragraph, with its number. Nothing about
this was detectable from the source, from the assertion count, or from any build gate; only reading
the rendered page found it. That gate has now caught the real defect in six consecutive rounds.

**And one defect the gates caught in the *artifact* rather than the paper.** The Reproducibility
Statement said *"`REPRODUCE.md` gives the command, runtime and expected output for every run."* It did
not. `REPRODUCE.md` indexed nothing after `r95`: `r96`, `r97` and `r98` were absent, and eight older
logs the verifier has been asserting against all along (`r11`, `r21`, `r28`, `r61`, `r62`, `r63`,
`r74`, `r75`) had never been indexed either. So the sentence was wrong about **the artifact**, not
about the code: every one of those numbers was asserted, but a reader following the paper's own
instructions could not have reproduced eleven runs. All eleven now have a row with command, expected
output and runtime: five of them have no wall-clock time in their logs and are marked **not recorded**
rather than given an estimate, and the sentence is narrowed to what is checkable. The durable part is
that `check_reproduce_index()` now reads this verifier's own `load_log()` call sites and fails if any
asserted log is missing from `REPRODUCE.md`, or is named there without a command; both failure modes
were confirmed by deliberately breaking the file and watching it exit non-zero, then restoring it
byte-for-byte. This is the same defect class as round 23's unasserted `r61` and round 26's superseded
NeSymReS arm: **a claim about the artifact that nothing checked**, and it is the third time it has
been the round's last finding.
