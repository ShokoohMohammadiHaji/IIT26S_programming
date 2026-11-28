
########################################################
# Task A9_T6
# Developer Shokooh Mohammadi
# Date 2026-11-28
########################################################

print("Program starting.")

lines = []

try:
    while True:
        print("Options:")
        print("1 - Insert line")
        print("2 - Save lines")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            text = input("Insert text: ")
            lines.append(text)
            print()

        elif choice == "2":
            filename = input("Insert filename: ")

            with open(filename, "w") as file:
                for line in lines:
                    file.write(line + "\n")

        elif choice == "0":
            break

        else:
            print("Unknown option!")
            print()

except KeyboardInterrupt:

    if len(lines) == 0:
        print("Closing suddenly.")

    else:
        print("Keyboard interrupt and unsaved progress!")

        answer = input("Save before quit(y/n)?: ")

        if answer.lower() == "y":
            filename = input("Insert filename: ")

            with open(filename, "w") as file:
                for line in lines:
                    file.write(line + "\n")

print("Program ending.")
