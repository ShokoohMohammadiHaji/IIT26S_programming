
print("Program starting.")
Num = int(input("Insert a positive integer: "))
loop_counter = -1
while True:
    print(Num, sep="")
    loop_counter += 1
    if Num == 1:
        break

    print(" -> ", sep="")

    if Num % 2 == 0:
        Num = Num // 2
    else:
        Num = 3 * Num + 1
print(f"\nSequence had {loop_counter} total steps.")
print("\nProgram ending.")
