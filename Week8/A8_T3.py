
def readValues(PfileName):
    NumList = []
    file = open(PfileName, "r")

    Row = file.readline()

    while Row != "":
        if Row != "\n":
            NumList.append(float(Row))

        Row = file.readline()

    file.close()
    return NumList


def AmountOfValues(PfileList):
    lenList = len(PfileList)
    return lenList


def CalculateSum(PfileList):
    total = 0

    for i in range(len(PfileList)):
        total += PfileList[i]

    return round(total, 1)


def CalculateAverage(PfileList):
    total = CalculateSum(PfileList)

    if len(PfileList) > 0:
        return round(sum(PfileList) / len(PfileList), 1)

    return 0


def ShowOptions():
    print("Options:\n1 - Read values\n2 - Amount of values\n3 - Calculate sum of values\n4 - Calculate average of values\n0 - Exit")


def AskChoice():
    choice = int(input("Your choice: "))
    return choice


def main():
    print("Program starting.")

    fileList = []
    total = 0

    while True:
        ShowOptions()
        choice = AskChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            fileName = input("Insert filename: ")
            fileList = readValues(fileName)

        elif choice == 2:
            print(f"Amount of values {AmountOfValues(fileList)}")

        elif choice == 3:
            total = CalculateSum(fileList)
            print(f"Sum of values {total}")

        elif choice == 4:
            if len(fileList) > 0:
                print(f"Average of values {CalculateAverage(fileList)}")
            else:
                print("No values available.")

        else:
            print("Unknown option!")

    print("\nProgram ending.")


main()

