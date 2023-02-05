import getpass

# set intro variables
our_pin = "1234"
attempts = 0
allowed_attempts = 3
asking_for_input = True

# while loop asking for input, as long as asking_for_input is true
# ask for input while hiding the entered pin from echo
while asking_for_input:
    supplied_pin = getpass.getpass(prompt="Enter your PIN: ")

    # if the entered pin matches, print message and alter loop condition
    if supplied_pin == our_pin:
        print("Thank you for entering your PIN")
        print("Welcome to the Bank. How can we help you today?")
        asking_for_input = False

    # otherwise add one to the attempts counter and prompt for more input
    else:
        attempts += 1
        print("Invalid PIN entered. You have " + str(allowed_attempts-attempts) + " attempts remaining.")

    # if attempts counter equals the number of allowed attempts, then alter loop condition and print message
    if attempts == allowed_attempts:
        asking_for_input = False
        print("You've exhausted your PIN attempts. Please try again later")
