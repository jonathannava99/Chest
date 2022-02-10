#! /usr/bin/envs python3
# coding: utf-8
from model.connection import Connection


class Tables(Connection):
    def create_table(self, sql_script, message):
        connection = self.getConnection()

        sql = sql_script

        try:
            connection.execute(sql)

        except NameError:
            print("La création de la table {} a echoué: {}".format(message, NameError))

        finally:
            connection.close()

    def create_table_game(self):

        sql = ("CREATE TABLE IF NOT EXISTS Game (gameID INTEGER PRIMARY KEY "
               "AUTOINCREMENT, score_player1 DECIMAL(10) DEFAULT NULL, "
               "score_player2 DECIMAL(10) DEFAULT NULL,"
               "player1_id INTEGER, player2_id INTEGER,turn_id INTEGER, "
               "tournament_id INTEGER,"
               "CONSTRAINT fk_tournament_id FOREIGN KEY (tournament_id)"
               "REFERENCES Tournament"
               "(tournamentID) ON DELETE CASCADE,"
               "CONSTRAINT fk_player1_id FOREIGN KEY (player1_id)"
               "REFERENCES Player"
               "(playerID) ON DELETE CASCADE,"
               "CONSTRAINT fk_player2_id FOREIGN KEY (player2_id)"
               "REFERENCES Player"
               "(playerID) ON DELETE CASCADE,"
               "CONSTRAINT fk_turn_id FOREIGN KEY (turn_id)"
               "REFERENCES Turn"
               "(turnID) ON DELETE CASCADE)")
        message = "Game"
        self.create_table(sql, message)

    def create_table_player(self):
        sql = ("CREATE TABLE IF NOT EXISTS Player (playerID INTEGER PRIMARY KEY "
               "AUTOINCREMENT,name VARCHAR(50), "
               "lastname VARCHAR(50), sex VARCHAR(50), birth DATE,"
               "ranking INT, points DECIMAL(10), tournament_id INTEGER, "
               "CONSTRAINT fk_tournament_id FOREIGN KEY (tournament_id)"
               "REFERENCES Tournament (tournamentID) ON DELETE CASCADE)")
        message = "Player"
        self.create_table(sql, message)

    def create_table_tournament(self):
        sql = ("CREATE TABLE IF NOT EXISTS Tournament (tournamentID INTEGER PRIMARY KEY "
               "AUTOINCREMENT,Status VARCHAR(50) DEFAULT Process, "
               "name VARCHAR(50), place VARCHAR(50),"
               "date DATE, "
               "number_of_turns INT, description VARCHAR(500) )")
        message = "Tournament"
        self.create_table(sql, message)

    def create_table_turn(self):
        sql = "CREATE TABLE IF NOT EXISTS Turn  " \
              "( turnID INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR NOT NULL," \
              "date_begining DATE, date_end DATE, tournamentID INTEGER, " \
              "CONSTRAINT tournament_id FOREIGN KEY (tournamentID)" \
              "REFERENCES Tournament (tournamentID) ON DELETE CASCADE) "
        message = "Turn"
        self.create_table(sql, message)
