# Introdução

# Fatiamento de string é uma técnica que permite extrair partes de uma string, utilizando índices para especificar o início e o fim do trecho desejado. Essa técnica é muito útil para manipular e analisar dados textuais.

# O fatiamento de string é feito utilizando colchetes `[]` e dois pontos `:` para indicar o intervalo desejado. A sintaxe básica é a seguinte:

# Fatiamento

nome = "Wendel Tertulino Da Cunha Gomes"

print(nome[0:5])  # Wende

print(nome[6:12])  # Tertul

print(nome[13:17])  # Da C

print(nome[18:23])  # Gomes

print(nome[0:5] + " " + nome[6:12] + " " + nome[13:17] + " " + nome[18:23])  # Wende Tertul Da C Gomes

# O fatiamento de string pode ser feito de várias maneiras, como por exemplo:

# - Fatiar do início até um determinado índice: `string[:índice]`

# - Fatiar de um determinado índice até o final: `string[índice:]`

# - Fatiar com um passo: `string[início:fim:passo]`
