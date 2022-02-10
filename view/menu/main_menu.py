#! /usr/bin/envs python3
# coding: utf-8
from view.menu.template_menu import TemplateMenu


class MainMenu(TemplateMenu):

    def create_menu(self) -> str:
        """Create the main menu with the options inside the list.

        Returns:
        - the number of the option chosen by the user
        """
        menu = ['1.Créer un tournoi', '2.Liste de tournois',
                '3.Tournois en cours', '4.Tournois terminés',
                '5.Effacer un tournoi', '6.Sortir']

        return self.choice_menu(menu)
