import streamlit as st

from nexora_agents import planner_agent
from core.tasks import add_task, get_tasks, complete_task


st.set_page_config(
    page_title="Planner Nexus",
    page_icon="🎯",
    layout="wide"
)



st.title("🎯 Tactical Matrix")

st.caption(
    "NEXORA Planning & Execution Agent"
)



goal = st.text_area(
    "Enter your goal",
    placeholder="Example: Become a full stack developer in 6 months"
)



mode = st.selectbox(
    "Planning Mode",
    [
        "Daily Plan",
        "Weekly Plan",
        "Project Roadmap",
        "Goal Strategy"
    ]
)



if st.button("🚀 Generate Plan"):


    if goal:


        prompt = f"""

Goal:
{goal}

Planning Mode:
{mode}

Create:

1. Objective
2. Strategy
3. Tasks
4. Timeline
5. Success Metrics

"""


        with st.spinner(
            "NEXORA planning..."
        ):

            response = planner_agent(
                prompt
            )


        st.success(
            "Plan Generated ⚡"
        )


        st.markdown(
            "## 🎯 Execution Blueprint"
        )


        st.write(response)


        add_task(goal)



    else:

        st.warning(
            "Enter your goal"
        )




st.divider()


st.markdown(
    "## ✅ Task Tracker"
)


tasks = get_tasks()


for i, task in enumerate(tasks):


    col1, col2 = st.columns([4,1])


    with col1:

        status = "✅" if task["done"] else "⬜"

        st.write(
            status,
            task["task"]
        )


    with col2:

        if not task["done"]:

            if st.button(
                "Done",
                key=i
            ):

                complete_task(i)

                st.rerun()