# Student Task Manager — User Guide

## Requirements
Python 3.11 or newer. No third-party dependencies.

## Start
From the project directory run `python main.py`. The menu offers five choices:

1. **Add task:** enter a non-empty task title. Surrounding whitespace is removed.
2. **Display tasks:** show each task's stable numeric ID and `[ ]` pending or `[x]` completed status.
3. **Complete task:** enter an existing positive integer ID to mark it complete.
4. **Delete task:** enter an existing positive integer ID to remove it.
5. **Exit:** end the interactive session.

Example:
```text
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
Choose an option (1-5): 1
Task title: Study Python
Added task #1: Study Python
```

## Data and errors
Tasks are stored automatically in `tasks.json`, which is ignored by Git. Restart the application to see stored tasks. Missing IDs and invalid input display error messages without stopping the menu. Deleting a task does not renumber existing IDs.

## Run tests
```bash
python -m unittest discover -s tests -v
```
The repository's GitHub Actions workflow also runs these tests on pushes and pull requests to `main`.
