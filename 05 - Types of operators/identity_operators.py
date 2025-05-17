# Identity Operators

course = "Python Course"
course_name = course
balance, limit = 200, 200

course is course_name  # Checks if both variables point to the same object in memory

course is not course_name  # Checks if both variables do NOT point to the same object in memory

balance is limit  # Checks if both variables point to the same object in memory

# Exercise to practice the concepts

balance = 1000
limit = 1000

print(balance is limit)
print(balance is not limit)
