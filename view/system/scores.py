#! /usr/bin/envs python3
# coding: utf-8

import inquirer


class Scores:

    def insert_scores(self) -> tuple:
        """Ask the score of two players and load the scores in a dictionnary

        Returns:
        - A tuple of the scores of two players
        """
        score_infos = [
            inquirer.Text('score_joueur_1', message="Score joueur 1"),
            inquirer.Text('score_joueur_2', message="Score joueur 2"),
        ]
        scores = inquirer.prompt(score_infos)
        score = {"scores": scores}
        score = (score["scores"]["score_joueur_1"], score["scores"]["score_joueur_2"])
        return score
