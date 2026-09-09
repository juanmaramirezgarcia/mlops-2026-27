# MLOps · Final Test — Answer Key (instructor)

**Do not distribute.** Coverage: Sessions 1–12, weighted to the second half. 25 questions, one correct answer each.

**Quick key:** 1‑B · 2‑C · 3‑D · 4‑A · 5‑C · 6‑B · 7‑D · 8‑A · 9‑B · 10‑C · 11‑D · 12‑A · 13‑B · 14‑C · 15‑D · 16‑A · 17‑B · 18‑C · 19‑D · 20‑A · 21‑B · 22‑C · 23‑D · 24‑A · 25‑B

Answer-letter spread: A ×6, B ×7, C ×6, D ×6.

**Coverage weighting** (second-half weighted, as requested): Foundations/personas (S1) — Q1–3 · Pipelines, environments, security & deployment (S3, S5) — Q4–8 · Monitoring & drift metrics (S7, Video 1/S9) — Q9–16 · LLMOps (S10) — Q17–21 · Governance & regulation (Video 2/S12) — Q22–25. That is 17 of 25 questions on Sessions 7–12.

---

## Foundations, personas & lifecycle

**1 — B** · *S1, personas & "a running process, not a file."* The failure is an ownership/hand-over gap: a live model needs one Accountable owner watching it. A and C are seductive "make the model better" distractors that miss that the model was fine — nobody was watching it; D is false.

**2 — C** · *S1, "the world changes under the model."* Decay comes from a shifting world, not from code edits, so retraining is "when, not if." A and B are the exact misconceptions the slide corrects; D is too narrow (retraining is mainly about restoring performance, not only adding features).

**3 — D** · *S1, business/product metrics.* Model metrics are proxies and can move without the business metric following, so the outcome metric must be tracked. A and B contradict the course; C leaps to a solution the evidence does not support.

## Pipelines, environments, deployment & security

**4 — A** · *S3, "three environments, two gates."* The point is a tested path to production with accountable sign-off, not cost, speed, or a regulatory head-count. B, C and D misattribute the purpose.

**5 — C** · *S3, AI model security.* Corrupting the *training* data to steer behaviour is **data poisoning**; the controls are input validation/sanitisation, provenance/lineage, and anomaly detection on new data. The distractors name the neighbouring threats (extraction, evasion, inversion) with implausible "fixes," testing whether students both name the attack and match a real control.

**6 — B** · *S3, "version everything."* Reproducibility needs versioned code + fingerprinted data snapshot + experiment log + registry, together. A is informal; C destroys history by overwriting; D cannot reconstruct the exact data+model behind a past prediction.

**7 — D** · *S5, rollout strategies.* Serving a small slice (2%) to contain damage is **canary**. Blue-green switches all traffic at once (A); shadow serves no users (B); an A/B test is about deciding between versions by a metric, not about limiting blast radius (C).

**8 — A** · *S5, CI/CD/CT and MLOps maturity levels.* A scheduled auto-retrain-and-redeploy loop is **Continuous Training** — the capability above plain CI/CD. B is wrong (they already had CI); C and D are unrelated concepts.

## Monitoring & drift metrics

**9 — B** · *S7/Video 1, the three drifts.* Data drift = input distribution moves (label-free); concept drift = the input→target relationship moves (needs labels). A and D collapse distinct ideas; C reverses the label requirement — the single most common error, so it is the key distractor.

**10 — C** · *Video 1, "the evidence decides the timing."* Input and prediction/output drift need no ground truth and warn immediately; every label-based metric (A, B, and concept drift in D) must wait for the delayed labels, so they cannot be the *early* signal.

**11 — D** · *S7, the monitoring-plan template.* A rule = metric + what it detects + threshold with a window + action + accountable person. "A chart" (A) and internal model facts (B) or infrastructure details (C) are not monitoring rules.

**12 — A** · *Video 1, "accuracy lies when the event is rare."* Under heavy class imbalance, accuracy is dominated by the majority class; precision/recall or the confusion matrix expose that no fraud is caught. B is the trap; C is false (AUC would be ~0.5, not 99.5%); D does not help a model that flags nothing.

**13 — B** · *Video 1, "precision and recall trade through the threshold."* A higher threshold flags fewer positives, usually raising precision and lowering recall; the right operating point depends on the cost of each error. A and C are impossible in general; D is false — AUC is threshold-independent.

**14 — C** · *Video 1, "AUC ignores the threshold; calibration asks if the number can be trusted."* AUC is a threshold-free ranking measure; calibration is about whether predicted probabilities match observed frequencies. A reverses AUC's property; B and D are false (a high AUC does not imply calibration; calibration is not about latency).

**15 — D** · *Video 1, "overall passed while the North fired."* Aggregate metrics can hide a failing subgroup; segment-level monitoring catches it. A only samples the same blind aggregate more often; B (blind weekly retraining) and C (a global threshold change) never surface the failing segment.

**16 — A** · *Video 1, missing/late ground truth and the feedback-loop trap.* A model that blocks cases never observes their true outcome, so its false positives are invisible; a small random *let-through* sample restores the ground truth. B is false; C measures only the visible side and entrenches the blind spot; D suppresses the signal instead of measuring it.

## LLMOps

**17 — B** · *S10, "the prompt is code and the documents are data."* Because you configure rather than train, the discipline moves to versioning/testing/promoting/rolling-back prompts and index, with a registry, golden set and sign-off as controls. A and D are the bad practices the slide warns against; C misunderstands how LLM apps change behaviour (no base-model retrain needed).

**18 — C** · *S10, RAG anatomy (documents → chunks → embeddings → index → retrieval → …).* Stale answers come from a stale **index/retrieval** layer, not the frozen base weights (A), prompt length (B) or embedding size (D). Index-refresh is the control.

**19 — D** · *S10, evaluation: golden set + human + judge, "then the judge is measured."* The three are complementary, and the judge must itself be validated against human labels. A, B and C each over-trust a single method, which the course explicitly rejects.

**20 — A** · *S10, guardrails: input vs output, with a latency budget.* Injection/PII are checked on the way *in*; toxicity/format/grounding on the way *out*; all cost latency. B and C swap the sides; D denies the latency cost the course stresses.

**21 — B** · *S10, cost/latency arithmetic.* Cost ≈ requests × tokens × price (+ human review), reduced by caching. A, C and D substitute quantities (licence, parameters, GPU count) that do not scale with the per-token usage that actually drives LLM cost.

## AI governance & regulation

**22 — C** · *Video 2, "governance is controls, not documents."* The test is enforce-prove-catch: a step that enforces it, an artefact that proves it, a monitor that catches it failing. A, B and D describe paperwork, which the course says is intention, not governance ("every Session 10 company had the policy").

**23 — D** · *Video 2, EU AI Act risk tiers.* Creditworthiness/credit scoring is an Annex III **high-risk** use, carrying the high-risk obligations. A and B misplace the tier; C is the exact "internal tool is exempt" fallacy the course debunks.

**24 — A** · *Video 2, penalties and roles.* Prohibited-practice breaches reach up to €35M or 7% of global turnover (whichever is higher), and provider vs deployer obligations differ. B understates by three orders of magnitude; C ignores the tiered obligations; D is false — the Act has extraterritorial reach.

**25 — B** · *Video 2, NIST AI RMF.* The four functions are **Govern, Map, Measure, Manage**. A is Deming's PDCA cycle; C is the NIST *Cybersecurity* Framework (a deliberate trap for the well-read); D is invented. Two of the course's own knowledge-check questions ask students to place an activity in one of these four functions.
