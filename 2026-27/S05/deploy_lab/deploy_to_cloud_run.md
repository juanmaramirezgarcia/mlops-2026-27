# Deploy the churn API to Google Cloud Run

Cloud Run runs your container for you: you hand it an image, it gives back an HTTPS URL, and it scales to zero when no one is calling (you pay only for the seconds it runs). It is the simplest way to put a containerised model in the cloud, and the natural next step after `run_local.command` works on your laptop.

You need: a Google Cloud account with billing enabled, the `gcloud` CLI installed and logged in (`gcloud auth login`), and Docker Desktop (for the explicit path). Nothing in this file runs automatically — copy the commands and replace `YOUR_PROJECT_ID` and the region.

## The easy path: one command, Cloud Run builds the container for you

From inside this `deploy_lab/` folder (make sure `churn_model.pkl` exists — run `python train.py` once):

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud run deploy churn-api \
    --source . \
    --region europe-west1 \
    --allow-unauthenticated
```

`--source .` uploads the folder; Cloud Run reads the `Dockerfile`, builds the image (with Cloud Build), stores it, and deploys it. After a minute or two it prints a **Service URL** like `https://churn-api-xxxxxxxx-ew.a.run.app`. Test it:

```bash
URL=https://churn-api-xxxxxxxx-ew.a.run.app     # paste the URL it printed
curl $URL/health
curl -X POST $URL/predict -H "Content-Type: application/json" \
     -d '{"tenure_months":6,"monthly_charges":85,"support_tickets":4,"promo_weeks_last_quarter":1,"is_monthly":1,"region_north":1}'
```

Open `$URL/docs` in a browser for the interactive Swagger page. That is the whole deployment: a model, in a container, on a public HTTPS endpoint, that scales to zero.

`--allow-unauthenticated` makes the URL public, which is fine for a class demo. In production you drop it and require an identity token (this is where Session 3's endpoint protections live: who may call it, how often, what is logged).

## The explicit path: build, push, deploy (what actually happens under `--source`)

Useful to show the three steps the easy path hides. It uses Artifact Registry (the modern replacement for the Container Registry / `gcr.io` in last year's deck).

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com

# 1. a place to store images
gcloud artifacts repositories create models --repository-format=docker --location=europe-west1

# 2. build the image and push it to the registry (Cloud Build does it in the cloud)
gcloud builds submit --tag europe-west1-docker.pkg.dev/YOUR_PROJECT_ID/models/churn-api:v1

# 3. deploy that image to Cloud Run
gcloud run deploy churn-api \
    --image europe-west1-docker.pkg.dev/YOUR_PROJECT_ID/models/churn-api:v1 \
    --region europe-west1 --allow-unauthenticated
```

To build locally with Docker instead of Cloud Build, replace step 2 with `docker build -t europe-west1-docker.pkg.dev/YOUR_PROJECT_ID/models/churn-api:v1 .` then `gcloud auth configure-docker europe-west1-docker.pkg.dev` and `docker push …`.

## At scale: GKE (Kubernetes), the heavier option

Cloud Run is the right tool for a single model served over HTTP. When you run **many** services that must be managed together, share a network, need fine-grained scaling, GPUs, or run more than just web requests, teams use **GKE (Google Kubernetes Engine)** — the path last year's deck showed. The same image works; the deployment is more involved:

```bash
gcloud container clusters create-auto churn-cluster --region europe-west1
kubectl create deployment churn-api --image europe-west1-docker.pkg.dev/YOUR_PROJECT_ID/models/churn-api:v1
kubectl expose deployment churn-api --type=LoadBalancer --port 80 --target-port 8080
kubectl get service churn-api        # wait for an EXTERNAL-IP, then curl it
```

The trade-off is exactly the Session 5 lesson: Cloud Run gives you less to operate (no cluster, scales to zero), GKE gives you more control and is worth its extra moving parts only when you have many things to run. Start on Cloud Run; move to GKE when you have outgrown it.

## Clean up (so you are not billed)

```bash
gcloud run services delete churn-api --region europe-west1
# and, if you created them:
gcloud artifacts repositories delete models --location=europe-west1
gcloud container clusters delete churn-cluster --region europe-west1
```

Cloud Run scales to zero, so an idle service costs almost nothing, but deleting it is tidiest after the class.
