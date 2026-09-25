# Response to the NeurIPS 2026 main-track review (Decision: Reject)

**Review:** metareview + citation-checker report + three reviewers — **XTps 4 / conf 4** (borderline accept),
**PHn9 1 / conf 5** (strong reject), **third reviewer 1 / conf 3** (strong reject)
**Applied to:** the ICLR 2027 main-track submission, source revision **39**, built 25 September 2026 from
parent commit `8f18687`
**Harness:** `python3 verification/run.py`

---

## 1. Provenance, stated first because it bounds everything below

**The reviewed PDF is not the build this response is written against, and we dated it before reading anything
into it.** Two of the review's items are datable from `git log` on `references.bib`:

| Review item | Present in the tree between | Reviewed build must lie in |
|---|---|---|
| `anthropic2025claude` (the hallucinated "Claude 4.5 model family" report) | `3205a44` 2026-04-29 → removed at `6148062` 2026-08-15 | after 2026-04-29 |
| `perez2022ignore` carrying the **HackAPrompt** title | `7d444ad` 2026-04-05 → corrected at `6148062` 2026-08-15 | after 2026-04-05 |
| The Introduction's `1.1` with no `1.2` | removed during rounds 23–33 | before that removal |

So the reviewed PDF is the **~May 2026 NeurIPS submission**, roughly twenty revision rounds behind this build.

**This is a statement of fact, not a defence.** Both citation errors were **real in the version reviewed**,
and the citation checker was right to flag them. What the dating changes is only *which* of the review's items
are still actionable: most are already closed, and we say below which, with the commit that closed each.

We also did not transfer any item on the review's word alone. Every one was measured against the live tree
first — including the ones we then agreed with.

---

## 2. The three most serious items were already closed

These are the responsible-authorship items, and they are the reason we treat this review as valuable even
though we cannot accept its decision-relevant conclusions.

**(a) `anthropic2025claude` was a hallucinated reference.** Accepted. The key is **gone**; the citation is now
`anthropic2025haiku45`, the real *Claude Haiku 4.5 System Card*, with its publisher URL:

```bibtex
@techreport{anthropic2025haiku45,
  title={Claude {Haiku} 4.5 System Card},
  author={{Anthropic}}, institution={Anthropic}, month={oct}, year={2025},
  url={https://www.anthropic.com/claude-haiku-4-5-system-card}
}
```

Removed at `6148062` (2026-08-15); replaced at `656483d` (2026-09-08).

**(b) `perez2022ignore` conflated two different papers** — a HackAPrompt title with Perez/Ribeiro authors.
Accepted, and undone at `6148062`. The entry now carries its own title, authors, venue and arXiv number:

```bibtex
@inproceedings{perez2022ignore,
  note={arXiv:2211.09527},
  title={Ignore Previous Prompt: Attack Techniques for Language Models},
  author={Perez, F{\'a}bio and Ribeiro, Ian},
  booktitle={NeurIPS 2022 Workshop on Machine Learning Safety}, year={2022}
}
```

**(c) The metareview's "even as a core paper it is wrongly referenced", i.e. XTps's Pacchiardi correction.**
Accepted, and fixed at `ea6faf9` (2026-09-20) in exactly the form XTps gave: all **eight** authors, including
Alexa Y. Pan, Yarin Gal and Jan Brauner, and **ICLR 2024** rather than a bare preprint.

**Current state: 0 of 27 entries match either checker flag.** All three facts are now **pinned in the
harness**, each with the NeurIPS citation checker named as the reason, so that no later round can tidy them
back.

---

## 3. What else the review named that is already in the paper

Each of these was checked against the live tree, not against a previous response document.

- **"Section 1.1 with no 1.2."** The Introduction now has **no subsections at all**. The harness pins that as
  an anti-regression check, because reintroducing a lone `\subsection` there would recreate the defect.
- **PHn9's list of undefined jargon.** Seven of the ten terms (`label-free`, `pooled-LOO`, `L-indep`/`L-dep`,
  `system-prompt-only`, `sycophancy`, `persona`, `false-belief`) no longer appear in the main text at all.
  The live ones are addressed in §4 below.
