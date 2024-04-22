.mode column
.header ON

-- Try table remove to be safe
DROP TABLE IF EXISTS Womens_5000m_temp;
DROP TABLE IF EXISTS Mens_5000m_temp;
DROP TABLE IF EXISTS Womens_5000m;
DROP TABLE IF EXISTS Mens_5000m;
DROP TABLE IF EXISTS Countries_Continents;
DROP TABLE IF EXISTS Combined_Data_temp;
DROP TABLE IF EXISTS Combined_Data;

-- Create a schema
CREATE TABLE Countries_Continents (
        Country VARCHAR(30) PRIMARY KEY NOT NULL,
        Continent VARCHAR(20) NOT NULL
);

CREATE TABLE Womens_5000m_temp (
	Year INT NOT NULL,
	Location VARCHAR(20) NOT NULL,
	Position VARCHAR(5),
        Name VARCHAR(50) NOT NULL,
        Nationality VARCHAR(50),
        Time_Taken VARCHAR(10),
        Notes VARCHAR(5),
        FOREIGN KEY (Nationality) REFERENCES Countries_Continents (Country)
);

CREATE TABLE Mens_5000m_temp (
        Year INT NOT NULL,
        Location VARCHAR(20) NOT NULL,
        Position VARCHAR(5),
        Name VARCHAR(50) NOT NULL,
        Nationality VARCHAR(50),
        Time_Taken VARCHAR(10),
        Notes VARCHAR(5),
        FOREIGN KEY (Nationality) REFERENCES Countries_Continents (Country)
);

-- Import Data
.separator ','
.import countries_and_continents.csv Countries_Continents
.import olympics_5000m_data_women.csv Womens_5000m_temp
.import olympics_5000m_data_men.csv Mens_5000m_temp

ALTER TABLE Womens_5000m_temp
ADD COLUMN Gender VARCHAR(10);

UPDATE Womens_5000m_temp SET Gender = 'Women';

ALTER TABLE Mens_5000m_temp
ADD COLUMN Gender VARCHAR(10);

UPDATE Mens_5000m_temp SET Gender = 'Men';

CREATE TABLE Womens_5000m AS
SELECT
	Year,
	Location,
	Position,
	Name,
	Gender,
	Nationality,
	Time_Taken,
	Notes
FROM Womens_5000m_temp
WHERE Time_Taken GLOB '[0-9]*' AND Position GLOB '[0-9]*';

CREATE TABLE Mens_5000m AS
SELECT
        Year,
        Location,
        Position,
        Name,
        Gender,
        Nationality,
        Time_Taken,
        Notes
FROM Mens_5000m_temp
WHERE Time_Taken GLOB '[0-9]*' AND Position GLOB '[0-9]*';

CREATE TABLE Combined_Data_temp AS
SELECT * FROM Mens_5000m
UNION ALL
SELECT * FROM Womens_5000m;

CREATE TABLE Combined_Data AS
SELECT
	cd.Year,
	cd.Location,
	cd.Gender,
	cd.Position,
	cd.Name,
	cd.Nationality,
	cc.Continent,
	cd.Time_Taken,
	cd.Notes
FROM Combined_Data_temp cd
JOIN Countries_Continents cc ON cd.Nationality = cc.Country;

.mode csv
.output combined_data.csv

SELECT * FROM Combined_Data;

.output stdout

.mode box
-- Drop temporary tables
DROP TABLE IF EXISTS Womens_5000m_temp;
DROP TABLE IF EXISTS Mens_5000m_temp;
DROP TABLE IF EXISTS Combined_Data_temp;
