from ui import show_task
from utils import add_time_mark
from file_manager import load_data

task_list = load_data("tasks")

def add_task():
    title = str(input("Task Name: "))
    comment = str(input("Comment: "))
    while True:
        try:
            deadline = int(input("Deadline at: "))
            break
        except ValueError:
            print("Invalid option")
    change = {"id": len(task_list),
              "title": title,
              "comment": comment,
              "deadline at": deadline,
              "status": False,
              "created at": add_time_mark(),
              "completed at": None
              }
    task_list[f"task{len(task_list)+1}"] = change

def show_tasks():
    if len(task_list) > 0:
        for i in range(len(task_list)):
            show_task(task_list[f"task{i+1}"]["title"], task_list[f"task{i+1}"]["id"]+1)
    else:
        print("No tasks, add a new task")

def delete_task():
    while True:
        try:
            option = int(input("Task Number to delete: "))
            del task_list[f"task{option}"]
            break
        except ValueError:
            print("Invalid option")
        except IndexError:
            print("Invalid option")
        except KeyError:
            print("Invalid option")

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