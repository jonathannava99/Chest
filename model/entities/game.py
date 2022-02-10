#! /usr/bin/envs python3
# coding: utf-8

class Game:

    def __init__(self, player1: int, player2: int, score: tuple) -> None:
        """Create an object game

        Attrs:
        - player1(int): Id player 1
        - player2(int): Id player 2
        -score(tuple): Game's score
        """
        self.player1 = player1
        self.player2 = player2
        self.score = score
