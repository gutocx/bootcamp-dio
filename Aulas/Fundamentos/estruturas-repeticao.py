# Estrutura de repetição: For
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")

# Estrutura de repetição: Range
# exibindo em sequencia de 0 -> 10
print()
for numero in range(0, 11):
    print(numero, end=" ")

# exibindo a tabuada do 5 (ultimo parametro)
print()
for numero in range(0, 51, 5):
    print(numero, end=" ")
