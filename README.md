# FilmPro

## Overview
FilmPro é um sistema de recomendação de filmes inteligente que expõe uma API RESTful construída no framework **FastAPI**. A API recebe preferências de filmes (por ex., "comédias românticas e ação") e devolve uma lista curada de títulos em português, com detalhes obtidos na API pública OMDB.

## Tech Stack
- **Python 3.13** – engine de execução.
- **FastAPI** – framework web + documentação OpenAPI automática.
- **uvicorn** – ASGI HTTP server.
- **Agno + Groq** – agente inteligente baseado em *open‑ai/gpt‑oss‑120b*, com prompts e auxílio de web‑search.
- **aiohttp** – cliente HTTP assíncrono para a chamada OMDB.
- **python‑dotenv** – carregador de secrets.

## Project structure
```text
.
├── src/
│   └── filmspro/
│       └── main.py          # runner – uvicorn
├── api/
│   ├── app.py              # FastAPI application
│   └── routers.py           # endpoint definitions
├── agent/
│   ├── core.py             # agno agent definitions
│   ├── config.py           # loads .env
│   ├── models/
│   │   └── movies.py       # Pydantic schemas
│   ├── prompts/
│   │   └── movie_search.py # prompt description
│   └── tools/
│       └── omdb.py         # OMDB search tool
├── requeriments.txt
├── pyproject.toml
├── README.md
└── .env
```

## Endpoints

- `GET /health` – health‑check.
- `GET /` – API information page.
- `POST /recommendations`
  ```json
  {
    "preferences": "comédias românticas e ação"
  }
  ```
  Returns a list of recommendations defined in `agent/models/movies.py`.

## Environment variables

```env
GROQ_API_KEY=<sua chave>
OMDB_API_KEY=<sua chave>
```

## Quick start

```bash
# Install dependencies
pip install -e .

# Run via uvicorn
uvicorn api.app:app --reload

# Or use the console script
filmspro
```

## Interface

![Interface](design/Interface.png)

## Next steps

- Add example Swagger calls to the docs.
- Implement caching for OMDB responses.
- Extend unit test coverage for endpoints and agents.

## Contributing
Feel free to open PRs, clone the repo, etc.