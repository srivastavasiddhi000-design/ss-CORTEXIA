import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.database import create_table, get_dossier
from components.nexora_widget import show_nexora
from components.medica_compendium import show_medica_compendium
from components.medica_data import MEDICA_MODULES
from components.health_radar import show_health_radar
st.write("MAIN FILE LOADED")


st.set_page_config(
    page_title="CORTEXIA",
    page_icon="🧠",
    layout="wide"
)


create_table()



st.markdown("""
<style>

html,body,[data-testid="stAppViewContainer"]{

font-family:"Segoe UI Variable","Segoe UI",sans-serif;
color:#F7FCFF;

}


.stApp{

background-image:
linear-gradient(
rgba(3,8,25,.60),
rgba(5,5,25,.88)
),
url("https://cdn.botpenguin.com/assets/website/background/background-17-18.webp");

background-size:cover;
background-position:center;
background-attachment:fixed;

}


#MainMenu,header,footer{
display:none;
}


.title{

font-size:56px;
font-weight:900;
letter-spacing:8px;
text-align:center;

}


.glass{

background:rgba(255,255,255,.045);

border:
1px solid rgba(255,255,255,.12);

border-radius:18px;

padding:22px;

backdrop-filter:blur(18px);

}


.card{

background:rgba(255,255,255,.045);

border:
1px solid rgba(255,255,255,.12);

border-radius:16px;

padding:12px;

text-align:center;

}


.card:hover{

background:rgba(255,255,255,.07);

}


.stButton button{

width:100%;

background:rgba(255,255,255,.05);

border:
1px solid rgba(255,255,255,.12);

border-radius:12px;

color:white;

}


.stButton button:hover{

border-color:#00eaff;

background:rgba(0,234,255,.08);

}


.module-card{

background:rgba(255,255,255,.045);

border:
1px solid rgba(255,255,255,.12);

border-radius:18px;

padding:18px;

min-height:150px;

}


.module-icon{

font-size:45px;

}


.module-title{

font-size:22px;
font-weight:700;

}


.module-desc{

color:#B8C5D3;

}


</style>

""",unsafe_allow_html=True)



st.markdown("""
<div class="title">
CORTEXIA
</div>

<p style="text-align:center;">
Neural Health Intelligence<br>
</p>

""",unsafe_allow_html=True)


# ==========================
# DASHBOARD LAYOUT
# ==========================


col = st.columns([1,2.7,1.4])


# ==========================
# PARADIGM
# ==========================

with col[0]:

    st.markdown("""
    <h2 style="
    text-align:center;
    color:#F5F7FA;">
    PARADIGM
    </h2>

    <p style="
    text-align:center;
    color:#B8C5D3;">
    CX-10286
    </p>
    """,unsafe_allow_html=True)



    if st.button("Dashboard"):

        st.rerun()



 


    if st.button("Risk Insights"):

        st.switch_page(
            "pages/risk_insights.py"
        )



    if st.button("Medical Records"):

        st.switch_page(
            "pages/medical_records.py"
        )



    if st.button("Reports"):

        st.switch_page(
            "pages/reports.py"
        )
        
        
        # ==========================
# PARADIGM ROUTER
# ==========================


if "page" not in st.session_state:
    st.session_state.page="dashboard"



if st.session_state.page=="risk":


    st.markdown("""
    <div class="glass">

    <h1 style="color:#00eaff;text-align:center;">
    RISK INSIGHTS
    </h1>

    <p style="text-align:center;color:#B8C5D3;">
    CORTEXIA Predictive Risk Monitoring
    </p>

    </div>
    """,
    unsafe_allow_html=True)



    stats=get_dossier()


    c1,c2,c3=st.columns(3)


    with c1:
        
        
    
        st.metric(
        "Cardio Risk",
        str(stats["cardio"])+"%"
        )


    with c2:
        st.metric(
        "Metabolic Risk",
        str(stats["metabolic"])+"%"
        )


    with c3:
        st.metric(
        "Renal Risk",
        str(stats["renal"])+"%"
        )




if st.session_state.page=="records":


    st.markdown("""
    <div class="glass">

    <h1 style="color:#00eaff;text-align:center;">
    MEDICAL RECORDS
    </h1>

    <p style="text-align:center;">
    Patient Health Dossier Archive
    </p>

    </div>
    """,
    unsafe_allow_html=True)


    try:

        import sqlite3


        conn=sqlite3.connect(
        "cortexia.db"
        )


        data=conn.execute(
        "SELECT * FROM predictions"
        ).fetchall()


        for row in data:

            st.write(row)


    except:

        st.info(
        "No medical records available"
        )




