# MLOps · Module Concept-Check Quizzes — Answer Key (instructor)

**Do not distribute.** Four quizzes, five questions each. One correct answer per question.

**Quick key**

- **Module 1:** 1.1‑B · 1.2‑A · 1.3‑C · 1.4‑B · 1.5‑D
- **Module 2:** 2.1‑C · 2.2‑B · 2.3‑A · 2.4‑D · 2.5‑B
- **Module 3:** 3.1‑A · 3.2‑C · 3.3‑B · 3.4‑A · 3.5‑C
- **Module 4:** 4.1‑A · 4.2‑A · 4.3‑D · 4.4‑C · 4.5‑B

---

## Module 1 — Foundations, personas & lifecycle

**1.1 — B.** Operationalising = putting the model into production as a live service with an accountable owner; training just produces a scored file. (*S1: "a running process, not a file."*)

**1.2 — A.** Models decay because the data and world shift under them, even with unchanged code — hence "retrain when, not if." The other options are physically false. (*S1: "the world changes under the model."*)

**1.3 — C.** A stage has exactly one Accountable owner (many can be Responsible). Sharing or removing accountability is the failure the course warns about. (*S1: personas & RACI.*)

**1.4 — B.** The business/product outcome the model is meant to move is what ultimately matters; model scores are proxies. (*S1: four categories of performance.*)

**1.5 — D.** "A model in production is a **running process**, not a **file**." (*S1, key phrase.*)

## Module 2 — Pipelines, environments, deployment & security

**2.1 — C.** A pipeline runs the same steps in order automatically, with checks that can halt it; a notebook is run by hand. (*S3: "a notebook is a workshop; a pipeline is a factory."*)

**2.2 — B.** Dev builds, QA tests as if live, Prod serves — with a sign-off gate between them. (*S3: three environments, two gates.*)

**2.3 — A.** Corrupting the training data with bad/mislabelled examples is **data poisoning**. Concept drift is not an attack; a canary and a unit test are unrelated. (*S3: AI model security.*)

**2.4 — D.** A container ships the model together with its code and exact environment so it runs identically everywhere. It does not change accuracy or cost. (*S5: "ship the artefact, not the file."*)

**2.5 — B.** A **canary** releases to a small slice of traffic first to limit the blast radius. (*S5: rollout strategies.*)

## Module 3 — Monitoring, drift & retraining

**3.1 — A.** Data drift = the input distribution changes versus training. The other options are unrelated operational events. (*S7 / Video 1: the three drifts.*)

**3.2 — C.** Input (data) drift needs no labels, so it warns early; precision, recall and F1 all require the true outcomes. (*Video 1: "the evidence decides the timing."*)

**3.3 — B.** A useful alert needs a threshold, an action, and a person to notify — otherwise it is just a chart or an ignored alarm. (*S7: the monitoring-plan template.*)

**3.4 — A.** With a rare event, high accuracy can hide that the model catches nothing; precision/recall reveal it. (*Video 1: "accuracy lies when the event is rare."*)

**3.5 — C.** Retrain when a monitored signal crosses its threshold (drift detected or performance dropped) — not "never," not only on code changes, not on a rigid calendar alone. (*S7: retraining triggers.*)

## Module 4 — GenAI (LLMOps) & governance

**4.1 — A.** With an LLM you mostly configure behaviour through prompts (which you version) rather than training from scratch. (*S10: "the prompt is code."*)

**4.2 — A.** RAG grounds answers in documents retrieved from a knowledge base and passed to the model as context. (*S10: RAG anatomy.*)

**4.3 — D.** Use a golden set, human review, and an LLM-as-a-judge together — no single method is enough. (*S10: evaluation.*)

**4.4 — C.** Credit scoring is a **high-risk** use under the EU AI Act, carrying obligations like human oversight, transparency and logging. (*Video 2: risk tiers.*)

**4.5 — B.** The NIST AI RMF functions are **Govern, Map, Measure, Manage**. (Option D is the NIST *Cybersecurity* Framework — a common mix-up.) (*Video 2: NIST AI RMF.*)
