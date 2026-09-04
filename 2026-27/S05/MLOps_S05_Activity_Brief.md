# Session 5 · Activity Brief

**MLOps: Machine Learning Operations · Session 5 · Saturday 17 October 2026**
*For students: posted on the virtual campus before the session. For the professor: facilitation notes in the last section.*

## Overview

| | |
|---|---|
| **When** | Minutes 58–86 of the live session (brief · 15 min in breakout rooms · 10 min debrief) |
| **Groups** | Rooms of 4–5 students (your group-project team) |
| **Output per room** | One slide or one whiteboard (the rollout card), presented by a spokesperson in 2 minutes |
| **Task** | Choose how version 2 of a bank's card-fraud model reaches customers |

*The chat poll ("A model that passed all automated tests can be released to 100% of customers at once") is run during the session and continued as Theme A of Forum 3.*

---

## The case: IberBank card-fraud model, version 2 (facts only)

IberBank's card-fraud model (Session 3) has a new version. The engineering team says it is ready. The question is how it reaches customers.

1. **Version 1** has been in production since March: about 40 million transactions a month, answering in under 150 ms, across three channels (point of sale, e-commerce, ATM). It blocks about 0.4% of transactions; roughly one in three blocks turns out to be a false positive (a legitimate purchase).
2. **Version 2** passed validation last week. On the evaluation set it catches 9% more fraud at the same false-positive rate, and the fairness check by region passed. It uses two new "velocity" features from the streaming system (spend and count in the last hour).
3. **Constraint 1 · zero downtime.** Card payments run 24/7. A minute without scoring means every transaction in that minute is either blocked or waved through; both cost money and reputation.
4. **Constraint 2 · the regulator.** After the March incident (Session 3), the regulator requires proof on real traffic that version 2 is at least as safe as version 1 *before any customer is affected by it*.
5. **Constraint 3 · budget.** Infrastructure allows a second production copy of the model for at most four weeks.
6. **Constraint 4 · operations.** The fraud operations team can review about 300 flagged transactions a day; above that, reviews are skipped. Chargebacks (the ground truth for fraud) arrive up to 60 days after the transaction.

### Your task: the rollout card

| Question | Your answer |
|---|---|
| **Plan.** Which strategies, in which order, with what traffic slices and for how long? | |
| **Why not the others?** One line per strategy you rejected. | |
| **A/B decision rule.** Metric · threshold · how much traffic before deciding. | |
| **Rollback trigger.** Which number, watched by whom (or what), makes you stop, and what "stop" means. | |
| **Who signs each step.** | |
| **Bonus.** One automated test you would add to the CI pipeline for this model (code, data or model layer). | |

**Vocabulary you can use**

- Strategies: basic · blue-green · shadow · canary · A/B test, and the scorecard (zero downtime, extra cost, customer risk, what you learn, rollback).
- The three ingredients of an A/B test: a metric · a threshold · enough traffic.
- The test pyramid: code tests · data tests · model tests.
- Personas: Product owner · ML engineer · IT / DevOps · Risk & Compliance · fraud operations team.

---

## Facilitation notes (professor only)

### Timing

| Minute | Step |
|---|---|
| 58–60 | Brief from the activity slide; rooms open; brief on campus. |
| 60–61 | Read the case aloud from the case slide, facts only. Send them to rooms. |
| 61–76 | Rooms work. Visit stuck rooms; ask "what does the regulator want to see?" Two-minute warning at 74. |
| 76–82 | Three rooms present, 2 minutes each. Pick one with shadow, one with canary only, one with blue-green, if they exist. |
| 82–86 | Synthesis with the debrief slide; bonus; closing line. |

### The chat poll (minute 31–35, slide "The artefact travels in a box")

Statement: "A model that passed all automated tests can be released to 100% of customers at once." AGREE/DISAGREE plus one line. Read two contrasting answers; do not resolve; send to Forum 3, Theme A (the rollback drill). The honest position, for the Friday synthesis: automated tests tell you the model is not broken; they cannot tell you how customers, fraudsters or the business react. Rollout strategies exist because passing tests is necessary, not sufficient.

### Expected answers

| Question | A strong answer |
|---|---|
| Plan | **Shadow** for two to three weeks: v2 scores every transaction alongside v1, answers logged, compared with v1's decisions and with confirmed fraud as it arrives; this is the regulator's proof on real traffic, inside the four-week budget. Then **canary by channel**, e-commerce first (most fraud, least in-person friction), 5% → 25% → 100%, over one to two weeks, with an A/B rule inside the canary. Then the other channels. |
| Why not the others | Basic: violates zero downtime and exposes everyone at once. Blue-green alone: the switch exposes everyone at once and gives no proof on real traffic before customers are affected; acceptable as the *mechanism* for the final 100% step. Canary alone: affects customers before the regulator's proof exists. A/B alone: half of customers exposed immediately. |
| A/B rule | Metric: confirmed fraud caught per 1,000 flagged transactions, at a false-positive rate no higher than v1's. Threshold: v2 wins if at least 5% better with false positives not worse. Traffic: enough that the difference is not luck; at least a full week including a weekend; the statisticians set the exact number. Note the 60-day lag: use early signals (chargebacks that arrive within the week, manual confirmations from the fraud team) and revisit after 60 days. |
| Rollback trigger | Any of: false-positive rate more than 10% above v1's for one hour; more than 300 flags a day (operations cannot cope); p95 latency above 150 ms. Watched by an automated monitor that pages the on-call ML engineer; "stop" = shrink the canary to 0% (v1 still serves everything), then investigate. Written before the rollout starts, not during. |
| Who signs | Product owner: the go from shadow to canary, and the full rollout. Risk & Compliance: the regulator's evidence package from the shadow phase. ML engineer: responsible for executing each step. IT / DevOps: confirms capacity for the second copy. |
| Bonus | A latency test in the model layer (score 1,000 sample transactions; p95 under 150 ms), a fairness-by-region test, or a data test on the two new velocity features (freshness: computed within the last hour). |

### Common misconceptions to correct

- "Shadow is enough." Shadow tells you what v2 *would* have decided; it does not tell you how fraudsters adapt or how many customers complain. Hence the canary.
- "Blue-green is zero downtime, so it satisfies the regulator." Zero downtime is constraint 1; the regulator is constraint 2, and blue-green gives no evidence on real traffic before the switch.
- "The metric is accuracy." With 0.4% blocks, accuracy is 99.6% for a model that blocks nothing. The metric must be fraud caught at a fixed false-positive rate.
- "We will decide the rollback when we see a problem." The trigger is written before; that is the whole point of a trigger.

### Closing line

"Every strategy is a way to make a mistake small. The pipeline decided the change was safe; the rollout decides how many customers find out if it wasn't."
