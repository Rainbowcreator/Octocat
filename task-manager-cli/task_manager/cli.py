import sys
from task_manager.tasks import Task, TaskList


def main():
    task_list = TaskList()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            description = input("Enter task description: ")
            task = Task(description)
            task_list.add_task(task)
        elif choice == '2':
            task_list.list_tasks()
        elif choice == '3':
            task_list.list_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            task_list.complete_task(index)
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
