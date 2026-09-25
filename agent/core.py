import asyncio

import dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.websearch import WebSearchTools

from agent.config import Config
from agent.models.movies import MovieRecommendation
from agent.prompts import description, instructions
from agent.tools.omdb import search_movie

dotenv.load_dotenv()
Config.validade()

research_agent = Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=Config.GROQ_API_KEY,
    ),
    tools=[
        WebSearchTools(backend="duckduckgo"),
        search_movie
    ]
)

parser_agent = Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=Config.GROQ_API_KEY,
    ),
    output_schema=MovieRecommendation,
)

movie_recommendation_agent = Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=Config.GROQ_API_KEY,
    ),
    tools=[WebSearchTools(backend="duckduckgo"), search_movie],
    parser_model=Groq(
        id="openai/gpt-oss-120b",
        api_key=Config.GROQ_API_KEY,
    ),
    description=description,
    instructions=instructions,
    markdown=True,
    add_datetime_to_context=True,
    output_schema=MovieRecommendation,
    debug_mode=True,
    debug_level=1,
)

async def recommendations(preferences):
    result = await movie_recommendation_agent.arun(
        preferences,
        stream=False,
    )

    if result and result.content:
        data: MovieRecommendation = result.content
        pretty_json_output = data.model_dump_json(indent=2)
        print(pretty_json_output)
        return data

    return None

if __name__ == "__main__":
    asyncio.run(recommendations())