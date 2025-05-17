# Conditional Structures in Python

# What are conditional structures?
# Conditional structures are commands that allow a block of code to be executed if a condition is true, 
# and another block if the condition is false. They are fundamental to programming logic because they 
# allow the program to make decisions based on specific conditions.
# The most common conditional structures in Python are: if, elif, and else.

# If Statement

# The if statement is used to execute a block of code if a condition is true.

# Example:

balance = 2000.0
withdrawal = float(input("Enter the withdrawal amount: "))

if balance >= withdrawal:
    print("Withdrawal successful!")

if balance < withdrawal:
    print("Insufficient balance to perform the withdrawal!")

# If-Else Statement

# The if-else statement is used to execute one block of code if a condition is true and another block if it is false.

# Example:

balance = 2000.0
withdrawal = float(input("Enter the withdrawal amount: "))

if balance >= withdrawal:
    print("Withdrawal successful!")

else:
    print("Insufficient balance to perform the withdrawal!")

# If-Elif-Else Statement

# The if-elif-else structure is used to evaluate multiple conditions:
# - if a condition is true, a block is executed
# - elif (else if) checks another condition
# - else is executed if none of the previous conditions are true

# Example:

import sys

option = int(input("Enter your choice: [1] Withdraw \n[2] Statement: "))

if option == 1:
    amount = float(input("Enter the withdrawal amount: "))

elif option == 2:
    print("Showing account statement...")

else:
    sys.exit("Invalid option!")  # You can also use: raise SystemExit("Invalid option!")
    # If you use sys.exit, the sys module must be imported.

# Practice Exercise

LEGAL_AGE = 18
SPECIAL_AGE = 17

age = int(input("Enter your age: "))

if age >= LEGAL_AGE:
    print("You are old enough to apply for a driver's license.")

elif age == SPECIAL_AGE:
    print("You can attend theoretical classes, but not practical driving classes.")

else:
    print("You are not yet allowed to apply for a driver's license.")
