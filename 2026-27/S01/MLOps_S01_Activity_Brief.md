# Session 1 · Activity Brief

**MLOps: Machine Learning Operations · Session 1 · Saturday 3 October 2026**
*For students: post on the virtual campus before the session. For the professor: facilitation notes are in the last section.*

## Overview

| | |
|---|---|
| **When** | Minutes 58–86 of the live session (brief · 15 min in breakout rooms · 10 min debrief) |
| **Groups** | Rooms of 4–5 students (your group-project team, where already formed) |
| **Output per room** | One slide or one whiteboard, presented by a spokesperson in 2 minutes |
| **Task** | Diagnose a failed deployment (15 min) |

*The business-value debate ("Is MLOps an unnecessary cost for a company with three models?") is run as a two-minute chat poll during the session and continued as Theme A of Forum 1, not as a breakout.*

---

## Diagnose a failed deployment (15 minutes)

### The case: NorthRetail demand forecast (facts only)

NorthRetail is a grocery chain with 400 stores. In the previous year it commissioned a demand-forecast model to decide how much of each product to send to each store every week.

1. **January.** A data scientist delivers the model. Accuracy on last year's data: 92%. The project is declared complete and the data scientist moves to another project. IT wraps the model in a service that the replenishment system calls every night.
2. **February.** A new supplier system changes the product codes for about a third of the catalogue. The model keeps running: the affected features arrive empty, and the model treats empty values as zero.
3. **March.** The commercial team moves from monthly promotions to weekly promotions. Nobody tells the data team; the promotion calendar the model uses is still the monthly one.
4. **April.** The data scientist leaves the company. The model has no documented owner. Her notebook is on a laptop that was returned to IT.
5. **January to June.** IT's dashboard shows the forecasting service as "green" every single day: the service is up, and it answers in 40 milliseconds.
6. **June.** Out-of-stock incidents are up 18% year on year; overstock write-offs reach €2.1 million. The model is switched off and replaced by last year's manual spreadsheets. The board asks: "How did nobody see this coming?"

### Your task

Four things went wrong. For each one, fill a row of the template below. Then answer the bonus question.

| # | What went wrong | Lifecycle stage where it originated | Persona who should have caught it | One control that would have prevented it |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

**Bonus:** what should IT's dashboard have shown, in addition to "up" and "40 ms"?

**Vocabulary you can use**

- Lifecycle stages: data ingestion & versioning · data validation · data pre-processing · model training · model tuning · model analysis · model validation · model deployment · model feedback.
- Personas: Business / Product owner · Data scientist · Data engineer · ML engineer · IT / DevOps · Risk & Compliance.

---

## Facilitation notes (professor only)

### Timing

| Minute | Step |
|---|---|
| 58–60 | Brief the activity from the activity slide; confirm rooms are open and the brief is on campus. |
| 60–61 | Read the case aloud from the case slide, facts only, no diagnosis. Send them to rooms. |
| 61–76 | Rooms work. Visit rooms that are stuck and point them to the vocabulary box. Two-minute warning at 74. |
| 76–82 | Three rooms present, 2 minutes each. |
| 82–86 | Your synthesis with the debrief slide: the expected mapping, the misconceptions, the closing line. |

### The chat poll (minute 23–27, slide "Why managing models at scale is hard")

Statement on screen: "MLOps is an unnecessary cost for a company with only three models in production." Everyone types AGREE or DISAGREE plus one line. Read two contrasting answers aloud and do **not** resolve it; send it to Forum 1, Theme A. The argument that decides it, for the Friday synthesis: **the cost of MLOps scales with the cost of being wrong, not with the number of models**. Three loan-pricing models and three banner-colour models are different problems. Secondary points: a company with three models today usually has ten in two years; the cheapest MLOps is a named owner and a monthly check of one business metric.

### Expected mapping

| # | What went wrong | Stage | Persona | Control |
|---|---|---|---|---|
| 1 | Product codes changed; features arrived empty and were read as zero | Data validation (also data ingestion) | Data engineer, with the ML engineer | A schema and range check that stops the pipeline and raises an alert when a feature is unexpectedly empty |
| 2 | Promotions moved from monthly to weekly; model logic outdated | Model feedback / monitoring (the change is a business change) | Product owner should have informed; ML engineer should have detected | Performance and drift monitoring with a retraining trigger; a change-notification rule between business and data teams |
| 3 | Data scientist left; no owner, notebook on a laptop | Governance / accountability (cross-cutting) | Product owner accountable; Risk & Compliance informed | A model registry entry with a named owner, versioned code and documentation; hand-over as a condition of "done" |
| 4 | Dashboard watched uptime and latency only | Model deployment / monitoring (system vs model performance) | IT / DevOps together with the ML engineer | Monitor prediction quality (forecast error against actuals as they arrive) and business metrics (out-of-stock rate), not only system health |

**Bonus answer.** Forecast error per week as actual sales arrive; share of features arriving empty; a "last retrained on" date; out-of-stock and overstock rates as business guardrails.

### Closing line

"Everything you just proposed is a session of this course." Point to the course map: validation and ownership (Session 3), automated checks (Session 5), monitoring and retraining triggers (Session 7), governance (Session 12).

### Common misconceptions to correct

- "The data scientist should have caught everything." She was not there after April, and most of the failures are not modelling failures. Push for the persona who was *in a position* to notice.
- "More accuracy would have prevented this." No: 92% on last year's data was fine. The model was correct for a world that stopped existing in February.
- "IT's dashboard was wrong." It was right about what it measured. The failure is that nobody defined model performance as something to measure.
