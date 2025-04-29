# Conversão de tipos em Python

# Em Python, podemos converter um tipo de dado para outro usando funções de conversão.
# O preço é um número inteiro, mas podemos convertê-lo para float
# Exemplo de conversão de inteiro para float
# Agora, o preço é um número de ponto flutuante (float).
# Podemos fazer operações matemáticas com números de ponto flutuante.

preco = 10 # O preço é um número inteiro (int).
print(preco)

preco = float(preco) # O preço é um número de ponto flutuante (float).
print(preco)


# Exemplo de divisão

preco = 10 / 2 # O resultado é um número de ponto flutuante (float).
print(preco)

# Float para inteiro

# O preço é um número de ponto flutuante, mas podemos convertê-lo para inteiro.

preco = 10.30
print(preco)

preco = int(preco) # O preço é um número inteiro (int).
print(preco)

# Conversão por divisão

preco = 10
print(preco)

# Exemplo de divisão inteira

print(preco / 2) # O resultado é um número de ponto flutuante (float).

print(preco // 2) # O resultado é um número inteiro (int).

# Número para string

preco = 10.50
idade = 28

print(str(preco)) # O resultado é uma string (str).

print(str(idade)) # O resultado é uma string (str).

texto = f"Idade {idade} anos e preço {preco} reais"
print(texto) # O resultado é uma string (str).

# String para número

preco = "10.50"
idade = "28"

print(float(preco)) # O resultado é um número de ponto flutuante (float).

print(int(idade)) # O resultado é um número inteiro (int).