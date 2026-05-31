from validators import input_option_validator
import utils
import menu_functions

def show_menu(options):
    utils.clear()
    func_num = 1
    for func in options:
        print(f"{func_num}. {func}")
        func_num += 1

    return input_option_validator() if options != menu_functions.statistics_menu else utils.pause()

def show_task(task, number):
    print(f"{number}. {task}")