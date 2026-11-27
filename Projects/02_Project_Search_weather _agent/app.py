from agent import get_agent
import streamlit as st

agent = get_agent()

st.subheader("Google  Search Agent")
st.caption("This agent can search anything on the Google for realtime information and also get Real  time weather  details like temperature, humidity, wind speed, and more for a specific city.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))

query = st.chat_input("Ask me anything about weather or search anything on Google...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    res = agent.invoke({"messages": [{"role": "user", "content": query}]},
                       {"config"})
    ans = res["messages"][-1].content

    st.session_state.messages.append({"role": "ai", "content": ans})
    st.chat_message("ai").markdown(ans)
