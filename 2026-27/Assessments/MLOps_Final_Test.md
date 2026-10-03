# MLOps · Final Test

**Master in Business Analytics and Data Science — MLOps elective (2026–27)**

Coverage: all sessions (Sessions 1–12) — foundations & personas; pipelines, environments & security; CI/CD & deployment; monitoring & drift metrics; LLMOps; and AI governance & regulation. The paper is weighted towards the second half of the course (monitoring, LLMOps, governance).
Format: 25 multiple-choice questions. Each has four options and **exactly one** correct answer.

> Name: ________________________  ·  Group: ______  ·  Date: ____________
>
> Duration: [set on campus] · Materials allowed: [set on campus] · Mark each answer clearly (one letter per question). No AI tools.

---

## Foundations, personas & lifecycle

**1.** A retail demand-forecast model silently degraded for four months before anyone noticed, because the data scientist who built it had moved to another team and no one was watching it. Which foundational MLOps principle was violated?

- A) The model needed a larger training set.
- B) A live model is a running process that needs a single Accountable owner watching it — it is not a finished deliverable that can be left alone.
- C) The model should have used a more sophisticated algorithm.
- D) Forecasting models cannot be used for automatic ordering.

**2.** Which statement best reflects the course's position on retraining?

- A) A model needs retraining only if its source code is changed.
- B) A model that was carefully validated at launch will not need retraining.
- C) Because the world shifts under the model, a live model decays even with unchanged code, so retraining is a matter of *when*, not *if*.
- D) Retraining exists only to add new input features to a model.

**3.** A recommender's offline ranking metric improves after a new release, but average order value and customer retention stay flat. What does the course say the team should conclude?

- A) The offline metric is all that matters; the release was a success.
- B) Business metrics are outside MLOps and should be ignored.
- C) The algorithm family should be swapped immediately.
- D) Model metrics are proxies that can improve without moving the business outcome; the product/business metrics are what ultimately matter and must be monitored.

## Pipelines, environments, deployment & security

**4.** Why do organisations separate Dev, QA and Prod environments with promotion gates?

- A) So that nothing reaches live systems untested: QA behaves like production and an accountable owner signs each gate, preventing a laptop-to-production jump.
- B) Because regulators require every company to run exactly three environments.
- C) To reduce cloud spend by using cheaper hardware in production.
- D) To make model training run faster by splitting it across three machines.

**5.** A vendor retrains its model every month on user-submitted data. Attackers deliberately feed it crafted, mislabelled examples over time to shift its behaviour in their favour. Which threat is this, and a valid control?

- A) Model extraction; mitigated by making the model larger.
- B) Adversarial evasion; mitigated by lowering the decision threshold.
- C) Data poisoning; mitigated by validating and sanitising incoming training data, tracking data provenance/lineage, and running anomaly detection on new data.
- D) Model inversion; mitigated by adding more features.

**6.** Which combination lets a team reproduce exactly how a past model version was built?

- A) A screenshot of the final metrics plus a Slack message describing the run.
- B) Versioned code, a fingerprinted (hashed) data snapshot, an experiment log, and a model registry entry.
- C) The most recent model kept on a shared drive, overwritten each retrain.
- D) A well-commented training notebook stored on the author's laptop.

**7.** A team wants to expose a new fraud model to just 2% of live traffic first, so that any damage is contained before a full rollout. Which strategy is this?

- A) Blue-green deployment.
- B) Shadow deployment.
- C) A full A/B test.
- D) Canary deployment.

**8.** A team adds a scheduled weekly pipeline that automatically retrains the model on fresh data and redeploys it if all tests pass. In MLOps terms, what capability does this add *beyond* basic CI/CD?

- A) Continuous Training (CT): automated retraining triggered by a schedule (or by drift), a higher level of MLOps maturity than manual retraining.
- B) Continuous Integration (CI), which it did not have before.
- C) A blue-green deployment strategy.
- D) A golden evaluation set.

## Monitoring & drift metrics

**9.** Which statement correctly distinguishes data drift from concept drift?

- A) Data drift and concept drift are two names for the same phenomenon.
- B) Data drift is a change in the input distribution (detectable without labels); concept drift is a change in the relationship between inputs and the target (confirmed only once labels arrive).
- C) Data drift needs labels to detect; concept drift can always be seen without labels.
- D) Both are simply other names for performance decay.

**10.** A fraud model's true labels only arrive weeks later, after chargebacks settle. What can the team monitor **today**, before labels, to get an early warning that something has changed?

- A) Precision and recall on today's transactions.
- B) The F1 score of the current day.
- C) Input (data) drift and prediction/output drift, which need no ground truth.
- D) Concept drift measured directly.

**11.** The course warns: "no threshold: a chart; no action: an alarm nobody answers." What must a complete monitoring *rule* specify?

- A) Only the metric and an attractive dashboard.
- B) The model's hyperparameters and its training-set size.
- C) The cloud region and the container image.
- D) The metric, what it detects, a threshold with a time window, and the action plus the person the alert routes to.

**12.** A classifier that always predicts "not fraud" achieves 99.5% accuracy because fraud is very rare. What is the correct reading?

