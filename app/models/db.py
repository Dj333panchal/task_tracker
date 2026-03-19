import pyodbc

def get_connection():
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=TS-WIN-26;"
    "DATABASE=Task_Tracker;"
    "UID=flask_user;"
    "PWD=StrongPassword123;"
)
    return conn
