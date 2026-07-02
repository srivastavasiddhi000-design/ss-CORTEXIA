import streamlit as st
from pypdf import PdfReader

from nexora_agents import knowledge_agent
from core.rag import chunk_text, retrieve_context


st.set_page_config(
    page_title="Knowledge Nexus",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 Knowledge Repository")

st.caption(
    "NEXORA Knowledge Intelligence Agent"
)



uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


question = st.text_area(
    "Ask from your document",
    placeholder="Explain this document"
)



chunks = []



if uploaded_file:

    reader = PdfReader(
        uploaded_file
    )


    text = ""


    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text



    chunks = chunk_text(text)


    st.success(
        f"PDF processed: {len(chunks)} chunks created"
    )




if st.button("⚡ Analyze"):


    if question:


        if chunks:

            context = retrieve_context(
                chunks,
                question
            )


            final_prompt = f"""

You are analyzing a PDF document.

Relevant Context:

{context}


Question:

{question}


Give:

1. Summary
2. Important Points
3. Explanation
4. Conclusion

"""


        else:

            final_prompt = question




        with st.spinner(
            "NEXORA analyzing..."
        ):

            response = knowledge_agent(
                final_prompt
            )


        st.markdown(
            "## 🤖 NEXORA RESPONSE"
        )

        st.write(response)



    else:

        st.warning(
            "Ask a question"
        )