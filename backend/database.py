import sqlite3
import os


DB = "cortexia.db"


def connect():
    return sqlite3.connect(DB)



def create_table():

    conn = connect()
    cursor = conn.cursor()


    # REPORTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        module TEXT,
        status TEXT,
        score INTEGER,
        summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # DOSSIER
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dossier(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cardio INTEGER,
        metabolic INTEGER,
        renal INTEGER,
        overall INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # RISK
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS risk_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        module TEXT,
        risk_level TEXT,
        score INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # RECORDS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medical_records(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        module TEXT,
        prediction TEXT,
        confidence INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conn.commit()
    conn.close()





def get_dossier():

    conn = connect()

    row = conn.execute(
    """
    SELECT cardio,metabolic,renal,overall
    FROM dossier
    ORDER BY id DESC
    LIMIT 1
    """
    ).fetchone()


    conn.close()


    if row:

        return {

        "cardio":row[0],
        "metabolic":row[1],
        "renal":row[2],
        "overall":row[3]

        }


    return {

        "cardio":92,
        "metabolic":86,
        "renal":89,
        "overall":90

    }





def save_report(
module,
status,
score,
summary=""
):

    conn=connect()

    conn.execute(
    """
    INSERT INTO reports
    (
    module,status,score,summary
    )
    VALUES(?,?,?,?)
    """,
    (
    module,
    status,
    score,
    summary
    )
    )

    conn.commit()
    conn.close()





def get_reports():

    conn=connect()

    data=conn.execute(
    """
    SELECT
    module,
    status,
    score,
    summary,
    created_at

    FROM reports

    ORDER BY id DESC
    """
    ).fetchall()


    conn.close()

    return data





def save_record(
module,
prediction,
confidence
):

    conn=connect()

    conn.execute(
    """
    INSERT INTO medical_records
    (
    module,
    prediction,
    confidence
    )
    VALUES(?,?,?)
    """,
    (
    module,
    prediction,
    confidence
    )
    )


    conn.commit()
    conn.close()





def get_records():

    conn=connect()

    data=conn.execute(
    """
    SELECT
    module,
    prediction,
    confidence,
    created_at

    FROM medical_records

    ORDER BY id DESC
    """
    ).fetchall()


    conn.close()

    return data






def save_risk(
module,
risk_level,
score
):

    conn=connect()

    conn.execute(
    """
    INSERT INTO risk_history
    (
    module,
    risk_level,
    score
    )
    VALUES(?,?,?)
    """,
    (
    module,
    risk_level,
    score
    )
    )

    conn.commit()
    conn.close()





def get_risks():

    conn=connect()

    data=conn.execute(
    """
    SELECT
    module,
    risk_level,
    score,
    created_at

    FROM risk_history

    ORDER BY id DESC
    """
    ).fetchall()


    conn.close()

    return data