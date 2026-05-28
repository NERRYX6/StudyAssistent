def input_validator():
    try:
        option = int(input("Choose an option:"))
        return option
    except ValueError:
        print("Invalid option")