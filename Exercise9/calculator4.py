numbers = input("Please enter as many numbers, as you want to calculate, separated by a space: ")
elements = numbers.split()
elementsToCalc = elements[1:]

operators = input("Please enter as many operators, as you want to use, separated by a space: ")
opElements = operators.split()

# print(elements)
# print(opElements)
# print(elementsToCalc)

if "+" in opElements:
    addSum = int(elements[0])
    for e in elementsToCalc:
        addSum = addSum + int(e)
    print("You asked to add {} to get a total of {}".format(numbers.replace(" ", ", "), addSum))

if "-" in opElements:
    minusSum = int(elements[0])
    for e in elementsToCalc:
        minusSum = minusSum - int(e)
    print("You asked to subtract {} to get a total of {}".format(numbers.replace(" ", ", "), minusSum))

if "*" in opElements:
    timesSum = int(elements[0])
    for e in elementsToCalc:
        timesSum = timesSum * int(e)
    print("You asked to multiply {} to get a total of {}".format(numbers.replace(" ", ", "), timesSum))

if "/" in opElements:
    divideSum = int(elements[0])
    for e in elementsToCalc:
        divideSum = divideSum / int(e)
    print("You asked to divide {} to get a total of {}".format(numbers.replace(" ", ", "), divideSum))
