import streamlit as st


def apply_theme(title):

    st.markdown(f"""
    <style>

    html, body, [data-testid="stAppViewContainer"] {{

        font-family:
        "Segoe UI Variable",
        "Segoe UI",
        sans-serif;

        color:#F7FCFF;

    }}

    .stApp {{

        background-image:
        linear-gradient(
        rgba(3,8,25,.60),
        rgba(5,5,25,.88)
        ),
        url("https://cdn.botpenguin.com/assets/website/background/background-17-18.webp");

        background-size:cover;
        background-position:center;
        background-attachment:fixed;

    }}

    #MainMenu,
    header,
    footer {{

        visibility:hidden;

    }}

    .title {{

        font-size:48px;

        font-weight:900;

        text-align:center;

        color:#F7FCFF;

        letter-spacing:6px;

        text-shadow:

        0 0 12px #00EAFF,

        0 0 35px #008CFF;

        margin-bottom:10px;

    }}

    .glass {{

        background:
        rgba(15,25,55,.50);

        border:
        1px solid rgba(0,234,255,.25);

        border-radius:24px;

        padding:24px;

        backdrop-filter:blur(18px);

        box-shadow:
        0 10px 30px rgba(0,0,0,.35);

    }}

    .stButton>button {{

        width:100%;

        border-radius:30px;

        border:none;

        padding:14px;

        color:white;

        font-weight:700;

        background:
        linear-gradient(
        90deg,
        #00EAFF,
        #008CFF
        );

    }}

    .stButton>button:hover {{

        box-shadow:
        0 0 25px rgba(0,234,255,.5);

    }}

    </style>

    <div class="title">
    {title}
    </div>

    """, unsafe_allow_html=True)