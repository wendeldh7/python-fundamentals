name = input("Enter your name: ")
age = input("Enter your age: ")

print(name, age)  # Print name and age with default separator (space) and newline at the end
print(name, age, end="...\n")  # Print name and age, ending with "..." and a newline
print(name, age, sep="#", end="...\n")  # Print name and age separated by "#" and ending with "..."
print(name, age, sep="#")  # Print name and age separated by "#" with default newline at the end
