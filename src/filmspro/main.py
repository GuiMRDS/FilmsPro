import asyncio
import os

import dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.websearch import WebSearchTools

from filmspro.models.movies import MovieRecommendation
from prompts import *
dotenv.load_dotenv()

movie_recommendation_agent = Agent(
    name="FilmPro",
    tools=[WebSearchTools(backend="duckduckgo")],
    model=Groq(id="openai/gpt-oss-120b",api_key=os.getenv("GROQ_API_KEY")),
    description=description,
    instructions=instructions,
    markdown=True,
    add_datetime_to_context=True,
    output_schema=MovieRecommendation,
    debug_mode=True,
    debug_level=1,
)

async def recommendations():
    result = await movie_recommendation_agent.arun(
        "Estou procurando filmes similares ao Tropa de Elite. "
        "Gosto de Filmes de ação, policial, drama realista com narrativa intensa e abordagem crua.",
        stream=False,
    )

    if result and result.content:
        data: MovieRecommendation = result.content
        pretty_json_output = data.model_dump_json(indent=2)
        print(pretty_json_output)

    return result

if __name__ == "__main__":
    asyncio.run(recommendations())

