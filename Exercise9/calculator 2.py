firstNumber = input("Please enter a numeric value: ")
secondNumber = input("Please enter a numeric value: ")

if firstNumber.isdecimal() == False or secondNumber.isdecimal() == False:
    print("Please only use numeric values")

else:
    print(float(firstNumber) + float(secondNumber))

