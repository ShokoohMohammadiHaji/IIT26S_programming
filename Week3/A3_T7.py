print("Program starting.")
print("Testing decision structures.")
Num=int(input("Insert an integer: "))
print("options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
choice=int(input("Your choice: "))
if choice==1:
    print("Using one multi-branched decision structure.")
    if Num >= 400:
        Num += 44
    elif Num >= 250:
        Num += 22
    elif Num >= 100:
        Num += 11
    print(f"Result is {Num}")


elif choice==2:
    print("Using multiple independent if-statements structure.")
    if Num >= 400:
        Num += 44
    if Num >= 250:
        Num += 22
    if Num >= 100:
        Num += 11
    print(f"Result is {Num}")

elif choice==0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")