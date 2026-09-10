from ui import show_task
from utils import add_time_mark

task_list = []

def add_task():
    title = str(input("Task Name: "))
    comment = str(input("Comment: "))
    while True:
        try:
            deadline = int(input("Deadline at: "))
            break
        except ValueError:
            print("Invalid option")

    task_list.append({"id": len(task_list),
                      "title": title,
                      "comment": comment,
                      "deadline at": deadline,
                      "status": False,
                      "created at": add_time_mark(),
                      "completed at": None
                      })

def show_tasks():
    if len(task_list) > 0:
        for task in task_list:
            show_task(task["title"], task["id"]+1)
    else:
        print("No tasks, add a new task")

def delete_task():
    while True:
        try:
            option = int(input("Task Number to delete: "))
            break
        except ValueError:
            print("Invalid option")
        except IndexError:
            print("Invalid option")
    task_list.pop(option-1)

def complete_task():
    return 0

def edit_task():
    return 0

def search_task():
    return 0

def sort_tasks():
    return 0

def expired_tasks():
    return 0