import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={os.getenv('DBHOST')};"
    f"Database={os.getenv('DBNAME')};"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT 'HOLA MUNDO' saludo;")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()