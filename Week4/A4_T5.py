text = ""
print("Program starting.\n")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
print()

if start >= stop:
    print("Starting point value must be less than the stopping point value.")

if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")

else:
    print("First loop - inspection with break:")

    for i in range(start, stop + 1):
        if i == inspect: 
            break
        text= text + str(i) + " "
    print(text[:-1])
    text = ""
    print("\nSecond loop - inspection with continue:")
    
    for i in range(start, stop ):
        text= text + str(i)+ " "
        if i == inspect:
            continue   
    print(text [:-1])

print()
print("\nProgram ending.")