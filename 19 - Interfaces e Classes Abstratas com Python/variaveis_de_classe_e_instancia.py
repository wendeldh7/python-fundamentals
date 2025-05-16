# Variáveis de classe e variáveis de instância

# Atributos do objeto
# Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

# Exemplo

class Estudante:
    escola = "DIO"

def __init__(self, nome, numero):
    self.nome = nome
    self.numero = numero

def __str__(self):
    return f"{self.nome} ({self.numero}) - {self.escola}"

gui = Estudante("Guilherme", 56451)
gi = Estudante("Giovanna", 17323)
