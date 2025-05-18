# Instrução Break
# A instrução break é usada para interromper um loop, seja ele um loop for ou while.

opcao = -1

while opcao != 0:
    opcao = int(input("Digite um número: "))
    
    if opcao == 10:
        break  # Interrompe o loop e sai
    print(opcao)

# Exercício de Prática

while True:
    numero = int(input("Digite um número: "))

    if numero == 10:
        continue  # Pula esta iteração e continua para a próxima

    if numero % 2 == 0:
        break  # Interrompe o loop e sai

    print(numero)

# Usando a instrução break em um loop for

for numero in range(100):

    if numero % 2 == 0:
        continue  # Pula esta iteração e continua para a próxima
    print(numero, end=" ")
