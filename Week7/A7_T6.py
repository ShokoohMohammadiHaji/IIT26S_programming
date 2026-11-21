
import random
random.seed(1234)


def displayMenu():
    print("\nOptions:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")


def displayChoice(PplayerName, Pchoice):

    rockArt = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

    paperArt = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

    scissorsArt = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

    if Pchoice == 1:
        choiceName = "rock"
        print(rockArt)

    elif Pchoice == 2:
        choiceName = "paper"
        print(paperArt)

    else:
        choiceName = "scissors"
        print(scissorsArt)

    print(f"{PplayerName} chose {choiceName}.")

    return choiceName


def playGame(PplayerName, PplayerChoice, PbotChoice,
             PplayerWins, PplayerLosses, Pdraws):

    print("\nRock! Paper! Scissors! Shoot!\n")

    print("#" * 25)
    playerChoiceName = displayChoice(PplayerName, PplayerChoice)

    print("#" * 25)
    botChoiceName = displayChoice("RPS-3PO", PbotChoice)

    print("#" * 25)

    if PplayerChoice == PbotChoice:
        print(f"Draw! Both players chose {playerChoiceName}.")
        Pdraws += 1

    elif (PplayerChoice == 1 and PbotChoice == 3) or \
         (PplayerChoice == 2 and PbotChoice == 1) or \
         (PplayerChoice == 3 and PbotChoice == 2):

        print(f"{PplayerName} {playerChoiceName} beats RPS-3PO {botChoiceName}.")
        PplayerWins += 1

    else:
        print(f"RPS-3PO {botChoiceName} beats {PplayerName} {playerChoiceName}.")
        PplayerLosses += 1

    return PplayerWins, PplayerLosses, Pdraws


def displayResult(PplayerName, PplayerWins, PplayerLosses, Pdraws):

    print("\nResults:")
    print(f"{PplayerName} - wins ({PplayerWins}), losses ({PplayerLosses}), draws ({Pdraws})")
    print(f"RPS-3PO - wins ({PplayerLosses}), losses ({PplayerWins}), draws ({Pdraws})")


def main():

    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    playerName = input("Insert player name: ")

    print(f"Welcome {playerName}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...")

    playerWins = 0
    playerLosses = 0
    draws = 0

    while True:

        displayMenu()

        playerChoice = int(input("Your choice: "))

        if playerChoice == 0:
            break

        elif playerChoice >= 1 and playerChoice <= 3:

            botChoice = random.randint(1, 3)

            playerWins, playerLosses, draws = playGame(
                playerName,
                playerChoice,
                botChoice,
                playerWins,
                playerLosses,
                draws
            )

        else:
            print("Invalid choice. Please choose 1, 2, 3 or 0.")

    displayResult(playerName, playerWins, playerLosses, draws)

    print("\nProgram ending.")


main()
