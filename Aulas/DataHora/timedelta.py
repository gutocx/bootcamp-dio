from datetime import datetime, timedelta

tipo_carro = 'P' # P, M, G
tempo_pequeno = 300
tempo_medio = 450
tempo_grande = 600
data_atual = datetime.now()

if tipo_carro =='P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O Carro chegou: {data_atual} e ficará pronto: {data_estimada}")
elif tipo_carro =='M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O Carro chegou: {data_atual} e ficará pronto: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O Carro chegou: {data_atual} e ficará pronto: {data_estimada}")