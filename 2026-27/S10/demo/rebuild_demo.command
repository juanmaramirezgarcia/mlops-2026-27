#!/bin/bash
# Rebuilds the Session 10 demo database and evaluation pages from scratch (only if you edit the prompts, the golden
# set or the answers). Uses the Session 3 environment.
cd "$(dirname "$0")"
VENV=../../S03/demo/mlflow/.venv
[ -x "$VENV/bin/python" ] || { echo "Run S03/demo/mlflow/start_mlflow_ui.command once first (it creates the environment)."; exit 1; }
rm -rf mlflow eval_results.html eval_results.csv eval_summary.png
"$VENV/bin/python" s10_demo_setup.py && "$VENV/bin/python" render_summary.py 2>/dev/null || echo "(render_summary.py needs Pillow; the HTML page is enough)"
echo "Done. Start the UI with start_prompt_registry.command."
