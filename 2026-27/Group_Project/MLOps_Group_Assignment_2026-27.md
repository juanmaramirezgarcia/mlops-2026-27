# Group Project — Collaborative MLOps Planning (2026–27)

**Weight:** 35% of the course grade · **Teams:** 3–5 students · **Deliverable:** one written report (PDF, ≤ 12 pages excluding the appendix) plus a live defence.

You are a **consulting MLOps team**. A company has built an AI prototype that works in a notebook and now wants to run it reliably in production. They have handed you a short brief describing the system, how its outputs are used, and how it was built so far. Every brief contains real, engineered weaknesses — the kind of things that make models fail silently, cost money, break a regulation, or erode trust. Your job is the job of an MLOps consultant: **first diagnose what is wrong or missing, then design the strategy that fixes it.**

This mirrors exactly what we do in class. In Session 10 you learned a root-cause method for diagnosing a failed AI system; here you apply it before anything has failed. The five artefacts you produce are the five deliverables named in the syllabus, and you defend them the way a real team defends a plan to a client.

---

## 1. What you have to produce

Your report has **two parts**. Part A is the diagnosis; Part B is the strategy. They are weighted roughly equally, and the live defence tests both.

### Part A — Diagnose the case (the consultant's first week)

Read your assigned brief and find everything that a good MLOps strategy should address. Organise your findings using the **four course modules**, because that is how you will fix them:

| Module | What to look for |
|---|---|
| **1 · Foundations, personas & lifecycle** (S1–2) | Who is accountable and for what? Is the right persona missing? Is the model being treated as a static asset? Is anyone actually responsible for the model once it is live? Is the business objective aligned with what the model optimises? |
| **2 · Pipelines, environments, deployment & security** (S3–6) | Is the work reproducible, or does it live in one person's notebook? Are dev/QA/prod separated? Is there any CI/CD, or is deployment manual? Is the input validated? Are there security exposures (data poisoning, prompt injection, an open endpoint)? |
| **3 · Monitoring & retraining** (S7–9) | How would they even know the model degraded? Is anyone watching drift, performance, or data quality? When and how do labels (ground truth) arrive? What triggers a retrain, and who approves it? Are alerts defined and actionable? |
| **4 · GenAI specifics & governance** (S10–12) | For LLM systems: prompt versioning, RAG grounding, evaluation (golden set / human / judge), guardrails. For all systems: does it fall under the EU AI Act, and at what risk tier? Is there documentation (model card, decision log), human oversight, and a governance owner? |

For each issue you find, use the **Session 10 root-cause template**:

> **symptom** (what goes wrong or could go wrong) → **stage where it originates** (where in the lifecycle) → **missing control** (what should have been there) → **persona accountable** (who should own it) → **corrective action** (what your Part B will do about it).

You are not expected to find a fixed number of issues, but a strong diagnosis surfaces problems in **all four modules**, not just the one your team finds easiest. Rank them: which two or three would you fix first, and why?

### Part B — Design the MLOps strategy (the five artefacts)

Turn your diagnosis into a plan. These are the five deliverables from the syllabus. Each one should visibly answer issues you raised in Part A — a reader should be able to trace a fix back to a problem.

1. **MLOps roadmap.** How this prototype becomes a reliable production system, in phases. What happens first, what can wait, and what "done" looks like at each phase. Anchor it to the lifecycle stages, not to a wish list of tools.

2. **Persona responsibilities.** Who does what across the lifecycle. A RACI-style map (lifecycle stages as rows, personas as columns) is the clearest form. Make sure every stage has an accountable owner — the gaps you found in Part A should now be filled.

3. **CI/CD pipeline schematic.** A diagram of the pipeline from a trigger through test → validate → train → evaluate → build → deploy, with the **gates** that stop a bad model or bad data from reaching production, and the **triggers** that start a run (a push, a schedule for continuous training, a monitoring alert). One clear diagram plus a short paragraph per stage.

4. **Monitoring-and-retraining policy.** What you measure, the threshold at which you act, who is alerted, and what the alert makes them do. Cover **classical ML metrics** (data drift, prediction drift, performance once labels arrive, data-quality checks) and, **where the case is an LLM system, the LLM/prompt metrics too** (grounding/faithfulness, answer quality via a golden set and a judge, guardrail hit-rate, cost and latency per request). State explicitly **how ground truth arrives and how long it takes**, and **what triggers a retrain and who approves it**.

