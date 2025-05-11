# Nosso primeiro programa POO

#  João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim, Plim...")
    
    def parar(self):
        print("Parando a Bicicleta...")
        print("Bicicleta parada!")
        
    def correr(self):
        print("Vrummmmm...")
    
    # Podemos usar dessa forma também

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("verde", "caloi", "2025", 600)

# Acessando os métodos

b1.buzinar()
b1.correr()
b1.parar()

# Acessando os atributos

print(b1.cor, b1.modelo, b1.ano, b1.valor)