if st.session_state.page=="reports":


    st.markdown("""
    <div class="glass">

    <h1 style="color:#00eaff;text-align:center;">
    REPORT CENTER
    </h1>

    <p style="text-align:center;">
    Generated AI Clinical Reports
    </p>

    </div>
    """,
    unsafe_allow_html=True)



    import os


    if os.path.exists(
    "health_report.json"
    ):


        with open(
        "health_report.json"
        ) as f:

            st.json(f.read())


    else:

        st.info(
        "No report generated yet"
        )
        
# ==========================
# NOSOGRAPHY CENTER
# ==========================
with col[1]:

    st.markdown("""

    <h2 style="
    text-align:center;
    color:#FFFFFF !important;
    font-weight:700;
    ">
    NOSOGRAPHY
    </h2>


    <div style="
    height:300px;
    display:flex;
    justify-content:center;
    align-items:center;
    ">

    <img width="280"
    src="https://static.vecteezy.com/system/resources/thumbnails/045/828/276/small/human-heart-image-free-png.png">

    </div>


    <h3 style="
    text-align:center;
    color:#F5F7FA;
    letter-spacing:2px;
    ">

    NEURAL ANALYSIS

    </h3>


    <p style="
    text-align:center;
    color:#B8C5D3;
    ">

    Predictive Clinical Intelligence Engine

    </p>

    """, unsafe_allow_html=True)
    
show_nexora()



show_medica_compendium()


show_health_radar()




    
    
    

# ==========================
# DOSSIER
# ==========================


with col[2]:

    stats = get_dossier()

    st.markdown(
    f"""
    <div class="glass">

    <h2 style="text-align:center;color:#F5F7FA;">
    DOSSIER
    </h2>


    <div class="card">

    <p style="font-size:12px;color:#AEB9C7;letter-spacing:2px;">
    CARDIO INDEX
    </p>

    <h1 style="margin:0;font-size:42px;">
    {stats['cardio']}%
    </h1>

    <p style="color:#6FD38A;">
    ▲ Stable
    </p>

    </div>


    <br>


    <div class="card">

    <p style="font-size:12px;color:#AEB9C7;letter-spacing:2px;">
    METABOLIC BALANCE
    </p>

    <h1 style="margin:0;font-size:42px;">
    {stats['metabolic']}%
    </h1>

    <p style="color:#6FD38A;">
    ▲ Optimal
    </p>

    </div>


    <br>


    <div class="card">

    <p style="font-size:12px;color:#AEB9C7;letter-spacing:2px;">
    RENAL INDEX
    </p>

    <h1 style="margin:0;font-size:42px;">
    {stats['renal']}%
    </h1>


    <p style="color:#6FD38A;">
    ▲ Normal
    </p>

    </div>


    <br>


    <div class="card">

    <p style="font-size:12px;color:#AEB9C7;letter-spacing:2px;">
    OVERALL HEALTH
    </p>

    <h1 style="margin:0;font-size:42px;">
    {stats['overall']}%
    </h1>

    <p style="color:#6FD38A;">
    ▲ CORTEXIA SCORE
    </p>

    </div>


    </div>
    """,
    unsafe_allow_html=True
    )

  # ==========================
# EMERGENCY RESPONSE MODULES
# ==========================

st.markdown("""
<div style="
text-align:center;
margin:45px 0 30px 0;
">

<p style="
letter-spacing:4px;
font-size:13px;
color:#9AA7B5;
">
EMERGENCY INTELLIGENCE
</p>


<h1 style="
font-size:38px;
color:#F5F7FA;
">
CORTEXIA RESPONSE NETWORK
</h1>


<p style="
color:#B8C5D3;
">
Blood assistance and healthcare discovery system
</p>

</div>
""", unsafe_allow_html=True)



response_cards = st.columns(2)



with response_cards[0]:

    st.markdown("""
    <div class="module-card">

    <div class="module-icon">
    •
    </div>

    <div class="module-title">
    Blood Donor Intelligence
    </div>

    <div class="module-desc">
    Emergency blood matching system
    </div>

    </div>
    """, unsafe_allow_html=True)


    if st.button("Open Blood Donor", key="blood_donor"):

        st.switch_page(
            "pages/blood_donor.py"
        )




   
   
