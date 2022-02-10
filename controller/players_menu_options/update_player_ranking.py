#! /usr/bin/envs python3
# coding: utf-8
from model.requests.request_player import RequestsPlayer
from view.system.update_player import UpdatePlayer


class UpdatePlayerRanking:

    def players_update_ranking(self, player_id: int) -> None:
        """Update player ranking. User insert a new ranking. New ranking
        is insert into database.

        Attr:
        - player_id (int): PPlayer's identifier

        Returns:
        - Player's Identifier of user's selected player
        """
        new_ranking = UpdatePlayer()
        ranking = new_ranking.insert_new_ranking()
        player_ranking = RequestsPlayer()
        player_ranking.update_player_ranking(ranking, player_id)
