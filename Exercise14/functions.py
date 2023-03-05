import random


# function to ask the player for input - will loop until valid input is given, and then assigned to rock,paper,scissors
def getPlayerChoice():
    userChoice = ""
    while userChoice == "":
        userInput = input("Please choose rock/paper/scissors by typing r, p or s: ")
        if userInput == "r" or userInput == "R":
            userChoice = "rock"
        elif userInput == "p" or userInput == "P":
            userChoice = "paper"
        elif userInput == "s" or userInput == "S":
            userChoice = "scissors"
        else:
            print("Please try again")
    return userChoice


# function to get computer selection and assign this to rock, paper, scissors
def getComputerChoice():
    compChoice = "scissors"
    compInput = random.randint(0, 2)
    if compInput == 0:
        compChoice = "rock"
    elif compInput == 1:
        compChoice = "paper"
    return compChoice


# function to compare player choice and computer choice - returning win/loss/draw
def gameComparison(playerChoice, computerChoice):
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
def logResults(outcome, win, loss, draw):
    if outcome == "win":
        win += 1
    if outcome == "loss":
        loss += 1
    if outcome == "draw":
        draw += 1
    return win, loss, draw


# function to log player selections
def logChoices(playerChoice, rocks, papers, scissors):
    if playerChoice == "rock":
        rocks += 1
    if playerChoice == "paper":
        papers += 1
    if playerChoice == "scissors":
        scissors += 1
    return rocks, papers, scissors