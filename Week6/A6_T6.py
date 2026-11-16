
def collectPlainText():
    print("Collecting plain text rows for ciphering.")

    content = ""
    plainText = input("Insert row(empty stops): ")

    while plainText != "":
        content += plainText + "\n"
        plainText = input("Insert row(empty stops): ")

    return content


def cipher(content):
    LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
    UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cipheredText = ""

    for i in range(len(content)):
        char = content[i]

        if char in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.index(char)
            cipheredText += LOWER_ALPHABETS[(index + 13) % 26]

        elif char in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.index(char)
            cipheredText += UPPER_ALPHABETS[(index + 13) % 26] # 26 for charecter after 13

        else:
            cipheredText += char

    return cipheredText


def saveFile(content):
    fileSaveName = input("Insert filename to save: ")

    if fileSaveName != "":
        targetFile = open(fileSaveName, "w", encoding="utf-8")
        targetFile.write(content)
        targetFile.close()
        print("Ciphered text saved!")
    else:
        print("File name not defined.")
        print("Aborting save operation.")

    return None


def main():
    print("Program starting.\n")

    file = collectPlainText()

    cipherFile = cipher(file)

    print("\n#### Ciphered text ####")

    saveFile(cipherFile)

    print("Program ending.")

if __name__=="__mani__":
    main()
