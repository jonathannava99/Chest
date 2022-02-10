#! /usr/bin/envs python3
# coding: utf-8
from datetime import datetime


class Player:

    def __init__(self, infos: dict) -> None:
        """Create an object player

        Attrs:
        - infos(dict): Player informations
        """
        self.name = infos["name_player"]
        self.sex = infos["sex"]
        self.lastName = infos["last_name"]
        self.birth = datetime.strptime(infos["birth_player"], "%Y-%m-%d")
        self.ranking = int(infos["ranking"])
