import streamlit as st
import requests


OVERPASS_URLS = [
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter"
]

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"





@st.cache_data(ttl=300)
def get_nearby_health_services(
        lat,
        lon,
        radius=3000
):


    query = f"""

    [out:json][timeout:15];

    (

    node["amenity"="hospital"]
    (around:{radius},{lat},{lon});

    way["amenity"="hospital"]
    (around:{radius},{lat},{lon});

    node["amenity"="clinic"]
    (around:{radius},{lat},{lon});

    node["amenity"="pharmacy"]
    (around:{radius},{lat},{lon});

    node["healthcare"="blood_bank"]
    (around:{radius},{lat},{lon});

    );

    out center tags;

    """



    for url in OVERPASS_URLS:


        try:


            response = requests.get(

                url,

                params={
                    "data": query
                },

                timeout=20,

                headers={
                    "User-Agent":
                    "CORTEXIA-Health-Radar"
                }

            )


            response.raise_for_status()


            data = response.json()


            services = []

            seen = set()



            for item in data.get(
                "elements",
                []
            ):



                tags = item.get(
                    "tags",
                    {}
                )


                lat2 = item.get("lat")
                lon2 = item.get("lon")



                if lat2 is None:


                    center = item.get(
                        "center",
                        {}
                    )


                    lat2 = center.get("lat")
                    lon2 = center.get("lon")



                if lat2 is None or lon2 is None:
                    continue




                name = tags.get(
                    "name",
                    "Unnamed Facility"
                )



                if name in seen:
                    continue



                seen.add(name)




                facility_type = (

                    tags.get("amenity")

                    or

                    tags.get("healthcare")

                    or

                    "facility"

                )




                services.append({

                    "name": name,

                    "type": facility_type,

                    "lat": float(lat2),

                    "lon": float(lon2)

                })



            return services



        except Exception:

            continue




    st.warning(
        "Health Radar service unavailable"
    )

    return []









# ================= SEARCH =================


def search_health_service(
        services,
        keyword
):


    keyword = keyword.lower().strip()



    for service in services:


        if keyword in service["name"].lower():

            return service



    return None







# ================= PLACE SEARCH =================


def find_place_location(
        place_name
):


    try:


        response = requests.get(

            NOMINATIM_URL,

            params={

                "q": place_name,

                "format": "json",

                "limit": 5,

                "addressdetails": 1,

                "namedetails": 1

            },


            headers={

                "User-Agent":
                "CORTEXIA-Health-Radar"

            },


            timeout=10

        )



        results = response.json()



        if not results:

            return None





        # choose best result

        best = results[0]




        return {

            "name":
            best.get(
                "display_name",
                place_name
            ),


            "lat":
            float(
                best["lat"]
            ),


            "lon":
            float(
                best["lon"]
            )

        }




    except Exception:


        return None