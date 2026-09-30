# Response to the review (round 9)

*Not part of the paper. Text for the response form.*

Thank you. Your central objection is **correct, and it had survived two previous rounds**: including
one in which a reviewer read the same section and did not catch it. We fixed it structurally rather
than verbally, and the fix cost us nothing empirically, which we explain below rather than leave you
to infer.

Two things need saying up front. **(1)** Your §1 formal inconsistency was real: Definition 1
contradicted the surrounding text. **(2)** Your §7 request on causal language is the *opposite* of what
the previous reviewer asked for on the same sentence; we have resolved it rather than oscillated, and
we say how.

---

## §1, §2: the control family was genuinely inconsistent. Split, and renamed

You are right. Definition 1 set

$$\mathcal{F}_3 = \{\phi_d\}_{d\in\{1,2,4,8\}} \cup \{\mathrm{WL}_h\}_{h\in\{1,2,3\}} \cup \{\phi_\infty,\ \text{tree-edit distance},\ \text{untrained encoder}\}$$

while §3.3, three paragraphs earlier, already described $\phi_\infty$ as *"the strongest extension
rather than a member."* **The paper contradicted itself**, and the version you object to is the one
Proposition 1 cannot support: $\phi_\infty$, tree-edit distance and an untrained encoder all *read
arrangement*, so none is invariant to the property tier 3 fails to determine, and beating them
falsifies nothing at tier 3 however high the margin.

**What we changed.** $\mathcal{F}_3$ now contains exactly the arrangement-invariant controls,
$\{\phi_d\} \cup \{\mathrm{WL}_h\}$. The other three are named as **structural stress tests**
$\mathcal{S}$ and reported *outside* the criterion: including in the composition table, where those
rows are now marked $\mathcal{S}$.

**Membership is a test we already ran, not a stipulation.** This is the part we think strengthens the
paper rather than patching it. The shape-matched twin differs *only* in sibling arrangement, so it is
an operational invariance test, per instance:

| representation | twin score | in $\mathcal{F}_3$? |
|---|---|---|
| every $\phi_d$, every $\mathrm{WL}_h$, both bags | **exactly 0.500** | yes: invariant, by measurement |
| tree-edit distance | 0.733 | no: reads arrangement |
| untrained encoder | 0.788 | no: reads arrangement |
| $\phi_\infty$ | order-sensitive by construction | no |

So the split is drawn by a number the paper already contained, not by our preference about what counts
as a fair baseline.

**Why this costs no result, and why that is an argument rather than a convenience.** Proposition 3
(added last round) proves the supremum in Definition 1 is attained at *coarse* members and that
adjoining a more resolving $g$ cannot raise it. Therefore **removing the most resolving member cannot
lower the bar**: the criterion is exactly as hard as before. And the encoder clears $\mathcal{S}$
anyway, at every depth and on the twin. Nothing that was established is now established against a
smaller set; what changed is that a tier-3 verdict now means what Proposition 1 says it means.

**Renamed throughout**, in your words: *control-complete through tier $T$ with respect to the control
family $\mathcal{F}$*. Body, appendices, `statements.tex`, `verify_claims.py` and `REPRODUCE.md`; zero
occurrences of the old term remain in the built PDF.

*One note on consistency with the previous round.* Round 8's response argued that the natural
"no finite family can certify semantics" theorem is false *for our family*, because $\mathcal{F}_3$
contained a complete member. Round 9 removes that member: on **invariance** grounds, not coarseness
grounds. The two are compatible: we still do not claim $\mathcal{F}$ is coarse-by-necessity, and
Proposition 3 (not a boundedness argument) is what carries the exclusion.

## §4: an external compositional benchmark. We ran two, and one of them is a different algebra

This was the concern we took most seriously, and your framing was half right in a way worth
separating. `poly8` **is** external: EQNET (Allamanis et al., 2017), evaluated on the benchmark's own
test classes. But the *composition* experiment is a corpus **we** built on those external anchors, and
that part of your objection stands.

So we replicated the entire design on two further EQNET corpora, changing only `--corpus`:

- **`oneVarPoly13`** (677 classes): same algebra, different corpus.
- **`boolean8`** (232 classes): **a different algebra**, requiring four new rewrite primitives
  (commutativity of $\wedge/\vee/\oplus$, double negation, De Morgan, $x \wedge \top$). The `poly8`
  primitives are *not valid here*: they inject arithmetic operators into boolean trees, which is
  exactly why a naive feasibility probe reports them as firing.

Each new primitive was held to the same two constraints as the original four: an exact identity, and
a **site-independent token delta**, which is what the paired-depth comparison and the size-matched
alternate-order arm both require. Verified, not asserted: deltas $(0, 6, 9, 4)$, site-independent on
193/200 anchors, and every depth-4 boolean form is exactly **+19 tokens** over its anchor *for all 24
orders*. The independent-seed closure guard passes at **200/200** (`oneVarPoly13`) and **180/180**
(`boolean8`) classes at every depth, with zero training composites and zero alternate-order forms
inside the closure.

**What replicated, and what did not.** We report both, because one of them goes against us.

| | `poly8` (published) | `oneVarPoly13` | `boolean8` |
|---|---|---|---|
| algebra | polynomial | polynomial | **boolean** |
| classes / drawn | 1102 / 200 | 677 / 200 | 232 / 180 |
| never-composed, $d{=}1 \to 4$ | .997 → .918 | .995 → .849 | .906 → .676 |
| paired cost of never composing ($d{=}4$) | +0.079 [.063,.097] | +0.146 [.124,.169] | **+0.230** [.197,.262] |
| trained ÷ strongest non-learned, $d{=}4$ | 5.0× | 2.3× | **7.6×** |
| tier-3 control-complete, all four depths | yes | yes | **yes** |
| $\phi_\infty$ below the tier-3 maximum (Prop. 3) | yes | yes | **yes** |
| alternate order ≥ forward chain | yes | yes (within noise) | yes (**above** it) |
| test-$d{=}4$ rises monotonically in training depth | yes | yes | **no** |
| above-diagonal cells hold | yes | yes | **no: 5 of 6 fail** |

**Three things replicate on both corpora, including across the change of algebra.** Tier-3
control-completeness holds at every depth in all eight corpus × depth cells, on disjoint class-level
intervals. Order is never the fragile axis. And Proposition 3 holds again: $\phi_\infty$ scores below
the tier-3 maximum at every depth on both corpora, the non-monotonicity that motivates a
*family*-level control is not an artefact of one corpus or one algebra.

**One thing does not replicate, and it is the mechanism claim, so we scoped it.** On `boolean8` the
test-depth-4 column reads .676 → .699 → **.727** → .706: it *peaks at training depth 3 and falls*.
The best library recovers only .051 of a .230 drop, the paired diagonal cost of never composing is only
+.030, and five of the six above-diagonal cells sit *below* the never-composed arm: putting
composites in the library **costs** shallow accuracy there. §4.3 previously read the depth-4 deficit as
a coverage deficit closed by seeing composites; it now says *here* it is one, and states that the
coverage-closure **mechanism** is polynomial-specific. The abstract, introduction and conclusion carry
the same scope, and the conclusion's "not established" list now includes it.

**The coverage price grows with algebraic distance** (+0.079 → +0.146 → +0.230) while the
margin over the strongest non-learned control **does not order the same way** (5.0× → 2.3× →
7.6×): `boolean8` clears the criterion *most* decisively and pays *most* for composition. Two
orderings, not one, which is why we report both rather than a single "difficulty" number.

**An audit finding about `boolean8` in its own right.** At $d{=}4$ the strongest control below tier 4
is the **tier-1 variable bag** at .089: 16× chance, and roughly constant in depth. Our own survey's
corpus-level statistic puts EQNET at ≤3.2% tier-1 separability, which does not surface this: a
composition draw from a clean corpus can still leave a tier-1 residue, and the criterion catches it
only because it is run per experiment rather than per corpus.

Cost: 5.2 GPU-hours for the two runs. Appendix AM gives the full construction, both matrices, both
non-learned ladders, and what these runs do *not* bound (one architecture, one recipe, one partition
per corpus).

