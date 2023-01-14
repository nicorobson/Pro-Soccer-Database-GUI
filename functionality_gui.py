import cx_Oracle
import tkinter as tk
from tkinter import ttk

# Defining the dimensions of the main window and the results window
MAIN_WIDTH = 150
MAIN_HEIGHT = 250
RESULTS_WIDTH = 1000
RESULTS_HEIGHT = 2000
GRID_PAD = 5

# Creating the main window and giving it the appropriate title
main_window = tk.Tk()
main_window.title('Professional Soccer Database')

# Setting the position of the main window
main_window.geometry(
    f'{MAIN_WIDTH}x{MAIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - MAIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - MAIN_HEIGHT / 2)}')

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

# Initializing the connection to our Oracle database
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_7")

# Connection string which will login to our specific database
conn = 'confidential'
# Creating connection and cursor objects
connection = cx_Oracle.connect(conn)
cur = connection.cursor()

# Function for creating all the tables
def create_all_table():
    # This function will create a separate window for the results output
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    # league_Information table
    cur.execute("""
        CREATE TABLE league_Information (
    				League_Name VARCHAR2(30) NOT NULL,
    				Division NUMBER,
    				Region VARCHAR2(10),
    				PRIMARY KEY (League_Name)
					)""")

    #scores table
    cur.execute("""
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
					)""")

    #team_Information table
    cur.execute("""
        CREATE TABLE team_Information (
    				Team_Name VARCHAR2(20) NOT NULL,
    				City VARCHAR2(20),
    				Home_Stadium VARCHAR2(20),
    				League_Name VARCHAR2(30),
    				PRIMARY KEY (Team_Name),
    				FOREIGN KEY (League_Name) 
    				REFERENCES league_Information(League_Name)
					)""")

    #team_Statistics table        
    cur.execute("""
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
                    )""")

    #player_Information table
    cur.execute("""
        CREATE TABLE player_Information (
    				Player_Name VARCHAR2(30) NOT NULL,
    				Age NUMBER,
    				Height VARCHAR2(10), 
    				Player_Position VARCHAR2(30),
    				Team_Name VARCHAR2(20),
    				PRIMARY KEY (Player_Name),
    				FOREIGN KEY (Team_Name)
    				REFERENCES team_Information(Team_Name)
                    )""")

    #player_Statistics table
    cur.execute("""
        CREATE TABLE player_Statistics (
    				Player_ID NUMBER NOT NULL,
    				Player_Name VARCHAR2(30),
    				Goals NUMBER,
    				Assists NUMBER,
    				Matches_Played NUMBER,
    				PRIMARY KEY (Player_ID),
    				FOREIGN KEY (Player_Name)
    				REFERENCES player_Information(Player_Name)
                    )""")

    #held_In table
    cur.execute("""
    	CREATE TABLE held_In (
    				Fixture VARCHAR2(10) NOT NULL REFERENCES scores(Fixture),
    				League_Name VARCHAR2(30) NOT NULL REFERENCES league_Information(League_Name),
    				PRIMARY KEY (Fixture, League_Name)
					)""")

    #registered_In table
    cur.execute("""
    	CREATE TABLE registered_In ( 
    				Team_Name VARCHAR2(20) NOT NULL REFERENCES team_Information(Team_Name),
    				League_Name VARCHAR2(30) NOT NULL REFERENCES league_Information(League_Name),
    				PRIMARY KEY(Team_Name, League_Name)
					)""")

    #plays_For table
    cur.execute("""
    	CREATE TABLE plays_For ( 
    				Player_Name VARCHAR2(30) NOT NULL REFERENCES player_Information(Player_Name),
    				Team_Name VARCHAR2(20) NOT NULL REFERENCES team_Information(Team_Name),
    				PRIMARY KEY (Player_Name, Team_Name)
					)""")

    #t_Performance table
    cur.execute("""
   		CREATE TABLE t_Performance (
    				Team_Name VARCHAR2(20) NOT NULL REFERENCES team_Information(Team_Name),    
    				Team_Ranking NUMBER NOT NULL REFERENCES team_Statistics(Team_Ranking),
    				PRIMARY KEY (Team_Name, Team_Ranking)
					)""")

    #p_Performance table
    cur.execute("""
    	CREATE TABLE p_Performance (
    				Player_Name VARCHAR2(30) NOT NULL REFERENCES player_Information(Player_Name),
    				Player_ID NUMBER NOT NULL REFERENCES player_Statistics(Player_ID),          
    				PRIMARY KEY (Player_Name, Player_ID) 
					)""")   

    output = "Table LEAGUE_INFORMATION created.\n\nTable SCORES created.\n\nTable TEAM_INFORMATION created.\n\nTable TEAM_STATISTICS created.\n\n\
Table PLAYER_INFORMATION created.\n\nTable PLAYER_STATISTICS created.\n\nTable HELD_IN created.\n\nTable REGISTERED_IN created.\n\nTable PLAYS_FOR created.\n\n\
Table T_PERFORMANCE created.\n\nTable P_PERFORMANCE created."
    ttk.Label(results_window, text=output).pack(
        padx=GRID_PAD, pady=GRID_PAD) 

