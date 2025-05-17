# Decoradores em Python

# Em Python, funções são objetos de primeira classe, o que significa que podem:
# - Ser atribuídas a variáveis
# - Ser passadas como argumentos
# - Ser retornadas por outras funções

# Também é possível definir funções dentro de outras funções (funções internas)
# e retornar essas funções. Isso nos permite criar decoradores.

# -------------------------------------------
# Exemplo de decorador simples
def meu_decorador(func):
    # Função interna (wrapper) que será executada no lugar da função original
    def wrapper(*args, **kwargs):
        # Aqui você pode adicionar código antes da execução da função original
        print("Antes da função ser executada.")
        resultado = func(*args, **kwargs)  # Chamada da função original
        # Aqui você pode adicionar código depois da execução da função original
        print("Depois da função ser executada.")
        return resultado  # Retorna o resultado da função original
    return wrapper  # Retorna a nova função com comportamento alterado

# Aplicando o decorador com o açúcar sintático @
@meu_decorador
def minha_funcao():
    print("Executando minha função!")

minha_funcao()

# -------------------------------------------
# Decorador aplicado manualmente, sem usar o @
def ola_mundo():
    print("Olá mundo!")

# Aplica o decorador 'meu_decorador' na função 'ola_mundo'
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

# -------------------------------------------
# Decorador que aceita qualquer número de argumentos com *args e **kwargs
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Executando algo antes da função.")
        resultado = funcao(*args, **kwargs)
        print("Executando algo depois da função.")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("João", 1000)
print("Resultado retornado:", resultado)

# -------------------------------------------
# Introspecção e uso de functools.wraps
# functools.wraps é usado para preservar metadados da função original,
# como o nome, docstring, etc.

import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)  # Preserva as informações da função original
    def envelope(*args, **kwargs):
        print("Antes da execução")
        return funcao(*args, **kwargs)
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    """Esta função exibe uma saudação personalizada."""
    print(f"Olá mundo {nome}!")

print(ola_mundo.__name__)  # Sem functools.wraps, isso retornaria "envelope"
print(ola_mundo.__doc__)   # Mostra a docstring da função original
ola_mundo("Maria", 123)

# -------------------------------------------
# Outro exemplo de decorador com lógica antes e depois da função

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")

ola_mundo("João", 1000)
