import streamlit as st

from backend.health_engine import predict_cycle
from backend.ai_model import create_summary, save_report


def cycle_module():

    st.markdown("### 🌸 Cycle ANN Analysis")


    age = st.number_input(
        "Age",
        10,
        60,
        25
    )


    cycle = st.number_input(
        "Cycle Length (days)",
        10,
        60,
        28
    )


    pain = st.slider(
        "Pain Level (0-10)",
        0,
        10
    )


    flow = st.slider(
        "Flow Level (0-10)",
        0,
        10
    )


    if st.button("Run Cycle Analysis"):


        result = predict_cycle(
            [
                age,
                cycle,
                pain,
                flow
            ]
        )


        st.success(f"""
Status : {result["status"]}

Risk Score : {result["score"]}%

{result["message"]}
""")


        summary = create_summary(result)

        save_report(summary)