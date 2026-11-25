
import TimestampLibrary


def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")
    return None


def AskChoice():
    choice = int(input("Your choice: "))
    return choice


def main():
    print("Program starting.")

    fileName = input("Insert filename: ")

    Timestamps = []
    TimestampLibrary.readTimestamps(fileName, Timestamps)

    while True:
        showOptions()
        choice = AskChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            year = int(input("Insert year: "))

            years = TimestampLibrary.calculateYears(year, Timestamps)

            print(f"Amount of timestamps during year '{year}' is {years}")

        elif choice == 2:
            monthName = input("Insert month: ")

            months = TimestampLibrary.calculateMonths(monthName, Timestamps)

            print(f"Amount of timestamps during month '{monthName}' is {months}")

        elif choice == 3:
            weekday = input("Insert weekday: ")

            weekdays = TimestampLibrary.calculateWeekdays(weekday, Timestamps)

            print(f"Amount of timestamps during weekday '{weekday}' is {weekdays}")

        else:
            print("Unknown option!")

    print("\nProgram ending.")


main()
