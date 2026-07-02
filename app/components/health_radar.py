import streamlit as st
import folium
import requests

from math import radians, sin, cos, sqrt, atan2
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation

from backend.health_radar_backend import (
    get_nearby_health_services,
    find_place_location
)



def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        +
        cos(radians(lat1))
        *
        cos(radians(lat2))
        *
        sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return R * c




def show_health_radar():


    st.markdown("""
    <div style="
    margin-top:35px;
    background:rgba(255,255,255,.045);
    border:1px solid rgba(255,255,255,.12);
    border-radius:22px;
    padding:28px;
    backdrop-filter:blur(18px);
    ">

    <h2 style="
    color:white;
    text-align:center;
    letter-spacing:3px;
    ">
    🛰 CORTEXIA HEALTH RADAR
    </h2>

    <p style="color:#B8C5D3;text-align:center;">
    Real-Time Healthcare Discovery System
    </p>

    </div>
    """,
    unsafe_allow_html=True)



    # ---------- GPS ----------


    location = get_geolocation()


    if location:

        lat = location["coords"]["latitude"]
        lon = location["coords"]["longitude"]


    else:

        lat = 28.6139
        lon = 77.2090

        st.warning(
            "Allow location access for live distance"
        )





    # ---------- SEARCH ----------


    st.markdown(
        """
        <h3 style="color:white;">
        🔎 Search Healthcare Facility
        </h3>
        """,
        unsafe_allow_html=True
    )


    search = st.text_input(
        "",
        placeholder="Type hospital / clinic name..."
    )



    if search:


        place = find_place_location(search)



        if place:


            dest_lat = place["lat"]
            dest_lon = place["lon"]
            name = place["name"]


            distance = calculate_distance(
                lat,
                lon,
                dest_lat,
                dest_lon
            )


            time = (distance / 35) * 60



            st.success(
                f"""
📍 {name}

🚗 Distance: {distance:.2f} km

⏱ Travel Time: {int(time)} minutes
"""
            )


            st.link_button(
                "🗺 Open Route",
                f"https://www.google.com/maps/dir/?api=1&origin={lat},{lon}&destination={dest_lat},{dest_lon}"
            )


        else:

            st.warning(
                "Facility not found"
            )






    services = get_nearby_health_services(
        lat,
        lon
    )





    # ---------- MAP ----------


    m = folium.Map(

        location=[
            lat,
            lon
        ],

        zoom_start=14,

        tiles="CartoDB dark_matter"

    )



    # user dot

    folium.CircleMarker(

        location=[
            lat,
            lon
        ],

        radius=10,

        color="#00EAFF",

        fill=True,

        fill_color="#00EAFF",

        fill_opacity=1,

        popup="CORTEXIA Current Location"

    ).add_to(m)





    hospital_count = 0
    pharmacy_count = 0
    blood_count = 0





    for s in services:


        t = s.get(
            "type",
            "facility"
        )


        if t == "hospital":

            hospital_count += 1
            dot = "red"


        elif t == "pharmacy":

            pharmacy_count += 1
            dot = "green"


        elif t == "blood_bank":

            blood_count += 1
            dot = "darkred"


        else:

            dot = "orange"




        folium.CircleMarker(

            location=[

                s["lat"],
                s["lon"]

            ],

            radius=4,

            color=dot,

            fill=True,

            fill_color=dot,

            fill_opacity=0.85,

            tooltip=s["name"]

        ).add_to(m)





    st_folium(

        m,

        height=380,

        width=700,

        key="radar_map"

    )





    # ---------- METRICS ----------


    c1,c2,c3 = st.columns(3)


    with c1:

        st.metric(
            "Hospitals",
            hospital_count
        )


    with c2:

        st.metric(
            "Pharmacies",
            pharmacy_count
        )


    with c3:

        st.metric(
            "Blood Banks",
            blood_count
        )