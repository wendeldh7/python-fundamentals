# Conversão de tipos em Python

# Em Python, podemos converter um tipo de dado em outro usando funções de conversão.
# O preço é um número inteiro, mas podemos convertê-lo para ponto flutuante.
# Exemplo de conversão de inteiro para float.
# Agora, price é um número de ponto flutuante (float).
# Podemos fazer operações matemáticas com números de ponto flutuante.

preco = 10  # preco é um número inteiro (int).
print(preco)

preco = float(preco)  # preco agora é um número de ponto flutuante (float).
print(preco)


# Exemplo de divisão

preco = 10 / 2  # O resultado é um número de ponto flutuante (float).
print(preco)

# Float para inteiro

# preco é um número de ponto flutuante, mas podemos convertê-lo para inteiro.

preco = 10.30
print(preco)

preco = int(preco)  # preco agora é um número inteiro (int).
print(preco)

# Conversão usando divisão

preco = 10
print(preco)

# Exemplo de divisão inteira

print(preco / 2)  # Resultado é um número de ponto flutuante (float).

print(preco // 2)  # Resultado é um número inteiro (int).

# Número para string

preco = 10.50
idade = 28

print(str(preco))  # Resultado é uma string (str).

print(str(idade))  # Resultado é uma string (str).

texto = f"Idade {idade} anos e preço {preco} dólares"
print(texto)  # Resultado é uma string (str).

# String para número

preco = "10.50"
idade = "28"

print(float(preco))  # Resultado é um número de ponto flutuante (float).

print(int(idade))  # Resultado é um número inteiro (int).
