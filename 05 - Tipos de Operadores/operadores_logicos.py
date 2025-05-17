# Operadores Lógicos
# Exemplo de operadores lógicos em Python

balance = 1000
withdraw = 200
limit = 100

balance >= withdraw 
# True, porque o saldo é maior ou igual ao valor do saque

withdraw <= limit
# False, porque o valor do saque não é menor ou igual ao limite

# Operador lógico AND (E)

balance = 1000
withdraw = 200
limit = 100

balance >= withdraw and withdraw <= limit
# False, porque o saque não está dentro do limite
# O operador AND retorna True apenas se todas as condições forem True
# O operador AND retorna False se pelo menos uma condição for False

# Operador lógico OR (OU)

balance = 1000
withdraw = 200
limit = 100

balance >= withdraw or withdraw <= limit
# True, porque o saldo é maior ou igual ao valor do saque
# O operador OR retorna True se pelo menos uma das condições for True
# O operador OR retorna False apenas se todas as condições forem False

# Operador lógico NOT (NÃO)

emergency_contacts = []

not 1000 > 1500 
# True, porque 1000 não é maior que 1500
# O operador NOT inverte o valor lógico da expressão

not emergency_contacts
# True, porque a lista emergency_contacts está vazia
# O operador NOT inverte o valor lógico da expressão

not "withdraw 1500;"
# False, porque a string não está vazia
# O operador NOT inverte o valor lógico da expressão

not ""
# True, porque a string está vazia
# O operador NOT inverte o valor lógico da expressão

# Parênteses

balance = 1000
withdraw = 250
limit = 200
special_account = True

balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
# True, porque o saldo é suficiente para o saque e é uma conta especial

(balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
# True, mesmo resultado, mas agrupar condições com parênteses melhora a legibilidade

# Exercício para praticar os conceitos

# AND = para ser True, tudo deve ser True
# OR = para ser True, pelo menos uma condição deve ser True

print(True and True and True)        # True
print(True and False and False)      # False
print(False and False and False)     # False
print(True or True or True)          # True
print(True or False or True)         # True
print(False or False or False)       # False

balance = 1000
withdraw = 250
limit = 200
special_account = True

exp = balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
print(exp)  # True

exp_2 = (balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
print(exp_2)  # True

normal_account_with_sufficient_balance = balance >= withdraw and withdraw <= limit
special_account_with_sufficient_balance = special_account and balance >= withdraw

exp_3 = normal_account_with_sufficient_balance or special_account_with_sufficient_balance
print(exp_3)  # True
