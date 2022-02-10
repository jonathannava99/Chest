#! /usr/bin/envs python3
# coding: utf-8
from model.entities.player import Player
from model.requests.request_player import RequestsPlayer
from view.system.tournament_creation import TournamentCreation
from model.entities.tournament import Tournament
from model.requests.request_tournament import RequestsTournament


class CreateTournament:
    def create_tournament(self) -> None:
        """Create tournament and players and insert into the database

        Attr:
        - tournament_id (int): Tournament's identifier
        """
        tournament_creation_view = TournamentCreation().create_tournament()
        tournament_infos = tournament_creation_view['tournament']
        tournament = Tournament(tournament_infos)
        RequestsTournament().create_tournament(tournament)
        self.create_players(tournament_creation_view)

    def create_players(self, players_infos: dict) -> None:
        """Create players and insert into the database

        Attr:
        - players_infos(dict): dictionary with player's infos
        """
        tournament_id = RequestsTournament().read_tournament_id()
        player_file = players_infos["players"]
        for player_infos in player_file:
            request_player = RequestsPlayer()
            player = Player(player_infos)
            request_player.create_player(player, tournament_id)
