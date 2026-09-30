# Response to the review (round 13)

*Not part of the paper. Structured in the reviewer's own §22 priority order.*

The review's diagnosis is accepted in full: **Clarity 6.5 is the binding score, and no new
experiment is what this round needed.** We ran none. Every change below is presentational, and the
verifier count is **unchanged at 1717/1717 by design**, nothing in this round touched a claim, a
number, or a protocol. `verify_claims.py` exits 0 with 1717/1717 in all three shipped copies.

## Three items were already answered before the review was written

The reviewed PDF is stamped `20260903-154033`. Run `r89` (leave-one-primitive-out) completed at
16:35 and is Appendix AQ, which the review never cites, so three of its asks are answered by text
that already exists rather than by a change:

| Review item | Where it already is |
|---|---|
| **§7 / §19.4**: "four primitives is still an important weakness; add one genuinely harder composition experiment" | This is `r89`, already run and in **Appendix AQ**. Holding a primitive **out of the library entirely** costs $+0.535$ pooled at $d{=}4$ (**an order of magnitude more** than never having *composed* ($+0.079$)) dropping the encoder onto its untrained control while its flatness in depth survives. It also **refuted both pre-registered predictions**, and the assertions are written in the refuting direction. The abstract's Finding 3 and §4.3 now carry this contrast in one clause each. |
| **§10**: "state the causal claim more carefully" | §4.4 already reads, verbatim: *"under this leave-one-schema-out intervention, including the generating schema in the training library **causally changes** identification accuracy, structural distance held exactly fixed — not a correlate of how far the held-out form is."* That is the review's own formulation. |
| **§11**: "structure the conclusion as what we establish / what we don't" | §5 already reads *"**Established**: … **Not established**: …"* as a single paragraph. We did **not** convert it to bullets: it costs ~3 rendered lines at a 9-page limit for no content gain, and three earlier reviewers credited the block as written. |

## 🔴 Must-do (their items 1–7): all seven done

| # | Ask | What changed |
|---|---|---|
| 1 | Rewrite the abstract as Problem → Method → 3 Findings → Scope | **Done, rewritten end to end.** Five paragraphs: problem; method and criterion; `Finding 1: a held-out-form score can be a lookup task`; `Finding 2: one architecture survives the criterion`; `Finding 3: what generalizes is library coverage, not composition`; `What we do not claim`. The $M(\phi_d)$ machinery is **gone from the abstract**, replaced by its plain-English form: *"a stronger baseline is not necessarily a stronger control"*, and stated in full at §1 instead. Three-decimal numbers **10 → 5**. Labels are inline `\textbf{}`, not `\paragraph{}`, because `\paragraph` headings here spill the abstract onto page 2. |
| 2 | **Add a running symbolic example** *(their highest-value ask)* | **Done, and it is their example.** New §3.3 paragraph *"One example, walked up all four tiers"*: the class of $x{+}y$ containing $y{+}x$, $(x{+}0){+}y$, $y{+}(x{+}0)$, walked up tiers 1→4, tier 1 identifies nothing *here* but solves a benchmark whose classes have unique variable sets; tier 2 sees the identity insertion as $\{+\}$ vs $\{+,+\}$; tier 3 is order-blind by construction, so $x{+}y$ and $y{+}x$ are **identical** to every $\phi_d$, *which is why $\phi_d$ can falsify an order claim and never support one*; tier 4 is left with the one thing none of them can do. We deliberately do **not** call $x{+}y$/$y{+}x$ a twin pair: the twin construction swaps siblings under a *non-commutative* operator. |
| 3 | Move Table 2 immediately after Figure 1 | **Moved one page earlier, to the top of §3: now page 5, beside Definition 1 and the boxed contract.** Not literal adjacency: that would put the entitlements float ahead of Table 1 in float order and **renumber both**, and three review rounds now refer to "Table 1 = what the audit changes". Verified from the built PDF: Figure 1 p3, Table 1 p4 (still numbered 1), Table 2 p5 (still numbered 2), Table 3 p8. §1 now points at it inline. |
| 4 | Explain the audit intuitively before the formal definitions | **Done, one sentence before Proposition 1**: *"In one sentence: if a method that provably cannot see $P$ scores as well as your model, your model's score is not evidence that it sees $P$."* We did not add a second box: the paper already has one, and a competing box costs ~4 lines. |
| 5 | Replace "$\mathcal{F}_3$-complete" with "passes the $\mathcal{F}_3$ audit" | **Done at every site: 7 now read "passes the $\mathcal{F}_3$ audit", 0 read "$\mathcal{F}_3$-complete".** The defining line is now *"we say a result **passes the $\mathcal{F}_3$ audit** … it never means exhaustive structural completeness"*, which keeps round 11's requirement that the family travel in the name. The last appendix instance of "$\mathcal{F}_3$-completeness" is renamed too. |
| 6 | Turn the experiment subsections into question headings | **Done, all four**: `4.1 Can a Held-Out-Form Score Be Solved Without Reading Structure? (AI Feynman)`, `4.2 How Widespread Is That? A 23-Corpus Audit`, `4.3 Does Clearing Every Bag Make a Score Evidence of Composition?`, `4.4 Is the OOD Axis the One the Protocol Names?` Each renders on **one** line; `Finding N` is kept in the abstract so the mapping question → finding stays explicit. |
| 7 | Break the long multi-clause sentences | **Done at the eight worst offenders** in §1 and §4, the em-dash chains at `experiments.tex` :18, :60, :62, :69 and `introduction.tex` :4, :8 are now split at sentence boundaries. Split **sentences, not paragraphs**: a paragraph break costs a rendered line at a hard 9-page limit, a sentence break costs none. One genuine grammar defect surfaced doing this (*"$\Delta$plain is $+0.061$ — and to $+0.054$…"*) and is fixed. |

