# Video 1 · Session 9 · Cue sheet: talk from prompts, not from the script

**MLOps · Master in Business Analytics and Data Science · MBDS-PT2026F · Video 1 (Session 9), Monitoring Metrics in Depth · 60 minutes, recorded in seven segments**

For each slide: the **point** (why it is there), **say it** (the cues in order, with the numbers you must get right, separated by ·), the **line to land**, and, on four slides, a **pause** for students to write their note. The full word-for-word script stays in the speaker notes if you lose the thread. Timings match the notes.

The shape: opening (1–2) → the drifts (3–7) → performance (8–12) → ground truth (13–15) → operational (16) → LLM deployments (17–20) → alerts in production, with the demo (21–24) → wrap-up (25). Record one segment per take; a mistake costs one segment, not the hour.

Three threads to pull all the way through, and the three things on slide 25: **the evidence decides the timing** (no truth needed → today; truth needed → late, partial or never), **every performance metric is a ratio of four boxes, at a threshold someone chose**, and **a metric is only a control when it is a rule** with a route and an action.

---

## Before recording: checklist

- [ ] Deck at full screen; this cue sheet on the second screen or printed (the notes are the backup)
- [ ] Demo prepared following `MLOps_S09_Demo_Script.md` (the day before: `update_venv_and_run.command` → 3 PASS, 5 FIRE, exit 1)
- [ ] Do Not Disturb on; camera off or small, bottom right
- [ ] Water; pace about 130 words a minute; a one-second pause at every slide change makes editing easy
- [ ] Say the four pause prompts (slides 7, 12, 13, 21): those slides hold the quiz answers
- [ ] After recording: chapter markers at the segment starts (0:00, 3:00, 13:30, 24:00, 31:00, 34:00, 45:00, 56:00); deck as PDF next to the video

---

## Opening (1–2)

### Slide 1 — Title *(0:00–1:00)*
**Point:** welcome, and what kind of lesson this is. **Say it like this:** first video lesson of the course · Session 7 was *why* models get worse and the plan; today the toolbox, metric by metric · what it measures, which failure it reveals · second half: the two things textbooks skip, **getting the truth** and **what an alert looks like in production** · ~60 minutes, seven segments, the label top-right tells you where you are · ten-question check at the end; keep a page of notes · very little maths. **Land:** "For every metric today, two questions: what would it catch, and what does it need to be computed?" **Ask:** —

### Slide 2 — Seven segments, two families *(1:00–3:00)*
**Point:** the map, and the note-taking habit. **Say it like this:** walk the table in one breath: drifts · performance · ground truth · operational · LLM · alerts (a demo with real files) · wrap-up · examples you know: **TelcoNova churn**, **IberBank fraud**, and an **HR assistant** that answers from policy documents · classical ML: eventually there is a right answer; LLM: usually no single right answer · the note habit: one line per metric, *"this metric would catch …, and it needs … to be computed"*. **Land:** "The quiz asks for both halves of that sentence." **Ask:** —

## Segment 1 · The drifts (3–7)

### Slide 3 — Two windows and five choices *(3:00–5:30)*
**Point:** every drift metric compares two windows; your choices decide if the alert means anything. **Say it like this:** the model is a photo of June; the world keeps moving; drift = distance between photo and world · **reference** (training data or the first good weeks) vs **current window** (last week, last month, last 10,000 requests) · too short = noise, too long = late · then the five choices on the slide: reference · window · threshold (from the cost of a false alarm vs a missed one, not a p-value alone) · weighting (drift in a feature the model ignores is noise) · segments (drift hides in a region) · Evidently, the cloud monitors, watsonx.governance compute the same distances. **Land:** "The tools compute the distance. These five choices are yours, and they are where monitoring succeeds or fails." **Ask:** —

