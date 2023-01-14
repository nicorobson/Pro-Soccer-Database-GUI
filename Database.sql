DROP TABLE p_Performance;
DROP TABLE t_Performance;
DROP TABLE plays_For;
DROP TABLE registered_In;
DROP TABLE held_In;
DROP TABLE player_Statistics;
DROP TABLE player_Information;
DROP TABLE team_Statistics;
DROP TABLE team_Information;
DROP TABLE scores;
DROP TABLE league_Information;

--------------------------------Tables for the entities
-- Table for league_Information which has a primary key
CREATE TABLE league_Information (
    League_Name VARCHAR2(30) NOT NULL,
    Division NUMBER,
    Region VARCHAR2(10),
    PRIMARY KEY (League_Name)
);
-- Table for scores which has a primary key and a foreign key from league_Information
CREATE TABLE scores (
    Fixture VARCHAR2(10) NOT NULL,
    Home_Team VARCHAR2(20),
    Away_Team VARCHAR2(20),
    Match_Result VARCHAR2(6),
    Stadium VARCHAR2(20),
    Match_Date VARCHAR2(20),
    League_Name VARCHAR2(30),
    PRIMARY KEY (Fixture),
    FOREIGN KEY (League_Name)
    REFERENCES league_Information(League_Name)
);
-- Table for team_Information which has a primary key and a foreign key from league_Information
CREATE TABLE team_Information (
    Team_Name VARCHAR2(20) NOT NULL,
    City VARCHAR2(20),
    Home_Stadium VARCHAR2(20),
    League_Name VARCHAR2(30),
    PRIMARY KEY (Team_Name),
    FOREIGN KEY (League_Name) 
    REFERENCES league_Information(League_Name)
);
-- Table for team_Statistics which has a primary key and a foreign key from team_Information
CREATE TABLE team_Statistics (
    Team_Ranking NUMBER NOT NULL,
    Team_Name VARCHAR2(20),
    Points NUMBER,
    Games_Played NUMBER,
    Wins NUMBER,
    Losses NUMBER,
    Draws NUMBER,
    Total_Goals NUMBER,
    PRIMARY KEY (Team_Ranking),
    FOREIGN KEY (Team_Name)
    REFERENCES team_Information(Team_Name)
); 
-- Table for player_Information which has a primary key and a foreign key from team_Information
CREATE TABLE player_Information (
    Player_Name VARCHAR2(30) NOT NULL,
    Age NUMBER,
    Height VARCHAR2(10), 
    Player_Position VARCHAR2(30),
    Team_Name VARCHAR2(20),
    PRIMARY KEY (Player_Name),
    FOREIGN KEY (Team_Name)
    REFERENCES team_Information(Team_Name)
);
-- Table for player_Statistics which has a primary key and a foreign key from player_Information
CREATE TABLE player_Statistics (
    Player_ID NUMBER NOT NULL,
    Player_Name VARCHAR2(30),
    Goals NUMBER,
    Assists NUMBER,
    Matches_Played NUMBER,
    PRIMARY KEY (Player_ID),
    FOREIGN KEY (Player_Name)
    REFERENCES player_Information(Player_Name)
);
--------------------------- Tables for the relationships between the above entities
-- Table for relationship between league_Information and scores
-- has 2 primary keys and 2 foreign keys for each respective entity
CREATE TABLE held_In (
    Fixture VARCHAR2(10) NOT NULL REFERENCES scores(Fixture),
    League_Name VARCHAR2(30) NOT NULL REFERENCES league_Information(League_Name),
    PRIMARY KEY (Fixture, League_Name)
);
-- Table for relationship between league_Information and team_Information
-- has 2 primary keys and 2 foreign keys for each respective entity
CREATE TABLE registered_In ( 
    Team_Name VARCHAR2(20) NOT NULL REFERENCES team_Information(Team_Name),
    League_Name VARCHAR2(30) NOT NULL REFERENCES league_Information(League_Name),
    PRIMARY KEY(Team_Name, League_Name)
);
-- Table for relationship between team_Information and player_Information
-- has 2 primary keys and 2 foreign keys for each respective entity
CREATE TABLE plays_For ( 
    Player_Name VARCHAR2(30) NOT NULL REFERENCES player_Information(Player_Name),
    Team_Name VARCHAR2(20) NOT NULL REFERENCES team_Information(Team_Name),
    PRIMARY KEY (Player_Name, Team_Name)
);
-- Table for relationship between team_Information and team_Statistics
-- has 2 primary keys for each respective entity
CREATE TABLE t_Performance (
    Team_Name VARCHAR2(20) NOT NULL REFERENCES team_Information(Team_Name), 
    Team_Ranking NUMBER NOT NULL REFERENCES team_Statistics(Team_Ranking),
    PRIMARY KEY (Team_Name, Team_Ranking)
);
-- Table for relationship between player_Information and player_Statistics
-- has 2 primary keys for each respective entity
CREATE TABLE p_Performance (
    Player_Name VARCHAR2(30) NOT NULL REFERENCES player_Information(Player_Name),
    Player_ID NUMBER NOT NULL REFERENCES player_Statistics(Player_ID),
    PRIMARY KEY (Player_Name, Player_ID) 
);


