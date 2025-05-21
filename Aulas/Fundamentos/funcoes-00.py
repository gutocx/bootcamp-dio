def exibir_mensagem():
    print('Olá mundo!')
    print()

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    print()

# Após a definição da função é necessário chama-la para que ela ative.
exibir_mensagem()

# Caso a função peça um ou mais parâmetros eles devem ser inseridos
exibir_mensagem_2("Augusto")