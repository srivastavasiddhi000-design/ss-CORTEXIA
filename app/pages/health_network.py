import streamlit as st
import sqlite3
from streamlit_geolocation import streamlit_geolocation
import folium
from streamlit_folium import st_folium
from math import radians, sin, cos, sqrt, atan2


st.set_page_config(
    page_title="Health Network",
    page_icon="•",
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


cursor.execute("""
CREATE TABLE IF NOT EXISTS health_centres(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
type TEXT,
location TEXT,
contact TEXT,
status TEXT,
latitude REAL,
longitude REAL
)
""")


conn.commit()



# ==========================
# DISTANCE FUNCTION
# ==========================

def distance(lat1,lon1,lat2,lon2):

    R = 6371

    dlat = radians(lat2-lat1)
    dlon = radians(lon2-lon1)

    a = (
        sin(dlat/2)**2 +
        cos(radians(lat1)) *
        cos(radians(lat2)) *
        sin(dlon/2)**2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1-a)
    )

    return round(
        R*c,
        2
    )



# ==========================
# CSS
# ==========================

st.markdown("""
<style>

html,body,[data-testid="stAppViewContainer"]{

font-family:"Segoe UI Variable","Segoe UI",sans-serif;
color:white;

}


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



#MainMenu,header,footer{
display:none;
}




.card{

background:rgba(255,255,255,.05);

border:
1px solid rgba(0,234,255,.18);

border-radius:18px;

padding:22px;

margin:15px 0;

backdrop-filter:blur(12px);

}




.title{

text-align:center;

font-size:42px;

font-weight:900;

letter-spacing:4px;

color:#00eaff;

}



.subtitle{

text-align:center;

color:#B8C5D3;

}



.stButton button{

background:
rgba(0,234,255,.08)!important;

border:
1px solid #00eaff!important;

border-radius:14px!important;

color:white!important;

}


</style>

""",
unsafe_allow_html=True)




# ==========================
# HEADER
# ==========================


st.markdown("""
<div>

<h1 class="title">
 HEALTH NETWORK INTELLIGENCE
</h1>


<p class="subtitle">
CORTEXIA Smart Healthcare Discovery System
</p>


</div>
""",
unsafe_allow_html=True)




# ==========================
# GPS
# ==========================


st.markdown("""
<h2 style="
text-align:center;
color:#00eaff;
letter-spacing:3px;
margin-top:35px;
">

 CORTEXIA LOCATION SCAN

</h2>


<p style="
text-align:center;
color:#B8C5D3;
">

Live GPS Health Network Tracking

</p>

""",
unsafe_allow_html=True)



location_data = streamlit_geolocation()



user_lat = None
user_lon = None



if location_data:


    user_lat = location_data.get(
        "latitude"
    )

    user_lon = location_data.get(
        "longitude"
    )



    if user_lat and user_lon:


        st.success(
            f"GPS Locked : {user_lat:.4f}, {user_lon:.4f}"
        )



        m = folium.Map(
            location=[
                user_lat,
                user_lon
            ],
            zoom_start=13
        )


        folium.Marker(
            [
                user_lat,
                user_lon
            ],
            popup="Your Location",
            icon=folium.Icon(
                color="blue"
            )
        ).add_to(m)



        centres = cursor.execute(
        """
        SELECT name,latitude,longitude
        FROM health_centres
        WHERE latitude IS NOT NULL
        """
        ).fetchall()



        for c in centres:

            folium.Marker(
            [
            c[1],
            c[2]
            ],
            popup=c[0],
            icon=folium.Icon(
                color="green"
            )
            ).add_to(m)



        st_folium(
            m,
            width=900,
            height=500
        )





tabs = st.tabs(
[
" Add Centre",
" Find Centre"
]
)




# ==========================
# ADD CENTRE
# ==========================


with tabs[0]:


    st.markdown(
    "<div class='card'>",
    unsafe_allow_html=True
    )


    st.subheader(
        "Register Health Centre"
    )


    name = st.text_input(
        "Centre Name"
    )


    centre_type = st.selectbox(
        "Centre Type",
        [
        "Hospital",
        "Clinic",
        "Diagnostic Centre",
        "Emergency Unit"
        ]
    )


    centre_location = st.text_input(
        "Location"
    )


    contact = st.text_input(
        "Contact"
    )


    status = st.selectbox(
        "Availability",
        [
        "Open",
        "Emergency Available",
        "Closed"
        ]
    )



    if st.button(
        "Add Health Centre"
    ):



        cursor.execute(
        """
        INSERT INTO health_centres
        (
        name,
        type,
        location,
        contact,
        status,
        latitude,
        longitude
        )

        VALUES(?,?,?,?,?,?,?)

        """,
        (
        name,
        centre_type,
        centre_location,
        contact,
        status,
        user_lat,
        user_lon
        )
        )


        conn.commit()


        st.success(
        "Centre added to CORTEXIA network"
        )



    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )






# ==========================
# SEARCH
# ==========================


with tabs[1]:


    st.markdown(
    "<div class='card'>",
    unsafe_allow_html=True
    )


    st.subheader(
        "AI Health Centre Finder"
    )


    if user_lat:

        data = cursor.execute(
        """
        SELECT 
        name,type,location,contact,status,latitude,longitude
        FROM health_centres
        WHERE latitude IS NOT NULL
        """
        ).fetchall()



        if data:


            st.success(
            f"{len(data)} centre(s) detected"
            )


            sorted_data=[]


            for c in data:


                d = distance(
                user_lat,
                user_lon,
                c[5],
                c[6]
                )


                sorted_data.append(
                    (
                    d,
                    c
                    )
                )


            sorted_data.sort()



            for d,c in sorted_data:


                st.markdown(
                f"""

<div class="card">


<b>{c[0]}</b>


<br><br>

🩺 {c[1]}


<br>

 {c[2]}


<br>

 {c[3]}


<br>

 {c[4]}


<br><br>

 Distance:
<b>{d} KM</b>


</div>


                """,
                unsafe_allow_html=True
                )



        else:

            st.info(
            "No centres registered yet"
            )



    else:

        st.warning(
        "Enable GPS to find nearest centres"
        )



    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )