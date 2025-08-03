# Trabalho final da disciplina ECD14 - Arquitetura de Microsserviços
> Desenvolvido por Lorenzo Moreira Donatti
> lorenzodonatti@hotmail.com

Disponivel em: 

# API de Agenda de Contatos

Uma API REST desenvolvida com **FastAPI** para gerenciar uma agenda de contatos. Permite criar, listar, buscar e remover contatos com múltiplos números de telefone, classificados por categorias.

## Funcionalidades

- ✅ Criar novo contato
- 📄 Listar todos os contatos
- 🔍 Buscar contato por nome
- ❌ Deletar contato por nome

---

## 📦 Tecnologias

- Python 3.10+
- FastAPI
- Redis
- Uvicorn
- Docker Compose

---

## ⚙️ Executando com Docker Compose

```bash
docker compose up --build
```

Acesse a documentação automática em:
http://localhost:8000/docs

# Testando a API
Você pode usar ferramentas como curl, Postman ou executar o script abaixo:

```bash
python test_api.py
```

# Exemplo de JSON para criação
```json
{
  "nome": "joao",
  "telefones": [
    {
      "numero": "1234-5678",
      "tipo": "móvel"
    }
  ],
  "categoria": "familiar"
}
```
# Endpoints
| Método | Rota           | Descrição                 |
|--------|----------------|---------------------------|
| POST   | /agenda/       | Adiciona um novo contato  |
| GET    | /agenda/       | Lista todos os contatos   |
| GET    | /agenda/{nome} | Busca contato por nome    |
| DELETE | /agenda/{nome} | Remove contato por nome   |


# Estrutura do diretório
```css
.
├── Dockerfile
├── requirements.txt
├── src/
│   └── main.py
├── teste_agenda.py
└── README.md
```