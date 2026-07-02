import streamlit as st


def apply_theme(title=""):


    st.markdown(
    """

<style>


/* =====================
   CORTEXIA GLOBAL
===================== */


html,body,[data-testid="stAppViewContainer"]{

font-family:
"Segoe UI Variable",
"Segoe UI",
sans-serif;

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




.block-container{

padding-top:2rem!important;

padding-bottom:2rem!important;

}





/* =====================
   TITLE
===================== */


.cortex-title{


text-align:center;

color:#00eaff;

letter-spacing:4px;

font-size:38px;

font-weight:900;

margin-bottom:30px;


}





/* =====================
   PANELS
===================== */


.cortex-panel{


background:
rgba(255,255,255,.045);


border:
1px solid rgba(255,255,255,.14);


border-radius:18px;


padding:25px;


backdrop-filter:blur(18px);


margin-bottom:25px;


transition:.3s;


}




.cortex-panel:hover{


border-color:
rgba(0,234,255,.35);


}





/* =====================
   INPUTS
===================== */


.stNumberInput input{


background:
rgba(255,255,255,.06)!important;


color:white!important;


border-radius:12px!important;


border:
1px solid rgba(255,255,255,.15)!important;


}





label{


color:#B8C5D3!important;


font-weight:600!important;


}






/* =====================
   BUTTONS
===================== */


.stButton button{


width:100%;


background:
rgba(0,234,255,.08);


color:white;


border-radius:12px;


border:
1px solid rgba(0,234,255,.35);



font-weight:700;



}




.stButton button:hover{


background:
rgba(0,234,255,.20);


border-color:#00eaff;


}




/* =====================
   DATAFRAME
===================== */


[data-testid="stDataFrame"]{


border-radius:16px!important;

overflow:hidden!important;


}





/* =====================
   RESULT CARDS
===================== */


.result-card{


background:
rgba(255,255,255,.05);


border:

1px solid rgba(255,255,255,.15);


border-radius:18px;


padding:25px;


text-align:center;


}





</style>

""",
unsafe_allow_html=True
)




    if title:


        st.markdown(
        f"""
        <div class="cortex-title">

        {title}

        </div>
        """,
        unsafe_allow_html=True
        )