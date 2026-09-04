# Session 10 · Live demo script: "two versions of one prompt, one golden set, one judge you can read"

**Slot:** minutes 29–34 (slide 12 "Demo", then slide 13 "What you just saw" with the chat poll)
**Duration:** 5 minutes, browser only; everything pre-rendered, nothing computed live
**Assets:** `S10/demo/` — the MLflow prompt registry (`mlflow/mlflow.db`, served by `start_prompt_registry.command`), `eval_results.html`, `eval_summary.png`; the policies in `hr_policies/`, `golden_set.csv`, `answers_v1.csv`, `answers_v2.csv`, and the script that built it all, `s10_demo_setup.py`

---

## 1. What is real and what is illustrative (say it once, on slide 12)

The policies, the golden set, the two prompts, the registry and the MLflow runs are real files and real objects. The **answers** in `answers_v1.csv` and `answers_v2.csv` are illustrative transcripts written for the class: what a baseline prompt and a grounded prompt typically produce; no language model is called when the demo is built. The **judge** is a transparent, rule-based stand-in: *correct* = HR's key facts are present; *grounded* = every number in the answer exists in the source policy (or in HR's reference answer); *PII* = an employee's name from the policies is repeated. In production the judge is itself a language model with a rubric, checked against humans on a sample (Video 1, segment 5). The pattern (golden set → judge → scores per prompt version → registry with aliases) is exactly the production pattern; only the judge is simplified so students can read it. One sentence in class is enough; the appendix slide 40 shows the code if anyone asks.

## 2. Setup (before the session)

1. Double-click `S10/demo/start_prompt_registry.command` (first time: it builds the database in ~10 s; then it starts MLflow on port 5002 and opens `http://127.0.0.1:5002/#/prompts`). It uses the Session 3 environment; no new installs.
2. In the browser: **Tab 1** the MLflow Prompts page; click `hr-assistant`, then the **Compare** tab, so v2 and v1 are side by side. **Tab 2** `eval_results.html` (double-click the file). Zoom both to 125%.
3. Optional **Tab 3**: MLflow → Experiments → `hr-assistant-eval` (switch the top-left toggle to "Model training" to see the classic runs table; use the Columns menu to add `correctness`, `groundedness`, `cost_per_1000_questions_eur`).
4. Slide 13 carries the scorecard (`eval_summary.png`) as the landing slide; slide 12 carries a screenshot of the Compare view as fallback.

Numbers to have in your head: v1 **6/12 correct, 7/12 grounded, 1 PII leak, 1.59 EUR per 1,000 questions, p95 1.84 s**; v2 **11/12, 11/12, 0 leaks, 2.24 EUR (+40%), p95 1.35 s**. v2's one miss: question 11 says "until the child is 8"; the policy says 12.

## 3. The five minutes, click by click

### Tab 1 · The prompt registry (≈ 1.5 min)

> "This is MLflow, the registry you saw for the churn model in Session 3. Same idea, different artefact: the thing under version control is text. One prompt, `hr-assistant`, two versions, two aliases: version 1 is `production`, version 2 is `challenger`; the application asks for `@production`, never for a number."

Click **Compare**. Point at the right (v1): "The baseline: 'answer the employee's question in a friendly, helpful way', then the context and the question." Point at the left (v2): "Version 2 adds five rules: answer only from the policy text; if it is not there, say 'I cannot answer that' and refer to HR; quote the numbers exactly; end with the source section; sixty words; never a name, even if a name appears in the policy. Read the commit message: that is the change log. Who wrote v2? An engineer typed it; HR signed it. Hold that."

### Tab 2 · The evaluation page (≈ 2.5 min)

> "Twelve questions employees actually ask, with HR's approved answer: the golden set. Both prompts answered all twelve. A judge gives three verdicts per answer."

Point at the two summary cards at the top, then scroll:

- **Question 2** (11 years of service): "v1 says 26 days, three extra after ten years. The policy says two extra: 25. Plausible, friendly, wrong. Correct: FAIL. Grounded: FAIL, because 26 appears nowhere in the policy. v2: 25, with the section."
- **Question 5** (a month in Portugal): "v1 says yes, 45 days a year, and mentions Ana García from Sales who works from Lisbon. Three problems in one answer: the number is invented, the limit is 20 days, and it repeated a real employee's name that was in the policy as an example. Correct FAIL, grounded FAIL, PII LEAK. v2: 'not for a full month', 20 days, HR approval, no name."
- **Question 12** (the salary band): "Not in any policy. v1 invents a band: 45 to 58 thousand. That is the Air Canada pattern: confident, specific, false. v2: 'I cannot answer that; contact HR.' The refusal is the correct answer."
- **Question 11**: "And v2 is wrong once: 'until the child is 8'; the policy says 12. A grounded prompt reduces invention; it does not abolish it. That is why the judge runs daily and humans weekly."

### Back to the slide (≈ 1 min) → slide 13

> "The scorecard. v2: eleven of twelve correct and grounded, no leak, refused the out-of-scope question, and faster, because its answers are half as long. But: 2.24 euros per thousand questions against 1.59, forty percent more, because its rules add input tokens and it retrieves two passages instead of one. That is the trade-off sentence Forum 5 Q1 asks for, with numbers."

Then the poll (2 minutes, in chat): **"Promote v2 to production today?" A: yes · B: no · C: only as a canary for 10% of questions, with the judge watching.** One letter and one line. Do not resolve it; C is the Session 5 answer, and who signs the promotion (HR, not the engineer) is Forum 5's Theme B.

## 4. If someone asks (one-liners)

| Question | Answer |
|---|---|
| "Is the judge an AI?" | "Here, no: a dozen lines of rules so you can read it (appendix slide 40). In production, yes: a model with a rubric, and then humans check the judge on a sample." |
| "Why not just always use v2?" | "Forty percent more per question, and it still made one mistake. The decision needs the cost and the golden set together; that is what the registry is for." |
| "Where do the 'answers' come from?" | "Illustrative transcripts written for the class. The point is the pipeline, not the model." |
| "Can the golden set be too small?" | "Twelve is a classroom size. Real ones have 100–500 questions and grow from the questions the judge flags." |
| "Who owns the prompt?" | "HR. The engineer types it; the content owner signs it. Forum 5, Theme B." |

## 5. If something goes wrong

| Problem | Do this |
|---|---|
| MLflow does not start | Slide 12 carries the Compare screenshot; `eval_results.html` still opens (no server needed). Do the whole demo from Tab 2 and the slide. |
| Port 5002 in use | The launcher falls back to 5003; read the address it prints. |
| The Compare tab shows "diff not supported in Markdown view" | Click **Text** at the top right of the compare pane. |
| No time | Skip Tab 1; do questions 5 and 12 on Tab 2 (2 min), then slide 13 and the poll. |

## 6. Rebuilding (not needed)

`rebuild_demo.command` deletes `mlflow/` and the evaluation pages and re-runs `s10_demo_setup.py` and `render_summary.py`. Edit `golden_set.csv`, the answers or the two prompt templates in the script first if you want different content; the judge's verdicts follow automatically.

## 7. Checklist

- [ ] `start_prompt_registry.command` run once before class; the Prompts page opens
- [ ] Tab 1 on hr-assistant → Compare; Tab 2 `eval_results.html`; both at 125%
- [ ] The numbers memorised: 6/12 → 11/12; 1.59 → 2.24 EUR (+40%); 1.84 → 1.35 s; v2's one miss is Q11
- [ ] Slide 13 (scorecard + poll) ready as the landing slide
- [ ] The one sentence about what is illustrative said on slide 12
