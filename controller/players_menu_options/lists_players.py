#! /usr/bin/envs python3
# coding: utf-8
from view.lists.list_players import ListPlayers
from model.requests.request_player import RequestsPlayer


class PlayerLists:
    def players_lists_by_name(self, tournament_id: int) -> int:
        """Read all of tournament's players order by lastname. User can select one of them

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - Player's Identifier of user's selected player
        """
        player_list_by_name = RequestsPlayer().read_player_by_lastname(tournament_id)
        player_id = ListPlayers().list_players(player_list_by_name)
        return player_id

    def players_lists_by_ranking(self, tournament_id: int) -> int:
        """Read all of tournament's players order by ranking. User can select one of them

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - Player's Identifier of user's selected player
        """
        player_list_by_ranking = RequestsPlayer().read_player_by_ranking(tournament_id)
        player_id = ListPlayers().list_players(player_list_by_ranking)
        return player_id

    def players_lists_by_points(self, tournament_id: int) -> int:
        """Read all of tournament's players order by points. User can select one of them

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - Player's Identifier of user's selected player
        """
        player_list_by_points = RequestsPlayer().read_player_by_points(tournament_id)
        player_id = ListPlayers().list_players(player_list_by_points)
        return player_id
