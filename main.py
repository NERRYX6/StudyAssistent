"""Task structure
      ↓
Add / Show / Remove
      ↓
Complete / Edit
      ↓
JSON saving/loading
      ↓
Search / Sort / Expired
"""

import sys

from ui import show_menu
from utils import out_of_range, end_of_menu
from file_manager import save
from menu_functions import *
from task_manager import task_list
import task_manager

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
                            save(task_list, "tasks")
                        case 5:
                            task_manager.complete_task()
                        case 6:
                            task_manager.edit_task()
                        case 7:
                            break
                        case _:
                            out_of_range()
                    end_of_menu()
            case 2:
                save(task_list, "tasks")
            case 3:
                return 0
            case _:
                out_of_range()

if __name__ == "__main__":
    sys.exit(main())