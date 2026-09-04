# Video 1 · Session 9 · Monitoring Metrics in Depth

**Recording guide, segment plan and the knowledge check (with answer key)**
*Deck: `MLOps_S09_Video1_Monitoring_Metrics_in_Depth.pptx` (25 slides; the segment label sits top-right on every slide). The speaker notes of every slide contain the recording script, with minute marks. Demo files for segment 6 are in `S09/demo/`.*

---

## 1. What this is

A self-paced 60-minute video lesson, released on Saturday 24 October together with Session 7 and open until Friday 30 October. It is the technical deep-dive the syllabus promises for Session 9: a systematic catalogue of monitoring metrics for classical ML and for prompt/LLM deployments, with a ten-question knowledge check that counts towards continuous assessment (15% of the course, shared with the module quizzes and Video 2's check).

Session 7 teaches the concepts (why models get worse, the monitoring plan, the loop). The video teaches the metrics one by one, and adds two things the textbooks skip: **ground truth** (segment 3: which metrics need to know what really happened, why that truth arrives late, partially or never, and what to do about it) and **alerts in production** (segment 6: a screen-recorded demo of a rules file, the monitoring job that evaluates it, the scheduler that runs it and the message a person receives). Forum 4 stays on decisions and thresholds and points students to the video for definitions; its Theme C ("ground truth arrives late") is the bridge to segment 3.

## 2. Segment plan

Record in segments; each is a separate take and a separate chapter marker on the campus player, so students can rewatch one topic.

| Segment | Slides | Minutes | Content | Running example |
|---|---|---|---|---|
| Opening | 1–2 | 0:00–3:00 | Title; the map of seven segments; "this metric would catch …, and it needs … to be computed" | — |
| 1 · The drifts | 3–7 | 3:00–13:30 | Two windows and five choices (reference, window, threshold, weighting, segments); input drift; prediction drift; concept drift; side-by-side table | TelcoNova churn |
| 2 · Performance | 8–12 | 13:30–24:00 | The confusion matrix (1,000 customers; "the rows are the truth"); accuracy and why it lies; precision and recall through the threshold; AUC and calibration; which metric for which decision, with a "needs the truth?" column | TelcoNova churn, IberBank fraud |
| 3 · Ground truth | 13–15 | 24:00–31:00 | Which metric families need the truth, when it arrives and for how many cases; four ways it goes missing (late, decoupled, partial/selective labels, absent); five practices (proxies, design the join, backfill, random samples let through, deliberate labelling) | IberBank fraud, credit, NorthRetail, HR assistant |
| 4 · Operational | 16 | 31:00–34:00 | Latency (p95, the bank queue), throughput, error rate; batch on time; cost per thousand; freshness | IberBank fraud, NorthRetail |
| 5 · LLM deployments | 17–20 | 34:00–45:00 | What is different; judge then measure the judge (three methods); hallucination, HAP, PII, retrieval quality and groundedness; tokens and cost, feedback, the three drifts of an LLM app | HR policy assistant (RAG) |
| 6 · Alerts in production | 21–24 | 45:00–56:00 | Anatomy of a rule (`alerts.yaml`, eight rules); **Demo 1** the monitoring job (`run_alert_checks.py`: 3 pass, 5 fire, 1 incident); **Demo 2** the scheduler (`monitoring.yml`), the Slack-style message and the Evidently Tests report; the owner's one page with "Oct pending"; the alert-fatigue rule | TelcoNova churn |
| 7 · Wrap-up | 25 | 56:00–60:00 | Three things to remember; how the knowledge check works | — |

## 3. Recording notes

- **Read the notes, not the slides.** The script in the notes is written to be spoken; it says more than the slide shows, on purpose. Numbers on slides (the confusion matrix 140, 60, 110, 690; overall accuracy 82% → 80%; the North segment 89% → 65%) are the ones the script uses; do not change one without the other.
- **Pace.** About 130 words a minute. Each slide's notes end with a `[Timing: from–to]` line; if you are a minute late at the end of a segment, it does not matter, but re-check at segments 5 and 6, which are the longest.
- **The demo (slides 22–23) is a screen recording, not a slide.** Record it separately and cut it in. Before recording: double-click `S09/demo/update_venv_and_run.command` once (it adds Evidently to the Session 3 venv and does a first run), then open a terminal in `S09/demo/`, activate the venv (`source ../../S03/demo/mlflow/.venv/bin/activate`), zoom the terminal font to 18 pt, and have `monitoring.yml` and `alert_message.md` open in an editor and `alert_checks.html` open in the browser. Then: (1) `python run_alert_checks.py`, about ten seconds; read the PASS/FIRE lines aloud following the slide 22 notes, and finish with `echo $?` → `1`; (2) show `monitoring.yml` (the two cron lines, `if: failure()`), then `alert_message.md`, then the browser report and click **Tests** (1 success, 3 fail), following the slide 23 notes. The slides carry the same three pictures as fallback, so if the recording fails the video still works from the slides alone. The console output is deterministic (fixed seeds); only the timestamp changes.
- **Setup.** Slides at full screen, notes on a second display or printed. Record segment by segment; a mistake costs one segment, not the hour. Camera optional; if used, small, bottom right.
- **Pauses.** Say "pause here if you want to write your one-line note" at the end of slides 7 (the three drifts table), 12 (which metric for which decision), 13 (which metrics need the truth) and 21 (the anatomy of a rule). Those four slides are where the quiz answers live.
- **Consistency with the live sessions.** The examples are the ones students already know: TelcoNova (Session 7 activity), IberBank (Sessions 3 and 5), NorthRetail (Session 1), and the HR assistant, which Session 10 builds. Keep the names.
- **After recording.** Upload with chapter markers at the segment starts; attach the deck as PDF; open the knowledge check with a one-week window and a single attempt (see section 4).

## 4. The demo folder (`S09/demo/`)

| File | What it is | Used on |
|---|---|---|
| `alerts.yaml` | The eight monitoring rules for the TelcoNova churn model: metric, threshold, window, severity (incident/trend), route, action | Slide 21 |
| `run_alert_checks.py` | The monitoring job (≈100 lines): scores reference and current data, runs Evidently drift and missing-value checks as tests, computes accuracy overall and per region × tenure band on the month's labels, reads batch time and p95 latency, prints PASS/FIRE per rule, writes `alert_message.md` and `alert_checks.html`, exits 1 if any rule fired | Slide 22, Demo 1 |
| `monitoring.yml` | The GitHub Actions workflow that runs the job weekly (drifts) and on the 2nd of the month (labels have arrived), posts the message only `if: failure()`, and keeps the report as an artefact | Slide 23, Demo 2 |
| `reference.csv`, `current.csv`, `churn_model.pkl` | June reference, October current data and the model (the Session 7 demo assets, reused) | inputs |
| `alert_checks.html` | Evidently report; the **Tests** tab shows the four data rules with their thresholds (1 success, 3 fail) | Slide 23, Demo 2 |
| `alert_message.md`, `console_output.txt` | The last run's message and console output, as text | reference |
| `console_output.png`, `alert_message.png`, `alert_checks.png`, `alert_checks_tests.png` | The same, rendered as images for the slides (`render_assets.py` regenerates the first two) | Slides 22–23 |

Expected console result: **3 passed** (missing-features 0%, accuracy-overall 0.80, batch 05:42) and **5 fired** (drifted-features 3 of 7, charges-mean-shift 76.5 > 70, prediction-drift 0.116 ≥ 0.10, accuracy-segment North 3y+ 0.65 on 349 customers, latency-p95 659 ms · incident). The point of the demo is the pair accuracy-overall PASS / accuracy-segment FIRE, the exit code, and the two cron schedules: the truth has its own calendar.

## 5. Knowledge check

**Settings for the campus:** 10 questions, multiple choice, one correct answer each; single attempt; 20-minute limit (target 12); randomise question order; show the score but not the answers until the window closes on 30 October; individual work, no AI tools (syllabus policy).

Each question describes a symptom an owner would notice and asks for the metric that reveals it, and what it needs to be computed. Six classical, four LLM; one on a missing truth (Q2), one on routing an alert (Q10). Distractors are plausible metrics that would not reveal that symptom.

### Questions

**Q1.** The retention team says October's call list "feels wrong": many loyal, long-tenure customers in one region were not on it, and the saved-customers count fell 15%. The weekly drift report on the input features showed nothing. Which metric would have revealed the problem, and what kind of change is it?

a) Share of drifted input features; data drift
b) Accuracy on the monthly labels, by region and tenure band; concept drift
c) p95 scoring latency; system health
d) Precision at the 0.5 threshold, overall; performance decay