### Slide 4 — Input drift *(5:30–8:00)*
**Point:** the inputs no longer look like the training inputs. **Say it like this:** the picture: monthly charges, June centred on **€62**, October on **€76**, a new pricing plan · numeric: a distance between curves (**Wasserstein**: how far you would move one pile of sand to make the other) or a test (**Kolmogorov–Smirnov**, a p-value) · categorical: **Jensen–Shannon** or chi-squared · two cautions: on big data, tests flag harmless changes, so read the distance · one drifted feature is a question, half of them is an alarm · catches: units, pricing, a new segment · misses: same inputs, new behaviour. **Land:** "It needs the inputs only: no labels, no waiting. Remember that for segment three." **Ask:** —

### Slide 5 — Prediction drift *(8:00–10:00)*
**Point:** the model's own outputs moved: the earliest warning you get. **Say it like this:** the drift people forget, and the most useful when labels are late · June: **12%** of customers above 50% risk; October: **21%** · needs only the logged predictions · why it matters: it summarises all input drifts *as the model sees them*, plus a hint of concept drift · catches: broken combinations, a deployment that flags everyone or nobody, a growing segment · misses: a model confidently wrong in the same proportions. **Land:** "For that you need labels, and that is the third drift." **Ask:** —

### Slide 6 — Concept drift *(10:00–12:00)*
**Point:** same inputs, different outcome. **Say it like this:** Session 7's demo: a competitor launched fibre in the North; long-tenure customers who never churned started leaving · tenure didn't move, region didn't move; behaviour moved · drift report: nothing; accuracy in that segment **89% → 65%** · you only *know* with labels, by segment, over time · you *guess early* with prediction drift, a shift in which features drive explanations, and the business KPI ("the call list feels wrong") · four shapes: sudden, gradual, seasonal (not drift if the model knows the season), recurring. **Land:** "It catches everything the other two miss. What it costs is waiting for the truth." **Ask:** —

### Slide 7 — The three drifts side by side *(12:00–13:30)*
**Point:** the summary table for the quiz. **Say it like this:** read across, one line each: input = the features moved, inputs only, daily · prediction = the outputs moved, predictions only, daily, the earliest warning · concept = the relationship moved, needs labels, monthly or later. **Land:** "The first two buy time while you wait for the third." **Pause:** "Stop here if you want to write your one-line notes for the three drifts."

*End of segment one.*
## Segment 2 · Performance (8–12)

### Slide 8 — The confusion matrix *(13:30–15:30)*
**Point:** one picture behind every performance metric. **Say it like this:** **1,000** customers scored in June · model flagged **250** · **200** actually churned · cross them: **140** flagged and left (true positives) · **110** flagged but stayed (false positives, called for nothing) · **60** left unflagged (false negatives, missed) · **690** stayed, not flagged (true negatives) · every metric in this segment is a ratio of these four. **Land:** "The rows are the truth. Without knowing who really churned, you cannot fill a single box. Hold that." **Ask:** —

### Slide 9 — Accuracy *(15:30–17:00)*
**Point:** how often the model is right, and why that can lie. **Say it like this:** (140 + 690) / 1,000 = **83%** · fine for balanced problems; churn at 20% is usable, with care · the fraud model: **10,000** transactions, **40** fraud; a model that blocks *nothing* scores **99.6%** and catches zero · accuracy rewards the majority. **Land:** "When someone says '99% accurate', ask first: how rare is the thing it predicts?" **Ask:** —

### Slide 10 — Precision, recall and the threshold *(17:00–20:00)*
**Point:** two metrics that trade against each other through one dial. **Say it like this:** precision: of what was flagged, how much was right · 140 / 250 = **56%** · low precision = wasted calls, customers wrongly blocked · recall: of what really happened, how much was caught · 140 / 200 = **70%** · low recall = churners never called, fraud that went through · retention: precision is money (each call €4); fraud: recall is money, precision is reputation · the model says 0.73, *someone* decides that above 0.5 means churn · threshold **0.3**: 400 flagged, recall 85%, precision 42% · **0.7**: 120 flagged, precision 75%, recall 45% · María chose 0.4 by looking at the test set; a retention manager should choose it from the budget · F1 compares models, it does not explain them. **Land:** "The threshold is a business setting, not a model property. Report the metrics at the threshold you actually use." **Ask:** —

