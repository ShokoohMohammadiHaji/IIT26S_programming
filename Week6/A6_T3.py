def readFile(sourceFileName : str) -> str:
    content = ""
    sourceFile=open(sourceFileName,"r",encoding="utf-8")
    Row = sourceFile.readline()
    print(f"reading file {sourceFileName} content.")
    while Row!="":
        content += Row
        Row = sourceFile.readline()
    sourceFile.close()
    print("File content ready in memory.")
    return content

def writeFile(destFileName : str, content : str) -> None:
    destFile= open(destFileName,"w",encoding="utf-8")
    print(f"Writing content into file {destFileName}.")
    destFile.write(content)
    destFile.close()
    return None


# def readWriteFile(sourceFileName , destFileName : str) -> str:
#     content = ""
#     sourceFile=open(sourceFileName,"r",encoding="utf-8")
#     destFile= open(destFileName,"w",encoding="utf-8")
#     Row = sourceFile.readline()
#     print(f"reading file {sourceFileName} content.")
#     while Row!="":
#         content += Row
#         Row = sourceFile.readline()
#         destFile.write(Row)

#     destFile.close()
#     sourceFile.close()
#     print("File content ready in memory.")
#     print(f"Writing content into file {destFileName}.")
#     return content

def main():
    print("Program starting.")
    print("This program can copy a file.")
    sourceFileName=input("Insert source filename: ")
    destFileName=input("Insert destination filename: ")
    Content=readFile(sourceFileName)
    writeFile(destFileName,Content)
    print("Copying operation complete.")
    print("Program ending.")

main()