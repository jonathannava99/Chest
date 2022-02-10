#! /usr/bin/envs python3
# coding: utf-8

from view.lists.template_list import TemplateList


class ListTournamentsMenu(TemplateList):

    def lists_tournaments(self, tournaments: list) -> int:
        """Create a the list of tournaments that the user can select

         Attrs:
         - tournaments (list): List of tournaments

        Returns:
        - A number int that represents the option selected by the user
        """
        return self.list(tournaments, "Il n'y a pas de tournoi disponible", "Choissisez un tournoi")
