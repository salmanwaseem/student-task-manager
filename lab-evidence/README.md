# Lab Evidence Checklist

Store actual screenshots here, for example:

- `01-repository-files.png` — repository main page and required files.
- `02-commit-history.png` — repository history showing at least 12 meaningful commits.
- `03-feature-branches.png` — branches list showing three feature branches.
- `04-issues.png` — at least four labeled Issues.
- `05-merged-pull-requests.png` — five merged PRs.
- `06-merge-conflict-before.png` — PR #10's conflict notice or actual terminal conflict markers.
- `07-merge-conflict-after.png` — resolved PR #10 and its merge commit.
- `08-actions-failed.png` — https://github.com/salmanwaseem/student-task-manager/actions/runs/44263434800
- `09-actions-passed.png` — https://github.com/salmanwaseem/student-task-manager/actions/runs/44263610867
- `10-release-v1.0.0.png` — release after publication.

**Important:** Images in this folder must be captured from actual GitHub pages or local Git commands; never manufacture evidence. A resolved PR no longer shows the pre-resolution warning, so if that warning was not captured at the time, document the genuine rejected merge attempt in LAB-REPORT.md and demonstrate a new local conflict for the 'before' screenshot.

Suggested terminal evidence:
```bash
git clone https://github.com/salmanwaseem/student-task-manager.git
cd student-task-manager
git status
git log --oneline --graph --all --decorate
git branch -a
python -m unittest discover -s tests -v
```