## 🟠 Strongly recommended (their items 8–12)

| # | Ask | What changed |
|---|---|---|
| 8 | **Demote Proposition 3 to the appendix** | **Done, and this is what funded the whole round.** The `Resolution–retrieval tradeoff` statement now sits in Appendix AN beside its own proof (page 59). Proposition counters are global, so it still **prints as Proposition 3** at all 10 citing sites with `??` = 0. What replaces it in §3.3 is the measurement, which is the reviewer's point: *"What carries the argument is not a theorem but the measurement: $M(\phi_d)$ is non-monotone on **three corpora, two algebras and both protocols**."* |
| 9 | Reduce notation in the narrative | **Done.** The narrative now carries only $M$, $\phi_d$, $\mathcal{F}_3$. The $C_t$/$g_t$/$P_t$ triple is gone from the prose, replaced by the skyline statement in words, which also makes **"skyline" the recurring metaphor** (their §3). Removing them left Definition 1 referring to symbols no longer introduced, so **Definition 1 is now self-contained in prose**: *"Let $\mathcal{F}_t$ be a set of representations each determined by the cues at tiers ${\leq}t$ alone, and hence invariant to the structure those cues do not determine."* |
| 10 | Plain-English takeaway before Table 3 | **Done, and it replaces the self-referential phrasing the review's §20 flags**: *"In plain terms: the encoder generalises to rewrite **orders** and **depths** it never saw, and does not generalise to a rewrite it never saw."* Table 3's caption now opens `The central experiment:` instead of the paper describing its own object. |
| 11 | Conclusion as "what we establish / what we don't" | **Already exact**; see the table above. Unchanged deliberately. |
| 12 | Compress the appendix revision history into a 4-row table | **Done.** Appendix F now opens with **Table 11**, four rows (`incident | what was wrong | how it was found | what is in the paper now`) covering the r17 phantom number, the r20 vacuous held-out, the r26 deduplication gap and the zero-triplet-loss misreading. The per-run detail stays below it, and the paragraphs the table subsumes are cut to a row pointer. |

## 🟢 Nice-to-have (their items 13–15)

| # | Ask | What changed |
|---|---|---|
| 13 | One-line glossary | **Done**, folded into the running example rather than added as a float: *"a **cue** is information a form carries; a **skyline** is a non-learned method that keeps one tier's cue and discards everything above it; a **twin** is a non-equivalent form matched on every lower-tier cue; and **coverage** asks whether a held-out form's generating rewrite was in the training library."* |
| 14 | Question-based headings replacing "Finding 1/2/3" | Item 6. Questions in §4; `Finding N` retained in the abstract, per the review's own §6-vs-§14 tension. |
| 15 | Remove self-referential "the paper's…" phrases | **Done: 0 remain in the main text** (the three the review names are gone). The only surviving instances are in appendix prose and one LaTeX comment. |

## Also in this round

- **Title, their §21 Option A, adopted**: *When Does Held-Out-Form Generalization Test Structure? A Falsification Framework for Neuro-Symbolic Benchmarks.*
- **Their §4 reframe**: the audit is now described as *"23 corpora spanning four benchmark families"*. The concessive clause stays (*"the breadth is over corpora, not over benchmark families: 15 of the 23 are EQNET variants"*), because that honesty is the point of the sentence.
- **Their §10, inference hierarchy and multiple testing**, added to §3.4: *"the class (equation) is the primary unit, so every interval we report is a class-level bootstrap, while seeds quantify training stochasticity only; and inferential claims are restricted to the prespecified primary contrasts, so the exploratory appendix tests are descriptive."*
- **Their §16, the negative result**: §4.2 states it plainly, in its own sentence: *"The screen is a diagnostic, never a difficulty predictor: across 12 corpora no separability statistic predicts untrained-encoder accuracy."* The sentence-breaking of item 7 leaves it standing alone rather than buried in a chain.
- **Their §18**: §2's encoder-list clause, which restated §3.2 verbatim, is cut to its citations; the AI-assistant disclosure's third paragraph is compressed to two sentences.

## What we did not do, and why

- **No new experiment.** The review asked for none and said so twice; `r89` already covers §7/§19.4.
- **No bulleted conclusion** (item 11) and **no second principle box** (item 4): both cost rendered
  lines at a hard limit for no content gain.
- **Table 2 is not literally adjacent to Figure 1** (item 3), for the renumbering reason above.

## Build state

Main text **exactly 9 pages**: page 10 carries zero main-text lines before the Ethics heading, the
round-12 baseline position, and the abstract still ends on page 1 with §1 starting on page 2. 65
pages total (the appendix grew by one page: Table 11). 0 LaTeX errors, 0 unresolved references, 0
`Float too large`, **one** overfull hbox (the pre-existing 3.509 pt), 0 bibtex warnings, one benign
`TS1/ptm/m/sc` font warning. `verify_claims.py`: **1717/1717, exit 0, in all three copies**; the
count is unchanged because no claim was touched, which is the intended signal for a
presentation-only round.
