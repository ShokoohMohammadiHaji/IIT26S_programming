
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


def displayResult(Prows):
    print("Electricity usage:")

    for item in range(len(Prows)):
        print(f" - {Prows[item][0]} {Prows[item][1]}, price {float(Prows[item][3]):.2f} €, consumption {float(Prows[item][2]):.2f} kWh, total {Prows[item][4]:.2f} €")


def calculateTotal(Prows):
    for item in range(len(Prows)):
        Prows[item] = Prows[item].split(";")

        total = float(Prows[item][2]) * float(Prows[item][3])

        Prows[item].append(total)

    return Prows


def main():
    rows = []

    print("Program starting.")
    fileName = input("Insert filename: ")

    rows = readFile(fileName)

    rows = calculateTotal(rows)

    displayResult(rows)

    print("Program ending.")


main()
