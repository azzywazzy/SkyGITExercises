import getpass

our_pin = "1234"
attempts = 0
allowed_attempts = 3
asking_for_input = True


while asking_for_input:
    supplied_pin = getpass.getpass(prompt="Enter your PIN: ")

    if supplied_pin == our_pin:
        print("Thank you for entering your PIN")
        print("Welcome to the Bank. How can we help you today?")
        asking_for_input = False
    else:
        attempts += 1
        print("Invalid PIN entered. You have " + str(allowed_attempts-attempts) + " attempts remaining.")

    if attempts == allowed_attempts:
        asking_for_input = False
        print("You've exhausted your PIN attempts. Please try again later")
