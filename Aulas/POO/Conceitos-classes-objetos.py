#Crie um programa onde João informe: cor, modelo, ano e valor
#da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
#self é uma referência explicita pro objeto. Essa é a instância do objeto que foi passado.

    def buzinar(self):
        print("Honk! Honk!")
    
    def parar(self):
        print("Freiando...")
        print("Bicicleta parada.")

    def correr(self):
        print("Acelerando.... VRUUUUUMMMMMMMMMM")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor
                                                        in self.__dict__.items()])}"
    
b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 450)
print(b2)