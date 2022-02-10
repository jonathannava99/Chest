#! /usr/bin/envs python3
# coding: utf-8
from view.lists.template_list import TemplateList


class ListPlayers(TemplateList):

    def list_players(self, players: list) -> int:
        """Create a the list of players that the user can select

         Attrs:
         - players (list): List of players

        Returns:
        - A number int that represents the option selected by the user
        """
        return self.list(players, "Il n'y a pas de joueurs disponibles", "Voici la liste de joueurs")
