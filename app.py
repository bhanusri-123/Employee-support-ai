import streamlit as st

from graph.graph_builder import chatbot_graph

from utils.data_loader import load_json

from ui.styles import load_css

from ui.sidebar import render_sidebar

from ui.chat import render_chat

from ui.components import response_card


st.set_page_config(
    page_title="Employee Support AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

employee = load_json("employees.json")[0]

render_sidebar(employee)

st.markdown(
    '<p class="title">Employee Support AI</p>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# Initialize chat history with welcome message
# -------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content":
"""👋 Welcome to Employee Support AI!

I can assist you with:

• Password Reset \n
• Account Unlock \n
• Leave Management \n
• Employee Profile \n
• Support Tickets \n
• Company Policies \n

How can I help you today?"""
        }

    ]

render_chat()

query = st.chat_input(
    "Ask about leave, tickets, policies, passwords or your profile..."
)
if query:

    st.session_state.messages.append(

        {
            "role": "user",
            "content": query
        }

    )

    state = {

        "query": query,

        "intent_result": {},

        "tool_result": [],

        "response": "",

        "method": "",

        "intent": "",

        "confidence": 0,

        "response_time": 0

    }

    result = chatbot_graph.invoke(state)

    if result["intent"] == "policy_query":

        result["method"] = "rag"

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": response_card(result)

        }

    )

    st.rerun()