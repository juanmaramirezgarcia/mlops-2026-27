# Session 5 deploy lab · package a model as a container, run it locally, deploy it to the cloud

A small, self-contained hands-on lab: take a trained model, wrap it in a REST API with **FastAPI**, put it in a **Docker** container, run it on your laptop, and deploy it to **Google Cloud Run**. It is the practical companion to Session 5's deployment block, and the modernised version of last year's "Conda – Docker – GCP" walkthrough (FastAPI instead of bare Flask; Cloud Run instead of a full Kubernetes cluster, with GKE noted as the scale path).

Optional and self-paced: nothing here is examinable. Do it to feel how a model actually ships.

## The four files that make a model an API

| File | What it is |
|---|---|
| `churn_model.pkl` | The trained model. `train.py` builds it from a small synthetic dataset using the course's churn features (tenure, monthly charges, support tickets, promos, contract type, region). |
| `app.py` | The REST API (FastAPI): a `/predict` endpoint that takes one customer and returns a churn probability, plus `/health` and automatic docs at `/docs`. |
| `requirements.txt` | The exact library versions. This is what makes the container reproducible — no "it worked on my laptop". |
| `Dockerfile` | The recipe: start from slim Python, install the requirements, copy the model and the code, run the API. |

Everything else is convenience or automation: `run_local.command` (build and run in one click), `call_api.py` (call the API from Python), `test_api.py` (the CI tests), `deploy_to_cloud_run.md` (the cloud commands), `pipeline.yml` (the complete pipeline, automated — see below), `.dockerignore`.

## Run it on your laptop (needs Docker Desktop running, and Python 3)

Easiest — double-click **`run_local.command`** (or run it in Terminal). It trains the model if needed, builds the image, starts the container on port 8080, tests it, and opens the interactive docs. To stop it: `docker rm -f churn-api`.

By hand, to see each step:

```bash
cd deploy_lab
python train.py                                   # writes churn_model.pkl  (once)
docker build -t churn-api:v1 .                    # the recipe -> an image
docker run -d -p 8080:8080 --name churn-api churn-api:v1   # the image -> a running container
curl http://127.0.0.1:8080/health
curl -X POST http://127.0.0.1:8080/predict -H "Content-Type: application/json" \
     -d '{"tenure_months":6,"monthly_charges":85,"support_tickets":4,"promo_weeks_last_quarter":1,"is_monthly":1,"region_north":1}'
python call_api.py                            # the same call, from Python
open http://127.0.0.1:8080/docs                   # try it in the browser
docker rm -f churn-api                            # stop and remove
```

Expected: `/health` returns `{"status":"ok",...}`; the high-risk customer above returns about **`{"churn_probability":0.88,"churn":true}`**; a loyal customer (long tenure, no tickets, annual contract) returns about `0.02`. A request missing a field is rejected with a clear `422` — that is FastAPI validating the input, a small piece of the Session 3 "check what comes in" idea.

## Without Docker (just the API)

If you only want to see the API, skip the container: `pip install -r requirements.txt` then `uvicorn app:app --reload --port 8080`, and use the same `curl` / `/docs` as above. Docker is what makes it shippable; uvicorn alone is what makes it run.

## Deploy it to the cloud

See **`deploy_to_cloud_run.md`**. The short version, once you have `gcloud` set up:

```bash
gcloud run deploy churn-api --source . --region europe-west1 --allow-unauthenticated
```

Cloud Run reads the Dockerfile, builds the image, and gives you an HTTPS URL that scales to zero. The same file also shows the explicit build → push → deploy steps, and the GKE (Kubernetes) path for when one service becomes many.

## What is real and what is illustrative

Real and runnable: the training, the API, the container, the Cloud Run commands. Illustrative: the **data is synthetic** (generated in `train.py`, no real customers) and the model is a small teaching model, not TelcoNova's. The *shape* — model → API → container → local → cloud — is exactly what a production deployment looks like; only the data and the scale are shrunk so it runs on a laptop in a few minutes.

## The complete pipeline, automated (pipeline.yml)

`pipeline.yml` is the whole thing running by itself: a trigger → test → train → build → deploy, the modern equivalent of last year's Jenkins trigger demo. In a real repository it goes in `.github/workflows/`. On a push to `main`, a weekly schedule (continuous training), or the manual button, GitHub Actions runs the tests, trains the model, and — from `main`, when a cloud credential is configured — builds the container and deploys it to Cloud Run. Without the credential the deploy job is skipped, so the file is safe to commit and the CI half runs for anyone. See the lab guide (`../MLOps_S05_Deploy_Lab_Guide.md`, section "The complete pipeline") for the one-time GCP setup.

## Where this sits in Session 5

The live session teaches the concepts (containers, serving patterns, rollout strategies, serverless vs Kubernetes) and demos the CI pipeline. This lab is the hands-on that the 90 minutes cannot fit: the actual `docker build` / `docker run` / `gcloud run deploy`. The deck's appendix slides "Package a model as a REST API" and "Run it locally, then deploy to Cloud Run" point here.
