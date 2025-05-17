# Break Statement
# The break statement is used to interrupt a loop, whether it's a for loop or a while loop.

option = -1

while option != 0:
    option = int(input("Enter a number: "))
    
    if option == 10:
        break  # Interrupts the loop and exits
    print(option)

# Practice Exercise

while True:
    number = int(input("Enter a number: "))

    if number == 10:
        continue  # Skips this iteration and continues to the next

    if number % 2 == 0:
        break  # Interrupts the loop and exits

    print(number)

# Using the break statement in a for loop

for number in range(100):

    if number % 2 == 0:
        continue  # Skips this iteration and continues to the next
    print(number, end=" ")
