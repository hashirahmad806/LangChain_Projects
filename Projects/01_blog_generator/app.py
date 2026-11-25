from pathlib import Path
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# Loads .env located in the exact same directory as this script
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)


# look it the image in the assets folder and   ist our project  Overview and the project name and the project description and the project goal and the project objective and the project scope and the project deliverables and the project milestones and the project timeline and the project budget and the project risks and the project assumptions and the project constraints and the project stakeholders and the project team members and the project communication plan and the project change management plan and the project quality management plan and the project procurement management plan and the project human resource management plan and the project integration management plan

# in the image show three  main chains one Outline chain  , 2 is Draft  Chain and 3 is polish chain  and them Final Post

# for cahin  we needs prompt template and output parser and the tool and the agent and the chat model
# so for ever chain we need  to define the seperate prompt

# Prompt | LLM |String Parser

# for ever chain we need  a llm object is need so we can define the llm object for every chain and we can use the same llm object for all the chains or we can define different llm object for every chain
MODEL = "openai/gpt-oss-20b"

llm = ChatGroq(model=MODEL)


HUMAN_STYLE = """Write like a person, not like an AI:
- Vary your sentence length. Some short. Others longer, with a clause that earns its place.
- Use contractions (it's, don't, you'll) and talk straight to the reader as "you".
- Replace vague claims with a concrete example, a number, or a small story.
- Having an opinion is fine. Saying "I" is fine.
- Never use these words and phrases: "in today's fast-paced world", "delve", "moreover",
  "furthermore", "unlock", "leverage", "robust", "seamless", "game-changer",
  "it's worth noting", "navigate the landscape", "at the end of the day".
- Do not start every section the same way.
- Only use a bullet list when the content really is a list. Prefer paragraphs.
- Do not end with a summary of what you just said. End with one useful thought."""


# Here we define the prompt templates for each of the three chains: Outline, Draft, and Polish. Each prompt template specifies the instructions for generating the respective outputs.

# In the Outline prompt, we ask the model to create a short outline for a blog post based on a given topic and tone. The output includes an opening line, section headings, and key points.

OUTLINE_PROMPT = ChatPromptTemplate.from_template(
    "Write a short outline for a blog post.\n\n"
    "Topic: {topic}\n"
    "Tone: {tone}\n\n"
    "Give me:\n"
    "- one opening line that makes the reader curious\n"
    "- 4 section headings\n"
    "- 5 key points the post must cover\n\n"
    "Just the outline. Do not write the post."
)


# In the Draft prompt, we instruct the model to write a full blog post based on the provided outline.Human style  must be include    The output should be in markdown format, with section headings marked as ###.

DRAFT_PROMPT = ChatPromptTemplate.from_template(
    "Write a blog post from this outline.\n\n"
    "{outline}\n\n"
    + HUMAN_STYLE
    + "\n\n"
    "Tone: {tone}\n"
    "Output markdown, with the section headings as ###.\n"
    "Make it as long or as short as the topic actually needs."
)


# In the Polish prompt, we ask the model to improve an existing blog post without changing its meaning. We also request that the model adds a suitable title at the top and maintains the markdown formatting.

POLISH_PROMPT = ChatPromptTemplate.from_template(
    "Improve this blog post without changing what it says.\n\n"
    + HUMAN_STYLE
    + "\n\n"
    "Also:\n"
    "- add a good # title at the top\n"
    "- keep the markdown\n\n"
    "Reply with the improved post only, no commentary.\n\n"
    "{draft}"
)


outline_chain = OUTLINE_PROMPT | llm | StrOutputParser()
draft_chain = DRAFT_PROMPT | llm | StrOutputParser()
final_chain = POLISH_PROMPT | llm | StrOutputParser()


# now here we cannect all the chains together to create a complete blog post generation workflow. The user will provide a topic and tone, and the system will generate an outline, draft the blog post, and then polish it for final output.

# but Here we want  give user alert when on chain  is completed and the next chain is starting so we can use streamlit to show the alert to the user when one chain is completed and the next chain is starting


# using streamlit we can create a simple web interface for the blog post generator. The user will input the topic and tone, and the system will display the generated outline, draft, and final polished post in sequence, with alerts indicating the progress of each chain.

# UI  DESIGN

st.title(" Ai Blog Post Generator")
