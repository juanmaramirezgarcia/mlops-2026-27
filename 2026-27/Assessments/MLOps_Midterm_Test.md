# MLOps · Midterm Test

**Master in Business Analytics and Data Science — MLOps elective (2026–27)**

Coverage: Sessions 1–6 (Foundations, personas & lifecycle; ML pipelines, environments & security; CI/CD & deployment strategies).
Format: 15 multiple-choice questions. Each has four options and **exactly one** correct answer.

> Name: ________________________  ·  Group: ______  ·  Date: ____________
>
> Duration: [set on campus] · Materials allowed: [set on campus] · Mark each answer clearly (one letter per question). No AI tools.

---

**1.** A data scientist reports: "The model is finished — it reached 0.91 AUC on the hold-out set and I've saved the `.pkl` file." From an MLOps standpoint, why is "finished" the wrong framing?

- A) AUC is not valid for production models; only accuracy matters once a model is live.
- B) The `.pkl` format cannot be deployed, so the model must be retrained inside the production environment first.
- C) A deployed model is a running process that must answer real requests every day and have an accountable owner; training yields a file, operationalising yields a service that someone must keep alive.
- D) The model must reach at least 0.95 AUC before it can be called production-ready.

**2.** Unlike an ordinary software function, a deployed ML model can silently become less accurate over months even though its code is never touched. What is the primary MLOps reason?

- A) Model binaries degrade physically on disk over time.
- B) The statistical relationships in the live data move away from those the model learned, so its performance decays even with unchanged code — retraining is a question of *when*, not *if*.
- C) Cloud providers throttle the compute available to older models.
- D) Pickle files lose numerical precision each time they are loaded into memory.

**3.** The course states that most model failures happen "between roles, not inside them," and that each lifecycle stage needs one Accountable owner. In a RACI map, which statement is correct?

- A) Several people should be Accountable for the same stage so that risk is shared.
- B) "Responsible" and "Accountable" are two labels for the same person — the one doing the work.
- C) The Data Scientist should be Accountable for every stage because they built the model.
- D) Exactly one role is Accountable for a stage (it answers for the outcome), while one or more may be Responsible (doing the work); the hand-overs between roles are where failures concentrate.

**4.** A churn model has excellent ROC-AUC, but the retention campaign it feeds has not reduced actual churn or revenue loss. According to the course's view of performance, what does this reveal?

- A) The AUC was probably miscalculated, because a high AUC guarantees business impact.
- B) Model-quality metrics are necessary but not sufficient; what ultimately matters are the product/business metrics the model is meant to move, and those must be tracked too.
- C) Business metrics fall outside the scope of MLOps and should not be monitored.
- D) The model should immediately be replaced with a deep-learning architecture.

**5.** The course opens with the idea of "hidden technical debt" in ML systems. Which situation best illustrates *that* debt, rather than ordinary software debt?

- A) A function with unclear variable names that is hard to read.
- B) A missing semicolon that breaks the build.
- C) A feature computed by an undocumented SQL script kept on one analyst's laptop, with a second, slightly different copy elsewhere, so the model's inputs cannot be reliably reproduced.
- D) A user interface that loads slowly on older browsers.

**6.** The course contrasts "a notebook is a workshop; a pipeline is a factory." Which property most distinguishes a production pipeline from a notebook?

- A) It runs its steps in the same defined order every time, with validation checks that can halt the run before a bad model is produced, and it is executed by a machine rather than ad hoc by a person.
- B) It must be written in a compiled language, whereas notebooks use Python.
- C) It stores its outputs in the cloud, whereas a notebook stores them locally.
- D) It can only be triggered on a fixed schedule, never on demand.

**7.** An auditor asks: "For this specific prediction made last March, exactly which data and which model version produced it?" Which set of practices makes that answerable?

- A) Keeping the latest model on a shared drive and overwriting it on each retrain.
- B) Writing thorough comments in the training notebook.
- C) Storing all predictions in a timestamped spreadsheet.
- D) Versioning code in a repository, snapshotting data with a fingerprint/hash, logging experiments, and registering model versions, so any prediction traces back to its exact inputs and model.

**8.** A team promotes a model directly from a data scientist's laptop into the live ordering system after hours. Which risk does the Dev/QA/Prod separation with promotion gates specifically address?

- A) It lowers cloud cost by training on cheaper machines.
- B) It guarantees the model will be more accurate.
- C) It stops an untested change from reaching live systems by first requiring it to pass a QA environment that behaves like production, with an accountable sign-off at each gate.
- D) It makes training faster by parallelising work across the three environments.

**9.** An attacker repeatedly queries a deployed credit model with carefully crafted inputs and uses the responses to reconstruct sensitive attributes of individuals who were in the training data. Which threat is this?

- A) Data poisoning.
- B) Model inversion.
- C) A canary deployment gone wrong.
- D) Concept drift.

**10.** In the Session 5 demo, the pipeline "stopped at the data test; nothing was trained, nothing was deployed." What is the purpose of placing a data-validation step early in the pipeline?

- A) To catch bad or out-of-range input data and halt the run *before* compute is spent training and *before* a flawed model can be deployed.
- B) To speed up training by dropping rows at random.
- C) To encrypt the data before training.
- D) To convert the dataset into a container image.

**11.** The course says a CI pipeline runs "tests for code, tests for data, tests for models." Which of the following is a *data* test, as opposed to a code test or a model test?

- A) Checking that a function returns the correct output for a known input.
- B) Checking that the source code passes the linter.
- C) Checking that an incoming feature's values fall within the expected range and schema before training.
- D) Checking that the trained model's AUC exceeds a threshold on a validation set.

**12.** "Ship the artefact, not the file." What best captures why a container image is preferred over emailing a `.pkl` model file to the IT team?

- A) Container images are always smaller than pickle files.
- B) The artefact bundles the model with its code, configuration, exact environment/dependencies and documentation, so it runs the same everywhere — removing "it worked on my machine."
- C) Pickle files cannot be stored in a registry.
- D) Putting a model in a container automatically raises its accuracy.

**13.** A customer-facing bank model must be updated with **zero downtime** and an **instant way back** if the new version misbehaves. Which rollout strategy fits best?

- A) Blue-green: stand up the new version alongside the old, switch traffic across, and switch straight back if anything goes wrong.
- B) Shadow deployment as the final production step.
- C) Retraining directly in production during business hours.
- D) Pushing to 100% of users at once and watching the dashboards.

**14.** The course frames "every rollout strategy is a way to make a mistake small." Which pairing of strategy and purpose is stated **correctly**?

- A) Canary: replace 100% of traffic at once to get a clean measurement.
- B) A/B test: its purpose is to guarantee zero downtime during the release.
- C) Blue-green: expose the new model to just 1% of users to limit the blast radius.
- D) Shadow: send real traffic to the new model without using its outputs, to prove it before it serves anyone.

**15.** A team wants to decide whether a new model version genuinely outperforms the current one in production. What must an A/B test define **in advance** for the decision to be valid?

- A) The container base image and the cloud region.
- B) A primary metric and a decision threshold (and how users are assigned to each group), fixed before the test begins.
- C) The number of GPUs used to train each version.
- D) The colour scheme of the monitoring dashboard.

---

*End of midterm. 15 questions.*
