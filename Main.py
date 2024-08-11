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

cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
rows = cursor.fetchall()
for i in range(len(rows)):
    rows[i] = rows[i][0]

message = ''
if 'Flight' in rows:
    message += 'Tabla Flight Ya Existe'
if 'Passenger' in rows:
    message += '\nTabla Passenger Ya Existe'
if 'Airport' in rows:
    message += '\nTabla Airport Ya Existe'
if 'Country' in rows:
    message += '\nTabla Country Ya Existe'
if 'Continent' in rows:
    message += '\nTabla Continent Ya Existe'
if 'Pilot' in rows:
    message += '\nTabla Pilot Ya Existe'
if 'Status' in rows:
    message += '\nTabla Status Ya Existe'

print('Creación de Modelo')
if message == '':
    cursor.execute(open('./Scripts/LoadModel.sql', encoding = 'utf-8').read())
    cursor.commit()
    print(f'\033[32mTabla Flight Creada\nTabla Passenger Creada\nTabla Airport Creada\nTabla Country Creada\nTabla Continent Creada\nTabla Pilot Creada\nTabla Status Creada\n\033[0m')
else:
    print(f'\033[31m{message}\033[0m')

cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
rows = cursor.fetchall()
for i in range(len(rows)):
    rows[i] = rows[i][0]

message = ''
if 'Flight' in rows:
    message += 'Tabla Flight No Existe'
if 'Passenger' in rows:
    message += '\nTabla Passenger No Existe'
if 'Airport' in rows:
    message += '\nTabla Airport No Existe'
if 'Country' in rows:
    message += '\nTabla Country No Existe'
if 'Continent' in rows:
    message += '\nTabla Continent No Existe'
if 'Pilot' in rows:
    message += '\nTabla Pilot No Existe'
if 'Status' in rows:
    message += '\nTabla Status No Existe'

print('Eliminación de Modelo')
if message != '':
    cursor.execute(open('./Scripts/DeleteModel.sql', encoding = 'utf-8').read())
    cursor.commit()
    print(f'\033[32mTabla Flight Eliminada\nTabla Passenger Eliminada\nTabla Airport Eliminada\nTabla Country Eliminada\nTabla Continent Eliminada\nTabla Pilot Eliminada\nTabla Status Eliminada\n\033[0m')
else:
    print(f'\033[31m{message}\033[0m')

cursor.close()
conn.close()