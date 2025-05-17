# Conditional Structures (Nested if)

# We can create conditional structures inside other conditional structures.
# This is called a nested if.

# Example:

regular_account = True
student_account = False
overdraft_limit = 450
balance = 2000
withdrawal = 1500

if regular_account:
    if balance >= withdrawal:
        print("Withdrawal successful!")
    elif withdrawal <= (balance + overdraft_limit):
        print("Withdrawal successful using overdraft!")
        
elif student_account:
    if balance >= withdrawal:
        print("Withdrawal successful!")
    else:
        print("Insufficient balance to perform the withdrawal!")

# Practice Exercise

regular_account = False
student_account = False
special_account = True

balance = 2000
withdrawal = 1500
overdraft_limit = 450

if regular_account:

    if balance >= withdrawal:
        print("Withdrawal successful!")
    elif withdrawal <= (balance + overdraft_limit):
        print("Withdrawal successful using overdraft!")
    else:
        print("Unable to complete the withdrawal, insufficient funds!")

elif student_account:

    if balance >= withdrawal:
        print("Withdrawal successful!")
    else:
        print("Insufficient funds!")

elif special_account:
    print("Special account selected!")

else:
    print("The system could not recognize your account type. Please contact your manager.")
