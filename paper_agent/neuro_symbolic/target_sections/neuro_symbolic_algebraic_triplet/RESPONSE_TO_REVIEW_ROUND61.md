# Response to Review, Round 61: the two NeurIPS 2026 TAE workshop reviews

**These two reviews are of a different paper.** They review the workshop version
(`target_sections/taieval_workshop_audit`), not this ICLR submission, and the first thing we did
was measure which of their asks transfer. Three of the four do not transfer in the form they were
written, and saying so is only credible because the fourth one **does**, is the sharpest thing
either reviewer wrote, and is a defect of *this* paper that 60 prior rounds and four gate scripts
did not see.

| | Quality | **Clarity** | Signif. | Orig. | Rating |
|---|---|---|---|---|---|
| **R1** | 3 | **1 (poor)** | 2 | 2 | **3 borderline reject** |
| **cHnS** | 3 | **2 (fair)** | 3 | **4 (excellent)** | **4 borderline accept** |

Clarity is the lowest score from both of you. That is the only fully corroborated complaint, and we
have treated it as a **routing** problem rather than a writing problem, because in three of the four
cases the answer you wanted was already in the ICLR paper and was not where you were reading for it.

---

## 1. R1: *"Mismatch with statistical claims"*; you are right, and it is worse here than in the paper you read

> *"Several of the controlled-probe experiments are still summarized using only three seeds (Tables 2
> and 4 for example)… report twin-level bootstrap confidence intervals for the trained/untrained
> gaps … in line with the paper's own recommendations."*

**Conceded without qualification.** This is the round's real defect. In the ICLR paper the twin rung
is the centrepiece: *"no admissible comparator narrows the $0.206$"* (`experiments.tex:68`), and its
trained/untrained gap shipped as a spread over **3 seeds** (`poly8`) and **5 seeds** (`boolean8`),
i.e. dispersion over *initializations*, which is the unit this paper spends a whole section arguing
against. Meanwhile, in the same document:

- `experiments.tex:401` asserts *"every interval above is a class-level bootstrap"*;
- **Definition 1** (`methodology.tex:268`) *requires*, for a pass, *"class-level intervals excluding zero"*;
- and `tab:stronger_baselines`'s caption promises *"Class-level 95% bootstrap CIs in brackets"* while
  **all four of its encoder rows carry no bracket** and every bag and tree-edit row does.

So your phrase *"in line with the paper's own recommendations"* is exactly the right diagnosis: the
paper asked for one statistic and reported another, in a table whose own caption promised the first.
**A promised interval is a claim**, and this one had been promised and not delivered for many rounds.

Root cause, from the code rather than from reading: `run_r75_stronger_baselines.py` computes the bag
and tree-edit rows per class and bootstraps them, but pulls the two *encoder* arms from a stored
scalar copied out of `r72`/`r73`, so no per-class vector for either arm ever existed.

**What we are shipping.** A new tag re-runs the swap twin with per-class capture for *both* arms and
reports the **paired class-level bootstrap of the gap**: one class is one twin, so `tf[i]/th[i]/tw[i]`
are aligned across arms, `gap_i = trained_i − untrained_i` is defined per class, and resampling the
gap vector resamples one class index for both arms at once, a paired interval, not the difference of
two independent ones. Statistics are by the already-released `_class_bootstrap` (10 000 resamples);
no new estimator was written. On `poly8` this is 348 classes at $K{=}500$, on `boolean8` 73 at
$K{=}190$, the same populations the published means were computed over; we confirmed the split is
deterministic by reproducing the published **143** constructible twins at $K{=}200$ exactly.

