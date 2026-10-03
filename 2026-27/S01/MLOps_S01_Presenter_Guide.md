# Session 1 · Presenter's guide — how to explain each slide to a non-technical cohort

**MLOps elective · Master in Business Analytics and Data Science · MBDS-PT2026F · Session 1 (Live, 90 minutes)**

A companion to the deck's speaker notes, written for *delivery*: for each slide you get the **point** (why it's there), **say it like this** (plain-language framing and an analogy that works for students with no coding background), the **line to land**, and a **question to ask the room**. Timings match the notes in the deck.

The shape of the session: opening hook (1–4) → how we'll work together (5–9) → DevOps to MLOps (10–17) → the six personas (18–21) → break (22) → lifecycle & performance (23–25) → the activity (26–28) → close (29–31).

Two threads to keep pulling all session: **a model is not static, it rots** (slide 12), and **most failures are about people and process, not maths** (slides 13, 25, 28). If they leave remembering only those two, Session 1 worked.

---

## Opening (1–4)

### Slide 1 — Title / welcome
**Point:** atmosphere, not content. **Say it like this:** have the slide up five minutes early, camera on, and greet people by name as they arrive — for a part-time cohort giving up a Saturday, the first thing you teach is that this room is warm and worth showing up to. **Land:** "We start at [time] sharp — glad you're here." **Ask:** —

### Slide 2 — What you'll be able to do (the three outcomes)
**Point:** set the target for the week. **Say it like this:** read the three outcomes aloud, then tell them these three *are* this week's forum questions. **Land:** "If you can do these three things by next Saturday, Forum 1 is easy." **Ask:** — (keep momentum).

### Slide 3 — Hidden technical debt (the Google picture)
**Point:** the single most important image in the course — the model is the small part; the project is everything around it. **Say it like this:** point at the little "ML code" box in the middle, then sweep across all the big boxes around it (data collection, serving, monitoring, configuration). Do **not** use the "boxes not the box" wordplay out loud — it confuses a room. Say it plainly: "This little box is the model the data scientist is proud of. All these big boxes — getting data, checking it, serving it, watching it — that's where the work is. The model is maybe 5% of a real system; this course is about the other 95%." **Land:** "The clever model is the little box. This course is all the boxes around it." **Ask:** "Where do you think a data team's time actually goes?" — take two answers, then reveal it's the surrounding boxes.

### Slide 4 — Why this matters (the three numbers)
**Point:** the hook — most models never deliver value, and rarely because of the maths. **Say it like this:** 28% of AI use cases fully succeed (Gartner, late 2025), 95% of GenAI pilots show no measurable P&L impact (MIT, 2025), 87% of data-science projects never reached production (the 2019 baseline). Don't defend the exact numbers — "different surveys measure different things." The point is the seven-year pattern. **Land:** "The problem is almost never the algorithm. It's everything we're here to learn." **Ask:** "Why would a technically good model still fail to deliver value?" — their answers preview the whole syllabus.

## How we'll work together (5–9)

### Slide 5 — Divider: how we'll work
**Point:** gear-change; answer the "how am I assessed / how much work is this" anxiety before the content. **Say it like this:** "Before the content, five minutes on how we work, because the format is a bit unusual." **Land:** — **Ask:** —

### Slide 6 — The rhythm (timeline)
**Point:** predictability lowers anxiety for a working cohort. **Say it like this:** walk it left to right — every Saturday we meet live and I introduce the new ideas; during the week a forum recaps and asks three questions; twice in the term a self-paced video with a quiz. "Nothing here is a surprise; the shape repeats every week." **Land:** "Same rhythm every week — live, then forum, and two videos along the way." **Ask:** —

### Slide 7 — How you're graded
**Point:** the assessment weights, and two things students always re-ask later. **Say it like this:** four cards — 35% final exam, 35% group project, 15% quizzes, 15% participation. Repeat: the exam has a **minimum of 3.5/10** (below it, the course is failed regardless of average), and they may bring **one handwritten A4 sheet** — which is exactly what the "three things to remember" slide at the end of each session is for. **Land:** "Build your A4 sheet all term from the closing slides — that's what they're for." **Ask:** "Any questions on the weights before we move on?"

