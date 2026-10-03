# MLOps · Module Concept-Check Quizzes

**Master in Business Analytics and Data Science — MLOps elective (2026–27)**

Four short quizzes, one per module, five multiple-choice questions each (four options, one correct). They are light concept-checks to fix the key ideas after each module — not exam-level. Post each one after its module is taught.

> Name: ________________________  ·  Group: ______  ·  Mark one letter per question.

---

## Module 1 — Foundations, personas & the lifecycle (Sessions 1–2)

**1.1** What does it mean to *operationalise* a model, as opposed to *training* it?

- A) To run it once on a large dataset to get the best possible score.
- B) To put it into production as a running service that answers real requests every day, with someone accountable for it.
- C) To save the trained model as a file and email it to the IT team.
- D) To document the training process in a notebook.

**1.2** Why does a deployed ML model usually need monitoring and retraining, when an ordinary software function does not?

- A) Because the data and the world it sees keep changing, so the model's accuracy decays over time even if its code never changes.
- B) Because model files slowly corrupt on disk.
- C) Because cloud servers get slower over time.
- D) Because models are always written in Python, which is unreliable.

**1.3** In a RACI responsibility map, how many people should be *Accountable* for a given lifecycle stage?

- A) As many as possible, to share the risk.
- B) None — accountability is shared by the whole team.
- C) Exactly one — a single role that answers for the outcome of that stage.
- D) At least three, for redundancy.

**1.4** According to the course, which kind of metric ultimately matters most for a model in production?

- A) The size of the training dataset.
- B) The business/product outcome the model is meant to improve (e.g. reduced churn, higher revenue).
- C) The number of features used.
- D) The programming language of the model.

**1.5** Complete the course's key phrase: "A model in production is a ___, not a ___."

- A) prototype … product
- B) cost … benefit
- C) dataset … model
- D) running process … file

---

## Module 2 — Pipelines, environments, deployment & security (Sessions 3–6)

**2.1** What best describes the difference between a notebook and a production pipeline?

- A) A notebook is faster than a pipeline.
- B) A pipeline can only be written in Java.
- C) A pipeline runs the same steps in the same order automatically, with checks that can stop it, while a notebook is run by hand, step by step.
- D) A notebook can use data, but a pipeline cannot.

**2.2** What are the three environments a model typically moves through before it serves customers?

- A) Local, Remote, Cloud.
- B) Development (Dev), Quality Assurance (QA), and Production (Prod).
- C) Training, Testing, Validation.
- D) Draft, Review, Final.

**2.3** An attacker deliberately feeds a model bad, mislabelled training examples to corrupt what it learns. What is this attack called?

- A) Data poisoning.
- B) A canary deployment.
- C) Concept drift.
- D) A unit test.

**2.4** Why do teams package a model inside a container (e.g. with Docker) before deploying it?

- A) Because containers make the model more accurate.
- B) Because a container is the only place a model can run.
- C) Because containers are always cheaper than servers.
- D) So the model travels together with its code and exact environment and runs the same way everywhere — no more "it worked on my machine."

**2.5** Which deployment strategy releases a new model to only a small percentage of live traffic first, to limit the damage if something goes wrong?

- A) Deploying to everyone at once.
- B) A canary deployment.
- C) Deleting the old model first.
- D) Training in production.

---

## Module 3 — Monitoring, drift & retraining (Sessions 7–9)

**3.1** Which statement describes *data drift*?

- A) The distribution of the model's *inputs* changes over time compared with what it was trained on.
- B) The model's source code is edited.
- C) The server hosting the model is restarted.
- D) The model file is renamed.

**3.2** Some model problems can be spotted *before* the true labels (outcomes) are available. Which signal can you monitor **without** needing labels?

- A) Precision and recall.
- B) The F1 score.
- C) Input (data) drift — a change in the incoming data itself.
- D) Nothing; you always need labels to monitor anything.

**3.3** The course says "no threshold: a chart; no action: an alarm nobody answers." What must a useful monitoring alert include, beyond the metric?

- A) A nicer colour scheme.
- B) A threshold that triggers it, plus the action to take and the person to notify.
- C) The model's number of parameters.
- D) The name of the cloud provider.

**3.4** A fraud model is 99.5% accurate — but fraud is very rare, and the model actually flags almost no fraud. What does this show?

- A) Accuracy can be misleading when one class is rare; you need precision/recall to see the model catches nothing.
- B) The model is excellent and should be deployed.
- C) Accuracy is always the best metric.
- D) The model has no problem at all.

**3.5** When should a model typically be retrained?

- A) Never — a deployed model is finished.
- B) Only when the code is changed.
- C) When a monitored metric crosses its threshold (for example, drift is detected or performance drops).
- D) Exactly once a year, no matter what.

---

## Module 4 — GenAI (LLMOps) & governance (Sessions 10–12)

**4.1** How is working with a large language model (LLM) different from a classical ML model, in one key way the course stresses?

- A) You mostly *configure* it — by writing and versioning prompts — rather than training it from scratch.
- B) LLMs never make mistakes.
- C) LLMs do not need any monitoring.
- D) LLMs are always cheaper to run than classical models.

**4.2** In a RAG (retrieval-augmented generation) assistant, where do the answers get their factual grounding?

- A) From documents retrieved from a knowledge base and given to the model as context.
- B) From the model inventing plausible text on its own.
- C) From the user's question alone.
- D) From the colour of the interface.

**4.3** Which is a recommended way to evaluate the quality of an LLM's answers?

- A) Assume it is correct because it sounds confident.
- B) Only check it the first day and never again.
- C) Count how many words it produces.
- D) Compare its answers against a golden set, use human review, and use an LLM-as-a-judge.

**4.4** The EU AI Act classifies AI systems by risk. A system that scores people's creditworthiness to approve or deny loans falls into which tier?

- A) Minimal risk — no obligations.
- B) Banned outright.
- C) High-risk — it must meet obligations such as human oversight, transparency and logging.
- D) Not covered by the Act at all.

**4.5** What are the four core functions of the NIST AI Risk Management Framework?

- A) Plan, Build, Test, Ship.
- B) Govern, Map, Measure, Manage.
- C) Collect, Clean, Train, Deploy.
- D) Identify, Protect, Detect, Respond.

---

*End — four modules, 20 questions in total.*