# Function for inserting information into all tables
def populate_all_table():
    # This function will create a separate window for the results output
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

	#league_Information
    cur.execute("""INSERT INTO league_Information VALUES ('premier_League', 1, 'england')""")

    #scores
    cur.execute("""INSERT INTO scores VALUES ('tot_mnu', 'tottenham', 'manchester_United', '2-1', 'hotspur_Stadium', 'oct-11', 'premier_League')""")
    cur.execute("""INSERT INTO scores VALUES ('mnu_che', 'manchester_United', 'chelsea', '0-0', 'old_Trafford', 'oct-17', 'premier_League')""")
    cur.execute("""INSERT INTO scores VALUES ('mnu_tot', 'manchester_United', 'tottenham', '1-1', 'old_Trafford', 'oct-20', 'premier_League')""")
    cur.execute("""INSERT INTO scores VALUES ('tot_che', 'tottenham', 'chelsea', '4-1', 'hotspur_Stadium', 'oct-24', 'premier_League')""")
    cur.execute("""INSERT INTO scores VALUES ('che_mnu', 'chelsea', 'manchester_United', '2-0', 'stamford_Bridge', 'oct-25', 'premier_League')""")
    cur.execute("""INSERT INTO scores VALUES ('che_tot', 'chelsea', 'tottenham', '2-3', 'stamford_Bridge', 'oct-30', 'premier_League')""")

    #team_Information
    cur.execute("""INSERT INTO team_Information VALUES ('tottenham', 'london', 'hotspur_Stadium', 'premier_League')""")
    cur.execute("""INSERT INTO team_Information VALUES ('chelsea', 'london', 'stamford_Bridge', 'premier_League')""")
    cur.execute("""INSERT INTO team_Information VALUES ('manchester_United', 'manchester', 'old_Trafford', 'premier_League')""")

    #team_Statistics        
    cur.execute("""INSERT INTO team_Statistics VALUES (1, 'tottenham', 10, 4, 3, 0, 1, 10)""")
    cur.execute("""INSERT INTO team_Statistics VALUES (2, 'chelsea', 4, 4, 1, 2, 1, 5)""")
    cur.execute("""INSERT INTO team_Statistics VALUES (3, 'manchester_United', 2, 4, 0, 2, 2, 2)""")

    #player_Information
    cur.execute("""INSERT INTO player_Information VALUES ('ronaldo', 37, '187cm', 'attacker', 'manchester_United')""")
    cur.execute("""INSERT INTO player_Information VALUES ('fernandes', 28, '194cm', 'midfielder', 'manchester_United')""")
    cur.execute("""INSERT INTO player_Information VALUES ('maguire', 29, '179cm', 'defender', 'manchester_United')""")
    cur.execute("""INSERT INTO player_Information VALUES ('sterling', 27, '172cm', 'attacker', 'chelsea')""")
    cur.execute("""INSERT INTO player_Information VALUES ('kante', 31, '171cm', 'midfielder',  'chelsea')""")
    cur.execute("""INSERT INTO player_Information VALUES ('koulibaly', 29, '186cm', 'defender', 'chelsea')""")
    cur.execute("""INSERT INTO player_Information VALUES ('kane', 29, '188cm', 'attacker', 'tottenham')""")
    cur.execute("""INSERT INTO player_Information VALUES ('perisic', 33, '186cm', 'midfielder', 'tottenham')""")
    cur.execute("""INSERT INTO player_Information VALUES ('romero', 24, '88cm', 'defender', 'tottenham')""")

    #player_Statistics
    cur.execute("""INSERT INTO player_Statistics VALUES (7, 'ronaldo', 1, 0, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (8, 'fernandes', 0, 2, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (5, 'maguire', 1, 0, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (17, 'sterling', 3, 2, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (13, 'kante', 1, 3, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (26, 'koulibaly', 1, 0, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (10, 'kane', 6, 3, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (14, 'perisic', 3, 6, 4)""")
    cur.execute("""INSERT INTO player_Statistics VALUES (4, 'romero', 1, 1, 4)""")

    #held_In
    cur.execute("""INSERT INTO held_In VALUES ('tot_mnu','premier_League')""")
    cur.execute("""INSERT INTO held_In VALUES ('mnu_che','premier_League')""")
    cur.execute("""INSERT INTO held_In VALUES ('mnu_tot','premier_League')""")
    cur.execute("""INSERT INTO held_In VALUES ('tot_che','premier_League')""")
    cur.execute("""INSERT INTO held_In VALUES ('che_mnu','premier_League')""")
    cur.execute("""INSERT INTO held_In VALUES ('che_tot','premier_League')""")

    #registered_In
    cur.execute("""INSERT INTO registered_In VALUES ('tottenham', 'premier_League')""")
    cur.execute("""INSERT INTO registered_In VALUES ('chelsea', 'premier_League')""")
    cur.execute("""INSERT INTO registered_In VALUES ('manchester_United', 'premier_League')""")

    #plays_For
    cur.execute("""INSERT INTO plays_For VALUES ('ronaldo','manchester_United')""")
    cur.execute("""INSERT INTO plays_For VALUES ('fernandes','manchester_United')""")
    cur.execute("""INSERT INTO plays_For VALUES ('maguire','manchester_United')""")
    cur.execute("""INSERT INTO plays_For VALUES ('sterling','chelsea')""")
    cur.execute("""INSERT INTO plays_For VALUES ('kante', 'chelsea')""")
    cur.execute("""INSERT INTO plays_For VALUES ('koulibaly','chelsea')""")
    cur.execute("""INSERT INTO plays_For VALUES ('kane', 'tottenham')""")
    cur.execute("""INSERT INTO plays_For VALUES ('perisic', 'tottenham')""")
    cur.execute("""INSERT INTO plays_For VALUES ('romero', 'tottenham')""")

    #t_Performance
    cur.execute("""INSERT INTO t_Performance VALUES ('tottenham', 1)""")
    cur.execute("""INSERT INTO t_Performance VALUES ('chelsea', 2)""")
    cur.execute("""INSERT INTO t_Performance VALUES ('manchester_United', 3)""")  

    #p_Performance
    cur.execute("""INSERT INTO p_Performance VALUES ('ronaldo', 7)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('fernandes', 8)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('maguire', 5)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('sterling', 17)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('kante', 13)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('koulibaly', 26)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('kane', 10)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('perisic', 14)""")
    cur.execute("""INSERT INTO p_Performance VALUES ('romero', 4)""")

    populateOutput = "LEAGUE_INFORMATION  1 ROW INSERTED\n\nSCORES              6 ROWS INSERTED\n\nTEAM_INFORMATION    3 ROWS INSERTED\n\n\
TEAM_STATISTICS     3 ROWS INSERTED\n\nPLAYER_INFORMATION  9 ROWS INSERTED\n\nPLAYER_STATISTICS   9 ROWS INSERTED\n\nHELD_IN             6 ROWS INSERTED\n\n\
REGISTERED_IN       3 ROWS INSERTED\n\nPLAYS_FOR           9 ROWS INSERTED\n\nT_PERFORMANCE       3 ROWS INSERTED\n\nP_PERFORMANCE       9 ROWS INSERTED"
    ttk.Label(results_window, text=populateOutput).pack(
        padx=GRID_PAD, pady=GRID_PAD) 
    connection.commit()

