# MLOps — Master in Business Analytics and Data Science (Part-Time) · MBDS-PT2026F · 2026–27

Course materials for *MLOps: Machine Learning Operations*, IE School of Science & Technology.
Five live sessions, five discussion forums, and two self-paced video lessons, plus their demos, activities and knowledge checks.

## Layout

| Folder | What it holds |
|---|---|
| `2026-27/` | This edition's materials, one folder per session (`S01`–`S12`): decks (`.pptx` with speaker notes), activity briefs, demo scripts, forum packs, video guides, and runnable demo assets. See `2026-27/README.md` for the per-session index. |
| `00_Plan_and_Syllabus/` | The course preparation plan and the syllabus. |
| `2025-26_previous_edition/` | Last year's decks, kept for reference. |

## Conventions

- **Decks** are `.pptx` with speaker notes carrying the minute marks; appendix slides after the closing trio are marked "not examinable".
- **Documents** are Markdown (`.md`); the plan also has a `.docx`.
- **Demos** live in a `demo/` (or `deploy_lab/`) folder inside the session, each with a click-by-click script and a fallback.
- **Naming:** `MLOps_S<nn>_<what>.<ext>`.

## What is not in the repo (and why)

Machine-generated or heavy state is git-ignored because committed scripts rebuild it:

- Python virtual environments (`**/.venv/`) — rebuilt by the `*.command` launchers.
- MLflow run state (`**/mlruns/`, `**/mlflow.db`) — rebuilt by the demo setup scripts.
- Python and test caches, `.DS_Store`, and `_to_delete/` scrap.
- `2026-27/S01/demo/mlops-demo-churn/` — the GitHub demo repository, which lives in its own repo.

Pre-rendered demo assets (small models, CSVs, drift/eval reports, screenshots) **are** kept so the demos work without running anything first.
