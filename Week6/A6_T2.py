def writeFile(filename, content):
    filehandler = open (filename, "a", encoding="utf-8")
    filehandler.write(content )
    filehandler.close()
    return None

def main():
    print("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    content= "{}\n{}\n".format(firstName, lastName)
    fileName = input("Insert filename: ")
    writeFile(fileName, content)
    print("Program ending.")
    return None

main()