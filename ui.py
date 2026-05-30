from validators import input_validator
import utils
import menu_functions

def show_menu(options):
    func_num = 1
    for func in options:
        print(f"{func_num}. {func}")
        func_num += 1

    return input_validator() if options != menu_functions.statistics_menu else utils.pause()