# Student Task Manager

A Python 3 console application to add, display, complete, and delete student tasks. Built for COMSATS University Islamabad, Lahore Campus, CSC418 Lab Assignment 4.

Project status: Ready for release

## Features

- Add tasks with automatically assigned stable numeric IDs.
- Reject empty, blank or non-text titles; trim surrounding whitespace.
- Display all tasks with pending `[ ]` or completed `[x]` indicators.
- Complete or delete tasks by a validated positive integer ID.
- Save and restore tasks automatically in local `tasks.json`.
- Show friendly errors for invalid menu selections and IDs.
- Run automated `unittest` checks with GitHub Actions.

## Setup

Install Python 3.11+ and Git. Clone the repository:

```bash
git clone https://github.com/salmanwaseem/student-task-manager.git
cd student-task-manager
```

No external packages are required.

## Run the program

```bash
python main.py
```

Select 1 to add a title, 2 to list tasks, 3 to mark a task complete, 4 to delete by ID, or 5 to exit.

Example display:
```text
1. [ ] Study Python
2. [x] Submit lab report
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

The GitHub Actions workflow at `.github/workflows/tests.yml` tests every pull request targeting `main` and every push to `main`.

## Git and GitHub evidence

The repository was developed through meaningful commits and the following branches:

- `feature/add-task` — input validation; merged through PR #6
- `feature/complete-task` — completed status; merged through PR #7
- `feature/delete-task` — deletion by ID; merged through PR #8
- `conflict/status-testing` — first README status change; PR #9
- `conflict/status-ready` — competing README change; PR #10

The two conflict branches changed `Project status: Planning` in incompatible ways. GitHub rejected the second merge until the conflict was resolved in a merge commit preserving the README and both histories. See PR #10.

See [User Guide](docs/user-guide.md), [Lab Report](LAB-REPORT.md), and [Evidence Checklist](lab-evidence/README.md).

## License

MIT License (see [LICENSE](LICENSE)).
