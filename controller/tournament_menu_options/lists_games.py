#! /usr/bin/envs python3
# coding: utf-8
from view.lists.list_games import ListGames
from model.requests.request_game import RequestsGame


class GameLists:
    def games_tournament(self, tournament_id: int) -> int:
        """Read all of tournament's games. User can select one of them

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - Game's Identifier of user's selected game
        """
        game = RequestsGame()
        games = game.lists_read_game(tournament_id)
        game_id = ListGames().list_games(games)
        return game_id

    def games_turn(self, tournament_id: int, turn_id: int) -> int:
        """Read all of tournament's and turn's games. User can select one of them

        Attr:
        - tournament_id (int): Tournament's identifier
        - turn_id (int): Turn's identifier

        Returns:
        - Game's Identifier of user's selected game
        """
        game = RequestsGame()
        games = game.lists_read_game_by_turn(tournament_id, turn_id)
        game_id = ListGames().list_games(games)
        return game_id
