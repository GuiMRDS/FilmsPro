import asyncio
import os

import dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.websearch import WebSearchTools

from filmspro.models.movies import MovieRecommendation
from filmspro.tools.omdb import search_movie
from prompts import *
dotenv.load_dotenv()

research_agent = Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    ),
    tools=[search_movie],
)

parser_agent = Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    ),
    output_schema=MovieRecommendation,
)

movie_recommendation_agent = Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    ),
    tools=[search_movie],
    parser_model=Groq(
        id="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    ),
    markdown=True,
    add_datetime_to_context=True,
    output_schema=MovieRecommendation,
    debug_mode=True,
    debug_level=1,
)

async def recommendations():
    result = await movie_recommendation_agent.arun(
        "Estou procurando filmes similares ao Star Wars. "
        "Gosto de Filmes de ação.",
        stream=False,
    )

    if result and result.content:
        data: MovieRecommendation = result.content
        pretty_json_output = data.model_dump_json(indent=2)
        print(pretty_json_output)

    return result

if __name__ == "__main__":
    asyncio.run(recommendations())