import requests

BASE_URL = "http://localhost:8088/agenda"

def adicionar_contato(nome, numero, tipo, categoria):
    payload = {
        "nome": nome,
        "telefones": [{"numero": numero, "tipo": tipo}],
        "categoria": categoria
    }
    response = requests.post(BASE_URL + "/", json=payload)
    print("-----------------------")
    print("Adicionando Contatos:")
    print("-----------------------")
    print(f"Adicionado: {response.json()}")
    print("-----------------------")

def listar_contatos():
    response = requests.get(BASE_URL + "/")
    print("-----------------------")
    print("Listando Contatos:")
    print("-----------------------")
    print(f"Lista de contatos: {response.json()}")
    print("-----------------------")

def buscar_contato(nome):
    response = requests.get(f"{BASE_URL}/{nome}")
    print("-----------------------")
    print("Buscando Contato:")
    print("-----------------------")
    if response.status_code == 200:
        print(f"Contato encontrado: {response.json()}")
        print("-----------------------")
    else:
        print(f"Erro: {response.status_code} - {response.json()['detail']}")
        print("-----------------------")

def deletar_contato(nome):
    response = requests.delete(f"{BASE_URL}/{nome}")
    print("-----------------------")
    print("Deletando Contato:")
    if response.status_code == 200:
        print(response.json())
        print("-----------------------")
    else:
        print(f"Erro ao deletar: {response.status_code} - {response.json()['detail']}")
        print("-----------------------")

if __name__ == "__main__":
    contatos = [
        ("lorenzo", "1234-5678", "móvel", "familiar"),
        ("maria", "9876-5432", "fixo", "comercial"),
        ("pedro", "9999-8888", "móvel", "pessoal"),
        ("lucas", "9999-1234", "móvel", "pessoal"),
    ]

    listar_contatos()

    for nome, numero, tipo, categoria in contatos:
        adicionar_contato(nome, numero, tipo, categoria)

    listar_contatos()

    buscar_contato("lorenzo")

    deletar_contato("lorenzo")

    listar_contatos()
