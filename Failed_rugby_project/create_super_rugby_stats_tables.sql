.mode column
.header ON

-- Try table remove to be safe
DROP TABLE IF EXISTS Attack;
DROP TABLE IF EXISTS Kicking;
DROP TABLE IF EXISTS Defence;
DROP TABLE IF EXISTS Ladder;

-- Create a schema

CREATE TABLE Attack (
	Name VARCHAR(50) NOT NULL PRIMARY KEY,
	Club VARCHAR(50),
	Games INT,
	Tries INT,
	TryAssists INT,
	Points INT,
	Possessions INT,
	Runs INT,
	RunMetres INT,
	PickAndDrives INT,
	LineBreaks INT,
	LBAssists INT,
	TackleBusts INT,
	Offloads INT,
	Passes INT,
	LineoutWinsOwn INT,
	LineoutWinsOpp INT,
	Kicks INT,
	KickMetres INT,
	KickErrors INT
--	FOREIGN KEY Club REFERENCES Teams (Abbrevation)
);

CREATE TABLE Kicking (
	Name VARCHAR(5) NOT NULL PRIMARY KEY,
	Club VARCHAR(30),
	Games INT,
	Conversions INT,
	DropGoals INT,
	Kicks INT,
	PenaltyGoals INT,
	Points INT,
	KickMetres INT,
	KickErrors INT,
	ConversionAttempts INT,
	PenaltyGoalAttempts INT,
	DropGoalPercent FLOAT,
	GoalKickingPercent FLOAT,
	DropGoalAttempts INT
);

CREATE TABLE Defence (
	Name VARCHAR(50) NOT NULL PRIMARY KEY,
	Club VARCHAR(50),
	Games INT,
	HandlingErrors INT,
	YellowCards INT,
	Tackles INT,
	Pilfers INT,
	Turnovers INT,
	PenaltiesConceded INT,
	RedCards INT,
	MissedTackles INT,
	IneffectiveTackles INT,
	ForcedRuckAndMaulPenalties INT,
	TackleEfficiency FLOAT,
	ForcedPenalties INT
);

CREATE TABLE Ladder(
	Rank INT,
	Team VARCHAR (20) NOT NULL PRIMARY KEY,
	Games INT,
	Won INT,
	Drawn INT,
	Lost INT,
	BonusPoints INT,
	PointDifference INT,
	Points INT
);

-- Import Data
.separator ','
.import --skip 1 super_rugby_attack_data.csv Attack
.import --skip 1 super_rugby_kicking_data.csv Kicking
.import --skip 1 super_rugby_defence_data.csv Defence
.import --skip 1 super_rugby_ladder.csv Ladder
