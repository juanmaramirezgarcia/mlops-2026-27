# Forum 5 Pack · Session 11 · 31 October–6 November 2026 (the capstone)

**Recap of Session 10 — LLMOps & Enterprise Scenario Diagnostics**
*Coverage check, the opening post, extra themes, mid-week posts, the two templates, and model-answer notes. Runs in parallel with Video 2 (Session 12, AI Governance).*

---

## 1. Coverage check

| Forum question | Where it was taught in Session 10 | Gap? |
|---|---|---|
| Q1 · Operational architecture of a RAG-based internal assistant (retrieval, prompt management, evaluation, guardrails, monitoring) with one cost or latency trade-off | Slide 9 (RAG anatomy), slide 10 (the architecture built with the class), slides 11–13 (evaluation and the demo, with the 40% cost figure), slide 15 (guardrails and their latency), slide 16 (the cost arithmetic) | None; the students drew nothing themselves in class, so Q1 is where they draw it |
| Q2 · Two concrete differences between operating an LLM and a classical model | Slide 5 (five things that change), slide 6 (two lifecycles side by side, the four-row table) | None |
| Q3 · Corrective MLOps roadmap for one failure case across the four modules | Slides 21–23 (patterns, template, cases), the breakout, slide 26 (missing controls), slide 27 (the course in one picture); Video 2 for the governance row | None; tell students to watch Video 2 before writing the governance row |

---

## 2. Assets to post with the opening message

- The architecture slide (10) as an image, so students draw their own version rather than copy it (post it Wednesday, after most Q1 answers are in; see mid-week posts).
- The root-cause template and the six briefs (already on campus since 28 October).
- The demo scorecard (`eval_summary.png`) and `eval_results.html`, so Q1's trade-off sentence can use real numbers.
- The link to Video 2 and the knowledge-check deadline (Friday 6 November, 23:59).
- The group-project deliverable templates and the defence date (as posted).

---

## 3. Opening post (publish Saturday 31 October, after the live session)

