
import time

def analysingInput(Pchoice):
    global pauseTime

    if Pchoice == "1":
        pauseTime = float(input("Insert pause duration (s): "))

    elif Pchoice == "2":
        if pauseTime == None:
            print("Pause is not set.\nSet pause first.")
        else:
            print(f"Pausing for {pauseTime} seconds.")
            time.sleep(pauseTime)
            print("Unpaused.")

    else:
        print("Unknown option!")
    return None

def main():
    global pauseTime
    pauseTime = None

    print("Program starting.")

    while True:
        print("Options:\n1 - Set pause duration\n2 - Activate pause\n0 - Exit")

        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break

        analysingInput(choice)

    print("\nProgram ending.")


main()
