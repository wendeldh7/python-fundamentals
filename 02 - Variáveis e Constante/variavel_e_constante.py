# Declaração e impressão com f-strings

age = 28
name = "Wendel"
print(f'My name is {name} and I am {age} years old.')

# Atribuição múltipla usando tuplas

age, name = (28, "Wendel")
print(f'My name is {name} and I am {age} years old.')

surname = 'Gomes'
age = 18

surname, age = "Wendel", 28
print(surname, age)

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

daily_withdrawal_limit = 1000

BRAZILIAN_STATES = ["RN", "SP", "RJ", "MG", "ES"]

print(BRAZILIAN_STATES)
