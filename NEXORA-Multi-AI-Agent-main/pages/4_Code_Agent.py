import streamlit as st

from nexora_agents import code_agent


st.set_page_config(
    page_title="Code Nexus",
    page_icon="💻",
    layout="wide"
)


st.title("💻 Code Intelligence")

st.caption(
    "NEXORA Coding Intelligence Agent"
)



query = st.text_area(
    "Enter your coding problem",
    placeholder="Debug this Python code..."
)



mode = st.selectbox(
    "Coding Mode",
    [
        "Debug Code",
        "Explain Concept",
        "Generate Code",
        "Optimize Solution"
    ]
)



if st.button("⚡ Analyze Code"):


    if query:


        prompt = f"""

Mode:
{mode}


User Query:

{query}


Provide:

1. Explanation
2. Issues Found
3. Solution
4. Best Practices

"""


        with st.spinner(
            "NEXORA coding..."
        ):

            response = code_agent(
                prompt
            )


        st.success(
            "Analysis Complete"
        )


        st.markdown(
            "## 🤖 NEXORA RESPONSE"
        )

        st.write(response)



    else:

        st.warning(
            "Enter code/problem"
        )