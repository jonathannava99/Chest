#! /usr/bin/envs python3
# coding: utf-8
from model.entities.game import Game
from model.entities.turn import Turn
from model.requests.request_game import RequestsGame
from model.requests.request_player import RequestsPlayer
from model.requests.request_tournament import RequestsTournament
from model.requests.request_turn import RequestsTurn
from view.lists.list_turns import ListTurns
from view.system.play_tournament import PlayTournament
from view.system.scores import Scores


class Play:

    def begin_verfication(self, tournament_id: int) -> bool:
        """Verify if is the beginning of tournament

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - true or false if condition is checked
        """
        turn = RequestsTurn()
        turn = turn.read_a_turn(tournament_id)
        if len(turn) == 0:
            turn = True
        else:
            turn = False

        return turn

    def end_turn_verification(self, tournament_id: int, turn_id: int) -> bool:
        """Verify if is the end of the turn

        Attr:
        - tournament_id (int): Tournament's identifier
        - turn_id (int): Turn's identifier

        Returns:
        - true or false if condition is checked
        """
        player = RequestsPlayer()
        number_of_games = len(player.read_player_by_points(tournament_id)) // 2
        game = RequestsGame()
        games = len(game.lists_read_game_by_turn(tournament_id, turn_id))
        if games == number_of_games:
            turn = True
        else:
            turn = False
        return turn

    def end_tournament(self, tournament_id: int) -> bool:
        """Verify if is the end of the tournament

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - true or false if condition is checked
        """
        turn = RequestsTurn()
        game = RequestsGame()
        player = RequestsPlayer()
        tournament = RequestsTournament()
        turn_id = int(turn.read_turn_byid(tournament_id))
        tournament_turns = int(tournament.read_tournament_turns(tournament_id))
        player_games = len(player.read_player_by_points(tournament_id)) // 2
        number_of_games = len(game.lists_read_game_by_turn(tournament_id, turn_id))
        number_of_turns = len(turn.lists_read_turn(tournament_id))

        if tournament_turns == number_of_turns and number_of_games == player_games:
            tournament = True
        else:
            tournament = False
        return tournament

    def game_verification(self, player1_id: int, player2_id: int,
                          turn_id: int, tournament_id: int) -> bool:
        """Verify if game is already played

        Attr:
        - player1_id (int): player1_id's identifier
        - player2_id (int): player2_id's identifier
        - turn_id (int): Turn's identifier
        - tournament_id (int): Tournament's identifier

        Returns:
        - true or false if condition is checked
        """

        games = RequestsGame()
        game = games.lists_read_game_by_player(player1_id,
                                               player2_id, turn_id, tournament_id)
        size = len(game)
        if size == 0:
            game_verification = False
        else:
            game_verification = True

        return game_verification

    def get_index(self, round_turn: str) -> str:
        """Get turn number's round

        Attr:
        - player1_id (int): player1_id's identifier
        - player2_id (int): player2_id's identifier
        - turn_id (int): Turn's identifier
        - tournament_id (int): Tournament's identifier

        Returns:
        - the number's round of the current turn
        """
        if round_turn == "Revenir en arrière":
            round_turn = 0

        else:
            round_turn = round_turn.split(",")
            round_turn = round_turn[1].strip()
            round_turn = round_turn.split(" ")[1]
        return round_turn

    def create_turn(self, tournament_id: int, index: int) -> None:
        """Create turn

        Attr:
        - index(int): The number's round of the next turn
        - tournament_id (int): Tournament's identifier
        """
        turn_request = RequestsTurn()
        turn_entity = Turn("Round {}".format(index))
        turn_request.create_turn(turn_entity, tournament_id)

    def read_turn(self, tournament_id: int) -> str:
        """Read last turn created

         Attr:
         - tournament_id (int): Tournament's identifier

        Returns:
        - a string with the infos of turn selected by user
        """
        request_turn = RequestsTurn()
        turn_list = ListTurns()
        turn = request_turn.read_a_turn(tournament_id)
        turn_read = turn_list.list_turn(turn)
        return turn_read

    def getturnID(self, tournament_id: int):
        """Get turn ID by the last turn

         Attr:
         - tournament_id (int): Tournament's identifier

        Returns:
        - turn's identifier
        """
        request_turn = RequestsTurn()
        turn_id = request_turn.read_turn_byid(tournament_id)
        return turn_id

    def get_scores(self) -> tuple:
        """We ask scores to user and returns it

        Returns:
        - a tuple with the scores
        """
        score = Scores()
        score = score.insert_scores()
        return score

    def get_players(self, players: str) -> tuple:
        """Format string to get name and lastname of players of the games

        Attr:
        - players(str): a game with the name and last name of players

        Returns:
        - a tuple player1_name, player1_lastname, player2_name, player2_lastname
        """
        players = players
        player1_name = players[0].split(" ")[0]
        player1_lastname = players[0].split(" ")[1]
        player2_name = players[1].strip().split(" ")[0]
        player2_lastname = players[1].strip().split(" ")[1]
        players = (player1_name, player1_lastname, player2_name, player2_lastname)
        return players

    def get_id_players(self, players: tuple, tournament_id: int) -> tuple:
        """Format string to get name and lastname of players of the games

         Attr:
         - players(tuple): a tuple with player1_name, player1_lastname,
         player2_name, player2_lastname
         - tournament_id (int): Tournament's identifier

         Returns:
         - a tuple with ids of both players
         """
        player = RequestsPlayer()
        player_id_1 = player.get_player_id_by_name(players[0], players[1], tournament_id)
        player_id_2 = player.get_player_id_by_name(players[2], players[3], tournament_id)
        players_ids = (player_id_1, player_id_2)
        return players_ids

    def players_update_points(self, turn_id: int, tournament_id: int) -> None:
        """Update the points of a player

        Attr:
        - tournament_id (int): Tournament's identifier
        - turn_id (int): Turn's identifier
        """
        request_game = RequestsGame()
        games = request_game.lists_read_game_scores(tournament_id, turn_id)
        for game in games:
            player1_score = game[0]
            player2_score = game[1]
            player1_id = game[2]
            player2_id = game[3]
            player_points = RequestsPlayer()
            points_player_1 = int(player_points.read_points_of_player(player1_id))
            points_player_2 = int(player_points.read_points_of_player(player2_id))
            player_points.update_player_points((points_player_1 + player1_score), player1_id)
            player_points.update_player_points((points_player_2 + player2_score), player2_id)

    def update_date_end_turn(self, turn_id: int) -> None:
        """Update date_end_turn

        Attr:
        - turn_id (int): Turn's identifier
        """
        turn_request = RequestsTurn()
        turn_request.update_date_end(turn_id)

    def create_game(self, player1_id: int, player2_id: int,
                    turn_id: int, score: tuple, tournament_id: int):
        """Create game

        Attr:
        - tournament_id (int): Tournament's identifier
        - player1_id (int): Player1 identifier
        - player2_id (int): Player2 identifier
        - turn_id (int): Turn's identifier
        """
        game = Game(player1_id, player2_id, score)
        create_game = RequestsGame()
        create_game.create_game(game, turn_id, tournament_id)

    def swiss_tournament(self, index: [int, str], play: list) -> [tuple, list]:
        """Swiss game

        Attr:
        - index(int): Number of the current turn
        - play: list of games order by swiss game rules

        Returns:
        - the name and last name of the
        """
        play_tournament = PlayTournament()
        players_name = play_tournament.tournament_process(play, index)
        return players_name
