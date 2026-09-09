# MLOps · Midterm Test — Answer Key (instructor)

**Do not distribute.** Coverage: Sessions 1–6. 15 questions, one correct answer each.

**Quick key:** 1‑C · 2‑B · 3‑D · 4‑B · 5‑C · 6‑A · 7‑D · 8‑C · 9‑B · 10‑A · 11‑C · 12‑B · 13‑A · 14‑D · 15‑B

Answer-letter spread: A ×3, B ×5, C ×4, D ×3. Coverage: S1 (Q1–5), S3 (Q6–10), S5 (Q11–15) — five per live session.

---

**1 — C** · *S1, "a model in production is a running process, not a file."* Operationalising means the model serves real requests continuously and has an accountable owner; a file with a good score is the *start*, not the finish. A and D invent thresholds/rules that were never taught (accuracy-only, 0.95 gate); B is false — pickled models deploy fine.

**2 — B** · *S1, "the world changes under the model."* Models decay because the live data distribution and business context shift away from the training conditions, even with frozen code — hence "retrain when, not if." A, C and D are physically wrong distractors (disk rot, throttling, precision loss) that a careful student rules out.

**3 — D** · *S1, personas & RACI ("six personas, nine hand-overs").* A stage has exactly one Accountable owner and possibly several Responsible doers; failures cluster at the hand-overs. A (multiple Accountable) breaks single-point accountability; B conflates R and A; D... correct. C is the common misconception that the builder owns everything forever.

**4 — B** · *S1, four categories of performance ("product metrics that impact business performance are what matter").* Model metrics are proxies; they can improve while the business metric stays flat, so the business outcome must be tracked. A is a non-sequitur (high AUC ≠ guaranteed impact); C contradicts the course; D jumps to a solution not supported by the evidence.

**5 — C** · *S1 opener, hidden technical debt.* The debt in ML systems is in data/feature dependencies and reproducibility (the "two divergent SQL copies on a laptop"), not ordinary code smells. A, B and D are ordinary software issues, not the ML-specific hidden debt.

**6 — A** · *S3, "a notebook is a workshop; a pipeline is a factory."* The defining traits are determinism (same order every time), built-in validation gates that can halt the run, and machine execution. B (compiled language), C (cloud storage) and D (schedule-only) are incidental or false.

**7 — D** · *S3, "version everything: code, data, models" + lineage.* Reproducibility/traceability needs versioned code, fingerprinted data snapshots, an experiment log and a model registry together. A destroys history by overwriting; B and C are informal and cannot reconstruct the exact data+model that produced a past prediction.

**8 — C** · *S3, "three environments, two gates."* The separation exists so nothing goes laptop→prod untested: QA mimics production and an accountable owner signs each gate. A and D misattribute the purpose to cost/speed; B overclaims (it does not *guarantee* accuracy).

**9 — B** · *S3, AI model security.* Reconstructing training-data attributes from query responses is **model inversion**. Distractors are the neighbouring threats students must separate: data poisoning (corrupting training data), model extraction (stealing a copy of the model), and concept drift (not a security attack at all).

**10 — A** · *S3/S5, data validation as a pipeline gate.* A data test placed early catches bad/out-of-range inputs and stops the line before wasting compute or shipping a flawed model (exactly what the S5 demo showed). B, C and D describe unrelated operations (sampling, encryption, containerisation).

**11 — C** · *S5, "tests for code, tests for data, tests for models."* A range/schema check on incoming features is a **data** test. A is a code (unit) test; B is a code/style test; D is a **model** test. Getting these three categories apart is the point of the question.

**12 — B** · *S5, "ship the artefact, not the file."* The artefact = model + code + config + exact environment + docs, containerised so it runs identically everywhere. A (size) is not always true and misses the point; C is false (models can be registered); D is a non-sequitur (containers don't change accuracy).

**13 — A** · *S5, rollout strategies.* Blue-green gives an instant traffic switch and an instant switch-back — the fit for zero-downtime + fast rollback. Shadow (B) never serves users so it isn't the release mechanism; C and D are exactly the risky practices the strategies exist to avoid.

**14 — D** · *S5, rollout strategies ("a way to make a mistake small").* Only D pairs correctly: shadow proves a model on real traffic without using its outputs. A misdefines canary (it's a small slice, not 100%), B misdefines A/B (it's for deciding by a metric, not zero downtime), C misdefines blue-green (the 1% slice is canary). Tests whether students hold the four definitions apart.

**15 — B** · *S5, A/B testing.* A valid A/B test fixes the primary metric, the decision threshold, and the assignment of users **before** starting, so the result is not chosen after the fact. A, C and D are deployment/aesthetic details irrelevant to the decision rule.
