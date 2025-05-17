# Logical Operators
# Example of logical operators in Python

balance = 1000
withdraw = 200
limit = 100

balance >= withdraw 
# True, because the balance is greater than or equal to the withdrawal

withdraw <= limit
# False, because the withdrawal is not less than or equal to the limit

# Logical operator AND

balance = 1000
withdraw = 200
limit = 100

balance >= withdraw and withdraw <= limit
# False, because the withdrawal is not less than or equal to the limit
# The AND operator returns True only if both conditions are True
# The AND operator returns False if at least one condition is False

# Logical operator OR

balance = 1000
withdraw = 200
limit = 100

balance >= withdraw or withdraw <= limit
# True, because the balance is greater than or equal to the withdrawal
# The OR operator returns True if at least one condition is True
# The OR operator returns False only if both conditions are False

# Logical operator NOT

emergency_contacts = []

not 1000 > 1500 
# True, because 1000 is not greater than 1500
# The NOT operator inverts the logical value of the expression

not emergency_contacts
# True, because the list emergency_contacts is empty
# The NOT operator inverts the logical value of the expression

not "withdraw 1500;"
# False, because the string is not empty
# The NOT operator inverts the logical value of the expression

not ""
# True, because the string is empty
# The NOT operator inverts the logical value of the expression

# Parentheses

balance = 1000
withdraw = 250
limit = 200
special_account = True

balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
# True, because the balance is greater than or equal to the withdrawal and it's a special account

(balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
# True, same result, but grouping conditions improves readability

# Exercise to practice the concepts

# AND = to be True, everything must be True
# OR = to be True, at least one must be True

print(True and True and True)
print(True and False and False)
print(False and False and False)
print(True or True or True)
print(True or False or True)
print(False or False or False)

balance = 1000
withdraw = 250
limit = 200
special_account = True

exp = balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
print(exp)

exp_2 = (balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
print(exp_2)

normal_account_with_sufficient_balance = balance >= withdraw and withdraw <= limit
special_account_with_sufficient_balance = special_account and balance >= withdraw

exp_3 = normal_account_with_sufficient_balance or special_account_with_sufficient_balance
print(exp_3)
