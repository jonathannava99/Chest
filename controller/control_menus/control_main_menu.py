#! /usr/bin/envs python3
# coding: utf-8
import sqlite3

from controller.control_menus.control_tournament_menu import ControlTournamentmenu
from controller.main_menu_options.create_tournament import CreateTournament
from controller.main_menu_options.delete_tournament import TournamentDelete
from controller.main_menu_options.tournament_lists import TournamentLists
from view.menu.main_menu import MainMenu

SORTIR = "6"


class ControlMainmenu:

    def __init__(self):
        pass

    def changeView(self) -> None:
        """The main menu of the tournament. User select an option
        and each option do some instructions
        """

        menu = MainMenu()
        option = menu.create_menu()
        while option != SORTIR:
            if option == "1":
                # créer le tournoi
                create_tournament = CreateTournament()
                create_tournament.create_tournament()
                option = menu.create_menu()

            elif option == "2":
                # liste de tournois
                tournament_lists = TournamentLists()
                option_tournament = tournament_lists.tournament_lists()
                if str(option_tournament).isdigit():
                    ControlTournamentmenu().changeView(option_tournament)
                else:
                    option = menu.create_menu()

            elif option == "3":
                # tournois en cours
                option_tournament = None
                try:
                    tournament_inprocess_id = TournamentLists()
                    option_tournament = tournament_inprocess_id.tournament_lists_inprocess()
                except IndexError:
                    print("Pas de tournois en cours")
                if str(option_tournament).isdigit():
                    ControlTournamentmenu().changeView(option_tournament)
                else:
                    option = menu.create_menu()

            elif option == "4":
                # tournois terminés
                option_tournament = None
                try:
                    tournament_completed_id = TournamentLists()
                    option_tournament = tournament_completed_id.tournament_lists_completed()
                except IndexError:
                    print("Pas de tournois terminés")
                if str(option_tournament).isdigit():
                    ControlTournamentmenu().changeView(option_tournament)
                else:
                    option = menu.create_menu()

            elif option == "5":
                # effacer un tournoi
                try:
                    delete = TournamentDelete()
                    delete.delete_tournament()
                except sqlite3.OperationalError:
                    print("Pas de tournoi à affacer")
                option = menu.create_menu()
