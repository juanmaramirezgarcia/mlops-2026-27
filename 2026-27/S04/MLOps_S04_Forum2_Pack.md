# Forum 2 Pack · Session 4 · 10–16 October 2026

**Recap of Session 3 — ML Pipelines, Environments & Security**
*Everything needed to open, run and close the forum: coverage check, the opening post, extra themes, mid-week posts, the pipeline diagram template, the notebook answer key, and model-answer notes.*

---

## 1. Coverage check

| Forum question | Where it was taught in Session 3 | Gap? |
|---|---|---|
| Q1 · Restructure the exploratory notebook into a pipeline with ingestion, validation and preprocessing steps; diagram + rationale | Slides 3 (what you found messy), 6–8 (model = formula + transformations; notebook vs pipeline; why pipelines), 12–14 (versioning, validation, pre-processing) | None, provided `churn_exploration.pdf` is on campus by Wednesday 7 October (the "look at one thing" task) |
| Q2 · Why Dev, QA and Prod; what goes wrong laptop → production | Slides 18–20 (can it run there; three environments, two gates; laptop to production) and the chat poll | None |
| Q3 · One adversarial or data-integrity threat, a mitigation, and the lineage/auditability control that detects it | Slides 21 (lineage), 24–26 (risk sources, four attacks, controls) and the IberBank activity | None |

---

## 2. Assets to post with the opening message

- `churn_exploration.pdf` (the notebook, rendered; students do not run anything) and `churn_exploration.ipynb` for those who want to open it.
- `churn_raw.csv` (the data the notebook loads), optional.
- The pipeline diagram template (section 5 below).
- The IberBank case (activity brief), since Q3 answers may build on it.

---

## 3. Opening post (publish Saturday 10 October, after the live session)

> **Forum 2 · Recap of Session 3 · open until Friday 16 October, 23:59**
>
> This week's forum turns María's notebook into something a company could run, and asks you to defend two ideas from today: separate environments, and controls against attacks. No code is needed for any of the three questions; drawings and paragraphs are what I want.
>
> **Three questions, three artefacts**
>
> 1. **From notebook to pipeline.** Open `churn_exploration.pdf` on the campus. Sketch how you would restructure it into a reusable pipeline with separate **ingestion**, **validation** and **preprocessing** steps (and training/registration after them if you like). Use the template attached or draw by hand and photograph it. For each step, list which cells of the notebook it absorbs and which check it performs. Add a short rationale (150–250 words): what breaks in the notebook that your pipeline fixes.
> 2. **Three environments.** Explain why an organisation needs separate Dev, QA and Prod environments. Then describe, concretely, what could go wrong if a model is promoted straight from a data scientist's laptop to production. Three failure modes minimum; a real example beats an invented one.
> 3. **One threat, one control, one detector.** Identify one adversarial or data-integrity threat to a deployed model (you may use IberBank or a model from your own industry) and propose a mitigation. Then say which **lineage or auditability control** would let you detect the threat after the fact: which record would you look at, and what would it show?
>
> **How the week works.** Post by Tuesday if you can. Reply to at least two classmates with a challenge, an extension or a request for evidence. Nudge on Tuesday, twist on Thursday, synthesis on Friday.
>
> **AI tools.** Encouraged for structuring; declare them with the syllabus sentence, or state that none were used.
>
> **A theme to react to while you write:** *"Skip QA to hit the launch date."* You voted on this today. The CEO wants the churn model live on Friday; QA needs a week. What do you say, and what do you put in writing?

---

## 4. Extra discussion themes

**Theme A · Skip QA to hit the launch date** (posted Saturday)
Polled in chat, left unresolved. Push for a proportionate answer: what is the cheapest gate that still protects the company (a named owner, a rollback plan, a limited rollout)? Reward students who distinguish an internal low-risk model from a customer-facing one, and who write the "what I put in writing" part: a one-paragraph risk acceptance signed by the business owner.

