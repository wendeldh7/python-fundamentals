# Estruturas Condicionais em Python

# O que são estruturas condicionais?
# Estruturas condicionais são comandos que permitem que um bloco de código seja executado se uma condição for verdadeira,
# e outro bloco se a condição for falsa. Elas são fundamentais para a lógica de programação porque
# permitem que o programa tome decisões com base em condições específicas.
# As estruturas condicionais mais comuns em Python são: if, elif e else.

# Instrução If

# A instrução if é usada para executar um bloco de código se uma condição for verdadeira.

# Exemplo:

balance = 2000.0
withdrawal = float(input("Digite o valor do saque: "))

if balance >= withdrawal:
    print("Saque realizado com sucesso!")

if balance < withdrawal:
    print("Saldo insuficiente para realizar o saque!")

# Instrução If-Else

# A instrução if-else é usada para executar um bloco de código se a condição for verdadeira e outro bloco se for falsa.

# Exemplo:

balance = 2000.0
withdrawal = float(input("Digite o valor do saque: "))

if balance >= withdrawal:
    print("Saque realizado com sucesso!")

else:
    print("Saldo insuficiente para realizar o saque!")

# Instrução If-Elif-Else

# A estrutura if-elif-else é usada para avaliar múltiplas condições:
# - se uma condição for verdadeira, um bloco é executado
# - elif (else if) verifica outra condição
# - else é executado se nenhuma das condições anteriores for verdadeira

# Exemplo:

import sys

option = int(input("Digite sua opção: [1] Sacar \n[2] Extrato: "))

if option == 1:
    amount = float(input("Digite o valor do saque: "))

elif option == 2:
    print("Exibindo extrato da conta...")

else:
    sys.exit("Opção inválida!")  # Você também pode usar: raise SystemExit("Opção inválida!")
    # Se usar sys.exit, é necessário importar o módulo sys.

# Exercício de Prática

LEGAL_AGE = 18
SPECIAL_AGE = 17

age = int(input("Digite sua idade: "))

if age >= LEGAL_AGE:
    print("Você tem idade suficiente para tirar a carteira de motorista.")

elif age == SPECIAL_AGE:
    print("Você pode fazer aulas teóricas, mas não pode dirigir nas aulas práticas.")

else:
    print("Você ainda não tem idade para tirar a carteira de motorista.")
