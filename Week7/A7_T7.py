
import string


ALPHABET = string.ascii_uppercase


def readConfig(PFilename: str):
    Rotors = []
    Reflector = ""

    file = open(PFilename, "r")

    for Row in file:
        Row = Row.strip()

        if Row.startswith("Rotor"):
            Rotors.append(Row.split(":")[1])

        elif Row.startswith("Reflector"):
            Reflector = Row.split(":")[1]

    file.close()

    return Rotors, Reflector


def rotateRotors(PPositions: list[int]) -> None:
    PPositions[0] = (PPositions[0] + 1) % 26
    PPositions[1] = (PPositions[1] + 1) % 26
    PPositions[2] = (PPositions[2] + 1) % 26


def forwardPass(PCharacter: str, PRotors: list[str],
                PPositions: list[int]) -> str:

    for i in range(3):
        Index = (ALPHABET.index(PCharacter) + PPositions[i]) % 26
        PCharacter = PRotors[i][Index]
        Index = (ALPHABET.index(PCharacter) - PPositions[i]) % 26
        PCharacter = ALPHABET[Index]

    return PCharacter


def reflect(PCharacter: str, PReflector: str) -> str:
    Index = ALPHABET.index(PCharacter)
    return PReflector[Index]


def reversePass(PCharacter: str, PRotors: list[str],
                PPositions: list[int]) -> str:

    for i in range(2, -1, -1):
        Index = (ALPHABET.index(PCharacter) + PPositions[i]) % 26
        Index = PRotors[i].index(ALPHABET[Index])
        Index = (Index - PPositions[i]) % 26
        PCharacter = ALPHABET[Index]

    return PCharacter


def convertText(PText: str, PRotors: list[str],
                PReflector: str) -> str:

    Positions = [0, 0, 0]
    ConvertedText = ""

    for Character in PText:

        if Character in ALPHABET:
            rotateRotors(Positions)

            CurrentCharacter = forwardPass(
                Character, PRotors, Positions
            )

            CurrentCharacter = reflect(
                CurrentCharacter, PReflector
            )

            CurrentCharacter = reversePass(
                CurrentCharacter, PRotors, Positions
            )

        else:
            CurrentCharacter = Character

        print(
            f'Character "{Character}" illuminated as '
            f'"{CurrentCharacter}"'
        )

        ConvertedText += CurrentCharacter

    return ConvertedText


def main() -> None:
    print("Program starting.")

    fileName = input("Insert config(filename): ")
    Rotors, Reflector = readConfig(fileName)

    plugs = input("Insert plugs (y/n)?: ")

    if plugs.lower() == "n":
        print("No extra plugs inserted.")

    print("Enigma initialized.")

    while True:
        Text = input("\nInsert row (empty stops): ")

        if Text == "":
            break

        Text = Text.upper()

        ConvertedText = convertText(
            Text, Rotors, Reflector
        )

        print(f'Converted row - "{ConvertedText}".')

    print("\nEnigma closing.")


main()
