import streamlit as st

from backend.health_engine import predict_heart
from backend.ai_model import create_summary, save_report


def heart_module():

    st.markdown("### ❤️ Heart ANN Analysis")


    age = st.number_input(
        "Age",
        1,
        120,
        25
    )


    cp = st.number_input(
        "Chest Pain Type",
        0,
        3
    )


    bp = st.number_input(
        "Blood Pressure",
        0,
        250
    )


    chol = st.number_input(
        "Cholesterol",
        0,
        600
    )


    if st.button("Run Heart Analysis"):

        result = predict_heart(
            [
                age,
                cp,
                bp,
                chol
            ]
        )


        st.success(f"""
Status : {result["status"]}

Risk Score : {result["score"]}%

{result["message"]}
""")


        summary = create_summary(result)

        save_report(summary)