# Estruturas Condicionais (if aninhado)

# Podemos criar estruturas condicionais dentro de outras estruturas condicionais.
# Isso é chamado de if aninhado (nested if).

# Exemplo:

conta_regular = True
conta_estudante = False
limite_cheque_especial = 450
saldo = 2000
saque = 1500

if conta_regular:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + limite_cheque_especial):
        print("Saque realizado utilizando o cheque especial!")
        
elif conta_estudante:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque!")

# Exercício de Prática

conta_regular = False
conta_estudante = False
conta_especial = True

saldo = 2000
saque = 1500
limite_cheque_especial = 450

if conta_regular:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + limite_cheque_especial):
        print("Saque realizado utilizando o cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_estudante:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("O sistema não conseguiu reconhecer o tipo da sua conta. Por favor, entre em contato com seu gerente.")
