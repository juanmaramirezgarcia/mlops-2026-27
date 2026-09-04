#!/bin/bash
# Double-click to train one model live and log it to the demo database (Session 3, Optional C).
# Requires start_mlflow_ui.command to have been run once (it creates .venv).
cd "$(dirname "$0")"
[ -d .venv ] || { echo "Run start_mlflow_ui.command once first (it creates the environment)."; exit 1; }
echo "Training a random forest and logging the run to mlflow.db ..."
./.venv/bin/python train_with_mlflow.py "$@"
echo
echo "Now refresh the MLflow UI (Experiments -> churn-model). Press Enter to close."
read -r
