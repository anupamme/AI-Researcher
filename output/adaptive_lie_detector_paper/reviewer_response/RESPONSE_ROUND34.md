# Response to Reviewer (7/10, Weak Accept, confidence High) — the length round

Thank you, and thank you in particular for the sentence that made this round easy to plan:

> *"My biggest remaining concern is presentation rather than science: there is an excellent ~8-page paper
> buried inside a 90-page research audit."*

paired with *"I would not add another 10 experiments."* We took both literally. **This round ran no
experiment, added no pre-registration, and changed no number anywhere in the paper.** What it did is make
the document smaller — **91 pages → 89**, with the appendix **6,748 characters** shorter — and label the
novelty claim you said you had to hunt for. Everything below is measured, including the three edits we
withdrew after pricing them.

Two things come first, because they change which of your items are still actionable.

---

## §0. Provenance: you read round 31. Rounds 32, 33 and 34 are all invisible to your report.

Stated as **information, not rebuttal**. Your report names `main(20260919-020957).pdf`, and your §11 also
cites `main(20260918-111203).pdf`.

| Timestamp in your report | = IST | The tree it is |
|---|---|---|
| `20260919-020957` = 02:09:57 UTC | **07:39:57** | **round 31.** Commit `3d2805e` landed at **07:40:08** — **eleven seconds later** |
| `20260918-111203` = 11:12:03 UTC | **16:42:03** | **round 29** (`a239ad2`, 16:37:31) |

The heads you did **not** see:

- **`79d39b6`** — *"Round 32: name the two validity distinctions, and the inferential unit"* (09:02:56)
- **`225f069`** — *"Round 33: the clarity round — rung tags, an executable ladder, two numberings named
  apart"* (10:39:53)
- **round 34**, this reply.

**Round 33 in particular already landed three of the items your §25 lists as open**, because the previous
reviewer asked for the same things in different words. The table in §C below gives the sites. We are not
claiming credit for having anticipated you; we are telling you where to look so you do not re-request
work that exists.

---

## §A. The length receipt, then the length reduction

### A.0 — your diagnosis is right about the document and wrong about the location

**Main text: 9 pages. Front/back matter (ethics, reproducibility, references): 4. Appendix: 76.** You are
correct that the artifact reads as ~90 pages. But your §25.4 names five specific things to *"move out of
the main text"*, and **every one of them is already appendix-resident**. The `\ref` traffic, counted
mechanically:

| Your §25.4 item | mentions in main text | mentions in appendix |
|---|---|---|
| the recency check | **0** | 8 |
| pre-registration deviations | **0** | 12 |
| model-vintage discussion | **1** (a bare `\ref`) | 11 |
| EXP-IB (intervention B) | 2 | 9 |
| Krippendorff / rater reliability | 1 | 6 |
| EXP-R1d by name | **0** | 6 |

**There is nothing left to move out of the main text.** So the only lever that moves your actual
complaint is the appendix, and that is where this round spent itself.

### A.1 — what we cut, and what it bought

| Cut | Where | chars |
|---|---|---|
| **Illustrative interrogation transcripts** — two subsections collapse into **one**, keeping the single transcript that carries an analytic point | `app:transcripts` | **−4,374** |
| **A4's reader's-guide signpost** — an *addition*, §A.4 below | `app:criteria_taxonomy` preamble | **+472** |
| **The other 39 enumerated edits** — `Lie Mode`/`Truth Mode`/`API Configuration` demoted from subsections to two `\paragraph`s; 21 results-only condensations (per-model instructed and equalized detail, feature correlation, leave-one-model-out, enhanced zero-shot, hedging on instructed data, multi-turn, human baseline, machine-rater ICC, the four self-labelled *Exploratory: Not Load-Bearing* blocks); the criterion-5 transfer block; *Future Directions*; `app:adage_details` made canonical for B4 | 39 blocks | −2,807 |
| **Enumerated total** | | **−6,709** |
| Blank-line normalization outside the enumerated blocks | | −39 |
| **Measured file delta** | `sections/appendix.tex` 386,189 → 379,441 | **−6,748 → 91 pp. to 89 pp.** |

