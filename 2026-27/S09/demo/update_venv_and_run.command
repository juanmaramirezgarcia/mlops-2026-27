#!/bin/bash
# Double-click in Finder (or run in Terminal). Adds the Video 1 demo dependencies to the Session 3
# environment (S03/demo/mlflow/.venv) and runs the monitoring job once so you can see the output.
# First run: installs evidently (and shap, used by the Session 7 scripts); 1–3 minutes. Later runs: ~10 s.
cd "$(dirname "$0")"
VENV=../../S03/demo/mlflow/.venv
if [ ! -x "$VENV/bin/python" ]; then
  echo "The Session 3 environment was not found at $VENV."
  echo "Run 2026-27/S03/demo/mlflow/start_mlflow_ui.command once first (it creates it), then run this again."
  exit 1
fi
PY="$VENV/bin/python"
echo "Checking the environment..."
"$PY" - <<'PYCHECK'
import importlib.util, subprocess, sys
need = {"evidently": "evidently==0.7.21", "yaml": "pyyaml", "sklearn": "scikit-learn", "pandas": "pandas", "shap": "shap", "matplotlib": "matplotlib"}
missing = [pkg for mod, pkg in need.items() if importlib.util.find_spec(mod) is None]
if missing:
    print("Installing:", ", ".join(missing), "(this can take a couple of minutes)")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", *missing])
else:
    print("All packages present: evidently, pyyaml, scikit-learn, pandas, shap, matplotlib")
PYCHECK
echo
read -p "Also install LIME? Only needed to regenerate the Session 7 LIME images; not used in class. [y/N] " lime
if [ "$lime" = "y" ]; then
  "$PY" -m pip install --quiet "setuptools<70" wheel && "$PY" -m pip install --quiet lime && echo "LIME installed." || echo "LIME install failed; the pre-rendered images in S07/demo still work."
fi
echo
echo "Running the monitoring job (run_alert_checks.py)..."
echo
"$PY" run_alert_checks.py
CODE=$?
echo
echo "Exit code: $CODE   (1 = at least one rule fired; that is the expected result for the demo)"
"$PY" render_assets.py >/dev/null 2>&1 && echo "console_output.png and alert_message.png refreshed."
echo
read -p "Open alert_checks.html in the browser? [y/N] " yn
[ "$yn" = "y" ] && open alert_checks.html
echo "Done. You can close this window."
