.mode column
.header ON

-- Try removing existing tables to be safe
DROP TABLE IF EXISTS Womens_temp;
DROP TABLE IF EXISTS Mens_temp;
DROP TABLE IF EXISTS Womens_Marathon;
DROP TABLE IF EXISTS Mens_Marathon;
DROP TABLE IF EXISTS Countries_Continents;
DROP TABLE IF EXISTS Combined_Data_temp;
DROP TABLE IF EXISTS Combined_Data;

-- Create a schema

CREATE TABLE Countries_Continents (
	Country VARCHAR(30) PRIMARY KEY NOT NULL,
	Continent VARCHAR(20) NOT NULL
);

CREATE TABLE Womens_temp (
        Year INT NOT NULL,
        Location VARCHAR(20) NOT NULL,
        Position VARCHAR(5),
        Name VARCHAR(50) NOT NULL,
        Nationality VARCHAR(50),
        Time_Taken VARCHAR(10),
        Notes VARCHAR(5),
        FOREIGN KEY (Nationality) REFERENCES Countries_Continents (Country)
);

CREATE TABLE Mens_temp (
        Year INT NOT NULL,
        Location VARCHAR(20) NOT NULL,
        Position VARCHAR(5),
        Name VARCHAR(50) NOT NULL,
        Nationality VARCHAR(50),
        Time_Taken VARCHAR(10),
        Notes VARCHAR(5),
        FOREIGN KEY (Nationality) REFERENCES Countries_Continents (Country)
);

-- Import data from csv files created in the webscraping
.separator ','
.import countries_and_continents.csv Countries_Continents
.import olympic_marathon_data_women.csv Womens_temp
.import olympic_marathon_data_men.csv Mens_temp

-- Modify schema to add a column with the gender
ALTER TABLE Womens_temp
ADD COLUMN Gender VARCHAR(10);

ALTER TABLE Mens_temp
ADD COLUMN Gender VARCHAR(10);

-- Add the gender to every row in new column
UPDATE Womens_temp SET Gender = 'Women';

UPDATE Mens_temp SET Gender = 'Men';

-- Create tables for the mens and women marathon data only adding rows which have a 
-- valid time and position in the Time_Taken and Position columns respectively.
-- This is done by checking if the values in these two columns start with a number
CREATE TABLE Womens_Marathon AS
SELECT
        Year,
        Location,
        Position,
        Name,
        Gender,
        Nationality,
        Time_Taken,
        Notes
FROM Womens_temp
WHERE Time_Taken GLOB '[0-9]*' AND Position GLOB '[0-9]*';

CREATE TABLE Mens_Marathon AS
SELECT
        Year,
        Location,
        Position,
        Name,
        Gender,
        Nationality,
        Time_Taken,
        Notes
FROM Mens_temp
WHERE Time_Taken GLOB '[0-9]*' AND Position GLOB '[0-9]*';

-- Create a combined table with data from the mens and womens
CREATE TABLE Combined_Data_temp AS
SELECT * FROM Mens_Marathon
UNION ALL
SELECT * FROM Womens_Marathon;

-- Create a final combined table including the contintents of the nationalities for each row
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

-- Chaning output mode to be able to write combined data into a csv file
.mode csv
.output olympic_marathon_combined_data.csv
SELECT * FROM Combined_Data;

-- Reset output mode
.output stdout
.mode box

-- Drop temporary tables
DROP TABLE IF EXISTS Womens_temp;
DROP TABLE IF EXISTS Mens_temp;
DROP TABLE IF EXISTS Combined_Data_temp;
