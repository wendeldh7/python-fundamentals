# O que são estruturas de repetição?

# Estruturas de repetição são comandos que permitem repetir um bloco de código várias vezes, até que uma condição seja atendida. Elas são úteis para automatizar tarefas repetitivas e economizar tempo de programação.

# Existem dois tipos principais de estruturas de repetição em Python: o loop "for" e o loop "while".

# O loop "for" é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um intervalo de números. Ele executa um bloco de código para cada item na sequência.

# O loop "while" executa um bloco de código enquanto uma condição for verdadeira. Ele é útil quando não sabemos quantas vezes precisamos repetir o código, ou quando queremos repetir o código até que uma condição específica seja atendida.

# Comando "for"

# O comando "for" é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um intervalo de números. Ele executa um bloco de código para cada item na sequência.

# Exemplo estrutura de repetição "for"

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
        
print() # Exibe uma nova linha após o loop

# for/else


texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:        
    print() # Exibe uma nova linha após o loop
    
# função built-in range()

# A função built-in range() é usada para gerar uma sequência de números. Ela pode ser usada em loops "for" para iterar sobre um intervalo de números.

# A função range() pode receber até três argumentos: o valor inicial, o valor final e o passo. O valor inicial é incluído na sequência, enquanto o valor final não é incluído. O passo é opcional e define a diferença entre os números na sequência.

# Exemplo de uso da função range()

list(range(4)) # Gera uma lista com os números de 0 a 3
# >>> [0, 1, 2, 3]

# Utilizando range() em um loop "for"

for numero in range(11):
    print(numero, end=" ")
# >>> 0 1 2 3 4 5 6 7 8 9 10

# Exibindo a tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")
# >>> 0 5 10 15 20 25 30 35 40 45 50

# Exercício para fixação de conteúdo

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")