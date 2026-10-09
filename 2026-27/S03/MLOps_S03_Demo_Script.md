# Session 3 · Live demo script: "the memory for models" (MLflow)

**Slot:** minutes 28–35 (slide 15 "The memory for models", then slide 16 "What you just saw")
**Duration:** 7 minutes (8–9 with the two optional steps), browser only, no commands typed during class
**Setup file:** `demo/mlflow_demo_setup.py` (creates five logged runs and a registry with two versions)

---

## 1. Setup (already done; what you need to do before the session)

The demo database was built for you and lives in `S03/demo/mlflow/`: `mlflow.db` (five runs, the registry with two versions and their aliases), `mlruns/` (the model files) and `churn_demo.csv`. The stored paths already point at that folder on your Mac, so do not move the folder.

**To start the UI**, double-click `start_mlflow_ui.command` in `S03/demo/mlflow/` (or run it from Terminal). The first time it creates a virtual environment in that folder and installs MLflow, which takes two or three minutes; afterwards it starts in about 20 seconds and opens `http://127.0.0.1:5000` in your browser by itself (port 5001 if 5000 is busy). Stop it with Ctrl+C in the Terminal window. Do this once the day before class to trigger the first-time install, and again just before the session.

If macOS refuses to open the `.command` file ("cannot be opened because it is from an unidentified developer"), right-click it → Open → Open, once; or run `bash start_mlflow_ui.command` in Terminal.

Check the two pages you will use: **Experiments → churn-model** (five runs) and **Models → churn-model** (versions 1 and 2, aliases `production` and `challenger`). Keep both tabs open; zoom the browser to 125%.

To rebuild the runs from scratch on your Mac (not needed): `rebuild_demo.command` in the same folder; it deletes the database and re-runs `../mlflow_demo_setup.py`. The run names and metrics are deterministic (fixed random seeds), so the numbers below will match.

## 2. What the five runs tell

| Run name | What it is | Accuracy | Say |
|---|---|---|---|
| `lr-3-features` | Logistic regression, 3 features, March extract | ~0.81 | "The first baseline. This is the model in production." |
| `lr-4-features-promo` | Same, plus the promotions feature, June extract | ~0.82 | "The world changed in March; here the feature that captures it." |
| `rf-100` | Random forest, 100 trees, 5 features | ~0.82 | "A different algorithm. Same data version; you can see that." |
| `rf-300-depth8` | Random forest, 300 trees, depth 8 | ~0.83 | "The best so far. Registered as the candidate." |
| `rf-300-depth8-extract-0612` | Same model on an extract where 60% of `tenure_months` arrived empty and was read as 0 | ~0.80 | "The NorthRetail bug. The metric barely moved. Validation caught it, not the metric." |

Registry: **churn-model** version 1 (from run 1) with alias `production`, tag "approved by Product owner, 3 March 2026"; version 2 (from run 4) with alias `challenger`, tag "validation passed 9 June 2026; fairness check pending".

---

## 3. The seven minutes, click by click

### Tab 1 · Experiments → churn-model: the runs table (≈ 2.5 min)

> "This is an experiment log. Every attempt to train the churn model is one row: when, by whom, which algorithm, which settings, which **version of the data**, and what came out. María's notebook had three random forests copy-pasted and edited by hand; here they are rows you can sort and compare."

Click the **accuracy** column header to sort. Point at the top: "The best number is 0.83. Is it the best model? Not yet: it is the best number."

Tick two runs (`lr-3-features` and `rf-300-depth8`) and click **Compare**. Scroll to the parameters: "Same data version, different algorithm, different features. Now the difference is explainable."

### Tab 1 · The rejected run (≈ 1.5 min)

Go back to the runs table and click `rf-300-depth8-extract-0612`. Show the **Tags**: `rejected: data validation failed: 60% of tenure_months empty, read as 0`. Show the metric: accuracy ~0.80.

> "Look at the accuracy: 0.80, against 0.83. If you were only watching the metric you would say 'a bit worse, whatever'. But 60% of one feature was empty and read as zero: that is NorthRetail's bug. The validation check caught it, the metric did not. This is why validation is a step in the pipeline and not a comment saying 'looks fine'."

### Tab 2 · Models → churn-model: the registry (≈ 2 min)

> "The experiment log is every attempt. The registry is the shortlist: the models that matter, with a version number, an owner, and a status."

Show version 1: alias **production**, the tag with the approval date, the description "in production since 3 March". Show version 2: alias **challenger**, "validation passed 9 June; fairness check pending".

Click the alias `production`: "The application does not load 'the model from Tuesday'; it loads whatever the alias `production` points to. Promoting version 2 means moving this pointer. Nobody copies files; there is a record of who moved it and when."

Click version 1 → **Source run**: "And from the registry you walk back to the run, the settings, the data version. Session 1's history for code; this is the same for models."

### Optional A · Register a model live (≈ 1 min)

Registering in front of them turns the registry from a screenshot into a decision. Go back to **Tab 1**, open the run `rf-100` (the one that is neither the baseline nor the candidate). In the run page, find the logged model (in MLflow 3.x it is under the **Models** or **Artifacts** section of the run) and click **Register model**. In the dialog choose the existing model `churn-model` and confirm. Version 3 appears.

> "That took three seconds. It is now on the shortlist. Is it in production? No. It has no alias, no owner, no approval. It is a candidate that someone must now validate, and the registry shows exactly that."

Switch to **Tab 2** and refresh: three versions side by side. Version 1 with `production`, version 2 with `challenger` and the tag "fairness check pending", version 3 with nothing.

> "Registering is cheap. Promoting is the gate."

### Optional B · Promote the challenger (≈ 1 min, only if the runs table went quickly)

On the Models page, open version 2 and edit its aliases: add `production`. MLflow moves the alias off version 1 automatically (an alias points to one version at a time). Refresh.

> "The application now serves version 2. Nobody copied a file. Version 1 is still there to roll back to, and the change is timestamped with who made it. This is what Gate 2 looks like in a tool: a pointer that only certain people may move."

### Optional C · Show where the memory comes from: train a model live (≈ 1.5 min)

For a cohort that asks "but how does a run get in there?": the file `train_with_mlflow.py` in the same folder is a plain training script with the MLflow lines marked `# [MLflow]`. Two ways to use it.

*Show the code (30 s).* Open the file in any editor, scroll to section 5 and point at the marked lines: "the settings, the metrics, the tags, the model file. Eight lines. Everything else is what María already wrote." The appendix slide at the end of the deck shows the same before/after if you prefer not to open an editor.

*Run it (1 min).* Double-click `train_example.command` (or, in Terminal, from the `mlflow/` folder: `./.venv/bin/python train_with_mlflow.py`). It validates the data, trains a random forest and prints one line: `Run logged: RandomForest accuracy=0.823 …`. Refresh **Tab 1**: a new row, `rf-live-<today>`, tagged "trained live in Session 3", with `code_version: not versioned` because the folder is not a git repository (a good remark: "the run is logged, but the code that produced it is not; that is why the repository from Session 1 matters").

Two variants worth knowing. `--algorithm lr` trains a logistic regression on the five features and scores about 0.85, higher than the registered candidate: a live example of "the best number is not automatically the best model" (nobody has validated it). `--register` also creates version 3 in the registry with no alias and no owner, the same lesson as Optional A without the clicks.

If you do more than one optional step, skip the **Compare** click in the runs table to stay inside eight or nine minutes.

### Back to the slide (≈ 30 s)

> "Three things: every attempt is a row, not a memory; the rejected run shows why validation is not a metric; and the registry is a pointer with an owner, so registering is cheap and promoting is the gate."

Switch to slide 16, "What you just saw".

---

## 4. If something goes wrong

| Problem | Do this |
|---|---|
| UI not up yet | It needs about 20 s after the command; the first run also installs packages (2–3 min). Start it before class. |
| Port 5000 busy (macOS AirPlay uses it) | The launcher switches to 5001 by itself; open `http://127.0.0.1:5001`. |
| Runs missing | The UI was started from a different folder, or the `mlflow/` folder was moved. Use the launcher, and keep the folder where it is (or run `rebuild_demo.command`). |
| Registry page empty | Same cause as above; the registry lives inside `mlflow.db`. |
| No time | Do only the runs table (sort, compare) and the registry page. Skip the rejected run (it is on slide 16 anyway) and both optional steps. |
| "Register model" button not where expected | Its position varies by MLflow version: on the run page, under **Models** (3.x) or under **Artifacts → model** (2.x). Rehearse the click once before class. |
| Demo state changed after class | Optional A, B and C modify `mlflow.db` (extra runs, a third version, the alias moved). To restore the original five runs and two versions before reusing the demo, run `rebuild_demo.command` (about 30 s). |
| `train_example.command` fails with "validation failed" | Deliberate: the script refuses data with more than 5% empty values. Check `--data` points at `churn_demo.csv`. |
| Complete failure (MLflow will not start) | Open `demo/offline_fallback.html` in the browser: the runs table, the rejected run and the registry, read from the real `mlflow.db`, with links at the top in the same order as the demo. Read the same script. |

---

## 5. Checklist

- [ ] `start_mlflow_ui.command` run once the day before (first-time install) and again before class; both tabs open and zoomed
- [ ] Compare view tried once (two runs ticked → Compare)
- [ ] Optional A rehearsed once (Register model on `rf-100` → `churn-model`); Optional C rehearsed once (`train_example.command`, new row appears); then `rebuild_demo.command` run to reset
- [ ] `demo/offline_fallback.html` opens in the browser (the offline fallback)
- [ ] Slide 16 ready as the landing slide after the demo
