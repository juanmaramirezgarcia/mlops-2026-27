# Group Project — Evaluation Guide (professor only)

**Do not distribute.** This is the marking companion to `MLOps_Group_Assignment_2026-27.md`. It contains the rubric with descriptors, an answer key for each of the six cases (the issues each brief is engineered to surface, mapped to the four modules), and a scoring sheet template.

The project is worth **35%**. The syllabus fixes **four equally-weighted rubric dimensions**: technical soundness of the architecture; depth and clarity of documentation; quality of monitoring and governance design; and the team's defence of its decisions. This guide keeps those four and shows how Part A (diagnosis) and Part B (the five artefacts) feed each one.

---

## 1. How the two parts map to the four dimensions

The report has Part A (diagnose) and Part B (design the five artefacts). Both feed the rubric — a team cannot earn a dimension on Part B alone if the diagnosis that should drive it is missing.

| Rubric dimension (equal weight) | Fed mainly by | The question it answers |
|---|---|---|
| **1 · Technical soundness of the architecture** | Roadmap + CI/CD schematic + persona/RACI; the Part A findings in Modules 1–2 | Would this actually get the prototype into reliable production? Are the pipeline, environments, and ownership sound? |
| **2 · Depth and clarity of documentation** | The report as an artefact: readability, diagrams, the model card / decision log; how well findings are traced to fixes | Could the client act on this? Is it clear, honest, and complete, or hand-wavy? |
| **3 · Quality of monitoring & governance design** | Monitoring-and-retraining policy + governance framework; Part A findings in Modules 3–4 | Will they know when it breaks, and is it safe and legal? Are thresholds, triggers, ground-truth timing, EU AI Act tier, oversight, and documentation right? |
| **4 · Team's defence of its decisions** | The live defence | Do they own the plan? Can any member justify a choice under pressure and concede a real limitation? |

**Diagnosis quality is the multiplier.** A team that finds problems across all four modules and ranks them well will almost always score higher on 1–3, because their design has something to fix. A thin diagnosis (issues only in the module they found easiest) caps the whole report — note it explicitly in feedback.

---

## 2. The rubric (descriptors)

Score each dimension on the 1–4 band below; the band converts to the 10-point column on the scoring sheet (Excellent 9–10, Good 7–8, Satisfactory 5–6, Insufficient 0–4). The four dimension scores are averaged (equal weight) to the project mark.

### Dimension 1 — Technical soundness of the architecture

- **Excellent.** Roadmap is phased and lifecycle-anchored, not a tool wish-list; each phase has a clear "done." CI/CD schematic shows real gates (tests, data validation, model eval) and sensible triggers (push, schedule/CT, alert). Environments (dev/QA/prod) and reproducibility (versioned code + data, single source of truth for features) are addressed. Persona/RACI leaves no lifecycle stage without an accountable owner. The architecture visibly fixes the Module 1–2 issues the team diagnosed. Choices fit a non-technical, resource-real client.
- **Good.** Sound roadmap and pipeline with gates and triggers; minor gaps (e.g. environments implied not shown, or one stage without a clear owner). Fixes most diagnosed issues.
- **Satisfactory.** A pipeline and roadmap exist but are generic — could be pasted into any case; gates or triggers vague; reproducibility or environments not really addressed. Weak link to the diagnosis.
- **Insufficient.** Tool list rather than an architecture; no gates or triggers; no ownership; would not move this prototype to production. Ignores the case's specifics.

### Dimension 2 — Depth and clarity of documentation

- **Excellent.** A client could act on this. Clear structure (diagnosis → design), diagrams used where they beat prose (RACI, pipeline, monitoring), within the page limit with detail pushed to the appendix. Includes a real model card and a decision log. Every major fix traces back to a named problem. Honest about limits.
- **Good.** Clear and mostly complete; model card or decision log thin; some sections wordy where a diagram would serve; traceability mostly there.
- **Satisfactory.** Readable but shallow or padded; documentation artefacts (model card, decision log) missing or token; reader has to infer the reasoning.
- **Insufficient.** Disorganised, jargon-as-cover, over the limit or under-specified; no documentation artefacts; cannot be acted on.

### Dimension 3 — Quality of monitoring & governance design

