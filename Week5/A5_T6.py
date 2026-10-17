def main():
    print("Program starting.")
    runProgram ()
    print("Program ending.")

def showOptions():
    print("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")

def askChoice():
    Pchoice = input("Your choice: ")
    if Pchoice.isnumeric():
        if 0 <= int(Pchoice) < 4:
            return int(Pchoice)
        else:
            print("Unknown option!\n")
    else:
        print("Unknown option!\n")

def runProgram ():
    count = 0
    while (True):
        showOptions()
        choice = askChoice()
        if choice == 1:
            print (f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!\n")
        elif choice == 3:
            count = 0
            print("Cleared count!\n")
        elif choice ==0 :
            print("Exiting program.\n")
            break
main()