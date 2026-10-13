# Forum 2 Pack · Session 4 · 10–16 October 2026

**Recap of Session 3 — ML Pipelines, Environments & Security**
*Everything needed to open, run and close the forum: coverage check, the opening post, the optional extra themes (including the MLflow lab), mid-week posts, the pipeline diagram template, the notebook answer key, and model-answer notes.*

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
- *Tuesday, with Optional Theme A (MLflow lab):* `mlflow_lab/MLOps_S04_MLflow_Lab_Student_Guide.pdf`, `mlflow_lab/MLOps_S04_MLflow_Lab.ipynb`, `notebook/churn_raw.csv` and `mlflow_lab/MLOps_S04_MLflow_Lab_Example_Output.html`.

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

*The optional themes were not part of the opening post; see the posting plan in section 4.*

---

## 4. Extra discussion themes (all optional)

**Every theme is optional.** Say so each time you post one: the three questions are the graded work; a theme reply is a way to go further, and nobody loses marks for skipping it. Label each post "Optional Theme X" so students see it at a glance.

**Posting plan**

| When | Theme | Why then |
|---|---|---|
| Tuesday 13 October | **A · MLflow lab** and **B · Skip QA** | A is hands-on and takes 20 minutes. B needs only an opinion and is still warm from Saturday's poll, so students who will not do the lab have a theme too. Both are about who signs off. |
| Thursday 15 October | **D · Whose data is it** | The twist; bridges to Sessions 7 and 12. |
| Spare | **C · Feature store or not** | Post only if a thread needs a push, or keep it for Session 5. |

**Optional Theme A · Hands-on: give María's model a memory** (MLflow lab; post on Tuesday 13 October with Optional Theme B)
The only hands-on theme. Students who want to try MLflow themselves train four versions of María's churn model in Google Colab (nothing to install), and MLflow records each run. They then compare the runs and post a screenshot with 120–200 words. It is designed for people who have never written code: they press ▶, read and choose settings from a form. Like every theme, it is optional: it counts as a theme contribution in the rubric, and nobody is penalised for skipping it. Files are in `S04/mlflow_lab/`, and the expected results and grading notes are in section 8.

Post to paste:

