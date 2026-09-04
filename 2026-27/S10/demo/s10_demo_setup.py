"""
s10_demo_setup.py  -  builds the Session 10 demo: two versions of the HR-assistant prompt in MLflow's prompt
registry, a 12-question golden set, and an evaluation of each version logged as an MLflow run.

Run from this folder (S10/demo). Creates mlflow/mlflow.db (its own database, separate from the Session 3 one)
and eval_results.html. Start the UI afterwards with start_prompt_registry.command (Mac) or:
    mlflow ui --backend-store-uri sqlite:///mlflow/mlflow.db --port 5002

WHAT IS REAL AND WHAT IS ILLUSTRATIVE
- The policies (hr_policies/), the golden set, the two prompts and the registry are real files and real MLflow objects.
- The answers (answers_v1.csv, answers_v2.csv) are illustrative transcripts written for the class: what a baseline
  prompt and a grounded prompt typically produce. No language model is called when you run this script.
- The judge is a transparent, rule-based stand-in for an LLM judge: correctness = the key facts of the reference
  answer appear; groundedness = every number in the answer exists in the source policy or in HR's reference answer; PII = a name from the
  policies is repeated. In production the judge is itself a language model with a rubric, checked against humans
  on a sample (Video 1, segment 5). The pattern (golden set -> judge -> scores per prompt version -> registry)
  is exactly the production pattern; only the judge is simplified so students can read it.

Install (once, in the Session 3 venv):  nothing extra; mlflow and pandas are already there.
"""
import re
from pathlib import Path

import mlflow
import pandas as pd

HERE = Path(__file__).resolve().parent
DB = HERE / "mlflow" / "mlflow.db"
DB.parent.mkdir(exist_ok=True)
mlflow.set_tracking_uri(f"sqlite:///{DB}")
mlflow.set_registry_uri(f"sqlite:///{DB}")

# ------------------------------------------------------------------ 1. the two prompts, in the registry
PROMPT_V1 = """You are the TelcoNova HR assistant. Answer the employee's question in a friendly, helpful way.

Context from the HR policies:
{{context}}

Question: {{question}}"""

PROMPT_V2 = """You are the TelcoNova HR assistant. Answer the employee's question using ONLY the policy text below.

Rules:
1. If the answer is not in the policy text, say "I cannot answer that" and refer the employee to HR. Never guess.
2. Quote the numbers exactly as they appear in the policy. Do not add benefits, limits or exceptions that are not written there.
3. End with "Source:" and the policy code and section (for example HR-POL-03 §3.1).
4. Maximum 60 words. No greetings, no small talk.
5. Never mention the name of any employee, even if a name appears in the policy text.

Policy text:
{{context}}

Question: {{question}}"""

v1 = mlflow.genai.register_prompt(name="hr-assistant", template=PROMPT_V1,
                                  commit_message="v1: baseline prompt, friendly tone, no grounding rules",
                                  tags={"owner": "HR Digital", "model": "gx-2", "docs": "hr_policies v2026.1"})
v2 = mlflow.genai.register_prompt(name="hr-assistant", template=PROMPT_V2,
                                  commit_message="v2: answer only from context; refuse when absent; cite the section; 60-word cap; no names; retrieval top-2 passages",
                                  tags={"owner": "HR Digital", "model": "gx-2", "docs": "hr_policies v2026.1"})
mlflow.genai.set_prompt_alias("hr-assistant", alias="production", version=v1.version)
mlflow.genai.set_prompt_alias("hr-assistant", alias="challenger", version=v2.version)
print(f"registered hr-assistant v{v1.version} (production) and v{v2.version} (challenger)")

# ------------------------------------------------------------------ 2. golden set, answers, policies
gold = pd.read_csv(HERE / "golden_set.csv")
answers = {1: pd.read_csv(HERE / "answers_v1.csv").set_index("id")["answer"],
           2: pd.read_csv(HERE / "answers_v2.csv").set_index("id")["answer"]}
policies = {p.name: p.read_text() for p in (HERE / "hr_policies").glob("*.md")}
NAMES = ["Ana García"]                                   # the one personal name that appears in the policies
NUM = re.compile(r"\d+(?:[.,]\d+)?")
TEMPLATE_TOKENS = {1: int(len(PROMPT_V1.split()) * 1.3), 2: int(len(PROMPT_V2.split()) * 1.3)}
CONTEXT_TOKENS = {1: 350, 2: 600}                     # v1 retrieves the top passage; v2 retrieves the top two
PRICE_IN, PRICE_OUT = 2.5 / 1e6, 10 / 1e6              # EUR per token, illustrative


def judge(row, answer):
    """Rule-based stand-in for an LLM judge. Returns a dict of per-question verdicts."""
    facts = [f.strip() for f in str(row.key_facts).split(";")]
    a_low = answer.lower()
    correct = all(f.lower() in a_low for f in facts)
    if row.source_doc == "none":                        # out of scope: correct = refused and pointed to HR
        correct = ("cannot" in a_low or "not" in a_low) and "hr" in a_low and not NUM.search(answer)
        grounded = not NUM.search(answer)               # any number here is invented
    else:
        allowed = set(NUM.findall(policies[row.source_doc])) | set(NUM.findall(row.reference_answer)) | set(NUM.findall(row.question))
        grounded = all(n in allowed for n in NUM.findall(answer))   # a number the policy (or HR's reference answer) never states is an invented one
    pii = any(n.lower() in a_low for n in NAMES)
    out_tokens = int(len(answer.split()) * 1.3)
    return dict(correct=correct, grounded=grounded, pii=pii, out_tokens=out_tokens)


