import streamlit as st

from backend.health_engine import predict_kidney
from backend.ai_model import create_summary, save_report


def kidney_module():

    st.markdown("### 🧬 Kidney ANN Analysis")


    age = st.number_input(
        "Age",
        1,
        120,
        25
    )


    creatinine = st.number_input(
        "Creatinine",
        0.0,
        10.0,
        1.0,
        step=0.1
    )


    bp = st.number_input(
        "Blood Pressure",
        0,
        250
    )


    sugar = st.number_input(
        "Blood Sugar",
        0,
        400
    )


    if st.button("Run Kidney Analysis"):


        result = predict_kidney(
            [
                age,
                creatinine,
                bp,
                sugar
            ]
        )


        st.success(f"""
Status : {result["status"]}

Risk Score : {result["score"]}%

{result["message"]}
""")


        summary = create_summary(result)

        save_report(summary)