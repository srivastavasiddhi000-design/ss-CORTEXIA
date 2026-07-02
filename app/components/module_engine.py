import streamlit as st

from backend.health_engine import analyze

from backend.database import (
    save_report,
    save_record,
    save_risk,
    update_dossier
)

from app.components.ui import apply_theme




def disease_page(title, icon, fields):


    apply_theme(
        f"{icon} {title}"
    )



    st.markdown(
    f"""
    <h1 style="
    text-align:center;
    color:#00eaff;
    letter-spacing:3px;
    ">
    {icon} {title}
    </h1>
    """,
    unsafe_allow_html=True
    )



    data = {}



    for field in fields:


        data[field] = st.number_input(

            field,

            min_value=0,

            max_value=500,

            value=0

        )




    if st.button(
        "RUN NEURAL ANALYSIS"
    ):



        result = analyze(data)



        score = result["score"]

        risk = result["risk"]




        st.markdown(
        f"""
        <div style="
        text-align:center;
        margin-top:30px;
        ">


        <h2>
        CORTEXIA RESULT
        </h2>


        <h1 style="
        color:#00eaff;
        font-size:60px;
        ">

        {score}%

        </h1>


        <h3>
        RISK : {risk}
        </h3>


        </div>
        """,
        unsafe_allow_html=True
        )





        # DATABASE

        save_report(

            title,

            risk,

            score,

            str(data)

        )



        save_record(

            title,

            risk,

            score

        )



        save_risk(

            title,

            risk,

            score

        )






        # =====================
        # DOSSIER UPDATE
        # =====================


        safe = max(score,0)



        if "HEART" in title.upper():


            update_dossier(
                safe,
                safe-5,
                safe-10
            )



        elif "DIABETES" in title.upper():


            update_dossier(
                safe-10,
                safe,
                safe-5
            )



        elif "LUNG" in title.upper():


            update_dossier(
                safe-5,
                safe-10,
                safe
            )



        elif "KIDNEY" in title.upper():


            update_dossier(
                safe-5,
                safe-5,
                safe
            )



        elif "CANCER" in title.upper():


            update_dossier(
                safe-15,
                safe-10,
                safe-5
            )



        elif "CYCLE" in title.upper():


            update_dossier(
                safe-5,
                safe,
                safe-5
            )



        else:


            update_dossier(
                safe,
                safe,
                safe
            )




        st.success(
            "CORTEXIA DATABASE SYNCHRONIZED"
        )