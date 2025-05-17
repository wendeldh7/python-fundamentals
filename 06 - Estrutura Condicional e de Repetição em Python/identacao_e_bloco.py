# Indentação e Blocos de Código

# A indentação é uma parte importante da sintaxe do Python.
# Ela define blocos de código, como aqueles dentro de funções, laços e estruturas condicionais.

# Estética

# A indentação é uma questão de estilo, mas também é uma exigência da sintaxe.
# O Python não utiliza chaves ou palavras-chave para definir blocos de código.
# Em vez disso, usa a indentação para indicar onde um bloco começa e termina.

# Isso significa que a indentação deve ser consistente em todo o seu código.
# Se você usar 4 espaços para indentar um bloco, deve usar 4 espaços para todos os outros blocos também.

# Bloco de Código

# Um bloco de código é um conjunto de instruções que são executadas juntas.
# Em Python, um bloco é definido por uma linha que termina com dois-pontos (:) 
# e as linhas subsequentes com indentação.

# Por exemplo, o código a seguir define um bloco que imprime "Olá, mundo!" se a variável x for maior que 10:

# Usando Espaços

# Existe um guia de estilo chamado PEP 8 que recomenda o uso de 4 espaços por nível de indentação.
# Isso significa que, se você tiver um bloco dentro de outro, o bloco interno deve ser indentado com 4 espaços a mais que o externo.

# Exemplo:

def withdraw(self, amount: float) -> None:  # Início do bloco do método
    if self.balance >= amount:              # Início do bloco do if
        self.balance -= amount
    # Fim do bloco do if
# Fim do bloco do método

# Exercício de Prática

def withdraw(amount):
    balance = 500

    if balance >= amount:
        print("Valor sacado!")
        print("Por favor, retire seu dinheiro no caixa eletrônico.")

    print("Obrigado por ser nosso cliente. Tenha um ótimo dia!")


def deposit(amount):
    balance = 500
    balance += amount


withdraw(1000)
