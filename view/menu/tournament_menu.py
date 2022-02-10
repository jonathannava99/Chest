#! /usr/bin/envs python3
# coding: utf-8
from controller.game_system.play_tournament import Play
from view.lists.template_list import TemplateList
from view.menu.template_menu import TemplateMenu


class TournamentMenu(TemplateMenu):

    def tournament_menu(self, tournament_id: int) -> str:
        """Create the tournament menu with the options inside the list.

        Attrs:
        - tournament_id (int): l'identifiant du tournoi

        Returns:
        - A string of the option choosen
        """
        play = Play()
        menu = ['0.Revenir en arrière',
                "1.Menu Joueurs",
                "2.Liste de tous les tours du tournoi",
                "3.Liste de tous les matchs du tournoi"]
        if play.begin_verfication(tournament_id):
            menu.insert(len(menu), "4.Commencer le tournoi")
        elif play.end_tournament(tournament_id):
            menu.insert(len(menu), "4.Tournoi terminé")
        else:
            menu.insert(len(menu), "4.Continuer le tournoi")

        return TemplateList().choicelist("Choissisez une option", menu)
