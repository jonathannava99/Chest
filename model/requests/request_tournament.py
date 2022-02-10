#! /usr/bin/envs python3
# coding: utf-8
from model.entities.tournament import Tournament
from model.requests.request_template import RequestsTemplate


class RequestsTournament(RequestsTemplate):

    def create_tournament(self, tournament: Tournament) -> None:
        """Insert tournament into database

        Attrs:
        - sql (str): SQL request for create games
        - tournament (Tournament): Tournament object
        """
        name = tournament.name
        status = "process"
        place = tournament.place
        date = tournament.date
        number_of_turns = tournament.number_of_turns
        description = tournament.description
        val = (status, name, place, date, number_of_turns, description)
        sql = "INSERT INTO Tournament VALUES (null,?,?,?,?,?,?)"
        message = "Impossible de créer le tournoi"
        self.create(val, sql, message)

    def read_tournament(self, sql: str, message: str) -> list:
        """Read a lis of tournaments from the database

        Attrs:
        - sql (str): SQL request for read tournaments
        - message (str): Warning message if can't read tournaments

        Returns:
        - A format list with the tournaments
        """
        tournaments = []
        read_tournaments = self.read(sql, message)
        for i in read_tournaments:
            tournaments += ["id: {}, Tournoi: {}, Lieu: {}, "
                            "Date: {}, Tours: {}, Description: {}"
                            .format(i[0], i[1], i[2], i[3], i[4], i[5])]
        return tournaments

    def read_tournaments_list(self) -> list:
        """Read a lis of tournaments from the database

        Returns:
        - A format list with the tournaments
        """
        sql = "SELECT tournamentID,name,place,date," \
              "number_of_turns,description FROM Tournament"
        message = "Impossible de lire la liste de tournois"
        return self.read_tournament(sql, message)

    def read_tournaments_inprocess(self) -> list:
        """Read a lis of tournaments in process from the database

        Returns:
        - A format list with the tournaments in process
        """
        sql = "SELECT tournamentID,name,place,date,number_of_turns,description " \
              "FROM Tournament WHERE Status='process'"
        message = "Impossible de lire la liste de tournois en cours"
        return self.read_tournament(sql, message)

    def read_tournaments_completed(self) -> list:
        """Read a lis of tournaments completed from the database

        Returns:
        - A format list with the tournaments completed
        """
        sql = "SELECT tournamentID,name,place,date,number_of_turns,description " \
              "FROM Tournament WHERE Status= 'completed'"
        message = "Impossible de lire la liste de tournois completés"
        return self.read_tournament(sql, message)

    def read_tournament_id(self):
        """Read a tournament's ID from the last tournament

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A str with turn's ID
        """
        sql = "SELECT tournamentID FROM Tournament " \
              "ORDER BY tournamentID DESC LIMIT 1"
        message = "Impossible de lire le tournoi avec cet ID"
        tournament_id = self.read(sql, message)[0][0]
        return tournament_id

    def read_tournament_turns(self, tournament_id: int) -> str:
        """Read a number of turns where tournament_id == tournament_id

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A str with the  number of turns
        """
        sql = "SELECT number_of_turns FROM Tournament " \
              "WHERE tournamentID={}".format(tournament_id)
        message = "Impossible de lire le tournoi avec cet ID"
        tours = self.read(sql, message)[0][0]
        return tours

    def update_tournament_completed(self, tournament_id: int) -> None:
        """Update tournament status to completed from database

        Attrs:
        - tournament_id(int) : Tournament's identifier
        """
        sql = "UPDATE Tournament SET Status ='completed' WHERE tournamentID={}" \
            .format(tournament_id)
        message = "Impossible de modifier le statut du tournoi"
        self.update(sql, message)

    def delete_tournament(self, tournament_id: int) -> None:
        """Delete tournament from database where tournament_id = tournament_id

        Attrs:
        - tournament_id(int) : Tournament's identifier
        """
        table = "Tournament"
        table_id = "tournamentID"
        message = "Impossible de supprimer le tournoi"
        self.delete(table, table_id, tournament_id, message)
