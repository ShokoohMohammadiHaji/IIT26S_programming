########################################################
# Task A9_Tx
# Developer Shokooh Mohammadi
# Date YYYY-MM-DD
########################################################
import sys
print("Program starting.")
value=int(input("Insert exit code(0-255): "))
if (value >=0 and value<=255):
    if (value == 0):
        print("Clean exit")
        sys.exit(0)
    else:
        print("Error code")
        sys.exit(value)
else:
    sys.exit(1)       
