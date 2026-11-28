
########################################################
# Task A9_T1
# Developer Shokooh Mohammadi
# Date 2026-11-28
########################################################

print("Program starting.")

total = 0

while True:
    value = input("Insert a floating-point value (0 to stop): ")

    try:
        number = float(value)
        total += number

        if number == 0:
            print()
            print("Final sum is {:.2f}".format(total))
            break

    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(value))

print("Program ending.")
