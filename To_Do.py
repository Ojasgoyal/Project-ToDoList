#To_do_list
import sys
import json

file = 'tasks.json'

def Loadtasks(file):
    try:
        with open(file, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, file):
    with open(file, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks are added")
        return
    
    print("\nYour Tasks")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    try:
        task = input("Enter Task: ")
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks, 'tasks.json')
        print("\nTask Added !")
        return
    except:
        print("Invalid Input")
        pass


def mark_task_complete(tasks):
    try:
        view_tasks(tasks)
        task_num = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print(f'Task "{tasks[task_num]["task"]}" marked as complete.')
            save_tasks(tasks,'tasks.json')
        else:
            print("Invalid task number.")
    except:
        print("Invalid Input")
        pass

def mark_task_incomplete(tasks):
    try:
        view_tasks(tasks)
        task_num = int(input("Enter the number of the task to renew : ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = False
            print(f'Task "{tasks[task_num]["task"]}" marked as undone.')
            save_tasks(tasks,'tasks.json')
        else:
            print("Invalid task number.")
    except:
        print("Invalid Input")
        pass

def delete_task(tasks):
    view_tasks(tasks)
    tasktodel = int(input("Enter task index you want to delete: ")) - 1
    try:
        if 0 <= tasktodel < len(tasks):
            deletedtask = tasks.pop(tasktodel)
            save_tasks(tasks, 'tasks.json')
            print(f'Task "{deletedtask["task"]}" deleted.')

        else:
            print("Invalid task number")
    except:
        print("Please enter a valid number.")

    
def main():
    tasks = Loadtasks('tasks.json')
    while True:
        try:
            print()
            print("*" * 100)
            print("TO DO APP")
            print("*" * 100)
            print("What would you like to do:")
            print("1. View tasks")
            print("2. Add a new task")
            print("3. Mark a task as Complete")
            print("4. Renew a Done Task")
            print("5. Delete a task")
            print("6. Exit")

            choice = int(input("Enter Choice : "))

            match choice:
                case 1:
                    view_tasks(tasks)
                case 2:
                    add_task(tasks)
                case 3:
                    mark_task_complete(tasks)
                case 4:
                    mark_task_incomplete(tasks)
                case 5:
                    delete_task(tasks)
                case 6:
                    raise EOFError
                case _:
                    raise ValueError
                
        except EOFError:
            sys.exit("\nExiting the To-Do List Manager. Goodbye!\n")
        except: 
            print("Invalid Input")
            pass              
                


if __name__ == "__main__":
    main()