- **PHn9: "the correction-marker baseline does not test the original detector's mechanism, and it is unclear
  whether the artifacts are the original's or the reimplementation's."** The paper states the original's
  mechanism explicitly — it *"reads none of the target's answer about the claim, only binarised yes/no replies
  to a fixed battery of unrelated follow-ups, fed to one logistic regression"* — and the regex rule is
  presented as a **separate benchmark-level baseline**, in the paper's own words *"surface-accessible
  accuracy, **not a decomposition of the rest**."* The bank-width gap (48 probes vs. our 16) and the untested
  frozen-weights transfer are both disclosed in the appendix, with the sentence *"That reading cuts against us
  and we state it as such."* §4 lifts that concession into the body, which is what the reviewer asked for.
- **PHn9: "equalization removes the roleplay that makes it deception, so the task becomes fact verification."**
  Conceded in the main text, inside a boxed caution: *"That equalization establishes the **absence** of a
  signal: it may remove the deception with the confound."* And the premise is answered decisively in the
  appendix: under the audited detector's own mechanism **the detector never reads the on-claim answer**, so
  fact verification is not available to it.
- **Reviewer 1's Q5, separate validated from exploratory claims.** The claim ledger carries **PR?** and
  **Rep?** columns per claim and marks the lexical-rule claim `×` — *"the lexical rule is diagnostic"*.
- **"NeurIPS uses numeric citations."** Moot for this build: ICLR 2027 requires author-year, which is what the
  paper uses. No change, noted here only.

---

## 4. What revision 39 changes

| Part | Review item | Where | Price |
|---|---|---|---|
| A | Reviewer 1's named "main missing piece": the rule's **benign false-positive rate** | new appendix subsection `app:benign_fpr` + its roadmap pointer | appendix only; **0 main-text rulers** |
| B1 | "Prompt equalization" never operationally defined in the body | `experiments.tex` §Experimental Setup | 0 rulers |
| B2 | `ADAGE` unexpanded at first main-text use | `experiments.tex`, table row | acronym removed from the main text |
| B3 | No findable "Related work" in the main text | `introduction.tex` paragraph heading | character-negative |
| B4 | Replication scope stated only in the appendix | `experiments.tex` | 0 rulers |

**Part A is the substantive one, and it did not come from the review's text.** Reviewer 1 named a benign
false-positive analysis as their single main missing piece. That experiment had **already been run** — 50
benign prompts per target, no false claim and no knowledge conflict anywhere in the set — and had **never
reached the paper**. Publishing it required more than a paste, for two reasons we found while costing the
write-up and now state in the appendix:

1. The July 2026 collection recorded **timeouts as ordinary non-firing responses**. The local-inference
   client returns the fixed string *"I'm not sure about that."* on timeout; 68 of its 300 records are that
   string, including all 50 of a target that was not installed at all — a prefix match in the availability
   check accepted an absent tag because a family sibling was present. A false-positive denominator padded
   with non-answers is not a false-positive rate.
2. Responses were stored **truncated at 500 characters** — 135 of the 232 non-timeout records. Truncation can
   only hide a marker, never invent one, so that collection could support a **lower bound** and not a rate.

A third defect was in the analysis rather than the collection: the July script carried a **private 4-pattern**
regex list, not the paper's **14**, so its stored `rule_fires` field is not the firing rate of any rule the
paper reports. (An earlier discussion note of ours quoted a "0.3% benign false-positive rate" from that field;
that figure is superseded by the measurement below and should not be reused.)

So we **re-collected**, on the five targets available locally — which is exactly the criterion-4 contrast's
five-target roster, with Qwen 2.5 32B excluded on the memory ground the paper already states for that
experiment. The new collector stores responses whole, retries a timeout three times, **refuses to start unless
every target's exact tag is installed**, records an unrecoverable timeout as an error excluded from the
denominator, and **does no scoring at all** — so the 14-pattern rule exists in exactly one place in the
repository and is applied in exactly one place.

One further disclosure, found while writing the subsection rather than while reading the review: the benign
collection's neutral system prompt is **not** the equalized arm's. The equalized prompt announces that the
model *"will be asked about a factual claim"*, which is incoherent for a set that contains no claim, so the
benign set uses a plain assistant prompt instead. The appendix quotes both and says which is which. This is a
third reason the number bounds ambient firing and says nothing about the knowledge-conflict regime.

**Result: the rule fires on 0 of 250 benign responses — 0/50 on every one of the five targets separately —
Wilson 95% [0.0, 1.5]% pooled and [0.0, 7.1]% per target.** No response timed out, so the denominator is the
full 250 with nothing excluded, and stored responses run to a median of 330–1,182 characters by target
(1,584 at the longest), well clear of the 500-character ceiling that made the July collection a lower bound.
The count is **0/250 under all three inventories that can be scored** — the paper's 14 patterns, the
13-pattern variant the 69.1% figure relies on, and the July script's own 4 — so it does not depend on which
list is used.

