from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

print("Q&A Bot initialized! Type 'exit' to quit.\n")

while True:
    query = input("User : ")
    if query.strip().lower() == "exit":
        break
    if not query.strip():
        continue

    res = llm.invoke(query)
    print(f"Bot  : {res.content}\n")
