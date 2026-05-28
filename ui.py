from validators import input_validator

main_menu_funcs = ['Tasks',
                   'Notes',
                   'Pomodoro Timer',
                   'Statistics',
                   'Save Data',
                   'Exit']

task_menu_funcs = ['Add Task',
                   'Show Tasks',
                   'Remove Task',
                   'Mark Task as completed',
                   'Edit Task',
                   'Search Task',
                   'Sort Tasks',
                   'Expired Tasks',
                   'Back']

note_menu_funcs = ['Add Note',
                   'Show Notes',
                   'Remove Note',
                   'Edit Note',
                   'Search Notes',
                   'Back']

Pomodoro_timer_menu_options = ['Set focus time',
                               'Set Break time',
                               'Back']

statistics_menu = ['Total tasks',
                   'Completed tasks',
                   'Active tasks',
                   'Overdue tasks',
                   'Pomodoro Timer',
                   'Most active subjects']

def show_main_menu():
    func_num = 1
    for func in main_menu_funcs:
        print(f"{func_num}. {func}")
        func_num += 1

    return input_validator()

def task_menu():
    func_num = 1
    for func in task_menu_funcs:
        print(f"{func_num}. {func}")
        func_num += 1

    return input_validator()


def notes_menu():
    func_num = 1
    for func in task_menu_funcs:
        print(f"{func_num}. {func}")
        func_num += 1

    return input_validator()


def pomodoro_menu():
    func_num = 1
    for func in task_menu_funcs:
        print(f"{func_num}. {func}")
        func_num += 1

    return input_validator()

def stats_menu():
    func_num = 1
    for func in statistics_menu:
        print(f"{func_num}. {func}")
        func_num += 1
    input("Press Enter to continue...")


