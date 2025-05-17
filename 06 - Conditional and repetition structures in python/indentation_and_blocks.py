# Indentation and Code Blocks

# Indentation is an important part of Python's syntax.
# It defines blocks of code, such as those inside functions, loops, and conditionals.

# Aesthetic

# Indentation is a matter of style, but it's also a matter of syntax.
# Python does not use braces or keywords to define code blocks.
# Instead, it uses indentation to indicate where a block starts and ends.

# This means indentation must be consistent throughout your code.
# If you use 4 spaces to indent one block of code, you must use 4 spaces for all other blocks too.

# Code Block

# A code block is a set of instructions that are executed together.
# In Python, a block is defined by a line ending with a colon (:) and the subsequent indented lines.

# For example, the following code defines a block that prints "Hello, world!" if the variable x is greater than 10:

# Using Spaces

# There is a style guide called PEP 8 that recommends using 4 spaces per indentation level.
# This means that if you have a block inside another block, the inner block should be indented 4 spaces more than the outer block.

# Example:

def withdraw(self, amount: float) -> None:  # Starting the method block
    if self.balance >= amount:              # Starting the if block
        self.balance -= amount
    # End of the if block
# End of the method block

# Practice Exercise

def withdraw(amount):
    balance = 500

    if balance >= amount:
        print("Amount withdrawn!")
        print("Please collect your money at the ATM.")

    print("Thank you for being our customer. Have a great day!")


def deposit(amount):
    balance = 500
    balance += amount


withdraw(1000)
