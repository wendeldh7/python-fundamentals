# While Statement

# The while statement is used to execute a block of code while a condition is true.

option = -1

while option != 0:
    option = int(input("[1] Withdraw \n[2] Statement \n[0] Exit \n: "))

    if option == 1:
        print("Withdrawing...")
    elif option == 2:
        print("Showing account statement...")

# While/Else Structure

option = -1

while option != 0:
    option = int(input("[1] Withdraw \n[2] Statement \n[0] Exit \n: "))

    if option == 1:
        print("Withdrawing...")
    elif option == 2:
        print("Showing account statement...")

else:
    print("Thank you for using our banking system. See you next time!")
