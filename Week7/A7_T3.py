
def readFile(PfileName):
    Prows = []
    print(f'Reading file "{PfileName}".')
    solidFile = open(PfileName, "r", encoding="utf-8")
    
    solidFile.readline()  # Skip header

    for line in solidFile:
        line = line.strip()
        if line == "":
            continue
        Prows.append(line)

    solidFile.close()
    return Prows


def analyesTimestamps(Prows, PweekDay):
    print("Analysing timestamps.")
    weekDayCounter = []

    for day in PweekDay:
        dayCounter = 0

        for item in Prows:
            if item.startswith(day):
                dayCounter += 1

        weekDayCounter.append(dayCounter)

    return weekDayCounter


def displayResult(Pweekday, PweekDayCounter):
    print("Displaying results.")
    print("### Timestamp analysis ###")

    for i in range(len(Pweekday)):
        print(f" - {Pweekday[i]} {PweekDayCounter[i]} stamps")

    print("### Timestamp analysis ###")


def main():
    rows = []
    weekDay = ("Monday", "Tuesday", "Wednesday", "Thursday",
               "Friday", "Saturnday", "Sunday")

    print("Program starting.")
    fileName = input("Insert filename: ")

    rows = readFile(fileName)
    weekDayCounter = analyesTimestamps(rows, weekDay)
    displayResult(weekDay, weekDayCounter)

    print("Program ending.")


main()
