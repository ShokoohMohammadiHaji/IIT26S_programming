print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")
print("options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Choice=int(input("Your choice: "))
if Choice==1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2=int(input("Your choice: "))
    if choice2==1:
        meters=float(round(float(input("Insert meters: ")), 1))
        kilometers=round(meters*0.001, 1)
        print(f"{meters} m is {kilometers} km")
    elif choice2==2:
        kilometers=float(input("Insert kilometers: "))
        meters=round(kilometers*1000, 1)
        print(f"{kilometers} km is {meters} m")
    elif choice2==0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice==2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice2=int(input("Your choice: "))
    if choice2==1:
        grams=float(input("Insert grams: "))
        pounds=round(grams*0.002205, 1)
        print(f"{grams} g is {pounds} lb")
    elif choice2==2:
        pounds=float(input("Insert pounds: "))
        grams=round(pounds/0.002205, 1)
        print(f"{pounds} lb is {grams} g")
    elif choice2==0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice==0:
    print("\nExiting...")

else:
    print("\nUnknown option.")


print("\nProgram ending.")