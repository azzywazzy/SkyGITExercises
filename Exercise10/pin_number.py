import getpass

# set intro variables
# used a variable for allowed_attempts, rather than hardcoding it, in case we need to change it later
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
        print("Welcome to the Bank. Please choose from one of the following options...")
        asking_for_input = False

    # otherwise add one to the attempts counter and prompt for more input
    else:
        attempts += 1
        print("Invalid PIN entered. You have " + str(allowed_attempts-attempts) + " attempts remaining.")

    # if attempts counter equals the number of allowed attempts, then alter loop condition and print message
    if attempts == allowed_attempts:
        asking_for_input = False
        print("You've entered the wrong PIN {} times. Please contact your bank to unlock your account.".format(allowed_attempts))


# Second version below which does away the asking_for_input variable and uses the number of attempts instead.
# Unsure if I like this version, as there may be legitimate reasons why it's a bad idea to alter the attempts variable to exit the loop

# import getpass
#
# our_pin = "1234"
# attempts = 0
# allowed_attempts = 3
#
# # while loop asking for input, as long as number of attempts so far is not zero
# # ask for input while hiding the entered pin from echo
# while attempts < allowed_attempts:
#     supplied_pin = getpass.getpass(prompt="Enter your PIN: ")
#
#     # if the entered pin matches, print message and alter loop condition
#     if supplied_pin == our_pin:
#         print("Thank you for entering your PIN")
#         print("Welcome to the Bank. Please choose from one of the following options...")
#         attempts = allowed_attempts
#
#     # otherwise add one to the attempts counter and prompt for more input
#     else:
#         attempts += 1
#         print("Invalid PIN entered. You have " + str(allowed_attempts-attempts) + " attempts remaining.")
#
#         if attempts == allowed_attempts:
#             print("You've entered the wrong PIN {} times. Please contact your bank to unlock your account.".format(allowed_attempts))