We committed in the previous round to reporting a widened basis even when it went against us, and the
same applies here.

## §7, causal language: your request contradicts the previous reviewer's, and here is the resolution

The previous reviewer objected to an **unqualified** claim: Appendix W was titled *"Coverage Is
Causal"*, and round 8 removed the word entirely. You now ask, correctly, that the LOSO design's
actual strength be stated: it *is* a controlled intervention, with the held-out trees byte-identical
and only library membership varying.

**Resolution: causal language returns, scoped to the intervention, and stays out of headings.** The
body, abstract, introduction and Appendix W now say training-library membership is a *causal
determinant* of OOD performance **under this matched-schema intervention**, each with the scope
attached explicitly: *"not observational coverage."* Section headings remain non-causal. We believe
this satisfies both objections rather than splitting them, since neither reviewer disputed the
intervention; the dispute was over the unhedged generalisation from it.

## §5: the self-audit table

Already where you ask for it: **Table 1, top of page 3**, six rows, four of them our own claims, with
columns *Claim as published / Tier / Verdict after the audit*. We suspect it read as an appendix table
because the surrounding text pointed at it only once; the introduction now leads with it.

## §3: framing

The introduction already opens *"We introduce a falsification framework…"*, and the first paragraph
ends on the self-falsification. We sharpened rather than rewrote, and we **declined to coin an
"Evidence Hierarchy Principle."** A named principle with no content beyond the propositions already
stated is precisely the "dressed-up experimental common sense" a previous reviewer warned against;
naming it would raise the rhetorical temperature without adding a claim.

## §6: the three-panel figure

**Declined, with the reason stated rather than ignored.** The main text is at a hard nine-page limit,
exactly met. A full-width three-panel float costs ~18–22 rendered lines, and the only two things large
enough to fund it are Table 1, which *you* ask to make more prominent, and Table 2, added last round
at the previous reviewer's request. The existing three-panel figure is about Feynman leakage, not the
results, so promoting it would not answer your ask either. We chose the reframing and density work you
also asked for, which is what the space bought.

## §8: density

The additions above were paid for out of restatement, not by cutting evidence. Removed: the
conclusion's opening sentence (a **verbatim** duplicate of the introduction's closing sentence), the
"Non-learned is not structure-free" paragraph (now carried by the $\mathcal{S}$ discussion and §4.3),
and three further restatements of the necessary-not-sufficient point, which appeared eight times
across the paper. Nothing left the record.

---

## Reproducibility

Two new run families (`r83_composition_onevarpoly13`, `r84_composition_boolean8`) under the frozen
recipe, with a new `verify_claims.py` section §[12]. **The assertion count moves 1146 → 1421**,
which is the point: a *static* count would mean numbers had entered the paper unasserted. Two of the
new assertions are worth naming, because they are the ones that could have been written the easy way
and were not. The `boolean8` non-monotonicity is asserted as an **inequality**, and its five failing
above-diagonal cells as an **exact set**, so a rerun in which the coverage closure quietly *did*
replicate must **fail** the verifier rather than pass. And the recipe is compared **field by field
against `r81`'s own provenance** (`corpus` the only permitted difference) rather than against a copy of
the paper, the shape of assertion that previously caught a hardcoded architecture in an earlier round.
1421/1421 pass in all three shipped copies.

The vocabulary change the boolean corpus required was made so that **no published number could move**:
`data.VOCAB_SIZE` is frozen at its pre-boolean value of 34 and is the default of `build_encoder`, while
the five boolean tokens live in a separate `BOOL_VOCAB_SIZE` of 39 that only the boolean corpora pass
explicitly. So every existing token id is unchanged and every arithmetic model in the paper is built
with a bit-for-bit identical parameter shape. Measured, not argued: the boolean variants of all three
architectures gain exactly $5 \times 128 = 640$ parameters and nothing else, and §[12] asserts that the
*arithmetic* replication run still logs `vocab_size` 34, an inequality-style check, since a run that
had renumbered a token would log 39 there.
