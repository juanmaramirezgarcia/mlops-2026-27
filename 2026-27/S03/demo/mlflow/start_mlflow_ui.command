#!/bin/bash
# Double-click this file in Finder (or run it in Terminal) to start the MLflow demo UI.
# First run: creates a virtual environment in this folder and installs MLflow (2–3 minutes).
# Later runs: starts in ~20 seconds. Stop with Ctrl+C in the Terminal window.
cd "$(dirname "$0")"
if [ ! -d .venv ]; then
  echo "Creating virtual environment and installing MLflow (first time only)..."
  python3 -m venv .venv || { echo "python3 not found. Install Python 3 from python.org or via Homebrew (brew install python)."; exit 1; }
  ./.venv/bin/python -m pip install --quiet --upgrade pip
  ./.venv/bin/python -m pip install --quiet mlflow scikit-learn pandas
fi
PORT=5000
if lsof -i :$PORT >/dev/null 2>&1; then PORT=5001; fi
echo
echo "Starting MLflow UI on http://127.0.0.1:$PORT  (give it ~20 seconds, then open the address in your browser)"
echo "Experiments -> churn-model | Models -> churn-model"
echo
(sleep 20; open "http://127.0.0.1:$PORT") &
./.venv/bin/mlflow ui --backend-store-uri sqlite:///mlflow.db --port $PORT
