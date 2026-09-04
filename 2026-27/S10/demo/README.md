# Session 10 demo: two versions of one prompt, one golden set, one judge you can read

Everything is pre-built; the class needs a browser. Uses the Session 3 environment (`S03/demo/mlflow/.venv`); nothing new to install.

| File / folder | Role |
|---|---|
| `start_prompt_registry.command` | Mac launcher: builds the database on first run, starts MLflow on port 5002, opens the Prompts page |
| `rebuild_demo.command` | Deletes and rebuilds the database and the evaluation pages (only if you edit the content) |
| `s10_demo_setup.py` | Registers prompt v1 (`@production`) and v2 (`@challenger`) in MLflow's prompt registry; runs the judge on the golden set; logs one MLflow run per version; writes `eval_results.html/.csv` |
| `render_summary.py` | Draws `eval_summary.png` (the scorecard on slide 13) from `eval_results.csv` |
| `hr_policies/` | Four fictional TelcoNova HR policies (holidays, remote work, expenses, parental leave); one deliberately contains an employee's name as an example |
| `golden_set.csv` | 12 questions with HR's key facts and reference answer; question 12 is out of scope on purpose |
| `answers_v1.csv`, `answers_v2.csv` | Illustrative transcripts of what each prompt version answers (no model is called) |
| `mlflow/mlflow.db` | The registry and the two evaluation runs (`hr-assistant-eval`) |
| `eval_results.html`, `eval_results.png` | Per-question table: both answers, three verdicts each (correct · grounded · PII) |
| `eval_summary.png` | The v1-vs-v2 scorecard |
| `ui_prompts_list.png`, `ui_prompt_versions.png`, `ui_prompt_compare.png` | Screenshots of the MLflow UI, as fallback for the slides |

## What is real and what is illustrative

Real: the policies, the golden set, the two prompt templates, the registry entries, the MLflow runs. Illustrative: the answers (written for the class), and the judge (rule-based: key facts present; every number exists in the policy or HR's reference answer; no employee name repeated). In production the judge is a model with a rubric, checked against humans on a sample. The pattern is the production pattern.

## Expected numbers

v1 · production · baseline: 6/12 correct · 7/12 grounded · 1 PII leak · invents a salary band for Q12 · 399 in + 60 out tokens · 1.59 EUR per 1,000 questions · p95 1.84 s
v2 · challenger · grounded + top-2 passages: 11/12 · 11/12 · 0 leaks · refuses Q12 · 760 in + 34 out tokens · 2.24 EUR (+40%) · p95 1.35 s · one miss (Q11: "8" instead of "12")

## Run it by hand

```bash
cd S10/demo
source ../../S03/demo/mlflow/.venv/bin/activate
python s10_demo_setup.py            # ~10 s; prints the two metric sets
python render_summary.py            # optional; needs Pillow (already in the venv via matplotlib)
mlflow ui --backend-store-uri sqlite:///mlflow/mlflow.db --port 5002
```

The database stores absolute paths from the machine that built it; the launcher rewrites them to this folder on start. Runs have no artefacts, so the UI works either way.
