# O que são laços (loops)?

# Laços (ou loops) são comandos que permitem repetir um bloco de código várias vezes até que uma condição seja satisfeita.
# Eles são úteis para automatizar tarefas repetitivas e economizar tempo de desenvolvimento.

# Existem dois tipos principais de laços em Python: o laço "for" e o laço "while".

# O laço "for" é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um intervalo de números.
# Ele executa um bloco de código para cada item da sequência.

# O laço "while" executa um bloco de código enquanto uma condição for verdadeira.
# É útil quando não sabemos quantas vezes precisamos repetir o código ou quando queremos repetir até que uma condição específica seja atendida.

# A instrução "for"

# A instrução "for" é usada para iterar sobre uma sequência (como uma lista, tupla ou string) ou um intervalo de números.
# Ela executa um bloco de código para cada item da sequência.

# Exemplo usando o laço "for"

text = input("Digite um texto: ")
AEIOU = "AEIOU"

for letter in text:
    if letter.upper() in AEIOU:
        print(letter, end=" ")

print()  # Imprime uma nova linha após o laço

# Estrutura for/else

text = input("Digite um texto: ")
AEIOU = "AEIOU"

for letter in text:
    if letter.upper() in AEIOU:
        print(letter, end=" ")
else:
    print()  # Imprime uma nova linha após o laço

# Função embutida range()

# A função embutida range() é usada para gerar uma sequência de números.
# Ela pode ser usada em laços "for" para iterar sobre um intervalo de valores.

# A função range() pode receber até três argumentos: início, fim e passo.
# O valor de início está incluído na sequência, enquanto o valor de fim não está.
# O valor de passo é opcional e define o intervalo entre os números.

# Exemplo usando a função range()

list(range(4))  # Gera uma lista com os números de 0 a 3
# >>> [0, 1, 2, 3]

# Usando range() em um laço "for"

for number in range(11):
    print(number, end=" ")
# >>> 0 1 2 3 4 5 6 7 8 9 10

# Exibindo a tabuada do 5

for number in range(0, 51, 5):
    print(number, end=" ")
# >>> 0 5 10 15 20 25 30 35 40 45 50

# Exercício de prática

text = input("Digite um texto: ")
AEIOU = "AEIOU"

# Exemplo usando um iterável
for letter in text:
    if letter.upper() in AEIOU:
        print(letter, end="")
else:
    print()  # Adiciona uma quebra de linha ao final

# Exemplo usando a função embutida range
for number in range(0, 51, 5):
    print(number, end=" ")
