import random


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


def computerInput():
    compAction = "scissors"
    compInput = random.randint(0, 2)
    if compInput == 0:
        compAction = "rock"
    elif compInput == 1:
        compAction = "paper"
    return compAction


def comparison(player, computer):
    result = ""
    print("You chose {} and the computer chose {}!".format(player, computer))
    if player == "rock" and computer == "rock":
        print("\U0001F644 It's a draw!")
        result = "draw"
    elif player == "paper" and computer == "paper":
        print("\U0001F644 It's a draw!")
        result = "draw"
    elif player == "scissors" and computer == "scissors":
        print("\U0001F644 It's a draw!")
        result = "draw"
    elif player == "rock" and computer == "paper":
        print("\U0001F494 Computer wins!")
        result = "loss"
    elif player == "paper" and computer == "scissors":
        print("\U0001F494 Computer wins!")
        result = "loss"
    elif player == "scissors" and computer == "rock":
        print("\U0001F494 Computer wins!")
        result = "loss"
    elif player == "rock" and computer == "scissors":
        print("\U0001F389 You win!")
        result = "win"
    elif player == "paper" and computer == "rock":
        print("\U0001F389 You win!")
        result = "win"
    elif player == "scissors" and computer == "paper":
        print("\U0001F389 You win!")
        result = "win"
    return result


gameHistory = list()
keepPlaying = "y"
while keepPlaying == "y":

    playerChoice = playerInput()
    computerChoice = computerInput()
    results = comparison(playerChoice, computerChoice)
    gameHistory.append(results)
    print("Your game record is: " + ", ".join(gameHistory))
    # print("Your game record is: {}".format(gameHistory))
    keepPlaying = input("Would you like to keep playing? Choose y if you do, or press any other key to quit: ")

print("Thank you for playing!")
