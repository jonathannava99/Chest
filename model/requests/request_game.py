#! /usr/bin/envs python3
# coding: utf-8
from model.entities.game import Game
from model.requests.request_template import RequestsTemplate
from model.requests.request_player import RequestsPlayer


class RequestsGame(RequestsTemplate):
    def read_game(self, sql: str, message: str) -> list:
        """Read a lis of games from the database

        Attrs:
        - sql (str): SQL request for read games
        - message (str): Warning message if can't read games

        Returns:
        - A format list with the games
        """
        game_lists = []
        player = RequestsPlayer()
        read_games = self.read(sql, message)

        try:
            for i in read_games:
                id_game = i[0]
                score_player1 = i[1]
                score_player2 = i[2]
                player_1 = player.read_player_by_id(i[3])[0]
                player_1_name = player_1[0]
                player_1_lastname = player_1[1]
                player_2_id = player.read_player_by_id(i[4])[0]
                player_2_name = player_2_id[0]
                player_2_lastname = player_2_id[1]
                games = [id_game, score_player1, score_player2, player_1_name,
                         player_1_lastname, player_2_name, player_2_lastname]

                game_lists += ["id: {}, {} {}: {} - {} {}: {}"
                               .format(games[0], games[3], games[4],
                                       games[1], games[5], games[6], games[2])]
            return game_lists
        except IndexError:
            game_lists = []
            return game_lists
        finally:
            return game_lists

    def create_game(self, game: Game, turn_id: int, tournament_id: int) -> None:
        """Insert game into database

        Attrs:
        - sql (str): SQL request for create games
        - game (Game): Game object
        - turn_id: Turn's identifier
        - tournament_id: Tournament's identifier
        """
        player1 = game.player1
        player2 = game.player2
        score_player1 = game.score[0]
        score_player2 = game.score[1]
        turn_id = turn_id
        tournament_id = tournament_id
        val = (score_player1, score_player2, player1, player2, turn_id, tournament_id)
        sql = "INSERT INTO Game VALUES (null,?,?,?,?,?,?)"
        message = "Impossible de créer le match"
        self.create(val, sql, message)

    def lists_read_game(self, tournament_id):
        """Read a lis of tournaments from the database

        Attrs:
        - tournament_id(int): Tournament's identifier

        Returns:
        - A format list with the tournaments
        """
        sql = "SELECT gameID, score_player1, score_player2, player1_id, player2_id " \
              "FROM Game WHERE tournament_id={}".format(tournament_id)
        message = "Impossible de lire la liste de matchs"
        return self.read_game(sql, message)

    def lists_read_game_by_turn(self, tournament_id: int, turn_id: int) -> list:
        """Read a list of games from the database where tournament_id == tournament_id
        and turn_id = turn_id

        Attrs:
        - turn_id(int): Turn's identifier
        - tournament_id(int): Tournament's identifier

        Returns:
        - A format list with the games
        """
        sql = "SELECT gameID, score_player1, score_player2, player1_id, player2_id " \
              "FROM Game WHERE tournament_id={} AND turn_id={}".format(tournament_id, turn_id)
        message = "Impossible de lire la liste de matchs"
        return self.read_game(sql, message)

    def lists_read_game_scores(self, tournament_id: int, turn_id: int) -> tuple:
        """Read a list of game's scores and player's ids from the database where tournament_id == tournament_id
         and turn_id = turn_id

        Attrs:
        - turn_id(int): Turn's identifier
        - tournament_id(int): Tournament's identifier

         Returns:
         - A format list with Game's scores and players_id
         """
        sql = "SELECT score_player1, score_player2, player1_id, player2_id " \
              "FROM Game WHERE tournament_id={} AND turn_id={}".format(tournament_id, turn_id)
        message = "Impossible de lire la liste de matchs"
        return self.read(sql, message)

    def lists_read_game_by_player(self, player1_id: int, player2_id, turn_id, tournament_id):
        """Read a list of game from the database where player1_id == player1_id,
        tournament_id == tournament_id and turn_id = turn_id

        Attrs:
        - player1_id(int): PLayer's 1 Identifier
        - player2_id(int): PLayer's 2 Identifier
        - turn_id(int): Turn's identifier
        - tournament_id(int): Tournament's identifier

        Returns:
        - A format list with the games
        """
        sql = "SELECT gameID, score_player1, score_player2, player1_id, player2_id " \
              "FROM Game WHERE " \
              "player1_id={} AND player2_id={} AND turn_id={} AND tournament_id={}"\
            .format(player1_id, player2_id, turn_id, tournament_id)
        message = "Impossible de lire le match"
        return self.read_game(sql, message)
