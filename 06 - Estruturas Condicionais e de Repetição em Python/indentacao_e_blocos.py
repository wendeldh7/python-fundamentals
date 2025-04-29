# Indentação e os blos de comandos

# A indentação é uma parte importante da sintaxe do Python. Ela define os blocos de código, como os que estão dentro de funções, loops e condicionais.

# A Estética

# A indentação é uma questão de estética, mas também é uma questão de sintaxe. O Python não usa chaves ou palavras-chave para definir blocos de código. Em vez disso, ele usa a indentação para indicar onde um bloco começa e termina.

# Isso significa que a indentação deve ser consistente em todo o seu código. Se você usar 4 espaços para indentar um bloco de código, deve usar 4 espaços para todos os outros blocos de código também.

# Bloco de comando

# Um bloco de comando é um conjunto de instruções que são executadas juntas. No Python, um bloco de comando é definido por uma linha de código que termina com dois pontos (:) e todas as linhas subsequentes que estão indentadas em relação a essa linha.

# Por exemplo, o seguinte código define um bloco de comando que imprime "Olá, mundo!" se a variável x for maior que 10:

# Utilizando espaços

# Existe uma convenção de estilo chamada PEP 8 que recomenda o uso de 4 espaços para cada nível de indentação. Isso significa que, se você tiver um bloco de código dentro de outro bloco de código, o segundo bloco deve ser indentado com 4 espaços a mais do que o primeiro bloco.

# Exemplo:

def sacar(self, valor: float) -> None: # Iniciando do bloco método
    if self.saldo >= valor: # Iniciando do bloco if
        self.saldo -= valor
    # Fim do bloco if
# Fim do bloco método

# Exercício para fixação de conteúdo

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)