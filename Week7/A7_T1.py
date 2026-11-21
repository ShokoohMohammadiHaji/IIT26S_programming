def collectInt():
    IntList = []
    print("Collect positive integers.")
    while True :
        Int = int(input("Insert positive integer(negative stops): "))
        if Int < 0 :
            print("Stopped collecting positive integers.")
            break
        IntList.append(Int)
    return IntList

def displayInt(PcollecttedList):
    print(f"Displaying {len(PcollecttedList)} integers:")
    if (len(PcollecttedList)!= 0):
        for i in range (len(PcollecttedList)):
            print(f"- Index {i} => Ordinal {i+1} => Integer {PcollecttedList[i]}")
    else:
        print("No integers to display.")

def main():
    print("Program starting.")
    collectedList= collectInt()
    displayInt(collectedList)
    print("Program ending.")
    
main()