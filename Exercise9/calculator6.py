askingForInput = True
pastCalculations = list([])

print("\U0001F44B Welcome to the calculator!")
print("At any time, if you want to quit, type 'q' and press Enter. If you'd like to see your calculation history, "
      "type 'h' and press Enter. (This will quit the programme.)")

while askingForInput:

    # ask the user for input
    userInput = input("Please enter as many numbers, as you want to calculate, separated by a space: ")
    elements = userInput.split()
    elementsToCalc = elements[1:]

    # check to see if the user has asked for history, or to quit
    if "h" in elements:
        print("Your calculation history is:\n" + "\n".join(pastCalculations))
        askingForInput = False
        continue

    if "q" in elements:
        askingForInput = False
        continue

    # ask the user for the operator
    operator = input("Please enter the operator you'd like to use. Choose from +, -, * or /: ")

    # check to see if the user has asked for history, or to quit
    if "h" in operator:
        print("\n".join(pastCalculations))
        askingForInput = False

    if "q" in operator:
        askingForInput = False

    # start doing arithmetic
    if "+" in operator:
        addSum = int(elements[0])
        for e in elementsToCalc:
            addSum = addSum + int(e)
        sumString = str("\U00002795 {} = {}".format(userInput.replace(" ", " + "), addSum))
        print(sumString)
        pastCalculations.append(sumString)

    if "-" in operator:
        minusSum = int(elements[0])
        for e in elementsToCalc:
            minusSum = minusSum - int(e)
        minusString = str("\U00002796 {} = {}".format(userInput.replace(" ", " - "), minusSum))
        print(minusString)
        pastCalculations.append(minusString)

    if "*" in operator:
        timesSum = int(elements[0])
        for e in elementsToCalc:
            timesSum = timesSum * int(e)
        timesString = str("\U00002716 {} = {}".format(userInput.replace(" ", " * "), timesSum))
        print(timesString)
        pastCalculations.append(timesString)

    if "/" in operator:
        divideSum = int(elements[0])
        for e in elementsToCalc:
            divideSum = divideSum / int(e)
        divideString = str("\U00002797 {} = {}".format(userInput.replace(" ", " + "), divideSum))
        print(divideString)
        pastCalculations.append(divideString)

# exit loop and print thank you
print("Thank you, come again! \U0001F44B")
