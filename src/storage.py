# contacts_storage.py
import json

def contato_key(nome: str) -> str:
    return f"contato:{nome}"

async def salvar_contato(redis, contato: dict):
    await redis.set(contato_key(contato["nome"]), json.dumps(contato))
    await redis.sadd("contatos", contato_key(contato["nome"]))

async def excluir_contato(redis, nome: str):
    key = f"contato:{nome}"
    result = await redis.delete(key)
    return result > 0

async def buscar_contato(redis, nome: str):
    data = await redis.get(contato_key(nome))
    return json.loads(data) if data else None

async def listar_contatos(redis):
    keys = await redis.smembers("contatos")
    contatos = []
    for k in keys:
        raw = await redis.get(k)
        if raw:
            contatos.append(json.loads(raw))
    return contatos
