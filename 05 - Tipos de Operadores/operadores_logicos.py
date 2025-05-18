# Operadores Lógicos
# Exemplo de operadores lógicos em Python

saldo = 1000
saque = 200
limite = 100

saldo >= saque
# True, porque o saldo é maior ou igual ao valor do saque

saque <= limite
# False, porque o valor do saque não é menor ou igual ao limite

# Operador lógico AND (E)

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
# False, porque o saque não está dentro do limite
# O operador AND retorna True apenas se todas as condições forem True
# O operador AND retorna False se pelo menos uma condição for False

# Operador lógico OR (OU)

saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
# True, porque o saldo é maior ou igual ao valor do saque
# O operador OR retorna True se pelo menos uma das condições for True
# O operador OR retorna False apenas se todas as condições forem False

# Operador lógico NOT (NÃO)

contatos_de_emergencia = []

not 1000 > 1500
# True, porque 1000 não é maior que 1500
# O operador NOT inverte o valor lógico da expressão

not contatos_de_emergencia
# True, porque a lista contatos_de_emergencia está vazia
# O operador NOT inverte o valor lógico da expressão

not "saque 1500;"
# False, porque a string não está vazia
# O operador NOT inverte o valor lógico da expressão

not ""
# True, porque a string está vazia
# O operador NOT inverte o valor lógico da expressão

# Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# True, porque o saldo é suficiente para o saque e é uma conta especial

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
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

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # True

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)  # True

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)  # True
