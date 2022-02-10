#! /usr/bin/envs python3
# coding: utf-8

import inquirer


class UpdatePlayer:

    def insert_new_ranking(self) -> str:
        """User insert a new ranking for the player

        Returns:
        - A new ranking in string format
        """
        ranking_update = [
            inquirer.Text('ranking', message="Changer le classement")
        ]
        ranking = inquirer.prompt(ranking_update)
        ranking_update = ranking['ranking']
        return ranking_update