**Theme B · Feature store or not** (posted Tuesday)
A retailer has 40 models that share 12 customer features (tenure, average basket, last purchase…). Each team computes them slightly differently. What breaks without a shared feature layer? What breaks with one (rigidity, a central team as a bottleneck)? Reward answers that name training-serving skew as the thing a feature store prevents, and that set a threshold ("worth it at forty models, not at three").

**Theme C · Whose data is it** (posted Thursday, as the twist)
The fraud team wants to add a feature derived from the customer's nationality; the data exists in the warehouse. Which of the six data questions from the session stop this, and who has the authority to decide? Expected: question 6 (are we allowed to use it: protected attribute, GDPR, discrimination risk) stops it; Risk & Compliance decides, the product owner is accountable, the data scientist is consulted. Bridge to Session 7 (fairness) and Session 12 (governance).

---

## 5. Pipeline diagram template (attach to the opening post)

Draw four to six boxes in order. For each box, fill the three lines. Arrows go one way; no loops.

| Step | Input → Output | Which notebook cells it absorbs | Which check it performs (stop the pipeline if…) |
|---|---|---|---|
| 1 · Ingestion & versioning | raw file → dataset snapshot #__ | | |
| 2 · Validation | snapshot → validated snapshot (or STOP) | | |
| 3 · Pre-processing & features | validated snapshot → feature table | | |
| 4 · Training & evaluation | feature table → model + metrics | | |
| 5 · Registration | model + metrics → registry entry (version, owner) | | |
| (6 · Scoring) | new customers → predictions | | |

**Rationale (150–250 words):** what breaks in the notebook that this pipeline fixes.

---

## 6. Notebook answer key (professor only)

`churn_exploration.ipynb` was built with every problem planted on purpose. Q1 answers should catch most of the first two groups; the third group separates strong answers.

**Reproducibility (the notebook cannot be re-run)**

- The heading says "Don't run all cells at once, some of them are old."
- Execution counts are out of order (cells 12, 9, 10, 7, 8…): the state in memory depended on the order a human clicked.
- A hard-coded laptop path is commented out above a relative path.
- `import pandas` appears twice "in case the kernel restarted".
- The scaler cell overwrites the columns in place; running it twice scales twice ("the scaler cell breaks if you run it twice").
- `df = df[...]` mutates the working frame mid-way; later cells depend on which filters ran.
- No random seed: "0.84 yesterday, 0.87 today, whatever."
- The model is pickled mid-notebook (`final_model_v3_FINAL2.pkl`) with no record of the code, data or settings that produced it.

**Data is never validated (checks are comments, not code)**

- `df.isna().sum()` printed, followed by the markdown "looks fine, will fix later".
- `support_tickets` contains -1 (impossible); the notebook works around it with `.abs()` and a comment, and lists it under "things I still need to do".
- `MonthlyCharges` has 999 outliers, removed by a magic number (`< 118`) with the comment "some weird values".
- `Region` has "north" and "North"; fixed by hand for one value.
- Twelve duplicated customers, noted in the to-do list, never removed.
- `signup_date` is text in dd/mm/yyyy; never parsed.
- Missing charges filled with the mean after a first model was already trained without them.

**The result cannot be trusted (leakage and selection on the test set)**

- `plan_churn_rate` is computed from the target on the whole dataset, then used as a feature: target leakage.
- The scaler is fitted on the whole dataset before the split: the test set leaks into training statistics.
- The decision threshold (0.4) is chosen by looking at the test set, then reported as if it were an honest estimate.
- Three random forests copy-pasted with hand-edited settings; only the last survives, with no record of the others.
- Feature engineering appears in two places (`tenure_bucket` and the scaled numeric columns) with different logic.
- The "quick check for IT" scores one row from the test set with the in-memory scaler: production would have to reproduce `sc`, `num_cols`, `rate` and the 118 filter from memory.

**What a strong pipeline answer looks like.** Ingestion: read the raw file, record a snapshot number and a hash, parse dates. Validation: stop if columns are missing, if `support_tickets < 0`, if `MonthlyCharges` is outside a range or more than X% empty, if there are duplicated IDs, if `Region` has unknown values. Pre-processing: fill, scale and derive features with parameters **fitted on the training split only** and saved with the model; no target-derived features. Training and evaluation: fixed split, fixed seed, several metrics, threshold chosen on a validation split, not on test. Registration: model + parameters + data snapshot + metrics as one versioned entry with an owner. Scoring reuses the saved pre-processing.

