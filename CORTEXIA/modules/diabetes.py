import streamlit as st

from backend.health_engine import predict_diabetes
from backend.ai_model import create_summary, save_report


def diabetes_module():

    st.markdown("### 🩸 Diabetes ANN Analysis")


    age = st.number_input(
        "Age",
        1,
        120,
        25
    )


    glucose = st.number_input(
        "Glucose",
        0,
        400
    )


    bp = st.number_input(
        "Blood Pressure",
        0,
        250
    )


    bmi = st.number_input(
        "BMI",
        0.0,
        60.0,
        step=0.1
    )


    if st.button("Run Diabetes Analysis"):


        result = predict_diabetes(
            [
                age,
                glucose,
                bp,
                bmi
            ]
        )


        st.success(f"""
Status : {result["status"]}

Risk Score : {result["score"]}%

{result["message"]}
""")


        summary = create_summary(result)

        save_report(summary)