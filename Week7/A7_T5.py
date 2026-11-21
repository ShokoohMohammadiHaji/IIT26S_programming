
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


def calculateTotal(Prows, PweekDay):
    for item in range(len(Prows)):
        Prows[item] = Prows[item].split(";")

    print("Analysing timestamps.")

    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for day in PweekDay:
        totalconsumption = 0
        totalcost = 0

        for i in range(len(Prows)):
            if day == Prows[i][0]:
                totalconsumption += float(Prows[i][2])
                totalcost += float(Prows[i][2]) * float(Prows[i][3])

        print(f" - {day} usage {totalconsumption:.2f} kWh, cost {totalcost:.2f} €")

    print("### Electricity consumption summary ###")

    return Prows


def main():
    weekDay = ("Monday", "Tuesday", "Wednesday", "Thursday",
               "Friday", "Saturnday", "Sunday")

    print("Program starting.")
    fileName = input("Insert filename: ")

    rows = readFile(fileName)

    rows = calculateTotal(rows, weekDay)

    print("Program ending.")


main()