**The rule for every condensation was: keep the table or its headline figures, delete the walk-through
prose.** No number left the paper. The verifier pins 18 of them individually (83.9, 76.3, 91.4, 82.8,
74.7, 89.9, 75.0, 10.2, 68.5, 0.83, 35.0, 26.0, 54.0, 0.327, 57.6, 0.0045, 93.9, 1.61) precisely so that
"condensed" cannot quietly become "lost".

### A.2 — we owe you an honest correction on the size of this

**Our own plan mis-priced this round, and we are reporting the measured number rather than the planned
one.** The plan was built off a scan that found *"32 blocks, 76,216 characters, referenced by no
main-text `\ref` and pinned by no verifier check"* and promised **~12 pages**. Re-measuring that set block
by block showed it is **dominated by pre-registered material** — EXP-XL (15,986), EXP-XJ (9,520), EXP-IT2
(6,890), and the pre-registered 4th and 5th scenario blocks plus the pre-registered 2×2 factorial (8,698
together) — which is unreferenced only because pre-registrations are cited by experiment ID, not by `\ref`. Deleting it would be an integrity problem,
not a length win. **The honest reduction is two pages, not twelve, and that is what landed.**

Three further measurements, for the record, because they explain why two pages is the number:

- **The appendix is dense, not padded.** Measured on the rebuilt PDF, pp. 14–89: mean **4,407 characters
  per page**, sparsest page **2,721**, and **zero** `\clearpage`/`\newpage`. The float-spacing lever is
  already spent —
  `main.tex` has carried tightened `\abovecaptionskip` and `\textfloatsep` since an earlier round.
- **Diminishing returns, measured not asserted.** The three successive condensation batches returned
  **−237**, **−914** and **−297** characters. We stopped when the fourth pass stopped paying.
- **Your own §17 told us where to stop**, and we are quoting it back as the reason: the reproducibility
  material is *stronger than the narrative needs*. Being stronger than necessary is not the same as being
  padding, and we did not treat it as such.

### A.3 — what we refused to cut, and why

Pinned in the verifier so a later round's length pressure cannot quietly take them:

