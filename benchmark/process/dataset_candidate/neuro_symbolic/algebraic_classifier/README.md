# Algebraic-Constraint Satisfaction Classifier — Reference Scaffold

This directory provides a self-contained reference implementation of the
synthetic-data pipeline used by the
`neuro_symbolic_algebraic_triplet` benchmark instance.

It is intentionally minimal: a runnable expression-tree generator, a value
sampler with random + hard-negative components, and a tiny logistic-regression
baseline that uses bag-of-operators features. The ML agent is expected to
import the generator and replace the baseline encoder with a TreeNN / GNN /
Transformer.

## Layout

- `generator.py` — `ExpressionGenerator`, `AssignmentSampler`, `TripletDataset`.
- `baseline.py` — `BagOfOperatorsLogistic`, a tiny baseline classifier.
- `run_demo.py` — end-to-end sanity check; generates a small dataset, trains
  the baseline for a handful of steps, and prints train/test accuracy.

## Usage

```bash
cd /workplace/dataset_candidate/neuro_symbolic/algebraic_classifier
python run_demo.py --num_expressions 2000 --steps 200
```

Expected output (random seed fixed): the baseline should reach > 60% accuracy
on the synthetic test set within a few hundred steps. This is intentionally
modest — the proposed TreeNN / GNN / Transformer encoders are expected to do
substantially better.

## Notes for the ML agent

- The generator is deterministic given the seed; use `seed=0` for the canonical
  training split.
- Domain guards (`/`, `log`, `sqrt`) are already enforced; consult
  `generator._safe_eval` for the exact behaviour.
- The triplet construction in `TripletDataset.__getitem__` returns
  (anchor_expr, positive_expr, negative_expr, anchor_assignment,
  anchor_label) so the encoder can be trained with the FaceNet semi-hard
  online mining recipe.
