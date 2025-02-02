import unittest
from task_manager.tasks import Task, TaskList


class TestTask(unittest.TestCase):
    def test_mark_completed(self):
        task = Task("Test task")
        task.mark_completed()
        self.assertEqual(task.completed, True)


class TestTaskList(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()
        self.task = Task("Test task")
        self.task_list.add_task(self.task)

    def test_list_tasks(self):
        self.task_list.list_tasks()

    def test_complete_task(self):
        self.task_list.complete_task(0)
        self.assertEqual(self.task.completed, True)


if __name__ == '__main__':
    unittest.main()