> **Forum 5 · Recap of Session 10 · the capstone · open until Friday 6 November, 23:59**
>
> Last forum. Today the asset was a model that writes, and then six real systems that failed. This week you put the course together: one architecture, two differences, one roadmap.
>
> **Three questions, three artefacts**
>
> 1. **An architecture.** Design the operational architecture for a RAG-based internal assistant (the TelcoNova HR assistant, or one from your own company). Show the components: **retrieval, prompt management, evaluation, guardrails, monitoring**, and the log that ties them together. Draw it (a photo of paper is fine). Then note **one cost or latency trade-off** with a number: the demo gave you one (v2: +40% per question for 11/12 instead of 6/12), the cost slide gave you others.
> 2. **Two differences.** Compare classical MLOps and LLMOps: **two concrete ways** in which operating an LLM in production differs from operating a traditional model, each with its operational consequence (what you version, test, monitor or sign differently). Two paragraphs; an example each.
> 3. **Capstone synthesis.** Take **one failure case** from Session 10 (your team's, or another) and outline a **corrective MLOps roadmap across the four modules**: foundations · pipelines and deployment · monitoring · governance. One action per module, each with a metric, a gate, a person or a document in it. Start from your room's template; improve it. Watch Video 2 before writing the governance row.
>
> **How the week works.** Post by Tuesday if you can. Reply to at least two classmates: challenge a trade-off, add a component they missed, or propose a stronger control for their case. Nudge Tuesday, twist Thursday, synthesis Friday. Do the Video 2 knowledge check by Friday; it counts.
>
> **AI tools.** Encouraged for structuring and drawing; declare them with the syllabus sentence, or state that none were used. Not in the knowledge check.
>
> **A theme to react to while you write:** *"Promote v2 to production today?"* You voted A, B or C in class. What would you need to see, and who would have to sign, before the challenger becomes production?

---

## 4. Extra discussion themes

**Theme A · Can a model be trusted to grade another model?** (posted Saturday)
LLM-as-a-judge scales evaluation; it also has biases (it prefers long answers, it can be fooled by confident tone, it shares blind spots with the model it judges). Ask for **one situation where a judge works and one where it fails**. Reward answers that give the operational fix: a human sample to calibrate the judge, a rubric with examples, a different model as judge, and hard rules (PII, format) that need no judge at all.

**Theme B · The guardrail budget** (posted Tuesday)
Every guardrail adds latency and cost (slide 15). *If you could afford only two guardrails for the HR assistant, which two, and why?* Then the second half: *who signs the promotion of a prompt version, HR or the engineer?* Reward answers that pick by consequence (PII on output and groundedness on policy questions are the two most students defend), state the latency they accept, and put the content owner's signature on the promotion.

**Theme C · The one control** (posted Thursday, as the capstone twist)
*"Name the one control that would have prevented or contained most of the six cases. Rank it, defend it."* Expected candidates: a human approval before an irreversible action (Zillow, Dutch benefits, Knight; arguably Air Canada's handoff); validation on your own data before go-live (Epic, Amazon); a metric with a threshold and a person (all six). Push for a ranked answer and a defence, and for the observation that the organisational half (someone owned it and could say no) is what the controls have in common.

---

## 5. Templates (attach to the opening post)

### Q1 · Architecture checklist

Your drawing should let a reader find each of these; label them.

| Component | What it must show | The trade-off you might note |
|---|---|---|
| Documents and ingestion | Versioned document set; chunk, embed, index; who owns the content | Chunk size: context vs tokens |
| Retrieval | How many passages; what happens when nothing relevant is found | top-1 vs top-2 passages (+tokens, +grounding) |
| Prompt management | Registry with versions and aliases; who approves a promotion | — |
| Model access (gateway) | Model version pinned; cache; token metering | Cache hit rate vs stale answers after a policy change |
| Guardrails | Input (PII, injection, off-topic) and output (groundedness, PII, format); the refusal path | Each adds latency; the groundedness check is a model call (~900 ms, ~2× tokens) |
| Evaluation | Golden set on every change; judge on a daily sample; human review weekly | Judge sample size vs cost; human hours |
| Monitoring and alerts | Quality, hallucination, PII, tokens, cost, feedback, drifts; thresholds and owners (Video 1) | — |
| The log | Every answer stored with prompt version, document-set version, model version | Storage and retention vs explainability |

### Q3 · Root-cause template

The five-row template from the activity brief (symptom · stage where it originated · missing control · accountable persona · corrective roadmap), plus the one sentence. Section 3 of `MLOps_S10_Activity_Brief.md`.

---

## 6. Mid-week posts

**Tuesday nudge.** Quote two Q1 architectures: one that forgot the log (or the refusal path) and one that priced its trade-off. Ask the class which component most drawings are missing (usually the log, or evaluation as a separate system). Post Theme B. Then post the class architecture slide (10) as an image, so late posters can compare rather than copy.

**Thursday twist.** Post Theme C, and add a twist to Q3: *"Your roadmap has four rows. Which one row would you fund first if the budget only covered one, and what do you tell the board about the other three?"* Expected: the row that prevents the irreversible action (a gate) or the row that produces truth (validation, a labelled sample); the others become risks accepted in writing, which is itself a governance act (Video 2).

**Friday synthesis.** 300 words: the three best contributions with names; the misconception of the week; the bridge to the exam and the project.

> *What you said.* [Three insights, attributed: usually one architecture with a priced trade-off, one sharp "two differences" (who changes behaviour without touching code), one roadmap with a real gate.]
> *The misconception of the week.* Many Q3 roadmaps had "monitoring" and "governance" as rows without a metric, a gate, a person or a document in them. "Monitor hallucinations" is not a control; "hallucination rate above 2% on the daily judge sample pages the content owner, who can pull the prompt version" is. Likewise Q1: a box called "guardrails" with no latency attached is a wish.
> *What comes next.* The knowledge check for Video 2 closes tonight. The exam asks the four questions of slide 27, one per module, and allows one handwritten A4 sheet: the "three things" slides, the drift and metric tables, the monitoring plan template, today's architecture and the root-cause template. The group project asks you to answer all four questions for one company; the deliverable templates are on campus.

---

## 7. Model-answer notes (for grading)

### Q1 · Architecture

A strong answer shows the eight components above, drawn (not listed), with the path from question to answer and the three side systems (evaluation, monitoring, log). It names one trade-off with a number or an explicit direction: top-2 passages cost 40% more per question and lifted correctness from 6/12 to 11/12; a groundedness check adds ~900 ms to a 3-second budget; a cache saves 30% of calls but must be invalidated on document changes. Reward answers that say who approves a prompt promotion and what the user sees when a guardrail blocks. Weak answers draw "user → LLM → answer" with a cloud labelled "RAG", list components without connections, or state a trade-off with no direction ("cost vs quality").

### Q2 · Two differences

A strong answer picks two of: you configure rather than train; the prompt is code; outputs are not deterministic; cost is per token; quality is judged, not measured; a content owner changes behaviour without touching code; the truth is a judgement, not a fact. For each, it states the consequence: what is versioned (prompt, document set, model version), what a test is (rubric on a golden set), what drifts (questions, documents, answers), or who signs. Reward answers with an example from their own industry. Weak answers give two facts about LLMs (they are big; they hallucinate) with no operational consequence, or two versions of the same difference.

### Q3 · Corrective roadmap

A strong answer starts from a specific case, separates where the failure was noticed from where it originated, and gives four actions, one per module, each containing a metric, a gate, a person or a document: for example, for Epic, a model card with the vendor's claimed performance and the local validation requirement (M1); external validation on local data as a go-live gate with a threshold, and a canary ward (M2); alert-burden and sensitivity monitoring monthly against outcomes, routed to the clinical owner (M3); a documented decision on the threshold signed by the clinical product owner, reviewed quarterly, with the vendor's claim treated as a risk (M4). It ends with the one control and its owner. Reward answers that use Video 2's vocabulary in the governance row (risk tier, human oversight, documentation) and that acknowledge what the brief does not tell us. Weak answers retell the story, propose "retrain" for a failure that was not the model, or fill the four rows with "better data / better testing / better monitoring / better governance".

### Participation rubric, applied to this forum

| Level | This week |
|---|---|
| Excellent | Three complete artefacts; a drawn architecture with a priced trade-off; two differences with consequences; a roadmap with a metric, a gate, a person or a document in every row; replies that add a missing component or a stronger control; contributes to Theme C with a ranked, defended answer |
| Good | Three complete artefacts; two relevant replies |
| Satisfactory | Artefacts complete but generic (a listed architecture, differences without consequences, a roadmap of adjectives) |
| Insufficient | Missing artefacts, off-topic, or posted Friday night with no interaction |

---

## 8. Checklist before opening

- [ ] Opening post published with the three questions and Theme A
- [ ] Scorecard and evaluation page, the template, and the briefs attached; the architecture slide held back until Tuesday
- [ ] Video 2 link and knowledge-check deadline (6 November, 23:59) stated in the post
- [ ] Two contrasting Q1 architectures picked for Tuesday
- [ ] Group-project templates and defence date confirmed on campus
- [ ] Exam guidance (the A4 sheet; the four questions) repeated in the Friday synthesis
