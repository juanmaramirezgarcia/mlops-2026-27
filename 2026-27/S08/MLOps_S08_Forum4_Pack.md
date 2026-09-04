# Forum 4 Pack · Session 8 · 24–30 October 2026

**Recap of Session 7 — Monitoring, Explainability & Responsible AI**
*Coverage check, the opening post, extra themes, mid-week posts, the monitoring plan template, and model-answer notes. Runs in parallel with Video 1 (Session 9).*

---

## 1. Coverage check

| Forum question | Where it was taught in Session 7 | Gap? |
|---|---|---|
| Q1 · Monitoring plan for a churn model: metrics for data drift, concept drift and performance decay, and thresholds that trigger retraining | Slides 12 (the plan template), 13 (the loop), the TelcoNova activity; Video 1 for metric definitions and the failure-mode table (segments 1, 2 and 5) | None; tell students to watch Video 1 segments 1 and 5 before answering |
| Q2 · Data drift vs concept drift with a concrete example of each; how the operational response differs | Slide 6 (the taxonomy with responses), 7 (ground truth vs input drift), the demo (slide 15: the pricing change vs the competitor) | None |
| Q3 · An algorithmic decision system (e.g. credit scoring): one fairness risk, one explainability requirement, and how to audit each | Slides 18 (who asks), 20–21 (what an explanation looks like: SHAP, then LIME on the same customer and on text), 22 (do not trust blindly), 23 (bias: three places, two numbers), 26–28 (Responsible AI, guardrails, the risk questions) | None |

---

## 2. Assets to post with the opening message

- The TelcoNova case (activity brief), the shared scenario for Q1 and Q2.
- The monitoring plan template (section 5).
- Session 7 slides; the demo images (`performance_by_segment.png`, `shap_waterfall.png`, `shap_summary.png`, `lime_customer.png`, `lime_text.png`) so students can refer to them.
- The link to Video 1 and the knowledge-check deadline (Friday 30 October, 23:59).

---

## 3. Opening post (publish Saturday 24 October, after the live session)

> **Forum 4 · Recap of Session 7 · open until Friday 30 October, 23:59**
>
> The model is live, the world is moving, and this week you decide what to watch and what to do when it moves. Video 1 (Session 9) is open at the same time; it defines every metric in depth. Use it for definitions; use this forum for decisions.
>
> **Three questions, three artefacts**
>
> 1. **A monitoring plan.** For the TelcoNova churn model (case attached), define a monitoring plan using the template: the metrics you would track for **data drift**, **concept drift** and **performance decay**, each with a threshold (a number and a window) and the action it triggers, including the alert thresholds that would trigger **retraining**. Five to seven rows. Say who receives each alert.
> 2. **Two drifts.** Explain the difference between data drift and concept drift with a **concrete example of each**, from TelcoNova or from your own industry. Then say how your operational response would differ between the two, and why.
> 3. **Fairness and explainability in a decision system.** Pick an algorithmic decision system (credit scoring is the default; hiring, insurance pricing or fraud blocking also work). Identify **one fairness risk** and **one explainability requirement**, and describe **how you would audit for each**: what you would measure or sample, how often, and who would see the result.
>
> **How the week works.** Post by Tuesday if you can. Reply to at least two classmates with a challenge, an extension or a request for evidence. Nudge Tuesday, twist Thursday, synthesis Friday. Do the Video 1 knowledge check by Friday; it counts.
>
> **AI tools.** Encouraged for structuring; declare them with the syllabus sentence, or state that none were used. Not in the knowledge check.
>
> **A theme to react to while you write:** *"Retrain automatically?"* You voted on whether a drift alert should retrain and redeploy the model with no human involved. What exactly should be automatic, and where does a person have to sign?

---

## 4. Extra discussion themes

**Theme A · Retrain automatically?** (posted Saturday)
Polled in chat, left unresolved. Push for a precise split: automatic retraining and validation, yes; automatic redeployment, only for low-impact models with strong model tests and a rollback trigger; a human at "approve" for anything that decides about people. Reward answers that recall the rejected run in Session 3 (a model trained on a 60%-empty extract would have been auto-deployed) and that connect the gate to Session 5's rollout strategies (a canary is a form of automatic caution).

**Theme B · The cost of a false alarm** (posted Tuesday)
A drift alert triggers a retrain that costs two days of a data scientist and a review. The alert fired four times last quarter; twice the data was fine. How many false alarms a month before the team stops trusting the monitor? What would you change: the threshold, the window, or the action? Reward answers that propose a two-stage action (alert and investigate first; retrain only when confirmed) and that set thresholds from the cost of both errors.

**Theme C · Ground truth arrives late** (posted Thursday, as the twist)
For TelcoNova you learn who really churned 30 days later. What do you monitor in the meantime, and how much do you trust it? Expected: prediction drift, input drift, the business KPI (saved customers), explanation shifts; trusted as early warnings that trigger investigation, not retraining. Bridge to Video 1's "the first two drifts buy time while you wait for the third".

