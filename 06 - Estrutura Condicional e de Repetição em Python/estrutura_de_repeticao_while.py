# Instrução While usando variável 'opcao'

opcao = -1  # Inicializa a opção com valor diferente de 0 para entrar no loop

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato da conta...")

else:
    print("Obrigado por utilizar nosso sistema bancário. Até a próxima!")
