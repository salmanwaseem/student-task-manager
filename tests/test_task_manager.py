"""Core behavior tests; completion and deletion begin as red tests."""
import unittest

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Python")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Study Python")
        self.assertFalse(task.completed)

    def test_complete_task(self):
        task = self.manager.add_task("Submit report")
        self.manager.complete_task(task.id)
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = self.manager.add_task("Old task")
        removed = self.manager.delete_task(task.id)
        self.assertEqual(removed.title, "Old task")
        self.assertEqual(self.manager.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()
