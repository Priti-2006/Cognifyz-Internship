# ─────────────────────────────────────────
# Cognifyz Internship — Level 3, Task 5
# CRUD Application with File Storage (File I/O)
# ─────────────────────────────────────────

import os

FILENAME = "tasks_data.txt"
tasks = []


# ── Task Class ──────────────────────────
class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.task_id}] {self.title} | {self.status}\n      → {self.description}"

    # Convert task to a single line for saving in file
    def to_file_line(self):
        return f"{self.task_id}|{self.title}|{self.description}|{self.status}\n"


# ── LOAD TASKS FROM FILE (runs when program starts) ──
def load_tasks():
    global tasks
    tasks = []

    if not os.path.exists(FILENAME):
        print("📁 No previous data found. Starting fresh.")
        return

    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 4:
                        task_id, title, description, status = parts
                        task = Task(int(task_id), title, description, status)
                        tasks.append(task)
        print(f"✅ Loaded {len(tasks)} task(s) from file.")
    except Exception as e:
        print(f"❌ Error loading file: {e}")


# ── SAVE TASKS TO FILE (runs after every change) ──
def save_tasks():
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task.to_file_line())
    except Exception as e:
        print(f"❌ Error saving file: {e}")


# ── CREATE ──────────────────────────────
def create_task():
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()

    if not title:
        print("❌ Task title cannot be empty!")
        return

    task_id = (max([t.task_id for t in tasks]) + 1) if tasks else 1
    new_task = Task(task_id, title, description)
    tasks.append(new_task)

    save_tasks()  # Save to file immediately
    print(f"✅ Task '{title}' added and saved to file with ID {task_id}!")


# ── READ ─────────────────────────────────
def read_tasks():
    print("\n--- All Tasks ---")
    if not tasks:
        print("📭 No tasks found. Add a task first!")
        return

    for task in tasks:
        print(task)
        print("-" * 40)


# ── UPDATE ───────────────────────────────
def update_task():
    print("\n--- Update Task ---")
    if not tasks:
        print("📭 No tasks available to update!")
        return

    read_tasks()
    try:
        task_id = int(input("\nEnter Task ID to update: "))
    except ValueError:
        print("❌ Invalid ID!")
        return

    task_found = None
    for task in tasks:
        if task.task_id == task_id:
            task_found = task
            break

    if not task_found:
        print(f"❌ Task with ID {task_id} not found!")
        return

    print(f"\nUpdating: {task_found.title}")
    new_title = input(f"New title (leave blank to keep current): ").strip()
    new_desc = input(f"New description (leave blank to keep current): ").strip()
    new_status = input("New status (Pending/In Progress/Completed) or leave blank: ").strip()

    if new_title:
        task_found.title = new_title
    if new_desc:
        task_found.description = new_desc
    if new_status:
        task_found.status = new_status

    save_tasks()  # Save to file immediately
    print(f"✅ Task ID {task_id} updated and saved to file!")


# ── DELETE ───────────────────────────────
def delete_task():
    print("\n--- Delete Task ---")
    if not tasks:
        print("📭 No tasks available to delete!")
        return

    read_tasks()
    try:
        task_id = int(input("\nEnter Task ID to delete: "))
    except ValueError:
        print("❌ Invalid ID!")
        return

    for task in tasks:
        if task.task_id == task_id:
            confirm = input(f"Are you sure you want to delete '{task.title}'? (y/n): ").lower()
            if confirm == 'y':
                tasks.remove(task)
                save_tasks()  # Save to file immediately
                print(f"🗑️ Task ID {task_id} deleted and file updated!")
            else:
                print("❌ Deletion cancelled.")
            return

    print(f"❌ Task with ID {task_id} not found!")


# ── MAIN MENU ────────────────────────────
def display_menu():
    print("\n" + "="*50)
    print("   📋 TASK MANAGER WITH FILE STORAGE")
    print("   Cognifyz Technologies Internship")
    print("="*50)
    print("  1. Create Task")
    print("  2. Read / View Tasks")
    print("  3. Update Task")
    print("  4. Delete Task")
    print("  5. Exit")
    print("="*50)

def main():
    print("\nWelcome to the Task Manager (with File Storage)!")
    print("Developed for Cognifyz Technologies Internship")

    load_tasks()  # Load saved tasks when program starts

    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\n👋 All data saved! Thank you for using Task Manager!")
            print("Cognifyz Technologies — Where Data Meets Intelligence")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-5.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()