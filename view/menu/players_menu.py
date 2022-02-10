#! /usr/bin/envs python3
# coding: utf-8

from view.menu.template_menu import TemplateMenu


class PlayersMenu(TemplateMenu):

    def player_menu(self) -> str:
        """Create the player menu with the options inside the list.

        Returns:
        - the number of the option chosen by the user
        """
        menu = ['0.Revenir en arrière',
                "1.Liste de tous les joueurs du tournoi par ordre alphabétique",
                "2.Liste de tous les joueurs du tournoi par classement",
                "3.Liste de tous les joueurs du tournoi par points",
                "4.Modifier le classement du joueur"]

        return self.choice_menu(menu)