5. **Governance framework.** The case's EU AI Act risk tier and what that obliges you to do; the documentation you will keep (a model card and a decision log at minimum); where a human stays in the loop; and who owns governance. Tie each control to a point in your pipeline or monitoring policy — governance is not a separate document, it is controls wired into the system.

---

## 2. Your assigned case

Each team is assigned **one** of the six cases below. Do not switch cases. The cases differ in domain, in whether they involve an LLM, and in which regulations bite — but every one has weaknesses spread across all four modules, and every one can earn full marks. Read your brief as *facts about a real client*: some of what they tell you is fine, some is a problem, and some of the problem is what they **didn't** say.

> **A note on the facts:** the briefs describe how the client works today. Take the numbers and practices at face value — they are the evidence for your diagnosis. Where the brief is silent on something an MLOps team would expect (say, no mention of who relabels data), that silence is itself a finding: name it as a gap, don't assume it is handled.

---

### Case 1 — Retail demand forecasting & automatic replenishment

**The company.** *NorthRetail*, a grocery chain with 240 stores, forecasts weekly demand for 60,000 products per store and uses the forecast to place automatic replenishment orders with suppliers. The forecast decides how much stock is ordered; buyers only see exceptions.

**How the output is used.** The model's number is multiplied by a safety factor and sent straight to suppliers as a purchase order. A too-low forecast empties shelves; a too-high forecast fills warehouses with perishable waste. Roughly €40M of stock is ordered on the model's word each week.

**How it was built and runs today.** A data scientist trained a gradient-boosting model in a notebook on three years of sales history and got a good backtest error. The trained model file is emailed to the IT team, who load it into the ordering system by hand each quarter when a new version is produced. Features are computed by a SQL script that the data scientist maintains on her laptop; a second analyst has a slightly different copy. Promotions and weather are known to shift demand hard, but the live feature pipeline does not include them — they were in the training data as static columns. There is no separate test environment; changes are tried directly on the ordering database after hours. Nobody currently owns the model after it ships; the data scientist has moved to another project. The team knows accuracy "was good at launch" but has no measurement since. When COVID-era panic-buying hit historically, the model kept forecasting normal demand for weeks before anyone noticed.

---

### Case 2 — SME credit scoring

**The company.** *Corurbanco*, a mid-size bank, is replacing a manual underwriting process with a model that scores small-business loan applications and produces an approve / refer / decline recommendation plus a limit.

**How the output is used.** "Decline" and "approve" below a threshold are **fully automated** — the applicant never speaks to a human. "Refer" goes to an underwriter. About 70% of applications are decided by the model alone. A wrong decline costs a customer their loan; a wrong approve costs the bank money and can breach lending rules.

**How it was built and runs today.** A vendor delivered a trained model and a scoring API; the bank does not have the training data or the training code, only the endpoint and a one-page accuracy claim. Features include the applicant's postcode, industry sector, and years trading. The model was trained on the bank's historical decisions — which were made by underwriters over the last decade. It is deployed as a single API the loan-origination system calls; the same version has been live for 14 months. There is no logging of individual decisions beyond the final score, and no way to explain to a rejected applicant why they were declined. Performance is reviewed once a year by sampling 50 files. Nobody has checked whether approval rates differ by postcode or sector. The compliance team has heard of the EU AI Act but believes it "doesn't apply to internal tools."

---

### Case 3 — Real-time payment fraud detection

**The company.** *PayFlux*, a payments processor, scores every card transaction in under 50 ms and blocks those the model flags as fraud.

**How the output is used.** A score above a hard threshold **blocks the transaction in real time** — the customer's card is declined at the till. Below it, the payment goes through. False blocks anger genuine customers (and merchants); missed fraud is a direct loss. Volume is ~3,000 transactions per second.

**How it was built and runs today.** The model was trained on labelled fraud from 18 months ago. The label for whether a transaction was really fraud only becomes known **weeks later**, when chargebacks and customer disputes settle — so "recent performance" is always about the past. The threshold was set once at launch and hard-coded. Fraud patterns change constantly as fraudsters adapt, and there have been two recent periods where the block rate spiked and the call centre was flooded, but the team found out from customer complaints, not from a dashboard. The features are computed by a real-time service; a separate batch job computes the same features for training, and the two were written by different teams at different times. Retraining happens "when someone notices the numbers look off." There is no automated pipeline; a senior engineer retrains locally and pushes the new model over the weekend. The model that decides whether to block a payment has no documented owner on the risk side, only on the engineering side.

---

### Case 4 — Predictive maintenance on edge devices

**The company.** *TurbineWorks* sells industrial pumps and now offers a service that predicts failures from vibration and temperature sensors, so customers can service a pump before it breaks.

