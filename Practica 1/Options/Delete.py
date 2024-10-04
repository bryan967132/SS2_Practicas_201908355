from Options.Colors import Colors
from Options.Connection import Connection

class Delete:
    def __init__(self, connection: Connection):
        self.connection: Connection = connection

    def start(self):
        cursor = self.connection.start()

        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
        rows = cursor.fetchall()
        for i in range(len(rows)):
            rows[i] = rows[i][0]

        message = ''
        if not 'Flight' in rows:
            message += '\n  Tabla Flight No Existe'
        if not 'Passenger' in rows:
            message += '\n  Tabla Passenger No Existe'
        if not 'Airport' in rows:
            message += '\n  Tabla Airport No Existe'
        if not 'Country' in rows:
            message += '\n  Tabla Country No Existe'
        if not 'Continent' in rows:
            message += '\n  Tabla Continent No Existe'
        if not 'Pilot' in rows:
            message += '\n  Tabla Pilot No Existe'
        if not 'Status' in rows:
            message += '\n  Tabla Status No Existe'

        if message == '':
            cursor.execute(open('./Scripts/DeleteModel.sql', encoding = 'utf-8').read())
            cursor.commit()
            message = f'{Colors.GREEN.value}\n  Tabla Flight Eliminada\n  Tabla Passenger Eliminada\n  Tabla Airport Eliminada\n  Tabla Country Eliminada\n  Tabla Continent Eliminada\n  Tabla Pilot Eliminada\n  Tabla Status Eliminada{Colors.WHITE.value}'
        else:
            message = f'{Colors.RED.value}{message}{Colors.WHITE.value}'

        self.connection.close()

        return '\n  Eliminación de Modelo' + message