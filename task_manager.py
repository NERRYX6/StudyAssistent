from ui import show_task

task_list = []

def add_task():
    task_list.append(str(input("Task Name: ")))

def show_tasks():
    if len(task_list) > 0:
        n=1
        for task in task_list:
            show_task(task, n)
            n+=1
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