with response_cards[1]:

    st.markdown("""
    <div class="module-card">

    <div class="module-icon">
    •
    </div>

    <div class="module-title">
    Health Network
    </div>

    <div class="module-desc">
    Nearby healthcare assistance
    </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Health Network",
        key="health_network"
    ):
        st.switch_page(
            "pages/health_network.py"
        )


# ==========================
# EMERGENCY RESPONSE HUB
# ==========================

st.markdown("""
<div style="
margin-top:45px;
padding:30px;
border-radius:22px;
background:linear-gradient(
135deg,
rgba(255,255,255,.05),
rgba(255,255,255,.03)
);
border:1px solid rgba(255,255,255,.12);
box-shadow:0 0 20px rgba(255,0,0,.08);
backdrop-filter:blur(18px);
-webkit-backdrop-filter:blur(18px);
display:flex;
align-items:center;
justify-content:center;
gap:25px;
">

<img
src="https://png.pngtree.com/png-vector/20241203/ourmid/pngtree-a-flashing-red-siren-for-emergency-png-image_14558464.png"
width="110">


<div>

<h1 style="
margin:0;
color:white;
font-size:36px;
font-weight:800;
letter-spacing:3px;
">
EMERGENCY RESPONSE HUB
</h1>

<p style="
margin:8px 0 5px 0;
color:#E5E7EB;
font-size:17px;
">
Rapid AI Emergency Coordination
</p>

<p style="
margin:0;
color:#AEB9C7;
font-size:14px;
">
Blood Donors • Health Network • Critical Response
</p>

</div>

</div>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

left, center, right = st.columns([1,5,1])

with center:

    if st.button(
        " LAUNCH EMERGENCY HUB",
        key="emergency_hub_btn",
        use_container_width=True
    ):
        st.switch_page("pages/emergency_hub.py")

# ==========================
# AI MODULE HEADER
# ==========================

st.markdown("""

<div style="
text-align:center;
margin:45px 0 30px 0;
">

<p style="
letter-spacing:4px;
font-size:13px;
color:#9AA7B5;
">

CLINICAL INTELLIGENCE

</p>

<h1 style="
font-size:38px;
color:#F5F7FA;
">

AI HEALTH MODULES

</h1>

<p style="
color:#B8C5D3;
">

Predictive diagnostics powered by CORTEXIA Neural Engine

</p>

</div>

""", unsafe_allow_html=True)


features = [

("•","Heart"),
("•","Diabetes"),
("🫁","Lung"),
("•","Kidney"),
("•","Cancer"),
("•","Cycle")

]


module_pages = {

    "Heart":"pages/heart.py",

    "Diabetes":"pages/diabetes.py",

    "Lung":"pages/lung.py",

    "Kidney":"pages/kidney.py",

    "Cancer":"pages/cancer.py",

    "Cycle":"pages/cycle.py"

}



# ==========================
# MODULE CARDS
# ==========================


cards = st.columns(3)



for i,(icon,name) in enumerate(features):


    with cards[i % 3]:



        st.markdown(f"""

        <div class="module-card">


        <div class="module-icon">

        {icon}

        </div>


        <div class="module-title">

        {name}

        </div>


        <div class="module-desc">

        Predictive Clinical Assessment

        </div>


        <div class="module-arrow">

        →

        </div>


        </div>


        """,
        unsafe_allow_html=True)



        if st.button(
            f"Open {name}",
            key=f"open_{name}"
        ):


            st.switch_page(
                module_pages[name]
            )









# ==========================
# FOOTER
# ==========================


st.markdown("""

<div style="
text-align:center;
margin-top:40px;
padding:15px;
color:#7F8C9A;
font-size:12px;
letter-spacing:2px;
">


CORTEXIA © NEURAL HEALTH INTELLIGENCE


</div>

""",
unsafe_allow_html=True)

st.markdown("""
<style>

/* ===== CORTEXIA FINAL POLISH ===== */


.card,
.module-card,
.glass{

transition:
background .25s ease,
border .25s ease;

}



.card:hover,
.module-card:hover{

background:
rgba(255,255,255,.08)!important;

border-color:
rgba(0,234,255,.25)!important;

}




.stButton button{

font-weight:600!important;

letter-spacing:.5px;

}




[data-testid="stDataFrame"]{

border-radius:18px!important;

overflow:hidden;

}




input,
textarea,
select{

background:
rgba(255,255,255,.06)!important;

color:white!important;

border-radius:12px!important;

}




.block-container{

padding-top:2rem!important;

padding-bottom:2rem!important;

}



</style>

""", unsafe_allow_html=True)







# ==========================
# FINAL FOOTER
# ==========================


st.markdown("""

<br><br>

<div style="
text-align:center;
color:#7F8C9A;
font-size:12px;
letter-spacing:2px;
">


CORTEXIA © 2026

<br>

NEURAL HEALTH INTELLIGENCE SYSTEM


</div>


""",
unsafe_allow_html=True)




