__author__ = 'TheOneTAR'

import unittest
from connect4 import Connect4


class Connect4EndGameConditionTests(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def tearDown(self):
        del self.game

    def test_win_for_X_horizontal(self):

        board = [['O','O','X',' ',' ',' '],
                 ['O','X','O',' ',' ',' '],
                 ['O','X','X',' ',' ',' '],
                 ['O','X','O','X',' ',' '],
                 ['X','X','X','',' ',' '],
                 ['X','O','X',' ',' ',' '],
                 ['O','X',' ',' ',' ',' ']]

        win = self.game.winner_check(board, 'X')
        self.assertTrue(win)

    def test_win_for_X_vertical(self):

        board = [['O','O','X',' ',' ',' '],
                 ['O','X','O',' ',' ',' '],
                 ['O','O','X',' ',' ',' '],
                 ['X','X','X','X',' ',' '],
                 ['X','X','X','',' ',' '],
                 ['X','O','X',' ',' ',' '],
                 ['O','X',' ',' ',' ',' ']]

        win = self.game.winner_check(board, 'X')
        self.assertTrue(win)

    def test_win_for_X_diagonal_right(self):

        board = [['O','O','X',' ',' ',' '],
                 ['O','X','O','O',' ',' '],
                 ['X','O','O',' ',' ',' '],
                 ['X','X','O','X',' ',' '],
                 ['O','X','X',' ',' ',' '],
                 ['X','O','X','X',' ',' '],
                 ['O','X',' ',' ',' ',' ']]

        win = self.game.winner_check(board, 'X')
        self.assertTrue(win)

    def test_win_for_X_diagonal_left(self):

        board = [['O','O','X',' ',' ',' '],
                 ['O','X','O',' ',' ',' '],
                 ['O','O','O','X',' ',' '],
                 ['X','O','X','X',' ',' '],
                 ['O','X','X',' ',' ',' '],
                 ['X','O','X',' ',' ',' '],
                 ['O','X',' ',' ',' ',' ']]

        win = self.game.winner_check(board, 'X')
        self.assertTrue(win)

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
