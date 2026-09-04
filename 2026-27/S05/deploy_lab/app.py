"""
app.py  -  serves the churn model as a REST API with FastAPI.

Endpoints:
  GET  /health   -> {"status": "ok", "model": "churn-model"}     (for load balancers and uptime checks)
  POST /predict  -> {"churn_probability": 0.73, "churn": true, "model_version": "v1"}
  GET  /         -> a one-line hello, and a link to the automatic docs at /docs

Run locally without Docker:   uvicorn app:app --reload --port 8080   (then open http://127.0.0.1:8080/docs)
Inside the container the Dockerfile runs the same uvicorn command.
"""
import pickle
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

FEATURES = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "is_monthly", "region_north"]
MODEL = pickle.load(open(Path(__file__).resolve().parent / "churn_model.pkl", "rb"))
THRESHOLD = 0.5   # the business threshold (Video 1, segment 2): a decision, not a model property

app = FastAPI(title="TelcoNova churn API", version="1.0",
              description="Scores one customer's churn risk. A teaching example for MLOps Session 5.")


class Customer(BaseModel):
    # Pydantic validates the request: a missing or wrong-typed field is rejected with a clear 422 error.
    tenure_months: int = Field(ge=0, le=120, examples=[6])
    monthly_charges: float = Field(ge=0, examples=[85.0])
    support_tickets: int = Field(ge=0, examples=[4])
    promo_weeks_last_quarter: int = Field(ge=0, le=13, examples=[1])
    is_monthly: int = Field(ge=0, le=1, examples=[1])
    region_north: int = Field(ge=0, le=1, examples=[1])


@app.get("/")
def root():
    return {"service": "TelcoNova churn API", "docs": "/docs", "health": "/health"}


@app.get("/health")
def health():
    return {"status": "ok", "model": "churn-model", "version": app.version}


@app.post("/predict")
def predict(customer: Customer):
    row = pd.DataFrame([[getattr(customer, f) for f in FEATURES]], columns=FEATURES)
    prob = float(MODEL.predict_proba(row)[0, 1])
    return {"churn_probability": round(prob, 4), "churn": prob >= THRESHOLD,
            "threshold": THRESHOLD, "model_version": "v1"}
