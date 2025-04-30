def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []
    for transacao in transacoes:
        if abs(transacao) > limite:
            transacoes_filtradas.append(transacao)
    return transacoes_filtradas

entrada = input().strip()

if "]," in entrada:
    entrada_transacoes, limite = entrada.split("],", 1)
else:
    entrada_transacoes = entrada
    limite = "0"

entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
transacoes = [int(valor) for valor in entrada_transacoes.split(",") if valor]

limite = float(limite.strip())

resultado = filtrar_transacoes(transacoes, limite)
print(f"Transações: {resultado}")