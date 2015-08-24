__author__ = 'joecken'

import unittest

from connect4_game import Player, Game


class Connect4GetCurrentPlayerTest(unittest.TestCase):
    """Tests the Game's get_current_player method."""

    def setUp(self):
        self.game = Game()
        self.game.add_player("Tiffany", "\u25cb")
        self.game.add_player("Kyle", "\u25cf")

    def tearDown(self):
        del self.game

    def test_player_one(self):
        """
        Ensures the Game returns the first Player if turn is even
        :return: Returns None
        """
        self.game.turn = 8
        current_player = self.game.get_current_player()
        self.assertEqual(current_player, Player("Tiffany", "\u25cb"))

    def test_player_two(self):
        """
        Ensures the Game returns the second Player if turn is odd
        :return: Returns None
        """
        self.game.turn = 17
        current_player = self.game.get_current_player()
        self.assertEqual(current_player, Player("Kyle", "\u25cf"))


if __name__ == '__main__':
    unittest.main()
