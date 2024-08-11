import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

class Connection:
    def start(self) -> pyodbc.Cursor:
        self.__conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            f"Server={os.getenv('DBHOST')};"
            f"Database={os.getenv('DBNAME')};"
            "Trusted_Connection=yes;"
        )
        return self.__conn.cursor()

    def close(self):
        self.__conn.close()