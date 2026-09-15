from ui import show_task
from file_manager import load_data

task_info = load_data()
task_id = task_info["task_ID"]
task_list = task_info["tasks"]

def add_task():
    global task_id

    title = str(input("Task Name: "))
    comment = str(input("Comment: "))
    change = {"id": task_id,
              "title": title,
              "comment": comment,
              "completed": False
              }

    task_id += 1
    task_list[f"{task_id+1}"] = change

def show_tasks():
    num = 1

    if len(task_list) > 0:
        for task in task_list.values():
            show_task(task["title"], num)
            num += 1
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