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
                cursor.execute("""WITH FilteredCountries AS (
                                    SELECT
                                        T1.AirportCountryCode,
                                        T1.CountryName,
                                        T1.AirportContinent,
                                        ROW_NUMBER() OVER (PARTITION BY T1.AirportCountryCode ORDER BY (SELECT NULL)) AS rn
                                    FROM TemporaryTable T1
                                    WHERE T1.AirportCountryCode NOT LIKE '%[^a-zA-Z ]%' AND LEN(T1.AirportCountryCode) <= 4
                                    AND T1.AirportContinent NOT LIKE '%[^a-zA-Z ]%' AND LEN(T1.AirportContinent) <= 4
                                    AND T1.CountryName NOT LIKE '%[^a-zA-Z ]%'
                                    AND EXISTS (
                                        SELECT * FROM Continent C WHERE C.id = T1.AirportContinent
                                    )
                                )
                                INSERT INTO Country(code, name, continent_id) SELECT
                                    T2.AirportCountryCode,
                                    T2.CountryName,
                                    T2.AirportContinent
                                FROM FilteredCountries T2
                                WHERE T2.rn = 1;""")
                cursor.commit()
            except Exception as e:
                print(e)

            # Airport
            try:
                cursor.execute("""WITH FilteredAirports AS (
                                    SELECT
                                        T1.ArrivalAirport,
                                        T1.AirportName,
                                        T1.AirportCountryCode,
                                        ROW_NUMBER() OVER (PARTITION BY T1.ArrivalAirport ORDER BY (SELECT NULL)) AS rn
                                    FROM TemporaryTable T1
                                    WHERE T1.ArrivalAirport NOT LIKE '%[^a-zA-Z ]%'
                                    AND T1.AirportName NOT LIKE '%[^a-zA-Z ]%'
                                    AND T1.AirportCountryCode NOT LIKE '%[^a-zA-Z ]%'
                                    AND EXISTS(
                                        SELECT * FROM Country C WHERE C.code = T1.AirportCountryCode
                                    )
                                )
                                INSERT INTO Airport(id, name, country_code) SELECT
                                    T2.ArrivalAirport,
                                    T2.AirportName,
                                    T2.AirportCountryCode
                                FROM FilteredAirports T2
                                WHERE T2.rn = 1;""")
                cursor.commit()
            except:
                pass

            # Passenger
            try:
                cursor.execute("""WITH FilteredPassengers AS (
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
                                FROM FilteredPassengers
                                WHERE rn = 1;""")
                cursor.commit()
            except Exception as e:
                print(e)

            # Flight
            try:
                cursor.execute("""INSERT INTO Flight(departuredate ,passenger_id ,status_id ,pilot_id ,airport_id) SELECT * FROM (
                                    SELECT
                                        CASE 
                                            WHEN CHARINDEX('/', T1.DepartureDate) > 0 THEN 
                                                TRY_CONVERT(DATE, T1.DepartureDate, 101) -- 101 = MM/DD/YYYY
                                            WHEN CHARINDEX('-', T1.DepartureDate) > 0 THEN 
                                                TRY_CONVERT(DATE, T1.DepartureDate, 110) -- 110 = MM-DD-YYYY
                                            ELSE NULL
                                        END AS DepartureDate,
                                        P.id PassengerID,
                                        S.id StatusID,
                                        PL.id PilotID,
                                        A.id AirportID
                                    FROM TemporaryTable T1
                                    INNER JOIN Passenger P ON P.firstname = T1.FirstName AND P.lastname = T1.LastName AND P.gender = T1.Gender AND P.age = T1.Age AND P.nationality = T1.Nationality
                                    INNER JOIN Status    S ON S.name = T1.FlightStatus
                                    INNER JOIN Pilot     PL ON PL.name = T1.PilotName
                                    INNER JOIN Airport   A ON A.name = T1.AirportName
                                ) T2
                                WHERE T2.DepartureDate IS NOT NULL;""")
                cursor.commit()
            except Exception as e:
                print(e)

            cursor.execute('DROP TABLE TemporaryTable;')
            cursor.commit()
            return f'\n  Cargar Información\n{Colors.GREEN.value}  ¡Información Cargada!{Colors.WHITE.value}'
        except Exception as e:
            print(e)
            return f'\n  Cargar Información\n{Colors.RED.value}  ¡Ha Ocurrido Un Error!{Colors.WHITE.value}'