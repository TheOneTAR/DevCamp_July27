__author__ = 'joecken'

import unittest

from connect4_game import Game


class Connect4UpdatePlayerTest(unittest.TestCase):
    """Tests the Game's update_player method."""

    def setUp(self):
        self.game = Game()
        self.game.add_player("Tiffany", "\u25cb")
        self.game.add_player("Kyle", "\u25cf")

    def tearDown(self):
        del self.game

    def test_update_player(self):
        """
        Ensures that the game increments the turn when asked.
        :return: Returns None
        """
        self.game.update_player()
        self.assertEqual(self.game.turn, 1, "Fails to increment Game.turn")


if __name__ == '__main__':
    unittest.main()
