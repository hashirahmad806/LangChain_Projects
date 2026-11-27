from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools_modern import ALL_TOOLS
#  checkpoint AND  InMemorySaver we used  this Because  it helps us
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os
load_dotenv()

MODEL = os.getenv("MODEL")


def get_agent():
    "Get Agent with google search  and weather  search abilities"
    return create_agent(
        model=ChatGroq(model=MODEL),
        tools=ALL_TOOLS,
        system_prompt=(
            "You are a research assistant with google Search and weather  tools.\n"
            "Use 'google_search' for quick searches and 'weather_search' for real-time weather information.\n"
            "for deep research that may take several minutes."
            "if user is looking for weather  details like temperature, humidity, wind speed, and more for a specific city, use 'weather_search' tool.\n"
            "then call  the  'weather_search' tool with the city name as input to get the real time weather information.\n"

        ),
        checkpointer=InMemorySaver()
    )


# let Run local if  it  works then we can connect it to the  web app  and  then we can deploy it on the cloud.

# agent = get_agent()

# while True:
#     query = input("Enter your query (or type 'exit' to quit): ")
#     if query.lower() == 'exit':
#         break
#     res = agent.invoke({"messages": [{"role": "user", "content": query}]})
#     answer = res["messages"][-1].content
#     print("Agent's response:", answer)
