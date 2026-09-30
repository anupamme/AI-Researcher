# Response to the review (round 10)

*Not part of the paper. Text for the response form.*

Thank you, and thank you in particular for two sentences that shaped this revision more than the
numbered list did: *"I would not spend the next revision adding another 20 tables … the experimental
core is now strong enough,"* and your reconstruction of Proposition 3 as *"genuinely interesting."*
We took both literally. **This round adds exactly one experimental battery (your #2) and otherwise
elevates, reframes and compresses what was already there.** No table was added to the main text.

Your clarity score is the one we could act on most directly, and we made it a measurable target rather
than a matter of taste. The 9-page main text carried **39 appendix cross-references and 13 inline run
tags**; it now carries **20 and 2**: 19 after the compression pass, plus the one pointer the boolean appendix needs, with one pointer to the provenance appendix in place of the tag
soup. That is the mechanism behind *"45 minutes reconstructing the argument,"* and it is now roughly
half of what you read.

---

## #1 / W1, W4: the theory was in the paper as machinery. It is now billed as the contribution

You reconstructed the insight yourself: *raising a structural feature's resolution destroys the
invariance that makes it a valid control.* That is Proposition 3 and Corollary 2 (`prop:resolution`,
`cor:supremum`), and you are right that they were buried in §3 as lemmas serving Definition 1.

**What changed.** The abstract now states it as *the* theoretical result: "our main theoretical result
is that tier 3 cannot be audited by its *strongest* baseline: raising a structural feature's resolution
destroys the invariance that makes it a valid control, so $M(\phi_d)$ is *non-monotone* in $d$ and
completeness must quantify over a *family*", and contribution (1) in the introduction leads with it
rather than with the framework's plumbing. The proofs moved to Appendix AN so the *statements* could
stay prominent inside the page limit; nothing was weakened, and the appendix now also collects the
corollaries' one-line derivations, which used to be inline asides.

**W4, the tier-3 completeness objection, is now answered in your own formulation**, one sentence next
to Definition 1: the family is *explicit, not exhaustive*, and that is the design. Rather than enumerate
every structural explanation, which Proposition 3 says no canonical enumeration is on offer for, we fix
$\mathcal{F}$, **name it in the verdict**, and thereby make the epistemic scope of passing the test
transparent. "Control-complete w.r.t. $\mathcal{F}$" is a weaker, checkable claim standing in for an
unfalsifiable one.

**And the insight now has a third independent measurement**, which is the part we did not expect. See
the next section: on a *different algebra*, under the *unseen-class* protocol rather than the
composition protocol, $\phi_\infty$ again scores below every $\phi_d$ member and the $\mathcal{F}_3$
supremum is again attained at a **coarse** member ($d{=}1$ or $h{=}1$) at every scale. Proposition 3 is
now measured on two algebras and in two protocols.

## #2 / W2: the independent-domain replication, in full

You asked whether the twin and unseen-class results are `poly8` properties. Round 9 replicated only the
*composition* design off `poly8`. This round replicates **the rest of the design** on `boolean8`, a
different algebra: the shape-matched twin, the unseen-class tier ladder with its null, and the
architecture question, three architectures on the twin, three on the ladder.

**The twin replicates, and the gap *widens*.** Over the `73/190` `boolean8` classes admitting an
`implies` sibling swap (non-equivalence decided by an **exact 8-row truth table**, *stronger* than
`poly8`'s 24-sample numeric probe, with r73's other three acceptance tests unchanged so the twin is still
matched at tiers 1–2 **and** at `_tree_local`) the trained Tree-LSTM reads **0.934 ±.015** against an
untrained **0.636 ±.052**: a gap of **+0.299**, where `poly8` at matched `K=200` gives `1.000` vs `0.835`
for `+0.166`. Both $\mathcal{F}_3$ bags are pinned at **exactly 0.500**, and the separation is per seed:
worst trained `0.918` above best untrained `0.685`. The trained encoder no longer saturates, so unlike
`poly8` the measurement has headroom in both directions. Architecture ordering by gap: Tree-LSTM
`+0.299` ≫ Transformer `+0.114` > GIN `+0.034`, GIN's interval containing chance.

**The unseen-class ladder replicates at three scales.** Trained Tree-LSTM unseen precision
`0.940`/`0.974`/`0.955` at `K = 50,100,190`, clearing the upper bound of **every** non-learned interval at
**all three** scales, where on `poly8` the `K=50` and `K=100` intervals *overlap*, and the
trained-minus-untrained margin **grows with K** (`+0.127` → `+0.205` → `+0.258`), the direction `poly8`'s
margin moves in.

**Three results run the other way and all three ship, with the same pre-commitment language §4.3 uses.**
*(i)* The **untrained** encoder exceeds the $\mathcal{F}_3$ supremum at every scale (`0.813` vs `0.732`,
`0.769` vs `0.525`, `0.698` vs `0.511`), which on `poly8` it does not: 20 forms per class is an easy
enough neighbourhood that a random tree encoder beats every order-blind fingerprint we can build. That is
the $\mathcal{S}$-versus-$\mathcal{F}_3$ distinction doing visible work: the untrained encoder is not
arrangement-invariant, so Proposition 1 never applied to it, and the verifier asserts it at all three
scales so it cannot be quietly dropped. *(ii)* `SeenEqClass` identification **falls** with `K`
(`0.952`→`0.922`→`0.911`) where unseen precision does not. *(iii)* The Transformer's interval does **not**
clear the strongest non-learned bound (`[.588,.746]` against `0.596`), asserted as a **failure**, so a
rerun that promoted it breaks the verifier instead of agreeing with the appendix.

**And one finding we think is the most useful thing in the round.** **The same GIN clears tier 3 on
unseen classes: `0.881` `[.850,.909]` against `0.596`, and sits at *chance* on the twin (`0.511`).**
Same corpus, same partition, same architecture: one protocol passed, one at chance. Nothing in the
unseen-class protocol separates a representation that composes from one that merely clusters well under a
coarse similarity; the twin does. This is the sharpest form of §4.2's Finding 2 available anywhere in the
paper, because here the thing clearing the bags is a *trained encoder*, not a strawman: a reader who
accepted only the unseen-class number would have credited GIN with structural identification on this
corpus. The verifier asserts it as a **conjunction**, so neither half can be dropped.

**Two structural differences from `poly8`, disclosed rather than hidden by a ratio.** `boolean8`'s unseen
pool is 38 classes against `poly8`'s 100, so we report the **exact random-label null** (`0.02503`), not
`1/n_classes`; and it holds **20 forms per class** where `poly8`'s median is 6, which makes the k-NN task
easier in a way ratio-to-chance conceals. Because of that we quote **both** ratio and absolute margin,
and here they disagree: measured against chance the boolean ladder looks *better* (`38×` against
`poly8`'s `20×`, since the exact null is `1.8×` larger), while measured against the $\mathcal{F}_3$
supremum the two corpora sit in the same place (`0.511` at `K=190` against `poly8`'s `0.517` at `K=500`,
a `1.9×` against `1.7×` margin). The margin over the supremum is the conservative reading and it is the one Appendix AO
leads with.

**One correctness note we would rather state than have found.** Porting the twin exposed a trap that
would have produced a *silently wrong* number rather than a crash. The trained encoder threaded a
`vocab_size`; the **untrained control did not**, so it was built over the frozen arithmetic vocabulary
(34) while `boolean8` emits token ids up to 38, and on MPS an under-sized `nn.Embedding` does not
raise. It returns garbage, for the Tree-LSTM, the GIN and the Transformer alike. We fixed it, audited
every other `build_encoder` call site in the artifact, and verified before spending any compute that
(i) the trap was real and (ii) it is closed. For (iii), that the `poly8` path did not move, we make the
claim two ways and neither is a re-run of a trained row: Appendix AJ/AL already report those as not
bit-reproducible across environments, so a re-run could not have settled it. *By construction:* on every
arithmetic corpus the threaded value **is** `build_encoder`'s former default, so the `poly8` path builds
the same model bit for bit. *By re-run, on the part that is deterministic:* `r71`'s encoder-free ladder,
re-run on the `poly8` default, agrees with its shipped log on all **693** scalar cells with **zero** drift.
Appendix AO records this, because the same shape (a control that is not reconfigured along with the
model) is what produced the `r79` defect we disclosed in round 9.

## #3 / W7: compression, and what we spent it on

We cut about a page of main-text prose. **We did not ship an 8-page paper, and we would rather say so
than let you discover it.** The freed space went to your #2's results, to Proposition 3's elevation, and
to W3's scope statements; the alternative was deleting evidence that the previous two reviewers asked
for (Table 1 is round 7's and round 9's; Table 2 is round 8's; the "our positives are easy" disclosure
is round 6's). Main text is therefore still nine pages, carrying materially more.

What was actually removed, all of it duplication rather than evidence: the conclusion's restatement of
the abstract's architecture bounds; §4's inline run tags; four of five appendix pointers in the protocol
paragraph; the proofs (to Appendix AN); two paragraphs merged in Related Work; and the "Scope and
limitations" paragraph reduced to "Scope."

**Structural changes you asked for.** §4 is now organised around the three findings in your own words (
**Finding 1** a held-out-form score can be a lookup task, **Finding 2** clearing the bags is not enough,
**Finding 3** even a hardened benchmark measures training-library coverage) with the 23-corpus audit as
the question *"how widespread is Finding 1?"* rather than a co-equal contribution. **Table 1 moved to the
top of Related Work** so it lands on page 2 instead of page 3, per your note that it is the paper's most
persuasive object.

## #4, #5 / D1, D2: contributions and vocabulary

The contributions list is now contribution-shaped rather than claim-shaped: **(1)** the falsification
framework, led by the theoretical result; **(2)** the 23-corpus audit with the released auditor;
**(3)** the hardened evaluation study plus the matched-schema intervention. The heading names the thing
we do not claim, so the list reads as scope rather than as advertising: *"Contributions, and one claim
we do not make."*

The **licensing** vocabulary is now the framing rather than an aside: the opening paragraph asks what a
benchmark result *licenses*, and Table 2 ("What a result establishes, and what it does not") is where
that cashes out.

## W8: the score₅ leaderboard audit is now validation, not a fourth contribution

It sits under *"Validation: does the method catch protocol errors, including ours?"*, next to the four
claims of our own the audit changed. Two of those four moved **against** us, which is the strongest
thing we can say about the method's direction of inference and reads better as validation than as a
result.

## W5: one causal formulation, everywhere

Three sites disagreed. All three now carry §4.4's wording verbatim: **under our matched-schema
intervention, training-library membership is a causal determinant of out-of-distribution performance,
structural distance held exactly fixed.** Section headings stay non-causal. This also shortened the
abstract and the introduction, which is how part of #3 was paid for.

## W6: the composition experiment is renamed

Table 3 and the surrounding text now say **"generalization to unseen compositions of rewrite
primitives."** The unqualified phrase "compositional generalization" appears in the paper only where we
are describing what we *do not* claim.

## W3: scope stated, title kept

The abstract's first sentences now scope the contribution explicitly: *a methodology for
symbolic-expression representation benchmarks, not for reasoning benchmarks at large.* Contribution (2)
repeats it. We kept the title deliberately, and we would rather argue for that than quietly comply:
significance was your other 7.5, and a narrower title would cost the paper the framing that makes the
23-corpus audit worth reading.

## W9: why this is an ICLR paper

Added to the first paragraph: *we propose no model that wins a benchmark; we ask whether a benchmark's
protocol licenses the conclusions drawn from model performance*, which is a question about how
representation learning is evaluated.

## Reproducibility

`verify_claims.py` moves **1421 → 1599** assertions and passes in all three synced copies, exit 0, with no
earlier assertion perturbed by the new runs. Every new number this round is asserted, and the two hard
shapes from round 9 are used again on purpose: **the twin gap is asserted as an inequality**, against
`poly8`'s matched-`K` gap, so a rerun that merely *replicated* the poly8 number would fail, and **the
per-architecture ordering as an exact sequence**, so a rerun that reverses either must fail rather than
pass. Three more shapes are new. The two $\mathcal{F}_3$ bags are pinned at `tol=0`, because "pinned at
chance" is a membership test and not a measurement. The GIN result is a **conjunction** (clears tier 3
*and* sits at chance on the twin) so neither half can be dropped, and the Transformer's *failure* to clear
tier 3 is asserted as a failure, so a rerun that promoted it breaks the verifier rather than agreeing with
the appendix. And the three boolean runs are asserted to agree **bit-identically** on the shared split (38
unseen classes, 760 forms, the exact null `0.02503`, all three bag rows), which is what makes reading the
encoder off one log and the $\mathcal{F}_3$ supremum off another legitimate. **12 negative controls** were
run against the new block; one of them caught a defect of ours, two ordering assertions written over the
verifier's own constants rather than over the log, which is tautological. They now read from the log. The tier-3 ladder's assertions include the one thing a value check would miss:
`boolean8`'s tie-unsafe representations are pinned **as a set**, so a rerun that moved the flag onto the
member the appendix reads its supremum off breaks the verifier instead of the argument.
