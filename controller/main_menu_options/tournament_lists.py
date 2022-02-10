#! /usr/bin/envs python3
# coding: utf-8
from view.lists.list_tournaments import ListTournamentsMenu
from model.requests.request_tournament import RequestsTournament


class TournamentLists:
    def tournament_lists(self) -> int:
        """Read all of tournaments. User can select one of them

        Returns:
        - tournament_id (int): Tournament's identifier selected by user
        """
        tournaments_list = RequestsTournament().read_tournaments_list()
        tournament_id = ListTournamentsMenu().lists_tournaments(tournaments_list)
        return tournament_id

    def tournament_lists_completed(self) -> int:
        """Read all of completed tournaments. User can select one of them

        Returns:
        - tournament_id (int): Tournament's identifier selected by user
        """
        tournaments_list = RequestsTournament().read_tournaments_completed()
        tournament_id = ListTournamentsMenu().lists_tournaments(tournaments_list)
        return tournament_id

    def tournament_lists_inprocess(self) -> int:
        """Read all of tournaments in process. User can select one of them

        Returns:
        - tournament_id (int): Tournament's identifier selected by user
        """
        tournaments_list = RequestsTournament().read_tournaments_inprocess()
        tournament_id = ListTournamentsMenu().lists_tournaments(tournaments_list)
        return tournament_id
