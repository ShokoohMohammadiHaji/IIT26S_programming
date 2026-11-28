
########################################################
# Task A9_T7
# Developer Shokooh Mohammadi
# Date 2026-11-28
########################################################

import sys
import os


def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("[USAGE] python A9_T7.py src_file dst_file")


def copyFile(PSrcFile: str, PDstFile: str) -> None:

    Proceed = False

    if os.path.exists(PDstFile):
        print('Destination file: "{}" already exists.'.format(PDstFile))

        answer = input("Do you want to overwrite it? (y/n): ")

        if answer.lower() == "y":
            Proceed = True

    else:
        Proceed = True

    if Proceed:
        try:
            with open(PSrcFile, "r") as source:
                content = source.read()

            with open(PDstFile, "w") as destination:
                destination.write(content)

        except OSError:
            print('Couldn\'t copy "{}" to "{}".'.format(PSrcFile, PDstFile))
            print("Exiting program.")
            sys.exit(-1)


def main() -> None:

    print("Program starting.")

    if len(sys.argv) == 3:

        SrcFile = sys.argv[1]
        DstFile = sys.argv[2]

        print('Source file: "{}"'.format(SrcFile))
        print('Destination file: "{}"'.format(DstFile))
        print('Copying file: "{}" to "{}".'.format(SrcFile, DstFile))

        copyFile(SrcFile, DstFile)

    else:
        showHelp()

    print("Program ending.")


main()