### Slide 11 — AUC and calibration *(20:00–22:30)*
**Point:** "does it still rank?" versus "can I trust the number?". **Say it like this:** AUC without the curve: pick one churner and one stayer at random; AUC = probability the churner got the higher score · 0.5 coin toss, 0.8 good for churn, 1.0 perfect; the churn model in the Session 3 demo scored about **0.87** · good for comparing versions, says nothing about your threshold · calibration: take everyone scored 75–85%; did about 80% churn? if only 50% did, the model is overconfident · people act on the number: a **€50** discount to everyone "above 80%" wastes half the budget if 80% means 50% · curve bucket by bucket; one number, the Brier score; by segment too. **Land:** "Drift often breaks calibration before it breaks ranking: the order is still right, every score is too high. And both need the truth." **Ask:** —

### Slide 12 — Which metric for which decision *(22:30–24:00)*
**Point:** the decision picks the metric. **Say it like this:** read the left column as questions: balanced, right overall? accuracy · wasting effort on false alarms? precision · missing the cases that matter? recall · which model ranks better? AUC · can we trust the number to price an offer? calibration · always by segment, because the overall number hides the North · two habits: write the threshold next to the metric; store every prediction with model version and date, or the truth cannot be joined back. **Land:** "Look at the last column: every one of these needs the truth. Which brings us to the segment most courses skip." **Pause:** "Pause here to write your notes for the five metrics."

*End of segment two.*
## Segment 3 · Ground truth (13–15)

### Slide 13 — Which metrics need the truth *(24:00–26:00)*
**Point:** half the metrics in this video wait for the world to answer. **Say it like this:** ground truth = what really happened · in training it was in the dataset; in production it arrives from the world: slow, partial, sometimes silent · no truth needed: input and prediction drift, operational metrics (that is *why* they are early warnings) · truth needed: every performance metric, concept drift, fairness · LLM quality: the truth is a judgement, only for the sample someone judged · when it arrives: churn **30 days**, from billing, for everyone (the easy case) · fraud: chargebacks **30–90 days**, only if the customer complains · credit default **12 months**, only for those approved · forecast: end of period, only for what was in stock. **Land:** "An honest monitoring plan has a column that says when the truth arrives, and for how many cases." **Pause:** "Pause and note which metrics need the truth."

### Slide 14 — Four ways the truth goes missing *(26:00–29:00)*
**Point:** late, decoupled, partial, absent; the third is the trap. **Say it like this:** **late**: October's churn chart can only be drawn in November, credit a year later; meanwhile the dashboard should say "pending", not draw a flat line · **decoupled**: predictions keyed by transaction, chargebacks by card and date; nobody designed the join, so only half match, and not a random half · **partial**: IberBank blocks a payment, you never learn if it was fraud, because it never happened · a rejected loan never defaults · 100 units stocked, 100 sold, demand was maybe 150 · *selective labels*: truth only for the cases the model let through · **absent**: the HR assistant answers, the employee closes the window; the only truth is a judgement made later, for a sample. **Land:** "A model that blocks, rejects or limits is grading its own homework on the cases it chose to let through." **Ask:** —

### Slide 15 — Five practices for living without the truth *(29:00–31:00)*
**Point:** what you actually do about it; none is free. **Say it like this:** one, **proxies**: prediction drift, the business KPI, blocked customers who call to complain, thumbs down; they trigger investigation, never retraining on their own · two, **design the join before go-live**: id, timestamp, model version, an agreed key to the outcome · three, **backfill and recompute**: when labels land, fill October's slot, by segment · four, **random samples let through**: IberBank lets one in two hundred flagged payments through; the only honest measure of what the model hides; a cost, and a fairness question (whom does the model never learn about?) · five, **deliberate labelling**: pay for truth, e.g. 100 assistant conversations reviewed a week, 50 rejected loans audited a month. **Land:** "All five are cheaper than learning a month late that the model was wrong, or never learning at all." **Ask:** —

*End of segment three.*
## Segment 4 · Operational (16)

