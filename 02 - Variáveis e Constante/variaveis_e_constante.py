# Declaração e impressão com f-strings

idade = 28
nome = "Wendel"
print(f'Meu nome é {nome} e eu tenho {idade} anos.')

# Atribuição múltipla usando tuplas

idade, nome = (28, "Wendel")
print(f'Meu nome é {nome} e eu tenho {idade} anos.')

sobrenome = 'Gomes'
idade = 18

sobrenome, idade = "Wendel", 28
print(sobrenome, idade)

# Boas práticas para nomes de variáveis:

# 1. Use snake_case: letras minúsculas separadas por underscore
# 2. Evite nomes que são palavras reservadas do Python
# 3. Evite nomes genéricos como a, b, c, d, etc.
# 4. Evite nomes muito longos
# 5. Evite nomes muito parecidos (name1, name2, etc.)
# 6. Evite nomes que diferem só por maiúsculas/minúsculas (name, Name, NAME)
# 7. Evite nomes em línguas diferentes ou misturados (name, Nome, NOME)
# 8. Evite nomes confusos que dificultem o entendimento do código

# Exemplo de nomenclatura snake_case e constante em maiúsculas

limite_saque_diario = 1000

BRAZILIAN_STATES = ["RN", "SP", "RJ", "MG", "ES"]

print(BRAZILIAN_STATES)
