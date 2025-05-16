class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join
        ([f'{chave}={valor}' for chave, valor in self.
        __dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, transportando):
        super().__init__(cor, placa, numero_rodas)
        self.transportando = transportando

    def transportando(self):
        print(f"{'Sim' if self.transportando else 'Não'} estou transportando carga.")

moto = Motocicleta("Preta", "abc-1234", 2)
carro = Carro("Amarelo", "xdr-0098", 4)
caminhao = Caminhao("Branco", "mbn-8724", 8, True)

print(moto)
print(carro)
print(caminhao)