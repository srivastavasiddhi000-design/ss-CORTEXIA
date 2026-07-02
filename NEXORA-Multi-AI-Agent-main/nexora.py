import streamlit as st
import os

from pydub import AudioSegment

AudioSegment.ffmpeg = r"C:\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-8.1.1-essentials_build\bin"

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import tempfile





st.set_page_config(
    page_title="NEXORA AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================
# AGENT LOADER FINAL FIX
# ==========================

@st.cache_resource(show_spinner=False)
def load_agents():

    import nexora_agents

    return (
        nexora_agents.research_agent,
        nexora_agents.knowledge_agent,
        nexora_agents.planner_agent,
        nexora_agents.code_agent
    )
def get_agents():

    if "agents" not in st.session_state:

        with st.spinner(
"⚡ LOADING..."
):
            st.session_state.agents = load_agents()


    return st.session_state.agents



research_agent, knowledge_agent, planner_agent, code_agent = get_agents()



# ==========================
# CSS SAME
# ==========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Poppins:wght@300;400;600;700&display=swap');

*{
font-family:'Poppins',sans-serif;
}


.stApp{

background:
linear-gradient(
rgba(0,5,20,.55),
rgba(0,8,30,.75)
),
url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUQ5MFL2uwBPrbUx6JPMW8-AEPOzMM5DYgEe8hcYuJww&s=10");

background-size:cover;
background-position:center;
background-attachment:fixed;

}


#MainMenu,footer{
visibility:hidden;
}



.brain{

text-align:center;
margin-top:-25px;

}



