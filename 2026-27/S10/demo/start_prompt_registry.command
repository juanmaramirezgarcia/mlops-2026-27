#!/bin/bash
# Double-click in Finder (or run in Terminal) to open the Session 10 demo: MLflow's prompt registry with the two
# versions of the HR-assistant prompt and the evaluation runs. Uses the Session 3 environment (no new installs).
# Stop with Ctrl+C in the Terminal window.
cd "$(dirname "$0")"
VENV=../../S03/demo/mlflow/.venv
if [ ! -x "$VENV/bin/mlflow" ]; then
  echo "The Session 3 environment was not found at $VENV. Run S03/demo/mlflow/start_mlflow_ui.command once first."; exit 1
fi
if [ ! -f mlflow/mlflow.db ]; then
  echo "No database yet; building the demo (10 seconds)..."; "$VENV/bin/python" s10_demo_setup.py || exit 1
fi
# The database stores absolute paths from the machine that built it; point them at this folder.
"$VENV/bin/python" - <<'PY'
import sqlite3, re, os
db = sqlite3.connect("mlflow/mlflow.db"); here = os.path.abspath(".")
for table, col in (("experiments", "artifact_location"), ("runs", "artifact_uri")):
    for (val,) in db.execute(f"select distinct {col} from {table}"):
        if val and "/mlruns/" in val and not val.startswith(here):
            new = here + "/mlflow/mlruns/" + val.split("/mlruns/", 1)[1]
            db.execute(f"update {table} set {col}=? where {col}=?", (new, val))
db.commit()
PY
PORT=5002
if lsof -i :$PORT >/dev/null 2>&1; then PORT=5003; fi
echo
echo "Starting the prompt registry UI on http://127.0.0.1:$PORT/#/prompts  (about 20 seconds)"
echo "Prompts -> hr-assistant (two versions, aliases production / challenger; Compare tab)"
echo "Experiments -> hr-assistant-eval (one run per version; add metric columns with the Columns menu)"
echo "The per-question table is eval_results.html in this folder (double-click)."
echo
(sleep 20; open "http://127.0.0.1:$PORT/#/prompts") &
"$VENV/bin/mlflow" ui --backend-store-uri sqlite:///mlflow/mlflow.db --port $PORT
