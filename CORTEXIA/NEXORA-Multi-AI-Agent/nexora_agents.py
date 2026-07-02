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


# ==========================================
# MEDICAL SPECIALIST AGENT
# ==========================================

def medical_specialist_agent(specialist, query):

    prompt = f"""
You are an expert {specialist} with extensive clinical knowledge.

Your role is to provide medically accurate, evidence-based educational guidance.

Rules:

- Respond professionally and clearly.
- Explain the condition in simple language.
- Suggest healthy lifestyle practices where appropriate.
- Do not provide definitive diagnoses.
- Do not prescribe prescription medications.
- Mention when urgent medical attention may be necessary.
- Encourage consultation with a qualified healthcare professional for diagnosis and treatment.

Patient Question:

{query}
"""

    return groq_chat(prompt)