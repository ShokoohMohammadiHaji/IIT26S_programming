
def readValues(PfileName)->str:
    content = ""
    sourceFile = open(PfileName, "r", encoding="utf-8")

    Row = sourceFile.readline()

    while Row != "":
        content += Row.strip() + ";"
        Row = sourceFile.readline()

    sourceFile.close()
    return content


def analyseNumbers(Pfile, PfileName):
    print("#### Number analysis - START ####")

    cleanFile = Pfile.strip(";").split(";")

    cleanFileInt = []

    for i in range(len(cleanFile)):
        cleanFileInt.append(int(cleanFile[i]))

    cleanFileInt.sort()

    total = 0

    for i in range(len(cleanFileInt)):
        total += cleanFileInt[i]

    lineCounter = len(cleanFileInt)

    greatest = cleanFileInt[-1]

    average = total / lineCounter

    displayResults(total, lineCounter, greatest, average, PfileName)

    print("#### Number analysis - END ####")


def displayResults(Ptotal, PlineCounter, Pgreatest, Paverage, Pfilename):
    print(f'File "{Pfilename}" results:')
    print("Count;Sum;Greatest;Average")
    print(f'{PlineCounter};{Ptotal};{Pgreatest};{Paverage:.2f}')


def main():
    print("Program starting.")

    fileName = input("Insert filename: ")

    file = readValues(fileName)

    analyseNumbers(file, fileName)

    print("Program ending.")

if __name__=="__mani__":
    main()
