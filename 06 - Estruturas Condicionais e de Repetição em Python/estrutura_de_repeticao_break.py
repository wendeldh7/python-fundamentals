# Comando Break
# O comando break é utilizado para interromper um loop, seja ele um loop for ou while.

opcao = -1

while opcao != 0:
    opcao = int(input("Informe um número: "))
    
    if opcao == 10:
        break # Interrompe o loop e sai da execução
    print(opcao)

# Exercício para fixação de conteúdo

while True:
    numero = int(input("Informe um número: "))

    if numero == 10: 
        continue # Pula o loop e continua a execução

    if numero % 2 == 0:
        break # Interrompe o loop e sai da execução


    print(numero)

# Usando o comando break em um loop for

for numero in range(100):

    if numero % 2 == 0:
        continue # Pula o loop e continua a execução
    print(numero, end=" ")  