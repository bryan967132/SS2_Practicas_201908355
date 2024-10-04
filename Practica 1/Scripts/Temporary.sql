IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME = 'TemporaryTable')
BEGIN
    CREATE TABLE TemporaryTable(
		PassengerID        NVARCHAR(200) NOT NULL,
		FirstName          NVARCHAR(200) NOT NULL,
		LastName           NVARCHAR(200) NOT NULL,
		Gender             NVARCHAR(200) NOT NULL,
		Age                NVARCHAR(200) NOT NULL,
		Nationality        NVARCHAR(200) NOT NULL,
		AirportName        NVARCHAR(200) NOT NULL,
		AirportCountryCode NVARCHAR(200) NOT NULL,
		CountryName        NVARCHAR(200) NOT NULL,
		AirportContinent   NVARCHAR(200) NOT NULL,
		Continents         NVARCHAR(200) NOT NULL,
		DepartureDate      NVARCHAR(200) NOT NULL,
		ArrivalAirport     NVARCHAR(200) NOT NULL,
		PilotName          NVARCHAR(200) NOT NULL,
		FlightStatus       NVARCHAR(200) NOT NULL
	);
END

-- DROP TABLE ##TemporaryTable;