from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


llm =ChatGroq(
    model ="openai/gpt-oss-120b"
)

while True :
    query =input("User : ")
    if query == "exit" :
      break

    res = llm.invoke({"role" :"user" ,"content" :query})