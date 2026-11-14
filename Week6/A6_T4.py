
def readFile(PsourceFileName):
    content = ""
    sourceFile = open(PsourceFileName, "r", encoding="utf-8")

    print(f'Reading names from "{PsourceFileName}".')

    Row = sourceFile.readline()

    while Row != "":
        if Row.strip() != "":
            content += Row.strip() + ";"

        Row = sourceFile.readline()

    sourceFile.close()
    return content


def analyesNames(Pfile):
    print("Analysing names...")

    file = Pfile.strip(";").split(";")

    file.sort(key=len)
    sortedFile = file

    shortest = len(sortedFile[0])
    longest = len(sortedFile[-1])
    nameCount = len(sortedFile)

    total = 0

    for i in range(len(sortedFile)):
        total += len(sortedFile[i])

    average = total / nameCount

    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {nameCount}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print(f"Average name - {average:.2f} chars")
    print("#### REPORT END ####")


def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    sourceFileName = input("Insert filename to read: ")

    file = readFile(sourceFileName)

    analyesNames(file)

    print("Program ending.")


main()