-----------------------------A4 part A
-- INSERT statements to fill in the entity tables so we can test queries on them

--League Information
--INSERT INTO league_Information(league name, division, region)
INSERT INTO league_Information VALUES ('premier_League', 1, 'england');

--Team Information
--INSERT INTO team_Information (team name, region, stadium, league name)
INSERT INTO team_Information VALUES ('tottenham', 'london', 'hotspur_Stadium', 'premier_League');
INSERT INTO team_Information VALUES ('chelsea', 'london', 'stamford_Bridge', 'premier_League');
INSERT INTO team_Information VALUES ('manchester_United', 'manchester', 'old_Trafford', 'premier_League');

--Player Information
--INSERT INTO player_Information(player name, age, height, position, team name)
INSERT INTO player_Information VALUES ('ronaldo', 37, '187cm', 'attacker', 'manchester_United');
INSERT INTO player_Information VALUES ('fernandes', 28, '194cm', 'midfielder', 'manchester_United');
INSERT INTO player_Information VALUES ('maguire', 29, '179cm', 'defender', 'manchester_United');
INSERT INTO player_Information VALUES ('sterling', 27, '172cm', 'attacker', 'chelsea');
INSERT INTO player_Information VALUES ('kante', 31, '171cm', 'midfielder',  'chelsea');
INSERT INTO player_Information VALUES ('koulibaly', 29, '186cm', 'defender', 'chelsea');
INSERT INTO player_Information VALUES ('kane', 29, '188cm', 'attacker', 'tottenham');
INSERT INTO player_Information VALUES ('perisic', 33, '186cm', 'midfielder', 'tottenham');
INSERT INTO player_Information VALUES ('romero', 24, '88cm', 'defender', 'tottenham');

--Scores
--INSERT INTO scores(fixture, home team, away team, result, stadium, date, league name)
INSERT INTO scores VALUES ('tot_mnu', 'tottenham', 'manchester_United', '2-1', 'hotspur_Stadium', 'oct-11', 'premier_League');
INSERT INTO scores VALUES ('mnu_che', 'manchester_United', 'chelsea', '0-0', 'old_Trafford', 'oct-17', 'premier_League');
INSERT INTO scores VALUES ('mnu_tot', 'manchester_United', 'tottenham', '1-1', 'old_Trafford', 'oct-20', 'premier_League');
INSERT INTO scores VALUES ('tot_che', 'tottenham', 'chelsea', '4-1', 'hotspur_Stadium', 'oct-24', 'premier_League');
INSERT INTO scores VALUES ('che_mnu', 'chelsea', 'manchester_United', '2-0', 'stamford_Bridge', 'oct-25', 'premier_League');
INSERT INTO scores VALUES ('che_tot', 'chelsea', 'tottenham', '2-3', 'stamford_Bridge', 'oct-30', 'premier_League');

--Team Statistics
--INSERT INTO team_Statistics(team ranking, team name, points, games played, wins, losses, draws, total goals)
INSERT INTO team_Statistics VALUES (1, 'tottenham', 10, 4, 3, 0, 1, 10);
INSERT INTO team_Statistics VALUES (2, 'chelsea', 4, 4, 1, 2, 1, 5);
INSERT INTO team_Statistics VALUES (3, 'manchester_United', 2, 4, 0, 2, 2, 2);

