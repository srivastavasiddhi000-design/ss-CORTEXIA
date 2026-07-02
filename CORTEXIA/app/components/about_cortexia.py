import streamlit as st


def show_about_cortexia():

    st.markdown("""
    <div style="
    margin-top:35px;
    background:rgba(255,255,255,.045);
    border:1px solid rgba(255,255,255,.12);
    border-radius:18px;
    padding:25px;
    backdrop-filter:blur(15px);
    ">


    <h2 style="
    text-align:center;
    color:rgba(255,255,255,0.9);
    letter-spacing:3px;
    ">
    ABOUT CORTEXIA
    </h2>


    <div style="
    color:rgba(255,255,255,0.7);
    font-size:15px;
    line-height:1.8;
    ">


    <p>• CORTEXIA is an advanced Neural Health Intelligence System powered by Artificial Intelligence and predictive analytics.</p>

    <p>• It analyzes health-related data to identify potential risks and provide intelligent clinical insights.</p>

    <p>• The system includes AI-driven modules for cardiovascular, diabetes, respiratory, kidney, cancer, and cycle health assessment.</p>

    <p>• CORTEXIA enables early risk detection through smart data processing and predictive healthcare technology.</p>

    <p>• It provides personalized health insights to support better monitoring and informed decisions.</p>

    <p>• The platform combines medical intelligence with modern technology to improve healthcare accessibility.</p>

    <p>• CORTEXIA works as a smart healthcare companion, supporting proactive and efficient health management.</p>

    <p>• It represents the integration of artificial intelligence with the future of digital healthcare.</p>


    </div>

    </div>

    """, unsafe_allow_html=True)