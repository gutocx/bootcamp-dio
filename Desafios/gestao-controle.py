def calcular_saldo(transacoes):
    saldo = sum(transacoes)
    return f"Saldo: R$ {saldo:.2f}"

# Lê a entrada do usuário e remove espaços desnecessários
entrada = input().strip()

# Converte a entrada em uma lista de números
if entrada.startswith('[') and entrada.endswith(']'):
    # Remove os colchetes e divide os elementos
    elementos = entrada[1:-1].split(',')
    # Remove espaços em branco e converte para float
    transacoes = [float(elem.strip()) for elem in elementos]
else:
    # Se não estiver entre colchetes, trata como um único número
    transacoes = [float(entrada)]

# Calcula o saldo e imprime o resultado
resultado = calcular_saldo(transacoes)
print(resultado)