**The numbers.** `r104_swap_twin_classci` (poly8, 88 min) and `r106_boolean_swap_twin_classci`
(boolean8, 380 min) are both in the supplement, indexed as REPRODUCE row **R51**. On `poly8` the
paired gap is **`0.206` `[0.172, 0.240]`** over all 348 classes and **`0.166` `[0.119, 0.215]`** over
the 143 at the matched $K{=}200$; both exclude zero, and all four arm means reproduce the shipped
`r73` log **bit-for-bit** (`0.9943`, `0.7883`, `1.000`, `0.8345`), so nothing was renumbered and no
`tab:audit_changes` row is owed. On `boolean8` the three gaps are Tree-LSTM **`+0.296`
`[+0.225, +0.364]`**, Transformer **`+0.119` `[-0.004, +0.238]`** and GIN **`-0.004`
`[-0.047, +0.040]`** over the 73 twins, **only the Tree-LSTM's excludes zero**, which we print rather
than soften: the per-arm seed spreads (`±.026`, `±.028`) never gave GIN's `+0.034` a sign. The
untrained Tree-LSTM and untrained Transformer arms reproduce exactly; **both GIN arms do not**
(`0.494`/`0.499` against `0.511`/`0.477`), and Appendix AO says so beside the intervals, because
citing the arms that reproduce and omitting the one that does not would be selection. Appendix AO's
*"the gap widens"* survives the stricter statistic: at the matched $K{=}200$ the two paired intervals
are **disjoint** (`+0.2247` against `+0.2145`).

One thing we did **not** do with your statistic, because it would have been a misroute: we did not
label the trained−untrained interval as satisfying Definition 1. Definition 1's criterion gap is to
$\sup\{M(g) : g \in \mathcal{F}_t\}$; the `0.500` the family is pinned at, and the untrained
encoder is not a member of $\mathcal{F}_3$. Appendix AB now states that distinction explicitly where
the interval is reported.

---

## 2. cHnS: *"it is unclear what new conclusions the hierarchy licenses"*, the answer existed, on page 53

> *"Outperforming Tier-3 baselines does not establish compositional understanding either… a more
> precise discussion of the Tier 3–Tier 4 boundary."*

Two things, and the second is a defect you found without meaning to.

**First: your own sentence is this paper's Proposition 3.** *"Outperforming Tier-3 baselines does not
establish compositional understanding"* is `prop:nofinite`, titled **"No admissible family
certifies"**, and the paper states it more strongly than you did, not merely that a pass fails to
establish composition, but that **no** admissible family, at any cardinality, can be made to certify
it, and it is **Proposition 3, on page 70**. What was missing was not the claim. It was the
**mechanism**, which was sitting in appendix **AC on page 53**, cited from the body by number only.

**Shipped** (`methodology.tex:271`, p6): the four-kinds list's item *(iv) Proved, not open* now reads

> *(iv) Proved, not open*: **$\mathcal{F}_3$ is *bounded* and composition is not**, so completeness
> is unreachable (Cor. 3; Props. 2, 3).

which lands the boundedness mechanism in the paragraph where a reader is already asking your
question, one clause before the citations that prove it. Funded entirely inside its own paragraph
(the paragraph is still four lines; its last-line tail went 40.12pt → 31.55pt), because §3 spans the
paper's only two negative-slack pages.

**Second, the defect: this paper has no Tier 4.** The ICLR version deliberately replaced the
workshop's four tiers with **three cue levels S1–S3 plus a separate coverage axis C**:
`figure_audit.tex:226` says *"separate axis, not a fourth level"*, and `check_protected_claims.py`
bans the literal `Four levels` from the body and floats precisely so that the old framing cannot
creep back. Your question made us grep for it, and appendix AC's last bullet still read:

> *"**Levels 3 and 4** are separated by boundedness rather than categorically…"*:

workshop vocabulary naming an object this paper never defines, in the **exact sentence** your
question is about. Now repaired to *"**S3 and composition** are separated by boundedness rather than
categorically"*; the phrase `Levels 3 and 4` has **0** occurrences in the rendered document.

---

## 3. cHnS: *"which baselines correspond to the inventory, shape, and order columns"*, already fixed here, and we closed the one residue

> *"It is difficult to determine from the text which baselines correspond to the inventory, shape,
> and order columns in Table 1."*

Measured. Your Table 1 is the workshop's `tab:probes` (p5), whose header row is literally
`Probe & inventory & shape & order & untrained & trained & gap & corpora`: three column heads naming
cue *tiers* and no text saying which baseline realises each. Your complaint is correct about that
table.

The ICLR paper does not contain that table. Its counterpart, `tab:probe_ladder`
(`appendix_domain_guards.tex:1294`), replaced the anonymous columns with **`Holds invariant`** and
**`Strongest unpinned`**, which names the realising baseline *and* its value on every rung:

