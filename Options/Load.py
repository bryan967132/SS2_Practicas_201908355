from Options.Colors import Colors
from Options.Connection import Connection

class Load:
    def __init__(self, connection: Connection):
        self.connection: Connection = connection

    def start(self):
        try:
            cursor = self.connection.start()
            # status
            try:
                cursor.execute("INSERT INTO Status(name) SELECT DISTINCT FlightStatus FROM TemporaryTable WHERE CHARINDEX(',', FlightStatus) = 0;")
                cursor.commit()
            except:
                pass

            # Pilot
            try:
                cursor.execute("INSERT INTO Pilot(name) SELECT DISTINCT PilotName FROM TemporaryTable WHERE PilotName NOT LIKE '%[^a-zA-Z ]%';")
                cursor.commit()
            except:
                pass

            # Continent
            try:
                cursor.execute("INSERT INTO Continent(id, name) SELECT DISTINCT AirportContinent, Continents FROM TemporaryTable WHERE AirportContinent NOT LIKE '%[^a-zA-Z ]%' AND LEN(AirportContinent) <= 4;")
                cursor.commit()
            except:
                pass


            # Country
            try:
                cursor.execute("""SELECT DISTINCT T1.AirportCountryCode, T1.CountryName, T1.AirportContinent FROM TemporaryTable T1
                                    WHERE T1.AirportCountryCode NOT LIKE '%[^a-zA-Z ]%' AND LEN(T1.AirportCountryCode) <= 4
                                    AND T1.CountryName NOT LIKE '%[^a-zA-Z ]%' AND T1.AirportContinent NOT LIKE '%[^a-zA-Z ]%'
                                    AND EXISTS (SELECT DISTINCT T.AirportContinent, T.Continents FROM TemporaryTable AS T WHERE T.AirportContinent NOT LIKE '%[^a-zA-Z ]%' AND LEN(T.AirportContinent) <= 4 AND T1.AirportContinent = T.AirportContinent);""")
                rows = cursor.fetchall()
                aux = []
                values = ''
                for r in rows:
                    if not r[0] in aux:
                        aux.append(r[0])
                        values += (',' if values != '' else '') + f'({r[0], r[1]})'
                if len(aux) > 0:
                    cursor.execute(f'INSERT INTO Country(code,name,continent_id) VALUES {values};')
                    cursor.commit()
            except Exception as e:
                print(e)

            # Airport
            try:
                cursor.execute("""SELECT DISTINCT ArrivalAirport, AirportName, AirportCountryCode FROM TemporaryTable
                                    WHERE ArrivalAirport NOT LIKE '%[^a-zA-Z ]%'
                                    AND EXISTS (
                                        SELECT DISTINCT T1.AirportCountryCode, T1.CountryName, T1.AirportContinent FROM TemporaryTable T1
                                        WHERE T1.AirportCountryCode NOT LIKE '%[^a-zA-Z ]%' AND LEN(T1.AirportCountryCode) <= 4
                                        AND EXISTS (SELECT DISTINCT T.AirportContinent, T.Continents FROM TemporaryTable AS T WHERE T.AirportContinent NOT LIKE '%[^a-zA-Z ]%' AND LEN(T.AirportContinent) <= 4 AND T1.AirportContinent = T.AirportContinent)
                                        AND AirportCountryCode = T1.AirportCountryCode
                                    );""")
                rows = cursor.fetchall()
            except:
                pass

            # Passenger
            try:
                cursor.execute("""WITH RankedPassengers AS (
                                    SELECT
                                        PassengerID,
                                        FirstName,
                                        LastName,
                                        Gender,
                                        Age,
                                        Nationality,
                                        ROW_NUMBER() OVER (PARTITION BY PassengerID ORDER BY (SELECT NULL)) AS rn
                                    FROM TemporaryTable
                                )
                                INSERT INTO Passenger(id, firstname, lastname, gender, age, nationality) SELECT
                                    PassengerID,
                                    FirstName,
                                    LastName,
                                    Gender,
                                    Age,
                                    Nationality
                                FROM RankedPassengers
WHERE rn = 1;""")
            except Exception as e:
                print(e)
            
            # cursor.execute('DROP TABLE TemporaryTable;')
            # cursor.commit()
            return f'\n  Cargar Información\n{Colors.GREEN.value}  ¡Información Cargada!{Colors.WHITE.value}'
        except Exception as e:
            print(e)
            return f'\n  Cargar Información\n{Colors.RED.value}  ¡Ha Ocurrido Un Error!{Colors.WHITE.value}'