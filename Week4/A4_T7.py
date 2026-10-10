print("Program starting.")
print("\nCheck multiplicative persistence.")

Num = int(input("Insert an integer: "))
counter = 0

while Num >= 10:
    digit_counter = len(str(Num))
    product = 1

    for i in range(digit_counter):
        digit = (Num // (10 ** (digit_counter - i - 1))) % 10
        product *= digit

        if i < digit_counter - 1:
            print(digit, end=" * ")
        else:
            print(digit, end="")

    print(" =", product)
    Num = product
    counter += 1

print("No more steps.")
print(f"\nThis program took {counter} step(s)")
print("\nProgram ending.")