- A) Accuracy is misleading for rare events; precision/recall (or the confusion-matrix breakdown) reveal that the model catches no fraud at all.
- B) The model is excellent and should be deployed.
- C) The AUC of this model must also be 99.5%.
- D) Raising the decision threshold would fix the problem.

**13.** Raising the decision threshold of a binary classifier typically has which effect?

- A) It increases both precision and recall at the same time.
- B) It increases precision but lowers recall — the two trade off through the threshold, so the choice depends on the cost of each type of error.
- C) It decreases both precision and recall.
- D) It changes the model's AUC.

**14.** Which statement about AUC and calibration is correct?

- A) AUC depends on the chosen decision threshold.
- B) A high AUC guarantees that a model's predicted probabilities are well calibrated.
- C) AUC measures ranking quality independent of any chosen threshold, while calibration asks whether the predicted probabilities can be trusted as real probabilities.
- D) Calibration measures how fast the model returns a prediction.

**15.** Overall model accuracy held steady at about 80%, yet complaints from one region rose sharply. Which monitoring practice would have caught this earliest?

- A) Monitoring the aggregate accuracy more frequently.
- B) Retraining the model every week regardless of metrics.
- C) Raising the global decision threshold.
- D) Monitoring metrics by segment, not just in aggregate — an overall figure can pass while a subgroup fails.

**16.** A model that *blocks* the transactions it judges fraudulent never observes what would have happened to the blocked ones. Why is this a monitoring problem, and what is the fix?

- A) A blocking/rejecting model hides its own false positives, because the outcome of blocked cases is never seen; letting a small random sample through provides the ground truth needed to measure them.
- B) There is no problem; a blocking model is inherently accurate.
- C) The team should measure performance only on the approved transactions.
- D) The team should simply raise the block threshold until complaints stop.

## LLMOps

**17.** In an LLM/RAG system the course says "the prompt is code and the documents are data." Which operational practice follows from that?

- A) Prompts never need versioning, because no model training happens.
- B) Version, test, promote and roll back prompts (and the document index) like code — a prompt registry, a golden set, and a sign-off become the controls; you *configure* rather than train.
- C) Retrain the base model every time the prompt is edited.
- D) Keep the prompt only as a string inside the application code, where it is easiest to change.

**18.** A RAG customer-support assistant starts quoting tariffs that were withdrawn months ago. Where is the root cause?

- A) The base LLM's weights have become outdated.
- B) The prompt template is too long.
- C) The document index was never refreshed, so retrieval returns stale chunks and the model grounds its answer in outdated content; index freshness is the missing control.
- D) The embedding model has too few dimensions.

**19.** Why does the course insist on using a golden set, human review, **and** an LLM-as-a-judge together, rather than relying on one of them?

- A) Only the judge is needed, because it is the cheapest option.
- B) Human review alone is always sufficient for production quality.
- C) The golden set alone removes the need for any live monitoring.
- D) Each covers the others' gaps — the golden set gives repeatable regression coverage, humans catch what rules miss, and the judge scales — but the judge itself must be measured against human labels, because it can be wrong.

**20.** Which pairing of a guardrail with the correct side of the system is right?

- A) Prompt-injection and PII detection are *input* guardrails; toxicity, format and grounding checks are *output* guardrails — and each one adds latency.
- B) Grounding checks are an input guardrail applied before retrieval.
- C) Prompt-injection detection is an output guardrail applied to the generated answer.
- D) Guardrails add no latency, so you can add as many as you like for free.

**21.** How does the course say you should estimate the running cost of an LLM feature?

- A) A flat monthly licence fee, independent of how much it is used.
- B) Roughly requests × tokens per request × price per token (plus the cost of human review), with caching of repeated queries used to reduce it.
- C) By counting the number of parameters in the base model.
- D) By the number of GPUs in the data centre, regardless of traffic.

## AI governance & regulation

**22.** The course gives a single test for whether a written governance policy is *real* governance. What is it?

- A) Whether the policy has been printed, signed and filed.
- B) Whether the company's legal team approved it.
- C) For each requirement, ask which pipeline step enforces it, which artefact proves it, and which monitor catches it failing — a policy with none of these is intention, not governance.
- D) How many pages long the policy document is.

**23.** Under the EU AI Act's risk-based tiers, an AI system that scores individuals' creditworthiness to approve or deny loans is classified as:

- A) Minimal risk, so no specific obligations apply.
- B) Prohibited, so it cannot be used at all.
- C) Exempt, because it is used only internally by the bank.
- D) High-risk, and therefore subject to obligations such as risk management, data governance, human oversight, transparency and logging.

**24.** Which statement about the EU AI Act is correct?

- A) The most serious (prohibited-practice) breaches can draw fines up to €35 million or 7% of global annual turnover, whichever is higher, and obligations differ for providers and deployers.
- B) The maximum possible fine under the Act is €35,000.
- C) Every AI system faces exactly the same set of obligations regardless of its use.
- D) The Act applies only to companies headquartered inside the EU.

**25.** In the NIST AI Risk Management Framework, what are the four core functions?

- A) Plan, Do, Check, Act.
- B) Govern, Map, Measure, Manage.
- C) Identify, Protect, Detect, Respond.
- D) Collect, Clean, Train, Deploy.

---

*End of final. 25 questions.*
