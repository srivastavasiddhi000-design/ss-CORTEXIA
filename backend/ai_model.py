import sqlite3


def save_database_report(module, result):

    conn = sqlite3.connect("cortexia.db")

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO reports(

    module,
    status,
    score,
    message

    )

    VALUES(?,?,?,?)

    """,

    (

    module,
    result["status"],
    result["score"],
    result["message"]

    )

    )

    conn.commit()

    conn.close()