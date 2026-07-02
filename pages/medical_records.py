import streamlit as st

from backend.database import connect


st.set_page_config(
    page_title="CORTEXIA Medical Records",
    page_icon="📁",
    layout="wide"
)



st.markdown("""
<style>

html,body{
font-family:"Segoe UI Variable","Segoe UI",sans-serif;
color:#F7FCFF;
}


.stApp{

background-image:
linear-gradient(
rgba(3,8,25,.75),
rgba(5,5,25,.95)
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

text-align:center;
font-size:48px;
font-weight:900;
letter-spacing:6px;
color:#00eaff;

}



.panel{

background:#071426;

border:1px solid rgba(0,234,255,.25);

border-radius:18px;

padding:25px;

margin-top:25px;

}



.stDataFrame{

border-radius:15px;

}



.stButton button{

background:#071426;

color:white;

border:1px solid #00eaff;

border-radius:12px;

}



</style>

""",unsafe_allow_html=True)




st.markdown(
"""
<div class="title">
• MEDICAL RECORDS
</div>

<p style="
text-align:center;
color:#B8C5D3;
">
CORTEXIA Clinical Archive System
</p>

""",
unsafe_allow_html=True
)




conn = connect()



try:

    data = conn.execute(
    """
    SELECT *
    FROM medical_records
    ORDER BY id DESC
    """
    ).fetchall()


except Exception:

    data=[]


conn.close()



st.markdown(
"""
<div class="panel">

<h2 style="color:#00eaff;">
PATIENT HISTORY DATABASE
</h2>

<p style="color:#B8C5D3;">
Stored clinical observations and analysis reports
</p>

</div>
""",
unsafe_allow_html=True
)



if data:


    st.dataframe(
        data,
        use_container_width=True,
        height=450
    )


else:


    st.markdown(
    """
    <div class="panel">

    <h3>
    No Records Found
    </h3>

    <p style="color:#B8C5D3;">
    Medical analysis reports will appear here after prediction modules are used.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )