# Type conversion in Python

# In Python, we can convert one data type to another using conversion functions.
# The price is an integer, but we can convert it to a float.
# Example of converting an integer to a float.
# Now, price is a floating point number (float).
# We can do mathematical operations with floating point numbers.

price = 10  # Price is an integer (int).
print(price)

price = float(price)  # Price is now a floating point number (float).
print(price)


# Example of division

price = 10 / 2  # The result is a floating point number (float).
print(price)

# Float to integer

# Price is a floating point number, but we can convert it to an integer.

price = 10.30
print(price)

price = int(price)  # Price is now an integer (int).
print(price)

# Conversion using division

price = 10
print(price)

# Example of integer division

print(price / 2)  # Result is a floating point number (float).

print(price // 2)  # Result is an integer (int).

# Number to string

price = 10.50
age = 28

print(str(price))  # Result is a string (str).

print(str(age))  # Result is a string (str).

text = f"Age {age} years and price {price} dollars"
print(text)  # Result is a string (str).

# String to number

price = "10.50"
age = "28"

print(float(price))  # Result is a floating point number (float).

print(int(age))  # Result is an integer (int).
