# Video 1 · Session 9 · Demo script: alerts in production

**Slot:** segment 6, slides 22–23 (minutes 47:30–54:00 of the video)
**Duration:** about 6½ minutes of screen recording, recorded on its own and cut in after slide 21
**Folder:** `S09/demo/` (the TelcoNova churn model, eight rules, one monitoring job, one scheduler file)
**Fallback:** slides 22–23 already carry the console, the message and the report as images; if the recording fails, record your voice over those two slides

---

## 1. Setup

### The day before (10 minutes, once)

1. In Finder, open `2026-27/S09/demo/` and double-click **`update_venv_and_run.command`**.
   - It reuses the Session 3 environment (`S03/demo/mlflow/.venv`) and installs what is missing (Evidently 0.7.21); the first time takes 1–3 minutes.
   - If it says the Session 3 environment was not found, double-click `S03/demo/mlflow/start_mlflow_ui.command` once (it creates it), close it with Ctrl+C, and try again.
   - If macOS refuses to open it ("unidentified developer"): right-click → Open → Open, once.
   - **"Also install LIME?"**: answer **N**. **"Open alert_checks.html?"**: answer **y**.
2. Check the result against section 2: **3 PASS, 5 FIRE, exit code 1**. If it matches, the demo is ready.

### Just before recording (5 minutes)

| Window | Prepare |
|---|---|
| **Terminal** | `cd` into `2026-27/S09/demo`, then `source ../../S03/demo/mlflow/.venv/bin/activate` and `clear`. Font about 16–18 pt (Cmd + several times). Make the window **as wide as the screen**: the result lines are long, and a wrapped line is hard to read on video. |
| **Editor** (VS Code or TextEdit) | Two tabs: `monitoring.yml` and `alert_message.md`. Font 16 pt or more. |
| **Preview** | `alert_message.png`: the same message as it looks in Slack. Nicer on video than the raw `.md`. |
| **Browser** | `alert_checks.html`, left on the **Metrics** tab (you click **Tests** on camera). Zoom 125%. |
| **The Mac** | Do Not Disturb on, other apps closed, desktop tidy. |

**To record:** Cmd + Shift + 5 → *Record Entire Screen* (or *Selected Portion*), microphone on in *Options*. Do Demo 1 and Demo 2 as two takes if you prefer; each starts from a clean window.

---

## 2. What the run shows (identical every time, except the date and time)

| Rule | Result | Value | The one thing to say |
|---|---|---|---|
| `missing-features` | PASS | 0% missing | "The NorthRetail bug, as a rule. Nothing missing this month." |
| `accuracy-overall` | PASS | 0.80 (limit 0.75) | "Overall, the model 'is fine'." |
| `batch-late` | PASS | finished 05:42 | "The list was ready before the team started at six." |
| `drifted-features` | **FIRE** · trend | 2 of the 6 inputs (limit 2) | "Two inputs moved: charges and promotions." |
| `charges-mean-shift` | **FIRE** · trend | mean €76.5 (limit 70) | "The pricing change. Ask the business before retraining." |
| `prediction-drift` | **FIRE** · trend | 0.116 (limit 0.10) | "The model itself is reacting." |
| `accuracy-segment` | **FIRE** · trend | North, tenure 3y+: 0.65 on 349 customers | "The overall rule passed; the segment rule fired. That is Session 7's demo." |
| `latency-p95` | **FIRE** · **incident** | 659 ms (limit 500) | "The only one that pages someone now." |

Summary line: **5 fired (1 incident, 4 trend); 3 passed**. Exit code **1**.

**The story behind the date:** imagine this is the run of **2 October**, when September's labels have just arrived; the drift checks look at the 1 October data. That is why slide 24 (the owner's page) shows September's labels and "Oct · pending". You do not need to say it unless someone would wonder.

---

## 3. Click by click

### Demo 1 · The monitoring job (slide 22, about 3½ minutes)

**Terminal.** Type, and press Enter:

```
python run_alert_checks.py
```

It takes about ten seconds and prints nothing until the end. Fill the silence:

> "This is the monitoring job: about a hundred and twenty lines of Python you can open. It loads the June reference and this month's data, scores both with the churn model, runs the Evidently drift and missing-value checks, joins the month's labels, computes accuracy overall and by segment, reads the batch time and the latency log, and checks every rule in alerts.yaml."

When the output appears, **read it top down**, pointing with the mouse:

1. **The three PASS lines.** "Nothing missing. Accuracy overall 0.80, above 0.75: the overall number says the model is fine. Batch finished at 05:42."
2. **The five FIRE lines.** "Two of the six inputs drifted, which is the limit. Charges: mean 76.5 against a limit of 70, the pricing change. Prediction drift 0.116, above 0.10: the model is reacting."
3. **Stop on `accuracy-segment`.** "And here: one segment below 0.70. North, tenure over three years, 0.65 on 349 customers. The overall rule passed and the segment rule fired. That is why the rule exists twice."
4. **`latency-p95`.** "659 milliseconds over the last ten minutes, tagged incident. That one wakes somebody."
5. **The summary line.** "Five fired, one incident, four trends."

