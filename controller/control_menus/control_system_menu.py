#! /usr/bin/envs python3
# coding: utf-8
from controller.game_system.game_system import GameSystem
from controller.game_system.play_tournament import Play
from controller.game_system.swiss_game import SwissGame


class SystemMenu:

    def system_menu(self, tournament_id: int, option: str) -> None:
        """The system menu of the tournament during tournament is in process

        Attrs:
        - tournament_id(int): Tournament's identifier
        - option(str): Option selected by the user
        """
        system = GameSystem()
        # start the tournament
        if option == "4.Commencer le tournoi":
            index = 1
            turn_id, players = system.start_tournament(tournament_id, index)
            self.chose_option(players, index, turn_id, tournament_id)

        elif option == "4.Continuer le tournoi":
            # continue tournament
            play = Play()
            swissgame = SwissGame()
            turn_id, index, player = system.continue_tournament(tournament_id)
            if index == 0:
                print("")
            else:
                # first turn
                if int(index) == 1:
                    list_players = player.read_player_by_ranking(tournament_id)
                    swiss_game = swissgame.swiss_game_first_turn(list_players)
                else:
                    # others turn
                    list_players = player.read_player_by_points(tournament_id)
                    swiss_game = swissgame.swiss_game_others_turn(list_players)
                # games of the current turn
                players = play.swiss_tournament(index, swiss_game)
                self.chose_option(players, index, turn_id, tournament_id)
        else:
            # Tournament finished
            system.update_tournament_status(tournament_id)

    def chose_option(self, players: [str, list], index: int, turn_id: int, tournament_id: int) -> None:
        """Inside the option: "4.Continuer le tournoi" user has to choose
        between 3 options "Valider letour", "Revenir en arrière" or default option

        Attrs:
        - players(list): List of games done with the swiss game system
        - index(int): Number of the current turn
        - turn_id(int): Turn's Identifier
        - tournament_id(int): Tournament's identifier
        """
        system = GameSystem()
        if players == "Valider le tour: {}".format(index):
            system.new_turn(tournament_id, turn_id, index)
        elif players == "Revenir en arrière":
            pass
        else:
            system.creating_game(players, turn_id, tournament_id)
