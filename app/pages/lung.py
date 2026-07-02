import streamlit as st

from app.components.module_engine import disease_page



disease_page(

    title="LUNG ANALYSIS",

    icon="🫁",

    fields=[

        "Age",

        "Oxygen Level",

        "Respiratory Rate",

        "Lung Capacity",

        "Smoking",

        "Cough Duration",

        "Breathlessness Level",

        "Chest Pain"

    ]

)