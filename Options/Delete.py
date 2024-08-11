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

        self.connection.close()