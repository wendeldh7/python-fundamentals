# String em Python

# String é uma sequência de caracteres que pode ser manipulada de várias formas.
# Em Python, strings são representadas por aspas simples (' ') ou aspas duplas (" ").
# Strings podem conter letras, números, símbolos e espaços em branco.
# Strings são imutáveis, ou seja, uma vez criadas, não podem ser alteradas.

# Maiúscula, minúsculas e título
curso = "pYtHon"

print(curso.upper())  # Converte a string para maiúsculas
# >>> 'PYTHON'

print(curso.lower())  # Converte a string para minúsculas
# >>> 'python'

print(curso.title())  # Converte a string para título (primeira letra de cada palavra em maiúscula)
# >>> 'Python'

# Eliminação de espaços em branco

curso = "   Python   "

print(curso.strip())  # Remove os espaços em branco do início e do fim da string
# >>> 'Python'

print(curso.lstrip())  # Remove os espaços em branco do início da string
# >>> 'Python   '

print(curso.rstrip())  # Remove os espaços em branco do fim da string
# >>> '   Python'

# Junção e Centralização de strings

curso = "Python"

print(curso.center(20, "#"))  # Centraliza a string em um campo de 20 caracteres, preenchendo com '#'
# >>> '######Python######'

print(".".join(curso))  ## Junta os caracteres da string com '.' entre eles
# >>> 'P.y.t.h.o.n'