.mode column
.header ON

-- Try table remove to be safe
DROP TABLE IF EXISTS Womens_5000m_temp;
DROP TABLE IF EXISTS Mens_5000m_temp;
DROP TABLE IF EXISTS Womens_5000m;
DROP TABLE IF EXISTS Mens_5000m;

-- Create a schema
CREATE TABLE Womens_5000m_temp (
	Year INT NOT NULL,
	Location VARCHAR(20) NOT NULL,
	Position VARCHAR(5),
        Name VARCHAR(50) NOT NULL,
        Nationality VARCHAR(50),
        Time_Taken VARCHAR(10),
        Notes VARCHAR(5)
);

CREATE TABLE Mens_5000m_temp (
        Year INT NOT NULL,
        Location VARCHAR(20) NOT NULL,
        Position VARCHAR(5),
        Name VARCHAR(50) NOT NULL,
        Nationality VARCHAR(50),
        Time_Taken VARCHAR(10),
        Notes VARCHAR(5)
);

-- Import Data
.separator ','
.import olympics_5000m_data_women.csv Womens_5000m_temp
.import olympics_5000m_data_men.csv Mens_5000m_temp

-- Create final tables and transfer data with non-NULL Time_Taken values
CREATE TABLE Womens_5000m AS
SELECT * FROM Womens_5000m_temp WHERE Time_Taken IS NOT NULL;

CREATE TABLE Mens_5000m AS
SELECT * FROM Mens_5000m_temp WHERE Time_Taken GLOB '[0-9]*';

-- Drop temporary tables
DROP TABLE IF EXISTS Womens_5000m_temp;
DROP TABLE IF EXISTS Mens_5000m_temp;
