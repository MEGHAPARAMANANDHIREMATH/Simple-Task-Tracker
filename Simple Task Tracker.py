class TaskTracker:
    def __init__(self):
        self.tasks = {}

    def add_new_task(self, task_id, task_name, status="Pending"):
        if task_id in self.tasks:
            print("Task ID already exists.")
        else:
            self.tasks[task_id] = {"task_name": task_name, "status": status}
            print(f"Task {task_id} added successfully.")

    def update_task_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = status
            print(f"Task {task_id} status updated to {status}.")
        else:
            print("Task ID does not exist.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted successfully.")
        else:
            print("Task ID does not exist.")

    def get_task(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id]
        else:
            return "Task ID does not exist."

    def display_all_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"Task ID: {task_id}, Task Name: {task['task_name']}, Status: {task['status']}")

# Example usage
tracker = TaskTracker()

while True:
    print("\nTask Tracker Menu:")
    print("1. Add new task")
    print("2. Update task status")
    print("3. Delete task")
    print("4. Get task details")
    print("5. Display all tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_id = input("Enter task ID: ")
        task_name = input("Enter task name: ")
        tracker.add_new_task(task_id, task_name)
    elif choice == "2":
        task_id = input("Enter task ID: ")
        status = input("Enter new status: ")
        tracker.update_task_status(task_id, status)
    elif choice == "3":
        task_id = input("Enter task ID: ")
        tracker.delete_task(task_id)
    elif choice == "4":
        task_id = input("Enter task ID: ")
        print(tracker.get_task(task_id))
    elif choice == "5":
        tracker.display_all_tasks()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

