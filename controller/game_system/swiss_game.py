#! /usr/bin/envs python3
# coding: utf-8
import random as random


class SwissGame:

    def swiss_game_first_turn(self, list_ranking: list) -> list:
        """Games order by swiss game rules for the first turn

         Attr:
         - list_ranking(list): List of players order by ranking

         Returns:
        - a format list of games order by swiss game
        """
        player_lists = list_ranking
        size = len(player_lists) // 2
        games = []
        for player in range(size):
            player1 = player_lists[player]
            player2 = player_lists[(size + player)]
            player1 = self.formatplayer(player1)
            player2 = self.formatplayer(player2)
            colors = self.color_player()
            games += ["{}(en {}) - {}(en {})".format(player1, colors[0], player2, colors[1])]

        return games

    def swiss_game_others_turn(self, list_points: list) -> list:
        """Games order by swiss game rules for the other turns

         Attr:
         - list_ranking(list): List of players order by points

         Returns:
        - a format list of games order by swiss game
        """
        player_lists = list_points
        size = len(player_lists)
        games = []
        for player in range(0, size, 2):
            first_player = player_lists[player]
            second_player = player_lists[(player + 1)]
            player1, player2, color_player1, color_player2 = self.format_swiss_game(first_player, second_player)
            games += ["{}(en {}) - {}(en {})".format(player1, color_player1, player2, color_player2)]

        return games

    def format_swiss_game(self, first_player: str, second_player: str) -> tuple:
        """Games order by swiss game rules for the first turn

         Attr:
         - first_player(list): a string with the infos of the first player
         - second_player(list): a string with the infos of the second player

         Returns:
        - a tuple with first_player identifier, second player identifier,
        color player1 and color player2
        """
        first_player = self.formatplayer(first_player)
        second_player = self.formatplayer(second_player)
        colors = self.color_player()
        color_player1 = colors[0]
        color_player2 = colors[1]
        return first_player, second_player, color_player1, color_player2

    def color_player(self) -> list:
        """Colors of chest order randomly

        Returns:
        - list of colors order randomly
        """
        colors = ["noir", "blanc"]
        random.shuffle(colors)
        return colors

    def formatplayer(self, player: str) -> str:
        """Format the string to get player identifier

         Attr:
         - player(str): A string with player's infos

        Returns:
        - player identifier in string format
        """
        player = player.split(" ")
        player = "".join(player)
        player = player.split(",")
        del player[3:]
        player = " ".join(player)
        player = player.replace("Prenom:", "")
        player = player.replace("Nom:", "")
        player = player.replace("id:", "")
        player = player.strip()
        player = player.split(" ")
        player_id = ""
        for i in player:
            if i.isdigit():
                player.index(i)
                player.remove(i)
        player = " ".join(player)
        final_player = {player_id: player}
        return final_player[player_id]
