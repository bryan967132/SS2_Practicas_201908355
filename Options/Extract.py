from Options.Colors import Colors
from Options.Connection import Connection

class Extract:
    def __init__(self, connection: Connection):
        self.connection: Connection = connection

    def start(self, path):
        try:
            cursor = self.connection.start()

            cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
            rows = cursor.fetchall()
            for i in range(len(rows)):
                rows[i] = rows[i][0]

            isLoaded = True
            if any(table not in rows for table in ['Flight', 'Passenger', 'Airport', 'Country', 'Continent', 'Pilot', 'Status']):
                isLoaded = False

            if isLoaded:
                cursor.execute(open('./Scripts/Temporary.sql', encoding = 'utf-8').read())
                cursor.commit()

                cursor.execute(f'BULK INSERT TemporaryTable FROM \'{path}\' WITH (FIELDTERMINATOR = \',\',ROWTERMINATOR = \'\\n\',FIRSTROW = 2);')
                cursor.commit()
                self.connection.close()
                return f'\n  Extraer Información\n{Colors.GREEN.value}  ¡Información Extraida!{Colors.WHITE.value}'
            self.connection.close()
            return f'\n  Extraer Información\n{Colors.RED.value}  ¡No hay un modelo cargado!{Colors.WHITE.value}'
        except Exception as e:
            print(e)
            return f'\n  Extraer Información\n{Colors.RED.value}  ¡Ha Ocurrido Un Error!{Colors.WHITE.value}'

# ./Data/VuelosDataSet.csv
# C:\Users\bryan\Documents\USAC\Semi2\Lab\Practica1\Data\VuelosDataSet.csv