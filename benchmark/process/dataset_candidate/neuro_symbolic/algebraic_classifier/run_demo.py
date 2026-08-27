"""End-to-end sanity check for the algebraic-constraint generator + baseline.

Run as:

    python run_demo.py --num_expressions 2000 --steps 200

It generates a small dataset, splits it 80/20, trains the
`BagOfOperatorsLogistic` baseline for `--steps` SGD steps, and prints
train/test accuracy. This script has no third-party dependencies.
"""

from __future__ import annotations

import argparse
import random

from generator import AssignmentSampler, ExpressionGenerator, TripletDataset
from baseline import BagOfOperatorsLogistic, FEATURE_VOCAB, evaluate, featurise


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_expressions", type=int, default=2000)
    parser.add_argument("--num_variables", type=int, default=4)
    parser.add_argument("--max_depth", type=int, default=5)
    parser.add_argument("--negative_ratio", type=float, default=0.5)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    gen = ExpressionGenerator(
        num_variables=args.num_variables,
        max_depth=args.max_depth,
        seed=args.seed,
    )
    sampler = AssignmentSampler(
        n_pos=5, n_neg=5, negative_ratio=args.negative_ratio, seed=args.seed
    )
    dataset = TripletDataset(
        generator=gen, sampler=sampler, num_expressions=args.num_expressions,
        triplet_seed=args.seed,
    )
    examples = dataset.labelled_examples()
    print(f"Generated {len(examples)} (expression, assignment, label) examples")

    rng = random.Random(args.seed)
    rng.shuffle(examples)
    split = int(0.8 * len(examples))
    train, test = examples[:split], examples[split:]

    feature_dim = len(FEATURE_VOCAB) + 1 + args.num_variables
    model = BagOfOperatorsLogistic(dim=feature_dim, lr=0.05, seed=args.seed)
    for step in range(args.steps):
        ex = rng.choice(train)
        loss = model.step(featurise(ex), int(ex.label))
        if (step + 1) % max(1, args.steps // 10) == 0:
            print(f"step {step + 1:>5d} | loss {loss:.4f}")

    train_acc = evaluate(model, train)
    test_acc = evaluate(model, test)
    print(f"train accuracy: {train_acc:.3f}")
    print(f"test  accuracy: {test_acc:.3f}")


if __name__ == "__main__":
    main()
