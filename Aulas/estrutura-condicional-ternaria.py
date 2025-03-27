saldo = 2000
saque = int(input("Qual seria o valor do saque? "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")