> **Optional Theme A · Hands-on: give María's model a memory**
>
> On Saturday we looked at María's notebook: her model scored *"0.84 yesterday, 0.87 today"*, and nobody could say why. This week you can try MLflow yourself: train four versions of her churn model in Google Colab, let MLflow record every attempt, and compare them. No code to write and nothing to install; you need a laptop, a Google account and about 20 minutes.
>
> Files attached: `MLOps_S04_MLflow_Lab_Student_Guide.pdf` (start here), `MLOps_S04_MLflow_Lab.ipynb` (the lab), `churn_raw.csv` (María's data) and `MLOps_S04_MLflow_Lab_Example_Output.html` (all the results, if Colab does not work for you).
>
> Post one screenshot of your comparison table and 120–200 words: (1) which run you would send to QA and why; (2) what you changed in your own run and what happened; (3) what MLflow recorded and what is still missing if your manager asks in six months *"which model is live, and who said it was good enough?"*. Then reply to one classmate whose choice differs from yours.
>
> Optional, like every theme this week: it counts as a theme contribution, and nobody loses marks for skipping it.

**Optional Theme B · Skip QA to hit the launch date** (post on Tuesday 13 October with Optional Theme A)

Post to paste:

> **Optional Theme B · Skip QA to hit the launch date**
>
> On Saturday you voted on this in the chat, and I left it open. The CEO wants the churn model live on Friday; QA needs a week. What do you say to the CEO, and what do you put in writing? One paragraph is enough. If you also did Optional Theme A, connect the two: who would sign?
>
> Optional, like every theme this week: it counts as a theme contribution, and nobody loses marks for skipping it.

*Facilitator notes:* polled in chat, left unresolved. Push for a proportionate answer: what is the cheapest gate that still protects the company (a named owner, a rollback plan, a limited rollout)? Reward students who distinguish an internal low-risk model from a customer-facing one, and who write the "what I put in writing" part: a one-paragraph risk acceptance signed by the business owner.

**Optional Theme C · Feature store or not** (spare: post only if a thread needs a push, or keep it for Session 5)
A retailer has 40 models that share 12 customer features (tenure, average basket, last purchase…). Each team computes them slightly differently. What breaks without a shared feature layer? What breaks with one (rigidity, a central team as a bottleneck)? Reward answers that name training-serving skew as the thing a feature store prevents, and that set a threshold ("worth it at forty models, not at three").

**Optional Theme D · Whose data is it** (post on Thursday 15 October, as the twist)
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

**Tuesday nudge.** Quote two Q1 diagrams that put the validation step in different places (one before pre-processing, one after) and ask which is right and why (before: it protects the expensive steps and catches the raw problems; some checks, such as statistics on features, also belong after). Post Optional Theme A (the MLflow lab, with its four files) and Optional Theme B (Skip QA).

**Thursday twist.** Post Optional Theme D, and add a twist to Q2: "Your QA environment costs €40,000 a year and the CFO wants it cut. What is the minimum you would keep, and what would you say to the CFO in one sentence?" Expected: keep the gate even if the environment shrinks (a smaller copy, run on demand); the sentence relates the cost to the cost of one weekend like IberBank's.

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

### Optional Theme A · MLflow lab: expected results

The data is fixed and every random step has a seed, so every student gets **exactly** these numbers for the prepared runs (checked by running the notebook end to end with MLflow 3.15.2):

| Run | Unseen customers (test AUC) | Studied customers (train AUC) | Gap | Churners caught (recall) | Alerts right (precision) |
|---|---|---|---|---|---|
| A · simple-logistic | **0.715** | 0.715 | 0.000 | 0.466 | 0.626 |
| B · forest-depth-4 | 0.700 | 0.786 | 0.086 | 0.459 | 0.663 |
| C · forest-no-limit | 0.628 | **1.000** | 0.372 | 0.481 | 0.485 |
| *Example D: B with split seed 7* | 0.717 | 0.772 | 0.056 | 0.353 | 0.653 |

The cleaning receipt reads: 1,212 rows received, 12 duplicated customers removed, 25 rows set aside for negative support tickets, 8 charges above 200 marked empty, 1,175 rows ready, 67 charges filled inside the model, 38% churned, data fingerprint `churn_raw-2445f33d`. If a student shows a different fingerprint, they used a different file.

**What students will find in Step 7**

- **Seed only (model B unchanged):** the unseen score moves between **0.66 and 0.72** (seed 1: 0.703; 7: 0.717; 11: 0.668; 42: 0.700; 123: 0.660; 2026: 0.711). Logistic regression moves between 0.69 and 0.73. The identical model gains or loses five points depending on which customers land in the test set. That is María's "0.84 vs 0.87".
- **Depth (seed 42, 200 trees):** the unseen score stays flat at about 0.70 for depths 1–4, then falls (depth 6: 0.683; 8: 0.660; 10: 0.646; no limit: 0.628). Meanwhile the studied score climbs to 1.0. The sweet spot is a shallow forest, and it is no better than the logistic regression.
- **A side effect worth rewarding:** with seed 7, the AUC goes *up* (0.717) while churners caught goes *down* (0.459 → 0.353). Two metrics can disagree, so you choose the metric the business cares about *before* comparing runs.

**Q1 · Which run to QA.** A strong answer rejects C explicitly: 1.00 on studied customers is memorisation (overfitting), and C is the worst on unseen customers. It picks A, or B with a reason. The best answers notice that A and B differ by 0.015, which is less than the seed alone moves the score, so the data cannot separate them. They therefore prefer the simpler, explainable A, or ask for several splits (cross-validation) before choosing. Bonus: noticing that every model catches fewer than half the churners at the default threshold, which is a business decision to make with the retention team. Weak answers pick the highest number in any column.

**Q2 · Own run.** A strong answer states the setting changed, the before and after numbers, and the conclusion: "the same model scored 0.70 and 0.72, so a three-point difference between two untracked runs means nothing unless we know the seed and the data version". Reward students who connect this to why MLflow stores `split_seed` and `data_version` as parameters.

**Q3 · What is still missing.** MLflow recorded the settings, the split seed, the data fingerprint, the cleaning rules, the metrics, the author, the time and the model file. A strong answer names at least two things it did **not** capture:

- **Code version:** the Session 3 script logged a git commit; this Colab notebook is not versioned.
- **Approval:** who signed off, and when. This lives in the registry (version, alias, approval tag), seen in Session 3 and coming back in Session 5.
- **Business purpose and threshold:** what the score is used for, and at which score a customer gets called.
- **Data permission:** whether we are allowed to use this data (data question 6 from Session 3).
- **Fairness check** (Session 7).
- **Where the model is deployed and since when.**

The line to quote in the synthesis: *MLflow records the experiment; the registry and governance record the decision.*

**Misconception of the thread (likely):** "C is best because it scores 1.00." Answer with the exam analogy from the notebook: a student who memorises last year's answers scores 100% on last year's exam.

### Participation rubric, applied to this forum

| Level | This week |
|---|---|
| Excellent | Three complete artefacts; diagram with stopping conditions; replies that change or sharpen someone's pipeline; contributes to an optional theme thread (any of A–D) |
| Good | Three complete artefacts; two relevant replies |
| Satisfactory | Artefacts complete but generic (boxes without checks; "QA is for testing") |
| Insufficient | Missing artefacts, off-topic, or posted Friday night with no interaction |

---

## 9. Checklist before opening

- [ ] `churn_exploration.pdf` (and `.ipynb`, `churn_raw.csv`) on campus by Wednesday 7 October, announced as the "look at one thing" task
- [ ] Opening post published with the three questions
- [ ] Tuesday 13 October: Optional Themes A (lab, four files) and B (Skip QA) posted
- [ ] Thursday 15 October: Optional Theme D posted with the twist
- [ ] Pipeline diagram template attached
- [ ] Session 3 slides and the IberBank case posted
- [ ] Two contrasting Q1 diagrams picked for Tuesday
- [ ] Optional Theme A: open `MLOps_S04_MLflow_Lab.ipynb` in Colab yourself once and run all cells (about 3 minutes); check the receipt shows fingerprint `churn_raw-2445f33d` and run A scores 0.715
- [ ] Reading for Session 5 announced (Treveil ch. 5–6; Google Cloud MLOps whitepaper up to level 1)
