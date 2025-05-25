from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("\nLigando a TV...")
        print("A TV está ligada!")

    def desligar(self):
        print("\nDesligando a TV...")
        print("A TV foi desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("\nLigando o Ar Condicionado...")
        print("Ar Condicionado ligado!")
    
    def desligar(self):
        print("\nDesligando o Ar Condicionado...")
        print("Ar Condicionado desligado!")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)