"""
run_alert_checks.py  -  the "monitoring job" of Video 1: evaluates the rules in alerts.yaml against
this month's data and produces (a) a console report, (b) a Slack-style alert message, (c) an Evidently
test report (alert_checks.html) with one PASS/FAIL row per rule that Evidently can evaluate.

Inputs (same folder):  reference.csv, current.csv, churn_model.pkl  (copied from S07/demo),
                       latency_log.csv (generated here if missing), alerts.yaml
Outputs:               alert_checks.html, alert_message.md, console_output.txt, exit code 1 if any rule fired

In production this script is not run by hand: a scheduler runs it (cron, Airflow, GitHub Actions on a
schedule) and the exit code / the message are what page a person. See monitoring.yml next to this file.

Install (once):  pip install evidently scikit-learn pandas pyyaml
"""
import io
import pickle
import sys
import warnings
from contextlib import redirect_stdout
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

warnings.filterwarnings("ignore")   # the model was pickled with an older scikit-learn; predictions are identical, the warning would clutter the recording
HERE = Path(__file__).resolve().parent
F = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "is_monthly", "region_north"]
buf = io.StringIO()


def main():
    rules = {r["id"]: r for r in yaml.safe_load(open(HERE / "alerts.yaml"))["rules"]}
    ref = pd.read_csv(HERE / "reference.csv"); cur = pd.read_csv(HERE / "current.csv")
    model = pickle.load(open(HERE / "churn_model.pkl", "rb"))
    ref["prediction"] = model.predict_proba(ref[F])[:, 1]
    cur["prediction"] = model.predict_proba(cur[F])[:, 1]

    # a simulated latency log for the online endpoint (last 10 minutes): mostly fast, a slow tail after a deployment
    rng = np.random.default_rng(2)
    lat = np.concatenate([rng.gamma(4, 20, 1800), rng.gamma(6, 120, 200)])
    p95 = float(np.percentile(lat, 95))

    fired = []   # (rule_id, actual, threshold, severity, route, action)
    ok = []

    def check(rule_id, condition, actual):
        r = rules[rule_id]
        (fired if condition else ok).append((rule_id, actual, r["threshold"], r["severity"], r["route"], r["action"]))

    # ------------------------------------------------------------ Evidently: drift and missing values, as tests
    from evidently import Report, Dataset, DataDefinition
    from evidently.metrics import DriftedColumnsCount, ValueDrift, MissingValueCount, MeanValue
    from evidently.tests import lt, lte
    d = DataDefinition(numerical_columns=["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "prediction"],
                       categorical_columns=["is_monthly", "region_north"])
    rds = Dataset.from_pandas(ref.drop(columns=["churned"]), data_definition=d)
    cds = Dataset.from_pandas(cur.drop(columns=["churned"]), data_definition=d)
    report = Report([
        DriftedColumnsCount(tests=[lte(2)]),                       # drifted-features: no more than 2 of 7
        MeanValue(column="monthly_charges", tests=[lte(70)]),      # charges-mean-shift
        MissingValueCount(column="tenure_months", tests=[lte(0.05)]),  # missing-features
        ValueDrift(column="prediction", tests=[lt(0.10)]),        # prediction-drift
    ])
    snap = report.run(cds, rds)
    snap.save_html(str(HERE / "alert_checks.html"))
    tests = snap.dict()["tests"]
    status = {t["name"].split(":")[0]: (str(t["status"]).endswith("FAIL"), t["description"]) for t in tests}

    def ev(prefix):
        for k, v in status.items():
            if k.startswith(prefix):
                return v
        return (False, "n/a")

    f, desc = ev("Count of Drifted Columns");   check("drifted-features", f, desc.split(":")[-1].strip())
    f, desc = ev("Mean value of 'monthly_charges'"); check("charges-mean-shift", f, desc.split(":")[-1].strip())
    f, desc = ev("Column 'tenure_months' missing"); check("missing-features", f, desc.split(":")[-1].strip())
    f, desc = ev("Value drift for prediction");  check("prediction-drift", f, desc.split(":")[-1].strip())

    # ------------------------------------------------------------ performance: labels for the month have arrived
    acc_all = float((model.predict(cur[F]) == cur["churned"]).mean())
    check("accuracy-overall", acc_all < 0.75, f"accuracy {acc_all:.2f}")
    cur["tenure_band"] = pd.cut(cur["tenure_months"], [0, 12, 36, 100], labels=["0-1y", "1-3y", "3y+"])
    seg = cur.assign(correct=(model.predict(cur[F]) == cur["churned"])).groupby(["region_north", "tenure_band"], observed=True)["correct"].agg(["mean", "size"])
    bad = seg[(seg["size"] > 200) & (seg["mean"] < 0.70)]
    worst = seg[seg["size"] > 200]["mean"].idxmin()
    region = "North" if worst[0] == 1 else "rest"
    check("accuracy-segment", len(bad) > 0, f"{len(bad)} segment < 0.70: {region}, tenure {worst[1]}: {seg.loc[worst, 'mean']:.2f} (n={int(seg.loc[worst, 'size'])})")

    # ------------------------------------------------------------ operational
    finished = datetime.now().replace(hour=5, minute=42)
    check("batch-late", finished.hour >= 6, f"finished {finished:%H:%M}")
    check("latency-p95", p95 > 500, f"p95 {p95:.0f} ms over the last 10 minutes")

    # ------------------------------------------------------------ console report
    print(f"MONITORING RUN  ·  churn-model v1.1  ·  {datetime.now():%Y-%m-%d %H:%M}  ·  reference: June extract")
    print("-" * 96)
    for rid, actual, thr, sev, route, action in ok:
        print(f"  PASS  {rid:20s} {actual:45s} threshold {thr}")
    for rid, actual, thr, sev, route, action in fired:
        print(f"  FIRE  {rid:20s} {actual:45s} threshold {thr}   [{sev}]")
    print("-" * 96)
    inc = [x for x in fired if x[3] == "incident"]
    print(f"  {len(fired)} rule(s) fired ({len(inc)} incident, {len(fired) - len(inc)} trend); {len(ok)} passed. Report: alert_checks.html")

    # ------------------------------------------------------------ the message a person receives
    lines = [f"*churn-model v1.1 · monitoring run {datetime.now():%d %b %H:%M}* — {len(fired)} alert(s)", ""]
    for rid, actual, thr, sev, route, action in fired:
        icon = ":rotating_light:" if sev == "incident" else ":warning:"
        lines += [f"{icon} *{rid}* — {actual} (threshold {thr})", f"    → {action}", f"    to: {route}", ""]
    lines += [f"Passed: {', '.join(x[0] for x in ok) or 'none'}", "Report: alert_checks.html · Runbook: alerts.yaml · Run: monitoring.yml #142"]
    (HERE / "alert_message.md").write_text("\n".join(lines))
    return 1 if fired else 0


with redirect_stdout(buf):
    code = main()
out = buf.getvalue()
print(out)
(HERE / "console_output.txt").write_text(out)
sys.exit(code)
