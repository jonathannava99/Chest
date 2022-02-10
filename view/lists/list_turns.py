#! /usr/bin/envs python3
# coding: utf-8

from view.lists.template_list import TemplateList


class ListTurns(TemplateList):

    def list_turns(self, turns: list) -> int:
        """Create a the list of turns that the user can select

         Attrs:
         - turns (list): List of turns

        Returns:
        - A number int that represents the option selected by the user
        """
        return self.list(turns, "Il n'y a pas de tours disponibles", "Choissisez un tour")

    def list_turn(self, turn: list) -> str:
        """Create a the list with one turn that the user can select

         Attrs:
         - turn (list): List with one turn

        Returns:
        - A stirg with the selected choice
        """
        turn.insert(0, "Revenir en arrière")
        return self.choicelist("Choissisez le tour", turn)
