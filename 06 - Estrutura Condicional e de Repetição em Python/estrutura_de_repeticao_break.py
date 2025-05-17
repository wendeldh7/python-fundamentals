# Instrução Break
# A instrução break é usada para interromper um loop, seja ele um loop for ou while.

option = -1

while option != 0:
    option = int(input("Digite um número: "))
    
    if option == 10:
        break  # Interrompe o loop e sai
    print(option)

# Exercício de Prática

while True:
    number = int(input("Digite um número: "))

    if number == 10:
        continue  # Pula esta iteração e continua para a próxima

    if number % 2 == 0:
        break  # Interrompe o loop e sai

    print(number)

# Usando a instrução break em um loop for

for number in range(100):

    if number % 2 == 0:
        continue  # Pula esta iteração e continua para a próxima
    print(number, end=" ")
