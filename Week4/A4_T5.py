print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

if start >= stop:
    print("\nStarting point value must be less than the stopping point value.")

elif inspect < start or inspect > stop:
    print("\nInspection value must be within the range of start and stop.")

else:
    print("\nFirst loop - inspection with break:")
    for i in range(start, stop + 1):
        if i == inspect:
            break
        print(i, end=" ")
   # print()
    print("\nSecond loop - inspection with continue:")
    for i in range(start, stop ):
        if i == inspect:
            continue
        print(i, end=" ")

print()
print("\nProgram ending.")