**Q2.** IberBank's fraud model blocks about 0.4% of card payments. The team reports recall of 92%, computed on the chargebacks that arrived for the payments the model let through. A colleague objects that the number cannot mean what they think. Why, and what would fix it?

a) The number is fine: chargebacks are the ground truth for fraud
b) Blocked payments never happen, so their truth is never learned; the false positives are invisible and recall is computed only on the cases the model chose to let through (selective labels). Fix: let a small random sample of flagged payments through, or review them by hand
c) Recall should be replaced by accuracy, which does not need labels
d) The problem is latency: chargebacks arrive 30–90 days late, so the metric should be computed weekly instead

**Q3.** A fraud model blocks 0.4% of transactions. A colleague reports "the model is 99.6% accurate" and proposes accuracy as the A/B metric for the new version. What is wrong?

a) Nothing; 99.6% is a strong result
b) Accuracy rewards the majority class; a model that blocks nothing also scores 99.6%. Use fraud caught at a fixed false-positive rate (recall at fixed precision)
c) Accuracy should be replaced by latency for fraud models
d) Accuracy is fine but must be computed on the training set

**Q4.** After a deployment on Friday evening, the churn model flags 60% of customers as high risk instead of the usual 12%. Labels will not arrive for a month. Which metric shows the problem today?

