__author__ = 'TheOneTAR'

import unittest
from connect4_game import Player
from connect4 import Connect4
from unittest.mock import patch
from io import StringIO


class Connect4CreatePlayerTest(unittest.TestCase):
    """Ensure that players are properly created and stored."""

    def setUp(self):
        self.game = Connect4()

    def tearDown(self):
        del self.game

    @patch('builtins.input', return_value='Rob-E')
    def test_create_valid_player(self, inputted_value):
        """
        Create a player using a valid name.
        :return:
        """
        self.game.create_player('W')

        self.assertIn(Player('Rob-E','W'), self.game.model.players)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='')
    def test_create_valid_player(self, inputted_value, output):
        """
        Create a player using a valid name.
        :return:
        """
        self.game.create_player('W')

        # A Player did get made
        # The player does have a name
        # The player's color is what we picked.
        self.assertEqual(len(self.game.model.players), 1)
        self.assertEqual(self.game.model.players[0].token, 'W')


if __name__ == '__main__':
    unittest.main()
