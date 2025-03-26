nome = "Augusto Cardoso Xavier"
nome2 = "Camila Bartelli de Souza"

print(nome[0])
print(nome[:7]) #sem start (para no caracter definido).
print(nome[8:]) #só com o start (começa a partir da posição definida).
print(nome[8:15]) #define o inicio e o fim do corte.
print(nome[8:15:2]) #o terceiro valor (step) define de quanto em quanto.
print(nome[:]) #sem definição de inicio e fim, ou seja, completo.
print(nome[:: -1]) #criar espelhamento. (não passa o inicio e o fim, somente o step negativo)
print()
print(nome2[:: -1])