### Slide 8 — How to participate well
**Point:** set forum etiquette early, with humour. **Say it like this:** name the three characters to avoid — the **Repeater** (restates what's been said), the **Rambler** (long, low-value tangents), the **Distracted** (drops out, then re-asks an answered question). Everyone recognises all three; naming them sets the tone without singling anyone out. **Land:** "Great participation isn't the most words — it's moving the conversation forward." **Ask:** —

### Slide 9 — The lifecycle map (first appearance)
**Point:** plant the map you return to at every divider — don't explain the nine steps yet. **Say it like this:** "This is our map for the whole course. Every time I put up a divider today, it comes back and I point to where we are." **Land:** "This is our map — you'll see it a lot." **Ask:** —

## DevOps → MLOps: the conceptual spine (10–17)

### Slide 10 — Divider: from DevOps to MLOps *(minute 16)*
**Point:** reassure — software engineering solved a version of this before. **Say it like this:** "Software hit a version of this problem twenty years ago and solved it, with something called DevOps. MLOps borrows from it, so let's start there." **Land:** "We're not the first people to struggle with getting good work into production." **Ask:** —

### Slide 11 — Before MLOps there was DevOps
**Point:** DevOps is a culture fix — stop throwing work over a wall. **Say it like this:** once, developers *wrote* software and a separate operations team *ran* it; developers threw code "over the wall" and walked away, and when it broke each team blamed the other. DevOps tore down the wall — build and run are shared, with automation in between. The "over the wall" image does all the work. **Land:** "DevOps is a culture fix: share responsibility for building *and* running." **Ask:** "Has anyone lived the 'it's their problem, not mine' situation at work?" — hands go up; now it's theirs.

### Slide 12 — The one thing that makes ML different (models are not static) *(the key slide — slow down)*
**Point:** ordinary software is fixed; a model rots over time even untouched, because the world moves. **Say it like this:** a VAT calculator gives the same answer in ten years. A model learned from *past* data, so as the world changes it quietly gets *worse* although nobody edited it. Use the on-slide examples (behaviour shifts, prices change, a shock like a pandemic). **Land:** "Normal software rots only if you change it. A model rots if you *don't*." **Ask:** "Why would a model that was 90% accurate at launch be worse a year later, with no code changed?" — lead them to 'the world changed'.

### Slide 13 — Why models don't reach production (six reasons)
**Point:** every reason is organisational, not mathematical. **Say it like this:** read the six as a story — one model, built by one data scientist, on their laptop, that nobody can reproduce, with no owner once it ships, and no one watching it. **Land:** "Not one of these is 'the maths was wrong.' They're all people, ownership and process — which is what MLOps fixes." **Ask:** "Which of these six is the most common?" (usually 'no clear owner' — sets up the personas block).

### Slide 14 — So what is MLOps? (the definition)
**Point:** the definition matters less than three verbs. **Say it like this:** give the formal definition once, slowly, then the plain paraphrase — MLOps is how you **build, ship, and keep running** ML systems reliably, by combining machine learning with the DevOps discipline and solid data handling. **Land:** "Build it, ship it, keep it healthy — reliably, again and again. That's the job." **Ask:** —

### Slide 15 — Training vs operationalising a model *(answers Forum Q3)*
**Point:** the classic mistake — celebrating a good score and thinking you're done. **Say it like this:** "This slide is the answer to Forum question 3." **Training** delivers a *model* (a file and a score, made once); **operationalising** delivers a *service* (answers real requests every day, owned and monitored). **Land:** "Training gives you a file. Operationalising gives you a service someone is responsible for. The gap between them is this whole course." **Ask:** "If a team says '95% accurate, we're finished' — what have they forgotten?"

### Slide 16 — Version control, without jargon
**Point:** the habit everything later rests on (reproducibility, CI/CD, audit). **Say it like this:** it's like *track changes* / *version history* in a shared document — every change recorded, with who and when, and you can always go back. A repository is that idea for a whole project. **Land:** "It's version history for the whole project — nothing is silently lost, and you can always rewind." **Ask:** "Who's ever wished they could get back last Tuesday's version of a document?" — that instinct *is* version control.

### Slide 17 — What a repository looks like (fixes the demo)
**Point:** freeze the 4-minute demo into three capabilities. **Say it like this:** point at the **history** (a list of changes, each with author, date, and a short message), the ability to **see exactly what changed**, and the ability to **roll back** to a known-good version. No commands — just those three. **Land:** "History, what-changed, and rewind. That's why every serious team works this way." **Ask:** "How would this have helped the 'it broke and no one knows why' story?"

## The six personas *(minute 35 — core of Forum Q1 & Q2)* (18–21)

### Slide 18 — Divider: who does what
**Point:** shift from *what* MLOps is to *who* does it — where a non-technical cohort feels most at home. **Say it like this:** "Everything so far was about the work. Now: who does it? This block is where Forum questions 1 and 2 live." **Land:** — **Ask:** —

### Slide 19 — Six personas, six questions *(minute 35–39)*
**Point:** each role is defined by the *question it asks about the model* — a memorable hook. **Say it like this:** walk the six by their question — **Product owner:** "Is it worth it, and useful?" (sets the goal and what 'good enough' means); **Data scientist:** "Is it accurate?" (builds and evaluates it); **Data engineer:** "Is the data available, correct, on time?" (builds the pipelines the model depends on); **ML engineer:** "Does it run reliably in production?" (packages, deploys, automates monitoring — the bridge between data science and IT); **IT/DevOps:** "Does the infrastructure hold and stay secure?"; **Risk & Compliance:** "Can we prove it's fair, explainable and allowed?" Stress that in a small company one person wears three hats — but every question still needs answering. **Land:** "Six people, or one person with six hats — but all six questions must be answered." **Ask:** "Which of these is closest to your job today?" (also the break question on slide 22).

### Slide 20 — The nine hand-overs *(minute 39–43)*
**Point:** most failures happen *between* roles, not inside them. **Say it like this:** walk it as the story of a recommendation model — (1) business & experts give requirements, (2) data engineer makes the data available, (3) data scientist builds the model, (4) product owner + DS decide how it'll be used, (5) DS + ML engineer test it in a sandbox, (6) ML engineer deploys, (7) app developer integrates it, (8) IT runs and scales it, (9) everyone monitors and feeds back. Then point at hand-overs 5–6: that gap between data science and engineering is where it usually breaks — "that's *why* the ML engineer role was invented." **Land:** "Work rarely fails inside a role. It fails in the gaps between them — especially between data science and engineering." **Ask:** "Which hand-over do you think is most likely to fail?" — steer to 5–6.

### Slide 21 — The RACI map (a tool for the forum) *(minute 43–46)*
**Point:** give them the exact tool Forum Q2 asks for. **Say it like this:** four letters — **R**esponsible does the work; **A**ccountable owns the outcome and signs off (**only one A per row**); **C**onsulted gives input *before*; **I**nformed is told *after*. Rows are lifecycle stages, columns are personas. Walk the example row for "Model deployment": ML engineer Responsible, product owner Accountable, IT and DS Consulted, Risk & Compliance Informed. Stress this is *an* example, not *the* answer — the forum is about arguing your own allocation. **Land:** "One person accountable per stage — that single rule prevents a lot of the failures we just saw." **Ask:** "Would you move any letter in this row?" (there's no single right answer — that's the forum).

### Slide 22 — Break, 5 minutes *(minute 46)*
**Point:** rest, and read the room. **Say it like this:** keep the question on screen — "which of the six personas is closest to your current or future job?" — chat answers give you a read of the cohort. Use the break to check breakout rooms are set (teams of 4–5, ideally the future project teams). **Land:** "Back at [time]. Drop your persona in the chat while you wait." **Ask:** (the on-slide question).

## Lifecycle & performance *(minute 51 — short block, protect the activity)* (23–25)

### Slide 23 — Divider: the end-to-end lifecycle
**Point:** signal a short 7-minute block so the activity keeps its time. **Say it like this:** "Now the whole map, plus one idea that decides most projects before a line of code: what 'performance' actually means." **Land:** — **Ask:** —

### Slide 24 — The lifecycle in plain words *(minute 51–54)*
**Point:** two takeaways only — it's a **loop**, and the first three steps are about **data, not models**. **Say it like this:** one line per step, don't go deep (each gets its own session): get and version the data → check it → shape it the same way every time → train → tune → analyse by segment → validate against what's live → deploy → collect feedback, which loops back to the data. Then: "Notice the first three steps are all *data*. That's where most of the time — and most of the failures — live. That's Session 3." **Land:** "It's a loop, not a line — and it starts and ends with data, not the model." **Ask:** —

### Slide 25 — "Performance" means four things *(minute 54–58)*
**Point:** most failures are decided *here*, before training. **Say it like this:** four kinds, using the recommendation example — **Business** (the product metric you want to move, e.g. click-through, and a guardrail that mustn't fall, e.g. session length — the only metrics that matter in the end); **Model** (accuracy/AUC/F1/RMSE — but *sufficient* for the goal, not maximal; a product needing a perfect model will fail); **Data** (will tomorrow's data look like training data? how often must we retrain, at what cost?); **System** (how fast is fast enough, cost per prediction, never confuse dev with production). Close on the callout: most failures happen when the product metric and the model metric point in different directions, or an accurate model nobody acts on. **Land:** "The product metric is the only one that matters in the end — and most projects are lost right here, before any training." **Ask:** "Can you name a model that's accurate but useless because nobody acts on it?"

## The activity *(minute 58–86)* (26–28)

### Slide 26 — Activity brief *(brief at 58–60)*
**Point:** set up the diagnosis clearly before sending them to rooms. **Say it like this:** every room gets the same one-page case (NorthRetail demand forecast). Four things went wrong; for each, fill a template row — which lifecycle stage it came from, which persona should have caught it, and the one control that would have prevented it (bonus: what IT's dashboard should have shown). Rooms of 4–5 (their future project teams), one slide/whiteboard, a spokesperson with 2 minutes. Tell them to use today's vocabulary: the nine steps and the six personas. **Land:** "Use today's words — nine steps, six personas — to diagnose it like a team of consultants." **Ask:** —

### Slide 27 — The case, facts only *(read at 60–61)*
**Point:** read the facts aloud without diagnosing — the diagnosis is their job. **Say it like this:** read it once, plainly. The four problems are deliberately different kinds: a data schema change (data validation would catch it), a promotion-calendar change (a concept change — needs monitoring and retraining), loss of ownership (persona/governance), and a dashboard watching the wrong thing (system vs model performance). Then send them to rooms. **Land:** "Here are the facts. Don't diagnose yet — that's the room's job." **Ask:** —

### Slide 28 — Debrief *(76–86)*
**Point:** land that every fix they proposed is a future session. **Say it like this:** three rooms present (2 min each), then synthesise: empty features after the code change → data validation → data engineer + ML engineer → a schema check that stops the pipeline (Session 3); promotions moved weekly → monitoring/feedback → product owner informs, ML engineer detects → drift + performance monitoring with a retraining trigger; no owner → governance → product owner accountable, Risk & Compliance informed → a model registry with a named owner; green dashboard → system vs model performance → monitor prediction quality, not just uptime. Correct two misconceptions: "the data scientist should've caught everything" (she was gone by April, and most failures aren't modelling failures) and "more accuracy would've prevented this" (92% was fine for a world that stopped existing in February). **Land:** "Everything you just proposed is a session of this course." — point at the map. **Ask:** —

## Close (29–31)

### Slide 29 — Three things to remember *(cheat-sheet material)*
**Point:** the exam A4-sheet lines — read slowly, tell them to write these down now. **Say it like this:** (1) *A model in production is a running process, not a file* — training ends with a file and a score; operationalising means it answers real requests daily and someone is accountable. (2) *The world changes under the model* — unlike ordinary software, models decay; retraining is *when*, not *if*. (3) *Six personas, nine hand-overs* — most failures happen between roles; decide who is Responsible and Accountable before you start. **Land:** "Three lines for your A4 sheet — write them now." **Ask:** —

### Slide 30 — Your forum this week
**Point:** connect the session to the week's work. **Say it like this:** read the three questions (verbatim from the syllabus) and point to where each was covered today — Q1 = the "why MLOps" and persona slides; Q2 = the RACI slide and the template on campus; Q3 = the training-vs-operationalising slide. Remind them of the rhythm: post early, reply to two classmates, synthesis on Friday. **Land:** "Everything you need for these three is in today's slides." **Ask:** —

### Slide 31 — Before Session 3
**Point:** set the reading and the one thing to look at. **Say it like this:** read Treveil et al., *Introducing MLOps*, chapters 1–3 (short, non-technical); optional Huyen chapter 1. The "look at one thing": open the exploratory notebook on campus (a PDF, nothing to run) and note what looks messy — Session 3 starts from their list. Preview Session 3: turning notebooks into pipelines, why companies separate Dev/QA/Prod, and how a model can be attacked. Thank them and stop on time. **Land:** "Bring three things that looked messy in that notebook — that's where Session 3 begins." **Ask:** —

---

### Two delivery reminders
- **Protect the activity's time.** The lifecycle/performance block (23–25) is deliberately short (7 minutes). If you're running late, trim there, not the breakout.
- **Keep pulling the two threads.** "A model rots if you don't touch it" (12) and "most failures are people and process, not maths" (13, 25, 28). The activity and the three-things slide both pay them off.
