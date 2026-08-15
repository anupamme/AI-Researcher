# Official Comment — Closing Note (Reviewer, Borderline Accept)

Thank you for engaging so constructively throughout this discussion — we're grateful for it. As the discussion period closes, we wanted to leave one point crisply stated.

The concern that most weighed on the other reviews was whether the instruction-following artifact we identify is specific to our reimplementation. During this period we resolved that with evidence: we implemented Pacchiardi et al.'s *own* detector faithfully (fixed yes/no probes → binary logistic regression), and it collapses to chance under the same equalization control (18–46 pp; pooled 87% → 36%) — exactly as our pipeline does. Two mechanistically distinct detectors failing under one control shows the confound is a property of the *paradigm*, not any single implementation.

We believe this, together with the 0.3% benign false-positive rate, is what distinguishes the paper from an ordinary negative result. Thank you again for your careful reading and for recognizing the core contribution.