--Player Statistics
--INSERT INTO player_Statistics(player_id, player name, goals, assists, matches played)
INSERT INTO player_Statistics VALUES (7, 'ronaldo', 1, 0, 4);
INSERT INTO player_Statistics VALUES (8, 'fernandes', 0, 2, 4);
INSERT INTO player_Statistics VALUES (5, 'maguire', 1, 0, 4);
INSERT INTO player_Statistics VALUES (17, 'sterling', 3, 2, 4);
INSERT INTO player_Statistics VALUES (13, 'kante', 1, 3, 4);
INSERT INTO player_Statistics VALUES (26, 'koulibaly', 1, 0, 4);
INSERT INTO player_Statistics VALUES (10, 'kane', 6, 3, 4);
INSERT INTO player_Statistics VALUES (14, 'perisic', 3, 6, 4);
INSERT INTO player_Statistics VALUES (4, 'romero', 1, 1, 4);

--------------------Tables for Relations--------------------------------

--held_In
--INSERT INTO held_In(Fixture, League_Name)
INSERT INTO held_In VALUES ('tot_mnu','premier_League');
INSERT INTO held_In VALUES ('mnu_che','premier_League');
INSERT INTO held_In VALUES ('mnu_tot','premier_League');
INSERT INTO held_In VALUES ('tot_che','premier_League');
INSERT INTO held_In VALUES ('che_mnu','premier_League');
INSERT INTO held_In VALUES ('che_tot','premier_League');

--registered_In
--INSERT INTO registered_In(Team_Name, League_Name)
INSERT INTO registered_In VALUES ('tottenham', 'premier_League');
INSERT INTO registered_In VALUES ('chelsea', 'premier_League');
INSERT INTO registered_In VALUES ('manchester_United', 'premier_League');

--plays_For
--INSERT INTO plays_For(Player_Name, Team_Name)
INSERT INTO plays_For VALUES ('ronaldo','manchester_United');
INSERT INTO plays_For VALUES ('fernandes','manchester_United');
INSERT INTO plays_For VALUES ('maguire','manchester_United');
INSERT INTO plays_For VALUES ('sterling','chelsea');
INSERT INTO plays_For VALUES ('kante', 'chelsea');
INSERT INTO plays_For VALUES ('koulibaly','chelsea');
INSERT INTO plays_For VALUES ('kane', 'tottenham');
INSERT INTO plays_For VALUES ('perisic', 'tottenham');
INSERT INTO plays_For VALUES ('romero', 'tottenham');

--t_Perfomance
--INSERT INTO t_Perfomance(Team_Name, Team_Ranking)
INSERT INTO t_Perfomance VALUES ('tottenham', 1);
INSERT INTO t_Perfomance VALUES ('chelsea', 2);
INSERT INTO t_Perfomance VALUES ('manchester_United', 3);

--p_Performance
--INSERT INTO p_Performance(Player_Name, Player_Id)
INSERT INTO player_Statistics VALUES ('ronaldo', 7);
INSERT INTO player_Statistics VALUES ('fernandes', 8);
INSERT INTO player_Statistics VALUES ('maguire', 5);
INSERT INTO player_Statistics VALUES ('sterling', 17);
INSERT INTO player_Statistics VALUES ('kante', 13);
INSERT INTO player_Statistics VALUES ('koulibaly', 26);
INSERT INTO player_Statistics VALUES ('kane', 10);
INSERT INTO player_Statistics VALUES ('perisic', 14);
INSERT INTO player_Statistics VALUES ('romero', 4);

-- QUERIES to test the above INSERT statements for the entity tables

-- Queries to list all attributes of the entity/table
SELECT *
FROM league_Information;

SELECT *
FROM scores;

SELECT *
FROM team_Information;

SELECT *
FROM team_Statistics;

SELECT *
FROM player_Information;

SELECT *
FROM player_Statistics;

----------------------------

SELECT * 
FROM held_In;

SELECT * 
FROM registered_In;

SELECT * 
FROM plays_For;

SELECT * 
FROM t_Perfomance;

SELECT * 
FROM p_Performance;

-- Query to list all players with their number of goals and
-- assists if they scored more than 1 goal and have more than 2 assists
-- sorted in order of number of goals in descending order
SELECT Player_Name, Goals, Assists 
FROM player_Statistics
WHERE (Goals > 1)
      OR
      (Assists >= 3)
