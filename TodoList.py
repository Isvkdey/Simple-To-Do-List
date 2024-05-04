def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.append(task)

def view_tasks(todo_list):
    if todo_list:
        print("To-Do List:")
        for task in todo_list:
            print(task)
    else:
        print("To-Do List is empty.")

def remove_task(todo_list):
    if todo_list:
        print("Current To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(todo_list):
            removed_task = todo_list.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    else:
        print("To-Do List is empty.")

def todo_list_app():
    todo_list = []

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    todo_list_app()
