# src/routers/agenda_router.py
from fastapi import APIRouter, Depends, HTTPException
from src.schemas import Contato
from src.storage import salvar_contato, buscar_contato, listar_contatos, excluir_contato
from src.redis_funcs import dependency_redis

router = APIRouter(prefix="/agenda", tags=["Agenda"])

@router.post("/")
async def criar(contato: Contato, redis = Depends(dependency_redis)):
    await salvar_contato(redis, contato.dict())
    return contato

@router.delete("/{nome}", summary="Excluir contato pelo nome")
async def excluir_contato_endpoint(nome: str, redis=Depends(dependency_redis)):
    deletado = await excluir_contato(redis, nome)
    if not deletado:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return {"mensagem": f"Contato '{nome}' excluído com sucesso."}

@router.get("/{nome}")
async def buscar(nome: str, redis = Depends(dependency_redis)):
    contato = await buscar_contato(redis, nome)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contato

@router.get("/")
async def listar(redis = Depends(dependency_redis)):
    return await listar_contatos(redis)
