def frameWord(PWord):
    # for i in range (len(PWord)+4):
    #     print ("*", end="")
    # print(f"\n* {PWord} *")
    # for i in range (len(PWord)+4):
    #      print ("*", end="")
    print()
    print ("*" * (len(PWord)+4))
    print(f"* {PWord} *")
    print ("*" * (len(PWord)+4))
    print()

def main():
    print("Program starting.\n")
    word = input("Insert word: ")
    frameWord(word)
    print("Program ending.")

main()
