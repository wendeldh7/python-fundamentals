# Strings em Python

# Uma string é uma sequência de caracteres que pode ser manipulada de várias maneiras.
# Em Python, strings são representadas por aspas simples (' ') ou aspas duplas (" ").
# As strings podem conter letras, números, símbolos e espaços em branco.
# As strings são imutáveis, ou seja, uma vez criadas, não podem ser alteradas.

# Maiúsculas, minúsculas e título
curso = "pYtHon"

print(curso.upper())  # Converte a string para letras maiúsculas
# >>> 'PYTHON'

print(curso.lower())  # Converte a string para letras minúsculas
# >>> 'python'

print(curso.title())  # Converte a string para formato de título (primeira letra de cada palavra em maiúscula)
# >>> 'Python'

# Removendo espaços em branco

curso = "   Python   "

print(curso.strip())  # Remove os espaços em branco do início e do final da string
# >>> 'Python'

print(curso.lstrip())  # Remove os espaços em branco do início (lado esquerdo) da string
# >>> 'Python   '

print(curso.rstrip())  # Remove os espaços em branco do final (lado direito) da string
# >>> '   Python'

# Juntando e centralizando strings

curso = "Python"

print(curso.center(20, "#"))  # Centraliza a string em um campo de 20 caracteres, preenchendo com '#'
# >>> '######Python######'

print(".".join(curso))  # Junta os caracteres da string inserindo '.' entre eles
# >>> 'P.y.t.h.o.n'
