# Operadores de Identidade

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso  # Verifica se o objeto é o mesmo na memória

curso is not nome_curso  # Verifica se o objeto não é o mesmo na memória

saldo is limite  # Verifica se o objeto é o mesmo na memória

# Exercício para fixação de conteúdo

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)