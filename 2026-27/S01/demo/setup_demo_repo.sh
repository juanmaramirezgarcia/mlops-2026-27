#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup_demo_repo.sh
# Builds a small Git repository with a readable history for the Session 1
# demo ("every change has an author, a date and a reason").
#
# Usage:
#   bash setup_demo_repo.sh                # creates ./mlops-demo-churn
#   bash setup_demo_repo.sh my-folder      # custom folder name
#
# Then publish it (once):
#   1. Create an EMPTY public repo on GitHub, e.g. juanmaramirezgarcia/mlops-demo-churn
#      (no README, no .gitignore, no licence: the script creates them).
#   2. cd mlops-demo-churn
#      git remote add origin https://github.com/juanmaramirezgarcia/mlops-demo-churn.git
#      git push -u origin main --tags
#
# BACKDATE: when "yes", the commits are dated across Jan–Jun 2026 so the
# history reads like a real project (the tag v1.0 lands on 3 March, matching
# the slide). Set BACKDATE=no for real timestamps.
# ---------------------------------------------------------------------------
set -euo pipefail

REPO_DIR="${1:-mlops-demo-churn}"
BACKDATE="${BACKDATE:-yes}"
AUTHOR_NAME="${AUTHOR_NAME:-Juan Ramírez}"
AUTHOR_EMAIL="${AUTHOR_EMAIL:-jramirezg@faculty.ie.edu}"

if [ -e "$REPO_DIR" ]; then
  echo "Folder '$REPO_DIR' already exists. Remove it or pass another name." >&2
  exit 1
fi

mkdir -p "$REPO_DIR"
cd "$REPO_DIR"
git init -q -b main
git config user.name "$AUTHOR_NAME"
git config user.email "$AUTHOR_EMAIL"

# commit <date> <message...>  — date only used when BACKDATE=yes
commit() {
  local when="$1"; shift
  git add -A
  if [ "$BACKDATE" = "yes" ]; then
    GIT_AUTHOR_DATE="$when" GIT_COMMITTER_DATE="$when" git commit -q -m "$@"
  else
    git commit -q -m "$@"
  fi
}

# tag <date> <name> <message>
tag() {
  local when="$1" name="$2" msg="$3"
  if [ "$BACKDATE" = "yes" ]; then
    GIT_COMMITTER_DATE="$when" git tag -a "$name" -m "$msg"
  else
    git tag -a "$name" -m "$msg"
  fi
}

# ---------------------------------------------------------------------------
# Commit 1 · the first version of the model, as a data scientist would leave it
# ---------------------------------------------------------------------------
mkdir -p data src tests
cat > README.md <<'EOF'
# Customer churn model — demo repository

A deliberately small project used in the MLOps course (IE, Master in Business
Analytics and Big Data) to show what *versioning* looks like:

* every change is a **commit** with an author, a date and a message that says why;
* any two moments can be compared (a **diff**);
* a **tag** names the version that went to production.

Nothing here is meant to be a good model. It is meant to have a readable history.
EOF

cat > data/churn_sample.csv <<'EOF'
customer_id,tenure_months,monthly_charges,contract_type,support_tickets,churned
1001,24,55.2,annual,0,0
1002,3,89.9,monthly,4,1
1003,48,42.0,annual,1,0
1004,1,99.5,monthly,6,1
1005,12,60.0,monthly,2,0
1006,36,70.3,annual,0,0
1007,2,95.0,monthly,5,1
1008,60,38.4,annual,1,0
1009,6,80.0,monthly,3,1
1010,18,65.5,monthly,1,0
EOF

cat > src/train.py <<'EOF'
"""Train the churn model and save it to models/churn.pkl.  Run from the repo root: python src/train.py"""
import pickle
import sys
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

FEATURES = ["tenure_months", "monthly_charges", "support_tickets"]


