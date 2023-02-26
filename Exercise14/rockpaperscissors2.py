import random


# function to ask the player for input - will loop until valid input is given, and then assigned to rock,paper,scissors
def playerInput():
    userAction = ""
    while userAction == "":
        userInput = input("Please choose rock/paper/scissors by typing r, p or s: ")
        if userInput == "r" or userInput == "R":
            userAction = "rock"
        elif userInput == "p" or userInput == "P":
            userAction = "paper"
        elif userInput == "s" or userInput == "S":
            userAction = "scissors"
        else:
            print("Please try again")
    return userAction


# function to get computer selection and assign this to rock, paper, scissors
def computerInput():
    compAction = "scissors"
    compInput = random.randint(0, 2)
    if compInput == 0:
        compAction = "rock"
    elif compInput == 1:
        compAction = "paper"
    return compAction


# function to compare player choice and computer choice - returning win/loss/draw
def comparison(playerChoice, computerChoice):
    result = ""
    print("You chose {} and the computer chose {}!".format(playerChoice, computerChoice))
    if playerChoice == computerChoice:
        result = "draw"
    elif playerChoice == "rock" and computerChoice == "paper":
        result = "loss"
    elif playerChoice == "paper" and computerChoice == "scissors":
        result = "loss"
    elif playerChoice == "scissors" and computerChoice == "rock":
        result = "loss"
    elif playerChoice == "rock" and computerChoice == "scissors":
        result = "win"
    elif playerChoice == "paper" and computerChoice == "rock":
        result = "win"
    elif playerChoice == "scissors" and computerChoice == "paper":
        result = "win"
    return result


# function to print result on the screen
def displayResults(outcome):
    if outcome == "win":
        print("\U0001F389 You win!")
    elif outcome == "loss":
        print("\U0001F494 Computer wins!")
    elif outcome == "draw":
        print("\U0001F644 It's a draw!")


# function to log wins/losses/draws
def resultsLog(outcome, win, loss, draw):
    if outcome == "win":
        win += 1
    if outcome == "loss":
        loss += 1
    if outcome == "draw":
        draw += 1
    return win, loss, draw


# function to log player selections
def choicesLog(playerChoice, rocks, papers, scissors):
    if playerChoice == "rock":
        rocks += 1
    if playerChoice == "paper":
        papers += 1
    if playerChoice == "scissors":
        scissors += 1
    return rocks, papers, scissors


# initialise w/l/d variables
wins = 0
losses = 0
draws = 0

# initialise choice collection
rockChoice = 0
paperChoice = 0
scissorChoice = 0

# while loop so player can keep playing as long as they choose 'y' after each game
keepPlaying = "y"
while keepPlaying == "y":

    playerChoice = playerInput()
    computerChoice = computerInput()
    results = comparison(playerChoice, computerChoice)
    wins, losses, draws = resultsLog(results, wins, losses, draws)
    rockChoice, paperChoice, scissorChoice = choicesLog(playerChoice, rockChoice, paperChoice, scissorChoice)
    displayResults(results)
    print("You've chosen rock {} times, paper {} times and scissors {} times".format(rockChoice, paperChoice, scissorChoice))
    print("Your win/loss/draw record is {}/{}/{}".format(wins, losses, draws))
    keepPlaying = input("Would you like to keep playing? Choose y if you do, or press any other key to quit: ")

print("Thank you for playing!")
