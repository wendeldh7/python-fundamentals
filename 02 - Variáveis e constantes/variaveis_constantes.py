age = 28
name = "Wendel"
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade.')

# Exemplo

age, name = (28, "Wendel")
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade.')

nome = 'Gomes'
idade = 18

nome, idade = "Wendel", 28
print(nome, idade)

# Boas práticas

# 1. O padrão de nomenclatura é snake_case (letras minúsculas e separadas por underline)
# 2. Evitar nomes de variáveis que sejam palavras reservadas do Python
# 3. Evitar nomes de variáveis que sejam muito genéricos (ex: a, b, c, d, e, f, g, h, i, j)
# 4. Evitar nomes de variáveis que sejam muito longos (ex: nome_da_variavel_que_eh_muito_longo)
# 5. Evitar nomes de variáveis que sejam muito semelhantes (ex: nome, nome1, nome2, nome3, nome4, nome5)
# 6. Evitar nomes de variáveis que sejam muito parecidos (ex: nome, Nome, NOME, nOME, noME, noMe)
# 7. Evitar nomes de variáveis que sejam muito diferentes (ex: nome, Nome, NOME, nOME, noME, noMe)
# 8. Evitar nomes de variáveis que sejam muito confusos (ex: nome, Nome, NOME, nOME, noME, noMe)


# Exemplo de nomenclatura snake_case

limite_saque_diario = 1000

BRAZILIAN_STATES = ["RN", "SP", "RJ", "MG", "ES"]

print(BRAZILIAN_STATES)