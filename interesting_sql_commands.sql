.mode box

SELECT COUNT(*) FROM Mens_5000m;
SELECT COUNT(*) FROM Womens_5000m;

SELECT * FROM Womens_5000m WHERE Notes == 'OR' or Notes == 'WR' UNION SELECT * FROM Mens_5000m WHERE Notes == 'OR' or Notes == 'WR';

-- Runners who have finished in final multiple times
SELECT Name, Nationality, Gender, Year AS First_Final, COUNT(Name) AS Appearances
FROM Mens_5000m
GROUP BY Name
HAVING Appearances > 1
ORDER BY Appearances DESC;

-- Winners by Nationality and number of wins
SELECT Gender, Position, Nationality, COUNT(Nationality) AS Wins, GROUP_CONCAT(Year) AS Years
FROM Combined_Data
WHERE Position == '1'
GROUP BY Nationality, Gender
ORDER BY Gender, Wins DESC, Years;

-- Winners by Individual and number of wins
SELECT Gender, Position, Name, Nationality, COUNT(Name) AS Wins, GROUP_CONCAT(Year) AS Years
FROM Combined_Data
WHERE Position == '1'
GROUP BY Name, Gender
ORDER BY Gender, Wins DESC, Years;
