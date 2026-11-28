########################################################
# Task A9_Tx
# Developer Shokooh Mohammad
# Date YYYY-MM-DD
########################################################
def collectCelsius(Ptempature):
    TEMP_MIN = -273.15
    TEMP_MAX = 10000
    Ptempature=float(Ptempature)
    if (Ptempature<TEMP_MIN or Ptempature>TEMP_MAX):
        raise Exception("{} temperature out of range.".format(Ptempature))
    return Ptempature

def main():
    print("Program starting.")
    tempature = input("Insert celsius: ")
    try:
        Celsius = collectCelsius(tempature)
        print("You inserted {:.1f} °C".format(Celsius))
    except ValueError:
        print(f"could not convert string to float: '{tempature}'")
    except Exception as error:
        print(error)
    
    print("Program ending.")
main()