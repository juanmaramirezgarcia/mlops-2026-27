# Session 1 · Live demo script: "what versioning looks like"

**Slot:** minutes 31–35 (slide 16 "One habit underneath all of this", then slide 17 "What you just saw")
**Duration:** 4 minutes, browser only, no commands typed
**Repository:** `https://github.com/juanmaramirezgarcia/mlops-demo-churn` (created with `demo/setup_demo_repo.sh`)

---

## 1. Why not `mlops_course_materials`

I checked the existing repository. It is public and clones fine, but it does not show the three things the slide promises:

| The slide promises | What `mlops_course_materials` shows |
|---|---|
| Every change has an author, a date and a **reason** | 20 of 24 commits are titled "Add files via upload" (GitHub's web-upload default); the reason is never stated |
| A **diff** you can read | Commits upload whole notebooks and CSV files; the browser shows thousands of changed lines of JSON |
| A **tag** that names the production version | No tags, no releases |

The only readable commit (`fixed Wine\score.py`, a one-line change) is from April 2022 and buried under three years of uploads. Keep that repository for what it is (the MLflow, LIME and SHAP notebooks used in later demos) and use a purpose-built one for this demo.

## 2. The demo repository: `mlops-demo-churn`

Seven commits that tell the same story as the session, and two tags:

| Date | Commit | What to say |
|---|---|---|
| 14 Jan | Add churn model: training script and sample data | "The data scientist's first version. Accuracy 0.91." |
| 2 Feb | Add data validation: stop training if required columns are missing | "The first control: the pipeline now refuses bad data." |
| 19 Feb | **Fix: reject extracts where a feature arrives mostly empty** | "NorthRetail's bug, caught. Read the message: it says *why*." |
| 20 Feb | Add tests for the validation rules | "Nobody has to remember to check; the check is code." |
| 3 Mar · **v1.0** | Add model card with owner, training data and retrain trigger | "Before production: who is accountable, and when it must be retrained." |
| 9 Jun · **v1.1** | Retrain on Q2 data and add promotion feature | "The world changed in March; the model caught up in June, and the history says so." |
| 10 Jun | Add CI: run the tests and a training dry-run on every push | "We come back to this in Session 5." |

### One-time setup (10 minutes, before the session)

```bash
# On your laptop, in any folder
bash setup_demo_repo.sh            # creates ./mlops-demo-churn with the 7 commits and 2 tags
cd mlops-demo-churn
python -m pytest -q                # optional: 3 passed
```

Then on GitHub: **New repository** → name `mlops-demo-churn` → Public → leave README, .gitignore and licence **unticked** → Create. Back in the terminal:

```bash
git remote add origin https://github.com/juanmaramirezgarcia/mlops-demo-churn.git
git push -u origin main --tags
```

Within a minute GitHub Actions runs the CI workflow and a green tick appears next to the last commit. Check the four URLs below open before class and keep them as bookmarks in the order you will click them.

Notes on the script: the commits are back-dated to Jan–Jun 2026 so the history reads like a real project and `v1.0` lands on 3 March, the date used on the slide; run with `BACKDATE=no bash setup_demo_repo.sh` if you prefer real timestamps. Author name and e-mail default to yours; override with `AUTHOR_NAME="…" AUTHOR_EMAIL="…"`.

---

## 3. The four minutes, click by click

Open the four tabs before the session. Share the browser window, not the whole screen. Zoom the browser to 125–150% so the back rows can read.

### Tab 1 · The history (≈ 1 min)
`https://github.com/juanmaramirezgarcia/mlops-demo-churn/commits/main`

> "This is a repository: a folder with a memory. Every line here is one change. Look at what each line has: **who** made it, **when**, and a sentence saying **why**. Seven changes, six months. Read the messages from the bottom up: first version, then validation, then a fix, then tests, then a model card, then a retrain. You can reconstruct the whole life of the model without opening a single file."

Point at the green tick on the top commit: "We'll come back to that tick in Session 5."

### Tab 2 · The diff (≈ 1.5 min)
Click the commit **"Fix: reject extracts where a feature arrives mostly empty"** (19 Feb) → the diff view.
Direct link: `https://github.com/juanmaramirezgarcia/mlops-demo-churn/commit/d503ae0f1fb7fa9e0daad0721e11328674a0b87b`

> "This is a diff: exactly what changed, and nothing else. Eleven green lines. Read the comment at the top: *empty values used to be filled with zero, which the model read as a customer with zero months of tenure.* Does that sound familiar? It is the NorthRetail failure from the case you will diagnose after the break. Here it was caught, and the history says on which day, by whom, and why."

Scroll up to the commit message: "The message is written for the person who reads this in a year. That person is usually you."

### Tab 3 · The tag (≈ 1 min)
`https://github.com/juanmaramirezgarcia/mlops-demo-churn/tags`

> "A tag names a moment. **v1.0, 3 March**: this exact set of files went to production. **v1.1, 9 June**: this one replaced it. When the regulator, or the board, asks *which model was live in April?*, the answer is not a guess and not an e-mail search. It is v1.0, and you can open it."

Click **v1.0** → "Browse files" (or the commit link) to show the model card: "Owner, training data, accuracy, retrain trigger: that is what 'ready for production' means. Session 12 is about this document."

### Tab 4 · Back to the history (≈ 30 s)
Return to tab 1.

> "Three things: a history that says who, when and why; a diff that shows exactly what; a tag that says which version was live. Everything else in this course, pipelines, deployment, monitoring, governance, is built on this habit. No commands, no code: a folder with a memory."

Switch to slide 17, "What you just saw".

---

## 4. If something goes wrong

| Problem | Do this |
|---|---|
| No internet / GitHub down | Show the three screenshots in `demo/screenshots/` (take them once after pushing: history, the fix diff, the tags page) and read the same script. |
| The CI tick is red | Ignore it today; say "that cross is a story for Session 5". Fix afterwards: open the Actions tab, read the log. |
| Students ask "what is Python?" | "A programming language; you do not need to read the code, only the green and red lines and the messages." |
| A student asks to see the model itself | Open `src/train.py` at `v1.0`: "Twenty lines. The model is the small box in the middle; the history is the rest." |

---

## 5. Checklist

- [ ] `setup_demo_repo.sh` run; `pytest` passes locally
- [ ] Empty public repo created on GitHub; `git push -u origin main --tags` done
- [ ] CI run finished (green tick on the latest commit)
- [ ] Four tabs bookmarked in click order; commit hash of the "Fix" commit copied into tab 2's URL
- [ ] Screenshots of the three pages saved as the offline fallback
- [ ] Browser zoom at 125–150%; notifications off
