"""Interactive console for Student Task Manager."""
from task_manager import TaskManager


def ask_id():
    try:
        return int(input("Task ID: ").strip())
    except ValueError as exc:
        raise ValueError("Enter a whole-number task ID.") from exc


def main():
    manager = TaskManager("tasks.json")
    while True:
        print("\n=== Student Task Manager ===")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                task = manager.add_task(input("Task title: "))
                print(f"Added task #{task.id}: {task.title}")
            elif choice == "2":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks yet.")
                for task in tasks:
                    marker = "x" if task.completed else " "
                    print(f"{task.id}. [{marker}] {task.title}")
            elif choice == "3":
                task = manager.complete_task(ask_id())
                print(f"Completed task #{task.id}.")
            elif choice == "4":
                task = manager.delete_task(ask_id())
                print(f"Deleted task #{task.id}: {task.title}")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Choose a number from 1 to 5.")
        except (ValueError, KeyError, NotImplementedError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
