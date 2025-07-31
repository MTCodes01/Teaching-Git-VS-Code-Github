
class Task:
    def __init__(self, task , priority):
        self.task =task
        self.priority = priority

    def __str__(self):
        return f"{self.task}({self.priority})"
    
    def __repr__(self):
        return f"Task({self.task},{self.priority})"
    
class ToDoList:
    def __init__(self):
        self.task =[]

    def add_task(self, task):
        self.task.append(task)
    
    def delete_task(self,index):
        self.task.pop(index)

    def view_task(self):
        return [task for task in self.task]
    
if __name__ == "__main__":
    ToDoList = ToDoList()
    '''
    ToDoList.add_task(task("Task1","High"))
    ToDoList.add_task(task("Task2","low"))
    ToDoList.add_task(task("Task3","High"))
    ToDoList.add_task(task("Task4","medium"))
    
    print(ToDoList.task)

    for task in ToDoList.view_task():
        print(task)

    ToDoList.delete_task(1)
    '''

    while True:
        print("OPTIONS")
        print("1.Add\n2.Delete task\n3.View task\n4.Exit")

        chose = input("Enter your choice:")
        match chose:
            case "1":
                task = input("Enter the task name:")
                priority =input("Enter the priority:")
                ToDoList.add_task(Task(task , priority))

            case "2":
                idx = int(input("  Enter task index to delete:"))
                ToDoList.delete_task(idx)

            case "3":
                for task in ToDoList:
                    print(task)

            case "4":
                break

            case _:
                print("invalid input")
