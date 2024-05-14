from todo import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. View Pending Tasks")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_done(index)
        elif choice == '3':
            todo_list.view_pending_tasks()
        elif choice == '4':
            todo_list.delete_completed_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
