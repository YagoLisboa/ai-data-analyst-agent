
import sqlite3
import pandas as pd

DB_PATH = "database/database.db"

def run_query(query):

    conn = sqlite3.connect(DB_PATH)

    try:
        df = pd.read_sql_query(query, conn)
        return df.to_string()
    except Exception as e:
        return str(e)
    finally:
        conn.close()
