"""
train.py  -  trains the small churn model the deploy lab serves, and saves churn_model.pkl.

Self-contained: it makes a synthetic dataset with the course's churn features (the same ones used in
Sessions 1, 3, 5, 7 and Video 1), fits a small scikit-learn pipeline, and saves it. No external data,
no internet. Run once before building the container:  python train.py
"""
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

HERE = Path(__file__).resolve().parent
FEATURES = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "is_monthly", "region_north"]

rng = np.random.default_rng(42)
n = 4000
df = pd.DataFrame({
    "tenure_months": rng.integers(1, 72, n),
    "monthly_charges": rng.normal(62, 18, n).clip(15, 140).round(2),
    "support_tickets": rng.poisson(1.2, n),
    "promo_weeks_last_quarter": rng.integers(0, 13, n),
    "is_monthly": rng.integers(0, 2, n),
    "region_north": rng.integers(0, 2, n),
})
# a churn signal the model can learn: short tenure, many tickets, high charges, monthly contract raise risk
logit = (-1.0 + 1.6 * df.is_monthly + 0.55 * df.support_tickets
         + 0.03 * (df.monthly_charges - 62) - 0.06 * df.tenure_months + 0.6 * df.region_north)
df["churned"] = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)

model = Pipeline([("rf", RandomForestClassifier(n_estimators=120, max_depth=7, random_state=42))])
model.fit(df[FEATURES], df["churned"])
acc = (model.predict(df[FEATURES]) == df["churned"]).mean()
pickle.dump(model, open(HERE / "churn_model.pkl", "wb"))
print(f"churn_model.pkl written  ·  {len(df)} rows  ·  train accuracy {acc:.2f}  ·  features {FEATURES}")
