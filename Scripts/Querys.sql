-- 1. SELECT COUNT(*) de todas las tablas para ver que si realizo la carga en las tablas del modelo
SELECT 'Status' AS TableName, COUNT(*) AS TotalRecords FROM Status
UNION ALL
SELECT 'Pilot', COUNT(*) FROM Pilot
UNION ALL
SELECT 'Continent', COUNT(*) FROM Continent
UNION ALL
SELECT 'Country', COUNT(*) FROM Country
UNION ALL
SELECT 'Airport', COUNT(*) FROM Airport
UNION ALL
SELECT 'Passenger', COUNT(*) FROM Passenger
UNION ALL
SELECT 'Flight', COUNT(*) FROM Flight;
-- --
-- 2. Porcentaje de pasajeros por género
SELECT
    gender Gender,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Passenger) Percentage
FROM Passenger
GROUP BY gender;
-- --
-- 3. Nacionalidades con su mes año de mayor fecha de salida
SELECT
    nationality Nationality,
    FORMAT(departuredate, 'MM-yyyy') 'Month-Year',
    COUNT(*) Flights
FROM Flight f
JOIN Passenger p ON f.passenger_id = p.id
GROUP BY nationality, FORMAT(departuredate, 'MM-yyyy')
ORDER BY nationality, 'Month-Year';
-- --
-- 4. Count de vuelos por país
SELECT
    c.name Country,
    COUNT(*) Flights
FROM Flight f
JOIN Airport a ON f.airport_id = a.id
JOIN Country c ON a.country_code = c.code
GROUP BY c.name;
-- --
-- 5. Top 5 aeropuertos con mayor número de pasajeros
SELECT TOP 5
    a.name Airport,
    COUNT(*) Passengers
FROM Flight f
JOIN Airport a ON f.airport_id = a.id
GROUP BY a.name
ORDER BY Passengers DESC;
-- --
-- 6. Count divido por estado de vuelo
SELECT
    s.name Status,
    COUNT(*) Flights
FROM Flight f
JOIN Status s ON f.status_id = s.id
GROUP BY s.name;
-- --
-- 7. Top 5 de los países más visitados
SELECT TOP 5
    c.name Country,
    COUNT(*) Flights
FROM Flight f
JOIN Airport a ON f.airport_id = a.id
JOIN Country c ON a.country_code = c.code
GROUP BY c.name
ORDER BY Flights DESC;
-- --
-- 8. Top 5 de los continentes más visitados
SELECT TOP 5
    con.name Continent,
    COUNT(*) Flights
FROM Flight f
JOIN Airport a ON f.airport_id = a.id
JOIN Country c ON a.country_code = c.code
JOIN Continent con ON c.continent_id = con.id
GROUP BY con.name
ORDER BY Flights DESC;
-- --
-- 9. Top 5 de edades divido por género que más viajan
SELECT TOP 5
    age Age,
    gender Gender,
    COUNT(*) Passengers
FROM Passenger
GROUP BY age, gender
ORDER BY Passengers DESC;
-- --
-- 10. Count de vuelos por MM-YYYY
SELECT
    FORMAT(departuredate, 'MM-yyyy') 'Month-Year',
    COUNT(*) Flights
FROM Flight
GROUP BY FORMAT(departuredate, 'MM-yyyy')
ORDER BY 'Month-Year';