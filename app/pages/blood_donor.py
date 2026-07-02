import streamlit as st
import sqlite3
from datetime import date


st.set_page_config(
    page_title="Blood Donor Intelligence",
    page_icon="🩸",
    layout="wide"
)


# ==========================
# DATABASE
# ==========================

conn = sqlite3.connect("cortexia.db", check_same_thread=False)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS donors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
blood TEXT,
location TEXT,
phone TEXT,
last_donation TEXT,
available TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS blood_requests(
id INTEGER PRIMARY KEY AUTOINCREMENT,
blood TEXT,
location TEXT,
units TEXT,
urgency TEXT
)
""")


conn.commit()



# ==========================
# CSS
# ==========================

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



.glass{

background:
rgba(255,255,255,.045);

border:
1px solid rgba(255,255,255,.12);

border-radius:20px;

padding:25px;

backdrop-filter:blur(18px);

}



.title{

text-align:center;

font-size:42px;

font-weight:900;

letter-spacing:5px;

color:#F8FAFC;

}



.subtitle{

text-align:center;

color:#B8C5D3;

}



.card{

background:

rgba(255,255,255,.045);

border:

1px solid rgba(255,255,255,.12);

border-radius:18px;

padding:20px;

backdrop-filter:blur(15px);

}



.card:hover{

border-color:#00eaff;

background:

rgba(255,255,255,.08);

}



.stButton button{

width:100%;

background:

rgba(0,234,255,.08)!important;

border:

1px solid #00eaff!important;

border-radius:14px!important;

color:white!important;

font-weight:600!important;

}



input,textarea,select{

background:
rgba(255,255,255,.06)!important;

color:white!important;

border-radius:12px!important;

}



</style>
""",unsafe_allow_html=True)



# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="glass">

<div class="title">

• BLOOD DONOR INTELLIGENCE

</div>

<p class="subtitle">

CORTEXIA Emergency Blood Matching Network

</p>

</div>
""",unsafe_allow_html=True)



st.write("")



tab1,tab2,tab3 = st.tabs(
[
"• Register Donor",
"• Find Blood",
"• Emergency Request"
]
)



# ==========================
# REGISTER
# ==========================

with tab1:

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.subheader("Donor Registration")


    name = st.text_input("Donor Name")

    blood = st.selectbox(
        "Blood Group",
        [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
        ]
    )


    location = st.text_input("City / Location")

    phone = st.text_input("Contact")


    available = st.selectbox(
        "Availability",
        ["Available","Unavailable"]
    )


    if st.button("Register Donor"):

        cursor.execute(
        """
        INSERT INTO donors
        (name,blood,location,phone,last_donation,available)
        VALUES(?,?,?,?,?,?)
        """,
        (
        name,
        blood,
        location,
        phone,
        str(date.today()),
        available
        ))

        conn.commit()

        st.success(
        "Donor added to CORTEXIA network"
        )


    st.markdown("</div>",unsafe_allow_html=True)




# ==========================
# SEARCH
# ==========================

with tab2:

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.subheader("AI Blood Match Search")


    req_blood = st.selectbox(
        "Required Blood Group",
        [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
        ],
        key="search"
    )


    req_location = st.text_input(
        "Required Location"
    )


    if st.button("Find Compatible Donors"):


        result = cursor.execute(
        """
        SELECT name,location,phone
        FROM donors
        WHERE blood=?
        AND available='Available'
        """,
        (req_blood,)
        ).fetchall()



        if result:

            st.success(
            f"{len(result)} Donor(s) Found"
            )


            for donor in result:

                st.markdown(
                f"""
                <div class="card">

                • <b>{donor[0]}</b>

                <br>

                📍 {donor[1]}

                <br>

                • {donor[2]}

                </div>
                """,
                unsafe_allow_html=True
                )

        else:

            st.warning(
            "No donor available"
            )


    st.markdown("</div>",unsafe_allow_html=True)





# ==========================
# EMERGENCY
# ==========================

with tab3:


    st.markdown("<div class='card'>",unsafe_allow_html=True)


    st.subheader("Emergency Blood Request")


    blood = st.selectbox(
        "Blood Needed",
        [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
        ],
        key="request"
    )


    location = st.text_input(
        "Hospital Location"
    )


    units = st.number_input(
        "Units Required",
        1,
        10
    )


    urgency = st.selectbox(
        "Urgency",
        [
        "Normal",
        "Urgent",
        "Critical"
        ]
    )


    if st.button("Broadcast Request"):


        cursor.execute(
        """
        INSERT INTO blood_requests
        (blood,location,units,urgency)
        VALUES(?,?,?,?)
        """,
        (
        blood,
        location,
        units,
        urgency
        ))


        conn.commit()


        st.error(
        "Emergency request broadcasted"
        )


    st.markdown("</div>",unsafe_allow_html=True)