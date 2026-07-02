import json
import os
from datetime import datetime


FILE = "data/memory.json"



def load_memory():

    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)

    except:
        return []




def save_memory(agent, message):

    memory = load_memory()


    memory.append(
        {
            "agent": agent,
            "message": message.strip(),
            "time": str(datetime.now())
        }
    )


    with open(FILE, "w") as f:
        json.dump(
            memory,
            f,
            indent=4
        )




def recall_memory(agent=None):

    memory = load_memory()


    if agent:

        memory = [
            m for m in memory
            if m.get("agent") == agent
        ]


    return memory[-5:]