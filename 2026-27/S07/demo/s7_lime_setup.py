"""
s7_lime_setup.py  -  builds the LIME assets for the Session 7 demo. Pre-rendered; browser only in class.

Run AFTER s7_demo_setup.py, in the same folder (it reuses reference.csv, current.csv and churn_model.pkl).

Outputs:
  lime_customer.html / lime_customer.png   LIME explanation of the SAME customer SHAP explained (70% churn risk)
  lime_text.html / lime_text.png           LIME on text: which words make a support message read as "about to cancel"

Install note: lime's packaging is old; on a fresh environment do
  pip install "setuptools<70" wheel && pip install lime
(the pre-rendered files in S07/demo/ mean you do not need to run this at all).

Why two explanations of one customer: SHAP and LIME reach a similar story by different routes
(exact game-theory contributions vs a simple model fitted around the point). Agreement builds trust;
disagreement is itself information. The text example shows what LIME does best: highlight the words.
"""
import pickle
import re
import warnings

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from lime.lime_tabular import LimeTabularExplainer
from lime.lime_text import LimeTextExplainer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

warnings.filterwarnings("ignore")
FEATURES = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter", "is_monthly", "region_north"]
NICE = {"tenure_months": "tenure (months)", "monthly_charges": "monthly charges (€)", "support_tickets": "support tickets",
        "promo_weeks_last_quarter": "promo weeks last quarter", "is_monthly": "monthly contract", "region_north": "region North"}

reference = pd.read_csv("reference.csv")
current = pd.read_csv("current.csv")
model = pickle.load(open("churn_model.pkl", "rb"))

# ------------------------------------------------------------------ 1. LIME on the same customer as the SHAP waterfall
cand = current[(current.region_north == 1) & (current.tenure_months > 36)].copy()
cand["prediction"] = model.predict_proba(cand[FEATURES])[:, 1]
cand = cand.sort_values("prediction", ascending=False).head(1)
x = cand[FEATURES].iloc[0].values
p = float(cand["prediction"].iloc[0])

explainer = LimeTabularExplainer(reference[FEATURES].values, feature_names=[NICE[f] for f in FEATURES],
                                 class_names=["stays", "churns"], categorical_features=[4, 5],
                                 discretize_continuous=True, random_state=7, mode="classification")
exp = explainer.explain_instance(x, model.predict_proba, num_features=6, num_samples=5000)
exp.save_to_file("lime_customer.html")

pairs = exp.as_list(label=1)
labels = [a for a, _ in pairs][::-1]; vals = [b for _, b in pairs][::-1]
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.barh(labels, vals, color=["#E07A2F" if v > 0 else "#2F80ED" for v in vals])
for i, v in enumerate(vals):
    ax.text(v + 0.005 if v > 0 else 0.005, i, f"{v:+.2f}", va="center", ha="left", fontsize=10)
ax.axvline(0, color="#6B7280", lw=1)
ax.set_title(f"LIME: the same customer, {p:.0%} churn risk (orange = towards churn)", loc="left", fontsize=11.5)
ax.set_xlabel("contribution of the condition to 'churns'")
for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
plt.tight_layout(); plt.savefig("lime_customer.png", dpi=160); plt.close()
print("lime_customer.html / .png written  (prediction %.2f)" % p)
for a, b in pairs: print(f"   {b:+.3f}  {a}")

# ------------------------------------------------------------------ 2. LIME on text: support messages, "about to cancel" or not
rng = np.random.default_rng(5)
cancel = ["I want to cancel my contract, the price went up again and the service is slow",
          "Third outage this month, I am switching to another provider unless this is fixed",
          "Please tell me how to terminate my subscription, your competitor offers fibre for less",
          "I have been waiting two weeks for a technician, I am done with this company",
          "The new bill is 20 euros more than agreed, I will leave at the end of the month",
          "Cancel my line, the support team never answers and the router keeps disconnecting",
          "Unless you match the competitor's offer I am moving my number next week",
          "This is the fourth complaint about the same problem, I am leaving",
          "How do I cancel? The connection drops every evening and nobody helps",
          "Your price increase is unacceptable, I am switching providers",
          "I am not renewing, the service has been terrible since the upgrade",
          "Send me the cancellation form, I found a cheaper plan elsewhere",
          "The connection drops constantly and the price is too high, I am cancelling",
          "Another price increase and still slow internet, I am switching",
          "I am leaving for a competitor, your support is useless and the outages continue",
          "Terminate my contract at the end of the month, the service is not worth the price"]
stay = ["Can you confirm my invoice was paid? Thank you for the quick help last time",
        "I would like to add a second line for my daughter, what are the options?",
        "The technician was excellent, the new router works perfectly",
        "How do I change my billing date to the 15th? Everything else is fine",
        "Please send me the manual for the router, I want to set up the guest network",
        "I moved house, can you transfer my service to the new address next month?",
        "Great speed since the fibre upgrade, just checking if there is a family discount",
        "Could you explain the roaming charges on my last bill? I travel to France next week",
        "I want to upgrade to the premium TV package, what does it include?",
        "Thanks for resolving the ticket so fast, the connection is stable now",
        "Is there a way to see my data usage in the app? Otherwise all good",
        "I'd like to renew for another year, can you keep the same price?",
        "The connection is excellent, I only need help changing my wifi password",
        "Can I get a copy of my contract for my records? No problems with the service",
        "The technician fixed everything, thank you, quick and friendly",
        "Please add the sports channels to my TV package from next month"]
texts = cancel + stay
y = np.array([1] * len(cancel) + [0] * len(stay))
clf = make_pipeline(TfidfVectorizer(stop_words="english", min_df=1), LogisticRegression(C=10, max_iter=1000))
clf.fit(texts, y)

msg = "Hi, the price went up again and the connection drops every evening. Unless this is fixed this week I am switching to another provider."
texp = LimeTextExplainer(class_names=["stays", "about to cancel"], random_state=7, bow=True)
te = texp.explain_instance(msg, clf.predict_proba, num_features=8, num_samples=3000)
te.save_to_file("lime_text.html")
pp = float(clf.predict_proba([msg])[0, 1])

pairs = te.as_list(label=1)
labels = [a for a, _ in pairs][::-1]; vals = [b for _, b in pairs][::-1]
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.barh(labels, vals, color=["#E07A2F" if v > 0 else "#2F80ED" for v in vals])
for i, v in enumerate(vals):
    ax.text(v + 0.001 if v > 0 else 0.001, i, f"{v:+.2f}", va="center", ha="left", fontsize=10)
ax.axvline(0, color="#6B7280", lw=1)
ax.set_title(f"LIME on text: which words make this message read as 'about to cancel' ({pp:.0%})", loc="left", fontsize=12)
ax.set_xlabel("contribution of the word to 'about to cancel'")
for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
plt.figtext(0.01, -0.02, f'Message: "{msg}"', fontsize=9, style="italic", wrap=True)
plt.tight_layout(); plt.savefig("lime_text.png", dpi=160, bbox_inches="tight"); plt.close()
print("lime_text.html / .png written  (prediction %.2f)" % pp)
for a, b in pairs: print(f"   {b:+.3f}  {a}")
