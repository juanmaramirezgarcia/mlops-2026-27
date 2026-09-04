"""
s7_demo_setup.py  -  builds the Session 7 demo assets. Everything is pre-rendered:
during class you only open two files in the browser.

Outputs (in the folder where you run it):
  drift_report.html     Evidently data-drift report: reference (training) vs current (this month)
  shap_waterfall.png    one customer's churn prediction, explained feature by feature
  shap_summary.png      which features matter most across all customers
  reference.csv, current.csv, churn_model.pkl   the inputs, for reproducibility (also used by s7_lime_setup.py)

Run once (the S03 mlflow venv has pandas and scikit-learn; add the two libraries):
  ./.venv/bin/pip install evidently shap matplotlib
  ./.venv/bin/python s7_demo_setup.py

The story: the churn model was trained in June (reference). In October (current) two things
changed: a new pricing plan moved monthly_charges up for many customers (data drift), and a
competitor launched fibre in the North region so long-tenure customers started leaving
(concept drift: same inputs, different behaviour). The report shows the first; the second is
invisible to a drift report and only appears when labels arrive. That contrast is the lesson.
"""
import pickle
import warnings

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")
rng = np.random.default_rng(11)
FEATURES = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "is_monthly", "region_north"]


def make(n, shift_charges=0.0, promo_shift=0, north_churn_boost=0.0):
    tenure = rng.integers(1, 72, n)
    charges = (rng.normal(62, 20, n) + shift_charges).clip(15, 160)
    tickets = rng.poisson(1.2, n)
    promo = (rng.integers(0, 4, n) + promo_shift).clip(0, 6)
    monthly = rng.random(n) < 0.6
    north = rng.random(n) < 0.25
    logit = -3.2 - 0.07 * tenure + 0.045 * charges + 0.8 * tickets + 1.6 * monthly - 0.6 * promo
    # concept drift: in the current period, long-tenure customers in the North start leaving
    logit = logit + north_churn_boost * north * (tenure > 36)
    y = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    return pd.DataFrame({"tenure_months": tenure, "monthly_charges": charges.round(2), "support_tickets": tickets,
                         "promo_weeks_last_quarter": promo, "is_monthly": monthly.astype(int),
                         "region_north": north.astype(int), "churned": y})


reference = make(6000)                                            # June: training data
current = make(3000, shift_charges=14.0, promo_shift=1, north_churn_boost=2.2)   # October: new pricing, competitor in the North
reference.to_csv("reference.csv", index=False)
current.to_csv("current.csv", index=False)

# ------------------------------------------------------------------ the model (trained in June)
Xtr, Xte, ytr, yte = train_test_split(reference[FEATURES], reference["churned"], test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=300, max_depth=8, random_state=1).fit(Xtr, ytr)
pickle.dump(model, open("churn_model.pkl", "wb"))
ref_acc = (model.predict(Xte) == yte).mean()
cur_acc = (model.predict(current[FEATURES]) == current["churned"]).mean()
north_long = current[(current.region_north == 1) & (current.tenure_months > 36)]
north_acc = (model.predict(north_long[FEATURES]) == north_long["churned"]).mean()
print(f"accuracy June (hold-out): {ref_acc:.3f} | October overall: {cur_acc:.3f} | October, North & tenure>36: {north_acc:.3f}")

reference["prediction"] = model.predict_proba(reference[FEATURES])[:, 1]
current["prediction"] = model.predict_proba(current[FEATURES])[:, 1]

# ------------------------------------------------------------------ Evidently drift report
from evidently import Report, Dataset, DataDefinition
from evidently.presets import DataDriftPreset

definition = DataDefinition(numerical_columns=["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "prediction"],
                            categorical_columns=["is_monthly", "region_north"])
ref_ds = Dataset.from_pandas(reference.drop(columns=["churned"]), data_definition=definition)
cur_ds = Dataset.from_pandas(current.drop(columns=["churned"]), data_definition=definition)
report = Report([DataDriftPreset()])
snapshot = report.run(cur_ds, ref_ds)
snapshot.save_html("drift_report.html")
print("drift_report.html written")

# ------------------------------------------------------------------ SHAP: one customer, and the summary
import shap
explainer = shap.TreeExplainer(model)
# a long-tenure North customer predicted to churn: the case a retention manager would ask about
cand = current[(current.region_north == 1) & (current.tenure_months > 36)].copy()
cand = cand.sort_values("prediction", ascending=False).head(1)
x = cand[FEATURES]
sv = explainer(x)
sv1 = sv[0, :, 1] if len(sv.shape) == 3 else sv[0]
plt.figure(figsize=(9, 5))
shap.plots.waterfall(sv1, max_display=6, show=False)
plt.title(f"Why this customer scores {float(cand['prediction'].iloc[0]):.0%} churn risk", fontsize=13, loc="left")
plt.tight_layout(); plt.savefig("shap_waterfall.png", dpi=160, bbox_inches="tight"); plt.close()

sample = current[FEATURES].sample(600, random_state=3)
svs = explainer(sample)
svs1 = svs[:, :, 1] if len(svs.shape) == 3 else svs
plt.figure(figsize=(9, 5))
shap.plots.beeswarm(svs1, max_display=6, show=False)
plt.title("What drives churn risk across customers (October)", fontsize=13, loc="left")
plt.tight_layout(); plt.savefig("shap_summary.png", dpi=160, bbox_inches="tight"); plt.close()
print("shap_waterfall.png and shap_summary.png written")

# ------------------------------------------------------------------ performance by segment: what the drift report cannot see
def acc(df):
    return (model.predict(df[FEATURES]) == df["churned"]).mean()
ref_te = reference.loc[Xte.index]
segs = {"All customers": (ref_te, current),
        "North, tenure > 36": (ref_te[(ref_te.region_north == 1) & (ref_te.tenure_months > 36)], current[(current.region_north == 1) & (current.tenure_months > 36)]),
        "North, tenure <= 36": (ref_te[(ref_te.region_north == 1) & (ref_te.tenure_months <= 36)], current[(current.region_north == 1) & (current.tenure_months <= 36)]),
        "Other regions": (ref_te[ref_te.region_north == 0], current[current.region_north == 0])}
labels = list(segs); june = [acc(v[0]) for v in segs.values()]; octo = [acc(v[1]) for v in segs.values()]
fig, ax = plt.subplots(figsize=(9, 4.6)); xs = np.arange(len(labels)); w = 0.36
ax.bar(xs - w/2, june, w, label="June (evaluation set)", color="#0E7C86"); ax.bar(xs + w/2, octo, w, label="October (labels just arrived)", color="#E07A2F")
for i, (a, b) in enumerate(zip(june, octo)):
    ax.text(i - w/2, a + 0.01, f"{a:.0%}", ha="center", fontsize=10); ax.text(i + w/2, b + 0.01, f"{b:.0%}", ha="center", fontsize=10)
ax.axhline(0.75, color="#B42318", ls="--", lw=1); ax.text(3.45, 0.722, "retrain trigger for this model: accuracy 0.75", color="#B42318", ha="right", fontsize=9)
ax.set_ylim(0.4, 1.0); ax.set_ylabel("accuracy"); ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=10); ax.legend(frameon=False, fontsize=10)
ax.set_title("Performance decay hides in a segment: same inputs, different behaviour", loc="left", fontsize=13)
for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
plt.tight_layout(); plt.savefig("performance_by_segment.png", dpi=160); plt.close()
print("performance_by_segment.png written")
print("\nOpen drift_report.html in a browser; keep the two PNGs ready. Script: MLOps_S07_Demo_Script.md")
