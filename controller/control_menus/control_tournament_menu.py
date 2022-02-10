#! /usr/bin/envs python3
# coding: utf-8
from controller.control_menus.control_player_menu import ControlPlayermenu
from controller.control_menus.control_system_menu import SystemMenu
from controller.tournament_menu_options.list_turns import TurnLists
from controller.tournament_menu_options.lists_games import GameLists
from view.menu.tournament_menu import TournamentMenu

SORTIR = "0.Revenir en arrière"


class ControlTournamentmenu:

    def __init__(self):
        pass

    def changeView(self, tournament_id: [str, int]):
        """Player menu. User can select an option. Each option do a certain instructions
         Attr:
         - tournament_id (int): Tournament's identifier
         """

        menu = TournamentMenu()
        option = menu.tournament_menu(tournament_id)
        while option != SORTIR:
            if option[0] == "1":
                ControlPlayermenu().changeView(tournament_id)
                option = menu.tournament_menu(tournament_id)

            elif option[0] == "2":
                turns = TurnLists()
                turn_id = turns.lists_turns(tournament_id)
                if str(turn_id).isdigit():
                    game = GameLists()
                    game.games_turn(tournament_id, turn_id)
                    option = "2"
                else:
                    option = menu.tournament_menu(tournament_id)

            elif option[0] == "3":
                game = GameLists()
                game.games_tournament(tournament_id)
                option = menu.tournament_menu(tournament_id)

            elif option[0] == "4":
                system_menu = SystemMenu()
                system_menu.system_menu(tournament_id, option)
                option = menu.tournament_menu(tournament_id)
