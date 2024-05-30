from crewai import Agent
from dotenv import load_dotenv
from tools import tool
from util import *

load_dotenv()

# Load the LLM
llm = configure_llm()

# Creating a News Researcher agent
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=("Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge"
               "that could change the world."),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a Writer Agent responsible for writing News blog
news_writer = Agent(
    role="Writer",
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=("With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, "
               "bringing new discoveries to light in an accessible manner."),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