**How the output is used.** A model runs **on a small device attached to each pump** (thousands of them, in factories with poor connectivity) and raises a maintenance alert. A missed failure means an unplanned shutdown of a customer's production line; a false alarm means an unnecessary, costly service visit. Alerts go straight to the customer's maintenance team.

**How it was built and runs today.** One model was trained on data from a set of pilot pumps and copied to every device. Different customers run pumps in very different conditions (temperature, load, altitude), but they all get the same model. The devices are in the field; updating the model on them requires a manual firmware push that has happened once in two years. The data the devices see never comes back to the company — there is no channel to collect it — so the team cannot tell how the model is doing across the fleet except when a customer complains about a missed failure or too many false alarms. New pump models have been released since training, running conditions the original model never saw. There is no versioning of which device runs which model; the team is "fairly sure" they are all on v1. The engineer who built it keeps the training notebook on a personal drive.

---

### Case 5 — GenAI customer-support assistant (RAG)

**The company.** *Helios Energy*, a utility, has built a chatbot that answers customer questions (billing, tariffs, outages, how to switch plans) by retrieving from its help-centre documents and generating an answer with an LLM.

**How the output is used.** The assistant is on the public website and the app, answering customers directly with **no human in between** for most conversations. It quotes tariffs, explains charges, and tells customers what they are entitled to. A wrong answer about a tariff or a right-to-switch is a real commitment the company may have to honour, and a compliance exposure.

**How it was built and runs today.** A developer wired an LLM API to a vector search over a dump of the help-centre PDFs and tuned the prompt by hand until the demo looked good. The prompt lives as a string in the application code; when someone edits it, there is no record of what changed or why, and the change goes straight to production. The document index was built once at launch; help-centre content has changed since (new tariffs), but the index has not been rebuilt, so the assistant sometimes retrieves and quotes **outdated tariffs**. There is no golden set of question-answer pairs and no evaluation — quality is judged by "it seemed fine in testing." There are no guardrails on input or output: a user recently got the assistant to ignore its instructions and produce off-topic content, and there is nothing checking that answers are grounded in the retrieved documents rather than invented. Cost is a per-token surprise on the monthly bill; nobody tracks it per conversation. No one has assessed whether an AI system that talks to customers about their contracts carries transparency or other obligations.

---

### Case 6 — Clinical readmission early-warning

**The company.** *Ribera Health*, a hospital group, has a model that predicts which discharged patients are at high risk of readmission within 30 days, so a care team can follow up.

**How the output is used.** A risk score appears in the clinician's dashboard and drives which patients get a follow-up call or an earlier appointment. It **influences care decisions** for real patients. A missed high-risk patient may be readmitted in crisis; flagging everyone overwhelms a small care team and they stop trusting the score.

**How it was built and runs today.** A research team trained the model on five years of records from **one flagship hospital** and rolled it out to all twelve hospitals in the group, which serve different populations. The model was validated once, in a paper, at launch; it has not been checked since, and case mix has shifted (an ageing catchment, a new specialty unit). The score is not explained to clinicians — they see a number, not why — and some have quietly stopped using it because they "don't know what it's based on." Labels (was the patient actually readmitted?) are available in the hospital record 30–60 days later, but nobody feeds them back to check the model. Patient data flows into the model through a pipeline a since-departed contractor built; it is undocumented. There is no model card, no record of who approved clinical use, and no defined process for a clinician to challenge or override a score. The data-governance office is not aware the model is in live clinical use.

---

## 3. The concept checklist — what "good" looks like

Use this to check your own work before you submit. A strong report touches most of these; the professor's rubric is built from them. You do not need to name-drop every term, but a fix that ignores a whole column is a fix with a hole in it.

**Module 1 — Foundations, personas & lifecycle**

- The model is treated as a **living asset**, not a one-off deliverable — someone owns it after launch.
- The right **personas** appear (data scientist, ML/platform engineer, data engineer, product owner, risk & compliance) and each lifecycle stage has an **accountable** owner (RACI).
- The **business objective** is connected to what the model optimises, and the cost of each kind of error is stated.

**Module 2 — Pipelines, environments, deployment & security**

- The work is **reproducible**: versioned code and data, one source of truth for features (no "two copies of the SQL"), not a laptop notebook.
- **Environments** are separated (dev / QA / prod) with promotion gates; deployment is not a manual after-hours push.
- There is **CI/CD** (automated test → build → deploy) and, where relevant, **CT** (scheduled or triggered retraining).
- **Input validation** and **training/serving consistency** (the same features computed the same way in both places).
- **Security** exposures are named and mitigated (open endpoints, data poisoning, prompt injection for LLMs).

