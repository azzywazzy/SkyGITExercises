# Notes
# Doesn't validate number input (check that it's suitable
# Does validate that operators are one of the selected options - is there a better way?
# Doesn't validate y/n selection - just carries on if anything except "n" is entered
# Have explicitly only delivered what was asked for in the requirements

askingForInput = True

while askingForInput:
    # ask the user for input
    number1 = input("Please enter the first number you would like to calculate: ")
    operator = input("Please select the operator to use. Choose from +, -, *, or /: ")
    number2 = input("Please enter the second number you would like to calculate: ")

    # check which operator was used and calculate accordingly
    if operator == "+":
        print("{} {} {} = {}".format(number1, operator, number2, float(number1) + float(number2)))

        # when calculated, ask the user if they want to continue
        carryOn = input("Would you like to carry on? Type y/n and hit Enter: ")
        if carryOn == "n":
            askingForInput = False
            print("Thank you, come again!")

    # check which operator was used and calculate accordingly
    elif operator == "-":
        print("{} {} {} = {}".format(number1, operator, number2, float(number1) - float(number2)))
        # when calculated, ask the user if they want to continue
        carryOn = input("Would you like to carry on? Type y/n and hit Enter: ")
        if carryOn == "n":
            askingForInput = False
            print("Thank you, come again!")

    # check which operator was used and calculate accordingly
    elif operator == "*":
        print("{} {} {} = {}".format(number1, operator, number2, float(number1) * float(number2)))
        # when calculated, ask the user if they want to continue
        carryOn = input("Would you like to carry on? Type y/n and hit Enter: ")
        if carryOn == "n":
            askingForInput = False
            print("Thank you, come again!")

    # check which operator was used and calculate accordingly
    elif operator == "/":
        print("{} {} {} = {}".format(number1, operator, number2, float(number1) / float(number2)))
        # when calculated, ask the user if they want to continue
        carryOn = input("Would you like to carry on? Type y/n and hit Enter: ")
        if carryOn == "n":
            askingForInput = False
            print("Thank you, come again!")

    # if an incorrect operator was used, flag with user and remind of accepted inputs
    else:
        print("Please enter a valid operator. Only +, -. *, or / are permitted")
