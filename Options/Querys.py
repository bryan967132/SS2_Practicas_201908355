from Options.Colors import Colors
from Options.Connection import Connection
from prettytable import PrettyTable

class Querys:
    def __init__(self, connection: Connection):
        self.connection: Connection = connection

    def writeReport(self, title, headers, data) -> str:
        table = PrettyTable()
        table.field_names = headers
        for d in data:
            table.add_row(d)
        return f'{title}\n{table.__str__()}'

    def start(self):
        cursor = self.connection.start()

        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
        rows = cursor.fetchall()
        for i in range(len(rows)):
            rows[i] = rows[i][0]

        isLoaded = True
        if any(table not in rows for table in ['Flight', 'Passenger', 'Airport', 'Country', 'Continent', 'Pilot', 'Status']):
            isLoaded = False

        data = {}
        c = 1
        if isLoaded:
            report = ''
            for q in open('./Scripts/Querys.sql', encoding = 'utf-8').read().split('-- --'):
                cursor.execute(q)
                rows = cursor.fetchall()
                if c == 1:
                    report += self.writeReport('1. Count De Todas Las Tablas', ['No', 'Table', 'Count'], rows)
                elif c == 2:
                    report += self.writeReport('\n\n2. Porcentaje De Pasajeros Por Género', ['Gender', 'Percentaje'], rows)
                elif c == 3:
                    report += self.writeReport('\n\n3. Nacionalidades Con Su Mes-Año De Mayor Fecha De Salida', ['No', 'Nationality', 'Month-Year', 'Flights'], rows)
                elif c == 4:
                    report += self.writeReport('\n\n4. Count De Vuelos Por País', ['Country', 'Flights'], rows)
                elif c == 5:
                    report += self.writeReport('\n\n5. Top 5 Aeropuertos Con Mayor Número De Pasajeros', ['Top', 'Airport', 'Passengers'], rows)
                elif c == 6:
                    report += self.writeReport('\n\n6. Count Divido Por Estado De Vuelo', ['Status', 'Flights'], rows)
                elif c == 7:
                    report += self.writeReport('\n\n7. Top 5 De Los Países Más Visitados', ['Top', 'Country', 'Flights'], rows)
                elif c == 8:
                    report += self.writeReport('\n\n8. Top 5 De Los Continentes Más Visitados', ['Top', 'Continent', 'Flights'], rows)
                elif c == 9:
                    report += self.writeReport('\n\n9. Top 5 De Edades Divido Por Género Que Más Viajan', ['Top', 'Age', 'Gender', 'Flights'], rows)
                elif c == 10:
                    report += self.writeReport('\n\n10. Count de vuelos por MM-YYYY', ['Month-Year', 'Flights'], rows)
                c += 1

            with open('./Reports/Report.txt', 'w', encoding = 'utf-8') as file:
                file.write(report)

            self.connection.close()
            return f'\n  Consultas\n{Colors.GREEN.value}  ¡Consultas Completadas!{Colors.WHITE.value}'
        else:
            self.connection.close()
            return f'\n  Consultas\n{Colors.RED.value}  ¡No hay un modelo cargado!{Colors.WHITE.value}'