Then type:

```
echo $?
```

It prints **`1`**.

> "That is the whole trick. Exit code one means 'something fired'. A scheduler needs to understand none of these metrics to know something is wrong. So who runs this, and who gets told?"

### Demo 2 · The scheduler, the message, the report (slide 23, about 3 minutes)

**Editor, `monitoring.yml`.**

1. Point at the two `cron` lines. "Every Monday at six, the drift checks. The second of every month at seven, once the labels have arrived, the performance checks. Two schedules, because the truth has its own calendar." Point at `workflow_dispatch`: "And on demand."
2. Point at the steps. "Fetch this month's data. Run the rules."
3. Point at **`if: failure()`**. "Only if the job failed, that is, only if the exit code was one, post the message to the channel."
4. Point at **`if: always()`** on *Keep the report*. "And always keep the report, above all when something fired, so whoever answers has the evidence."

> "It is GitHub Actions because you saw it in Session 5; cron, Airflow or a cloud scheduler do the same job."

**Preview, `alert_message.png`** (or the editor tab `alert_message.md`).

> "This is what the ML engineer sees on their phone. Five alerts. Each one: the rule, the value against the threshold, the action, and who it went to. The incident is marked differently, because it pages IT rather than posting to a channel. At the bottom, the three that passed, and links to the report, the rules and the run. Everything needed to act; nothing to interpret at three in the morning."

**Browser, `alert_checks.html`.** Click **Tests**.

> "And this is where the engineer clicks when the message arrives: Evidently's Tests tab. One success, three failures: the four data checks, each with its threshold written on it."

Point at the first red box (*Count of Drifted Columns*) and then the green one (*missing values*). Optional: click **Metrics** to show there are charts behind each test.

> "Scheduler, job, exit code, message, person, report. Back to the slides."

Stop the recording.

---

## 4. Reading the output aloud: four things that look odd on screen

| On screen | What it means | Say, if anything |
|---|---|---|
| `Actual value 2.000 >= 2.000` | Two drifted inputs; the rule fires at two or more | "Two, and the limit is two." |
| Evidently: `Count of Drifted Columns: Less 2.000` | The **pass** condition (fewer than 2); it failed | Nothing; point at the red colour |
| `p95 659 ms` | The latency log is simulated for the demo (there is no live endpoint) | Nothing |
| Date and time in the header | Today's date: the job stamps when it ran | Nothing |

---

## 5. If something goes wrong

| Problem | Do this |
|---|---|
| `ModuleNotFoundError: evidently` | The venv is not active. Run `source ../../S03/demo/mlflow/.venv/bin/activate`, or double-click `update_venv_and_run.command` again. |
| "The Session 3 environment was not found" | Double-click `S03/demo/mlflow/start_mlflow_ui.command` once, Ctrl+C, then run the S09 launcher again. |
| Lines wrap and look messy | Make the Terminal wider or reduce the font one step, `clear`, and run again. |
| Numbers differ from section 2 | You are in the wrong folder, or a demo file was edited. Check that you are in `S09/demo` and that `git status` shows no change to `current.csv`, `reference.csv` or `churn_model.pkl`. |
| A red warning about scikit-learn versions | Harmless (the model was saved with an older version). The script hides it; if it appears, carry on. |
| The recording fails or looks bad | Use slides 22–23 as they are: they show the console, the message and the Tests tab. Record the same words over the slides. |

---

## 6. After recording

Running the job rewrites `alert_checks.html`, `alert_message.md` and `console_output.txt` (only the date and time change), so `git status` will show them as modified. Commit them, or discard with `git checkout -- 2026-27/S09/demo`. If you want the slide images to match the new time stamp, double-click `update_venv_and_run.command` (it refreshes the PNGs); not necessary.

---

## 7. Checklist

- [ ] `update_venv_and_run.command` run the day before: 3 PASS, 5 FIRE, exit code 1
- [ ] Terminal in `S09/demo`, venv active, wide window, 16–18 pt, cleared
- [ ] Editor: `monitoring.yml` and `alert_message.md` open; Preview: `alert_message.png`; browser: `alert_checks.html` on the Metrics tab
- [ ] Do Not Disturb on
- [ ] Demo 1 recorded (`python run_alert_checks.py`, then `echo $?` → 1)
- [ ] Demo 2 recorded (`monitoring.yml` → message → Tests tab)
- [ ] Both takes cut in after slide 21; slide 24 follows
