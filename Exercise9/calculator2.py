# ask the user for input
number1 = input("Please enter the first number you would like to add: ")
number2 = input("Please enter the second number you would like to add: ")
operator = input("Please select the operator to use. Choose from +, -, *, or /: ")

# check which operator was used and calculate accordingly
if operator == "+":
    print("{} {} {} = {}".format(number1, operator, number2, float(number1) + float(number2)))

elif operator == "-":
    print("{} {} {} = {}".format(number1, operator, number2, float(number1) - float(number2)))

elif operator == "*":
    print("{} {} {} = {}".format(number1, operator, number2, float(number1) * float(number2)))

elif operator == "/":
    print("{} {} {} = {}".format(number1, operator, number2, float(number1) / float(number2)))

# if an incorrect operator was used, flag with user and remind of accepted inputs
else:
    print("Please enter a valid operator. Only +, -. *, or / are permitted")
