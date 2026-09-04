"""
mlflow_demo_setup.py  -  builds the MLflow demo for Session 3 (7 minutes, browser only).

What it creates, in the folder where you run it:
  mlflow.db        the tracking + registry database (SQLite)
  mlruns/          the logged models and files
  churn_demo.csv   the data used by the runs

Normal use (macOS): the folder S03/demo/mlflow/ already contains the built database.
  Start the UI with start_mlflow_ui.command (double-click); reset the demo after
  registering or promoting models live with rebuild_demo.command.

Manual use (any OS), from an empty folder:
  pip install mlflow scikit-learn pandas          # if not installed
  python mlflow_demo_setup.py                     # ~30 s
  mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000
  -> http://127.0.0.1:5000

The story the runs tell (see MLOps_S03_Demo_Script.md):
  experiment "churn-model"
    run 1  logistic regression, 3 features        accuracy ~0.81  <- registered as version 1, alias "production"
    run 2  logistic regression, 4 features        accuracy ~0.82
    run 3  random forest, 100 trees               accuracy ~0.82
    run 4  random forest, 300 trees, depth 8      accuracy ~0.83  <- registered as version 2, alias "challenger"
    run 5  same model on a broken extract (60% of tenure_months empty, read as 0)
           accuracy ~0.80: the metric barely moves, only the validation check catches it.
           Tagged "rejected: data validation failed"
"""
import os
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
from mlflow import MlflowClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")
HERE = Path.cwd()
# Relative paths on purpose: the folder can be moved or copied and still work,
# as long as `mlflow ui` is started from inside it.
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# ------------------------------------------------------------------ data
rng = np.random.default_rng(3)
n = 4000
tenure = rng.integers(1, 72, n)
charges = rng.normal(62, 20, n).clip(15, 130)
tickets = rng.poisson(1.2, n)
promo = rng.integers(0, 4, n)
monthly = rng.random(n) < 0.6
logit = -3.2 - 0.07 * tenure + 0.045 * charges + 0.8 * tickets + 1.6 * monthly - 0.6 * promo
y = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
df = pd.DataFrame({"tenure_months": tenure, "monthly_charges": charges.round(2), "support_tickets": tickets,
                   "promo_weeks_last_quarter": promo, "is_monthly": monthly.astype(int), "churned": y})
df.to_csv("churn_demo.csv", index=False)

F3 = ["tenure_months", "monthly_charges", "support_tickets"]
F4 = F3 + ["promo_weeks_last_quarter"]
F5 = F4 + ["is_monthly"]

def split(frame, feats):
    return train_test_split(frame[feats], frame["churned"], test_size=0.3, random_state=42)

# ------------------------------------------------------------------ experiment
exp_name = "churn-model"
client = MlflowClient()
if client.get_experiment_by_name(exp_name) is None:
    client.create_experiment(exp_name, artifact_location="mlruns/churn-model")
mlflow.set_experiment(exp_name)

def log_run(name, model, feats, frame, params, tags, data_version):
    Xtr, Xte, ytr, yte = split(frame, feats)
    with mlflow.start_run(run_name=name) as run:
        model.fit(Xtr, ytr)
        pred = model.predict(Xte)
        proba = model.predict_proba(Xte)[:, 1]
        mlflow.log_params({**params, "n_features": len(feats), "features": ",".join(feats),
                           "train_rows": len(Xtr), "data_version": data_version})
        mlflow.log_metrics({"accuracy": round(accuracy_score(yte, pred), 4),
                            "roc_auc": round(roc_auc_score(yte, proba), 4)})
        mlflow.set_tags({"owner": "ML engineer, Data Platform", "requested_by": "Customer Retention", **tags})
        mlflow.sklearn.log_model(model, name="model", input_example=Xtr.head(3))
        print(f"{name:42s} accuracy={accuracy_score(yte, pred):.3f}")
        return run.info.run_id

r1 = log_run("lr-3-features", LogisticRegression(max_iter=1000), F3, df,
             {"algorithm": "LogisticRegression", "max_iter": 1000}, {"stage_note": "first baseline, March"}, "extract-2026-03-01")
r2 = log_run("lr-4-features-promo", LogisticRegression(max_iter=1000), F4, df,
             {"algorithm": "LogisticRegression", "max_iter": 1000}, {"stage_note": "adds promotions feature"}, "extract-2026-06-01")
r3 = log_run("rf-100", RandomForestClassifier(n_estimators=100, random_state=1), F5, df,
             {"algorithm": "RandomForest", "n_estimators": 100, "max_depth": "None"}, {}, "extract-2026-06-01")
r4 = log_run("rf-300-depth8", RandomForestClassifier(n_estimators=300, max_depth=8, random_state=1), F5, df,
             {"algorithm": "RandomForest", "n_estimators": 300, "max_depth": 8}, {"stage_note": "candidate for production"}, "extract-2026-06-01")

# a run on a broken extract: tenure_months mostly empty and filled with 0 (the NorthRetail bug)
bad = df.copy()
bad.loc[rng.random(n) < 0.6, "tenure_months"] = 0
r5 = log_run("rf-300-depth8-extract-0612", RandomForestClassifier(n_estimators=300, max_depth=8, random_state=1), F5, bad,
             {"algorithm": "RandomForest", "n_estimators": 300, "max_depth": 8},
             {"rejected": "data validation failed: 60% of tenure_months empty, read as 0"}, "extract-2026-06-12")

# ------------------------------------------------------------------ registry
model_name = "churn-model"
try:
    client.create_registered_model(model_name, description="Customer churn model for the retention campaign. Owner: Customer Retention (accountable), Data Platform (responsible).")
except Exception:
    pass
v1 = client.create_model_version(model_name, f"runs:/{r1}/model", r1, description="v1.0 - baseline, 3 features. In production since 3 March 2026.")
v2 = client.create_model_version(model_name, f"runs:/{r4}/model", r4, description="v1.1 candidate - random forest, 5 features. Passed validation on 9 June; awaiting sign-off.")
client.set_registered_model_alias(model_name, "production", v1.version)
client.set_registered_model_alias(model_name, "challenger", v2.version)
client.set_model_version_tag(model_name, v1.version, "approved_by", "Product owner, 3 March 2026")
client.set_model_version_tag(model_name, v2.version, "validation", "passed 9 June 2026; fairness check pending")

# ------------------------------------------------------------------ relocation (optional)
# MLflow stores absolute paths for artifacts. If this folder will be served from a
# different location than where the script ran (for example built on one machine,
# copied to another), set MLFLOW_DEMO_TARGET_DIR to the final folder and the stored
# paths are rewritten. Not needed when you run the script in its final folder.
target = os.environ.get("MLFLOW_DEMO_TARGET_DIR")
if target:
    import sqlite3
    src_prefix, dst_prefix = str(HERE), str(Path(target))
    con = sqlite3.connect("mlflow.db")
    cur = con.cursor()
    n = 0
    for (tbl,) in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
        cols = [r[1] for r in cur.execute(f"PRAGMA table_info('{tbl}')").fetchall() if (r[2] or "").upper().startswith(("VARCHAR", "TEXT", "CHAR"))]
        for c in cols:
            n += cur.execute(f"UPDATE '{tbl}' SET \"{c}\" = REPLACE(\"{c}\", ?, ?) WHERE \"{c}\" LIKE ?", (src_prefix, dst_prefix, f"%{src_prefix}%")).rowcount
    con.commit(); con.close()
    print(f"Rewrote {n} stored paths from {src_prefix} to {dst_prefix}")

print("\nDone. Start the UI from this folder with:\n  mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000\nthen open http://127.0.0.1:5000")
