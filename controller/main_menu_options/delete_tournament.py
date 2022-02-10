#! /usr/bin/envs python3
# coding: utf-8
from controller.main_menu_options.tournament_lists import TournamentLists
from model.requests.request_tournament import RequestsTournament


class TournamentDelete:
    def delete_tournament(self) -> None:
        """Delete tournament selected by user
        """
        tournament_id = TournamentLists().tournament_lists()
        RequestsTournament().delete_tournament(tournament_id)
