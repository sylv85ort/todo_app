class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added.")

    def mark_task_done(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task '{task}' marked as done.")
        else:
            print("Invalid task number.")

    def view_pending_tasks(self):
        print("\nPending Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def delete_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.startswith("[Done]")]
        for task in completed_tasks:
            self.tasks.remove(task)
        self.save_tasks()
        print("Completed tasks deleted.")
