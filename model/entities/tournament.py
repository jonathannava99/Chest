#! /usr/bin/envs python3
# coding: utf-8

from datetime import datetime


class Tournament:

    def __init__(self, infos: dict, playersList=None) -> None:
        """Create an object tournament

        Attrs:
        - infos(dict): Tournament informations
        - playersList(list): Players informations
        """
        self.name = infos["name_tournament"]
        self.place = infos["place"]
        self.date = datetime.strptime(infos["date_tournament"], "%Y-%m-%d")
        self.number_of_turns = int(infos["turns"])
        self.description = infos["description"]
        self.playersList = playersList
