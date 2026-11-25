
import Calculate


def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None


def askChoice() -> int:
    choice = int(input("Your choice: "))
    return choice


def askValue(PPrompt: str) -> float:
    value = float(input(PPrompt))
    return value


def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            firstValue = askValue("Insert first addend value: ")
            secondValue = askValue("Insert second addend value: ")
            result = Calculate.add(firstValue, secondValue)
            print(f"{firstValue} + {secondValue} = {result}")

        elif choice == 2:
            firstValue = askValue("Insert minuend value: ")
            secondValue = askValue("Insert subtrahend value: ")
            result = Calculate.subtract(firstValue, secondValue)
            print(f"{firstValue} - {secondValue} = {result}")

        elif choice == 3:
            firstValue = askValue("Insert multiplicant value: ")
            secondValue = askValue("Insert multiplier value: ")
            result = Calculate.multiply(firstValue, secondValue)
            print(f"{firstValue} * {secondValue} = {result}")

        elif choice == 4:
            firstValue = askValue("Insert dividend value: ")
            secondValue = askValue("Insert divisor value: ")

            if secondValue != 0:
                result = Calculate.divide(firstValue, secondValue)
                print(f"{firstValue} / {secondValue} = {result}")
            else:
                print("Cannot divide by zero!")

        else:
            print("Unknown option!")

    print("\nProgram ending.")


main()
