# Estruturas Condicionais em Python

# O que são estruturas condicionais?
# Estruturas condicionais são comandos que permitem que um bloco de código seja executado se uma condição for verdadeira,
# e outro bloco se a condição for falsa. Elas são fundamentais para a lógica de programação porque
# permitem que o programa tome decisões com base em condições específicas.
# As estruturas condicionais mais comuns em Python são: if, elif e else.

# Instrução If

# A instrução if é usada para executar um bloco de código se uma condição for verdadeira.

# Exemplo:

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")

if saldo < saque:
    print("Saldo insuficiente para realizar o saque!")

# Instrução If-Else

# A instrução if-else é usada para executar um bloco de código se a condição for verdadeira e outro bloco se for falsa.

# Exemplo:

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
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

opcao = int(input("Digite sua opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Digite o valor do saque: "))
    print(f"Você solicitou o saque de R$ {valor:.2f}.")

elif opcao == 2:
    print("Exibindo extrato da conta...")

else:
    sys.exit("Opção inválida!")  # Você também pode usar: raise SystemExit("Opção inválida!")

# Exercício de Prática

IDADE_LEGAL = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= IDADE_LEGAL:
    print("Você tem idade suficiente para tirar a carteira de motorista.")

elif idade == IDADE_ESPECIAL:
    print("Você pode fazer aulas teóricas, mas não pode dirigir nas aulas práticas.")

else:
    print("Você ainda não tem idade para tirar a carteira de motorista.")