# Function for dropping all tables
def drop_all_table():
    # This function will create a separate window for the results output
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cur.execute("""DROP TABLE p_Performance""")
    cur.execute("""DROP TABLE t_Performance""")
    cur.execute("""DROP TABLE plays_For""")
    cur.execute("""DROP TABLE registered_In""")
    cur.execute("""DROP TABLE held_In""")
    cur.execute("""DROP TABLE player_Statistics""")
    cur.execute("""DROP TABLE player_Information""")
    cur.execute("""DROP TABLE team_Statistics""")
    cur.execute("""DROP TABLE team_Information""")
    cur.execute("""DROP TABLE scores""")
    cur.execute("""DROP TABLE league_Information""")  

    droppedOutput = "Table P_PERFORMANCE dropped.\n\nTable T_PERFORMANCE dropped.\n\nTable PLAYS_FOR dropped.\n\nTable REGISTERED_IN dropped.\n\n\
Table HELD_IN dropped.\n\nTable PLAYER_STATISTICS dropped.\n\nTable PLAYER_INFORMATION dropped.\n\nTable TEAM_STATISTICS dropped.\n\n\
Table TEAM_INFORMATION dropped.\n\nTable SCORES dropped.\n\nTable LEAGUE_INFORMATION dropped.\n\n"
    ttk.Label(results_window, text=droppedOutput).pack(
        padx=GRID_PAD, pady=GRID_PAD)  

