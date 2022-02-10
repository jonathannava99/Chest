#! /usr/bin/envs python3
# coding: utf-8
from controller.game_system.play_tournament import Play
from controller.game_system.swiss_game import SwissGame
from model.requests.request_player import RequestsPlayer
from model.requests.request_tournament import RequestsTournament
from view.system.scores import Scores


class GameSystem:

    def creating_game(self, players: str, turn_id: int, tournament_id: int) -> None:
        """User select one game and insert points for each player
        then we create a game and insert into database

        Attr:
        - players(list): list of games to come order by swiss game rules
        - turn_id (int): Turn's identifier
        - tournament_id (int): Tournament's identifier
        """
        play = Play()
        players = play.get_players(players)
        players_id = play.get_id_players(players, tournament_id)
        player1_id = players_id[0]
        player2_id = players_id[1]
        if play.game_verification(player1_id, player2_id, turn_id, tournament_id):
            print("Match déjà joué")
        else:
            score = Scores()
            score = score.insert_scores()
            play.create_game(player1_id, player2_id, turn_id, score, tournament_id)
            if play.end_tournament(tournament_id):
                tournament = RequestsTournament()
                tournament.update_tournament_completed(tournament_id)
                play.update_date_end_turn(turn_id)

    def update_tournament_status(self, tournament_id: int) -> None:
        """Update tournament status to completed

         Attr:
         - tournament_id (int): Tournament's identifier
         """
        tournament = RequestsTournament()
        tournament.update_tournament_completed(tournament_id)

    def start_tournament(self, tournament_id: int, index: int) -> tuple:
        """The tournament start so a new turn is created. We have a list of games
        order by swiss game rules

         Attr:
         - index(int): number of the round current turn
         - tournament_id (int): Tournament's identifier

        Returns:
        - A tuple with the turn Identifier and games order by swiss game rules
        """
        play = Play()
        swissgame = SwissGame()
        play.create_turn(tournament_id, index)
        turn_id = play.getturnID(tournament_id)
        player = RequestsPlayer()
        list_players = player.read_player_by_ranking(tournament_id)
        swiss_game = swissgame.swiss_game_first_turn(list_players)
        players = play.swiss_tournament(index, swiss_game)
        start = (turn_id, players)
        return start

    def new_turn(self, tournament_id: int, turn_id: int, index: int) -> None:
        """If user select "Valider tour" then we check if is the end of the turn
        create a new turn and change the index for the next turn. If not print
        "Vous n'avez pas fait tous les matchs du tour"

         Attr:
         - index(int): number of the round current turn
         - turn_id(int):
         - tournament_id (int): Tournament's identifier
        """
        play = Play()
        if play.end_turn_verification(tournament_id, turn_id) \
                and not play.end_tournament(tournament_id):
            play.players_update_points(turn_id, tournament_id)
            play.update_date_end_turn(turn_id)
            index = int(index) + 1
            play.create_turn(tournament_id, index)
        else:
            print("Vous n'avez pas fait tous les matchs du tour")

    def continue_tournament(self, tournament_id: int) -> tuple:
        """If the tournament continue we read the turn_id and the index of the current turn

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - a tuple with turn's Identifier, index and object player
        """
        play = Play()
        turn_id = play.getturnID(tournament_id)
        round_turn = play.read_turn(tournament_id)
        index = play.get_index(round_turn)
        player = RequestsPlayer()
        to_continue = (turn_id, index, player)
        return to_continue
