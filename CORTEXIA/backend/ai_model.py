import json



def create_summary(result):


    summary = {


        "module":
        "CORTEXIA Neural Health System",


        "analysis":
        "AI Clinical Assessment",


        "risk":
        result["risk"],


        "score":
        result["score"],


        "status":
        result["status"]


    }


    return summary





def save_report(data):


    with open(
        "health_report.json",
        "w"
    ) as file:


        json.dump(
            data,
            file,
            indent=4
        )


    return True