def load_data(path: Path = ROOT / "data" / "churn_sample.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def train(df: pd.DataFrame) -> LogisticRegression:
    model = LogisticRegression(max_iter=500)
    model.fit(df[FEATURES], df["churned"])
    return model


if __name__ == "__main__":
    df = load_data()
    model = train(df)
    (ROOT / "models").mkdir(exist_ok=True)
    with open(ROOT / "models" / "churn.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model trained on", len(df), "customers")
EOF

cat > requirements.txt <<'EOF'
pandas>=2.0
scikit-learn>=1.3
pytest>=7.0
EOF

cat > .gitignore <<'EOF'
models/
__pycache__/
.pytest_cache/
EOF

commit "2026-01-14T10:12:00+01:00" "Add churn model: training script and sample data

First version of the churn model delivered by the data-science team.
Logistic regression on three features; accuracy 0.91 on last year's data."

# ---------------------------------------------------------------------------
# Commit 2 · data validation is added: the pipeline stops if the data is wrong
# ---------------------------------------------------------------------------
cat > src/validate.py <<'EOF'
"""Data validation: stop the pipeline before training if the data is not what we expect."""
import pandas as pd

REQUIRED_COLUMNS = ["customer_id", "tenure_months", "monthly_charges", "support_tickets", "churned"]


class DataValidationError(Exception):
    """Raised when the incoming data does not match the expected schema."""


def validate(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    if len(df) == 0:
        raise DataValidationError("Dataset is empty")
EOF

python3 - <<'EOF'
import re, pathlib
p = pathlib.Path("src/train.py")
s = p.read_text()
s = s.replace('sys.path.insert(0, str(ROOT / "src"))\n',
              'sys.path.insert(0, str(ROOT / "src"))\nfrom validate import validate  # noqa: E402\n')
s = s.replace("    df = load_data()\n    model = train(df)",
              "    df = load_data()\n    validate(df)\n    model = train(df)")
p.write_text(s)
EOF

commit "2026-02-02T17:40:00+01:00" "Add data validation: stop training if required columns are missing

Before this change a file with a different schema would train a model
silently. Now the pipeline fails loudly and nothing is deployed."

# ---------------------------------------------------------------------------
# Commit 3 · the NorthRetail bug: empty values were read as zero
# ---------------------------------------------------------------------------
python3 - <<'EOF'
import pathlib
p = pathlib.Path("src/validate.py")
s = p.read_text()
s = s.replace('''    if len(df) == 0:
        raise DataValidationError("Dataset is empty")
''', '''    if len(df) == 0:
        raise DataValidationError("Dataset is empty")

    # Empty numeric values used to be filled with 0 downstream, which the model
    # read as "a customer with zero months of tenure". Reject them instead.
    numeric = ["tenure_months", "monthly_charges", "support_tickets"]
    empty_share = df[numeric].isna().mean()
    too_empty = empty_share[empty_share > 0.05]
    if not too_empty.empty:
        raise DataValidationError(
            f"More than 5% empty values in: {too_empty.index.tolist()} "
            f"({too_empty.round(2).to_dict()}). Check the upstream extract."
        )
''')
p.write_text(s)
EOF

commit "2026-02-19T09:05:00+01:00" "Fix: reject extracts where a feature arrives mostly empty

After the supplier system change on 12 Feb, tenure_months arrived empty for
a third of customers and was read as 0. Validation now fails if more than
5% of any numeric feature is empty, so the model is not retrained on it."

# ---------------------------------------------------------------------------
# Commit 4 · tests for the validation rules
# ---------------------------------------------------------------------------
cat > tests/test_validate.py <<'EOF'
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from validate import DataValidationError, validate  # noqa: E402


def good_df():
    return pd.DataFrame({
        "customer_id": [1, 2, 3, 4],
        "tenure_months": [1.0, 12.0, 24.0, 36.0],
        "monthly_charges": [90.0, 60.0, 55.0, 40.0],
        "support_tickets": [5, 2, 1, 0],
        "churned": [1, 0, 0, 0],
    })


def test_good_data_passes():
    validate(good_df())


def test_missing_column_fails():
    df = good_df().drop(columns=["support_tickets"])
    with pytest.raises(DataValidationError):
        validate(df)


def test_mostly_empty_feature_fails():
    df = good_df()
    df.loc[:, "tenure_months"] = np.nan
    with pytest.raises(DataValidationError):
        validate(df)
EOF

commit "2026-02-20T11:30:00+01:00" "Add tests for the validation rules

Three tests: good data passes, a missing column fails, a mostly-empty
feature fails. They run before every training."

# ---------------------------------------------------------------------------
# Commit 5 · a model card, then the first production tag
# ---------------------------------------------------------------------------
cat > MODEL_CARD.md <<'EOF'
# Model card — churn model

| | |
|---|---|
| **Version** | 1.0 |
| **Trained on** | data/churn_sample.csv, extract of 1 March 2026 |
| **Algorithm** | Logistic regression, 3 features |
| **Accuracy (hold-out)** | 0.91 |
| **Owner (accountable)** | Product owner, Customer Retention |
| **Maintainer (responsible)** | ML engineer, Data Platform team |
| **Monitoring** | Weekly: share of empty features, churn rate vs. prediction |
| **Retrain trigger** | Accuracy below 0.85 on the monthly labelled sample |
EOF

commit "2026-03-03T16:20:00+01:00" "Add model card with owner, training data and retrain trigger

Required before the first production release: who is accountable, what
data the model was trained on, and when it must be retrained."

tag "2026-03-03T16:30:00+01:00" v1.0 "v1.0 — first production release, 3 March 2026"

# ---------------------------------------------------------------------------
# Commit 6 · retrained with a new feature, second tag
# ---------------------------------------------------------------------------
python3 - <<'EOF'
import pathlib
p = pathlib.Path("src/train.py")
s = p.read_text()
s = s.replace('FEATURES = ["tenure_months", "monthly_charges", "support_tickets"]',
              'FEATURES = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter"]')
p.write_text(s)

d = pathlib.Path("data/churn_sample.csv")
rows = d.read_text().strip().split("\n")
promo = ["promo_weeks_last_quarter", "2", "0", "3", "0", "1", "2", "0", "3", "1", "1"]
rows = [r + "," + v for r, v in zip(rows, promo)]
d.write_text("\n".join(rows) + "\n")

v = pathlib.Path("src/validate.py")
s = v.read_text()
s = s.replace('REQUIRED_COLUMNS = ["customer_id", "tenure_months", "monthly_charges", "support_tickets", "churned"]',
              'REQUIRED_COLUMNS = ["customer_id", "tenure_months", "monthly_charges", "support_tickets",\n                    "promo_weeks_last_quarter", "churned"]')
s = s.replace('numeric = ["tenure_months", "monthly_charges", "support_tickets"]',
              'numeric = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter"]')
v.write_text(s)

t = pathlib.Path("tests/test_validate.py")
s = t.read_text()
s = s.replace('        "support_tickets": [5, 2, 1, 0],\n',
              '        "support_tickets": [5, 2, 1, 0],\n        "promo_weeks_last_quarter": [0, 2, 1, 3],\n')
t.write_text(s)

m = pathlib.Path("MODEL_CARD.md")
s = m.read_text()
s = s.replace("| **Version** | 1.0 |", "| **Version** | 1.1 |")
s = s.replace("extract of 1 March 2026", "extract of 1 June 2026")
s = s.replace("Logistic regression, 3 features", "Logistic regression, 4 features (adds promotions)")
s = s.replace("| **Accuracy (hold-out)** | 0.91 |", "| **Accuracy (hold-out)** | 0.93 |")
m.write_text(s)
EOF

commit "2026-06-09T14:45:00+02:00" "Retrain on Q2 data and add promotion feature (v1.1)

Commercial moved to weekly promotions in March; the v1.0 model did not know.
Adds promo_weeks_last_quarter, retrains on the June extract, accuracy 0.93.
Validation rules, tests and model card updated."

tag "2026-06-09T15:00:00+02:00" v1.1 "v1.1 — retrained with promotion feature, 9 June 2026"

# ---------------------------------------------------------------------------
# Commit 7 · CI: tests run on every push (used again in Session 5)
# ---------------------------------------------------------------------------
mkdir -p .github/workflows
cat > .github/workflows/ci.yml <<'EOF'
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python -m pytest -q
      - run: python src/train.py
EOF

commit "2026-06-10T09:00:00+02:00" "Add CI: run the tests and a training dry-run on every push

Nobody has to remember to run the tests: GitHub runs them and shows a
green tick or a red cross next to every commit."

echo
echo "Repository created in: $(pwd)"
echo
git log --oneline --decorate
echo
echo "Next: create an empty public repo on GitHub, then"
echo "  git remote add origin https://github.com/<user>/mlops-demo-churn.git"
echo "  git push -u origin main --tags"
