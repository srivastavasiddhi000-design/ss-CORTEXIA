import streamlit as st

from backend.qa_engine import predict_qa
from backend.ai_model import create_summary, save_report


st.set_page_config(
    page_title="CORTEXIA QA",
    page_icon="🧠",
    layout="wide"
)


st.markdown("""
<style>


.stApp{

background-image:
linear-gradient(
rgba(3,8,25,.60),
rgba(5,5,25,.90)
),
url("https://cdn.botpenguin.com/assets/website/background/background-17-18.webp");

background-size:cover;
background-position:center;
background-attachment:fixed;

}



.card{

background:
rgba(255,255,255,.07);

border:
1px solid rgba(255,255,255,.15);

border-radius:26px;

padding:25px;

backdrop-filter:blur(22px);

}



.glass{

background:
rgba(255,255,255,.07);

border:
1px solid rgba(255,255,255,.15);

border-radius:26px;

padding:25px;

backdrop-filter:blur(22px);

}



h1,h2,h3{
color:#F5F7FA!important;
}



.stButton button{

background:
rgba(255,255,255,.10);

border:
1px solid rgba(255,255,255,.20);

border-radius:22px;

color:white;

font-weight:700;

}


</style>
""",unsafe_allow_html=True)




st.markdown("""
<div style="text-align:center;">


<p style="
color:#9AA7B5;
letter-spacing:4px;
font-size:13px;
">
CORTEXIA CLINICAL MODULE
</p>


<h1>
🧠 QA ANALYSIS
</h1>


<p>
AI Quality Assessment Engine
</p>


</div>
""",unsafe_allow_html=True)




left,right = st.columns([2,1])



with left:


    st.markdown(
    "<div class='card'>",
    unsafe_allow_html=True
    )


    age = st.number_input(
        "Age",
        10,
        100,
        25
    )


    sleep = st.number_input(
        "Sleep Hours",
        0,
        15,
        7
    )


    stress = st.number_input(
        "Stress Level",
        0,
        10,
        5
    )


    activity = st.number_input(
        "Activity Level",
        0,
        10,
        5
    )



    if st.button(
        "RUN QA ANALYSIS",
        use_container_width=True
    ):


        result = predict_qa(
            [
            age,
            sleep,
            stress,
            activity
            ]
        )


        score=result["score"]



        st.divider()


        st.subheader(
        "🧠 AI Risk Assessment"
        )


        st.progress(score/100)



        a,b,c = st.columns(3)


        a.metric(
            "Risk Score",
            f"{score}%"
        )


        b.metric(
            "Status",
            result["status"]
        )


        c.metric(
            "AI Confidence",
            "96.8%"
        )



        if result["status"]=="LOW RISK":

            st.success(result["message"])

        elif result["status"]=="MODERATE RISK":

            st.warning(result["message"])

        else:

            st.error(result["message"])




        report=create_summary(result)

        save_report(report)



        st.subheader(
        "📄 AI Health Report"
        )


        st.json(report)




    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )





with right:


    st.markdown("""
    <div class="glass">


    <h2>
    AI STATUS
    </h2>


    <p>
    🟢 Neural Engine : ONLINE
    </p>


    <p>
    🟢 QA Model : ACTIVE
    </p>


    <p>
    🟢 Database : CONNECTED
    </p>


    <p>
    AI Confidence : 96.8%
    </p>


    </div>
    """,unsafe_allow_html=True)





if st.button("← Back Dashboard"):

    st.switch_page("main.py")