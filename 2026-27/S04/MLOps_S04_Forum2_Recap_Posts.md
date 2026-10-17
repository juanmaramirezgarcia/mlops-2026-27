# Forum 2 · Recap posts (one per question)

*Ready to paste on the campus, one per thread. Built from `MLOps_Forum2_Evaluation_and_Feedback.md` (17 October).*

---

## Q1 recap · From notebook to pipeline

Thank you all: 27 pipelines, and the shape is now right in almost all of them. Ingest, validate, pre-process, train, register, score, with the split done first and every transformer fitted on training rows only. That was the main lesson of Session 3, and you got it. Three things worth keeping:

**1. Look at the data before you trust a fix.** Mohamed ran the checks on `churn_raw.csv`. The 12 "duplicate customers" are rows 1200–1211, exact copies of rows 0–11: an export appended twice, so the fix is a row-count check at ingestion. 825 customers have a tenure their signup date does not allow. The mean fill (61.55) is inflated by the 999s, while the median is 51.31. And abs() turns 26 unknown ticket counts into 1. Sigursteinn and Mohamed both noticed that the <118 filter only works because the highest real charge is €114.32: a €120 customer next month would vanish silently. Manuel found that In [22], the check "for IT", scores a row that is already scaled, so it proves nothing about how a raw customer will be scored.

**2. Validation has two outcomes, not one** (Khem to Julio M.). If validation stops on *every* failed check, it stops on every run, because the raw data already contains 999s, -1 tickets and duplicates. Anas had the answer in his table: stop on what is broken (a missing column, a wrong type) and flag what is known. Known problems are then quarantined (Jack) and fixed by a written rule in pre-processing (Mohamed), not silently in a notebook cell.

**3. A pass mark needs a reference.** Marketing's 0.8 would reject every model, since the best accuracy is about 0.68 (Manuel to Rateel). The minimum is the "nobody churns" baseline, about 62% (Camila C., Barbara), *and* the model already in production (Fabio). The 0.8 is a business target to discuss, not a pass mark. Rateel's registration question belongs in every pipeline: *has anyone besides the builder approved it?*

Line of the week, from Anas: *"STOP if critical, warning if small."* In Session 5's demo you see exactly that: the pipeline stops when 70% of one feature is empty.

---

## Q2 recap · Three environments

24 answers, and most of you described Dev, QA and Prod correctly. Three lessons:

**1. Two things make the separation real.** First, the person who built the model is not the one who promotes it (Ana Cristina, Fabio, Samah). Second, what moves forward is the *same artefact*, not a rebuilt copy: Sigursteinn's *"build once, promote the same artefact"*. Gerard framed it well: each environment answers a different question.

**2. The failure you found most often was in María's own notebook:** the mean fill in training, fillna(0) in the March scoring cell. That is training–serving skew, and it is invisible until the predictions are wrong. Armen named one nobody else did: a leaked metric (plan_churn_rate, or a threshold picked on the test set) that the business then plans on.

**3. Your own stories were the best examples.** Gvantsa's next-best-offer model ran five times when a feature's update frequency changed, and customers were flooded with offers. Jack's team built 47 sensors directly on the live plant, and a 45-day deadline became a 6-month rebuild. In Tomás's case, a vendor churn model degraded for months because Dev and QA lived on the laptop of someone who had left. Among public cases, Julio M.'s Epic Sepsis Model is truly about ML: an AUC of 0.76–0.83 reported by the developer, 0.63 on another hospital's data. Ana Cristina's Google Health case in Thailand shows the same thing: lab images versus clinic photos.

A note on the public examples. Knight Capital (a trading software release), CrowdStrike (a faulty software update) and the 2020 Excel case (COVID test results lost in a spreadsheet) are good lessons about releasing untested changes. But none of them involved a machine-learning model, and several of you pointed that out yourselves, which was a good call. For this question, the strongest example is one where a model worked well in testing and then behaved differently on real data, like the Epic Sepsis Model or Google Health in Thailand above.

---

