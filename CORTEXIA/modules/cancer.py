import streamlit as st

from backend.health_engine import predict_cancer
from backend.ai_model import create_summary, save_report


def cancer_module():

    st.markdown("### 🎗 Cancer ANN Analysis")


    age = st.number_input(
        "Age",
        1,
        120,
        25
    )


    tumor = st.number_input(
        "Tumor Size (cm)",
        0.0,
        20.0,
        1.0,
        step=0.1
    )


    smoking = st.slider(
        "Smoking Level (0-10)",
        0,
        10
    )


    weight = st.number_input(
        "Weight Loss (kg)",
        0.0,
        30.0,
        0.0,
        step=0.5
    )


    if st.button("Run Cancer Analysis"):


        result = predict_cancer(
            [
                age,
                tumor,
                smoking,
                weight
            ]
        )


        st.success(f"""
Status : {result["status"]}

Risk Score : {result["score"]}%

{result["message"]}
""")


        summary = create_summary(result)

        save_report(summary)