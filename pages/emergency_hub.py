import streamlit as st
import sqlite3
from math import radians, sin, cos, sqrt, atan2


st.set_page_config(
    page_title="Emergency Response Hub",
    page_icon="🚨",
    layout="wide"
)



# ==========================
# DATABASE
# ==========================

conn = sqlite3.connect(
    "cortexia.db",
    check_same_thread=False
)

cursor = conn.cursor()



# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.stApp{

background-image:

linear-gradient(
rgba(3,8,25,.65),
rgba(5,5,25,.9)
),

url("https://cdn.botpenguin.com/assets/website/background/background-17-18.webp");

background-size:cover;
background-attachment:fixed;

}


.title{

text-align:center;
font-size:45px;
font-weight:900;
letter-spacing:5px;
color:#ff4b4b;

}


.card{

background:rgba(255,255,255,.05);
border:1px solid rgba(255,75,75,.35);
border-radius:20px;
padding:25px;
margin:15px;

}


.stButton button{

background:#ff4b4b!important;
color:white!important;
border-radius:14px!important;

}

</style>
""",
unsafe_allow_html=True)




# ==========================
# HEADER
# ==========================

st.markdown("""
<h1 class="title">
🚨 EMERGENCY RESPONSE HUB
</h1>

<p style="
text-align:center;
color:#B8C5D3;
">
CORTEXIA Rapid Medical Assistance System
</p>

""",
unsafe_allow_html=True)





# ==========================
# INPUT
# ==========================


st.markdown(
"<div class='card'>",
unsafe_allow_html=True
)


blood = st.selectbox(
"Required Blood Group",
[
"A+","A-",
"B+","B-",
"AB+","AB-",
"O+","O-"
]
)



location = st.text_input(
"Patient Location"
)



urgency = st.selectbox(
"Emergency Level",
[
"Normal",
"Urgent",
"Critical"
]
)



if st.button(
"🚨 Activate Emergency Search"
):


    st.error(
    "Emergency mode activated"
    )


    st.markdown(
    "### 🔎 Searching CORTEXIA Network..."
    )



    # BLOOD SEARCH

    donors = cursor.execute(
    """
    SELECT name,location,phone
    FROM donors
    WHERE blood=?
    AND available='Available'
    """,
    (blood,)
    ).fetchall()



    if donors:


        st.success(
        f"{len(donors)} donor(s) found"
        )


        for d in donors:


            st.markdown(
            f"""
            <div class="card">

            🩸 <b>{d[0]}</b>

            <br>

            📍 {d[1]}

            <br>

            📞 {d[2]}

            </div>
            """,
            unsafe_allow_html=True
            )


    else:


        st.warning(
        "No matching donor found"
        )





    # HEALTH CENTRE SEARCH


    centres = cursor.execute(
    """
    SELECT name,type,location,contact,status
    FROM health_centres
    """
    ).fetchall()



    if centres:


        st.info(
        f"{len(centres)} health centre(s) available"
        )


        for c in centres:


            st.markdown(
            f"""
            <div class="card">

            🏥 <b>{c[0]}</b>

            <br>

            🩺 {c[1]}

            <br>

            📍 {c[2]}

            <br>

            ⚡ {c[4]}

            </div>

            """,
            unsafe_allow_html=True
            )



st.markdown(
"</div>",
unsafe_allow_html=True
)