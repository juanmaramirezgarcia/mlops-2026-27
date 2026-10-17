# Lab · From the registry to a container · Notes for the professor

*Not for students. Expected results, checked by serving the same model (churn-model v1, the registry's `production` version) with the same request format.*

## What to post on the campus

- `MLOps_S05_Registry_to_Container_Lab.pdf` (the student guide)
- `MLOps_S05_Registry_to_Container_Lab.zip` (the `churn_model_box` folder: `model/`, `Dockerfile`, `customers.json`, `my_customer.json`, `README.txt`)

The model in the zip is a copy of version 1 of `churn-model` from the Session 3 registry (logistic regression on 3 features, trained with scikit-learn 1.7.2, Python 3.10.12). The box installs exactly those versions, so every student gets the same answers. Built and tested on an Apple-silicon Mac with Rancher Desktop (dockerd): image 891 MB, build about 30 seconds once the downloads are cached, a few minutes the first time.

## Expected results

| Step | Command | Expected |
|---|---|---|
| 2 | `docker images churn-model` | `churn-model:production`, about 900 MB |
| 3 | ping | `200` |
| 4 | `customers.json` | `{"predictions": [0, 1]}` |
| 6 | missing column | HTTP 400, `INVALID_PARAMETER_VALUE`: "Failed to enforce schema … 'support_tickets': long (required)" |
| 6 | `"two years"` | HTTP 400, `BAD_REQUEST`: "Data is not compatible with model signature. Failed to convert column tenure_months to type 'int64'" |
| 7 | `docker logs churn-prod` | one uvicorn line per request: `"POST /invocations HTTP/1.1" 200 OK`, and `400 Bad Request` for Step 6 |

## Step 5 answers (the "what if?" questions)

- **Support tickets** (24 months, €70): 0, 1, 2 tickets → 0; **3 or more → 1**.
- **Tenure** (€70, 2 tickets): **22 months or fewer → 1**; 23 or more → 0.
- **Price** (24 months, 1 ticket): up to €86 → 0; **€88 and above → 1** (the flip is around €87).

## The three reflection questions, strong answers

1. **The artefact (slide 13):** present: the model, the environment (exact versions in `requirements.txt`, the Python version in the Dockerfile), part of the documentation (`MLmodel`: signature, run id, versions), a reference to the training run. Missing: the code that trained it, the configuration in readable form, the data reference (version and hash), the model card (owner, retrain trigger), the test scenarios. Strong answers notice the run id is the thread that leads back to most of what is missing.
2. **Scale:** several copies of the box behind a load balancer, autoscaling on requests or latency, health checks (the `/ping` they used), and in practice Kubernetes or a managed service; plus monitoring of latency and errors (the logs from Step 7). For a fraud model: p95 latency under 150 ms and zero downtime, so a rollout strategy (canary or blue-green), not `docker rm` and `docker run`.
3. **Another check before going live:** any layer of the test pyramid, with a reason: a code test (the endpoint answers the two reference customers with `[0, 1]`), a data test (ranges: negative tenure is accepted by the signature but makes no sense), a model test (latency, fairness by segment, not worse than the current version). The best answers spot that the signature checks *types* but not *meaning*: `-5` months passes.

## If you use it on the forum

A simple prompt: *"Post the answer your box gave for your own customer in Step 5 (the numbers you chose and the prediction), and answer one of the three questions at the end of the lab."* It works as an optional theme, like the MLflow lab in Forum 2.
