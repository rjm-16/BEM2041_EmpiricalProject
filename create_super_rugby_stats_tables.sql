.mode column
.width 25 5
.header ON

-- Try table remove to be safe
DROP TABLE IF EXISTS attack;
DROP TABLE IF EXISTS kicking;
DROP TABLE IF EXISTS defence;

-- Create a schema
CREATE TABLE attack (
    Name VARCHAR(50) NOT NULL PRIMARY KEY,
    Club VARCHAR(50),
    Games INT,
    Runs INT,
    Linebreaks INT,
    Offloads INT,
    Kicks INT,
    Tries INT,
    Points INT,
    RunMetres INT,
    TackleBusts INT,
    KickMetres INT,
    TryAssists INT,
    Possession INT,
    Passes INT,
    LineoutWinsOwn INT,
    PickAndDrives INT,
    LBAssists INT,
    LineoutWinsOpp INT,
    KickErrors INT
);

CREATE TABLE kicking (
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

CREATE TABLE defence (
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

-- Import Data
.separator ','
.import --skip 1 super_six_attack_data.csv attack
.import --skip 1 super_six_kicking_data.csv kicking
.import --skip 1 super_six_defence_data.csv defence
