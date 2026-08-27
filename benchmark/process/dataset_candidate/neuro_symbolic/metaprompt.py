TASK = r"Learn a continuous latent representation of algebraic constraints over real-valued random variables. The encoder is trained on a satisfaction-classification corpus with a triplet-loss objective; the resulting latent distance is then evaluated as a regulariser on the n-body and spring physics benchmarks of Cranmer et al."

DATASET = r"""
The training corpus is a \textbf{programmatically generated dataset of algebraic constraints}. There is no external download for the classification task: the data generator must be implemented in the project and invoked once at the start of training. The reference implementation is provided in the directory \texttt{/workplace/dataset\_candidate/neuro\_symbolic/algebraic\_classifier/}.

Specification of the synthetic generator:

\begin{itemize}
    \item \textbf{Expression trees.} Sample binary trees with depth drawn uniformly from $[2, 6]$. Internal nodes are drawn from the operator vocabulary $\{+, -, *, /\}$ for binary nodes and $\{\sin, \cos, \exp, \log, \sqrt{\cdot}\}$ for unary nodes. Leaves are drawn from a bank of real-valued random variables $\{x_1, \dots, x_k\}$ with $k \in \{2, 3, 4, 5\}$ together with numeric constants sampled from a small lookup table. Wrap each tree in an outermost relation drawn from $\{<, \le, =, \ge, >\}$ to obtain a satisfaction predicate.
    \item \textbf{Value sampling.} For each expression, sample $n_{\text{pos}} = 5$ satisfying and $n_{\text{neg}} = 5$ non-satisfying assignments. Use a mixture of (a) uniform random sampling over the variable supports and (b) hard-negative sampling that perturbs a satisfying assignment until the label flips (and vice versa). The negative-sampling ratio is a hyperparameter swept over $\{0.0, 0.25, 0.5, 0.75, 1.0\}$ in the ablation.
    \item \textbf{Triplets.} Within each mini-batch, construct (anchor, positive, negative) triplets using FaceNet's semi-hard online mining over the expression embeddings.
    \item \textbf{Sizes.} Training: $\approx$ 200{,}000 expressions; validation: 10{,}000; test: 10{,}000. With 10 assignments per expression this gives $\approx$ 2M training pairs.
    \item \textbf{Domain guards.} Division and $\log / \sqrt{\cdot}$ are domain-guarded during sampling; expressions with empty satisfying sets after $k=64$ retries are discarded.
\end{itemize}

The downstream evaluation also uses the \textbf{n-body and spring-system benchmarks of Cranmer et al. (2019)}, available from \url{https://github.com/MilesCranmer/symbolic_deep_learning}. The reference graph-network implementation is checked into the same repository; clone it into \texttt{/workplace/dataset\_candidate/neuro\_symbolic/symbolic\_deep\_learning/} on first use. The downstream task reuses Cranmer et al.'s training script unchanged, except for the addition of a $\lambda \, \| f_\theta(\text{expr}_i) - f_\theta(\text{expr}_j) \|$ regulariser computed over pairs of algebraic expressions that describe equivalent Newtonian / Hookean laws.

\begin{verbatim}
# Minimal example for loading the synthetic generator
from algebraic_classifier.generator import (
    ExpressionGenerator, AssignmentSampler, TripletDataset,
)

gen = ExpressionGenerator(num_variables=4, max_depth=6, seed=0)
sampler = AssignmentSampler(n_pos=5, n_neg=5, negative_ratio=0.5)
train_ds = TripletDataset(gen, sampler, num_expressions=200_000)

for expr, assignment, label in train_ds:
    ...
\end{verbatim}
"""

BASELINE = r"""
The proposed model is a Tree Neural Network (TreeNN) encoder trained with a joint binary cross-entropy satisfaction loss and a FaceNet semi-hard online triplet loss. The encoder is compared against the following baselines:

\begin{itemize}
    \item \textbf{GNN (GIN/GAT)}: A Graph Isomorphism Network (or Graph Attention Network) applied to the expression DAG, with the same shared classifier and triplet heads.
    \item \textbf{Transformer}: A Transformer applied to a depth-first linearisation of the expression tree with explicit open/close tokens, plus learned positional encodings of node depth.
    \item \textbf{No-regulariser physics baseline}: For the downstream evaluation, the unmodified Cranmer et al. graph network trained without the latent-distance regulariser.
    \item \textbf{Hard-constraint physics baseline}: For the downstream evaluation, the Stewart & Ermon (2017) style hand-coded algebraic loss for each known law, instead of a learned latent-distance regulariser.
\end{itemize}

References:
[1] Lample, G. and Charton, F. Deep learning for symbolic mathematics. ICLR 2020.
[2] Xie, Y. et al. Embedding symbolic knowledge into deep networks. NeurIPS 2019.
[3] Stewart, R. and Ermon, S. Label-free supervision of neural networks with physics and domain knowledge. AAAI 2017.
[4] Cranmer, M. et al. Learning symbolic physics with graph networks. arXiv:1909.05862.
[5] Schroff, F., Kalenichenko, D., and Philbin, J. FaceNet: A unified embedding for face recognition and clustering. CVPR 2015.
[6] Tai, K. S., Socher, R., and Manning, C. Improved semantic representations from tree-structured long short-term memory networks. ACL 2015.
"""

COMPARISON = r"""
\begin{table*}[htbp]
    \centering
    \caption{Expected experimental results. Classifier accuracy and triplet-retrieval mAP@10 are reported on the held-out synthetic test set; physics MSE is reported on the n-body benchmark (lower is better). Numbers are placeholders to be overwritten by the actual experimental run.}
    \begin{threeparttable}
    \renewcommand\tabcolsep{10pt}
    \renewcommand\arraystretch{1.05}
    \begin{tabular}{c|ccc}
        \toprule[1.2pt]
            Encoder & Classifier acc.\ (\%) $\uparrow$ & Retrieval mAP@10 $\uparrow$ & Physics MSE ($\times 10^{-3}$) $\downarrow$ \\
        \midrule
        TreeNN (ours)            & TBD            & TBD            & TBD            \\
        GNN (GIN)                & TBD            & TBD            & TBD            \\
        Transformer              & TBD            & TBD            & TBD            \\
        \midrule
        No regulariser           & --             & --             & TBD            \\
        Hard-constraint loss     & --             & --             & TBD            \\
        \bottomrule[1.2pt]
    \end{tabular}
    \end{threeparttable}
    \label{tab:main}
\end{table*}
"""

EVALUATION = r"""
The model is evaluated on four axes:

\begin{enumerate}
    \item \textbf{Classifier accuracy}: Binary accuracy on the held-out synthetic test set of (expression, assignment, label) triples.
    \item \textbf{Triplet retrieval}: mAP@10 retrieval accuracy over the held-out expression set, where a retrieval is correct iff the retrieved expression shares the same satisfying region (within a tolerance) as the query.
    \item \textbf{Negative-sampling ablation}: Repeat (1)-(2) with negative-sampling ratio in $\{0.0, 0.25, 0.5, 0.75, 1.0\}$ to verify that hard-negative sampling is necessary.
    \item \textbf{Downstream physics MSE}: On the n-body and spring benchmarks of Cranmer et al., report position / velocity MSE with and without the latent-distance regulariser, sweeping $\lambda \in \{0, 10^{-3}, 10^{-2}, 10^{-1}, 1.0\}$.
\end{enumerate}

\begin{verbatim}
def accuracy(y_pred, y_true):
    preds = (y_pred > 0.0).long()
    correct = (preds == y_true.long()).sum().item()
    return correct / len(y_true)

def map_at_k(retrievals, relevance, k=10):
    # retrievals: list of ranked lists of indices per query
    # relevance: boolean matrix [num_queries, num_documents]
    aps = []
    for ranking, rel in zip(retrievals, relevance):
        hits = 0
        precisions = []
        for rank, idx in enumerate(ranking[:k]):
            if rel[idx]:
                hits += 1
                precisions.append(hits / (rank + 1))
        if hits > 0:
            aps.append(sum(precisions) / hits)
        else:
            aps.append(0.0)
    return sum(aps) / len(aps)
\end{verbatim}
"""

REF = r"""
All synthetic-data utilities are in the directory \texttt{/workplace/dataset\_candidate/neuro\_symbolic/algebraic\_classifier/}; refer to it when implementing the expression generator, value sampler, and triplet dataset. The downstream physics task reuses Cranmer et al.'s graph-network implementation in \texttt{/workplace/dataset\_candidate/neuro\_symbolic/symbolic\_deep\_learning/} (clone from \url{https://github.com/MilesCranmer/symbolic_deep_learning} on first use).

[IMPORTANT]
1. Do \emph{not} attempt to download the classification dataset; it must be generated locally with the provided generator (random seed fixed for reproducibility).
2. Run the synthetic-data sanity check (\texttt{python algebraic\_classifier/run\_demo.py}) before training to verify the generator and the tiny logistic-regression baseline both work end-to-end.
3. First train for 2 epochs to confirm the full pipeline (data, encoder, triplet mining, classifier head, physics regulariser) runs end-to-end. Then scale up to the full training budget.
4. Report all four evaluation axes in the final results table; ablations on negative-sampling ratio and on $\lambda$ are required.
"""
