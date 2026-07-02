import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def groq_chat(prompt):

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content