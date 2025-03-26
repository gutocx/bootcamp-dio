nome = "Augusto"
idade = 25
profissao = "Estudante"
linguagem = "Python"

cadastro = {"nome": "Augusto", "idade": 25}

# Old Style % (rara utilização / dificil manutenção em strings longas)
print("Nome: %s Idade: %d Profissão: %s" % (nome, idade, profissao)) #precisa colocar em ordem sequencial os valores
print()

# Método format (bom para reaproveitamento de variáveis)
print("Nome: {2} Idade: {0} Profissão: {1} Linguagem: {2}".format(idade, profissao, nome, linguagem)) #utiliza índice para "armazenar" o valor solicita
print()
print("Nome: {nome} Idade: {idade}".format(**cadastro)) #utilizando a biblioteca
print()

# Método f-string (a mais comum de ser utilizada)
print(f"Nome: {nome} Idade: {idade} Profissao: {profissao}")