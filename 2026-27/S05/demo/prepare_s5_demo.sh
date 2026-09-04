#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# prepare_s5_demo.sh  -  prepares the GitHub Actions demo for Session 5.
#
# Run this ONCE, a few days before Session 5, inside your local clone of the
# demo repository (the folder that contains src/, tests/, .github/):
#
#   cd "/Users/juanramirez/Documents/JM new/MLOps Rev2026/2026-27/S01/demo/mlops-demo-churn"
#   bash "../../../S05/demo/prepare_s5_demo.sh"
#
# What it does (two commits on main, one new branch):
#   1. Names the CI steps so the Actions page reads like the slide:
#        "Tests on code" -> "Validate data" -> "Train and evaluate" -> "Model card present"
#      and adds src/check_data.py, a tiny script that runs the validation rules on
#      data/churn_sample.csv (that is the "Validate data" step).
#   2. Pushes main: a GREEN run appears on GitHub.
#   3. Creates the branch  extract-2026-10-12  where data/churn_sample.csv has
#      tenure_months empty for most customers (the NorthRetail bug), pushes it,
#      and prints the link to open a pull request: a RED run appears, failing at
#      "Validate data". Nothing is merged; main stays green.
#
# Needs: git with push access to the repo (you set that up in Session 1).
# ---------------------------------------------------------------------------
set -euo pipefail

if [ ! -f src/validate.py ] || [ ! -d .github/workflows ]; then
  echo "Run this inside the mlops-demo-churn repository folder (src/validate.py not found here)." >&2
  exit 1
fi
git diff --quiet || { echo "You have uncommitted changes; commit or discard them first." >&2; exit 1; }
git checkout -q main
git pull -q --ff-only origin main || true

# ---------------------------------------------------------------- 1. named CI steps + data check
cat > src/check_data.py <<'EOF'
"""Run the data validation rules on the training extract. Exit code 1 stops the pipeline."""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import DataValidationError, validate  # noqa: E402

path = Path(__file__).resolve().parents[1] / "data" / "churn_sample.csv"
df = pd.read_csv(path)
try:
    validate(df)
except DataValidationError as err:
    print(f"DATA VALIDATION FAILED: {err}")
    sys.exit(1)
print(f"Data validation passed: {len(df)} rows, {df.shape[1]} columns, no missing columns, no mostly-empty features.")
EOF

cat > .github/workflows/ci.yml <<'EOF'
name: ci
on: [push, pull_request]
jobs:
  pipeline:
    runs-on: ubuntu-latest
    steps:
      - name: Check out the code
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Tests on code
        run: python -m pytest -q
      - name: Validate data
        run: python src/check_data.py
      - name: Train and evaluate
        run: python src/train.py
      - name: Model card present
        run: test -f MODEL_CARD.md && grep -q "Owner" MODEL_CARD.md
EOF

git add -A
git commit -q -m "Name the CI steps and add a data validation step

The pipeline now reads: tests on code -> validate data -> train and evaluate
-> model card present. check_data.py runs the validation rules on the
training extract and stops the pipeline if they fail."
git push -q origin main
echo "Pushed main: a green run should appear at https://github.com/juanmaramirezgarcia/mlops-demo-churn/actions"

# ---------------------------------------------------------------- 2. broken-extract branch
BRANCH="extract-2026-10-12"
git branch -D "$BRANCH" >/dev/null 2>&1 || true
git checkout -q -b "$BRANCH"
python3 - <<'EOF'
import csv, random
random.seed(4)
rows = list(csv.DictReader(open("data/churn_sample.csv")))
for r in rows:
    if random.random() < 0.7:
        r["tenure_months"] = ""            # the supplier feed dropped the field
with open("data/churn_sample.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
EOF
git add -A
git commit -q -m "Load the 12 October extract from the new supplier feed

Automated weekly extract. NOTE: the supplier changed the customer schema;
tenure_months is missing for most rows."
git push -q -f origin "$BRANCH"
git checkout -q main

echo
echo "Pushed branch $BRANCH: a RED run should appear, failing at 'Validate data'."
echo "Optional but recommended for the demo: open a pull request for it (do NOT merge):"
echo "  https://github.com/juanmaramirezgarcia/mlops-demo-churn/compare/main...$BRANCH"
echo
echo "Demo tabs:"
echo "  green run : https://github.com/juanmaramirezgarcia/mlops-demo-churn/actions"
echo "  red run   : same page, filter by branch $BRANCH, or the pull request's Checks tab"
