# FilmPro – Contextualização

## Visão geral
FilmPro é um sistema de recomendação inteligente de filmes. Ele expõe uma API RESTful via **FastAPI** que recebe as preferências do usuário e devolve uma lista de filmes curados em português.

## Stack tecnológico
- **Python 3.13** – linguagem de implementação.
- **FastAPI** – framework web e geração automática de documentação OpenAPI.
- **uvicorn** – ASGI server.
- **Agno + Groq** – agente inteligente usando o modelo *open‑ai/gpt-oss-120b* com prompts e ferramentas de web‑search.
- **aiohttp** – cliente HTTP assíncrono para chamar a API OMDB.
- **python‑dotenv** – carregamento dos secrets.

## Estrutura de código
```
.
├── src/
│   └── filmspro/
│       └── main.py          # runner – uvicorn
├── api/
│   ├── app.py              # FastAPI app
│   └── routers.py           # endpoints
├── agent/
│   ├── core.py              # agno agent definitions
│   ├── config.py            # Config carrega .env
│   ├── models/
│   │   └── movies.py          # Pydantic models
│   ├── prompts/
│   │   └── movie_search.py   # Descrição do agente
│   └── tools/
│       └── omdb.py           # Busca no OMDB
├── requeriments.txt
├── pyproject.toml
├── README.md
└── .env
```

## Endpoints principais

* **GET /health** – Verifica se a API está ativa.
* **GET /** – Informação geral da API.
* **POST /recommendations** – Recebe JSON:

```json
{"preferences": "comédias românticas e ação"}
```
O retorno contém uma lista de recomendações conforme definido em `agent/models/movies.py`.

## Variáveis de ambiente
```
GROQ_API_KEY=<sua chave>
OMDB_API_KEY=<sua chave>
```

## Como executar
```bash
# Instalar dependências
pip install -e .

# Rodar via uvicorn
uvicorn api.app:app --reload

# Ou usar o script de console
filmspro
```

## Próximos passos
- Adicionar exemplos de chamadas na documentação Swagger.
- Implementar cache de resultados para evitar chamadas repetidas ao OMDB.
- Expandir suíte de testes unitários para endpoints e agentes.
