contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "91111-1111"},
    "augusto@gmail.com": {"nome": "Augusto", "telefone": "92222-2222"},
    "luiz@gmail.com": {"nome": "Luiz", "telefone": "93333-3333"},
    "camila@gmail.com": {"nome": "Camila", "telefone": "94444-4444"},
    "juliana@gmail.com": {"nome": "Juliana", "telefone": "95555-5555"},
    "marcos@gmail.com": {"nome": "Marcos", "telefone": "96666-6666", "extra":{"a": 1}},
}

# for chave in contatos:
#     print()
#     print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)