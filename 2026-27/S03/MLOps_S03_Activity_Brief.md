# Session 3 · Activity Brief

**MLOps: Machine Learning Operations · Session 3 · Saturday 10 October 2026**
*For students: posted on the virtual campus before the session. For the professor: facilitation notes in the last section.*

## Overview

| | |
|---|---|
| **When** | Minutes 58–86 of the live session (brief · 15 min in breakout rooms · 10 min debrief) |
| **Groups** | Rooms of 4–5 students (your group-project team) |
| **Output per room** | One slide or one whiteboard, presented by a spokesperson in 2 minutes |
| **Task** | A model-risk mitigation blueprint for a bank's card-fraud model |

*The chat poll ("A model that works on the laptop can go to production the same day if the business is in a hurry") is run during the session and continued as Theme A of Forum 2.*

---

## The case: IberBank card-fraud model (facts only)

IberBank issues about 6 million payment cards. A machine-learning model scores every card transaction in real time and decides whether to let it through or block it.

1. **What it does.** The model scores about 40 million transactions a month and must answer in under 150 milliseconds. Above a threshold, the transaction is blocked and the customer receives an SMS. Three channels call it: point-of-sale terminals, e-commerce, and ATMs.
2. **What it uses.** Three groups of features: the transaction itself (amount, merchant type, country, time); the customer profile, loaded every night from the data warehouse (tenure, average spend, home region); and "velocity" features computed by a streaming system (number and value of transactions in the last hour).
3. **How it is maintained.** The data-science team retrains it every quarter on confirmed fraud cases. The fraud operations team labels about 2,000 confirmed cases a month; chargebacks (the customer disputing a payment) arrive up to 60 days after the transaction.
4. **Incident 1 (March).** An external data vendor changed the unit of the "amount" field from euros to cents for a subset of merchants. For three days, thousands of legitimate purchases of €20–€50 were scored as if they were €2,000–€5,000 and blocked. Customer complaints reached the press.
5. **Incident 2 (June).** A fraud ring discovered that purchases just under €30 at grocery merchants were never blocked. Over two weeks they cycled about 1,200 stolen cards through such purchases. The pattern was found only when chargebacks arrived in August.
6. **Incident 3 (September).** After a spike in false positives, a data scientist pushed a "hotfix" to the threshold on a Friday evening from her laptop directly into production, skipping QA. The hotfix also changed how one velocity feature was calculated. False positives doubled over the weekend; nobody noticed until Monday.

### Your task

For each incident, fill a row of the blueprint. Then answer the bonus question.

| # | Threat (what happened) | Lifecycle stage where it enters | One control that would have prevented it | Who owns the control | How you would detect it (which lineage or monitoring signal) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

**Bonus:** which of the three incidents would a financial regulator care about most, and why?

**Vocabulary you can use**

- Lifecycle stages: data ingestion & versioning · data validation · data pre-processing · model training · model tuning · model analysis · model validation · model deployment · model feedback.
- The three checks of data validation: anomalies · schema · statistics.
- The three environments: Dev · QA · Prod, with Gate 1 (Dev → QA) and Gate 2 (QA → Prod).
- The three control families: information security (existing) · AI-specific · AI-system level.
- Personas: Business / Product owner · Data scientist · Data engineer · ML engineer · IT / DevOps · Risk & Compliance · (here also the fraud operations team).

---

## Facilitation notes (professor only)

### Timing

| Minute | Step |
|---|---|
| 58–60 | Brief from the activity slide; rooms open; brief on campus. |
| 60–61 | Read the case aloud from the case slide, facts only. Send them to rooms. |
| 61–76 | Rooms work. Visit stuck rooms; point them to the vocabulary box. Two-minute warning at 74. |
| 76–82 | Three rooms present, 2 minutes each. Pick one that did incident 1 well, one incident 2, one incident 3. |
| 82–86 | Synthesis with the debrief slide (expected mapping below), the bonus, the closing line. |

### The chat poll (minute 41–44, slide "What goes wrong when a model goes from a laptop straight to production")

Statement: "A model that works on the data scientist's laptop can go to production the same day if the business is in a hurry." AGREE/DISAGREE plus one line. Read two contrasting answers. Do not resolve; send to Forum 2, Theme A. The honest position, for the Friday synthesis: sometimes yes, for a low-risk internal model with a named owner and a rollback plan; never for a customer-facing or regulated decision. The point is not "always QA" but "the gate must be proportionate to the cost of being wrong".

### Expected mapping

| # | Threat | Enters at | Control | Owner | Detected by |
|---|---|---|---|---|---|
| 1 | Data-integrity: vendor changed units | Data ingestion / validation | Schema and range validation on the vendor feed (an amount of €5,000 at a grocery merchant is an anomaly); a data contract with the vendor requiring notice of changes | Data engineer (control), Product owner (contract) | Validation report per snapshot; a spike in blocked transactions per merchant; the lineage of the blocked predictions points at the same feed version |
| 2 | Adversarial evasion: probing the threshold | Inference / model feedback (also model design) | Monitor for probing patterns (many small transactions just under a band at one merchant type); never a fixed, guessable threshold (randomise, use bands); retrain on discovered patterns; rate limits per card | ML engineer with the fraud operations team | Transaction patterns by amount band and merchant type; late chargebacks confirm; a feedback loop that shortens the 60-day lag with early signals |
| 3 | Environment: hotfix from a laptop, skipping QA | Model deployment | The two gates: only a versioned, registered artefact can be deployed; QA sign-off by someone other than the author; rollback plan; IT enforces that nothing deploys from a laptop | Product owner (accountable), ML engineer (responsible), IT / DevOps (enforces) | Lineage: a change in production with no QA record; false-positive rate over the weekend against a threshold, with an alert to a human on call |

**Bonus.** Regulators care most about incident 3 (no human oversight, no record, a change affecting customers made without control) and about the customer impact of incident 1 (thousands of people blocked from paying). Under the EU AI Act, models that decide on access to financial services affecting people are treated as high risk, with obligations for logging, human oversight and risk management; Session 12.

### Closing line

"Every control you named is a step in the pipeline or a gate between environments. That is what MLOps is."

### Common misconceptions to correct

- "Retrain more often." Retraining would not have prevented any of the three; it would have made incident 1 worse (training on cents).
- "Lower the threshold." Any fixed threshold will be found by a determined ring; the control is detecting the probing, not moving the number.
- "Blame the data scientist for incident 3." She fixed a real problem the only way the system allowed; the failure is that the system allowed it. Push for the gate, not the person.
