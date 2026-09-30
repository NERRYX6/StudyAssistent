from ui import show_task
from file_manager import load_data
from validators import input_option_validator

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

    task_list[str(task_id)] = change
    task_id = task_id + 1
    task_info["task_ID"] = task_id

def show_tasks():
    if len(task_list) > 0:
        for key, task in task_list.items():
            show_task(task["title"], key)
    else:
        print("No tasks, add a new task")

def delete_task():
    show_tasks()
    while True:
        try:
            option = int(input("Task Number to delete: "))
            del task_list[str(option)]
            break
        except ValueError:
            print("Invalid option")
        except IndexError:
            print("Invalid option")
        except KeyError:
            print("Invalid option")

def complete_task():
    show_tasks()
    task = input_option_validator()
    try:
        task_list[task]["completed"] = True
    except KeyError:
        print("Invalid option")


def edit_task():
    return 0