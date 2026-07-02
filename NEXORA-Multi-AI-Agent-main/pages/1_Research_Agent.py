import streamlit as st
from nexora_agents import research_agent


st.set_page_config(
    page_title="NEXORA Research",
    page_icon="🔎",
    layout="wide"
)


st.title("🔎 NEXORA Research Agent")

st.markdown(
"""
### Research Intelligence Module

Ask anything and get:
- Detailed analysis
- Latest insights
- Key findings
- Future scope
"""
)


# chat history
if "research_chat" not in st.session_state:
    st.session_state.research_chat = []


for chat in st.session_state.research_chat:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])



query = st.chat_input(
    "Ask your research question..."
)


if query:

    st.session_state.research_chat.append(
        {
            "role":"user",
            "content":query
        }
    )


    with st.chat_message("user"):
        st.markdown(query)


    with st.chat_message("assistant"):

        with st.spinner("Researching..."):

            response = research_agent(query)

        st.markdown(response)


        st.session_state.research_chat.append(
            {
                "role":"assistant",
                "content":response
            }
        )
