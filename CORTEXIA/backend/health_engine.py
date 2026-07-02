def analyze(data):
    
    score = 0


    for value in data.values():

        if isinstance(value,(int,float)):

            score += value



    score = int(score)%100



    if score > 80:

        risk="LOW"


    elif score > 50:

        risk="MODERATE"


    else:

        risk="HIGH"



    return {

        "score":score,

        "risk":risk,

        "status":"Analysis Completed"

    }



def predict_heart(data):

    return analyze(data)


def predict_lung(data):

    return analyze(data)


def predict_kidney(data):

    return analyze(data)


def predict_diabetes(data):

    return analyze(data)


def predict_cancer(data):

    return analyze(data)


def predict_cycle(data):

    return analyze(data)