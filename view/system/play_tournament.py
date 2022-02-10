#! /usr/bin/envs python3
# coding: utf-8

from view.lists.template_list import TemplateList


class PlayTournament:

    def tournament_process(self, games_process: list, turn: str) -> tuple:
        """Create a menu with the list

        Attrs:
        - games_process (list): A list of games of a turn during the tournament
        - turn (string): Number round's turn

        Returns:
        - A tuple with the names of the two players or a string with the selected
        option
        """
        games_process.insert(len(games_process), "Valider le tour: {}".format(turn))
        games_process.insert(0, "Revenir en arrière")
        return self.list(games_process, turn)

    def list(self, list_elements: list, turn: str) -> [tuple, str]:
        """Create a menu with the list

         Attrs:
         - list_elements (string): A list that is in fact the list of a menu
         - turn (string): The identifier of a turn of the tournament

        Returns:
        - A tuple with the names and lastnames of the two players or a string with the selected
        option
        """
        object_id = TemplateList().choicelist("Choissisez le match à jouer", list_elements)
        if object_id != "Revenir en arrière" and object_id != "Valider le tour: {}".format(turn):
            object_id = object_id.split("(")
            player1 = object_id[0]
            player2 = object_id[1].split("-")[1]
            object_id = (player1, player2)
            return object_id

        else:
            return object_id
