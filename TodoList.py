


tasks = []

def show_menu():
    print("\n==== To-Do List ====")
    print("1.add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("📭 No tasks added yet.")
        return
    for i, t in enumerate(tasks):
        status = "✔️ Done" if t["done"] else "❌ Not Done"
        print(f"{i+1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("🎉 Task marked as done!")
    except:
        print("⚠️ Invalid input!")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("🗑️ Task deleted!")
    except:
        print("⚠️ Invalid input!")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")