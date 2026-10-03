print("Program starting.")
name=input("This is a program with simple menu, where you can choose which operation the program performs.Before the menu, please insert your name: ")
print("\noptions:")
print("1 _ Print welcome message")
print("2 _ Print the name backwards")
print("3 _ Print the first character")
print("4 _ Show the amount of characters in the name")
print("0 - Exit")
Choice=int(input("Your choice: "))
if Choice==1:
    print("Welcome John!")
elif Choice==2:
    print(f"Your name backwards is \"{name[::-1]}\"")
elif Choice==3:
    print(f"The first character in name \"{name}\" is \"{name[0]}\"")
elif Choice==4:
    print(f"There are {len(name)} characters in the name \"{name}\"")
elif Choice==0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")