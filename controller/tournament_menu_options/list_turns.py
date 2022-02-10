#! /usr/bin/envs python3
# coding: utf-8
from view.lists.list_turns import ListTurns
from model.requests.request_turn import RequestsTurn


class TurnLists:

    def lists_turns(self, tournament_id: int) -> int:
        """Read all of tournament's turns. User can select one of them

        Attr:
        - tournament_id (int): Tournament's identifier

        Returns:
        - Turn's Identifier of user's selected turn
        """
        lists_turn = RequestsTurn()
        turns = lists_turn.lists_read_turn(tournament_id)
        turn_id = ListTurns().list_turns(turns)
        return turn_id

    def turn(self, tournament_id: int) -> int:
        """Read the last turn of the tournament. User can select one of them
        Attr:
        - tournament_id (int): Tournament's identifier
        Returns:
        - Turn's Identifier of user's selected turn
        """
        turn = RequestsTurn()
        turn = turn.read_a_turn(tournament_id)
        turn_id = ListTurns().list_turns(turn)
        return turn_id
