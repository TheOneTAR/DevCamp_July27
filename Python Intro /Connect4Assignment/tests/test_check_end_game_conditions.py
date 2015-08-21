__author__ = 'TheOneTAR'

import unittest
from connect4 import Connect4



class Connect4EndGameConditionTests(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def tearDown(self):
        del self.game

    def test_update_player_tie(self):
        """
        Update the current player and determine a tie is True.
        """
        self.game.model.turn = 41
        tie = self.game.update_player()
        self.assertTrue(tie)


    def test_update_player_tie(self):
        """
        Update the current player and determine a tie is False.
        """
        self.game.model.turn = 30
        tie = self.game.update_player()
        self.assertFalse(tie)


if __name__ == '__main__':
    unittest.main()
