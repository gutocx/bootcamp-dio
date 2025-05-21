# Utilizando o break
# while True:
#    numero = int(input("Informe um número: "))

#    if numero == 10:
#        break

#    print(numero)

#for numero in range(100):
#    if numero == 10:
#        break
#    print(numero, end=" ")

# substituindo o break por continue, ele ira pular o que foi informado na condicional

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")