| Probe | Holds invariant | Strongest unpinned |
|---|---|---|
| `rotate` | inventory | tree-local **0.909** |
| `swap` | + local shape | token $n$-gram 0.769 |
| `relocate` | + argument order | *none left unpinned* |

and `tab:entitlements` (Table 2, p5) carries a *Strongest admissible control* column per claim, while
Definition 1 declares the families by name ($\mathcal{F}_1$ variable bags, $\mathcal{F}_2$
operator/arity bags, $\mathcal{F}_3=\{\phi_d\}\cup\{\mathrm{WL}_h\}$).

**One residue was real, and is fixed.** §3.2's level table (the first place a reader meets S1/S2/S3)
named *no* baseline at all. Its "The control reads" column now names the realising control in every
row: **a variable bag** (S1), **op bag** (S2), **$\phi_d$, $\mathrm{WL}_h$** (S3). At zero page cost,
on a page with 0.000pt of slack.

---

## 4. R1: *"very narrow evaluation"*; measured, and this is where we push back

> *"The evaluation is very narrow… too narrow to make any claims outside of some basic algebraic
> expressions."*

**True of the paper you read; not true of this one, and the difference is not a matter of emphasis.**
The workshop abstract states its breadth as *"a targeted audit of 23 corpora from four benchmark
families"*, all of them symbolic mathematics, and mentions neither natural language nor code. The
ICLR submission audits **25 corpora across three modalities and two algebras**, and its abstract says
so in words: *"The levels name cues, not algebra: **the audit ports to language and to code**, where
**our own** inversion fails to replicate."*

Re-derived from the source rather than from the old caption, `tab:benchmark_survey` is: 3
physics-derived + 15 EQNET (7 `poly`, 8 `bool`) + 2 generated SR/integration + 3 shared-variable
designs + 1 Python stdlib clone corpus + 1 SCAN = **25**.

