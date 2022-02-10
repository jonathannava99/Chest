#! /usr/bin/envs python3
# coding: utf-8

import inquirer
import os

NOMBRE_JOUEURS = 4


class TournamentCreation:

    def create_players(self) -> list:
        """Create the players of the tournament asking the user theirs informations.
        We create a list with the informations tha we want from the user

        Returns:
        - A list with all of the players end theirs respective informations
        """
        players = []

        print("\nAjoutez", NOMBRE_JOUEURS, "joueurs:\n")

        for i in range(NOMBRE_JOUEURS):
            print("Ajouter le joueur n°", i + 1, "\n")
            player_infos = [
                inquirer.Text('name_player', message="Prenom du joueur"),
                inquirer.Text('last_name', message="Nom de famille du joueur"),
                inquirer.Text('sex', message="Sexe"),
                inquirer.Text('birth_player', message="Date de naissance"),
                inquirer.Text('ranking', message="Classement",)
            ]
            player = inquirer.prompt(player_infos)
            players.append(player)
            os.system('clear')

        return players

    def create_tournament(self) -> dict:
        """Create the tournament asking the user theirs informations.
        We create a list with the informations tha we want from the user

        Returns:
        - A dictionnary with all of the players end theirs respective informations and with
        the tournament and its informations
        """
        tournament_infos = [
            inquirer.Text('name_tournament', message="Nom du tournoi"),
            inquirer.Text('place', message="Lieu du tournoi"),
            inquirer.Text('turns', message="Nombre de tours"),
            inquirer.Text('description', message="Description du tournoi"),
            inquirer.Text('date_tournament', message="Date")
        ]

        os.system('clear')
        tournament = inquirer.prompt(tournament_infos)
        tournament = {"tournament": tournament, "players": self.create_players()}
        return tournament
