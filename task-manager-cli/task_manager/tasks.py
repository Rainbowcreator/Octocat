class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start = 1):
            status = '✓' if task.completed else ' '
            print(f"{index}. [{status}] {task.description}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Invalid task index.")