---

## 7. Mid-week posts

**Tuesday nudge.** Quote two Q1 diagrams that put the validation step in different places (one before pre-processing, one after) and ask which is right and why (before: it protects the expensive steps and catches the raw problems; some checks, such as statistics on features, also belong after). Post Theme B.

**Thursday twist.** Post Theme C, and add a twist to Q2: "Your QA environment costs €40,000 a year and the CFO wants it cut. What is the minimum you would keep, and what would you say to the CFO in one sentence?" Expected: keep the gate even if the environment shrinks (a smaller copy, run on demand); the sentence relates the cost to the cost of one weekend like IberBank's.

**Friday synthesis.** 300 words: the three best contributions with names; the misconception of the week; the bridge to Session 5.

> *What you said.* [Three insights, attributed.]
> *The misconception of the week.* Many Q1 answers put "validation" as a box that prints statistics. A validation step that cannot stop the pipeline is a comment, not a control. The test is: what happens at 3 a.m. if the vendor changes the units? If the answer is "the model trains anyway", it is not validation.
> *What comes next.* On Saturday the pipeline starts running itself: tests for code and tests for data on every change, and the ways a new model reaches customers without anyone noticing: canary, blue-green, A/B. Look at the Actions tab of the demo repository before class and note what the green tick is checking.

Reuse the synthesis as the recap slide for Session 5.

---

## 8. Model-answer notes (for grading)

### Q1 · Notebook to pipeline

A strong answer has four or more boxes in a sensible order, names which cells each box absorbs, and gives each box a **stopping condition**. It mentions at least one leakage problem (scaler fitted before the split, or the target-derived feature) and says pre-processing parameters must be saved with the model for scoring. The rationale connects to a production failure ("IT cannot reproduce `sc` from memory"). Weak answers redraw the notebook's headings as boxes with no checks, or describe validation as "look at the data".

### Q2 · Three environments

A strong answer explains each environment by **who** works there, **what data** it has and **what can go wrong** there without harm, and describes the two gates (tests and validation; sign-off and rollback). The laptop-to-production part names concrete failure modes: library versions, pre-processing left behind, load, live feed vs file, nothing to roll back to, nobody accountable. Reward proportionality (a low-risk internal model may need a lighter gate). Weak answers say "QA is where you test" and stop.

### Q3 · Threat, mitigation, detector

A strong answer names a **specific** threat with a mechanism (not "hackers"), a control from one of the three families, and a detector that is a **record**: the validation report for a snapshot, the lineage from a wrong prediction back to the data version and the change that entered that day, the registry showing a deployment with no QA record, or a monitoring signal (blocked-rate per merchant, amount-band patterns). Reward answers that distinguish prevention from detection. Weak answers give the mitigation only, or a detector that is a person ("someone would notice").

### Participation rubric, applied to this forum

| Level | This week |
|---|---|
| Excellent | Three complete artefacts; diagram with stopping conditions; replies that change or sharpen someone's pipeline; contributes to a theme thread |
| Good | Three complete artefacts; two relevant replies |
| Satisfactory | Artefacts complete but generic (boxes without checks; "QA is for testing") |
| Insufficient | Missing artefacts, off-topic, or posted Friday night with no interaction |

---

## 9. Checklist before opening

- [ ] `churn_exploration.pdf` (and `.ipynb`, `churn_raw.csv`) on campus by Wednesday 7 October, announced as the "look at one thing" task
- [ ] Opening post published with the three questions and Theme A
- [ ] Pipeline diagram template attached
- [ ] Session 3 slides and the IberBank case posted
- [ ] Two contrasting Q1 diagrams picked for Tuesday
- [ ] Reading for Session 5 announced (Treveil ch. 5–6; Google Cloud MLOps whitepaper up to level 1)