- **Excellent.** Monitoring policy names what is measured, the **threshold**, **who is alerted**, and **what they then do** — actionable, not a metric list. Handles the case's hard truth (delayed/absent ground truth, fleet data that never returns, stale RAG index) explicitly. Retraining has a **trigger and an approval step**. For LLM cases, prompt/RAG/eval/guardrail/cost metrics are all present. Governance: correct **EU AI Act tier** with justification, right documentation, human oversight where it matters, a named governance owner, and controls wired into the pipeline. LLM cases address transparency; automated-decision cases address oversight and contestability.
- **Good.** Solid monitoring with thresholds and alerts and a retraining trigger; governance tier correct with most obligations; one weak spot (e.g. ground-truth timing glossed, or oversight named but not designed).
- **Satisfactory.** Monitoring is a list of metrics without thresholds or actions; retraining "periodically"; governance mentions the EU AI Act but the tier is wrong or unjustified; documentation named but not designed.
- **Insufficient.** No real monitoring (or "we'll watch accuracy" with no ground-truth plan); no retraining trigger; governance absent or wrong (e.g. calls a high-risk case unregulated). Misses the case's central monitoring challenge.

### Dimension 4 — Team's defence of its decisions

- **Excellent.** Any member can justify any part; answers the pushback (why this first, what if labels are late, who approves a retrain, which AI Act tier and why) with reasoning, not recitation. Concedes real limitations gracefully and says what they'd do next. Evidently a shared understanding.
- **Good.** Confident on their own sections; a couple of members carry the harder questions; handles most pushback.
- **Satisfactory.** Rehearsed presentation but thin under questions; one member answers everything; concedes little.
- **Insufficient.** Cannot explain their own artefacts; contradict each other; no engagement with the pushback.

---

## 3. Answer keys — the engineered issues, by case

Each brief plants weaknesses across **all four modules**, plus at least one *silence* (something an MLOps team should expect that the brief simply omits — naming the gap is a valid finding) and one **EU AI Act tier judgement** that separates strong teams. Use these as a checklist of what a full diagnosis should surface; teams may phrase differently or find extras — credit those.

### Case 1 — NorthRetail demand forecasting

- **M1 Foundations.** No owner after launch (the data scientist left; "nobody owns the model") — the central lifecycle failure. Model treated as static (hand-loaded quarterly). Business objective (cost of over- vs under-forecast, perishable waste) never tied to a monitored metric.
- **M2 Pipelines.** Lives in a notebook (not reproducible). Feature SQL on a laptop with two divergent copies — no single source of truth; **training/serving skew** (promotions and weather were static columns in training but are absent from the live feature pipeline). Model emailed and hand-loaded — manual deploy, no CI/CD, no versioning. No test environment; changes made directly on the prod ordering DB after hours.
- **M3 Monitoring.** No performance measurement since launch. The COVID anecdote is a **concept-drift / no-monitoring** failure (kept forecasting normal demand for weeks). No data-quality checks; no drift detection; retraining is a manual quarterly reload with no trigger.
- **M4 Governance.** Not an LLM. **Tier judgement:** demand forecasting is *not* Annex III high-risk — a strong team says so and right-sizes governance (documentation and ownership, not a heavy compliance apparatus). Still needs a model card and clear accountability. Weak teams over- or under-claim the tier.
- **Silence to catch:** no mention of what happens when a supplier order is obviously wrong — no human exception review on a €40M/week automated order.

### Case 2 — Corurbanco SME credit scoring

- **M1 Foundations.** 70% of decisions fully automated with no human; no clear internal owner of a vendor black box. Business objective vs lending-rule compliance not connected.
- **M2 Pipelines.** Vendor delivered only an endpoint — no training data or code, so **no reproducibility or auditability**. Single API unchanged for 14 months, no versioning/CI/CD. Trained on a decade of human underwriting decisions — **historical bias baked into the labels**. No decision logging beyond the score.
- **M3 Monitoring.** Performance "reviewed" once a year on 50 sampled files — inadequate. No drift monitoring. No check of approval rates by postcode/sector (**fairness/subgroup drift**). No retraining process.
- **M4 Governance.** **Tier judgement (the big one):** credit scoring / creditworthiness is **EU AI Act Annex III high-risk** — the compliance team's "internal tools don't apply" is wrong, and catching that is a strong signal. Obligations: right to an **explanation** for declines (also GDPR Art. 22 automated-decision territory), **human oversight** on the automated 70%, bias/fairness testing and documentation, logging, a model card and decision log. Postcode as a feature raises proxy-discrimination risk.
- **Silence to catch:** no process for a rejected applicant to contest a decision.

