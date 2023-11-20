def exit(message=None):
    while True:
        leaving = input("Would you like to leave? (Y/N): ").upper()
        if leaving == "":
            print("Please enter a valid input.")
        elif leaving == "Y" and message != None:
            print(message)
            return True
        elif leaving == "Y" and message == None:
            print("Thanks for using the program!")
            return True
        else:
            return False
