opcao = -1
# o while é como se fosse um if mas que continua executando enquanto a condição não é atendida
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

# podemos também como no for, utilizar o else no while.
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
