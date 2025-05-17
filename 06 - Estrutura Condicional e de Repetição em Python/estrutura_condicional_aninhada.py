# Estruturas Condicionais (if aninhado)

# Podemos criar estruturas condicionais dentro de outras estruturas condicionais.
# Isso é chamado de if aninhado (nested if).

# Exemplo:

regular_account = True
student_account = False
overdraft_limit = 450
balance = 2000
withdrawal = 1500

if regular_account:
    if balance >= withdrawal:
        print("Saque realizado com sucesso!")
    elif withdrawal <= (balance + overdraft_limit):
        print("Saque realizado utilizando o cheque especial!")
        
elif student_account:
    if balance >= withdrawal:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque!")

# Exercício de Prática

regular_account = False
student_account = False
special_account = True

balance = 2000
withdrawal = 1500
overdraft_limit = 450

if regular_account:

    if balance >= withdrawal:
        print("Saque realizado com sucesso!")
    elif withdrawal <= (balance + overdraft_limit):
        print("Saque realizado utilizando o cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif student_account:

    if balance >= withdrawal:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif special_account:
    print("Conta especial selecionada!")

else:
    print("O sistema não conseguiu reconhecer o tipo da sua conta. Por favor, entre em contato com seu gerente.")
