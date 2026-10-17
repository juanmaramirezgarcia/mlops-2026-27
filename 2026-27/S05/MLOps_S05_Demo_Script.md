# Session 5 · Live demo script: "a pipeline that runs itself" (GitHub Actions)

**Slot:** minutes 19–26 (slide 11 "What a pipeline run looks like", then slide 12 "What you just saw")
**Duration:** 6 minutes, browser only; one optional live push
**Repository:** `https://github.com/juanmaramirezgarcia/mlops-demo-churn` (the Session 1 repository)
**Preparation:** `demo/prepare_s5_demo.sh`, run once a few days before the session (dry-run tested on 16 October: green on `main`, red on the branch at "Validate data")
**Offline fallback:** `demo/offline_fallback.html` (the four views, rebuilt from the real pipeline output)

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

Then, on GitHub, open a pull request for the branch using the link the script prints (title it "Weekly extract 12 October"), **do not merge it**, and click **Convert to draft** so it cannot be merged by accident. (Done 16 October: pull request #1, draft, two failing checks.) The pull request page shows the red check next to the description, which is the most natural place to click during the demo.

Check the four URLs open, and bookmark them in this order:

| Tab | URL |
|---|---|
| 1 · All runs | `https://github.com/juanmaramirezgarcia/mlops-demo-churn/actions` |
| 2 · The green run | click the latest run on `main` ("Name the CI steps and add a data validation step") |
| 3 · The pull request | `https://github.com/juanmaramirezgarcia/mlops-demo-churn/pulls` → "Weekly extract 12 October" |
| 4 · The red run's log | from the pull request, **Checks** → `ci` → the step "Validate data" |

Zoom the browser to 125–150%. **Be signed in to GitHub in that browser:** the step-by-step logs of a run are only shown to signed-in users, even on a public repository. Tested: on `main` all four steps pass; on the branch the pipeline stops at "Validate data" with the message `DATA VALIDATION FAILED: More than 5% empty values in: ['tenure_months'] ({'tenure_months': 0.7})`.

---

## 2. The six minutes, click by click

### Tab 1 · The list of runs (≈ 1 min)

> "This is the Actions page: every time someone pushed a change to the repository, a machine somewhere started, ran the pipeline, and wrote down what happened. Green tick: everything passed. Red cross: something stopped it. Two weeks ago you saw the commits; these are the runs the commits triggered. Nobody clicked 'run'."

Point at the workflow name `ci` and at the two most recent runs: one green on `main`, one red on the branch.

### Tab 2 · The green run (≈ 1.5 min)

Open the run on `main`. The job `pipeline` shows the steps with times.

> "Read the steps. Check out the code, set up Python, install the exact libraries. Then the four that matter: **tests on code**, the validation rules behave as specified; **validate data**, the training extract passes the checks; **train and evaluate**, the model trains end to end; **model card present**, an owner is written down. About twenty-five seconds. Every push, forever."

Click **Validate data** to expand it: one line, "Data validation passed: 10 rows, 7 columns…". "This is the test pyramid's middle layer, running."

### Tab 3 · The pull request (≈ 1 min)

> "Now a different day. The weekly extract arrives from the supplier; an automated job proposes it to the repository as a pull request. Look at the description: 'the supplier changed the customer schema'. And look at the check: red."

Point at the red ✗ next to `ci`. "The pipeline is refusing to let this data in. Let's see why." (If someone asks about the grey **Draft** label: "I locked it so nobody can merge it by accident; in a real team the failing check alone would block the merge.")

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

## 3. Demo 2 · From the registry to a container, click by click

**Slot:** slide 16 ("Demo: from the registry to a live endpoint, in four steps"), right after the container explanation on slide 15. Launch the chat poll on slide 15 and leave it open while you do the demo; read two answers at the end. About 4 minutes. Point to the slide's four cards as you go: registry, Dockerfile, container running, two customers.

**What it shows:** the model that the Session 3 registry calls **production** (`churn-model`, version 1), copied out of the registry and packed into a container last night, started live, and answering two customers. The last mile students have not seen yet: from a registry entry to a running service waiting for requests.

**Files:** `S05/demo/build_registry_container.command` (run once, the night before), `S05/demo/class_commands.txt` (the commands to copy in class), `S05/demo/customers.json` (two customers).

**The night before (10 minutes):** open Rancher Desktop and wait until it says Ready (engine: **dockerd (moby)**, in Preferences → Container Engine). Then double-click `build_registry_container.command`. It asks the registry which version is `production`, copies that model into `S05/demo/registry_box/model`, writes an eight-line recipe (`registry_box/Dockerfile`: a slim Python, the model's exact libraries, the model, MLflow's web server) and builds the image `churn-model:production` (3–6 minutes the first time), then starts it once, checks it answers, and stops it. (It builds natively for Apple-silicon Macs; MLflow's own `build-docker` forces an Intel image that crashes there.) Expected last lines: `ping : HTTP 200` and `prediction : {"predictions": [0, 1]}`.

**Before class:** Rancher Desktop running; a Terminal window in `S05/demo` at 18 pt, cleared; `class_commands.txt` open next to it. Optional: the MLflow UI from Session 3 (`S03/demo/mlflow/start_mlflow_ui.command`) on **Models → churn-model**, to show where the box came from.

### Where it comes from (≈ 30 s)

If the MLflow UI is open, show **Models → churn-model**: version 1 carries the alias **production**. Otherwise say it.

> "Last week you saw this registry: version 1 is the one called 'production'. Last night I copied exactly that version out of the registry and packed it into a box. The recipe is eight lines: a slim Python, the model's exact libraries, the model, and MLflow's web server." (Optional: `cat registry_box/Dockerfile` to show it.)

Type `docker images churn-model`: one line, `churn-model:production`, 891 MB.

> "That is the box. It's sitting on my laptop, switched off."

### Start it (≈ 1 min)

Type `docker run -d -p 5002:8080 --name churn-prod churn-model:production`, then `docker ps`.

> "Now it's running: a little server, inside the box, waiting for customers on door number 5002. It doesn't know about my laptop; it carries everything it needs."

Wait about ten seconds (talk), then `curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:5002/ping` → **200**.

> "200 is the web's way of saying 'I'm alive'. It's the same question a load balancer asks every few seconds; you'll meet load balancers after the break."

### Send it two customers (≈ 1.5 min)

Type `cat customers.json`: two customers, a loyal one (60 months, €45 a month, no complaints) and an at-risk one (3 months, €110, five support tickets). Then the request:

`curl -s -X POST http://127.0.0.1:5002/invocations -H "Content-Type: application/json" -d @customers.json`

Answer: **`{"predictions": [0, 1]}`**.

> "Zero: the loyal customer stays. One: the at-risk customer is likely to leave, so the retention team should call. That's a prediction from the production model, through a network request, from a box that would run the same in a bank's cloud. This is what 'deployed' means."

### Stop it, and the rollback line (≈ 30 s)

Type `docker rm -f churn-prod`.

> "Gone. And rollback, from the next block, is exactly this: stop this box, start the previous version's box. Because the box holds everything, the previous version runs exactly as it did."

Then read two answers from the chat poll.

### Option: Talend API Tester instead of curl (cards 3 and 4)

Start the box in Terminal as above, then in Talend (project **MLOps**): **1 · ping**, `GET http://127.0.0.1:5002/ping` → **200 OK** (the body is empty on purpose; set the body view to *raw* so Talend does not show a JSON error). **2 · two customers**, `POST http://127.0.0.1:5002/invocations`, header `Content-Type: application/json`, body = the contents of `customers.json` → **200**, `{"predictions": [0, 1]}`. Optional **3 · missing column** (the same body without `support_tickets`) → **400**, "Failed to enforce schema". Stop the box in Terminal with `docker rm -f churn-prod`.

### If it fails

- `docker: command not found` or "Cannot connect to the Docker daemon": Rancher Desktop is not running, or its engine is containerd. Skip the demo and say the lines over slide 16 (its four cards tell the story); the offline page (`demo/offline_fallback.html`, section 5) shows the same screens.
- `ping` returns `000`: the server is still starting; wait five seconds and repeat.
- Port 5002 busy: use `-p 5003:8080` and `5003` in the two `curl` lines.

## 4. If something goes wrong (Demo 1)

| Problem | Do this |
|---|---|
| The runs are not there | The preparation script did not push (permission or network). Re-run it; it is safe to run twice. Check that the personal access token still has the `workflow` scope (Session 1): pushing a change to `.github/workflows/` needs it. |
| The red run is green | GitHub ran an older workflow file. Open the branch's run and check the step names; if they are the old ones, re-run the preparation script. |
| Runs are queued and not starting | GitHub Actions can lag a few minutes at busy times. Do the demo from the existing runs; skip the live push. |
| No internet, or GitHub is down | Open `demo/offline_fallback.html` in the browser: the runs list, the green run's steps, the pull request and the red run's "Validate data" log, with links at the top in the same order as the demo. Read the same script. |
| A student asks "who pays for the machine?" | "GitHub, for public repositories; a few euros a month for private ones; your own servers in a bank." |
| A student asks to see the workflow file | It is the appendix slide "A CI workflow file is the pipeline written down". Show that rather than the raw file. |

---

## 5. Optional: the container deploy lab (self-paced)

Demo 2 above shows a registry model running in a container. Separately, `S05/deploy_lab/` is a self-paced hands-on that packages a model as a FastAPI service, containerises it, runs it locally (`docker build` / `docker run`), and deploys it to Google Cloud Run — the modernised version of last year's "Conda – Docker – GCP" walkthrough. It has no cost to the 90-minute timing; point students to it, or record a ~6-minute clip. It also carries `pipeline.yml` — the **complete** pipeline automated end to end (a trigger runs test → train → build → deploy to Cloud Run, plus a weekly schedule for continuous training), the modern equivalent of last year's Jenkins trigger demo. Full instructions: `MLOps_S05_Deploy_Lab_Guide.md`. The deck's appendix slides 37–38 (package and deploy) and 39–40 (the complete pipeline in one file; orchestration in one slide) reference it.

## 6. Checklist

- [ ] `prepare_s5_demo.sh` run; green run on `main`, red run on `extract-2026-10-12`
- [ ] Pull request "Weekly extract 12 October" opened and **not merged**
- [ ] Demo 2: `build_registry_container.command` run the night before (ends with `HTTP 200` and `[0, 1]`); Rancher Desktop running before class; Terminal in `S05/demo` at 18 pt; `class_commands.txt` open
- [ ] Four tabs bookmarked in click order; "Validate data" step expanded once in each run
- [ ] `demo/offline_fallback.html` opened once (the offline fallback)
- [ ] Signed in to GitHub in the demo browser (logs need it); zoom at 125–150%; notifications off
- [ ] After the term, optionally close the pull request and delete the branch (or keep them as a teaching artefact)
