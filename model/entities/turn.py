#! /usr/bin/envs python3
# coding: utf-8
import datetime


class Turn:

    def __init__(self, name: str) -> None:
        """Create an object turn

         Attrs:
         - name (name): Turn's name
        """
        self.name = name
        self.date_begining = datetime.date.today()
        self.date_end = None
        self.game_lists = None
