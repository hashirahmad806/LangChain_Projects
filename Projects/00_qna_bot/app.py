import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model="openai/gpt-oss-20b")

if "messages" not in st.session_state:
    st.session_state.messages = []

# ui
st.subheader("🤖 Qna Bot")
# session state is used to store the messages between the user and the model
# we can use this to show the previous messages in the chat window
# we use this because streamlit reruns the script every time the user interacts with the app, so we need to store the messages in the session state to persist them across reruns.
# history [] is not working Because it will be reinitialized every time the script is rerun, so we need to use session state to store the messages.
for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))


query = st.chat_input("Ask anything ....")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    # here We can show the user query in the chat window before getting the response from the model
    st.chat_message("user").markdown(query)

    res = llm.invoke(st.session_state.messages)
    st.session_state.messages.append({"role": "ai", "content": res.content})

    # here We can show the model response in the chat window after getting the response from the model
    st.chat_message("ai").markdown(res.content)


print(st.session_state.messages)


# without streamlit means Using command line interface

# history = []

# while True:
#     query = input("Ask anything ....")
#     if query:
#         history.append({"role": "user", "content": query})
#         res = llm.invoke(history)
#         history.append({"role": "ai", "content": res.content})
#         print(res.content)
