#! /usr/bin/envs python3
# coding: utf-8
from model.entities.player import Player
from model.requests.request_template import RequestsTemplate


class RequestsPlayer(RequestsTemplate):

    def create_player(self, player: Player, tournament_id: int):
        """Insert player into database

        Attrs:
        - sql (str): SQL request for create player
        - player (Player): Player object
        - tournament_id: Tournament's identifier
        """
        name = player.name
        lastname = player.lastName
        birth = player.birth
        sex = player.sex
        ranking = player.ranking
        val = (name, lastname, sex, birth, ranking, tournament_id)
        sql = "INSERT INTO Player VALUES (null,?,?,?,?,?,0,?)"
        message = "Impossible de créer le joueur"
        self.create(val, sql, message)

    def read_player(self, sql, message):
        """Read a lis of players from the database

        Attrs:
        - sql (str): SQL request for read players
        - message (str): Warning message if can't read players

        Returns:
        - A format list with the players
        """
        players = []
        read_players = self.read(sql, message)
        for i in read_players:
            players += ["id: {}, Prenom: {},  Nom: {},  Genre: {},"
                        " Points: {}  Classement: {}  "
                        .format(i[0], i[1], i[2], i[3], i[4], i[5])]
        return players

    def read_player_by_ranking(self, tournament_id: int) -> list:
        """Read a list of players where tournament_id == tournament_id and order by ranking

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A format list with the players order by ranking
        """
        sql = "SELECT playerID,name,lastname,sex, points,ranking " \
              "FROM Player WHERE tournament_id={} " \
              "ORDER BY ranking ASC".format(tournament_id)

        message = "Impossible de lire liste de joueurs par classement"
        return self.read_player(sql, message)

    def read_player_by_points(self, tournament_id: int) -> list:
        """Read a list of players where tournament_id == tournament_id and order by points

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A format list with the players order by points
        """
        sql = "SELECT playerID,name,lastname,sex, points,ranking " \
              "FROM Player WHERE tournament_id={} " \
              "ORDER BY points DESC".format(tournament_id)
        message = "Impossible de lire la liste de joueurs par points"
        return self.read_player(sql, message)

    def read_player_by_lastname(self, tournament_id: int) -> list:
        """Read a list of players where tournament_id == tournament_id and order by lastname

        Attrs:
        - tournament_id (int): Tournament's identifier

        Returns:
        - A format list with the players order by lastname
        """
        sql = "SELECT playerID,name,lastname,sex, points,ranking " \
              "FROM Player WHERE tournament_id={} " \
              "ORDER BY lastname ASC".format(tournament_id)
        message = "Impossible de lire la liste de joueurs triés par nom"
        return self.read_player(sql, message)

    def read_player_by_id(self, player_id: int) -> tuple:
        """Read a list of players where playerID == player_id

        Attrs:
        - player_id (int): Player's identifier

        Returns:
        - A tuple with player's names and lastnames
        """
        sql = "SELECT name, lastname FROM Player " \
              "WHERE playerID={}".format(player_id)
        message = "Impossible de lire le joueur"
        return self.read(sql, message)

    def read_points_of_player(self, player_id: int) -> str:
        """Read player's points where playerID == player_id and order by lastname

        Attrs:
        - player_id (int): Players's identifier

        Returns:
        - A string with player's points
        """
        sql = "SELECT points " \
              "FROM Player WHERE playerID={} " \
              "ORDER BY points DESC".format(player_id)
        message = "Impossible d'obtenir les points du joueur"
        return self.read(sql, message)[0][0]

    def get_player_id_by_name(self, name: str, lastname: str, tournament_id: int) -> str:
        """Read player's ID where name == name, lastname == lastname and tournament_id = tournament_id

        Attrs:
        - name(str): Player's name
        - lastname(str): Player's lastname
        - tournament_id (int): Tournament's identifier

        Returns:
        - A string with player's ID
        """
        sql = "SELECT playerID FROM Player " \
              "WHERE name='{}' AND lastname='{}' AND tournament_id={}"\
            .format(name, lastname, tournament_id)
        message = "Impossible de lire le joueur"
        return self.read(sql, message)[0][0]

    def update_player_ranking(self, ranking: str, player_id: int) -> None:
        """Update player ranking from database

        Attrs:
        - player_id(int) : Player's identifier
        """
        sql = "UPDATE Player SET ranking = {} WHERE playerID={}" \
            .format(ranking, player_id)
        message = "Impossible de modifier le joueur"
        self.update(sql, message)

    def update_player_points(self, points: str, player_id: int) -> None:
        """Update player points from database

        Attrs:
        - player_id(int) : Player's identifier
        """
        sql = "UPDATE Player SET points = {} WHERE playerID={}" \
            .format(points, player_id)
        message = "Impossible de modifier le joueur"
        self.update(sql, message)
