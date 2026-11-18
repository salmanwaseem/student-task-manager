"""Task storage and operations for the Student Task Manager."""
from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass
class Task:
    """One student task."""

    id: int
    title: str
    completed: bool = False


class TaskManager:
    """Manage tasks in memory, optionally saving them as JSON."""

    def __init__(self, storage_file=None):
        self.storage_file = Path(storage_file) if storage_file is not None else None
        self.tasks = []
        self.next_id = 1
        if self.storage_file and self.storage_file.exists():
            self._load()

    def _load(self):
        data = json.loads(self.storage_file.read_text(encoding="utf-8"))
        self.tasks = [Task(**item) for item in data.get("tasks", [])]
        self.next_id = max((task.id for task in self.tasks), default=0) + 1

    def _save(self):
        if self.storage_file is None:
            return
        self.storage_file.parent.mkdir(parents=True, exist_ok=True)
        payload = {"tasks": [asdict(task) for task in self.tasks]}
        self.storage_file.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    def add_task(self, title):
        """Add a task and return it. Validation is developed in a feature branch."""
        if not isinstance(title, str):
            raise ValueError("Task title must be text.")
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Task title cannot be empty.")
        task = Task(self.next_id, clean_title)
        self.tasks.append(task)
        self.next_id += 1
        self._save()
        return task

    def list_tasks(self):
        """Return all tasks ordered by creation."""
        return list(self.tasks)

    def _find_task(self, task_id):
        if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive integer.")
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"No task exists with ID {task_id}.")

    def complete_task(self, task_id):
        """Implemented in feature/complete-task."""
        raise NotImplementedError("Task completion is not available yet.")

    def delete_task(self, task_id):
        """Implemented in feature/delete-task."""
        raise NotImplementedError("Task deletion is not available yet.")
