import os
import dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.websearch import WebSearchTools

from prompts import *
dotenv.load_dotenv()


movie_recommendation_agent = Agent(
    name="FilmPro",
    tools=[WebSearchTools(backend="duckduckgo")],
    model=Groq(id="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY")),
    description=description,
    instructions=instructions,
    markdown=True,
    add_datetime_to_context=True,
)

if __name__ == "__main__":
    movie_recommendation_agent.print_response(
        input="Estou procurando filmes similares ao Independence Day. "
              "Gosto de filmes de ficção científica com ação, invasão alienígena e espetáculos visuais impressionantes.",
        stream=True,
    )


