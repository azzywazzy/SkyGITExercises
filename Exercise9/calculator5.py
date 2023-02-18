askingForInput = True
pastCalculations = list([])

print("\U0001F44B Welcome to the calculator!")

while askingForInput:
    # ask the user for input

    numbers = input("Please enter as many numbers, as you want to calculate, separated by a space: ")
    elements = numbers.split()
    elementsToCalc = elements[1:]

    operators = input("Please enter as many operators, as you want to use, separated by a space: ")
    opElements = operators.split()

    if "+" in opElements:
        addSum = int(elements[0])
        for e in elementsToCalc:
            addSum = addSum + int(e)
        sumString = str("\U00002795 {} = {}".format(numbers.replace(" ", " + "), addSum))
        print(sumString)
        pastCalculations.append(sumString)

    if "-" in opElements:
        minusSum = int(elements[0])
        for e in elementsToCalc:
            minusSum = minusSum - int(e)
        minusString = str("\U00002796 {} = {}".format(numbers.replace(" ", " - "), minusSum))
        print(minusString)
        pastCalculations.append(minusString)

    if "*" in opElements:
        timesSum = int(elements[0])
        for e in elementsToCalc:
            timesSum = timesSum * int(e)
        timesString = str("\U00002716 {} = {}".format(numbers.replace(" ", " * "), timesSum))
        print(timesString)
        pastCalculations.append(timesString)

    if "/" in opElements:
        divideSum = int(elements[0])
        for e in elementsToCalc:
            divideSum = divideSum / int(e)
        divideString = str("\U00002797 {} = {}".format(numbers.replace(" ", " + "), divideSum))
        print(divideString)
        pastCalculations.append(divideString)

    # when calculated, ask the user if they want to continue
    carryOn = input("Would you like to carry on or view history? Type y to continue, h to view history or q to quit and hit Enter: ")
    if carryOn == "h":
        print("\n".join(pastCalculations))
    if carryOn == "q":
        askingForInput = False

print("Thank you, come again! \U0001F44B")
