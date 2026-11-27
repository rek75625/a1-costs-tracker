import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found. Check your .env file.")
    st.stop()

# Initialize ChatGroq
model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    temperature=1,
    max_tokens=2048,
    reasoning_effort="medium"
)

st.title("AI Chatbot")

# Store the exact same LangChain messages list in session_state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

# Display existing chat history (skip SystemMessage so only user & AI show in UI)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input box at the bottom
prompt = st.chat_input("You:")

if prompt and prompt.strip():
    # Append user input as a HumanMessage
    st.session_state.messages.append(HumanMessage(content=prompt.strip()))
    with st.chat_message("user"):
        st.write(prompt.strip())

    try:
        # invoke() using the messages list
        response = model.invoke(st.session_state.messages)

        with st.chat_message("assistant"):
            st.write(response.content)

        # Append AI reply as an AIMessage
        st.session_state.messages.append(AIMessage(content=response.content))

    except Exception as e:
        st.error(f"API Error: {e}")
        st.session_state.messages.pop()
