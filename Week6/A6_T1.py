def readFile(fileName : str) -> str:
    content = ""
    fileHandler = open(fileName, "r", encoding="utf-8")
    Row = fileHandler.readline()
    while Row!="":
        content += Row
        Row = fileHandler.readline()
    fileHandler.close()
    return content
   

def main():
    print("Program starting.\nThis program can read a file.")
    fileName = input("Insert filename: ")
    fileContent= readFile(fileName)
    print(f'#### START "{fileName}" ####')
    print(fileContent)
    print(f'\n#### END "{fileName}" ####')
    print("Program ending.")
    return None
main()