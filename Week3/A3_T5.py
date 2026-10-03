print("Program starting.")
print("\noptions:")
print("1 _ Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
Choice=int(input("Your choice: "))
if Choice==1:
    Celsius=float(input("Insert the amount of Celsius: "))
    Fahrenheit=Celsius*(1.8)+32
    print(f"{Celsius} °C equals to {Fahrenheit} °F")
elif Choice==2:
    Fahrenheit=float(input("Insert the amount of Fahrenheit: "))
    Celsius=round((Fahrenheit-32)/1.8, 1)
    print(f"{Fahrenheit} °F equals to {Celsius} °C")
elif Choice==0:
    print("Exiting...")
else:
    print("Unknown option.")
print("Program ending.")