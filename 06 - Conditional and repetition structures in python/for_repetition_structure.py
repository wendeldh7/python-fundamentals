# What are loops?

# Loops are commands that allow you to repeat a block of code multiple times until a condition is met.
# They are useful for automating repetitive tasks and saving development time.

# There are two main types of loops in Python: the "for" loop and the "while" loop.

# The "for" loop is used to iterate over a sequence (such as a list, tuple, or string) or a range of numbers.
# It executes a block of code for each item in the sequence.

# The "while" loop executes a block of code as long as a condition is True.
# It's useful when we don't know how many times we need to repeat the code, or when we want to repeat it until a specific condition is met.

# The "for" statement

# The "for" statement is used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.
# It runs a block of code for each item in the sequence.

# Example using a "for" loop

text = input("Enter a text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end=" ")

print()  # Prints a new line after the loop

# for/else structure

text = input("Enter a text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end=" ")
else:
    print()  # Prints a new line after the loop

# Built-in function range()

# The built-in range() function is used to generate a sequence of numbers.
# It can be used in "for" loops to iterate over a range of values.

# The range() function can take up to three arguments: start, stop, and step.
# The start value is included in the sequence, while the stop value is not.
# The step value is optional and defines the interval between numbers.

# Example using the range() function

list(range(4))  # Generates a list with numbers from 0 to 3
# >>> [0, 1, 2, 3]

# Using range() in a "for" loop

for number in range(11):
    print(number, end=" ")
# >>> 0 1 2 3 4 5 6 7 8 9 10

# Displaying the multiplication table of 5

for number in range(0, 51, 5):
    print(number, end=" ")
# >>> 0 5 10 15 20 25 30 35 40 45 50

# Practice Exercise

text = input("Enter a text: ")
VOWELS = "AEIOU"

# Example using an iterable
for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print()  # Adds a newline at the end

# Example using the built-in range function
for number in range(0, 51, 5):
    print(number, end=" ")