### Case 3 — PayFlux real-time fraud detection

- **M1 Foundations.** The model that blocks payments has an engineering owner but **no risk-side owner**. Error-cost trade-off (false block vs missed fraud) not managed.
- **M2 Pipelines.** Two separate feature implementations (real-time service vs batch training job) by different teams — the textbook **training/serving skew**. No automated pipeline; a senior engineer retrains locally and pushes on the weekend — manual, untested, no CI/CD, no rollback.
- **M3 Monitoring.** **Delayed ground truth** is the headline: labels settle weeks later via chargebacks, so "recent performance" is always stale — the policy must handle this (proxy metrics, block-rate/decline-rate monitoring in the interim). Threshold hard-coded once. Fraud patterns adapt = **concept drift** with no detection. Block-rate spikes discovered via customer complaints, not a dashboard — no operational alerting. Retrain "when someone notices" — no trigger.
- **M4 Governance.** **Tier judgement:** transaction fraud detection sits in a nuanced spot — often *not* treated as Annex III high-risk credit scoring (fraud detection is commonly carved out), but real-time blocking still needs an **audit trail, dispute handling, and transparency to affected customers**. Strong teams reason about the carve-out rather than reflexively stamping "high-risk." Documentation and a decision log for disputes.
- **Silence to catch:** no channel for a wrongly-blocked customer/merchant, and no monitoring of the *false-block* cost side at all.

### Case 4 — TurbineWorks predictive maintenance (edge)

- **M1 Foundations.** Builder keeps the training notebook on a personal drive — **bus factor / no ownership**. Error-cost trade-off (missed failure = line shutdown vs false alarm = wasted visit) unmanaged.
- **M2 Pipelines.** Not reproducible (personal notebook). **No versioning of which device runs which model** ("fairly sure they're all on v1"). One model copied to every device — no config/environment management for heterogeneous conditions. Firmware/model update is a manual push that has happened once in two years — effectively **no deployment path to the edge**.
- **M3 Monitoring.** **No field data returns** — the fleet cannot be monitored at all (the central failure). One model across very different operating conditions = **data/covariate drift** by design; new pump models are out-of-distribution. Problems only surface via customer complaints. No retraining channel and no way to close the loop.
- **M4 Governance.** **Tier judgement:** industrial predictive maintenance is generally *not* Annex III high-risk — right-size governance. But provenance, model/version documentation, and **auditability of which model raised which alert** matter (a missed failure could become a liability dispute). Edge-specific governance: traceability across the fleet.
- **Silence to catch:** no plan for the fact that customers depend on these alerts contractually — no SLA/accountability for a missed prediction.

### Case 5 — Helios Energy RAG assistant (GenAI)

- **M1 Foundations.** No owner. Business exposure: a wrong tariff/right-to-switch answer is a **commitment the company may have to honour** and a compliance risk — not connected to any control.
- **M2 Pipelines.** Prompt is a hard-coded string edited straight to production with no record — no versioning, no staging, no review (this is also an M4 LLMOps failure). No test/eval gate before changes ship. **Security: prompt injection already happened** (a user made it ignore its instructions).
- **M3 Monitoring.** No golden set and no evaluation — quality is vibes ("seemed fine in testing"). The document index was built once and is **stale** — retrieval of outdated tariffs is a **RAG-freshness** failure. No **grounding/faithfulness** check (hallucination risk on contractual facts). Cost is an unmonitored per-token surprise; nothing tracked per conversation.
- **M4 Governance (LLMOps core).** Full LLMOps set expected: **prompt versioning + environments; RAG grounding and index-refresh policy; evaluation via golden set + human review + LLM-as-a-judge; guardrails on input (injection, PII) and output (toxicity, format, grounding); cost/latency per request.** **Tier judgement:** a customer-facing assistant triggers the EU AI Act **transparency obligation** (users must be told they are interacting with AI — in force since Aug 2026); most likely limited-risk + transparency rather than high-risk, but the contractual-commitment angle raises the stakes. Human escalation path required; model card / decision log for prompt and index changes.
- **Silence to catch:** no human hand-off when the assistant is unsure, on a system that speaks for the company about contracts.

