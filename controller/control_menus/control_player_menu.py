#! /usr/bin/envs python3
# coding: utf-8

from controller.players_menu_options.lists_players import PlayerLists
from controller.players_menu_options.update_player_ranking import UpdatePlayerRanking
from view.menu.players_menu import PlayersMenu

SORTIR = "0"


class ControlPlayermenu:

    def __init__(self):
        pass

    def changeView(self, tournament_id: int) -> None:
        """Player menu. User can select an option. Each option do a certain instructions
        Attr:
        - tournament_id (int): Tournament's identifier
        """
        menu = PlayersMenu()
        option = menu.player_menu()
        while option != SORTIR:
            if option == "1":
                # read player list by name
                players_lists_by_name = PlayerLists()
                players_lists_by_name.players_lists_by_name(tournament_id)
                option = menu.player_menu()

            elif option == "2":
                # read player list by ranking
                players_lists_by_ranking = PlayerLists()
                players_lists_by_ranking.players_lists_by_ranking(tournament_id)
                option = menu.player_menu()

            elif option == "3":
                # read player list by points
                players_lists_by_points = PlayerLists()
                players_lists_by_points.players_lists_by_points(tournament_id)
                option = menu.player_menu()

            elif option == "4":
                # uodate ranking player
                players_lists_by_ranking = PlayerLists()
                player_id = players_lists_by_ranking.players_lists_by_ranking(tournament_id)
                if str(player_id).isdigit():
                    update_ranking = UpdatePlayerRanking()
                    update_ranking.players_update_ranking(player_id)
                else:
                    # revenir en arrière
                    option = menu.player_menu()
