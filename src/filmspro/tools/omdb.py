import os
from typing import Any
import aiohttp
from typer import params


async def search_movie(title:str) -> dict[str, Any] | str:
    api_key = os.getenv("OMDB_API_KEY")
    if not api_key:
        raise Exception("OMDB_API_KEY não configurada")

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                    "https://www.omdbapi.com/",
                    params={
                        "apikey": api_key,
                        "t": title,
                        "type": "movie",
                        "plot":"full",
                        "v":"1"
                    },
                timeout=aiohttp.ClientTimeout(total=10)
            ) as resp:
                if resp.status != 200:
                    raise f"Erro ao buscar filme, Status code: {resp.status}"

                data = await resp.json()

                if data.get("Response") == "False":
                    return f"Filme não encontrado, {title}"

                return data

        except Exception as e:
            return f"Erro na buscar filme, {title}"