# Function for running the main queries for each table
def query_all_table():
    # This function will create a separate window for the results output
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    # league_Information
    cur.execute("""SELECT * FROM league_Information""")

    # scores
    cur.execute("""SELECT * FROM scores""")

    # team_Information
    cur.execute("""SELECT * FROM team_Information""")

    # team_Statistics
    cur.execute("""SELECT * FROM team_Statistics""")
    
    # player_Information
    cur.execute("""SELECT * FROM player_Information""")

    # player_Statistics
    cur.execute("""SELECT * FROM player_Statistics""")

    # held_In
    cur.execute("""SELECT * FROM held_In""")

    # registered_In
    cur.execute("""SELECT * FROM registered_In""")

    # plays_For
    cur.execute("""SELECT * FROM plays_For""")

    # t_Performance
    cur.execute("""SELECT * FROM t_Performance""")

    # p_Performance
    cur.execute("""SELECT * FROM p_Performance""")
    
    import message
    ttk.Label(results_window, text=message.message).pack(
        padx=GRID_PAD, pady=GRID_PAD)

#Creating the layout of the main menu; including all available commands
ttk.Label(main_window, text='Commands').grid(
    row=0, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create all Tables', command=create_all_table).grid(
    row=1, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop all Tables', command=drop_all_table).grid(
    row=2, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate all Tables', command=populate_all_table).grid(
    row=3, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Query all Tables', command=query_all_table).grid(
    row=4, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Exit', command=main_window.destroy).grid(
    row=5, column=0, padx=GRID_PAD, pady=GRID_PAD)       

# If block which runs the GUI
if __name__ == '__main__':
    main_window.mainloop()
