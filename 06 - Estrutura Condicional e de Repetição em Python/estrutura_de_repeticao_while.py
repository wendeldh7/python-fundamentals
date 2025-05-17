# Instrução While

# A instrução while é usada para executar um bloco de código enquanto uma condição for verdadeira.

option = -1

while option != 0:
    option = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if option == 1:
        print("Sacando...")
    elif option == 2:
        print("Exibindo extrato da conta...")

# Estrutura While/Else

option = -1

while option != 0:
    option = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if option == 1:
        print("Sacando...")
    elif option == 2:
        print("Exibindo extrato da conta...")

else:
    print("Obrigado por utilizar nosso sistema bancário. Até a próxima!")
