# Ternary Conditional Structure

# The ternary conditional structure is a compact way of writing an if-else statement in Python.
# It allows you to assign a value to a variable based on a condition, all in a single line.

# Example:

balance = 2000
withdraw = 1500

status = "Success" if balance >= withdraw else "Failure"

print(f"{status} when performing the withdrawal!")

# Exercise to practice the concept

balance = 2000
withdraw = 2500

status = "Success" if balance >= withdraw else "Failure"

print(f"{status} when performing the withdrawal!")
