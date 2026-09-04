# Forum 3 Pack · Session 6 · 17–23 October 2026

**Recap of Session 5 — CI/CD & Deployment Strategies**
*Coverage check, the opening post, extra themes, mid-week posts, the CI/CD flow template, and model-answer notes.*

---

## 1. Coverage check

| Forum question | Where it was taught in Session 5 | Gap? |
|---|---|---|
| Q1 · CI/CD flow for a fraud model, showing which tests run on code and which on data before deployment | Slides 6–8 (CI/CD/CT, the three levels, stages and triggers), 10 (the test pyramid), 11–12 (the demo: a real pipeline with named steps, one stopping at the data test), appendix (the workflow file) | None |
| Q2 · Canary vs blue-green for a customer-facing bank model under strict zero downtime | Slides 17 (zero downtime and rollback), 18 (blue-green), 20 (canary), 22 (scorecard), the activity | None |
| Q3 · An A/B test to decide whether a new version outperforms the current one: metric and threshold | Slide 21 (A/B is not a canary; the three ingredients), the activity's decision rule | None, provided the IberBank brief (activity brief) is on campus so answers share a scenario |

---

## 2. Assets to post with the opening message

- The IberBank v2 rollout brief (activity brief), shared scenario for all three questions.
- The CI/CD flow template (section 5).
- Session 5 slides.
- A link to the demo repository's Actions page, for students who want to look at a real run again: `https://github.com/juanmaramirezgarcia/mlops-demo-churn/actions`.

---

## 3. Opening post (publish Saturday 17 October, after the live session)

> **Forum 3 · Recap of Session 5 · open until Friday 23 October, 23:59**
>
> This week's forum is about the two decisions that happen after a model is built: what must be checked before it is allowed out, and how it reaches customers. All three questions use the IberBank card-fraud model from the activity, so that your answers can be compared with each other. No code; diagrams and short texts.
>
> **Three questions, three artefacts**
>
> 1. **A CI/CD flow.** Design the CI/CD flow for the fraud-detection model: a diagram plus a short description (150–250 words). Use the template attached or draw by hand. The diagram must show **which automated tests run on code** and **which run on data** before deployment, and where the pipeline stops if a test fails. Add at least one model test (the top of the pyramid) and say what triggers a run.
> 2. **Canary or blue-green.** Compare canary and blue-green deployments for the customer-facing fraud model. Which would you recommend under a **strict zero-downtime** requirement, and why? Use the scorecard's five rows (zero downtime, cost, customer risk, what you learn, rollback), and say whether the regulator's requirement changes your answer.
> 3. **An A/B test.** Describe the A/B test you would run to decide whether version 2 outperforms version 1. Give the **metric**, the **decision threshold**, and how you would know you have enough traffic. Say what you would do about the 60-day lag in confirmed fraud.
>
> **How the week works.** Post by Tuesday if you can. Reply to at least two classmates with a challenge, an extension or a request for evidence. Nudge Tuesday, twist Thursday, synthesis Friday.
>
> **AI tools.** Encouraged for structuring; declare them with the syllabus sentence, or state that none were used.
>
> **A theme to react to while you write:** *"The rollback drill."* You voted on whether a model that passed every test can go to 100% of customers at once. Now the drill: a canary at 10% of traffic shows a 2% fall in fraud caught. Roll back, hold, or widen? I want the decision **rule**, not the decision.

---

## 4. Extra discussion themes

**Theme A · The rollback drill** (posted Saturday)
Polled in chat, left unresolved. A canary at 10% shows fraud caught down 2%. Push for a rule with three parts: the number (is 2% inside the noise at 10% of traffic for one day?), the watcher (who or what is looking, at what hour), and the action (shrink to 0%, hold at 10% for another day, widen). Reward answers that ask how long the canary has been running and how many confirmed cases 2% represents; punish "we'd look at it and decide".

**Theme B · Shadow was not in the question** (posted Tuesday)
The syllabus asks about canary and blue-green; the session added shadow. When is shadow the right choice for a bank, and why does it cost twice as much? Expected: it is the only strategy that produces evidence on real traffic with zero customer exposure, which is what regulators ask for; the price is scoring everything twice for weeks. Reward students who combine it with a canary rather than choosing one.

**Theme C · Serverless for fraud scoring?** (posted Thursday, as the twist)
IT proposes hosting version 2 as a serverless function to save money. The model must answer in under 150 ms, 24/7, with unpredictable peaks (Black Friday, Christmas). Is serverless a good fit? What would you want to know before deciding? Expected: cold starts against a 150 ms budget, cost at 40 million calls a month, model size; probably not for this model, plausible for a batch scoring job or a low-traffic internal model. Reward answers that ask for a latency test in the CI pipeline before deciding.

---

## 5. CI/CD flow template (attach to the opening post)

