import sys
from ui import *
from utils import *
from file_manager import *

def main():
    option = show_main_menu()

    while True:
        match option:
            case 1:
                task_menu()
            case 2:
                notes_menu()
            case 3:
                pomodoro_menu()
            case 4:
                stats_menu()
            case 5:
                save_data()
            case 6:
                return 0
            case _:
                print("You're out of range of menu, try again")
                pause()

if __name__ == "__main__":
    sys.exit(main())