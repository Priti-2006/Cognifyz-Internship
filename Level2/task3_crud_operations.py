# ─────────────────────────────────────────
# Cognifyz Internship — Level 2, Task 3
# CRUD Operations on Task List
# ─────────────────────────────────────────

# This list will store all our tasks (acts as our "database")
tasks = []

# ── Task Class — defines what a "Task" looks like ──
class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.task_id}] {self.title} | {self.status}\n      → {self.description}"


# ── CREATE ──────────────────────────────
def create_task():
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()

    if not title:
        print("❌ Task title cannot be empty!")
        return

    # Auto-generate ID
    task_id = len(tasks) + 1
    new_task = Task(task_id, title, description)
    tasks.append(new_task)

    print(f"✅ Task '{title}' added successfully with ID {task_id}!")


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
    new_title = input(f"New title (leave blank to keep '{task_found.title}'): ").strip()
    new_desc = input(f"New description (leave blank to keep current): ").strip()
    new_status = input("New status (Pending/In Progress/Completed) or leave blank: ").strip()

    if new_title:
        task_found.title = new_title
    if new_desc:
        task_found.description = new_desc
    if new_status:
        task_found.status = new_status

    print(f"✅ Task ID {task_id} updated successfully!")


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
                print(f"🗑️ Task ID {task_id} deleted successfully!")
            else:
                print("❌ Deletion cancelled.")
            return

    print(f"❌ Task with ID {task_id} not found!")


# ── MAIN MENU ────────────────────────────
def display_menu():
    print("\n" + "="*45)
    print("        📋 TASK MANAGER (CRUD APP)")
    print("  Cognifyz Technologies Internship")
    print("="*45)
    print("  1. Create Task")
    print("  2. Read / View Tasks")
    print("  3. Update Task")
    print("  4. Delete Task")
    print("  5. Exit")
    print("="*45)

def main():
    print("\nWelcome to the Task Manager!")
    print("Developed for Cognifyz Technologies Internship")

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
            print("\n👋 Thank you for using Task Manager!")
            print("Cognifyz Technologies — Where Data Meets Intelligence")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-5.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()