**Module 3 — Monitoring & retraining**

- **Drift** (data and prediction) and **performance** are monitored, with the delay before labels arrive made explicit.
- **Data-quality** checks at the input.
- **Thresholds** that are specific and **alerts** that tell a named person to do a specific thing.
- A **retraining trigger** (schedule, drift, or performance) and an **approval step** before a new model goes live.
- For edge/fleet cases: a way to **collect field data back** and to know **which version runs where**.

**Module 4 — GenAI specifics & governance**

- For LLM systems: **prompt versioning** and environments; **RAG grounding** and index freshness; **evaluation** with a golden set + human review + LLM-as-a-judge; **guardrails** on input and output; **cost/latency** tracked per request.
- **EU AI Act** risk tier identified for the case, and the resulting obligations named (many of these systems are high-risk: credit scoring and essential-services access are Annex III; medical use may be high-risk; transparency duties apply to the chatbot).
- **Documentation**: a model card and a decision log, and who writes them.
- **Human oversight**: where a person can review, challenge, or override, especially for the fully-automated cases.
- A named **governance owner** and controls wired into the pipeline and monitoring, not bolted on.

---

## 4. Calendar

The project runs alongside the taught sessions so you build each artefact roughly when we cover it. Dates are indicative and will be confirmed on the campus with the defence schedule.

| When | Milestone |
|---|---|
| **Week of Session 3 (from ~10 Oct)** | Teams formed and cases assigned. Read your brief. Start Part A — you already have the personas and lifecycle from Sessions 1–2. |
| **After Session 5 (~week of 17 Oct)** | Part A diagnosis in draft; first cut of the CI/CD schematic and roadmap (Sessions 3–5 give you pipelines, environments, deployment). *Optional checkpoint: one paragraph per team on your top three issues.* |
| **After Session 7 (~week of 24 Oct)** | Monitoring-and-retraining policy drafted (Session 7 gives you drift, thresholds, alerts). |
| **After Session 10 (~week of 31 Oct)** | LLM cases add prompt/RAG/eval to their monitoring; all teams draft the governance framework (Session 10 diagnostics + Session 12 governance video). Forum 5 (the capstone) is the rehearsal for your defence — bring your own case's roadmap to Q1. |
| **~Sun 8 Nov** | Final report submitted (PDF, ≤ 12 pages + appendix). |
| **Week of ~9 Nov** | Live defences (schedule published on the campus in the 2–6 Nov window). |

Starting Part A early is the single best thing you can do: the diagnosis is what everything else hangs on, and you have the tools for it after Session 2.

---

## 5. Format, submission & the defence

**The report.** One PDF, at most **12 pages** excluding an appendix, readable by a smart non-specialist (your client's product owner, not another data scientist). Structure it as Part A (diagnosis, using the root-cause template — a table is fine) then Part B (the five artefacts). Diagrams beat paragraphs for the RACI, the pipeline schematic, and the monitoring policy; put long tables, full threshold lists, or extra detail in the appendix. State your case number on the cover. Everyone's name on it.

**The defence (live, ~15 minutes per team + questions).** You present the plan to us as if we were the client, and we push back — that is the fourth rubric dimension, and it is worth as much as the artefacts. Expect questions like: *why did you rank that issue first? what happens the day your labels are three weeks late? who approves a retrain, and what stops a bad model shipping? which EU AI Act tier is this and how do you know? what does your monitoring actually make someone do at 3am?* Every team member should be able to defend any part — we may direct a question to anyone. A confident, honest "we considered X and chose Y because Z" earns more than a rehearsed script.

**How you are graded.** Four equally-weighted dimensions (per the syllabus): (1) technical soundness of the architecture, (2) depth and clarity of the documentation, (3) quality of the monitoring and governance design, (4) your team's defence of its decisions. The full rubric is on the campus. Note that Part A (diagnosis) and Part B (design) both feed these — a great plan that fixes problems you never named, or a sharp diagnosis with a thin plan, both lose marks.

**Using AI tools.** You may use AI assistants to help draft and check your work — you are an MLOps team, after all. But you own every claim: if the defence exposes that you cannot explain your own pipeline diagram or your EU AI Act tier, that is on the team. Cite any external source you rely on.

---

*Questions about your assigned case go to the capstone forum (Forum 5) or to me directly. Good diagnosis first; the strategy follows from it.*
