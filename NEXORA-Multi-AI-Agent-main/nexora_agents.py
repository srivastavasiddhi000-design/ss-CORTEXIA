from core.llm import groq_chat
from core.memory import recall_memory, save_memory
from search import web_search


def research_agent(query):

    memory = recall_memory("Research")

    sources = web_search(query)

    prompt = f"""
You are NEXORA Research Agent.

Previous Memory:
{memory}

Web Sources:
{sources}

User Query:
{query}

Create a detailed research report.
"""

    response = groq_chat(prompt)

    save_memory("Research", query)

    return response



def knowledge_agent(query):

    return groq_chat(query)



def planner_agent(query):

    return groq_chat(query)



def code_agent(query):

    return groq_chat(query)