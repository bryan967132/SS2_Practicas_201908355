from Options.Colors import Colors
from Options.Connection import Connection

class Querys:
    def __init__(self, connection: Connection):
        self.connection: Connection = connection

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
        c = 0
        if isLoaded:
            report = ''
            for q in open('./Scripts/Querys.sql', encoding = 'utf-8').read().split('-- --'):
                cursor.execute(q)
                rows = cursor.fetchall()
                if c == 0:
                    report += 'Reporte1'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 1:
                    report += '\nReporte2'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 2:
                    report += '\nReporte3'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 3:
                    report += '\nReporte4'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 4:
                    report += '\nReporte5'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 5:
                    report += '\nReporte6'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 6:
                    report += '\nReporte7'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 7:
                    report += '\nReporte8'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 8:
                    report += '\nReporte9'
                    for r in rows:
                        report += f'{r}\n'
                elif c == 9:
                    report += '\nReporte10'
                    for r in rows:
                        report += f'{r}\n'
                c += 1

            with open('./Reportes.txt', 'w', encoding = 'utf-8') as file:
                file.write(report)

            self.connection.close()
            return {'status': 1,'response': f'\n  Consultas\n{Colors.GREEN.value}  ¡Consultas Completadas!{Colors.WHITE.value}', 'data': data}
        else:
            self.connection.close()
            return {'status': 0,'response': f'\n  Consultas\n{Colors.RED.value}  ¡No hay un modelo cargado!{Colors.WHITE.value}'}