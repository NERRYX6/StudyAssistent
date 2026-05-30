from ui import show_task

task_list = []

def add_task():
    return 0

def show_tasks():
    if len(task_list) > 0:
        n=1
        for task in task_list:
            show_task(task, n)
            n+=1
    else:
        print("No tasks, add a new task")

def delete_task():
    return 0

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