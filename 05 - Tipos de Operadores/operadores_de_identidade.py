# Operadores de Identidade

course = "Python Course"
course_name = course
balance, limit = 200, 200

course is course_name  # Verifica se ambas as variáveis apontam para o mesmo objeto na memória

course is not course_name  # Verifica se ambas as variáveis NÃO apontam para o mesmo objeto na memória

balance is limit  # Verifica se ambas as variáveis apontam para o mesmo objeto na memória

# Exercício para praticar os conceitos

balance = 1000
limit = 1000

print(balance is limit)        # Pode ser True ou False, dependendo do cache de inteiros do Python
print(balance is not limit)    # O oposto da expressão anterior
