# Operadores de Identidade

curso = "Curso de Python"
nome_do_curso = curso
saldo, limite = 200, 200

curso is nome_do_curso  # Verifica se ambas as variáveis apontam para o mesmo objeto na memória

curso is not nome_do_curso  # Verifica se ambas as variáveis NÃO apontam para o mesmo objeto na memória

saldo is limite  # Verifica se ambas as variáveis apontam para o mesmo objeto na memória

# Exercício para praticar os conceitos

saldo = 1000
limite = 1000

print(saldo is limite)        # Pode ser True ou False, dependendo do cache de inteiros do Python
print(saldo is not limite)    # O oposto da expressão anterior
