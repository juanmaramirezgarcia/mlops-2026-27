"""
train_with_mlflow.py  -  a plain training script, plus the eight lines that give it a memory.

Every line marked  # [MLflow]  is what turns a script that "trains a model" into a run
that is logged, comparable, taggable and registrable. Remove those lines and you have
Maria's notebook, in a file.

Run from the S03/demo/mlflow/ folder (the UI reads the same mlflow.db):

    ./.venv/bin/python train_with_mlflow.py                       # random forest, default settings
    ./.venv/bin/python train_with_mlflow.py --algorithm lr        # logistic regression
    ./.venv/bin/python train_with_mlflow.py --n-estimators 500 --max-depth 6
    ./.venv/bin/python train_with_mlflow.py --register            # also create a new version in the registry

Refresh the MLflow UI: a new row appears in Experiments -> churn-model (and, with --register,
a new version in Models -> churn-model).
"""
import argparse
import subprocess
from datetime import date

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

import mlflow                                                    # [MLflow] the library
import mlflow.sklearn                                            # [MLflow] knows how to save scikit-learn models

# ------------------------------------------------------------------ settings from the command line
parser = argparse.ArgumentParser()
parser.add_argument("--algorithm", choices=["rf", "lr"], default="rf")
parser.add_argument("--n-estimators", type=int, default=200)
parser.add_argument("--max-depth", type=int, default=6)
parser.add_argument("--data", default="churn_demo.csv")
parser.add_argument("--data-version", default="extract-2026-06-01")
parser.add_argument("--register", action="store_true", help="also create a new version of 'churn-model' in the registry")
args = parser.parse_args()

FEATURES = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "is_monthly"]
TARGET = "churned"


def git_commit() -> str:
    """The code version, if this folder is inside a git repository; 'not versioned' otherwise."""
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return "not versioned"


# ------------------------------------------------------------------ 1. load
df = pd.read_csv(args.data)

# ------------------------------------------------------------------ 2. validate (stop before training if the data is wrong)
missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
if missing:
    raise SystemExit(f"Data validation failed: missing columns {missing}")
empty_share = df[FEATURES].isna().mean()
if (empty_share > 0.05).any():
    raise SystemExit(f"Data validation failed: more than 5% empty values in {empty_share[empty_share > 0.05].index.tolist()}")

# ------------------------------------------------------------------ 3. split once, with a fixed seed
X_train, X_test, y_train, y_test = train_test_split(df[FEATURES], df[TARGET], test_size=0.3, random_state=42)

# ------------------------------------------------------------------ 4. choose the model
if args.algorithm == "rf":
    model = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, random_state=1)
    params = {"algorithm": "RandomForest", "n_estimators": args.n_estimators, "max_depth": args.max_depth}
else:
    model = LogisticRegression(max_iter=1000)
    params = {"algorithm": "LogisticRegression", "max_iter": 1000}

# ------------------------------------------------------------------ 5. train, evaluate, and remember
mlflow.set_tracking_uri("sqlite:///mlflow.db")                   # [MLflow] where the memory lives (same file the UI reads)
mlflow.set_experiment("churn-model")                             # [MLflow] which experiment this run belongs to

with mlflow.start_run(run_name=f"{args.algorithm}-live-{date.today():%d%b}"):   # [MLflow] one run = one attempt
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

    mlflow.log_params({**params, "features": ",".join(FEATURES), "train_rows": len(X_train),
                       "data_version": args.data_version, "code_version": git_commit()})   # [MLflow] the settings: what was tried
    mlflow.log_metrics({"accuracy": round(accuracy, 4), "roc_auc": round(roc_auc, 4)})    # [MLflow] the result: how good it was
    mlflow.set_tags({"owner": "ML engineer, Data Platform",                                  # [MLflow] the context: who, for whom, why
                     "requested_by": "Customer Retention",
                     "stage_note": "trained live in Session 3"})
    mlflow.sklearn.log_model(model, name="model", input_example=X_train.head(3))            # [MLflow] the model file itself, with an example input

    print(f"Run logged: {params['algorithm']}  accuracy={accuracy:.3f}  roc_auc={roc_auc:.3f}")

    if args.register:                                                                        # [MLflow] optional: put it on the shortlist
        run_id = mlflow.active_run().info.run_id
        version = mlflow.register_model(f"runs:/{run_id}/model", "churn-model")
        print(f"Registered as churn-model version {version.version}: no alias, no owner, no approval yet.")

print("Refresh the MLflow UI: Experiments -> churn-model")
