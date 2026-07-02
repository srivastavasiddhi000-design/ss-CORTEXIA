import streamlit as st
import sys
import os


ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)


NEXORA_PATH = os.path.join(
    ROOT,
    "NEXORA-Multi-AI-Agent"
)


if NEXORA_PATH not in sys.path:
    sys.path.insert(0, NEXORA_PATH)



from nexora import (
    research_agent,
    knowledge_agent,
    planner_agent,
    code_agent
)



class NexoraAgent:

    def run(self, query):

        q = query.lower()

        if "research" in q:
            return research_agent(query)

        elif "plan" in q:
            return planner_agent(query)

        elif "code" in q:
            return code_agent(query)

        else:
            return knowledge_agent(query)



def show_nexora():


    if "nexora_agent" not in st.session_state:

        st.session_state.nexora_agent = NexoraAgent()



    st.markdown(
    """
    <style>

    .nexora-title{
        color:rgba(255,255,255,.85);
        letter-spacing:4px;
        font-size:38px;
        font-weight:800;
    }

    .nexora-sub{
        color:#B8C5D3;
    }

    </style>
    """,
    unsafe_allow_html=True
    )



    col1, col2 = st.columns([1,5])


    with col1:

        st.markdown("🤖")



    with col2:

        st.markdown(
        """
        <div class="nexora-title">
        NEXORA AI ClinIQ
        </div>

        <div class="nexora-sub">
        Intelligent Health Assistant
        </div>
        """,
        unsafe_allow_html=True
        )



    question = st.text_input(
        "",
        placeholder="Ask your health question...",
        key="nexora_input"
    )



    if st.button(
        "ASK NEXORA",
        key="nexora_btn"
    ):


        if question:


            with st.spinner(
                "NEXORA AI THINKING..."
            ):


                response = (
                    st.session_state
                    .nexora_agent
                    .run(question)
                )


            st.success(response)



        else:

            st.warning(
                "Enter your question"
            )