Draw the flow left to right. Every box is a step; every diamond is a test that can stop the flow. Fill the three columns for each test.

| Step | Trigger / input | Tests at this step (name each) | Runs on code, data or model? | If it fails |
|---|---|---|---|---|
| 1 · Change pushed | A developer or an automated extract | | | |
| 2 · Build and unit tests | | | code | stop, notify the author |
| 3 · Data validation | The training extract | | data | |
| 4 · Train and evaluate | | | model | |
| 5 · Model validation | Candidate vs production model | | model | |
| 6 · Register | | | | |
| 7 · Deploy (which strategy?) | | | | |
| 8 · Monitor (Session 7) | | | | |

**Description (150–250 words):** what each test protects against, and what triggers a run (a push, a schedule, new data, a performance signal).

---

## 6. Mid-week posts

**Tuesday nudge.** Quote two Q1 flows that disagree about where data validation sits (before training only, or also before scoring) and ask which is right (both: the training extract and the live requests both need checks; the second is Session 7's territory). Post Theme B.

**Thursday twist.** Post Theme C, and add a twist to Q2: "The CFO cancels the budget for a second production environment. Which strategies remain possible, and what do you lose?" Expected: blue-green and shadow disappear; canary and A/B remain; you lose the regulator's evidence on real traffic without exposure, so you would argue for a short shadow period as a one-off cost.

**Friday synthesis.** 300 words: the three best contributions with names; the misconception of the week; the bridge to Session 7 and to Video 1.

> *What you said.* [Three insights, attributed.]
> *The misconception of the week.* Many Q3 answers proposed "accuracy" as the A/B metric. For a model that blocks 0.4% of transactions, a model that blocks nothing has 99.6% accuracy. The metric must be fraud caught at a fixed false-positive rate; the threshold must be a difference on that metric; and you must say how much traffic makes the difference real.
> *What comes next.* On Saturday the model is live, and the world starts moving under it: data drift, concept drift, performance decay, and the thresholds that trigger retraining. Video 1 opens the same day with the metrics in depth and a quiz that counts. Before class: read the retrain trigger in the demo repository's model card and write down what you would need to measure every month.

Reuse the synthesis as the recap slide for Session 7.

---

## 7. Model-answer notes (for grading)

### Q1 · CI/CD flow

A strong answer has the steps in a sensible order, names at least two code tests (unit tests on the validation rules and pre-processing; an integration test that the steps fit together), at least three data tests (schema, ranges and allowed values, empty share or freshness, no leakage), and at least one model test (minimum metric on a fixed evaluation set, or not-worse-than-production, or latency under 150 ms). Every test has a stopping condition. The trigger is named. Reward students who reuse the demo's four steps and extend them. Weak answers draw boxes with no tests, or put all tests "at the end".

### Q2 · Canary vs blue-green

A strong answer uses the scorecard: both meet zero downtime (blue-green if the switch is instant); blue-green costs a second environment and exposes everyone at the switch; canary is cheaper, bounds risk by the slice, but needs monitoring to decide and shows two behaviours at once. Recommendation for a customer-facing bank model under strict zero downtime: canary (with the rollback trigger written first), possibly using blue-green infrastructure as the mechanism for the final step. Reward answers that add the regulator's requirement and conclude that a shadow phase precedes either. Weak answers pick one without the scorecard, or claim blue-green "has no risk".

### Q3 · A/B test

A strong answer names a metric appropriate to a rare event (fraud caught at a fixed false-positive rate, or false positives at a fixed catch rate), a threshold as a difference on that metric (with the other side not worse), a notion of enough traffic (a full week including a weekend; the statisticians set the number), and deals with the 60-day lag (early signals from the fraud team's confirmations and early chargebacks; a provisional decision revisited at 60 days). Reward answers that distinguish the A/B decision from the canary's safety checks. Weak answers use accuracy, give a metric without a threshold, or ignore the lag.

### Participation rubric, applied to this forum

| Level | This week |
|---|---|
| Excellent | Three complete artefacts; a flow with named tests and stopping conditions; an A/B rule with all three ingredients; replies that sharpen someone's rule; contributes to a theme thread |
| Good | Three complete artefacts; two relevant replies |
| Satisfactory | Artefacts complete but generic (tests "at the end"; "canary is safer"; accuracy as the metric) |
| Insufficient | Missing artefacts, off-topic, or posted Friday night with no interaction |

---

## 8. Checklist before opening

- [ ] Opening post published with the three questions and Theme A
- [ ] IberBank v2 brief and the CI/CD flow template attached
- [ ] Session 5 slides posted; Actions page link included
- [ ] Two contrasting Q1 flows picked for Tuesday
- [ ] Reading for Session 7 announced (Treveil ch. 7; optional Huyen ch. 8) and the "retrain trigger" preparation task
- [ ] Reminder that Video 1 (Session 9) opens on 24 October with a quiz that counts
