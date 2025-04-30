class Cachorro:

# Método Construtor
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

# Método Destrutor
    def __del__(self):
        print("Destruindo a instância")

    def falar(self):
        print("AuAu!")

def criar_cachorro():
    c = Cachorro("Leela", "Preto e Marrom", False)
    print(c.nome, c.cor)
    
criar_cachorro()