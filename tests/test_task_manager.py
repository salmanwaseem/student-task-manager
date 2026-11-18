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

    def test_reject_blank_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_unknown_or_invalid_task_id(self):
        self.manager.add_task("Existing")
        for invalid in (0, -1, True, "1"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    self.manager.complete_task(invalid)
        with self.assertRaises(KeyError):
            self.manager.delete_task(99)

    def test_deleting_does_not_reuse_ids(self):
        first = self.manager.add_task("First")
        self.manager.delete_task(first.id)
        later = self.manager.add_task("Later")
        self.assertEqual(later.id, 2)


if __name__ == "__main__":
    unittest.main()