rows = []
for _, r in gold.iterrows():
    for ver in (1, 2):
        j = judge(r, answers[ver][r.id])
        rows.append(dict(id=r.id, question=r.question, version=ver, answer=answers[ver][r.id], **j))
res = pd.DataFrame(rows)

# ------------------------------------------------------------------ 3. one MLflow run per prompt version
mlflow.set_experiment("hr-assistant-eval")
summary = {}
for ver in (1, 2):
    d = res[res.version == ver]
    in_tokens = TEMPLATE_TOKENS[ver] + CONTEXT_TOKENS[ver] + 20
    total = in_tokens + d.out_tokens.mean()
    cost_1000 = 1000 * (in_tokens * PRICE_IN + d.out_tokens.mean() * PRICE_OUT)
    m = dict(correctness=round(d.correct.mean(), 3), groundedness=round(d.grounded.mean(), 3),
             pii_leaks=int(d.pii.sum()), refusal_ok=int(d[d.id == 12].correct.iloc[0]),
             avg_output_tokens=round(d.out_tokens.mean(), 1), avg_input_tokens=in_tokens,
             avg_total_tokens=round(total, 1), cost_per_1000_questions_eur=round(cost_1000, 2),
             p95_latency_s=round(0.6 + d.out_tokens.quantile(0.95) / 60, 2))
    summary[ver] = m
    with mlflow.start_run(run_name=f"eval prompt v{ver} · golden set 12 · judge rule-based"):
        mlflow.log_params({"prompt": f"prompts:/hr-assistant/{ver}", "retrieval": "top-1 passage" if ver == 1 else "top-2 passages", "prompt_alias": "production" if ver == 1 else "challenger",
                           "model": "gx-2", "golden_set": "golden_set.csv (12 questions)", "judge": "rule-based stand-in v0",
                           "docs_version": "hr_policies v2026.1", "evaluated_by": "HR Digital"})
        mlflow.log_metrics(m)
        mlflow.set_tags({"session": "S10 demo", "kind": "prompt evaluation"})
    print(f"v{ver}: {m}")

# ------------------------------------------------------------------ 4. the per-question table, as a page
def cell(ok, txt_ok="PASS", txt_ko="FAIL"):
    return f'<td class="{"ok" if ok else "ko"}">{txt_ok if ok else txt_ko}</td>'

trs = []
for _, r in gold.iterrows():
    a1 = res[(res.id == r.id) & (res.version == 1)].iloc[0]; a2 = res[(res.id == r.id) & (res.version == 2)].iloc[0]
    trs.append(f"<tr><td>{r.id}</td><td class='q'>{r.question}</td>"
               f"<td class='a'>{a1.answer}</td>{cell(a1.correct)}{cell(a1.grounded)}{cell(not a1.pii, 'none', 'LEAK')}"
               f"<td class='a'>{a2.answer}</td>{cell(a2.correct)}{cell(a2.grounded)}{cell(not a2.pii, 'none', 'LEAK')}</tr>")
s1, s2 = summary[1], summary[2]
html = f"""<!doctype html><html><head><meta charset="utf-8"><title>hr-assistant · prompt evaluation</title>
<style>body{{font-family:Calibri,Arial,sans-serif;color:#1B2A4A;margin:24px}} h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#5B6472;margin-bottom:16px}}
table{{border-collapse:collapse;width:100%;font-size:12px}} th{{background:#1B2A4A;color:#fff;padding:6px;text-align:left}} td{{border:1px solid #D9DEE6;padding:6px;vertical-align:top}}
td.q{{width:14%;font-weight:bold}} td.a{{width:26%}} td.ok{{background:#E3F1F2;color:#0E7C86;font-weight:bold;text-align:center}} td.ko{{background:#FBE9DC;color:#B42318;font-weight:bold;text-align:center}}
.sum{{display:flex;gap:16px;margin:12px 0 20px}} .card{{border:1px solid #D9DEE6;border-radius:8px;padding:10px 14px;min-width:260px}} .card b{{display:block;font-size:14px;margin-bottom:6px}}
.v1 b{{color:#E07A2F}} .v2 b{{color:#0E7C86}}</style></head><body>
<h1>hr-assistant · prompt evaluation on the golden set (12 questions)</h1>
<div class="sub">Judge: rule-based stand-in (correctness = key facts present · groundedness = every number exists in the policy or HR's reference answer · PII = an employee name repeated). Model gx-2 · docs hr_policies v2026.1</div>
<div class="sum">
<div class="card v1"><b>v1 · production · baseline prompt</b>correctness {s1['correctness']:.0%} · groundedness {s1['groundedness']:.0%} · PII leaks {s1['pii_leaks']}<br>avg tokens {s1['avg_total_tokens']:.0f} · cost per 1,000 questions {s1['cost_per_1000_questions_eur']:.2f} EUR · p95 {s1['p95_latency_s']} s</div>
<div class="card v2"><b>v2 · challenger · grounded prompt</b>correctness {s2['correctness']:.0%} · groundedness {s2['groundedness']:.0%} · PII leaks {s2['pii_leaks']}<br>avg tokens {s2['avg_total_tokens']:.0f} · cost per 1,000 questions {s2['cost_per_1000_questions_eur']:.2f} EUR · p95 {s2['p95_latency_s']} s</div>
</div>
<table><tr><th>#</th><th>Question</th><th>v1 answer</th><th>correct</th><th>grounded</th><th>PII</th><th>v2 answer</th><th>correct</th><th>grounded</th><th>PII</th></tr>
{''.join(trs)}</table></body></html>"""
(HERE / "eval_results.html").write_text(html)
res.to_csv(HERE / "eval_results.csv", index=False)
print("eval_results.html and eval_results.csv written")
