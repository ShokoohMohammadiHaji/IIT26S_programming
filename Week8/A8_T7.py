
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon
import math


def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")

    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fillColor = input("- Fill color: ")
    strokeColor = input("- Stroke color: ")

    PDwg.add(Rect(
        insert=(x, y),
        size=(side, side),
        fill=fillColor,
        stroke=strokeColor
    ))

    return None


def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")

    x = int(input("- Center X coord: "))
    y = int(input("- Center Y coord: "))
    radius = int(input("- Radius: "))
    fillColor = input("- Fill color: ")
    strokeColor = input("- Stroke color: ")

    PDwg.add(Circle(
        center=(x, y),
        r=radius,
        fill=fillColor,
        stroke=strokeColor
    ))

    return None


def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")

    CenterX = int(input("Middle point X: "))
    CenterY = int(input("Middle point Y: "))
    apothem = int(input("Apothem length: "))
    fillColor = input("Insert fill: ")
    strokeColor = input("Insert stroke: ")

    # Calculate circumradius
    radius = apothem / math.cos(math.radians(30))

    # Angles for the six points
    Angles = [-60, 0, 60, 120, 180, 240]

    Points = []

    for Angle in Angles:
        x = CenterX + radius * math.cos(math.radians(Angle))
        y = CenterY + radius * math.sin(math.radians(Angle))

        Points.append((round(x), round(y)))

    # Add hexagon to SVG
    PDwg.add(Polygon(
        points=Points,
        fill=fillColor,
        stroke=strokeColor
    ))

    return None


def saveSvg(PDwg: Drawing) -> None:
    fileName = input("Insert filename: ")

    print(f'Saving file to "{fileName}"')

    answer = input("Proceed (y/n)?: ")

    if answer.lower() == "y":
        PDwg.saveas(fileName, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Saving cancelled!")

    return None


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")
    return None


def AskChoice():
    choice = int(input("Your choice: "))
    return choice


def main() -> None:
    print("Program starting.")

    Dwg = Drawing()

    while True:
        showOptions()
        choice = AskChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            drawSquare(Dwg)
            print()

        elif choice == 2:
            drawCircle(Dwg)
            print()

        elif choice == 3:
            drawHexagon(Dwg)
            print()

        elif choice == 4:
            saveSvg(Dwg)
            print()

        else:
            print("Unknown option!")
            print()

    print("\nProgram ending.")

    return None


main()
