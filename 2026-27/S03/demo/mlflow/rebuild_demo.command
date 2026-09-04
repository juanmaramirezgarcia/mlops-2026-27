#!/bin/bash
# Rebuilds the demo database from scratch on this Mac (only if you want fresh runs).
cd "$(dirname "$0")"
[ -d .venv ] || { echo "Run start_mlflow_ui.command once first (it creates the environment)."; exit 1; }
rm -rf mlflow.db mlruns churn_demo.csv
./.venv/bin/python ../mlflow_demo_setup.py
