import os

def pause():
    input("Press any key to continue...")

def out_of_range():
    print("You're out of range of menu, try again")
    pause()

def clear():
    os.system("cls")