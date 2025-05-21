class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    

p = Pessoa().criar_de_data_nascimento(1999,6,2,"Augusto")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(29))
print(Pessoa.e_maior_idade(12))