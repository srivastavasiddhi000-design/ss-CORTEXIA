import json
import os


FILE = "data/tasks.json"



def load_tasks():

    if not os.path.exists(FILE):
        return []

    try:

        with open(FILE,"r") as f:
            return json.load(f)

    except:
        return []




def add_task(task):

    tasks = load_tasks()

    tasks.append(
        {
            "task": task,
            "done": False
        }
    )


    with open(FILE,"w") as f:
        json.dump(
            tasks,
            f,
            indent=4
        )



def complete_task(index):

    tasks = load_tasks()

    if index < len(tasks):

        tasks[index]["done"] = True


    with open(FILE,"w") as f:
        json.dump(
            tasks,
            f,
            indent=4
        )



def get_tasks():

    return load_tasks()