.brain img{

width:160px;

filter:
drop-shadow(0 0 35px #00eaff)
drop-shadow(0 0 90px #0066ff);

animation:pulse 2s infinite;

}


@keyframes pulse{

0%{
transform:scale(1);
}

50%{
transform:scale(1.08);
}

100%{
transform:scale(1);
}

}


.logo{

text-align:center;

font-family:'Orbitron';

font-size:105px;

font-weight:900;

letter-spacing:25px;

color:white;

text-shadow:

0 0 30px #00ffff,
0 0 80px #008cff,
0 0 160px #0066ff;

}



.main-title{

text-align:center;

font-family:'Orbitron';

font-size:30px;

color:white;

text-shadow:
0 0 25px cyan;

}



.tagline{

text-align:center;

font-size:18px;

letter-spacing:3px;

color:#bffaff;

}




div.stButton > button{

height:260px!important;

width:100%!important;

background:
rgba(5,20,45,.65)!important;


border:
1px solid cyan!important;


border-radius:35px!important;


box-shadow:
0 0 35px #0066ff!important;


color:white!important;

font-size:20px!important;

font-weight:700!important;

}



div.stButton > button:hover{

transform:
translateY(-10px)
scale(1.04);


box-shadow:
0 0 70px cyan!important;

}







.micbox button{


height:65px!important;
width:65px!important;


border-radius:50%!important;


background:
linear-gradient(
135deg,
rgba(0,255,255,.3),
rgba(0,20,70,.9)
)!important;


border:2px solid cyan!important;


box-shadow:

0 0 30px cyan,
0 0 100px blue!important;


font-size:28px!important;


}

}


.micbox button:hover{

transform:scale(1.15);


box-shadow:

0 0 60px cyan,
0 0 150px blue!important;

}

/* ==========================
   NEXORA GLASS NEON SEARCH BAR
========================== */


div[data-testid="stChatInput"]{

background:
rgba(0,20,60,0.45)!important;

backdrop-filter:
blur(20px)!important;

-webkit-backdrop-filter:
blur(20px)!important;

border:

1px solid rgba(0,255,255,0.7)!important;


border-radius:30px!important;


box-shadow:

0 0 25px cyan,
0 0 70px #0066ff,
inset 0 0 25px rgba(0,255,255,.25)!important;


}



div[data-testid="stChatInput"] textarea{


color:white!important;

font-size:18px!important;


background:
transparent!important;


}



div[data-testid="stChatInput"] textarea::placeholder{


color:#bffaff!important;

opacity:0.8!important;

}




div[data-testid="stChatInput"]:focus-within{


box-shadow:

0 0 40px cyan,
0 0 120px blue,
inset 0 0 35px rgba(0,255,255,.35)!important;


transform:scale(1.02);

transition:.3s ease;


}

</style>

""",
unsafe_allow_html=True)



# ==========================
# HEADER
# ==========================

st.markdown("""

<div class="brain">

<img src="https://static.vecteezy.com/system/resources/previews/053/964/142/non_2x/a-digital-representation-of-a-brain-connected-by-glowing-lines-and-nodes-symbolizing-neural-networks-and-cognitive-processes-png.png">

</div>


<div class="logo">
NEXORA
</div>


<div class="main-title">
MULTI AI AGENT SYSTEM
</div>


<div class="tagline">
Retrieve • Augment • Integrate • Instantiate
</div>


""",
unsafe_allow_html=True)



# ==========================
# AGENT CARDS
# ==========================


a,b,c,d = st.columns(4)


with a:

    if st.button(
"""
🔎 Research Nexus

Web Intelligence
Deep Search
""",
key="research_card"
):

        st.switch_page(
        "pages/1_Research_Agent.py"
        )


with b:

    if st.button(
"""
🧠 Insight Repository

PDF + Knowledge
Analysis
""",
key="knowledge_card"
):

        st.switch_page(
        "pages/2_Knowledge_Agent.py"
        )


with c:

    if st.button(
"""
🎯 Tactical Matrix

Planning
Execution
""",
key="planner_card"
):

        st.switch_page(
        "pages/3_Planner_Agent.py"
        )
with d:

    if st.button(
        """
💻 Code Intelligence

Debug +
Development
        """,
        key="code_card"
    ):

        st.switch_page(
            "pages/4_Code_Agent.py"
        )

# ==========================
# COMMAND CENTER
# ==========================


st.markdown(
"""
<h2 style="
text-align:center;
color:#00ffff;
text-shadow:0 0 25px cyan;
">
⚡ NEXUS COGNIISPHERE
</h2>
""",
unsafe_allow_html=True
)



mic_col, search_col = st.columns(
    [1,12],
    vertical_alignment="center"
)
# ==========================
# MIC BUTTON
# ==========================

with mic_col:

    st.markdown(
        "<div class='micbox'>",
        unsafe_allow_html=True
    )


    audio = mic_recorder(

        start_prompt="◉",

        stop_prompt="■",

        just_once=True,

        key="nexora_mic"

    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )




# ==========================
# SEARCH
# ==========================


with search_col:

    voice_query = st.session_state.get(
        "voice_text",
        ""
    )


    query = st.chat_input(
        "Ask NEXORA anything..."
    )


    if voice_query and not query:

        query = voice_query
        st.session_state["voice_text"] = ""



# ==========================
# TEXT CHAT
# ==========================


if query:


    (
    research_agent,
    knowledge_agent,
    planner_agent,
    code_agent
    ) = get_agents()



    q = query.lower()



    if "research" in q:


        answer = research_agent(query)



    elif "plan" in q or "planner" in q:


        answer = planner_agent(query)



    elif "code" in q:


        answer = code_agent(query)



    else:


        answer = knowledge_agent(query)




    st.markdown(
    """
    ## 🤖 NEXORA RESPONSE
    """
    )


    st.write(answer)







# ==========================
# VOICE PROCESSING
# ==========================


if audio is not None:


    (
        research_agent,
        knowledge_agent,
        planner_agent,
        code_agent
    ) = get_agents()



st.info(
    "🟢 NEXORA listening..."
    )



recognizer = sr.Recognizer()



recognizer.energy_threshold = 200

recognizer.dynamic_energy_threshold=True

recognizer.pause_threshold=0.6


# ==========================
# VOICE PROCESSING
# ==========================


if audio is not None:


    try:

        st.info("🟢 NEXORA listening...")


        # --------------------------
        # Save recorded audio
        # --------------------------

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".webm"
        ) as f:

            f.write(
                audio["bytes"]
            )

            raw_file = f.name



        # --------------------------
        # Convert WEBM -> WAV
        # --------------------------

        voice_file = raw_file.replace(
            ".webm",
            ".wav"
        )


        sound = AudioSegment.from_file(
            raw_file
        )


        sound.export(
            voice_file,
            format="wav"
        )



        # --------------------------
        # Speech Recognition
        # --------------------------

        recognizer = sr.Recognizer()


        with sr.AudioFile(
            voice_file
        ) as source:


            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.3
            )


            voice_audio = recognizer.record(
                source
            )



        text = recognizer.recognize_google(
            voice_audio,
            language="en-IN"
        )



        st.success(
            "🎧 Heard: " + text
        )



        # --------------------------
        # Agent Routing
        # --------------------------

        v = text.lower()



        if "research" in v:


            answer = research_agent(text)



        elif "plan" in v or "planner" in v:


            answer = planner_agent(text)



        elif "code" in v:


            answer = code_agent(text)



        else:


            answer = knowledge_agent(text)




        # --------------------------
        # Response
        # --------------------------

        st.markdown(
        """
        ## 🤖 NEXORA RESPONSE
        """
        )


        st.write(answer)



    except sr.UnknownValueError:


        st.warning(
            "⚠ Voice not clear, try again"
        )



    except sr.RequestError:


        st.error(
            "⚠ Speech service unavailable"
        )



    except Exception as e:


        st.error(
            f"Voice error: {e}"
        )



    finally:


        # cleanup files

        try:

            if os.path.exists(raw_file):
                os.remove(raw_file)


            if os.path.exists(voice_file):
                os.remove(voice_file)


        except:
            pass