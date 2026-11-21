
def convertStrToList(PvalueString):
    valueList = []
    PvalueString = PvalueString.split(",")

    for i in range(len(PvalueString)):
        try:
            valueList.append(int(PvalueString[i]))
        except ValueError:
            print(f"Invalid value '{PvalueString[i]}' detected.")

    # for i in range(len(PvalueString)):
    #     if PvalueString[i].isdigit():
    #         valueList.append(int(PvalueString[i]))
    #     else:
    #         print(f"Invalid value '{PvalueString[i]}' detected.")


    if len(valueList) == 0:
        return valueList, False

    return valueList, True


def defineOddEven(PsumList):
    if PsumList % 2 == 1:
        return True
    else:
        return False


def sum(PvalueList):
    sumList = 0
    for i in range(len(PvalueList)):
        sumList += PvalueList[i]
    return sumList


def display(PvalueList, PsumList, PSumType):
    print(f"There are {len(PvalueList)} integers in the list.")
    if PSumType == True:
        print(f"Sum of the integers is {PsumList} and it's odd")
    else:
        print(f"Sum of the integers is {PsumList} and it's even")


def main():
    print("Program starting.")
    valueString = input("Insert comma separated integers: ")
    valueList, validationSing = convertStrToList(valueString)

    if validationSing == True:
        sumList = sum(valueList)
        SumType = defineOddEven(sumList)
        display(valueList, sumList, SumType)
    else:
        print("No values to analyse.")

    print("Program ending.")


main()
