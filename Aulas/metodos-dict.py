contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "91111-1111"},
    "augusto@gmail.com": {"nome": "Augusto", "telefone": "92222-2222"},
    "luiz@gmail.com": {"nome": "Luiz", "telefone": "93333-3333"},
    "camila@gmail.com": {"nome": "Camila", "telefone": "94444-4444"},
    "juliana@gmail.com": {"nome": "Juliana", "telefone": "95555-5555"},
    "marcos@gmail.com": {"nome": "Marcos", "telefone": "96666-6666", "extra":{"a": 1}},
}

#.clear
contatos.clear()

#.copy
copia = contatos.copy()

#.fromkeys
contatos.fromkeys(["nome", "telefone"])
contatos.fromkeys(["nome", "telefone"], "vazio")

#.get
contatos.get("chave")
contatos.get("chave", {})
contatos.get("augusto@gmail.com", {})

#.items
contatos.items()

#.keys
contatos.keys()

#.pop
contatos.pop("camila@gmail.com")
contatos.pop("augusto@gmail.com", {})

#.popitem
contatos.popitem()

#.setdefault
contatos.setdefault("idade", 25)

#.update
contatos.update({"camila@gmail.com": {"nome": "Camis"}})
contatos.update({"marcos@gmail.com": {"nome": "Marcão", "telefone": "92323-5234"}})

#.values
contatos.values()

# in
resultado = "augusto@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["juliana@gmail.com"]
print(resultado)

# del
del contatos["luiz@gmail.com"]["telefone"]
del contatos["guilherme@gmail.com"]