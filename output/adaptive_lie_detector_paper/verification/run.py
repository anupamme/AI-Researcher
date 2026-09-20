#!/usr/bin/env python3
"""Run the paper's verification harness from the repo copy.

`verify_r36.py` is a GENERATED file: each round's verifier is produced from the
previous round's by `generators/mk_verify_rNN.py`, which asserts that every
string it rewrites occurs exactly once before rewriting it. That discipline is
what makes a retained check impossible to weaken by accident, and it is also why
the generated file must not be hand-edited -- including to change its paths.

So it still loads its ledgers from /tmp, exactly as it did when it was written.
This wrapper seeds /tmp from `data/` and runs it from the paper directory (the
verifier opens `sections/*.tex` relatively).  Usage, from anywhere:

    python3 verification/run.py            # the current harness, r36
    python3 verification/run.py r35        # the previous round, for comparison
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.dirname(HERE)
DATA = os.path.join(HERE, "data")
SNAP = os.path.join(HERE, "snapshots")

which = sys.argv[1] if len(sys.argv) > 1 else "r36"
verifier = os.path.join(HERE, "verify_%s.py" % which)
if not os.path.exists(verifier):
    sys.exit("no such verifier: %s" % verifier)

for name in sorted(os.listdir(DATA)):
    src, dst = os.path.join(DATA, name), os.path.join("/tmp", name)
    if os.path.isdir(src):
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
# the round-36 ledger generator and mk_verify_r36 read the pre-conversion tree;
# `snapshots/` already has this round's layout (PRE/ plus the two BASE files)
dst = "/tmp/r36_snapshots"
shutil.rmtree(dst, ignore_errors=True)
shutil.copytree(SNAP, dst)
# generators/mk_verify_rNN.py reads its predecessor as /tmp/verify_r{NN-1}.py
for name in os.listdir(HERE):
    if name.startswith("verify_r") and name.endswith(".py"):
        shutil.copy2(os.path.join(HERE, name), os.path.join("/tmp", name))

sys.exit(subprocess.call([sys.executable, verifier], cwd=PAPER))