ORDER BY Goals DESC;
 
-- Query to list all teams in the league and the amount of players they have
-- Grouped by their team name
SELECT Team_Name, COUNT(*) AS Number_Of_Players
FROM player_Information
GROUP BY Team_Name;
 
-- Query to list the number of goals each team has grouped by
-- the team names and in descending order
SELECT Team_Name, AVG(Total_Goals) AS Num_Goals
FROM team_Statistics
GROUP BY Team_Name
ORDER BY Num_Goals DESC;

-- Assignment 4 Part b

-- Join queries

-- List all players with their team name and orders them from most to least goals if they have over 0 
-- Uses implicit join on 3 tables, 
-- team_Information and player_Information for Team_Name
-- player_Information and player_Statistics for Player_Name

SELECT t.Team_Name, p_i.Player_Name, p_s.Goals
FROM team_Information t, player_Information p_i, player_Statistics p_s
WHERE p_s.Goals > 0
      AND t.Team_Name = p_i.Team_Name
      AND p_i.Player_Name = p_s.Player_Name
ORDER BY p_s.Goals DESC;

-- Lists all players with their team name, goals and assists, that have more than 2 goals OR 3 assists, orders by goals descending
-- Groups player_Information and player_Statistics tables for Player_Name attribute

SELECT Team_Name, p_i.Player_Name, Goals, Assists
FROM player_Information p_i, player_Statistics p_s
WHERE Goals > 2 OR Assists > 3
      AND p_i.Player_Name = p_s.Player_Name
ORDER BY Goals DESC;
-- Inner join example
-- We don't have rows in different tables with the same matching common field but not the same attribute name
-- The closest to this is when rows match with common feilds, but as seen below, the attribute names are the same
SELECT player_Information.Player_Name, player_Statistics.Player_Name
FROM player_Information
INNER JOIN player_Statistics
ON player_Information.Player_Name = player_Statistics.Player_Name;

-- Views

-- Creates a VIEW for the top goals scorers in the league from player statistics by selecting player name and goals, and sorting them by most to least number of goals
CREATE VIEW Top_Scorers (Scorer_Player_Name, Scorer_Goals) AS
SELECT Player_Name, Goals
FROM player_Statistics
ORDER BY Goals DESC;
 
-- Creates a view for the tallest players from player information by 
selecting player name and height, then ordering it in descending order
CREATE VIEW Tallest_Players AS
SELECT Player_Name, Height
FROM player_Information
ORDER BY Height DESC;
 
-- Creates a view of the player ages within the database. This view takes every player's age from the Player Information table, ordering the players from oldest to youngest.
 
CREATE VIEW Player_Ages AS
SELECT Player_Name, Age
FROM player_Information
ORDER BY Age DESC;


-----------------------------A5 queries from topic 5 q11-23, using exists, union, minus

-- Uses Count() and GROUP BY
SELECT Team_Name, COUNT(*) AS Number_Of_Players
FROM player_Information
GROUP BY Team_Name;

-- Uses MINUS
SELECT Player_Name, Goals, Assists
FROM player_Statistics
MINUS 
(SELECT p_i.Player_Name, Goals, Assists
FROM player_Information p_i, player_Statistics p_s
WHERE Goals < 2 OR Assists < 3
      AND p_i.Player_Name = p_s.Player_Name);

-- Uses UNION
SELECT Player_Name
FROM player_Statistics
WHERE Goals > 2 
UNION
(SELECT Player_Name
FROM player_Statistics
WHERE Assists > 3);

-- Uses EXISTS
SELECT Player_Name
FROM player_Statistics
WHERE EXISTS
    (SELECT p_i.Player_Name, Goals, Assists
    FROM team_Statistics t_s, player_Statistics p_s, player_Information p_i
    WHERE Goals > 3 
        AND t_s.Wins > 2
        AND t_s.Team_Name = p_i.Team_Name
        AND p_i.Player_Name = p_s.Player_Name);

-- Uses HAVING

SELECT Player_Name, AVG(Goals)
FROM player_Statistics
GROUP BY Player_Name
HAVING AVG(Goals) > (SELECT AVG(Goals)
                     FROM player_Statistics);




