a) Prediction drift: the distribution of the model's own scores against the reference
b) Concept drift, measured on labels
c) Precision on the monthly labelled sample
d) Cost per thousand predictions

**Q5.** The retention team gives a €50 discount to every customer the model scores above 80% risk. A month later, only half of those customers had actually been at risk. The ranking of customers was still correct. Which metric captures this failure?

a) AUC
b) Recall
c) Calibration (the calibration curve or Brier score)
d) Throughput

**Q6.** The fraud model's requirement is "answer in under 150 ms". The average latency is 90 ms, yet the card network reports that about one in twenty transactions times out. Which number should the dashboard show?

a) The average latency, which already meets the requirement
b) The 95th-percentile latency (p95)
c) The error rate on the training set
d) The share of drifted features

**Q7.** The HR assistant told an employee they were entitled to 30 days of holiday; the policy document says 23. The retrieved passage was correct. Which metric counts this failure, and how is it measured?

a) Retrieval hit rate on the golden set, measured by word overlap
b) Hallucination / groundedness: a judge compares each claim in the answer with the retrieved passages, confirmed by a human sample
c) Time to first token, p95
d) Escalation rate

**Q8.** After the HR policy documents were updated, the assistant keeps giving answers that match the old policy. Retrieval brings back the new passages. Which metric would reveal that the answers are not built from what was retrieved?

a) Tokens per request
b) Groundedness (context faithfulness) against the current document set
c) Toxicity rate on outputs
d) Thumbs-up rate

**Q9.** The monthly bill for the HR assistant has risen 40% with the same number of conversations, after someone edited the prompt to add instructions and the document chunks were made longer. Which metric would have shown the change as it happened?

a) Hallucination rate
b) Tokens per request (input and output), tracked over time
c) Accuracy
d) Share of drifted input features

**Q10.** In one week, three of the HR assistant's answers contained an employee's full name and salary, copied from an example in a policy document. How should this metric be treated in the monitoring plan?

a) As a trend: alert if the weekly rate exceeds 5%
b) As an incident: a PII detector on every output with a threshold of zero, blocking the output and paging the on-call engineer
c) As a quality issue for the weekly human sample
d) As a cost issue: fewer tokens would reduce the leak

### Answer key and rationale (professor only)

| Q | Answer | Why | Family |
|---|---|---|---|
| 1 | b | Same inputs, different behaviour in a segment; invisible to input drift; visible only with labels, by segment (the Session 7 demo). | Classical · concept drift |
| 2 | b | The model's own decision hides the truth: a blocked payment produces no outcome, so false positives are never observed and recall is measured on a non-random subset. Only a random sample let through (or a manual review) reveals what the model hides. Late labels (d) are a real but different problem. | Classical · ground truth (selective labels) |
| 3 | b | Rare event: accuracy is dominated by the majority class. The right A/B metric is fraud caught at a fixed false-positive rate. | Classical · performance |
| 4 | a | The model's own outputs moved; no labels needed; the earliest warning after a deployment accident. | Classical · prediction drift |
| 5 | c | Ranking intact (AUC fine), numbers not trustworthy: an overconfident model; calibration curve / Brier score. | Classical · performance |
| 6 | b | The average hides the tail; a percentile requirement (p95 under 150 ms) is what "under 150 ms" must mean. | Classical · operational |
| 7 | b | A confident statement unsupported by the (correct) source: hallucination; measured by a judge, confirmed by humans. | LLM · hallucination / groundedness |
| 8 | b | Retrieval works; generation ignores the context and answers from memory: a groundedness failure against the new documents. | LLM · groundedness |
| 9 | b | Cost drift caused by longer prompts and chunks shows up as tokens per request; conversations unchanged. | LLM · tokens and cost |
| 10 | b | Personal data in an output is an incident, not a trend: severity incident, threshold zero, route = page the on-call engineer, action = block the output. The six parts of a rule from slide 21. | LLM · PII · routing an alert |

**Scoring:** 1 point each; pass at 6/10 for the continuous-assessment component; the two most-missed questions are worth a two-minute recap at the start of Session 10 (usually Q2, Q5 and Q8).

---

## 6. Checklist

- [ ] Deck reviewed; the numbers in the notes match the slides
- [ ] Recorded in seven segments; total between 55 and 65 minutes
- [ ] Demo screen recording (slides 22–23) captured from `S09/demo/` and cut in; `run_alert_checks.py` exits 1 with 3 PASS / 5 FIRE
- [ ] `S09/demo/` files attached on the campus next to the deck (students may open `alerts.yaml`, `run_alert_checks.py`, `monitoring.yml`, `alert_checks.html`)
- [ ] Uploaded with chapter markers; deck attached as PDF
- [ ] Knowledge check created with the settings above; opens 24 October, closes 30 October 23:59
- [ ] Session 7 closing slide and Forum 4 opening post point to the video and the deadline
