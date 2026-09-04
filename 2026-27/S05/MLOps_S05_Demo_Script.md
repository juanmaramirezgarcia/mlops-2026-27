# Session 5 · Live demo script: "a pipeline that runs itself" (GitHub Actions)

**Slot:** minutes 19–26 (slide 11 "What a pipeline run looks like", then slide 12 "What you just saw")
**Duration:** 6 minutes, browser only; one optional live push
**Repository:** `https://github.com/juanmaramirezgarcia/mlops-demo-churn` (the Session 1 repository)
**Preparation:** `demo/prepare_s5_demo.sh`, run once a few days before the session

---

## 1. Preparation (10 minutes, a few days before)

The repository already has a CI workflow (the "green tick" students were asked to look at). The preparation script makes two changes so the Actions page reads like the slide, and creates the red run.

In Terminal, inside your local clone of the repository:

```bash
cd "/Users/juanramirez/Documents/JM new/MLOps Rev2026/2026-27/S01/demo/mlops-demo-churn"
bash "../../../S05/demo/prepare_s5_demo.sh"
```

What it does:

1. Renames the CI steps so they appear on GitHub as **Tests on code → Validate data → Train and evaluate → Model card present**, and adds `src/check_data.py`, which runs the Session 1 validation rules on the training extract and fails the pipeline if they do not pass. Commits and pushes to `main`: a **green run** appears within a minute or two.
2. Creates a branch `extract-2026-10-12` in which `data/churn_sample.csv` has `tenure_months` empty for 70% of customers (the NorthRetail bug, again) with a commit message that reads like an automated extract. Pushes it: a **red run** appears, failing at "Validate data". `main` is untouched.

Then, on GitHub, open a pull request for the branch using the link the script prints (title it "Weekly extract 12 October"), and **do not merge it**. The pull request page shows the red check next to the description, which is the most natural place to click during the demo.

Check the four URLs open, and bookmark them in this order:

| Tab | URL |
|---|---|
| 1 · All runs | `https://github.com/juanmaramirezgarcia/mlops-demo-churn/actions` |
| 2 · The green run | click the latest run on `main` ("Name the CI steps and add a data validation step") |
| 3 · The pull request | `https://github.com/juanmaramirezgarcia/mlops-demo-churn/pulls` → "Weekly extract 12 October" |
| 4 · The red run's log | from the pull request, **Checks** → `ci` → the step "Validate data" |

Zoom the browser to 125–150%. Tested: on `main` all four steps pass; on the branch the pipeline stops at "Validate data" with the message `DATA VALIDATION FAILED: More than 5% empty values in: ['tenure_months'] ({'tenure_months': 0.7})`.

---

## 2. The six minutes, click by click

### Tab 1 · The list of runs (≈ 1 min)

> "This is the Actions page: every time someone pushed a change to the repository, a machine somewhere started, ran the pipeline, and wrote down what happened. Green tick: everything passed. Red cross: something stopped it. Two weeks ago you saw the commits; these are the runs the commits triggered. Nobody clicked 'run'."

Point at the workflow name `ci` and at the two most recent runs: one green on `main`, one red on the branch.

### Tab 2 · The green run (≈ 1.5 min)

Open the run on `main`. The job `pipeline` shows the steps with times.

> "Read the steps. Check out the code, set up Python, install the exact libraries. Then the four that matter: **tests on code**, the validation rules behave as specified; **validate data**, the training extract passes the checks; **train and evaluate**, the model trains end to end; **model card present**, an owner is written down. Forty seconds. Every push, forever."

Click **Validate data** to expand it: one line, "Data validation passed: 10 rows, 7 columns…". "This is the test pyramid's middle layer, running."

### Tab 3 · The pull request (≈ 1 min)

> "Now a different day. The weekly extract arrives from the supplier; an automated job proposes it to the repository as a pull request. Look at the description: 'the supplier changed the customer schema'. And look at the check: red."

Point at the red ✗ next to `ci`. "The pipeline is refusing to let this data in. Let's see why."

### Tab 4 · The red run's log (≈ 1.5 min)

Click **Details** → the run → expand **Validate data**.

> "`DATA VALIDATION FAILED: More than 5% empty values in tenure_months, 0.7`. Seventy percent of one feature is empty. The steps after it never ran: nothing was trained, nothing was deployed, and there is a record of exactly what was rejected and when. Compare with NorthRetail, where the same problem ran for four months. The difference is one step in a pipeline."

Point at the greyed-out steps below: "Train and evaluate: skipped. Model card: skipped."

### Optional · Push a change live (≈ 1 min, only if ahead of time)

In Terminal, in the repository folder, a one-line change and a push:

```bash
echo "" >> MODEL_CARD.md && git commit -qam "Touch the model card (live in Session 5)" && git push -q
```

Switch to Tab 1 and refresh: a yellow dot appears, the run is queued. "By the time we finish the next slide it will be green or red. That is what continuous means." Check it again after slide 13.

### Back to the slide (≈ 30 s)

> "Three things: it ran by itself; it stopped at the data test, before anything was trained; and it left a record. The pipeline decided the change was safe, or not. Next: what exactly gets shipped when it says yes, and how it reaches customers."

Switch to slide 12, "What you just saw".

---

## 3. If something goes wrong

| Problem | Do this |
|---|---|
| The runs are not there | The preparation script did not push (permission or network). Re-run it; it is safe to run twice. Check that the personal access token still has the `workflow` scope (Session 1). |
| The red run is green | GitHub ran an older workflow file. Open the branch's run and check the step names; if they are the old ones, re-run the preparation script. |
| Runs are queued and not starting | GitHub Actions can lag a few minutes at busy times. Do the demo from the existing runs; skip the live push. |
| No internet | Screenshots in `demo/screenshots/`: the runs list, the green run's steps, the red run's "Validate data" log. Take them once after preparation. |
| A student asks "who pays for the machine?" | "GitHub, for public repositories; a few euros a month for private ones; your own servers in a bank." |
| A student asks to see the workflow file | It is the appendix slide "A CI workflow file is the pipeline written down". Show that rather than the raw file. |

---

## 4. Optional: the container deploy lab (not the live demo)

The live demo is the GitHub Actions pipeline above. Separately, `S05/deploy_lab/` is a self-paced hands-on that packages a model as a FastAPI service, containerises it, runs it locally (`docker build` / `docker run`), and deploys it to Google Cloud Run — the modernised version of last year's "Conda – Docker – GCP" walkthrough. It has no cost to the 90-minute timing; point students to it, or record a ~6-minute clip. It also carries `pipeline.yml` — the **complete** pipeline automated end to end (a trigger runs test → train → build → deploy to Cloud Run, plus a weekly schedule for continuous training), the modern equivalent of last year's Jenkins trigger demo. Full instructions: `MLOps_S05_Deploy_Lab_Guide.md`. The deck's appendix slides 36–37 (package and deploy) and 39–40 (the complete pipeline in one file; orchestration in one slide) reference it.

## 5. Checklist

- [ ] `prepare_s5_demo.sh` run; green run on `main`, red run on `extract-2026-10-12`
- [ ] Pull request "Weekly extract 12 October" opened and **not merged**
- [ ] Four tabs bookmarked in click order; "Validate data" step expanded once in each run
- [ ] Screenshots saved as the offline fallback
- [ ] Browser zoom at 125–150%; notifications off
- [ ] After the term, optionally close the pull request and delete the branch (or keep them as a teaching artefact)
