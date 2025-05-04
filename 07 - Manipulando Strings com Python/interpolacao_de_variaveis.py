# Introdução

# Interpolação de variáveis é o processo de inserir valores de variáveis em uma string. Isso pode ser feito de várias maneiras em Python, incluindo o uso de f-strings, o método format() e a concatenação de strings.

# O sinal % não é mais utilizado para interpolação de variáveis em Python, mas ainda pode ser encontrado em código legado.

# Old style %

nome = "Wendel"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Meu nome é %s, tenho %d anos e sou %s. Estou aprendendo %s." % (nome, idade, profissao, linguagem)) # O operador % é usado para formatar strings, onde %s é um espaço reservado para uma string, %d para um número inteiro e %f para um número de ponto flutuante.

# Método format()

nome = "Wendel"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Meu nome é {}, tenho {} anos e sou {}. Estou aprendendo {}.".format(nome, idade, profissao, linguagem)) # O método format() é usado para formatar strings, onde {} é um espaço reservado para uma string.

print("Meu nome é {3}, tenho {2} anos e sou {1}. Estou aprendendo {2}.".format(linguagem, profissao, idade, nome)) # O método format() também permite especificar a ordem dos argumentos.

print("Meu nome é {nome}, tenho {idade} anos e sou {profissao}. Estou aprendendo {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)) # O método format() também permite usar nomes de variáveis como argumentos.

# Uso de dicionários

pessoa = {
    "nome": "Wendel",
    "idade": 28,
    "profissao": "Programador",
    "linguagem": "Python"
}

print("Meu nome é {nome}, tenho {idade} anos e sou {profissao}. Estou aprendendo {linguagem}.".format(**pessoa)) # O método format() também permite usar dicionários como argumentos.

# Uso do f-string

nome = "Wendel"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Meu nome é {nome}, tenho {idade} anos e sou {profissao}. Estou aprendendo {linguagem}.") # O f-string é uma forma mais moderna e legível de formatar strings, onde as variáveis são inseridas diretamente na string usando chaves {}.


# Formatar strings com f-string

PI = 3.14159

print(f"PI = {PI:.2f}") # O f-string também permite formatar números, onde :.2f significa que o número deve ser formatado com 2 casas decimais.

print(f"PI = {PI:10.2f}") # O f-string também permite formatar números com largura mínima, onde 10.2f significa que o número deve ser formatado com 10 caracteres de largura e 2 casas decimais.