### Slide 16 — The machine's side *(31:00–34:00)*
**Point:** the metrics IT already collects, and why the average lies. **Say it like this:** latency: one prediction's time · throughput: predictions per second · error rate: requests that fail · none needs the truth, all are real-time · the bank queue: average wait **4 minutes**, but **one in twenty waits 25**; the percentile shows them, the average hides them · p95 = the time within which 95% are answered · "under 150 ms" must mean **p95** under 150 ms · model additions: missing or out-of-range inputs (the Session 3 checks, live) · batch on time: the churn list before the team starts at **06:00**; a late batch is an outage · cost per 1,000 predictions next to accuracy · freshness: NorthRetail ran **four months** (February to June) on empty features. **Land:** "When you see a latency number, ask: which percentile?" **Ask:** —

*End of segment four.*
## Segment 5 · LLM deployments (17–20)

### Slide 17 — What is different with a language model *(34:00–36:30)*
**Point:** four differences that change the metrics. **Say it like this:** new running example: an internal HR assistant answering from policy documents (a RAG system; Session 10 builds it) · one: usually **no single right answer**, so quality is *judged*, and then we measure the judge; segment three's "absent truth" is the normal case here · two: **the model is rarely yours**; what drifts is the prompt, the documents and the questions · three: **cost is per token**; a verbose answer or a pasted document costs more · four: **new failures**: confident falsehoods, offensive output, leaked personal data. **Land:** "Human feedback matters more here than anywhere: it is often the only label you will ever get." **Ask:** —

### Slide 18 — Judge, then measure the judge *(36:30–39:00)*
**Point:** three ways to judge quality, and where each fits. **Say it like this:** **reference-based** (ROUGE, BLEU, similarity): compare with an approved answer; cheap, but needs a reference, so it runs on a **golden set** of questions, on every change to prompt, model or documents · **judge-based**: another model scores the answer against a rubric (correct, complete, faithful, 1–5), given the question and the retrieved passages; scales to live traffic; check it against humans, because judges prefer long answers · **human review**: the gold standard, expensive; e.g. 100 conversations a week by the HR team, same rubric as the judge. **Land:** "Golden set on every change, judge daily, humans weekly: deliberate labelling made routine." **Ask:** —

### Slide 19 — The failures you count on every request *(39:00–41:30)*
**Point:** hallucination, toxicity, personal data, and losing the ground. **Say it like this:** **hallucination rate**: answers not supported by the sources; a judge checks each claim, humans confirm a sample; an invented number of holiday days has legal consequences; in the Air Canada case (Session 10) a tribunal made the airline pay for what its chatbot had invented · **toxicity (HAP)**: hate, abuse, profanity, in both directions · **PII**: names, identifiers, salaries; any PII in an output is an incident, not a trend · retrieval systems add two halves: **retrieval quality** (was the right passage found? hit rate on the golden set) and **groundedness** (was the answer built from it? correct but ungrounded is still a failure). **Land:** "After a policy update, groundedness tells you whether the assistant answers from the new policy or from memory." **Ask:** —

### Slide 20 — Tokens, feedback and the three drifts *(41:30–45:00)*
**Point:** the operational side, the label you can get, and what drifts. **Say it like this:** latency in two parts: time to first token and total time, p95 of both · tokens in (question + passages + instructions) and out; the passages usually dominate, so a retrieval change can double the cost · cost = tokens × price, with a budget line; cost drift is real · feedback: thumbs up/down (biased, still the best daily signal), escalation and rephrasing, resolution rate, the weekly human review · three drifts: the **questions** (new topics), the **documents** (a policy update), the **answers** (longer, more refusals) · store every conversation with prompt, document-set and model versions. **Land:** "Vendor dashboards put all of this on one screen. Different vendors, same families. Next: what happens when a number crosses a line." **Ask:** —

*End of segment five.*
## Segment 6 · Alerts in production (21–24)

