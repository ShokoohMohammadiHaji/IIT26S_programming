
########################################################
# Task A9_Tx
# Developer Shokooh Mohammadi
# Date 2026-11-28
########################################################

def collectRGB():

    colors = ["red", "green", "blue"]
    values = []

    for color in colors:
        Feed = input("Insert {}: ".format(color))

        try:
            number = int(Feed)

            if str(number) != Feed:
                raise ValueError

        except ValueError:
            print('"{}" is non-numeric value.'.format(Feed))
            raise Exception

        if number < 0 or number > 255:
            print('Value "{}" is out of the range 0-255.'.format(number))
            raise Exception

        values.append(number)

    return values


def convert(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


def main():
    print("Program starting.")

    try:
        red, green, blue = collectRGB()

        color = convert(red, green, blue)

        print("RGB Details:")
        print("- Red {}".format(red))
        print("- Green {}".format(green))
        print("- Blue {}".format(blue))
        print("- Hex {}".format(color))

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


main()
