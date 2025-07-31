class Task:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority

    def __str__(self):
        return f"{self.task} ({self.priority})"
    
    def __repr__(self):
        return f"{self.task} at {self.priority} priority"
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        else:
            return -1

    def view_tasks(self):
        return self.tasks

if __name__ == "__main__":
    todolist = ToDoList()

    condition = True
    while condition:
        print("\n====OPTIONS====")
        print("1) Add Task")
        print("2) Delete Task")
        print("3) View Tasks")
        print("4) Exit")

        choice = input("\nEnter a choice: ")
        match choice:
            case "1":
                task = input("  Enter Task name: ")
                priority = input("  Enter Task Priority: ")
                todolist.add_task(Task(task, priority))
            
            case "2":
                idx = int(input("  Enter Task index to delete: "))
                deleted = todolist.delete_task(idx)
                if deleted == -1:
                    print("\nInvalid Index given, Try Again!")
                else:
                    print(f"\nDeleted {deleted.task} with {deleted.priority} priority!")

            case "3":
                print("")
                for task in todolist.view_tasks():
                    print(task)

            case "4":
                condition = False

            case _:
                print("\nInvalid Option\n")