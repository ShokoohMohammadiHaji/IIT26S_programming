print("Program starting.")
name=input("This is a program with simple menu, where you can choose which operation the program performs.Before the menu, please insert your name:")
print("\noptions:")
print("1 _ Print welcome message")
print("0 - Exit")
Choice=int(input("Your choice: "))
if Choice==1:
    print("Welcome John!")
elif Choice==0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")