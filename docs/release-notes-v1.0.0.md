# Student Task Manager v1.0.0

First stable release of the Python Student Task Manager for CSC418 Lab Assignment 4.

## Features
- Add student tasks with nonempty validated titles and sequential IDs.
- List pending and completed tasks.
- Mark tasks complete and delete tasks by ID.
- Persist tasks locally to JSON.
- Handle invalid input with readable errors.

## Quality and development process
- Python `unittest` coverage for the three core operations and extra edge cases.
- GitHub Actions runs on pushes and pull requests to `main`.
- Three feature branches and five reviewed, merged pull requests.
- Deliberate README conflict documented and resolved.

## Get started
```bash
git clone https://github.com/salmanwaseem/student-task-manager.git
cd student-task-manager
python main.py
python -m unittest discover -s tests -v
```
