numbers = input("Please enter as many numbers, as you want to add, separated by a space: ")
elements = numbers.split()
elementsToCalc = elements[1:]

operators = input("Please enter as many operators, as you want to add, separated by a space: ")
opElements = operators.split()

# print(elements)
# print(opElements)
# print(elementsToCalc)

if "+" in opElements:
    addSum = int(elements[0])
    for e in elementsToCalc:
        addSum = addSum + int(e)
    print(addSum)

if "-" in opElements:
    minusSum = int(elements[0])
    for e in elementsToCalc:
        minusSum = minusSum - int(e)
    print(minusSum)

if "*" in opElements:
    timesSum = int(elements[0])
    for e in elementsToCalc:
        timesSum = timesSum * int(e)
    print(timesSum)

if "/" in opElements:
    divideSum = int(elements[0])
    for e in elementsToCalc:
        divideSum = divideSum / int(e)
    print(divideSum)