/*
Status:
    - StatusID
    - Name
*/
CREATE TABLE Status (
    id   INTEGER NOT NULL PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(200) NOT NULL
);
/*
Pilot:
    - PilotID
    - Name
*/
CREATE TABLE Pilot (
    id   INTEGER NOT NULL PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(200) NOT NULL
);
/*
Continent:
    - ContinentID
    - Name
*/
CREATE TABLE Continent (
    id   NVARCHAR(200) NOT NULL PRIMARY KEY,
    name NVARCHAR(200) NOT NULL
);
/*
Country:
    - CountryCode
    - Name
    - ContinentID
*/
CREATE TABLE Country (
    code         NVARCHAR(200) NOT NULL PRIMARY KEY,
    name         NVARCHAR(200) NOT NULL,
    continent_id NVARCHAR(200) NOT NULL,
    FOREIGN KEY (continent_id) REFERENCES Continent(id)
);
/*
Airport:
    - AirportID
    - Name
    - CountryCode
*/
CREATE TABLE Airport (
    id           NVARCHAR(200) NOT NULL PRIMARY KEY,
    name         NVARCHAR(200) NOT NULL,
    country_code NVARCHAR(200) NOT NULL,
    FOREIGN KEY (country_code) REFERENCES Country(code)
);
/*
Passenger:
    - PassengerID
    - FirstName
    - LastName
    - Gender
    - Age
    - Nacionality
*/
CREATE TABLE Passenger (
    id          NVARCHAR(200) NOT NULL PRIMARY KEY,
    firstname   NVARCHAR(200) NOT NULL,
    lastname    NVARCHAR(200) NOT NULL,
    gender      NVARCHAR(200) NOT NULL,
    age         INTEGER NOT NULL,
    nationality NVARCHAR(200) NOT NULL
);
/*
Flight:
    - DepartureDate
    - PassengerID
    - AirportID
    - PilotID
    - StatusID
*/
CREATE TABLE Flight (
    departuredate DATE NOT NULL,
    passenger_id  NVARCHAR(200) NOT NULL,
    status_id     INTEGER NOT NULL,
    pilot_id      INTEGER NOT NULL,
    airport_id    NVARCHAR(200) NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES Passenger(id),
    FOREIGN KEY (status_id)    REFERENCES Status(id),
    FOREIGN KEY (pilot_id)     REFERENCES Pilot(id),
    FOREIGN KEY (airport_id)   REFERENCES Airport(id)
);