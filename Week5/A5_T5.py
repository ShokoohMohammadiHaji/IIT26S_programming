
def main():
    print("Program starting.")
    wordProgram()
    print("Program ending.")

def wordProgram():
    word = ""
    while True:
        print("Options:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            word = input("Insert word: ")
            print()
        elif choice == "2":
            print(f'Current word - "{word}"\n')
        elif choice == "3":
            print(f'Word reversed - "{word[::-1]}"\n')
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Unknown option! Try again.\n")

main()