## Q3 recap · One threat, one control, one detector

Only 12 of you answered this one, which is a pity, because the answers were very good. The strongest followed the structure exactly. Each named one specific threat and one proportionate control. Each then walked back the lineage (prediction → model version → training run → data snapshot → log) and said *what you would see* at the end of it.

- **Marcos:** a claims handler closing fake claims as "no fraud". The log shows one handler closing 120 claims from five shops in two weeks.
- **Armen:** label poisoning at one merchant. Its fraud rate falls from 2% to 0 between two snapshots.
- **Julio M.:** customers opening empty tickets to earn a retention offer. Every value stays in range and validation passes, so only a rule on the *mean* catches it.
- **Ayushi:** a feed sending "2:30" read as 2.30, making every aircraft about 8% younger. The giveaway is that no decimal part is ever above .59.
- **Sigursteinn:** competitors booking and cancelling to inflate demand. The control is to train only on paid rentals.
- **Fernando:** model inversion on salary data. The control is to block queries on groups of fewer than 5–10 people.

Notice that most of these are not hackers. They are insiders, customers or a data migration (Edgar's complaint history lost in a migration, so customers look low-risk). The same audit trail catches all of them. A test for your own answer: does your detector say what you would actually *find* in the record? Writing "we would review the logs" is not enough, because it doesn't say what to look for. Marcos's answer does: in the log of claim closures, one handler closed 120 claims from the same five shops in two weeks. That is a pattern someone can search for and spot.

---

## Optional Theme A recap · Give María's model a memory

Three of you ran the MLflow lab, and the conclusion was right: send the simple logistic regression to QA, not the forest with a perfect 1.00 on the customers it studied. The gap between the studied and the unseen score is memorisation.

The most useful finding was Raissa's and Samah's. Changing *only the split seed* moved the test AUC by about 0.05 (0.715 → 0.666; 0.711 → 0.661). That is larger than María's "0.84 to 0.87 improvement", which may simply be a different test sample. The model didn't get worse or better: the test customers changed. This is why the pipeline fixes the seed and uses cross-validation. Samah also noticed that the models with the best precision barely flag anyone: they catch 18% of churners.

What MLflow didn't record, as you pointed out: who approved the model, which version is live, and the business cost of a missed churner. The registry (Session 3) and the rollout (Session 5) are where those answers live.

I would love to see more of you in the optional themes. They are not graded, and nobody loses marks for skipping them. But they are where the ideas from the sessions stop being something you have read and become something you have done. Raissa and Samah saw the seed effect for themselves, and no slide makes that point as well. This week there is a new hands-on lab on the campus, *From the registry to a container*. You take the production model out of the registry, pack it into a container on your own laptop and send it customers: the same steps as the live demo in Session 5. It takes about 30 minutes, needs no code, and every step tells you what you should see. If you have half an hour this week, it is the best way to understand what "deployed" really means.

---

## Optional Theme B recap · Skip QA to hit the launch date

Only Samah answered, and her answer is the one I hoped for. Don't refuse, and don't quietly comply. Put the untested areas and the risks in writing, get a named person to approve the risk formally, and agree a rollback. QA has done its job when it makes the risk visible and someone owns the decision.

One thing to add: offer a smaller launch. That could be one region, or a shadow mode where the model scores but does not act. Then the date and the test can both be kept. Session 5 turns this into the rollout strategies: shadow, canary, blue-green.

I would like to see more of you in these discussion themes. They are short (one paragraph is enough) and not graded, but they are the conversations you will actually have at work: a CEO with a date, a QA team with a risk, and you in the middle. Writing your answer down, and reading how a classmate would handle the same pressure, is the best practice you can get before it happens for real. Forum 3 continues the story with the rollback drill, from the poll in Session 5: if you have ten minutes, try it.

---

*A reminder for everyone: declare AI use (or no use) on every post, replies included. And the debate matters as much as the artefacts: this week 18 of you posted no reply, and good questions from Khem, Julio M. and Camila went unanswered. In Forum 3, reply to at least two classmates.*
