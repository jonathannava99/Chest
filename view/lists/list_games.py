#! /usr/bin/envs python3
# coding: utf-8

from view.lists.template_list import TemplateList


class ListGames(TemplateList):

    def list_games(self, games):
        """Create a the list of games that the user can select

         Attrs:
         - games (list): List of games

        Returns:
        - A number int that represents the option selected by the user
        """
        return self.list(games, "Il n'y a pas de match disponible", "Voici la liste de matchs")
