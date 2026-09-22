tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓ Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    # Complete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print(f"Deleted: {deleted['task']}")
            else:
                print("Invalid task number.")
    # Exit
    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")