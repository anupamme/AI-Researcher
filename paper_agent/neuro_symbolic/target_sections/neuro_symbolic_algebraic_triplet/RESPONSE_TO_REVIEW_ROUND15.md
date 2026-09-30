# Response to review: round 15

**Summary: no new experiments.** The review says twice (§19, §20) that the bottleneck is conceptual
novelty and presentation, not experiment count, and asks for *one* additional conceptual leap rather
than more benchmarks. This round adds no run, no corpus and no log. The verifier count is **unchanged
at 1742/1742**, which is the mechanical proof of that: `verify_claims.py` never reads the `.tex`, so a
round that added a measurement would have moved it. Round 14's entry recorded *why the count moved*;
this one records why it did not.

**Main text is still exactly 9 pages**, `E THICS S TATEMENT` back at index 7 of page 10.

---

## §5 and §17: the four-tier hierarchy is not a clean hierarchy. **Agreed, and changed.**

This was the sharpest criticism in the review and we have taken it in full. The paper had already
conceded the point in a trailing sentence (*"Tiers 1–3 are invariances; coverage is different in
kind"*), which was exactly the problem: a category distinction stated as an afterthought to a
structure that contradicted it.

- The three **representational** levels are now **S1 / S2 / S3**.
- Training-library coverage is **gate C**, and is no longer a level. §3.3 states plainly that S1–S3
  are invariances a representation does or does not have, while coverage is a property of the
  train/test split, so stacking them would be a category error.
- **Definition 1 is split into two conditions**: *control-complete through level S$T$* ($T\le3$) and
  *coverage-gated*, stated apart because they are different in kind. Proposition 2 now licenses "no
  claim beyond S$T$ — and none about coverage at all, which only gate C addresses."
- **Figure 1 draws gate C off the ladder**, below a dashed rule, so the structure is visible without
  prose.
- The trailing concession sentence is deleted, because the structure now carries it.

**One deviation from the reviewer's proposed naming, for a reason we think they will accept.** The
review suggests S1/S2/S3; the paper already used $\mathcal{S}$ for the *structural stress tests*
($\phi_\infty$, tree-edit distance, the untrained encoder): the set deliberately **outside** the
criterion. Shipping both would collide on the same letter. We renamed that set to **$\mathcal{X}$
(extensions)**, which is the word the text was already using for $\phi_\infty$ ("a strictly stronger
*extension*, not a member"). $\mathcal{F}_1,\mathcal{F}_2,\mathcal{F}_3$ are unchanged, so no
mathematics moved.

The appendix is renamed to match. **Log keys, verifier keys and run tags were deliberately left
alone**; they are data, and renaming them would invalidate byte-level assertions that currently
pass. Appendix AR and `REPRODUCE.md` now carry the exact mapping (`tier2_operator_arity_bag` is level
S2, and so on).

## §6 and §20: "Proposition 1 is nearly tautological" and the novelty sentence. **Answered directly.**

The review names the rejection argument it wants made impossible: *"a careful application and
synthesis of known ideas ... conceptual novelty insufficient for main track."* Two changes.

**(1) The claim is now on page 2**, opening the contributions paragraph, in the review's own terms:

> What is new is not that controls detect shortcuts. It is that the standard abstraction — *did the
> model beat a baseline* — is the wrong one: a valid control must be **invariant** to the property
> claimed, and because control strength is **non-monotone** in resolution, an evaluation must quantify
> over a **family** rather than over any single baseline, however strong.

Related Work's opening sentence, which said the same thing on page 3, is deleted rather than
duplicated.

**(2) §18's Option C is done: a general proposition, protocol-free.** See below.

## §18 Option C: generalize the supremum result. **Done, as a new proposition.**

The review asks to prove that *"given a nested family of invariant representations, the appropriate
audit statistic is the supremum over the family, rather than the score of its maximally resolving
member"*, and to make it general rather than tied to our retrieval construction.

**New Proposition 3 (the admissibility ceiling), in the main text, proved in Appendix AN:**

> For a family $\mathcal{F}_t$ whose membership *requires* invariance to the structure level $t$'s
> cues do not determine, refining any member either preserves that invariance — leaving it in the
> family, where the supremum already dominates it — or destroys it, forfeiting membership. Hence the
> supremum is the audit statistic, and no member, in particular not the most resolving one, can stand
> in for it.

It assumes **no protocol, no retrieval construction and nothing about $\phi_d$**; it follows from the
invariance requirement in Definition 1 alone. Corollary 2 is re-derived from it rather than from the
old retrieval-specific proposition, which is what makes Definition 1 independent of that construction.

**We want to flag the obvious risk ourselves rather than have it found.** This proposition is *shallow*;
it follows from the definition, and §6's complaint was precisely that Proposition 1 is nearly
tautological. Answering that with a second near-tautology would be no answer. Our position is that a
general statement of this kind is worth stating **only because the corresponding measurement is
non-obvious and already in the paper**: $M(\phi_d)$ is measured non-monotone in $d$ on three corpora,
two algebras and both protocols, and again externally on a corpus we did not build. The proposition
says the ceiling exists for any invariant family; the measurement says it binds here, at a *coarse*
member, which is the counter-intuitive part. We have kept the two adjacent throughout and never ship
one without the other.

**This also resolves a standing disagreement between reviewers rather than reopening it.** Round 13
asked us to demote the retrieval-specific Proposition to the appendix; round 15 asks for stronger
control-family theory. The new proposition takes over that Proposition's role inside Definition 1,
which lets it **stay demoted** in Appendix AN as the *measured* mechanism. Nothing was re-promoted.

## §14: a figure that gives a reviewer the whole paper. **Done, and merged with the relabel.**

Figure 1 is rebuilt. Rather than a separate 4-panel empirical figure, each **level carries the
exemplar result that settles it**, which delivers the review's request and makes the S1/S2/S3 + gate C
structure visible in the same image:

| | System | Result | Verdict |
|---|---|---|---|
| **S1** | AI Feynman | variable bag `1.000` vs Tree-LSTM `0.972` | **fails**: a lookup by construction |
| **S2** | Lample–Charton 80M | operator/arity bag `0.941` vs `0.872` | **fails**: correctly; labels *are* operator-defined |
| **S3** | EQNET `poly8` | Tree-LSTM `0.894` vs token bag `0.517` vs $\sup\mathcal{F}_3$ `0.277` | **clears** |
| **gate C** | leave-one-schema-out | $\Delta$plain `+0.061`, $\Delta$renamed `+0.054` | the axis that actually moves |

Every number was already in the paper. The old panel (B), the procedure column, moved to the appendix
as Figure 3: once each rung states its own verdict the two were largely redundant, and that is part
of what paid for the new content.

## §7: too much "we caught our own mistakes". **Compressed in the main text; the record stays.**

Table 1 previously ran **four rows of our own claims against two external ones**, which is a large part
of why the paper reads as "framework plus our demonstration". It now runs **four external rows to
two**, at the same row count:

- AI Feynman: **broken** at S1
- the $\mathrm{score}_5$ leaderboard (EqNet, SemEmb), 14 corpora: **upheld**
- the StructEmb ablation, 14 corpora, **narrowed**: an *untrained* encoder reaches it on 5
- Lample–Charton 80M: **broken** at S2
- our poly8 and composition claims: **restated** (compressed from two rows)
- our depth curve and chance level: **narrowed** and **corrected**, both against us (compressed from two)

§1's self-audit paragraph is compressed to a single clause and merged into the preceding paragraph.
The full incident record stays in the appendix, unchanged.

## §9: the external audit is less useful than we think. **Agreed; narrative space cut.**

§4.5 is trimmed and now bills the result explicitly as **"a portability result, not a debunking."**
We removed the sentence that framed it as a verdict about the benchmark.

## §10: breadth rhetoric. **Done.** Every load-bearing mention now reads "23 corpora spanning four
benchmark families, **15 of them EQNET variants**": abstract, §1 and §4.2, so a reviewer meets the
concession in the same sentence as the claim rather than discovering it afterwards.

## §11: name the scope of the composition result. **Done.** §4.3 now names the phenomenon
**composition-of-known-transformations generalization**, stating that every primitive composed was
individually trained on.

## §12: bring boolean8 forward. **Done.** It already had a main-text paragraph; the problem was that
it read as a trailing clause. Its paragraph heading now leads with it: *"A different algebra:
`boolean8` clears the criterion harder and breaks the coverage story."*

## §8: the token-bag / JL account is over-claimed. **Weakened, and its scope moved to the front.**

The account is appendix-only, and its validity domain was already stated: 25 lines after the claim,
which is why it did not land. Appendix C now leads with the limits: it is **an empirical account of
much, not all, of the random-encoder signal**, it is **not a theorem**, and **a randomly initialised
recursive network is not a random projection of the token multiset**. That last point already appeared
elsewhere in the appendix and now agrees with the opening statement instead of contradicting it.

## §13: reduce defensive qualification. **Done, by removing repetition rather than statements.**

We note this pulls against the previous round's reviewer, who said explicitly that the scope
disclaimers were helping the paper. We think both are satisfiable, and cut **duplication** only: "this
does not show compositional reasoning" appeared in the abstract, §4.3 and the conclusion, and now
appears once in the boxed contract, referenced from §4.3. Every distinct disclaimer survives intact,
including the whole `Established / Not established` block.

## §19: do not add ten more benchmark experiments. **Followed.** Nothing was run.

## What we did not do

- **We did not re-promote the retrieval-specific proposition** to the main text. Round 13 asked for it
  to be demoted; the new general proposition is what makes that demotion sustainable.
- **We did not rename the log keys** to match the new level names. They are data; the mapping is
  documented in two places instead.
- **We did not add NeSymReS to Table 1.** Appendix I states that its column-permutation control is not
  the analogue of symbolic renaming and is counted toward no level finding; putting it in a verdict
  table would contradict the paper's own disclaimer.

## Build state

- 68 pages; **main text exactly 9**, Ethics at index 7 of page 10.
- 0 LaTeX errors, 0 `Float too large`, 0 unresolved references, 1 overfull hbox (the pre-existing
  3.509 pt).
- `verify_claims.py` **1742/1742, exit 0** in all three copies: unchanged, by design.
