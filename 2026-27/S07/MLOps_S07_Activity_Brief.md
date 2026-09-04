# Session 7 · Activity Brief

**MLOps: Machine Learning Operations · Session 7 · Saturday 24 October 2026**
*For students: posted on the virtual campus before the session. For the professor: facilitation notes in the last section.*

## Overview

| | |
|---|---|
| **When** | Minutes 58–86 of the live session (brief · 15 min in breakout rooms · 10 min debrief) |
| **Groups** | Rooms of 4–5 students (your group-project team) |
| **Output per room** | One slide or one whiteboard (the monitoring plan), presented by a spokesperson in 2 minutes |
| **Task** | A monitoring plan for a churn model: metrics, thresholds, actions, people |

*The chat poll ("If the drift monitor fires, the model should retrain and redeploy automatically, no human needed") is run during the session and continued as Theme A of Forum 4.*

---

## The case: TelcoNova churn model (facts only)

TelcoNova is a telecom operator with 2 million residential customers. A churn model helps the retention team decide whom to call.

1. **How it is used.** On the first day of each month the model scores all 2 million customers. The retention team calls the top 5% (about 100,000 customers) with an offer. A call costs about €4; a saved customer is worth about €300 a year.
2. **The model.** Features: tenure, monthly charges, support tickets, promotions received, contract type, region. Trained in June on the previous twelve months. Evaluation accuracy 82%. The model card sets the retrain trigger at "accuracy below 75% on the monthly labelled sample".
3. **Labels.** Whether a customer churned is known at the end of the following month: a 30-day lag. Retraining costs two days of a data scientist plus a review by the product owner.
4. **Change 1 (September).** A new pricing plan moved monthly charges up by €10–20 for about 40% of customers. The data team was not told.
5. **Change 2 (September–October).** A competitor launched fibre in two regions. Long-tenure customers there, who never churned, have started to leave.
6. **The symptom.** The retention team reports that October's call list "felt wrong": many loyal customers were not on it, and the saved-customers count fell 15% against September.

### Your task: the monitoring plan

Fill one row per metric. Every row must end in a threshold (a number and a window) and an action (what happens, and who is alerted).

| # | Metric | What it detects | Threshold (number + window) | Action · who is alerted |
|---|---|---|---|---|
| 1 | *(data drift)* | | | |
| 2 | *(data drift)* | | | |
| 3 | *(concept-drift signal, before labels)* | | | |
| 4 | *(performance, on labels, by segment)* | | | |
| 5 | *(operational)* | | | |

**Bonus.** One fairness check you would add to the plan, and one question from the model-risk assessment list (slide 27) that applies to this model.

**Vocabulary you can use**

- The three kinds of "worse": data drift (inputs moved; visible without labels) · concept drift (behaviour moved; needs labels; hides in segments) · performance decay (the symptom).
- The plan's four columns: metric · what it detects · threshold (number + window) · action + person.
- The loop: monitor → alert → retrain → validate → approve → redeploy.
- Two fairness numbers: equal error rates across groups · equal selection rates across groups.
- Personas: Product owner · Data scientist · Data engineer · ML engineer · IT / DevOps · Risk & Compliance · the retention team.

---

## Facilitation notes (professor only)

### Timing

| Minute | Step |
|---|---|
| 58–60 | Brief from the activity slide; rooms open; brief on campus. |
| 60–61 | Read the case aloud from the case slide, facts only. Send them to rooms. |
| 61–76 | Rooms work. Visit stuck rooms and ask "what does a false alarm cost here? and a missed one?" Two-minute warning at 74. |
| 76–82 | Three rooms present, 2 minutes each. Pick one with a good concept-drift signal, one with a segment in the performance row, one without (to contrast). |
| 82–86 | Synthesis with the debrief slide; the bonus; the closing line. |

### The chat poll (minute 33–35, slide "The cost of a false alarm, and the cost of a missed one")

Statement: "If the drift monitor fires, the model should retrain and redeploy automatically, no human needed." AGREE/DISAGREE plus one line. Read two contrasting answers; do not resolve; send to Forum 4, Theme A. The honest position for the Friday synthesis: automatic retraining is fine and often desirable (Session 5's continuous training); automatic *redeployment* without validation and a gate is how you would have deployed a model trained on the broken extract in Session 3. The loop has a human at "approve" for a reason; what can be automated is everything up to that point.

### Expected answers

| # | A strong answer |
|---|---|
| 1 · Data drift | Share of drifted input features, weekly, against the June reference: more than 30% of features drifted for two consecutive weeks → alert the ML engineer; check the extract with the data team; if confirmed, retrain on recent data. |
| 2 · Data drift | Distribution of monthly charges vs training (a distance, or the mean): mean up by more than €8 → same alert, plus ask the business "what changed?" (the pricing plan nobody announced). |
| 3 · Concept-drift signal | Something visible before labels arrive: the distribution of predicted risk by region and tenure band (a segment's mean moves more than 5 points), or the composition of the call list by region shifting sharply month on month → investigate with the business ("what changed in those regions?"). The business KPI (saved customers per campaign down more than 10%) as a second early signal → escalate to the product owner. |
| 4 · Performance, by segment | Accuracy (and recall of actual churners) on the month's labels, by region and by tenure band: below 75% overall, or below 70% in any segment with more than 200 customers → retrain with the new labels, consider region interactions; the product owner approves the new version (the gate). |
| 5 · Operational | The batch finished before the retention team starts (by 6 a.m. on day 1; else page IT), and the share of customers with missing features above 5% → hold the call list until the data team confirms. |
| Bonus · fairness | Selection rate of the call list by region and by tenure band; if unequal, a documented justification (the offer targets those most at risk, not a protected group). |
| Bonus · risk question | Contestability (can a customer who was not offered a discount complain, and to whom?) or fairness (is a region being systematically excluded?). |

### Common misconceptions to correct

- "Retrain every month automatically." It costs two days each time, and in September it would have trained on the new pricing data without anyone knowing why the numbers moved. Retrain on a trigger, with a human at the gate.
- Thresholds without windows ("alert if accuracy drops"). A number without a window fires on noise; a window without a number never fires.
- A plan with no segment. The overall accuracy fell two points; the North fell seventeen. Every performance row needs "by segment".
- Only labels, or only drift. Labels arrive 30 days late; drift alone never confirms. The plan needs the early signals and the confirmation.
- Watching only the model. The batch that finishes late is an outage; the missing features are the NorthRetail bug; the business KPI is the first thing the retention team noticed.

### Closing line

"Monitoring is not a dashboard. It is a list of numbers, each with a line and a person behind it."
