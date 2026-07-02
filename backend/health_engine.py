def analyze(data):
    
    score = 100


    # =====================
    # HEART
    # =====================

    if "Blood Pressure" in data:

        bp = data["Blood Pressure"]

        if bp >= 180:
            score -= 25

        elif bp >= 140:
            score -= 10



    if "Heart Rate" in data:

        hr = data["Heart Rate"]

        if hr >= 120 or hr <= 45:
            score -= 15




    if "Cholesterol" in data:

        ch = data["Cholesterol"]

        if ch >= 260:
            score -= 20

        elif ch >= 220:
            score -= 10




    # =====================
    # DIABETES
    # =====================

    if "Glucose" in data:

        g = data["Glucose"]

        if g >= 200:
            score -= 25

        elif g >= 140:
            score -= 10



    if "HbA1c" in data:

        h = data["HbA1c"]

        if h >= 8:
            score -= 25

        elif h >= 6.5:
            score -= 10



    if "BMI" in data:

        bmi = data["BMI"]

        if bmi >= 35:
            score -= 15

        elif bmi >= 30:
            score -= 5





    # =====================
    # LUNG
    # =====================


    if "Oxygen Level" in data:

        oxygen = data["Oxygen Level"]

        if oxygen < 90:
            score -= 30

        elif oxygen < 94:
            score -= 15



    if "Respiratory Rate" in data:

        rate = data["Respiratory Rate"]

        if rate > 28:
            score -= 20

        elif rate > 22:
            score -= 10




    if "Lung Capacity" in data:

        cap = data["Lung Capacity"]

        if cap < 50:
            score -= 25

        elif cap < 70:
            score -= 10




    if "Smoking" in data:

        if data["Smoking"] == 1:
            score -= 10




    if "Cough Duration" in data:

        if data["Cough Duration"] > 14:
            score -= 10




    if "Breathlessness Level" in data:

        level = data["Breathlessness Level"]

        if level >= 7:
            score -= 20

        elif level >= 4:
            score -= 10




    if "Chest Pain" in data:

        if data["Chest Pain"] == 1:
            score -= 15





    # =====================
    # KIDNEY
    # =====================

    if "Creatinine" in data:

        cr = data["Creatinine"]

        if cr > 3:
            score -= 30

        elif cr > 1.5:
            score -= 15





    # =====================
    # CANCER
    # =====================

    if "Tumor Marker" in data:

        tm = data["Tumor Marker"]

        if tm > 10:
            score -= 30

        elif tm > 5:
            score -= 15





    score = max(0, min(100, int(score)))



    if score >= 80: 
        risk = "LOW"

    elif score >= 50:
        risk = "MODERATE"

    else:
        risk = "HIGH"



    return {

        "score": score,

        "risk": risk

    }