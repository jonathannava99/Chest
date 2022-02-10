#! /usr/bin/envs python3
# coding: utf-8
import datetime

from model.entities.turn import Turn
from model.requests.request_template import RequestsTemplate


class RequestsTurn(RequestsTemplate):
    def create_turn(self, turn: Turn, tournament_id: int) -> None:
        """Insert turn into database

        Attrs:
        - sql (str): SQL request for create turns
        - turn (Turn): Turn object
        - tournament_id: Tournament's identifier
        """
        name = turn.name
        beginning = turn.date_begining
        end = None
        tournament_id = tournament_id
        val = (name, beginning, end, tournament_id)
        sql = "INSERT INTO Turn VALUES (null,?,?,?,?)"
        message = "Impossible de créer le tour"
        self.create(val, sql, message)

    def read_turn(self, sql, message):
        """Read a lis of turns from the database

        Attrs:
        - sql (str): SQL request for read turns
        - message (str): Warning message if can't read turns

        Returns:
        - A format list with the turns
        """
        turns = []
        read_turns = self.read(sql, message)
        for i in read_turns:
            try:
                turns += ["id: {},  {},  Debut: {},  "
                          "Fin: {}".format(i[0], i[1], i[2], i[3])] \
                    if i[3] is not None else ["id: {},  {},  "
                                              "Debut: {}".format(i[0], i[1], i[2])]
            except IndexError:
                turns = []
        return turns

    def read_a_turn(self, tournament_id: int) -> list:
        """Read a turn where tournament_id == tournament_id

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A format list with the turn
        """
        sql = "SELECT turnID, name, date_begining, date_end " \
              "FROM Turn WHERE tournamentID={} " \
              "ORDER BY name DESC LIMIT 1".format(tournament_id)

        message = "Impossible de lire le tour"
        return self.read_turn(sql, message)

    def read_turn_byid(self, tournament_id: int) -> str:
        """Read a turn's ID where tournament_id == tournament_id

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A str with turn's ID
        """
        sql = "SELECT turnID " \
              "FROM Turn WHERE tournamentID={} " \
              "ORDER BY name DESC LIMIT 1".format(tournament_id)

        message = "Impossible de lire le tour"
        return self.read(sql, message)[0][0]

    def lists_read_turn(self, tournament_id: int) -> list:
        """Read a list of turns where tournament_id == tournament_id

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A format list with the turns
        """
        sql = "SELECT turnID, name, date_begining, date_end " \
              "FROM Turn WHERE tournamentID={}".format(tournament_id)

        message = "Impossible de lire la liste de tours"
        return self.read_turn(sql, message)

    def update_date_end(self, turn_id: int) -> None:
        """Update turn date_end from database

        Attrs:
        - turn_id(int) : Turn's identifier
        """
        date_end_turn = datetime.date.today()
        sql = "UPDATE Turn SET date_end = '{}' WHERE turnID={}" \
            .format(date_end_turn, turn_id)
        message = "Impossible de modifier le tour"
        self.update(sql, message)


