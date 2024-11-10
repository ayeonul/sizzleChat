import streamlit as st

from GPTAssistant import GPTAssistant
from GPT import ChatGPT
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

concept = "You are 'Sizzle(시즐)', a chatbot that provides guidance on cooking and ingredients. "

assistant = ChatGPT(
    api_key=OPENAI_KEY,
    model_name="gpt-4o-mini",
    concept=concept,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 저는 시즐이에요. 식재료나 음식 레시피에 관해서 뭐든 답해드릴게요.",
        }
    ]


user_input = st.chat_input("무엇이든 물어보세요!")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    result = assistant.chat(st.session_state.messages)
    res = res = result["res"][0]["res"]
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": res,
        }
    )

for msg in st.session_state.messages:
    message_view = st.chat_message(msg["role"])
    message_view.write(msg["content"])
