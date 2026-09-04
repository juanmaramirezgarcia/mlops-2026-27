# Session 5 · Deploy lab guide: package a model as a container, run it locally, deploy to GCP

**What it is:** a self-paced, hands-on lab that restores the practical deployment walkthrough from last year's "Conda – Docker – GCP" deck, modernised: **FastAPI** instead of bare Flask, **Google Cloud Run** as the simplest cloud target (with GKE noted as the scale path). It is optional and not examinable.

**Where it lives:** `S05/deploy_lab/`. The deck's appendix slides "Package a model as a REST API" and "Run it on your laptop, then deploy to Google Cloud Run" point here.

**Why it is a lab, not a live demo:** the live 90 minutes teaches the concepts (containers, serving patterns, rollout strategies, serverless vs Kubernetes) and demos the CI pipeline. The actual `docker build` / `docker run` / `gcloud run deploy` needs a laptop, Docker Desktop and a cloud account, so it is set up to be done outside class — by you as a screen-recorded optional segment, or by students who want the hands-on.

---

## 1. What the lab contains

| File | Role |
|---|---|
| `train.py` | Builds `churn_model.pkl` from a small synthetic dataset (the course's churn features). Self-contained; no data files, no internet. |
| `app.py` | The REST API (FastAPI): `POST /predict` returns a churn probability; `GET /health`; auto docs at `/docs`. |
| `requirements.txt` | Exact library versions (fastapi, uvicorn, scikit-learn, pandas). |
| `Dockerfile` | Packages the four files into an image; runs the API with uvicorn on port 8080. |
| `.dockerignore` | Keeps docs and scratch out of the image. |
| `run_local.command` | Mac one-click: train → build → run → test → open the docs. |
| `call_api.py` | Calls the running API from Python (last year's `requests.py`). |
| `test_api.py` | The CI tests (pytest): `/health`, a high-risk and a loyal customer, and a rejected bad request. |
| `pipeline.yml` | The complete pipeline automated end to end (trigger → test → train → build → deploy); see section 8. |
| `deploy_to_cloud_run.md` | The `gcloud` commands: the one-command path, the explicit build/push/deploy path, and the GKE option. |
| `README.md` | The student-facing explanation of the whole lab. |

## 2. The story it tells (the four moves)

1. **A model becomes a service.** `app.py` loads `churn_model.pkl` and answers HTTP requests. Ten lines of FastAPI turn a `.pkl` into something the rest of the company can call.
2. **A service becomes a shippable box.** The `Dockerfile` bundles the model, the code and the exact libraries into one image. "It worked on my laptop" stops being a risk because the laptop's environment travels inside the box.
3. **The box runs on your laptop.** `docker build` then `docker run -p 8080:8080`, and `curl localhost:8080/predict` answers. This is the local test last year's deck did with Flask on port 5000.
4. **The box runs in the cloud.** `gcloud run deploy --source .` hands the same image to Cloud Run and returns an HTTPS URL that scales to zero. GKE (Kubernetes) is the heavier path for when one service becomes many.

## 3. Running it yourself (about 10 minutes, laptop)

Prerequisites: **Docker Desktop** running, **Python 3**, and for the cloud part the **`gcloud` CLI** logged in to a project with billing.

The one-click way: double-click `S05/deploy_lab/run_local.command`. It trains the model, builds the image, starts the container, tests `/health` and `/predict`, and opens `http://127.0.0.1:8080/docs`. Stop it with `docker rm -f churn-api`.

By hand, to narrate each step (this is the sequence to screen-record if you want a video):

```bash
cd S05/deploy_lab
python train.py                                    # -> churn_model.pkl
docker build -t churn-api:v1 .                     # the recipe -> an image
docker run -d -p 8080:8080 --name churn-api churn-api:v1
curl http://127.0.0.1:8080/health
curl -X POST http://127.0.0.1:8080/predict -H "Content-Type: application/json" \
     -d '{"tenure_months":6,"monthly_charges":85,"support_tickets":4,"promo_weeks_last_quarter":1,"is_monthly":1,"region_north":1}'
open http://127.0.0.1:8080/docs                     # try it in the browser
docker rm -f churn-api                              # stop
```

**Expected results** (verified): `/health` returns `{"status":"ok",...}`; the high-risk customer above returns about `{"churn_probability":0.88,"churn":true}`; a loyal customer (60 months, 0 tickets, annual contract, `is_monthly:0`) returns about `0.02`; a request missing a field is rejected with `422`. Point out the last one: FastAPI validated the input for free — the Session 3 "check what comes in" idea, without extra code.

## 4. Deploying to Cloud Run (about 5 minutes, needs a GCP account)

From `deploy_to_cloud_run.md`, the short path:

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud run deploy churn-api --source . --region europe-west1 --allow-unauthenticated
```

Cloud Run reads the Dockerfile, builds the image, deploys it, and prints a **Service URL**. Test it with the same `curl` against that URL, and open `URL/docs`. That is a containerised model on a public HTTPS endpoint that scales to zero. The file also has the explicit build → push (Artifact Registry) → deploy steps, and the GKE cluster commands for the "at scale" story.

**Teaching point (the Session 5 trade-off, made concrete):** Cloud Run gives you less to operate and scales to zero; GKE gives you more control and is worth its extra moving parts only when you run many services or need GPUs. Start on Cloud Run; move to GKE when you have outgrown it. This is the same "match the tool to the constraint" lesson as the rollout-strategy scorecard.

## 5. If you want to show it live (optional, ~6 minutes)

Not required — the CI/GitHub Actions demo remains the session's live demo. But if you have time or want a short screen-recording to post on the campus:

1. Have Docker Desktop running and the lab folder open. Run `run_local.command`; while it builds, narrate the four files.
2. When the docs page opens, submit the example request in the browser (`/docs` → `POST /predict` → "Try it out" → Execute) so students see the JSON answer.
3. Show `deploy_to_cloud_run.md`; if you have a project ready, run the one-command deploy and `curl` the live URL. If not, show the command and the URL from a previous run.
4. Land on the appendix slide "Run it on your laptop, then deploy to Cloud Run".

If you screen-record it, put it on the campus next to the Session 5 materials as an optional "how a model actually ships" clip.

## 6. What is real and what is illustrative

Real and runnable: the training, the API, the container, and the Cloud Run commands. Illustrative: the **data is synthetic** (generated in `train.py`; no real customers) and the model is a small teaching model, not TelcoNova's. The shape — model → API → container → local → cloud — is exactly a production deployment; only the data and the scale are shrunk to fit a laptop and a few minutes.

## 7. Relationship to last year's "Conda – Docker – GCP" deck

| Last year (05P) | This lab |
|---|---|
| Environments: conda, pyenv, poetry | `requirements.txt` + the container (the environment travels in the box); a one-line note is enough for a non-technical cohort |
| Flask + gunicorn REST API | FastAPI (automatic validation and docs; less code) |
| `docker build` / `docker run -p 5000:5000`, test with requests/curl/Talend | Same, port 8080, tested with curl / `/docs` / `call_api.py` |
| Deploy to GCP with GKE: cluster create, `kubectl` deploy, LoadBalancer | Deploy to **Cloud Run** with one command; GKE kept as the documented "scale path" |
| Container Registry (`gcr.io`) | Artifact Registry (its modern replacement), in the explicit path |

The concepts are unchanged; the tools are the 2026 defaults, and the cloud step is much shorter, which suits the non-technical audience.

## 8. The complete pipeline: automate it end to end (pipeline.yml)

This is the answer to "how would a *complete* MLOps pipeline be automated?", and the modern equivalent of last year's Jenkins trigger demo. The file is `deploy_lab/pipeline.yml`; in a real repository it lives at `.github/workflows/pipeline.yml`. The deck appendix slide "The complete pipeline in one file" shows it.

**What it does.** One trigger starts the whole pipeline, which runs itself:

1. **Triggers** — a push to `main` (code or data changed), a weekly **schedule** (`cron`, = continuous training on fresh data), and a manual button (`workflow_dispatch`).
2. **Job `test-train`** (Pipeline CI + Continuous Training) — install, `python train.py` (train on the latest data), `pytest -q test_api.py` (the gate: a failing test stops the run red), and keep the trained model as an artefact.
3. **Job `deploy`** (Model CD) — only from `main`, only when enabled: authenticate to Google Cloud, then `gcloud run deploy churn-api --source .`. The pipeline ends in a live, updated prediction service; monitoring (Session 7, Video 1) watches it and can raise the next trigger, closing the loop.

**How it maps to the live session.** It is the "stage by stage" slide made real: trigger → Pipeline CI (test) → Continuous Training (train) → Model CD (build + deploy). The Session 5 live demo showed the CI half running on a push; this file is the same idea carried through to deployment and to a schedule.

**Making the deploy step actually run (one-time GCP setup).** The CI half needs nothing. To turn the deploy job on:

1. In Google Cloud, create a service account with the roles *Cloud Run Admin*, *Cloud Build Editor*, *Artifact Registry Writer* and *Service Account User*, and download a JSON key.
2. In the GitHub repository → Settings → Secrets and variables → Actions, add two **secrets**: `GCP_SA_KEY` (paste the JSON) and `GCP_PROJECT_ID` (your project id). Add one **variable** `DEPLOY_ENABLED` = `true`.
3. Push to `main`. The Actions tab shows the run: `test-train` then `deploy`, ending with a Cloud Run URL. (A cleaner production setup uses Workload Identity Federation instead of a JSON key; the key is fine for a class.)

Leave `DEPLOY_ENABLED` unset and the pipeline is still a complete, safe CI+CT demo that anyone can run; the deploy job simply shows as skipped.

**If you want to show it live (optional, ~3 minutes):** open the repository's Actions tab, click the latest run, and walk the two jobs and their steps; then show `pipeline.yml` and point at the three triggers and the `deploy` job. This is the "complete automation" moment last year's Jenkins demo delivered, without leaving GitHub.

## 9. Checklist

- [ ] `run_local.command` runs clean on your Mac (Docker Desktop up): build succeeds, `/predict` returns ~0.88 for the high-risk example
- [ ] `gcloud run deploy --source .` tested once against a real project (or the commands read and understood)
- [ ] Decide: leave as an optional student lab, or record a ~6-minute clip for the campus
- [ ] Lab folder present under `S05/deploy_lab/`; appendix slides 36–37 (package/deploy) and 39–40 (complete pipeline, orchestration) point to it
- [ ] `pytest -q test_api.py` passes locally (4 tests); `pipeline.yml` reviewed; decide whether to wire the GCP secret for a live deploy
