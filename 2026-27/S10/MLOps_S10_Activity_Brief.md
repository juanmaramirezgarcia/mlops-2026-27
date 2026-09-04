# Session 10 · Activity brief: diagnose a real failure case

**Slot:** minutes 58–86 (brief 58–61 · breakout rooms 61–76 · debrief 76–86)
**Format:** one case per room (rooms of 4–5, the project teams); every team read its one-page brief before class
**Output:** the root-cause template filled on one slide or whiteboard, plus one sentence; two rooms present; everyone posts theirs in Forum 5 (it is the basis of Q3)

---

## 1. The task, as read to the class (minute 58–61)

> Your team read one of the six failure briefs. Diagnose it with the template: five rows. **Symptom**: what was observed, by whom, when; facts only, from the brief. **Stage where it originated**: where in the lifecycle the problem was created, which is usually earlier than where it was noticed. **Missing control**: the specific check, gate, metric or rule that did not exist or was not applied; use the course vocabulary (a data validation step, a model-validation gate, a canary, a drift metric with a threshold and an owner, a groundedness guardrail, a bias audit, a human approval before an irreversible action…). **Accountable persona**: who should have owned that control; a person with a role, not "the algorithm" and not "the company". **Corrective roadmap**: one action per module, ten words each: foundations · pipelines and deployment · monitoring · governance; each action must contain a metric, a gate, a person or a document.
>
> Then one sentence: *the single control that would most likely have prevented or contained it, and who should have owned it.* If you disagree inside the room, keep both candidates and say why.
>
> Also map your case onto one or two of the six patterns from slide 21. Fifteen minutes. Spokesperson: two minutes.

## 2. Room allocation (adjust to the real rooms on the day)

| Room | Case | Brief | Kind |
|---|---|---|---|
| 1 | Zillow Offers (2018–2021) | `failure_briefs/01_zillow_offers.md` | Classical ML · forecasting |
| 2 | Amazon recruiting tool (2014–2017) | `failure_briefs/02_amazon_recruiting.md` | Classical ML · classification, bias |
| 3 | Air Canada chatbot (2022–2024) | `failure_briefs/03_air_canada_chatbot.md` | Generative AI · assistant |
| 4 | Dutch childcare-benefits algorithm (2013–2021) | `failure_briefs/04_dutch_childcare_benefits.md` | Risk scoring · public sector |
| 5 | Epic sepsis model (2021) | `failure_briefs/05_epic_sepsis_model.md` | Classical ML · clinical prediction |
| 6 | Knight Capital (2012) | `failure_briefs/06_knight_capital.md` | Deployment failure (not ML) |

With five rooms, drop Knight Capital (or give it to the strongest room as a second case). With more than six rooms, two rooms take Air Canada (the only GenAI case) and compare in the debrief. Post the allocation on campus by Wednesday 28 October, with the briefs.

## 3. The root-cause template (post with the briefs)

**Case:** ______________________  **Room:** ____  **Patterns (slide 21):** ____ and ____

| Row | Your answer |
|---|---|
| **Symptom** — what was observed, by whom, when (facts only, from the brief) | |
| **Stage where it originated** — the lifecycle stage where the problem was created (usually earlier than where it was noticed) | |
| **Missing control** — the check, gate, metric or rule that did not exist or was not applied (course vocabulary) | |
| **Accountable persona** — who should have owned that control (a role: product owner, data scientist, ML engineer, IT, Risk & Compliance, content owner, the business sponsor) | |
| **Corrective roadmap** — one action per module, ten words each, with a metric, a gate, a person or a document in each | M1 Foundations: <br> M2 Pipelines & deployment: <br> M3 Monitoring: <br> M4 Governance: |

**One sentence:** the single control that would most likely have prevented or contained it, and who should have owned it: ______________________________________________

### Worked example (NorthRetail, Session 1)

| Row | Answer |
|---|---|
| Symptom | Forecast error doubled over four months; noticed by store managers overriding orders; nobody looked at the dashboard |
| Stage where it originated | Data ingestion: a supplier feed changed format in February; the features went silently empty |
| Missing control | Data validation at ingestion (S3); a freshness metric "share of features updated this week" with a threshold and an owner (S7) |
| Accountable persona | ML engineer for the check; product owner for reading the number monthly |
| Corrective roadmap | M1: model card with a retrain trigger · M2: validation step that fails the pipeline · M3: freshness and KPI alerts routed to a person · M4: monthly review signed by the owner |
| One sentence | A data-validation step that fails the pipeline when a feature goes empty, owned by the ML engineer, with the product owner reading the freshness tile monthly |

