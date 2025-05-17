age = 28
name = "Wendel"
print(f'My name is {name} and I am {age} years old.')

# Example

age, name = (28, "Wendel")
print(f'My name is {name} and I am {age} years old.')

surname = 'Gomes'
age = 18

surname, age = "Wendel", 28
print(surname, age)

# Best practices

# 1. The naming convention is snake_case (lowercase letters separated by underscores)
# 2. Avoid variable names that are Python reserved words
# 3. Avoid variable names that are too generic (e.g., a, b, c, d, e, f, g, h, i, j)
# 4. Avoid variable names that are too long (e.g., variable_name_that_is_too_long)
# 5. Avoid variable names that are very similar (e.g., name, name1, name2, name3, name4, name5)
# 6. Avoid variable names that differ only by case (e.g., name, Name, NAME, nAME, noME, noMe)
# 7. Avoid variable names that are too different (e.g., name, Nome, NOME, nOME, noME, noMe)
# 8. Avoid variable names that are confusing (e.g., name, Name, NAME, nAME, noME, noMe)

# Example of snake_case naming

daily_withdrawal_limit = 1000

BRAZILIAN_STATES = ["RN", "SP", "RJ", "MG", "ES"]

print(BRAZILIAN_STATES)
