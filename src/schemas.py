from enum import Enum
from pydantic import BaseModel
from typing import List

class TipoTelefone(str, Enum):
    movel = "móvel"
    fixo = "fixo"
    comercial = "comercial"

class Categoria(str, Enum):
    familiar = "familiar"
    pessoal = "pessoal"
    comercial = "comercial"

class Telefone(BaseModel):
    numero: str
    tipo: TipoTelefone

class Contato(BaseModel):
    nome: str
    telefones: List[Telefone]
    categoria: Categoria
