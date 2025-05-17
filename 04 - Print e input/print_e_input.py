name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

print(name, age)  # Imprime nome e idade com separador padrão (espaço) e quebra de linha no final
print(name, age, end="...\n")  # Imprime nome e idade, terminando com "..." e uma quebra de linha
print(name, age, sep="#", end="...\n")  # Imprime nome e idade separados por "#" e terminando com "..."
print(name, age, sep="#")  # Imprime nome e idade separados por "#" com quebra de linha padrão no final