### Slide 21 — An alert is a rule *(45:00–47:30)*
**Point:** a monitoring plan is a short list of rules, not twenty charts. **Say it like this:** six parts: metric · threshold · window · severity (wake someone at 3 a.m., or post to a channel?) · route (who receives it) · action (what they do) · on screen, `alerts.yaml`, eight rules for TelcoNova churn, in the demo folder · read **drifted-features**: how many of the model's **six** inputs drifted vs June; **two or more** fires; weekly; trend; Slack channel and ML engineer; check the extract, retrain if confirmed · **missing-features**: tenure missing for more than 5%; incident; page on-call; hold the call list (the NorthRetail bug, as a rule) · the performance rules say "monthly, when labels arrive": segment three, written into the file · the accuracy rule exists twice, overall and by segment, with a minimum size so twelve customers cannot page anyone. **Land:** "A rule without a route and an action is a chart, not a control." **Pause:** "Pause here and write the six parts of a rule."

### Slide 22 — Demo 1: the monitoring job *(47:30–51:00)*
**Point:** the job evaluates the rules and exits with a code. **Say it like this:** cut to the screen recording (`MLOps_S09_Demo_Script.md`, Demo 1) · `python run_alert_checks.py`, about ten seconds · three PASS: nothing missing; accuracy overall **0.80** (above 0.75: "the model is fine"); batch at **05:42** · five FIRE: **2 of 6** inputs drifted; charges mean **76.5** vs 70; prediction drift **0.116** vs 0.10; **North, tenure 3y+, 0.65 on 349 customers**; p95 latency **659 ms**, tagged incident · `echo $?` → **1**. **Land:** "The overall rule passed and the segment rule fired: that is why the rule exists twice. And exit code one is how a scheduler knows something is wrong without understanding any metric." **Ask:** —

### Slide 23 — Demo 2: scheduler, message, report *(51:00–54:00)*
**Point:** nobody runs it by hand; a message finds a person. **Say it like this:** screen recording, Demo 2 · `monitoring.yml`: Monday 06:00 for drift, the 2nd of the month 07:00 once labels arrive, plus on demand · steps: fetch, run the rules · `if: failure()`: send the message only when a rule fired · `if: always()`: keep the report, above all when something fired · GitHub Actions because you saw it in Session 5; cron or Airflow do the same · the message: five alerts, each with value vs threshold, action and recipient; the incident pages IT · the report's Tests tab: 1 success, 3 fail. **Land:** "Scheduler, job, exit code, message, person, report. Two schedules, because the truth has its own calendar." **Ask:** —

### Slide 24 — One page for the owner, and the rule against alert fatigue *(54:00–56:00)*
**Point:** the owner needs one page; the responder gets the alerts. **Say it like this:** top: health tiles (batch 05:42, missing 0%, drifted 2 of 6) and the dates (snapshot, retrain, model version) · middle: accuracy by segment on the monthly labels, with the threshold; on the right, **October: pending, labels due 2 November**; the chart does not pretend · bottom: predicted risk vs reference (needs no labels) and the KPI: saved customers **4,120 → 3,500** · the six feature histograms live one click deeper · the HR assistant's page has the same shape · the fatigue rule: every alert answered within a defined time; anything that fires weekly without action is reviewed or deleted · our demo fired five in one run; every Monday, and by November nobody reads the channel. **Land:** "Five alerts that always mean something beat fifty that sometimes do." **Ask:** —

*End of segment six.*
## Segment 7 · Wrap-up (25)

### Slide 25 — Three things, and the knowledge check *(56:00–60:00)*
**Point:** what to remember, and what happens next. **Say it like this:** one: three drifts, the evidence decides the timing; input and prediction drift warn today; concept drift and performance wait for labels, late, partial or never; "pending" is honest; a blocking model hides its own false positives · two: every performance metric is a ratio of four boxes at a threshold someone chose; overall passed, the North fired · three: a metric is a control only when it is a rule, a job that exits 1, a scheduler on the truth's calendar, a message that finds a person; for an LLM, a judge in place of the label and humans to check the judge · the check: on the campus after this video, **ten questions, about twelve minutes**, each a symptom → which metric, and what it needs · individual, no AI tools · counts towards continuous assessment · open until **Friday 30 October, 23:59** · demo files on the campus. **Land:** "See you on Saturday 31 October for Session 10, where we build the assistant we have just learned to monitor." **Ask:** —
