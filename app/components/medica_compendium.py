import streamlit as st
import sys
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "NEXORA-Multi-AI-Agent"
    )
)


from nexora_agents import medical_specialist_agent
from app.components.medica_data import MEDICA_MODULES



def show_medica_compendium():


    st.markdown(
        """
        <style>

        .medica-header{
            background:#111827;
            padding:30px;
            border-radius:20px;
            text-align:center;
            border:1px solid rgba(255,255,255,.08);
            margin-bottom:30px;
        }

        .medica-title{
            font-size:34px;
            font-weight:800;
            color:#F8FAFC;
        }

        .medica-subtitle{
            color:#B8C5D3;
            margin-top:10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="medica-header">

        <div class="medica-title">
        NEXORA Medica Compendium
        </div>

        <div class="medica-subtitle">
        AI-powered guidance across specialised medical disciplines.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )



    cols = st.columns(4)


    for col, module in zip(cols, MEDICA_MODULES):

        with col:

            st.markdown(
                f"""
                ### {module["icon"]}

                **{module["title"]}**

                {module["subtitle"]}
                """
            )


            if st.button(
                "Explore",
                key=f"explore_{module['agent']}"
            ):

                st.session_state["selected_medica"] = module



    if "selected_medica" in st.session_state:


        module = st.session_state["selected_medica"]


        st.divider()


        st.subheader(module["title"])

        st.caption(module["subtitle"])



        question = st.text_area(
            "Medical Inquiry",
            placeholder=f"Ask anything related to {module['title']}...",
            key="medica_question"
        )



        if st.button(
            "Consult NEXORA",
            key=f"consult_{module['agent']}"
        ):


            if question.strip():


                with st.spinner(
                    "Consulting NEXORA AI..."
                ):

                    try:

                        response = medical_specialist_agent(
                            module["agent"],
                            question
                        )


                        st.success(
                            "Analysis Completed"
                        )


                        st.markdown(
                            "### NEXORA AI Response"
                        )


                        st.write(response)


                    except Exception as e:

                        st.error(
                            f"NEXORA Error: {e}"
                        )


            else:

                st.warning(
                    "Please enter your medical question."
                )