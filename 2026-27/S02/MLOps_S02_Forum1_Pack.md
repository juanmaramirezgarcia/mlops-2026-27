# Forum 1 Pack · Session 2 · 3–9 October 2026

**Recap of Session 1 — Foundations, Personas & the MLOps Lifecycle**
*Everything you need to open, run and close the forum: the opening post, the three extra discussion themes, the mid-week posts, the RACI template, and model-answer notes for grading.*

---

## 1. Coverage check

| Forum question | Where it was taught in Session 1 | Gap? |
|---|---|---|
| Q1 · Three reasons a company's models never reach production, and the persona to address each | Slides 4 (statistics), 12–13 (models are not static; why it is hard), 19 (six personas), 25 (four kinds of performance, where projects die) | None |
| Q2 · RACI-style responsibility map for a recommendation-model project | Slides 19–21 (personas, hand-overs, RACI explained with an example row) plus the template below | None, provided the template is posted with the opening message |
| Q3 · Training vs operationalising a model, with a business consequence | Slide 15 and the NorthRetail case (slides 27–28) | None |

---

## 2. Opening post (publish Saturday 3 October, after the live session)

> **Forum 1 · Recap of Session 1 · open until Friday 9 October, 23:59**
>
> Welcome to the first forum. The forums are where the concepts from the live session become yours: you use them on a case, and you argue with each other about them. Nothing new is introduced here; if a word in a question is unfamiliar, it is in today's slides.
>
> **Three questions, three artefacts**
>
> 1. **Why models never reach production.** Choose a real or hypothetical company and explain, in a short post (200–300 words), three reasons its ML models might never reach production. For each reason, say which persona is best positioned to address it, and why that persona and not another.
> 2. **A responsibility map.** Draft a one-page RACI-style map for a fictional recommendation-model project (an online retailer, a streaming service, a bank's "next best offer": your choice). Use the template attached. Rows are the lifecycle stages; columns are Data Scientist, ML Engineer, IT/DevOps, Product Owner and Risk/Compliance. Only one *A* per row. Add three lines explaining the two allocations you found hardest.
> 3. **Training vs operationalising.** In your own words (no quotes from the slides), define the difference between "training a model" and "operationalising a model", and give one concrete business consequence of confusing the two. A real example from your own experience is worth more than an invented one.
>
> **How the week works.** Post your answers by Tuesday if you can; the best debates need time. Reply to at least two classmates with a challenge, an extension or a request for evidence: "I agree" is not a reply. I will post a nudge on Tuesday, a twist on Thursday and a synthesis on Friday.
>
> **What is assessed.** Quality and insight, not volume: a post that connects a concept to a real example and a constraint beats three posts that restate the slides. Avoid being the Repeater, the Rambler or the Distracted.
>
> **AI tools.** Encouraged for drafting and structuring; declare them with the sentence from the syllabus at the end of your post, or state that none were used.
>
> **A theme to react to while you write:** *"The three-model company."* Is MLOps proportionate for an organisation with only three models in production? You voted on this in the chat today and I refused to settle it. Where is the threshold at which it becomes necessary, and what is the cheapest possible version of MLOps for a company below it?

---

## 3. Extra discussion themes

Post these as separate threads during the week. They give students who finish the three questions early something to argue about, and they generate the replies that participation is graded on.

**Theme A · The three-model company** (posted Saturday, in the opening message)
This was polled in chat during the live session (AGREE/DISAGREE, one line each) and deliberately left unresolved; quote two or three of the chat answers in the thread to start it. Is MLOps proportionate for a company with three models? Push for a threshold and for a definition of the *minimum viable* MLOps: a named owner, a versioned artefact, one business metric checked monthly. The insight to reward: the cost of MLOps scales with the cost of being wrong, not with the number of models.

**Theme B · Two job postings, which persona?** (posted Tuesday)
Attach two real, anonymised job postings: one titled "Machine Learning Engineer", one titled "Data Scientist". Ask: which persona from the session is each one really describing? What responsibility is missing from both? Typical finding: both postings describe model building; neither mentions monitoring, ownership after deployment or compliance. Reward students who notice that Risk & Compliance almost never appears in job postings and ask who does that work.

**Theme C · A model you met this week** (posted Thursday, as the twist)
Ask every student to name one product or service they used this week that has a model behind it (a recommendation, a fraud check, a price, a route) and to describe what "degrading" would look like from the customer's side. Then the twist: "Now you are the product owner. Which single number would you check every Monday morning?" This rehearses business performance and guardrail metrics.

---

## 4. Mid-week posts

**Tuesday nudge.** Quote two contrasting student answers to Q1 (for example one that blames the data scientist for everything and one that blames IT) and ask the group: who is right, and what would the persona framework say? Post Theme B.

**Thursday twist.** Post Theme C, and add a twist to Q2: "Your company has just been told that the recommendation model falls under a regulation that requires an explanation for every recommendation shown to a customer. Which letters in your RACI map change?" Expected: Risk & Compliance moves from *I* to *C* or *A* at model validation and deployment; the data scientist gains an *R* for explainability.

**Friday synthesis.** A 300-word post that names the three or four best contributions (with names), states the most common misconception, and bridges to Session 3. Suggested skeleton:

> *What you said.* [Three insights, each attributed.]
> *The misconception of the week.* Most answers to Q3 described operationalising as "putting the model on a server". A server is necessary, not sufficient: operationalising means the model answers real requests every day with today's data, and someone is accountable when it is wrong.
> *What comes next.* On Saturday we take the model apart: the exploratory notebook on campus becomes a pipeline, we see why Dev, QA and Prod are separate, and we look at how a model can be attacked. Bring your list of "three messy things" from the notebook.

Reuse this synthesis as the recap slide at the start of Session 3.

---

## 5. RACI template (attach to the opening post)

**Project:** ____________________ (recommendation model for ____________________)

R = Responsible (does the work) · A = Accountable (owns the outcome, signs off; one per row) · C = Consulted (input before) · I = Informed (told after)

| Lifecycle stage | Product Owner | Data Scientist | ML Engineer | IT / DevOps | Risk / Compliance |
|---|---|---|---|---|---|
| Define goal, product metric and guardrails | | | | | |
| Data ingestion and versioning | | | | | |
| Data validation | | | | | |
| Data pre-processing and feature engineering | | | | | |
| Model training and tuning | | | | | |
| Model analysis and validation (incl. fairness, explainability) | | | | | |
| Model deployment | | | | | |
| Monitoring and alerting | | | | | |
| Retraining decision | | | | | |
| Decommissioning | | | | | |

**The two allocations I found hardest, and why:**

1.
2.

*(Data Engineer is not a column because the syllabus question lists five roles; if your project has one, add a column and say so.)*

---

## 6. Model-answer notes (for grading)

### Q1 · Three reasons, three personas

A strong answer gives reasons from **different layers** and matches each to the persona *in a position to act*, with a justification. Reward variety across these families:

| Reason family | Example | Best-positioned persona |
|---|---|---|
| Wrong target | Model metric and product metric misaligned; accurate model nobody acts on | Product Owner |
| Data | Sources not available in production; training data not representative; features that cannot be reproduced live | Data Engineer (or Data Scientist where no DE exists) |
| Engineering gap | Notebook cannot be turned into a service; environment mismatch; no versioning | ML Engineer |
| Infrastructure | No capacity, no scaling plan, no security review | IT / DevOps |
| Trust and compliance | Cannot explain decisions; bias risk; regulation blocks deployment | Risk & Compliance |
| Ownership | Nobody accountable after hand-over; the author leaves | Product Owner (accountable), with ML Engineer responsible |

Weak answers: three reasons from the same family (for example three data problems), or "the data scientist" for all three.

### Q2 · RACI map

There is no single correct map; grade the **reasoning**. Look for: exactly one *A* per row; the Product Owner accountable for goal definition and for deployment (a business decision); the ML Engineer responsible for deployment and monitoring; Risk & Compliance at least *C* at validation and deployment; the Data Scientist not *A* for deployment (the most common error: it confuses building with operating). The three lines on "hardest allocations" are where insight shows; typical honest answers are "who is accountable for retraining?" and "is IT consulted or responsible for deployment?".

### Q3 · Training vs operationalising

A strong answer contains the three elements from slide 15: training ends with a file and a score on historical data; operationalising means answering real requests every day with today's data, integrated into an application, with a named accountable owner; and a **specific** consequence with a cost (write-offs, lost customers, a regulatory finding, a project declared successful and quietly abandoned). Reward answers that use a real example from the student's own experience. Weak answers restate the slide or give "the model will be wrong" without a mechanism.

### Participation rubric (from the syllabus), applied to this forum

| Level | What it looks like this week |
|---|---|
| Excellent | Three complete artefacts with a real example; at least two replies that change someone's mind or add evidence; contributes to a theme thread |
| Good | Three complete artefacts; two relevant replies |
| Satisfactory | Artefacts complete but generic; replies are agreement only |
| Insufficient | Missing artefacts, off-topic, or posted on Friday night with no interaction |

---

## 7. Checklist before opening

- [ ] Opening post published with the three questions and Theme A
- [ ] RACI template attached (this file, section 5, or a separate sheet)
- [ ] Session 1 slides posted on campus
- [ ] NorthRetail case (activity brief) posted, since Q3 answers may refer to it
- [ ] Two anonymised job postings ready for Tuesday (Theme B)
- [ ] Exploratory notebook (PDF) for Session 3 posted by Wednesday, so students can do the "look at one thing" preparation
