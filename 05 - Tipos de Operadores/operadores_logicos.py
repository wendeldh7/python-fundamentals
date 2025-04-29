# Operadores lógicos
# Exemplo de operadores lógicos em Python

saldo = 1000
saque = 200
limite = 100

saldo >= saque 
# True, pois o saldo é maior ou igual ao saque

saque <= limite
# False, pois o saque não é menor ou igual ao limite

# Operador lógico AND(E)

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
# False, pois o saque não é menor ou igual ao limite
# O operador AND retorna True se ambas as condições forem verdadeiras
# O operador AND retorna False se uma das condições for falsa

# Operador lógico OR(OU)
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
# True, pois o saldo é maior ou igual ao saque
# O operador OR retorna True se uma das condições for verdadeira
# O operador OR retorna False se ambas as condições forem falsas

# Operador lógico NOT(NÃO)

contatos_emergencia = []

not 1000 > 1500 
# True, pois 1000 não é maior que 1500
# O operador NOT inverte o valor lógico da expressão

not contatos_emergencia
# True, pois a lista contatos_emergencia está vazia
# O operador NOT inverte o valor lógico da expressão

not "saque 1500;"
# False, pois a string não está vazia
# O operador NOT inverte o valor lógico da expressão

not ""
# True, pois a string está vazia
# O operador NOT inverte o valor lógico da expressão

# Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# True, pois o saldo é maior ou igual ao saque e o saque é menor ou igual ao limite

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# True, pois o saldo é maior ou igual ao saque e o saque é menor ou igual ao limite

# Exercício para fixação de conteúdo

# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and False)
print(False and False and False)
print(True or True or True)
print(True or False or True)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)