## 4. Running the rooms (minute 61–76)

Visit each room once. The three ways rooms go wrong, and the question that fixes each:

- **Narrating instead of diagnosing.** The room retells the story. Ask: "which row are you on?" and point at the template.
- **"Monitoring" or "governance" as the missing control.** Ask: "which metric, with which threshold, read by whom?" or "which document, signed by whom, before what?".
- **"The algorithm" or "the company" as the persona.** Ask: "who, with what job title, could have said no, and when?".

Warn at 12 minutes; ask for the one sentence to be written down at 13.

## 5. Debrief (minute 76–86)

**76–82 · Two presentations.** One classical case (Zillow or Epic present well: the truth arrived late; the vendor's claim was not checked) and the GenAI case (Air Canada). Two minutes each, then one question from the class each. The other rooms post their one sentence in chat; read four aloud, naming the room.

**82–86 · Synthesis.** Reveal slide 26 (the table of missing controls and owners) and walk it quickly, one line per case. Then the course-in-one-picture slide (27): each case failed on a question one module answers.

### Model answers per case (professor only)

| Case | Stage where it originated | The missing control (strong answers) | Persona | Patterns |
|---|---|---|---|---|
| Zillow Offers | Model deployment / decision design: the forecast became an irreversible purchase at scale with no gate | A human approval and exposure limit above a threshold (offers above X, or aggregate inventory above Y); forecast-vs-resale monitoring by market routed to a person; a stop rule on forecast uncertainty | Product owner (the business sponsor of Offers) | 1 (no human gate), 4 (truth arrives late; concept drift in the market) |
| Amazon recruiting | Data collection / training: ten years of mostly male hires as the target | A bias audit of the training data and of outcomes by gender before any use; documented prohibition of proxy features and terms; a decision on whether the use case is appropriate (it was abandoned) | Data scientist + Risk & Compliance / HR as owner | 2 (data encoded the past) |
| Air Canada chatbot | Generation without grounding; no ownership of the output | A groundedness guardrail against the policy pages it cites, with a refusal-and-handoff path for policy questions; an owner who signs for the assistant's answers; hallucination monitoring | Product owner + Legal (the company is liable) | 6 (generation without grounding or accountability) |
| Dutch childcare benefits | Feature selection and decision design: nationality as a risk indicator; a score treated as proof; no contestability | A feature review against the law; an explanation per decision; a human review before any enforcement action; contestability | Risk & Compliance; ultimately the political owner | 2 and 1 (no human gate on enforcement); the EU AI Act high-risk case |
| Epic sepsis model | Model validation: a vendor's performance claim deployed without local validation | External validation on the hospital's own data as a go-live gate; calibration and threshold per site; alert-burden monitoring (alerts per true case); measurement of what the model adds over clinicians | Clinical product owner + ML engineer | 3 (claim never validated locally), 4 (truth existed but was never joined) |
| Knight Capital | Deployment: manual, unverified across servers; dead code never removed; alerts that were not alerts | Automated deployment with verification that all servers match; automated rollback; a kill switch; alerts that page a person; removing dead code | IT / ML engineer (release manager) | 5 (deployment without verification or rollback) |

Reward rooms that: separate where it was noticed from where it originated; name a metric with a threshold and an owner; say who could have said no; note that the organisational failure (nobody owned the control) matters as much as the technical one. Correct rooms that: propose "retrain" for a problem that was not the model (Knight, Air Canada); propose "more monitoring" without a metric; put "the AI" as the persona.

Close with: *"In every case somebody could have said no, and the system was not built to let them."*

## 6. Checklist

- [ ] Briefs and allocation posted on campus by Wednesday 28 October; each team confirmed its case
- [ ] Template (section 3) posted with the briefs
- [ ] Breakout rooms pre-assigned to project teams; timer set for 15 minutes
- [ ] Slides 26 (missing controls) and 27 (the course in one picture) ready to reveal
- [ ] Two rooms pre-warned that they will present (one classical, Air Canada)