- **EXP-R1d**, the recency check — **pre-registered, attempted, paid for, and reported inconclusive**
  (three of four targets void on the pre-registered probe-channel gate; *"One target is not a panel"*, so
  the pre-registration's own fewer-than-two rule applies and no recency claim enters the paper). A prior
  reviewer asked for it. **Reporting a paid-for pre-registered null is a strength, and deleting it to buy
  a page would be the exact behavior this paper criticizes.**
- **EXP-XJ and EXP-IT2** — named as tokens in Table 2's rows and load-bearing for requirements (iv) and
  (v).
- **The pre-registered 4th and 5th scenario blocks and the pre-registered 2×2 factorial**, and all **16**
  `docs/PREREG_EXP_*.md` files, which are frozen by standing constraint.
- **The mock-transcript block**, which we had listed for deletion and kept: the appendix roadmap's bucket 4
  and the experiment summary table both `\ref` it, and its own section title already warns the reader —
  *"Mock Transcripts; Not Predictive of Real-Model Performance."*
- **Future Directions**, condensed rather than deleted, with **item numbering (1)–(12) preserved** because
  two paragraphs elsewhere cite item **(7)** by number.
- **The three `\fbox{\parbox}` caution boxes.** Standing decline: every reviewer who has commented on them
  has called them a strength, and they are the first thing a length cut reaches for.

### A.4 — your §10, answered directly: the appendix now tells you which four sections matter

> *"Why am I still reading 50 pages of increasingly specialized diagnostics?"*

The reader's guide now opens with a ranking, one entry per link of §2.2's load-bearing chain:

> **If you read four appendices, read these**, one per link of §2.2's chain: **identification** (A),
> **equalization** (U.2), **criterion 4 on a public release** (AB), **criterion 4 on materials built for
> it** (X). **Those four carry the argument**; the rest is a robustness check on one of them or is marked
> exploratory in its own section title.

The appendix roadmap's caption carries the same four, so the paragraph and the table cannot drift apart.
**Four sections out of 76 pages.** If that ranking is right, your *"excellent ~8-page paper"* is now
9 pages plus four named appendix sections, and the audit trail is explicitly labelled as audit trail.

---

## §B. The main-text edits: four landed, three withdrawn, every price measured

Context you should have, because it governed the round: **the main text is 9 pages at a hard 9-page limit
with slack exactly 0.** It ends on p9 at margin ruler **485**, and 485 *is* the last ruler on the page. In
this layout an addition upstream of the spill costs about one line per line, while an upstream **cut
refunds nothing at all**. So each edit below had to be funded from inside §3.4/§3.5/Conclusion, or not
made.

### B1 — your §25.1, the biggest 7→8 lever you name · `introduction.tex` · **+22 chars, 0 lines**

Your complaint was that you had to *find* the novelty claim. It existed, unlabelled, mid-paragraph inside
Contribution 2. It now reads:

> **What is new.** **The novelty is not the observation that confounding exists; it is turning a
> previously implicit causal-validity requirement into an auditor-executable protocol and showing that
> existing behavioral deception benchmarks fail it in empirically distinct ways.**

**The sentence is byte-unchanged** — it is pinned verbatim by an earlier round's must-fix — and the label
is the entire edit.

### B2 — your §12 · `experiments.tex` · **self-funding**

Your §12 calls *"scaling does not rescue construct validity"* a powerful message and does not notice it is
already a **Proposition corollary** at `methodology.tex:25`. §3.4's frontier sentence now names it:

> Frontier scale: rule 80–90%, pipeline 40–56% (EXP-FS) — **scale moves the numbers, not the verdict**,
> which is the Corollary of §2.1.

### B3 — **withdrawn after measurement.** Your §11's vintage-independence, promoted into the main text · measured at **+224, then +162, then +67 characters — all three spilled the document to p10**

The §2.1 Corollary paragraph sits on a line boundary, so **+67 characters there is a new page.** We
measured it three times and reverted to byte-identical. **The canonical statement stays where it is** —
`appendix.tex:680`, *"**Identification is vintage-independent.** … **The magnitudes are vintage-dependent,
and are claims about these targets only**"* — and the verifier now pins its presence there, so what we
lost is placement, not content. **This is the edit we would land first given ten more lines.**

### B4 — the funding cut · `experiments.tex` · **−215 chars**

We cut §3.4's *"**ADAGE is an apparatus, not a contribution**, reproducing §3.2 under neutral prompts and
cross-family re-extraction"* — a secondary detector analysis inside the spilling region, which is exactly
what your §25.4 authorizes moving out. **The fact is not dropped**: `app:adage_details` now bolds it and
says so in its own words (*"and this paragraph is where the paper says so"*), and the verifier's two
pre-existing checks on that span were **retargeted to the appendix rather than deleted**. Two details we
checked rather than assumed: `fig:feature_collapse` had **exactly one** `\ref` in the whole main text,
inside the clause we cut, so a pointer was kept or the figure would float uncited; and our first rewrite
opened a sentence with *"EXP-A/EXP-G reproduce…"*, which the retained style suite correctly flagged — we
fixed the prose, not the check.

### B5 — **withdrawn after measurement.** Your §25.3's consistent strength vocabulary in Table 1 · measured at **+6 characters = one reflowed row = one spilled page**

We drafted *"Replicated: accuracy is regime-dependent"* / *"Diagnostic: no learned features"* for claims 2
and 3. **Six characters** into that column reflows a row in an already-tight table and pushes the
Conclusion onto p10. Our own plan's rule was *"if it reflows, skip it"*, so it was skipped. **The verdicts
are already there in bold** — *Instructed accuracy is regime-dependent*, *No learned features needed* —
what you asked for is the consistent two-word prefix, and that is what cost a page.

### B6 — **declined, with receipts.** Your §26's abstract transition

The abstract is ratcheted at **403 words** (non-Scope body 383, Scope sentence 20) with **10 of its 13
sentences pinned verbatim** by earlier rounds' must-fixes — one of them promoted *into* the abstract at a
prior reviewer's explicit request. Any edit must be word-neutral, and a transition rewrite is not. **We
declined rather than deferred**, and the verifier pins the sentence you targeted so a later round does not
quietly relitigate it.

---

## §C. Already closed in rounds 32–33 — do not re-request; here are the sites

| Your item | Where it already is |
|---|---|
| §25.3 / clarity #3: *"tell the reader every experiment moves the evidence one rung"* | **round 33**: all four §3 subsection titles carry a rung tag — *Rung 1 to 2*, *Rung 2 to 3*, *Rung 2 to 3 Again*, *Rung 3 to 4*. The table of contents reads as the ladder |
| §25B: the protocol *"executable in ~10 lines"* | **round 33**: Figure 2's middle column is numbered **1–5** and the caption instructs *"run steps 1–5 bottom-up and report the highest rung reached"* |
| clarity #1: one short repeatable anchor | **round 33**: *"the problem is identification, not classification"* in Figure 1's caption title and at the end of Figure 3's caption |
| §14's conflation of criterion 5 with annotation leakage | **round 33** named the two schemes apart at the collision point: *"**Criteria 1–5 and requirements (i)–(v) are different lists**"*. Criterion 5 is **cross-target transfer**; annotation leakage and circularity are **(iv)** and **(v)** |
| §6: predictive vs. attributional validity | **round 32**, `introduction.tex:61` + the p3 comparison table |
| §13: construct vs. instrument validity | **round 32**, `methodology.tex:78` |
| §21-adjacent multiplicity | **round 32**: the inferential unit is **target × claim-pair**; "thousands of trials" reduces to **12–23 paired claims per target** |
| §25.5: make criterion 4 psychologically smaller | **round 31**, `conclusion.tex:4` — *"(4)–(5) as a weaker, target-dependent secondary finding"* |
| §12's theoretical half | `methodology.tex:25`, **Corollary (scale does not help)** — *"No increase in accuracy, model scale, or detector sophistication resolves this"* |
| §19's ASCII DAG, §25.2's ordering | §2.1 is already in your requested order (plain → notation → estimands → ECCP → Proposition), and `fig:dag` already draws both your panels, including *"(A) move D, hold E = criterion 4"* |
| §13's three "don't claim" items | all three explicitly disclaimed in `methodology.tex:83`'s *Does not establish* list |
| §5 / §26's surface-accessibility distinction | already the abstract's own words: *"a parameter-free lexical rule reaches 69–80% — surface-accessible accuracy, not a decomposition of the detector's signal"* |
| §11's vintage statement | `appendix.tex:680` (see B3) |

---

## §D. Where you and previous reviewers disagree. We are showing these, not resolving them quietly.

**D1 — your §11 asks us to compress the vintage discussion; a previous reviewer's *"these are old
models"* objection is what created it.** We kept it and left it in the appendix, which is the compromise
that costs neither of you anything — but you should know the block exists because someone asked for it.

**D2 — your §25.5 agrees with our standing decline against a previous reviewer.** You want criterion 4
made psychologically smaller; they wanted it elevated. We had already taken your side in round 31
(`conclusion.tex:4`). Recording the agreement because it is the one place your report *resolves* a
conflict rather than adding to it.

**D3 — your §17 concedes the reproducibility material is stronger than the narrative needs.** We treat
that as the boundary of the length round, not as permission to thin it. That sentence is the reason A1/A2
stopped at −6,748 characters instead of hunting for more.

---

## §E. Declines, each with its price

- **E1 — your §16's *"the paper is doing too much"* as a structural split into Papers A/B/C.** That is a
  different submission, not a revision.
- **E2 — new experiments implied anywhere in §25.** Declined **on your own instruction**.
- **E3 — B3** (vintage-independence in the main text): **+67 chars = one page.** Content survives in the
  appendix.
- **E4 — B5** (Table 1's strength prefixes): **+6 chars = one reflowed row = one page.**
- **E5 — B6** (the abstract transition): the **403-word ratchet**, 10 of 13 sentences pinned.
- **E6 — standing declines carried forward:** the title (user decision); the ladder remaining Figure 2
  rather than moving earlier; `tab:criteria` remaining in Appendix A.

---

## §F. Carried-forward disclosures — restated, not dropped

- **Generality stays bounded, and we say why rather than claiming otherwise.** §2.1: *"outside deception
  the precondition is thus decidable and decided; **the magnitude is measured only for deception**."*
  EXP-AF decides the ECCP precondition on **28** pinned public corpora but measures no effect size outside
  deception. **Measuring one such magnitude is the single change that would move both your novelty 7 and
  your generality 7 — and it is a new experiment.**
- **The non-English pilot** (*n* = 50, Spanish or Mandarin) is named, scoped and **unrun**. Materials are
  English-only.
- **EXP-C4B's −30.3 / −28.7 pp surface-rule deltas remain appendix-only.**
- **`tab:frontier_panel`**: 50.5% is the same-family sensitivity, 49.5% the cross-family primary.
- **This paper reaches rung 4, not rung 5**, and says so in the abstract, Figure 2, Table 1's claim 5, and
  the §2.2 box.

---

## Verification

`latexmk` exits **0** with **0 overfull boxes**, **0 undefined references**, `main.blg` reporting
`warning$ -- 0`, and no `??` or `[?]` in the rendered text. The page count is **89**, pinned as an
equality in both directions. Main text still ends on **p9 at ruler 485** with the Ethics Statement opening
p10 at 486. All **5 main-text float pins** are byte-identical to their committed pages (`fig:dag` 1/p2,
`tab:claim_ledger` 1/p5, `fig:ladder` 2/p5, `fig:r1c_collapse` 3/p7, `tab:external_audit` 2/p8).

The regression suite is at **2,082 checks, all passing**: **1,820 retained** from round 33, of which
**12 were *updated*** with the round-34 reason recorded in a comment — never deleted — plus **262 new**.

Two things about the update discipline are worth naming, because they are what makes a deletion round
auditable:

1. **Every appendix float pin was re-measured from the rebuilt `main.aux`, not assumed.** Ten pins: four
   unchanged, six repaged, and **every float NUMBER unchanged**. That is the control — A1/A2 deleted
   prose, never a float, so a number change would have meant a table was dropped to buy length. Three
   floats move *backward* by a page (p68→p67, p70→p69, p41→p40), which is the deletion showing up exactly
   where the deletions are.
2. **The 44 edits of this round are enumerated in a machine-generated ledger** and replayed against the
   round-33 baseline, with the 42 appendix entries pinned in both directions: post-image present exactly
   once, **pre-image absent**. A word that disappears without an enumerated edit fails the suite.

---

## What we think this round is worth, stated plainly

- **Your own heading caps this route at 8**, and we are not going to claim past it: *"What would move my
  score from 7 → **8**."* We landed your §25.1 in full, your §10 and §12 in full, your §25.4's
  authorization used as funding, and a **measured** two-page reduction.
- **We are reporting two pages, not the twelve our plan promised**, and the reason is in §A.2: the
  cuttable-looking mass was pre-registered material. We would rather hand you a smaller honest number than
  a larger one obtained by deleting a pre-registered null.
- **The residual gap is novelty and generality, and both are evidence-shaped, not presentation-shaped.**
  Your novelty 7 is bounded by *"the underlying causal principle is standard"* — that is an evidence
  objection, and no amount of rewriting closes it. The experiment that would is named in §F, and it is not
  in this round because your report told us not to run one.
- **Realistic landing: 7.5, with 8 credible if you credit the novelty label and the length reduction.**
