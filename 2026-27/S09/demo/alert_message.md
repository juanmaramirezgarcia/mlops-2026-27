*churn-model v1.1 · monitoring run 01 Sep 15:49* — 5 alert(s)

:warning: *drifted-features* — Actual value 3.000 >= 2.000 (threshold > 2 of 7 features)
    → check the extract with the data team; if confirmed, retrain on recent data
    to: #churn-model-alerts (Slack), ML engineer

:warning: *charges-mean-shift* — Actual value 76.511 >= 70.000 (threshold > 70 EUR (reference 62))
    → ask the business what changed (pricing?); do not retrain until answered
    to: #churn-model-alerts, ML engineer; copy Product owner

:warning: *prediction-drift* — Actual value 0.116 >= 0.100 (threshold drift score >= 0.10)
    → compare by segment; investigate before labels arrive
    to: #churn-model-alerts, ML engineer

:warning: *accuracy-segment* — 1 segment < 0.70: North, tenure 3y+: 0.65 (n=349) (threshold < 0.70 in any segment with > 200 customers)
    → retrain with new labels; consider region interactions; approve
    to: ML engineer + Product owner

:rotating_light: *latency-p95* — p95 659 ms over the last 10 minutes (threshold > 500 ms for 10 minutes)
    → roll back if it followed a deployment
    to: page IT on call

Passed: missing-features, accuracy-overall, batch-late
Report: alert_checks.html · Runbook: alerts.yaml · Run: monitoring.yml #142