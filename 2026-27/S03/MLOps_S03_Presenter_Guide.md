# Session 3 · Presenter's guide: how to explain each slide to a non-technical cohort

**MLOps elective · Master in Business Analytics and Data Science · MBDS-PT2026F · Session 3 (Live, Saturday 10 October 2026, 90 minutes)**

A companion to the deck's speaker notes, written for *delivery*. For each slide: the **point** (why it is there), **say it like this** (plain language and an analogy that works for students with no coding background), the **line to land**, and a **question to ask the room**. Timings match the notes in the deck.

The shape of the session: opening and Forum 1 recap (1–4) → notebook to pipeline (5–8) → data (9–14) → the MLflow demo (15–16) → environments (17–21) → break (22) → security (23–26) → the IberBank activity (27–29) → close (30–32). Slides 33–38 are an appendix, not covered live.

Three threads to keep pulling all session: **a pipeline is a factory, not a workshop** (5–8), **version everything, so any prediction can be traced back** (12, 15–16, 21), and **nothing reaches production without passing a gate signed by someone accountable** (19–20, 29). They are the three things to remember on slide 30.

---

## Before Saturday: checklist

- [ ] **Slide 2:** paste two or three quotes from your Forum 1 synthesis into the placeholders (Friday night, after the forum closes).
- [ ] **Slide 3:** María's notebook (PDF, in `S04/notebook/`) is on the campus; the session opens by harvesting what students found in it.
- [ ] **Activity:** the student part of `MLOps_S03_Activity_Brief.md` (everything above "Facilitation notes") and the blueprint template are on the campus.
- [ ] **Breakout rooms:** decide random rooms or project teams (slide 27 says "your project team"); set up during the break.
- [ ] **Demo, the day before:** double-click `demo/mlflow/start_mlflow_ui.command`; check the runs table shows `accuracy` and `data_version` (add them with **Columns** if not); rehearse Optional A once (Register model on `rf-100`); then run `rebuild_demo.command` to reset; open `demo/offline_fallback.html` once so you know it is there.
- [ ] **Slide 32:** open the demo repository's Actions tab (`github.com/juanmaramirezgarcia/mlops-demo-churn/actions`) and check the latest run is green; students are asked to look at it this week.
- [ ] **Forum 2 pack** (`S04/MLOps_S04_Forum2_Pack.md`) ready to open on Saturday night.

---

## Opening (1–4)

### Slide 1 — Title *(leave by minute 2)*
**Point:** atmosphere and a link back to last week. **Say it like this:** as people arrive, ask in the chat "Did you open María's notebook?"; it warms the room and tells you how many prepared. Opening line: "Last week we said a model in production is a running process, not a file. Today we take that process apart: how a notebook becomes a pipeline, why companies keep three copies of everything, and how a model can be attacked." Same rhythm as last week: break at minute 46, one breakout after it, the forum opens tonight. **Land:** the opening line. **Ask:** —

### Slide 2 — What Forum 1 said, and what today adds *(minutes 2–4)*
**Point:** show students their own words, then set today's outcomes. **Say it like this:** read one quote, name the student and thank them; students who see their words on the first slide post more next week. Then the misconception of the week, *operationalising = "putting it on a server"*, corrected in one sentence with last week's phrase: it is a running process with an owner. Read the three outcomes. **Land:** "Same shape as last week: concepts, a demo, a poll, a break, one breakout." **Ask:** —

### Slide 3 — What you found messy in María's notebook *(minutes 4–6)*
**Point:** every messy thing in a notebook is a production failure waiting to happen. **Say it like this:** 90 seconds in the chat, "type one messy thing you noticed"; read five or six aloud and sort them live into the three columns (it cannot be re-run · nobody checks the data · the result cannot be trusted). For non-technical students a notebook is a **personal lab notebook**: it works for the person who wrote it, in the order they happened to write it. "Cells run out of order" is a recipe where step 5 only works if you happened to do step 8 the day before. Do not diagnose the whole notebook: that is Forum 2, question 1. **Land:** "Every messy thing in that notebook is a production failure waiting to happen, and each column is a part of today." **Ask:** the chat harvest.

### Slide 4 — The questions an MLOps plan must answer *(minutes 6–8)*
**Point:** the course map, and the group project in one table. **Say it like this:** read only the column headings and give one example question for each of the four on the left (today); the two on the right are Sessions 5 and 7; the bars at the bottom apply everywhere. **Land:** "Your group project is, essentially, this table filled in for a real company, with a roadmap and owners." Say it slowly. **Ask:** —