**But the charge landed on a real defect anyway**, of the kind we now expect: the paper was printing
a *log's* count against a *table*. `r57_eqnet_survey` audits **23** corpora; the table it was cited
beside lists **25** (r57's 23 plus the Python-clone and SCAN blocks). Fixed at the two body sites
(`experiments.tex:43`, `introduction.tex:106` → *"25 corpora"*), and the appendix manifest row that
carried the mirror-image error (`23 corpora (Table 23)`) now reads **`23 of Table 23's 25
corpora`**, which is what is true of both objects. The verifier's own note, which still quoted the
*workshop* caption to justify asserting 23, now says which object the 23 belongs to.

Widening 23→25 does not weaken the paper's scoping claim, and it is worth being exact about why,
because one of the two added corpora is the **worst** case in the table. SCAN is immune at T1
(**0.3%** unique var-sets, like EQNET's $\leq 3.2\%$). The Python-clone corpus is not: **T1 fires
harder there than in any symbolic corpus, 96%, against AI~Feynman's 84%.** The claim *"the T1
failure is confined to the physics block"* survives only because that corpus is **constructed by us,
not published**, which is the distinction the survey's own caption draws: *"constructed, so evidence
the auditor ports and not of prevalence there."* So the larger denominator leaves the published-family
scoping intact while adding the sharpest instance of the effect, and we would rather state it that way
than let "25" read as 25 clean corpora.

**What we did not do, deliberately.** We did not add a breadth count to the abstract. It was drafted
(`", three modalities"`, +18 characters, and it fits), and declined: the abstract already states the
portability in words in the same paragraph, a numeral there would be the third site to state the same
count, and a first-pass reader's complaint about narrowness is answered by the sentence, not by the
number. We also left `experiments.tex:230` alone (*"portability, not general validation, never
prevalence"*), because the fair half of your charge is that every **deep** result here is symbolic,
and that sentence is the paper conceding exactly that. Breadth of *audit* is not breadth of
*demonstration*, and we would rather keep drawing that line than answer a breadth complaint by
over-claiming breadth.

---

## 5. Found while checking, raised by neither of you

**A shipped log can be staler than the paper it supports.** `tab:stronger_baselines` prints
tree-edit distance at `0.723 [0.694, 0.751]`. The verifier *recomputes* TED live and pins `0.7227`,
so the paper's number is right, but `logs/r75_stronger_baselines.json` still holds the
pre-round-14 `0.7328 [0.7026, 0.7629]`, from before `_postorder` was corrected. Two consequences: no
shipped log contains `[0.694, 0.751]`, so that bracket pair has no artifact provenance; and
`verify_claims.py` computes its `best_nonlearned` comparison from the **stale** value, passing only
because `0.7328 < 0.788` regardless. No gate can see either, because the verifier recomputes one
number and reads another. Being resolved by refreshing the log, one change at a time, with the
verifier re-run between.

**Our own reproducibility number was the smallest of several we had measured.** R1's heading was
*"Mismatch with statistical claims"*, and answering it produced one more mismatch of exactly that kind:
created by the new run itself. The Reproducibility Statement said *"re-running a trained cell in a
different environment reproduces it to `0.0023`"*. That figure is correctly measured, but on **one**
cell (`poly8`, `K=500`, Tree-LSTM), and the same paper measures replicate envelopes of `0.047` (GIN)
and `0.062` (Transformer) on trained cells in Appendix AK, which states, ten lines earlier, the
principle the sentence broke: *"a bound on one arm is not a bound on another."* `r106` then measured
it directly: same script, same device, same 5 seeds, 20 days apart, the two GIN arms moved `0.0165`
and `0.0219` while the untrained Tree-LSTM and Transformer arms reproduced **exactly** and the two
trained non-GIN arms moved `0.0027` and `0.0055`, and that `0.0219` is what carried GIN's `+0.034`
boolean gap across zero. This confirms rather than contradicts Appendix AJ, which already states in
bold that *"GIN and Transformer training in this harness is not run-to-run reproducible."* A `0.0023` envelope tells a reader such a thing cannot happen here. The statement now
prints both scopes and the largest value (*"to `0.0023` across environments and, on other arms, only
to `0.062` across replicates"*) in place, funded by two trims in its own paragraph.

**The body carried your ask for one twin and not the other.** `experiments.tex:218` printed the `boolean8`
twin margin as a bare `+0.299` (a *seed* mean, in a paper whose stated unit of inference is the
equivalence class *"never the seed"*), while the `poly8` sentence four pages earlier had been given
`0.206 [0.172, 0.240]`. The class-level figure existed in the new log and sat only in Appendix AO. The
body now reads `+0.296 [0.225, 0.364]`, from `r106`'s 73 paired twins. Your sentence asked for
twin-level intervals on the gaps; both twins now carry one where a reader meets them.

**And in the same sentence, one clause earlier:** *"training is stochastic and we report `5` seeds."* The
paper uses `25` seeds at 21 sites, `5` at 16, and `3` at one (the `poly8` twin at matched `K=200`, which
Appendix AO already discloses). Now *"we report `3`–`25` seeds per run."* Both repairs are in the
Reproducibility Statement, and both are the same defect: a global sentence carrying one value for a
quantity the paper measures several ways.

---

## Board

0 LaTeX errors · 0 `(Reference|Citation).*undefined` · 0 `Float too large` · exactly **2**
pre-existing overfull boxes at unchanged sizes (`\vbox` 6.4211pt, `\hbox` 3.509pt) · **102 pages**, up one, the added page being
`fig:scale_curve` becoming a float page of its own once the appendix text spilled; measured,
irreversible (the float is `[t]` and `\input` last, so it can only head a page, and a `[b]` placement
is refused at ~200pt against `\bottomfraction`'s ~193pt), and disclosed rather than bought back by
deleting the interval this round exists to add
· the eleven-page **body** slack profile **byte-identical on every page** (p1 +0.561 · p2 +6.197 ·
p3 +9.463 · p4 0.000 · p5 −0.695 · p6 −1.927 · p7–p10 0.000 · p11 +0.687) · `wc -l` unchanged for
every `.tex`, so every line pin in this letter holds · four gates **PASS**, controls
**54 / 9 inline / 1 / 2**, `check_reviewer_map` at **18 rows, 307 checks, 54 literal `load_log()`
sites, 56 appendix letters** · `verify_claims.py` **2619/2619**, md5
`bcdfacebb5723f737ab393fa7495ac6e` at 9416 lines, the delta accounted for assertion by assertion, and
all three shipped copies md5-identical · p4, p6, p10 and p52 read as images at 150 dpi, not only
through `pdftotext`.