---

## 5. Monitoring plan template (attach to the opening post)

**Model:** TelcoNova churn (monthly batch, 2M customers, top 5% called; labels 30 days later; retrain trigger 75% in the model card)

| # | Metric (and how often it is computed) | What it detects | Threshold: number + window | Action · who is alerted |
|---|---|---|---|---|
| 1 | | data drift | | |
| 2 | | data drift | | |
| 3 | | concept drift (early signal) | | |
| 4 | | performance decay, by segment | | |
| 5 | | operational | | |
| 6 | | *(your choice: business KPI, fairness, explanations…)* | | |

**Rule:** a metric without a threshold is a chart; a threshold without an action is an alarm nobody answers. **Which rows trigger retraining, and who approves the new version?**

---

## 6. Mid-week posts

**Tuesday nudge.** Quote two Q1 plans that set the performance threshold differently (one on the overall accuracy only, one by segment) and ask which would have caught the North (only the second; the overall number fell two points). Post Theme B.

**Thursday twist.** Post Theme C, and add a twist to Q3: "Your credit-scoring model passes the fairness audit on gender but the postcode feature turns out to be a proxy for it. Is the audit wrong, the model wrong, or both?" Expected: the audit measured outcomes correctly; the model uses a proxy; both the pre-processing (remove proxies) and the audit (test for proxies, not only protected attributes) need to change.

**Friday synthesis.** 300 words: the three best contributions with names; the misconception of the week; the bridge to Session 10 and Video 2.

> *What you said.* [Three insights, attributed.]
> *The misconception of the week.* Many Q1 plans had a threshold with no window, or a metric with no owner. "Alert if accuracy drops" fires on noise; "alert the team" alerts nobody. The plans that would have caught TelcoNova's North had a segment in the performance row and a person in the action column.
> *What comes next.* On Saturday the model is a language model, and most of what we monitored this week has to be judged rather than measured; Video 1 segment 4 is the preparation. Session 10 is also the failure-case workshop: read your team's brief before class. Video 2, on governance, opens the same day.

Reuse the synthesis as the recap slide for Session 10.

---

## 7. Model-answer notes (for grading)

### Q1 · Monitoring plan

A strong answer has five to seven rows covering all three kinds of "worse" plus an operational row, each with a threshold that has a number and a window, and an action that names a person. It has at least one early concept-drift signal (prediction drift by segment, the call list's composition, the business KPI) and a performance row computed by segment on the monthly labels. It says which rows trigger retraining (performance below 75% overall or 70% in a segment; confirmed data drift) and that the product owner approves the new version. Reward students who set thresholds from the cost of a false alarm versus a missed one. Weak answers list metrics without thresholds, thresholds without windows, or "retrain monthly".

### Q2 · Two drifts

A strong answer gives two examples that are unambiguously different in kind: inputs moved (pricing change, a unit change, a new customer segment) versus behaviour moved with the same inputs (a competitor, a regulation, a crisis). It states the evidence for each (inputs alone; labels, by segment) and the response: for data drift, check the data first and retrain on recent data if confirmed; for concept drift, retrain with new labels, possibly with new features, and revisit the threshold. Reward answers that note concept drift hides in segments and that explanations can hint at it. Weak answers give two examples of the same kind, or say "retrain" for both without distinguishing.

### Q3 · Fairness and explainability

A strong answer names a specific fairness risk (unequal error rates by group, unequal approval rates, a proxy feature such as postcode) and a specific explainability requirement (a customer's right to the reasons for a rejection; the regulator's demand for evidence of non-discrimination), and for each an audit that is a procedure: which number, on which sample, how often, who sees it (Risk & Compliance, the product owner). Reward answers that say the two fairness numbers can conflict and that choosing is a business and legal decision. Weak answers say "check for bias" or "use SHAP" without a procedure or an owner.

### Participation rubric, applied to this forum

| Level | This week |
|---|---|
| Excellent | Three complete artefacts; a plan with windows, segments and owners; two distinct drift examples with different responses; an audit that is a procedure; replies that sharpen someone's thresholds; contributes to a theme thread |
| Good | Three complete artefacts; two relevant replies |
| Satisfactory | Artefacts complete but generic (no windows, no segments, "retrain monthly", "check for bias") |
| Insufficient | Missing artefacts, off-topic, or posted Friday night with no interaction |

---

## 8. Checklist before opening

- [ ] Opening post published with the three questions and Theme A
- [ ] TelcoNova case, monitoring plan template and the three demo images attached
- [ ] Video 1 link and knowledge-check deadline (30 October, 23:59) stated in the post
- [ ] Two contrasting Q1 plans picked for Tuesday
- [ ] Failure briefs for Session 10 posted and allocated to teams by Wednesday 28 October
- [ ] Reading for Session 10 announced (the allocated brief; optional Huyen 2025 ch. 1 and 4)