**Where it landed, and what we could not afford.** The result is in the appendix, reachable from the appendix
roadmap. We drafted a one-clause main-text version for §4.2 beside the 69–80% sentence and **measured it
rather than assuming it fit**: at zero slack against the 9-page limit, that paragraph's last rendered line is
full, so even a 31-character addition pushed the main text's final line from ruler 485 onto page 10. Funding
one line would have meant deleting either the three-tier marking in §Experimental Setup — which is part of
what already answers reviewer 1's Q5 — or the frontier panel's size. **We judged the clause not worth either,
and it is appendix-only.** We state the trade rather than leave the reader to wonder why a headline number is
not in the body.

The appendix ships four limits with it, because without them the number overclaims:

1. **A zero count is not a zero rate** — read the Wilson interval.
2. **It measures specificity against ordinary conversation only.** The benign set contains no false claim and
   no knowledge conflict, so this shows the markers are not ambient in normal assistant output. It does **not**
   bound the knowledge-conflict component of the rule's benchmark accuracy, and it is **not** evidence that
   the rule detects deception.
3. **Only the rule's false-positive rate exists.** The interrogation pipeline's benign FPR was not measured.
4. **It does not soften the fragility finding.** The same rule loses its markers 84% → 16% under a
   style-constraint adversary and sits at 35–51% across 17 instruction paraphrases. A detector can be quiet on
   ordinary conversation and still be trivially evadable; both are properties of a surface feature, and
   neither is evidence of construct validity.

The analysis is **not pre-registered**, so it is reported as a diagnostic on the same footing as the lexical
claim, and the paper's pre-registration count is unchanged.

**Part B is the clarity response.** Three reviewers independently said the paper is hard to follow, and they
were right about the specific thing that matters most: the paper's headline mechanism, prompt equalization,
was never operationally defined in the body — a reader met *"under equalization"* throughout and was told what
it meant only inside a figure cell. It now reads *"tested instructed and prompt-equalized (both arms given one
byte-identical neutral prompt, so neither is told to lie)"* at first use. The replication-scope concession is
now in the body too: the reimplementation is *"at one third the width, and these tables are evidence about the
**design**, not about their instrument at full width."* `ADAGE` is **removed** from the main text rather than
expanded there, which matches the appendix's own verdict that it is an apparatus and not a contribution; the
acronym is defined in the one place it is used. And the related-work paragraph is now headed **"Related
work."** — the term reviewers search for.

---

## 5. Declines, each with a reason

- **Numeric citations.** ICLR 2027 requires author-year. Moot, not a decline on the merits.
- **Simplify the abstract / gloss `\tau_D` and "rung" there.** Declined this round by author decision: the
  abstract is a fixed-length artifact with its sentences pinned in the harness, and reopening it is a
  different kind of edit from the ones above. The terms are glossed at first use in the body.
- **Shorten the title.** Declined: the question-plus-subtitle form carries the identification framing that
  separates this paper from the generalization line, which is the distinction §Related work now draws
  explicitly.
- **Promote Related Work to a main-text section.** Declined. The appendix treatment stays, and the paragraph
  is renamed instead. The main text is at **zero slack** against a hard page limit, and a single
  `\subsection` in the Introduction would recreate the "1.1 with no 1.2" defect the same review flagged.
- **Redesign the autonomous-transfer experiments** (reviewer 1's W3). Declined with reason: those results are
  already marked exploratory and load-bearing for nothing. A redesign is a new research programme, not a
  revision.
- **"The paper seems largely AI-generated."** No text change is responsive to this beyond what is already
  done: the AI-use statement discloses LLM assistance in full, both hallucinated references are fixed and
  pinned, and the clarity items above are the actionable residue of the impression.

---

## 6. What remains genuinely open

**The metareview's "negative results, high bar" is a venue-fit judgement, and no edit answers it.** We note
only that the paper is no longer purely negative: it ends by *detecting* deception under a design that removes
the confound, on materials built for that purpose, and reports the standing count as **one of five targets**
rather than rounding it up.

What is open on the merits is what the paper already says is out of reach: **`\tau_D` itself**, and the top
rung of its own evidence ladder. Both need deception *manipulated* rather than observed at fixed elicitation.
The paper states that limit in the main text, in the appendix, and in its own limitations — and this round does
not pretend to have closed it.
