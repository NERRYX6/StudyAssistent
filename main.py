import sys
from ui import show_menu
from utils import out_of_range, end_of_menu
from file_manager import save
from menu_functions import *
import task_manager
import notes_manager
import pomodoro
import statistics_manager

def main():

    while True:
        option =  show_menu(main_menu_funcs)

        match option:
            case 1:
                while True:
                    option = show_menu(task_menu_funcs)
                    match option:
                        case 1:
                            task_manager.add_task()
                        case 2:
                            task_manager.show_tasks()
                        case 3:
                            task_manager.delete_task()
                        case 4:
                            task_manager.complete_task()
                        case 5:
                            task_manager.edit_task()
                        case 6:
                            task_manager.search_task()
                        case 7:
                            task_manager.sort_tasks()
                        case 8:
                            task_manager.expired_tasks()
                        case 9:
                            break
                        case _:
                            out_of_range()
                    end_of_menu()
            case 2:
                while True:
                    option = show_menu(note_menu_funcs)
                    match option:
                        case 1:
                            notes_manager.create_note()
                        case 2:
                            notes_manager.show_notes()
                        case 3:
                            notes_manager.delete_note()
                        case 4:
                            notes_manager.edit_note()
                        case 5:
                            notes_manager.search_notes()
                        case 6:
                            break
                        case _:
                            out_of_range()
                    end_of_menu()
            case 3:
                while True:
                    option = show_menu(pomodoro_timer_menu_options)
                    match option:
                        case 1:
                            pomodoro.set_focus_time()
                        case 2:
                            pomodoro.set_break_time()
                        case 3:
                            break
                        case _:
                            out_of_range()
                    end_of_menu()
            case 4:
                statistics_manager.show_stats()
                end_of_menu()
            case 5:
                save()
            case 6:
                return 0
            case _:
                out_of_range()

if __name__ == "__main__":
    sys.exit(main())