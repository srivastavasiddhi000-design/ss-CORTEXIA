import streamlit as st

from backend.health_engine import predict_lung
from backend.ai_model import create_summary, save_report


def lung_module():

    st.markdown("### 🫁 Lung ANN Analysis")


    age = st.number_input(
        "Age",
        1,
        120,
        25
    )


    smoking = st.slider(
        "Smoking Level (0-10)",
        0,
        10
    )


    oxygen = st.number_input(
        "Oxygen Saturation (%)",
        50,
        100,
        98
    )


    cough = st.slider(
        "Cough Severity (0-10)",
        0,
        10
    )


    if st.button("Run Lung Analysis"):


        result = predict_lung(
            [
                age,
                smoking,
                oxygen,
                cough
            ]
        )


        st.success(f"""
Status : {result["status"]}

Risk Score : {result["score"]}%

{result["message"]}
""")


        summary = create_summary(result)

        save_report(summary)