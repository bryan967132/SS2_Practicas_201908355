from Options.Colors import Colors
from Options.Connection import Connection

class Create:
    def __init__(self, connection: Connection):
        self.connection: Connection = connection

    def start(self):
        cursor = self.connection.start()

        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
        rows = cursor.fetchall()
        for i in range(len(rows)):
            rows[i] = rows[i][0]

        message = ''
        if 'Flight' in rows:
            message += '  Tabla Flight Ya Existe'
        if 'Passenger' in rows:
            message += '\n  Tabla Passenger Ya Existe'
        if 'Airport' in rows:
            message += '\n  Tabla Airport Ya Existe'
        if 'Country' in rows:
            message += '\n  Tabla Country Ya Existe'
        if 'Continent' in rows:
            message += '\n  Tabla Continent Ya Existe'
        if 'Pilot' in rows:
            message += '\n  Tabla Pilot Ya Existe'
        if 'Status' in rows:
            message += '\n  Tabla Status Ya Existe'

        print('  Creación de Modelo')
        if message == '':
            cursor.execute(open('./Scripts/LoadModel.sql', encoding = 'utf-8').read())
            cursor.commit()
            print(f'{Colors.GREEN.value}  Tabla Flight Creada\n  Tabla Passenger Creada\n  Tabla Airport Creada\n  Tabla Country Creada\n  Tabla Continent Creada\n  Tabla Pilot Creada\n  Tabla Status Creada\n  {Colors.WHITE.value}')
        else:
            print(f'{Colors.RED.value}{message}{Colors.WHITE.value}')

        self.connection.close()