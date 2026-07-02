import streamlit as st

from backend.database import create_table,get_reports


st.set_page_config(
    page_title="CORTEXIA Reports",
    page_icon="📄",
    layout="wide"
)


create_table()



st.markdown("""
<style>

.stApp{

background:
linear-gradient(
rgba(3,8,25,.7),
rgba(5,5,25,.9)
),
url("https://cdn.botpenguin.com/assets/website/background/background-17-18.webp");

background-size:cover;
color:white;

}


h1,h2{
color:#00eaff;
}


</style>
""",unsafe_allow_html=True)



st.title("📄 AI REPORT ARCHIVE")


data=get_reports()



if not data:

    st.info(
    "No reports generated yet."
    )


else:

    for row in data:

        st.markdown(
        f"""

        ### {row[0]}

        Status:
        **{row[1]}**

        Score:
        **{row[2]}%**

        Summary:

        {row[3]}

        Date:
        {row[4]}

        ---

        """
        )