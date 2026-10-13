# MLflow lab · Give María's model a memory

**MLOps · Master in Business Analytics and Data Science · MBDS-PT2026F · Forum 2, Optional Theme A**

*About 20 minutes. No code to write, nothing to install on your computer.*

---

## What this is about

In Session 3 you saw María's notebook: a model that scored *"0.84 yesterday, 0.87 today, whatever"*, with no record of which settings or which data gave which number. You also saw MLflow keep that record.

In this lab you do it yourself. You train four versions of María's churn model in Google Colab, MLflow records every attempt, and you compare them side by side. The point is not to build the best model. The point is to see what a tracked experiment lets you answer that an untracked notebook cannot.

**This theme is optional**, like every theme in the forum. It counts as a theme contribution, and nobody loses marks for skipping it.

---

## Before you start

You need:

- **A laptop or desktop** with Chrome, Edge, Firefox or Safari. A phone or tablet will not work well.
- **A Google account** (a personal Gmail is fine). Colab is Google's free online notebook service.
- **Two files from the campus** (Forum 2 → Optional Theme A):
  - `MLOps_S04_MLflow_Lab.ipynb`: the lab notebook
  - `churn_raw.csv`: María's data (the same file as last week)

Save both files somewhere easy to find, such as your Desktop.

---

## Open the lab in Colab (2 minutes)

1. Go to **colab.research.google.com** and sign in with your Google account.
2. In the window that opens, click **Upload** (in older versions: menu **File → Upload notebook**).
3. Choose `MLOps_S04_MLflow_Lab.ipynb`. The lab opens in a new tab.
4. **Optional:** to keep your work after you close the tab, use **File → Save a copy in Drive**. Otherwise everything disappears when you close the tab. That is fine for this lab.

---

## Run the lab (15 minutes)

The notebook is a series of grey **cells** with explanations between them. To run a cell, hover over it and click ▶ on its left, or click inside it and press **Shift + Enter**. Run the cells **in order, from top to bottom**, and read the text between them.

| Step | What you do | What you should see |
|---|---|---|
| 1 · Install MLflow | ▶ and wait 1–2 minutes | *"MLflow is ready, version 3.15.2"* |
| 2 · Load María's data | ▶, then **Choose files** and pick `churn_raw.csv` | *"Loaded 1,212 rows and 9 columns"* and a preview |
| 3 · Clean the data | ▶ | A **cleaning receipt**: 12 duplicates removed, 1,175 rows ready, and a *data fingerprint* |
| 4 · Switch on MLflow | ▶ | *"Recipe ready"* |
| 5 · Train three models | ▶ and wait about 30 seconds | Three lines, one each for models A, B and C |
| 6 · Compare | ▶, then **read and think** | A table and a chart of all runs |
| 7 · Your turn | Change the settings in the form, then ▶ | Your run added at the bottom of the table |
| 8 · MLflow screen | *(Optional)* ▶ and click the link | The MLflow interface from the class demo |
| 9 · Forum | Take a screenshot and write your post | |

**Two experiments for Step 7** (run the cell once for each, changing the run name each time):

- **María's 0.84 vs 0.87.** Keep everything as in model B (random forest, depth 4, 200 trees) and change only the **split seed**: 7, 123, or any number you like. The model is identical. Only *which customers end up in the unseen 30%* changes.
- **The sweet spot.** Try a forest with a depth of 2, 6 or 10. Watch the score on unseen customers and the gap.

### The words you will meet

| In the table | In plain words |
|---|---|
| **Run** | One attempt at training a model. MLflow keeps a record of each one. |
| **Score on UNSEEN customers (test AUC)** | How well the model ranks customers who will leave above those who will stay, measured on 30% of customers it never saw. **This is the score that predicts real life.** 0.5 is a coin flip; 1.0 is perfect. |
| **Score on studied customers (train AUC)** | The same score, measured on the customers the model learned from. |
| **Gap** | Studied score minus unseen score. Think of a student who memorises last year's exam answers. |
| **Churners caught (recall)** | Of the customers who really left, the share the model flagged. |
| **Alerts that were right (precision)** | Of the customers the model flagged, the share who really left. |
| **Split seed** | The number that decides which customers go into the unseen 30%. Same seed means the same split. |
| **Data version (fingerprint)** | A short code computed from the cleaned data. If one value in the data changes, the code changes. |

---

## What to post in the Optional Theme A thread

Post **one screenshot** of your comparison table or chart that includes your own run (on a Mac: Cmd + Shift + 4; on Windows: Windows + Shift + S). Add **120–200 words** answering:

1. **Which run would you send to QA, and why?** Not "the highest number": say *which* number you trusted and why the others mislead.
2. **Your own run.** What did you change, and what happened? If you changed only the split seed, what does that tell you about María's *"0.84 yesterday, 0.87 today"*?
3. **What is still missing?** Look at what MLflow recorded for each run. Six months from now, your manager asks *"which model is live, and who said it was good enough?"* What does this record answer, and what would you still need that MLflow did not capture here?

Then reply to one classmate whose choice differs from yours. As always, declare AI use, or state that no AI was used.

---

## If something goes wrong

| Problem | What to do |
|---|---|
| *"This notebook was not authored by Google"* | Click **Run anyway**. The notebook only uses Colab's own machine. |
| Text saying *"you may need to restart"* after Step 1 | Ignore it and carry on with Step 2. |
| Step 2 shows no **Choose files** button | Run the cell again. If the button still does not appear, open the folder icon on the left and drag `churn_raw.csv` into it, then run Step 2 again. |
| An error in red, or *"name 'df' is not defined"* | You probably skipped a cell. Run every cell from Step 1 again, in order. |
| Anything else, or Colab seems stuck | Menu **Runtime → Restart session**, then run all cells again from Step 1. |
| The Step 8 link shows a blank page or an error | Skip Step 8. Everything you need is in the Step 6 table. |
| Colab does not work at all on your computer | Open `MLOps_S04_MLflow_Lab_Example_Output.html` from the campus. It shows every result, and you can answer questions 1 and 3 from it. For question 2, comment on the example run D. |

Questions about the lab go in the Optional Theme A thread. Someone else will have had the same problem.
