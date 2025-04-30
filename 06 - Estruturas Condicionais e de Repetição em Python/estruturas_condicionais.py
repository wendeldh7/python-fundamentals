# Estruturas condicionais em Python

# O que são estruturas condicionais?
# Estruturas condicionais são comandos que permitem executar um bloco de código se uma condição for verdadeira e outro bloco de código se a condição for falsa. Elas são fundamentais para a lógica de programação, pois permitem que o programa tome decisões com base em condições específicas.
# As estruturas condicionais mais comuns em Python são o if, elif e else.

# Estrutura condicional (if)

# A estrutura condicional if é usada para executar um bloco de código se uma condição for verdadeira.

# Exemplo:

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")
    
if saldo < saque:
    print("Saldo insuficiente para realizar o saque!")
    
# Estrutura condicional (if-else)

# A estrutura condicional if-else é usada para executar um bloco de código se uma condição for verdadeira e outro bloco de código se a condição for falsa.

# Exemplo:

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")
    
else:
    print("Saldo insuficiente para realizar o saque!")
    
# Estrutura condicional (if-elif-else)

# A estrutura condicional if-elif-else é usada para executar um bloco de código se uma condição for verdadeira, outro bloco de código se outra condição for verdadeira e outro bloco de código se nenhuma das condições anteriores for verdadeira.

# Exemplo:
import sys

opcao = int(input("Digite a opção desejada: [1] Sacar \n[2] Estrato: "))

if  opcao == 1:
    valor = float(input("Digite o valor do saque: "))
    
elif opcao == 2:
    print("Exibindo extrato...")
    
else:
    sys.exit("Opção inválida!") # Também pode ser usado o raise SystemExit("Opção inválida!") não e comum, mas é uma opção válida.
    
    # Se for usar sys.exit é necessário importar a biblioteca sys.
    
# Exercício para fixação de conteúdo

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
    
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
    
else:
    print("Ainda não pode tirar a CNH.")