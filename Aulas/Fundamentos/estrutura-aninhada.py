# Definindo as variáveis
conta_normal = False
conta_universitaria = False
saldo = 800
cheque_especial = 200

# Input para verificação do tipo de conta de usuário
tipo_de_conta = str(input("Qual é seu tipo de conta? "))

# Condicional de conta
if tipo_de_conta == "normal":
    conta_normal = True
elif tipo_de_conta == "universitaria":
    conta_universitaria = True
else:
    print("O sistema não reconheceu o tipo de conta informado. Por favor, tente novamente!")
    exit()

# Input para obtenção do valor de saque desejado
saque = int(input("Qual valor você deseja sacar? ") )

# Método condicional de verificação do saque
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")