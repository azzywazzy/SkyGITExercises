from functions import *

# initialise w/l/d variables
wins = 0
losses = 0
draws = 0

# initialise choice collection
rockChoice = 0
paperChoice = 0
scissorChoice = 0

keepPlaying = "y"
while keepPlaying == "y" or keepPlaying == "Y":

    playerChoice = getPlayerChoice()
    computerChoice = getComputerChoice()

    results = gameComparison(playerChoice, computerChoice)

    wins, losses, draws = logResults(results, wins, losses, draws)
    rockChoice, paperChoice, scissorChoice = logChoices(playerChoice, rockChoice, paperChoice, scissorChoice)

    displayResults(results)
    print("You've chosen rock {} times, paper {} times and scissors {} times".format(rockChoice, paperChoice, scissorChoice))
    print("Your win/loss/draw record is {}/{}/{}".format(wins, losses, draws))

    keepPlaying = input("Would you like to keep playing? Choose y if you do, or press any other key to quit: ")

print("Thank you for playing!")