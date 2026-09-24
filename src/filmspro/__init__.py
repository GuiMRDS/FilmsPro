from agno.agent import Agent
from prompts import *



movie_recommentation_agent = Agent(
    name="Film Pro",
    description=description,
    instructions=instructions,
)