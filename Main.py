import pyodbc

# Configura los parámetros de conexión con autenticación integrada
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Practica1;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()