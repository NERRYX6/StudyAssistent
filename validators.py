def input_option_validator():
    while True:
        try:
            option = int(input("Choose an option:"))
            return option
        except ValueError:
            print("Invalid option")