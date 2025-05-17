# Conversão de tipos em Python

# Em Python, podemos converter um tipo de dado em outro usando funções de conversão.
# O preço é um número inteiro, mas podemos convertê-lo para ponto flutuante.
# Exemplo de conversão de inteiro para float.
# Agora, price é um número de ponto flutuante (float).
# Podemos fazer operações matemáticas com números de ponto flutuante.

price = 10  # Price é um número inteiro (int).
print(price)

price = float(price)  # Price agora é um número de ponto flutuante (float).
print(price)


# Exemplo de divisão

price = 10 / 2  # O resultado é um número de ponto flutuante (float).
print(price)

# Float para inteiro

# Price é um número de ponto flutuante, mas podemos convertê-lo para inteiro.

price = 10.30
print(price)

price = int(price)  # Price agora é um número inteiro (int).
print(price)

# Conversão usando divisão

price = 10
print(price)

# Exemplo de divisão inteira

print(price / 2)  # Resultado é um número de ponto flutuante (float).

print(price // 2)  # Resultado é um número inteiro (int).

# Número para string

price = 10.50
age = 28

print(str(price))  # Resultado é uma string (str).

print(str(age))  # Resultado é uma string (str).

text = f"Idade {age} anos e preço {price} dólares"
print(text)  # Resultado é uma string (str).

# String para número

price = "10.50"
age = "28"

print(float(price))  # Resultado é um número de ponto flutuante (float).

print(int(age))  # Resultado é um número inteiro (int).