### Case 6 — Ribera Health readmission early-warning

- **M1 Foundations.** Built by a research team with no production owner; the data-governance office is unaware it is in live clinical use — a serious **accountability gap**. Clinicians have quietly stopped trusting it (adoption failure). Trade-off (missed high-risk patient vs alert fatigue) unmanaged.
- **M2 Pipelines.** Data pipeline built by a departed contractor and undocumented — **provenance/reproducibility failure**. Trained on one flagship hospital, deployed to twelve different populations with no per-site validation. No versioning.
- **M3 Monitoring.** Validated once at launch, never since; case-mix has shifted = **population/covariate drift** unmonitored. Labels (actual readmission) arrive at 30–60 days and are **available but never fed back** — a monitoring failure despite obtainable ground truth. Flagging too many patients = precision/alert-fatigue problem with no threshold management. No retraining.
- **M4 Governance.** **Tier judgement:** clinical decision support influencing patient care is **high-stakes** — likely EU AI Act high-risk and/or overlapping medical-device rules; strong teams flag the tier and the overlap. Missing: **model card, record of who approved clinical use, human oversight and a clinician override/challenge path** (currently a clinician can't contest the score), explainability (they see a number, not why — ties to Session 7 XAI), and data-governance sign-off.
- **Silence to catch:** no consent/DPIA or ethics record for using patient data in a live clinical model.

---

## 4. Scoring sheet (per team)

> **Case:** ___ **Team:** _______________ **Members:** ___________________________ **Date:** ______

**Part A — diagnosis health check** (informs the scores below; not a separate mark)

| Module | Issues found? (0 / partial / strong) | Notes |
|---|---|---|
| 1 · Foundations, personas, lifecycle | | |
| 2 · Pipelines, environments, deployment, security | | |
| 3 · Monitoring & retraining | | |
| 4 · GenAI specifics & governance | | |
| Ranking & prioritisation of issues | | |
| EU AI Act tier judgement correct & justified | | |

**Part B — the four rubric dimensions** (equal weight; band → 0–10)

| Dimension | Band (Exc/Good/Sat/Insuf) | Score /10 | Evidence & comments |
|---|---|---|---|
| 1 · Technical soundness of the architecture | | | |
| 2 · Depth & clarity of documentation | | | |
| 3 · Quality of monitoring & governance design | | | |
| 4 · Team's defence of its decisions | | | |

**Project mark** = average of the four scores = **____ / 10**  → contributes 35% of the course grade.

**Two things this team did best:**

**Two things that would have raised the mark:**

---

## 5. Defence — questions that separate the bands

Keep a few case-specific probes ready; the generic ones apply to every team.

**Generic (ask every team):** Which issue did you fix first, and why that one? Who signs off before a new model reaches production, and what stops a bad one? What does your monitoring make a specific person do, and when? Which EU AI Act tier is this, and how did you decide? What is the one limitation of your plan you're least comfortable with?

**Case-specific probes:**

- **1 · NorthRetail:** Your labels (actual sales) come in weekly — so what exactly do you monitor *between* retrains? What catches the next COVID-style shift before four months pass?
- **2 · Corurbanco:** Compliance says the AI Act doesn't apply to internal tools. Are they right? What do you tell a rejected applicant who asks why?
- **3 · PayFlux:** Ground truth is three weeks late. What do you watch in the meantime, and what would have caught the block-rate spike on day one instead of via complaints?
- **4 · TurbineWorks:** No data comes back from the devices. How do you monitor a fleet you can't see, and how do you know a given pump is even on the right model version?
- **5 · Helios:** Someone edits the prompt on Friday and tariffs are wrong on Saturday — what in your design stops that? How do you know an answer is grounded in a real document and not invented?
- **6 · Ribera:** A clinician disagrees with the score — what can they do? You have the readmission labels at 60 days; why isn't the model already being checked against them?

A team in the Excellent band answers these with reasoning and a graceful concession; a Satisfactory team recites the report; an Insufficient team cannot answer about their own artefacts.
