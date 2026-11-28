########################################################
# Task A9_Tx
# Developer Shokooh Mohammadi
# Date YYYY-MM-DD
########################################################
import sys
print("Program starting.")
fileName= input("Insert filename: ")
try:
    file = open(fileName, "r")
    content = (file.read()).strip()
    file.close()
    print("##{}##".format(fileName))
    print(content)
    print("##{}##".format(fileName))
    print ("Program ending.")
except:
    print('Couldn\'t read file "{}".'.format(fileName))
    sys.exit(1)