## From notebook to pipeline (5–8)

### Slide 5 — Divider *(minute 8)*
**Point:** the image for the block. **Say it like this:** "A notebook is a workshop, where one craftsman makes one thing his way. A pipeline is a factory, which makes the same thing every time, with a quality check at each station." **Land:** that sentence. **Ask:** —

### Slide 6 — A model is a formula plus everything that feeds it *(minutes 8–10)*
**Point:** the formula is useless if its inputs are prepared differently in production. **Say it like this:** once trained, a model is just a formula: inputs in, a number out, same inputs, same answer. The right-hand box is the point: the preparation of the inputs is part of the model. A recipe that says "200 g of flour" is ruined if the kitchen measures in ounces; the recipe is fine, the ingredients arrived in a different shape. (Keep this analogy: IberBank's euros-to-cents incident in the activity is the same story.) **Land:** "The model is the formula *plus* everything that prepares its inputs. In María's notebook that preparation is scattered across 20 cells, which is why it can't be handed to IT." **Ask:** —

### Slide 7 — The same work, drawn twice *(minutes 10–13)*
**Point:** a pipeline is steps with an input, an output and a check, run in the same order every time. **Say it like this:** left, the tangle, where the order depends on what a human did; right, four labelled steps. Three properties, all plain English: each step can be **tested on its own, re-run on its own, and read by anyone**. **Land:** "Forum 2, question 1: you'll draw the right-hand side for María's notebook." **Ask:** "Which step on the right would have caught the '-1 support tickets'?" (Validate.)

### Slide 8 — Why pipelines, and the DAG *(minutes 13–16)*
**Point:** the chain runs itself, a class of bugs disappears, every experiment is tracked. **Say it like this:** when new data arrives the whole chain runs without anyone remembering the steps; the classic bug (preparation changed after training) disappears; every experiment is recorded. "DAG" is a **to-do list with arrows**: you can't bake before you mix, and you never loop back ("directed" = the arrows have a direction, "acyclic" = no circles). Name Airflow and Kubeflow as the tools that run these lists; do not explain them. **Land:** "A pipeline is a to-do list a machine follows, in order, every time." **Ask:** —

## Data: where the time, and the failures, live (9–14)

### Slide 9 — Divider *(minute 16)*
**Point:** frame the block. **Say it like this:** "These three steps look small on the map, but they are where most of the calendar goes in any real ML project, and most of the failures." **Land:** that sentence. **Ask:** —

### Slide 10 — Six questions to answer before training anything *(minutes 16–18)*
**Point:** you don't need to code to ask these. **Say it like this:** read each question as one a product owner could ask without any statistics. Before building a house you ask whether the land is yours, whether the trucks can reach it, and whether you're allowed to build there. The two orange questions kill projects late: data that exists in the warehouse but **not at the moment of the decision**, and data you are **not allowed to use**. **Land:** "These are business questions, and they come before the first model." **Ask (chat):** "Which of these did NorthRetail get wrong?" (Number 5: a source changed and nobody told the data team; and nobody owned the data.)

### Slide 11 — The data you train on must be obtainable when the model runs *(minutes 18–20)*
**Point:** two rules: the same shape in both places, and available at the moment of the decision. **Say it like this:** "In the notebook you had all the time in the world and a human to clean things. In production the model gets whatever arrives, instantly, alone." A fraud model can't wait for tonight's warehouse load: the customer is at the till now. A column called `MonthlyCharges` in one place and `monthly_charges_eur` in the other is a bug waiting to happen. **Land:** "Same shape, and available at the moment of the decision, not tonight." **Ask:** —

### Slide 12 — Version the data like the code *(minutes 20–22)*
**Point:** three habits that make a model reproducible and defensible. **Say it like this:** **split once and keep the split** ("Why did María get 0.84 yesterday and 0.87 today? She re-shuffled the data every time she ran it"); **snapshots** ("trained on snapshot 12" is a fact; "trained on the data" is not); **fingerprint**: a "hash" is a fingerprint for a file, a short code calculated from every byte, so change one comma and it changes, and you can prove the data is exactly the same. Callback: "Last week a repository was a folder with a memory. This is the same memory, for data." **Land:** "If you can't say which data trained the model, you can't reproduce it, and you can't defend it in an audit." **Ask:** —

### Slide 13 — Data validation: three checks that stop the pipeline *(minutes 22–25)*
**Point:** the heart of the block; validation is what makes automatic retraining safe. **Say it like this:** the goods-in dock of a factory checks a delivery *before* it goes on the line. (1) **Anomalies**: impossible items in the box, −1 support tickets, a €999 charge, a column that is 60% empty. (2) **Schema**: the box has the wrong labels, columns renamed or a code format changed. (3) **Statistics**: the delivery looks unusual compared with normal ones; either the world changed or the supplier sent the wrong thing, and both need a human. Connect to what they know: NorthRetail's product codes fail **check 2**; the "Fix" commit in last week's demo repository is **check 1**; in five minutes MLflow will show a run rejected by **check 1** while its accuracy barely moved. Name Great Expectations and Evidently; do not show them. **Land:** "'Looks fine' is a comment. Validation is a test, and it stops the line." **Ask:** —

### Slide 14 — The same code in training and in production *(minutes 25–28)*
**Point:** training-serving skew, the price of feature engineering, and the feature store. **Say it like this:** two cooks make "the same recipe" from memory, one with salted butter; each dish looks right, they taste different, and nobody can say why. The fix: **one** piece of preparation code, used both for training and for live predictions, never rewritten. More features mean more accuracy, but harder to reproduce live and harder to explain. A **feature store** is a shared, labelled pantry of ready-prepared ingredients every model uses, so forty models don't each calculate "customer tenure" differently. Tie it to last week's poll: "Is it worth it for three models? Probably not. At forty, yes. MLOps scales with what's at stake." **Land:** "Prepare once, use everywhere." **Ask:** —

## The memory for models: the MLflow demo (15–16)

### Slide 15 — An experiment log and a registry, then the demo *(minutes 28–35)*
**Point:** two kinds of memory for models, shown live. **Say it like this:** set up both ideas *before* switching to the browser. The **experiment log** is a lab journal the machine keeps for you: every attempt, with its code, data, settings, score and model file ("María's three copy-pasted random forests would be three rows here"). The **registry** is the shortlist, the "approved" shelf in a warehouse: only the models that matter, each with a version, an owner and a status. Read the bottom line as a recipe: *code v2.1 + data snapshot 12 + run 4 = model v1.1*. **Land:** "Every attempt is a row, not a memory." **Ask:** —

**Then run the demo (7 minutes, browser only), following `MLOps_S03_Demo_Script.md`:**
1. **Runs table (≈2.5 min).** Sort by accuracy: `rf-300-depth8` 0.833, `lr-4-features-promo` 0.823, `rf-100` 0.816, `lr-3-features` 0.809, `rf-300-depth8-extract-0612` 0.796. "The best number is 0.833. Is it the best model? Not yet; it's the best number." Compare `lr-3-features` with `rf-300-depth8` and point at `data_version` first: three things changed at once (the data, March against June; the algorithm; the features), so is the jump a better algorithm or just newer data? The log is what lets you ask.
2. **The rejected run (≈1.5 min).** Its tag: "data validation failed: 60% of tenure_months empty, read as 0". Accuracy 0.796 against 0.833 barely looks worse; check 1 caught it, the metric did not. (Naming NorthRetail here is fine: they diagnosed it last week.)
3. **The registry (≈2 min).** The model's description, "Owner: Customer Retention (accountable), Data Platform (responsible)", is Session 1's RACI written into the tool. Version 1 `@production`, approved by the product owner on 3 March 2026 (the same date as v1.0 in last week's GitHub demo). Version 2 `@challenger`, "validation passed 9 June 2026; fairness check pending". The `@production` label is a **pointer**: the "current version" sign on a shelf. The application takes whatever box the sign points at; promoting means moving the sign, not the boxes, and there is a record of who moved it. Click version 1 → source run to walk back to the attempt that produced it.
4. **Optional A (≈1 min), recommended:** register `rf-100` live. Version 3 appears with no label and no owner: "Registering is cheap. Promoting is the gate." Do B (move the label) only if ahead of time; skip C (training code) unless asked.

Be ready for: "version 2" in MLflow is the business release "v1.1" (MLflow counts registrations; the description carries the release name). If MLflow will not start: `demo/offline_fallback.html` shows the same three views from the real database.

### Slide 16 — What you just saw *(minutes 35–36)*
**Point:** freeze the demo into three sentences. **Say it like this:** **the runs table**: every attempt in one view, and the best number isn't automatically the best model; **the rejected run**: the metric barely moved, validation caught it; **the registry**: registering is cheap, promoting is the gate, a pointer only certain people may move. **Land:** "The registry says which model is approved. It doesn't say where it runs. That's next." **Ask:** —

## Environments: Dev, QA, Prod (17–21)

The tightest ten minutes of the session. If the demo ran over, shorten slide 18, never the poll.

### Slide 17 — Divider *(minute 36)*
**Point:** this block answers Forum 2, question 2. **Say it like this:** "Why do companies keep three copies of everything, and what does it cost to skip one? This block is Forum question 2, answered." **Land:** that sentence. **Ask:** —

### Slide 18 — Before "where", ask "whether" *(minutes 36–38)*
**Point:** a model often can't run in production as it is; decide the format on day one. **Say it like this:** three reasons it has to be adapted, sometimes rebuilt by another team: **tooling** (built in Python, production expects another format), **speed** (fine for one prediction, too slow for thousands a second, or it must run on a small device), **data access** (the inputs must be reachable where the model runs). *Measure the door before you build the sofa.* **Land:** "Decide the production format on day one, not at the end." If short of time, say only this. **Ask:** —

### Slide 19 — Three environments, two gates *(minutes 38–41)*
**Point:** the gates matter more than the boxes. **Say it like this:** a theatre. **Dev** is the rehearsal room (mistakes are the point); **QA** is the dress rehearsal on the real stage with no audience; **Prod** is opening night with paying customers and critics. **Gate 1 (Dev → QA):** tests pass, data validated, model registered with a version and an owner (what they just saw in MLflow). **Gate 2 (QA → Prod):** behaves like production under load, sign-off by the accountable owner, a rollback plan, and **not promoted by the person who built it**: the **four-eyes principle** they know from finance. "Gate 2 in a tool is the pointer only certain people may move." **Land:** "Nothing goes from a laptop to production. Someone accountable signs the gate." **Ask:** "Why shouldn't the person who built the model promote it?"

### Slide 20 — What goes wrong from a laptop straight to production, plus the poll *(minutes 41–44)*
**Point:** Forum 2, question 2, in one slide. **Say it like this:** six failures, each with an everyday version: **library versions** (a file from the newest Word opened in a ten-year-old version: it opens, garbled); **preparation left behind** (the recipe shipped without the preparation steps); **never tested under load** (dinner for two works, a wedding for a thousand collapses); **tested on a file, not the feed** (the live data has different names and arrives late); **nothing to roll back to**; **nobody signed off** (so nobody is accountable on a Saturday). Then the **chat poll (2 min):** "A model that works on the data scientist's laptop can go to production the same day if the business is in a hurry." AGREE or DISAGREE, one line why; use the "type it but don't press Enter until I say go" trick. Read two contrasting answers and **do not resolve**: it becomes Forum 2 Theme A. For your Friday synthesis: sometimes yes, for a low-risk internal model with a named owner and a rollback plan; never for a customer-facing or regulated decision. **Land:** "The gate should match the cost of being wrong", the same conclusion as Session 1's poll. **Ask:** the poll.

### Slide 21 — Reproducibility, auditability, lineage *(minutes 44–46)*
**Point:** from any prediction, walk back to its data. **Say it like this:** **food traceability**: a supermarket recall traces one bag of salad back to the farm, the field and the harvest date; lineage does the same for a prediction (14 April, customer 1042 → model v1.1 → run 4 → code commit → data snapshot 12). **Reproducibility:** re-run the exact experiment, get the same model. **Auditability:** the full history of every version in one reliable place. Bridge to security: "Lineage is also how you find an attack or a broken feed after the fact: if predictions went wrong from a certain day, lineage tells you what entered that day" (Forum 2, Q3). **Land:** "From any prediction, walk back to its data." **Ask:** —

### Slide 22 — Break, 5 minutes *(minute 46)*
**Point:** rest, and prime the security block. **Say it like this:** leave the question on screen: "What is the most valuable model in your company, and who could break it on purpose?" Use the five minutes to set up the breakout rooms (groups of 4–5). **Land:** "Back at minute 51." **Ask:** the on-screen question.

## Security: how a model can be attacked (23–26)

Seven minutes; its job is the vocabulary for the activity. Keep it brisk.

### Slide 23 — Divider *(minute 51)*
**Point:** come back from the break thinking like attackers. **Say it like this:** "Back with the question I left you: who could break your company's most valuable model on purpose? Seven minutes on how, then you'll defend a bank's model yourselves." Read one chat answer to the break question if there is one. **Land:** that sentence. **Ask:** —

### Slide 24 — Where model risk comes from *(minutes 51–53)*
**Point:** risk sources, and what amplifies them. **Say it like this:** the three questions on the slide: what if the model behaves in the worst way imaginable? what if someone extracts its data or its logic? what would that cost (money, legal, safety, reputation)? Sources: bugs, poor data, production data unlike training data, misuse of outputs. Amplified by wide use, a fast-changing world, models feeding each other. Every company keeps a risk register; AI adds new rows. **Land:** "Use the IBM AI Risk Atlas as the checklist for your group project." **Ask:** —

### Slide 25 — Four ways to attack a model *(minutes 53–56)*
**Point:** one picture and one control per attack. **Say it like this:**
- **Data poisoning** (corrupting what the model learns from): slipping wrong answers into the textbook a student studies from. Control: validate the data, know where labels came from, keep lineage.
- **Evasion** (inputs crafted to be misread): drivers who learn the speed camera flashes above 120 and drive at 119; here, transactions just under the blocking threshold. Control: watch for probing patterns, limit requests, retrain on what you find, never reveal the exact score.
- **Extraction and inversion** (querying thousands of times to copy the model or recover its data): asking a chef ten thousand "what if I add salt?" questions until you can cook the recipe yourself. Control: log-ins, request limits, answers rounded to "approve/decline" rather than "0.8731", monitoring who asks what.
- **Prompt injection** (AI chatbots): a note slipped into a letter, "ignore your boss and do what I say". Name it only; Session 10.

Name OWASP Machine Learning Top 10 and MITRE ATLAS, names only. The evasion example is deliberately close to incident 2 in the activity: it is the vocabulary they need, not a spoiler. **Land:** "Four attacks, four controls, and lineage to find them afterwards." **Ask:** —

### Slide 26 — Controls: the ones you already have, and the ones AI adds *(minutes 56–58)*
**Point:** you don't start from zero. **Say it like this:** most controls are what the company already does (access control, encryption, backups, incident handling, audits), extended to data, models and the model's interface. AI adds a few (drift detection, protection against probing, securing training data). At company level: a register of AI systems with owners, a risk assessment per use case, someone who signs off. **Land:** "In the activity you'll pick one control per incident; your answers come from these three columns." **Ask:** —

## The IberBank activity (27–29)

### Slide 27 — The brief *(minutes 58–60)*
**Point:** set up the task before opening the rooms. **Say it like this:** same case for every room, IberBank's card-fraud model with three incidents. For each: **threat → lifecycle stage where it entered → one control → who owns it → how you'd detect it**. Bonus: which incident would a financial regulator care about most? Rooms of 4–5, one slide or whiteboard, a spokesperson with 2 minutes. Paste this in the chat **before** opening the rooms:

> **Breakout rooms, 15 minutes (back at minute 76).** Zoom will move you automatically.
> 1. Open the IberBank case and the blueprint template on the campus.
> 2. Choose a spokesperson (2 minutes in the debrief).
> 3. For each of the 3 incidents: threat → lifecycle stage → one control → who owns it → how you'd detect it.
> 4. Bonus: which incident would a financial regulator care about most, and why?
>
> Need me? Click **Ask for Help**. To come back early: **Leave Room**, not "Leave Meeting".

**Land:** "Use today's words: the nine steps, the three checks, the three environments, the four attacks." **Ask:** —

### Slide 28 — The case, facts only *(minutes 60–61)*
**Point:** read the facts once, aloud, without diagnosing. **Say it like this:** three incidents, deliberately of different kinds: (1) **March**, a data vendor switched amounts from euros to cents for some merchants, so €20 purchases were scored as €2,000 and blocked (slide 6's grams-and-ounces, back again); (2) **June**, a fraud ring found that purchases just under €30 at grocery stores were never blocked; (3) **September**, a data scientist pushed a Friday-evening fix from her laptop straight to production, skipping QA. Then send them to the rooms. **Land:** "Here are the facts. The diagnosis is your job." **Ask:** —

### Slide 29 — Debrief *(minutes 76–86)*
**Point:** every control they named is a pipeline step or a gate. **Say it like this:** three rooms present (2 minutes each), ideally one strong on each incident; then synthesise:

| # | Threat | Enters at | Control | Owner | Detected by |
|---|---|---|---|---|---|
| 1 | Data integrity (vendor changed units) | Ingestion / validation | Range and schema checks on the vendor feed; a data contract requiring notice of changes | Data engineer (control), product owner (contract) | Validation report per snapshot; a spike in blocks per merchant |
| 2 | Evasion (probing the threshold) | Live predictions / feedback | Watch for probing patterns; no fixed, guessable threshold; retrain on what is found; limits per card | ML engineer with the fraud team | Patterns by amount band and merchant; chargebacks confirm 60 days later |
| 3 | Environment (laptop hotfix, QA skipped) | Deployment | The two gates: only registered versions deploy, QA sign-off by someone else, rollback plan | Product owner accountable, ML engineer responsible, IT enforces | Lineage shows a change with no QA record; the weekend false-positive rate |

**The bonus:** regulators care most about incident 3 (no record, no human oversight) and about the customers wrongly blocked in incident 1. If someone says "the EU AI Act makes this high-risk", teach the nuance: the Act lists credit scoring as high-risk but **explicitly excludes fraud detection** (Annex III, point 5(b)); the pressure here comes from banking supervisors and GDPR's safeguards for automated decisions. Reward whoever spots it.

**Three misconceptions to correct:** "retrain more often" (it would not have stopped any of the three, and would have made incident 1 worse, learning from cents); "lower the threshold" (any fixed threshold gets found; the control is spotting the probing); "blame the data scientist for incident 3" (she fixed a real problem the only way the system allowed; push for the gate, not the person).

**Land:** "Every control you named is a step in the pipeline or a gate between environments. That is what MLOps is." Say it slowly. **Ask:** —

## Close (30–32)

### Slide 30 — Three things to remember *(minutes 86–87)*
**Point:** the A4-sheet lines; read slowly and tell them to write these down now. **Say it like this:** (1) *A notebook is a workshop; a pipeline is a factory*: steps with inputs, outputs and checks, run by a machine in the same order every time, and validation stops the line before a bad model is built. (2) *Version everything: code, data, models*: a repository, numbered data snapshots with a fingerprint, an experiment log and a registry, so any prediction can be traced back to its data. (3) *Three environments, two gates*: nothing goes from a laptop to production; Dev builds, QA tests as if live, Prod serves, and someone accountable signs the gate. **Land:** "Three lines for your A4 sheet. Write them now." **Ask:** —

### Slide 31 — Your forum this week *(minutes 87–89)*
**Point:** connect the session to the week's work. **Say it like this:** read the three questions (verbatim from the syllabus) and point to where each was covered: **Q1** (restructure María's notebook into a pipeline; a drawing and a paragraph, no code) = slides 7 and 13; **Q2** (why Dev, QA and Prod; what goes wrong from a laptop) = slides 19 and 20; **Q3** (one threat, a mitigation, and the lineage control that would detect it) = slides 21, 25 and 26. Today's poll is Theme A. Opens tonight, closes Friday 16 October; post early, reply to two classmates. **Land:** "Everything you need for these three is in today's slides." **Ask:** —

### Slide 32 — Before Session 5 *(minutes 89–90)*
**Point:** the reading and the one thing to look at. **Say it like this:** read Treveil et al., *Introducing MLOps*, chapters 5–6 (preparing for and deploying to production) and the first half of Google Cloud's "MLOps: continuous delivery and automation pipelines in machine learning" (up to "MLOps level 1"); optional, Huyen chapter 7. The "look at one thing": the demo repository's **Actions** tab, where every push shows a green tick or a red cross; write down what the tick is checking. Preview Session 5: tests for code and for data, and releasing a model without downtime (canary, blue-green, A/B). Thank them and stop on time. **Land:** "Bring your guess about what that green tick checks: that's where Session 5 begins." **Ask:** —

## Appendix (33–38), not covered live

Kept for students who want the technical detail and as a reference for the group project: how models are tuned (hyperparameters; grid, random and Bayesian search), AutoML ("automating the search, not the judgement"), and challenging a model before trusting it (useful for the project). **Slide 38, "the eight lines that give a training script a memory"**, is the one to reach for if someone asks during the demo "but how does a run get into MLflow?": it shows the same before/after as `train_with_mlflow.py` without opening an editor.

---

### Three delivery reminders
- **Protect the activity's time.** If the demo runs long, shorten slide 18 (one sentence) and slide 24, never the poll or the breakout.
- **Use the callbacks.** NorthRetail (slides 10, 13, the rejected run), last week's GitHub demo (slides 12, 15), and the Session 1 poll (slides 14, 20) make the course feel like one story.
- **Say the closing line of slide 29 slowly.** It turns the activity into a summary of the whole session.
