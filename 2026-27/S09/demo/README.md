# Video 1 · Segment 6 demo: alerts in production (TelcoNova churn model)

Everything here is pre-computed; the video only needs a terminal, an editor and a browser.

| File | Role |
|---|---|
| `alerts.yaml` | The eight rules: metric, threshold, window, severity, route, action |
| `run_alert_checks.py` | The monitoring job. Evaluates the rules; prints PASS/FIRE; writes `alert_message.md` and `alert_checks.html`; exits 1 if any rule fired |
| `monitoring.yml` | The scheduler (GitHub Actions): weekly drift checks, monthly performance checks, message only on failure |
| `reference.csv`, `current.csv`, `churn_model.pkl` | Inputs (the Session 7 demo assets) |
| `alert_checks.html` | Evidently report; open the **Tests** tab |
| `alert_message.md`, `console_output.txt` | Last run, as text |
| `*.png` | The same, rendered for the slides; `render_assets.py` regenerates the console and message images |
| `update_venv_and_run.command` | Mac launcher: installs what is missing into the Session 3 venv, runs the job, refreshes the PNGs |

## Run it

**Easiest (Mac):** double-click `update_venv_and_run.command`. It adds `evidently` (and `shap`, for the Session 7 scripts) to the Session 3 environment `S03/demo/mlflow/.venv` the first time, runs the monitoring job, refreshes the two PNGs and offers to open the report.

**By hand:**

```bash
cd S09/demo
source ../../S03/demo/mlflow/.venv/bin/activate     # already has pandas, scikit-learn, pyyaml, matplotlib
pip install evidently==0.7.21 shap                    # once
python run_alert_checks.py ; echo "exit code $?"      # ~10 s; expect 3 PASS, 5 FIRE, exit code 1
python render_assets.py                               # optional: refresh the two PNGs
```

Numbers are deterministic (fixed seeds): drifted-features 3 of 7 · charges mean 76.5 · prediction drift 0.116 · accuracy overall 0.80 (PASS) · North, tenure 3y+ 0.65 on 349 (FIRE) · p95 latency 659 ms (incident) · batch 05:42 · missing 0%.
