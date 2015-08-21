__author__ = 'TheOneTAR'

import unittest
from connect4 import Connect4
from unittest.mock import patch

class Connect4MoveTests(unittest.TestCase):
    """
    Tests to ensure that the get move function behaves connectly.
    """

    def setUp(self):
        self.game = Connect4()

    def tearDown(self):
        del self.game

    @patch('builtins.input', return_value='5')
    def test_get_move_valid(self, inputted_value):
        """
        Given a valid move from the view,
        and ensure that what is returned is an int.
        Convert that int to a valid column index.
        :return:
        """
        # Give 5
        column = self.game.get_move()

        # Ensure 4 is returned
        self.assertEqual(column, 4)

    def test_check_move_with_valid(self):
        """
        Given a valid column, return True.
        :return:
        """
        board = [
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            ["\u25cb"] + [" "] * 5,
            [" "] * 6,
            [" "] * 6
        ]
        valid = self.game.check_move(board, 3)
        self.assertTrue(valid)

    def test_check_move_with_invalid(self):
        """
        Given an invalid column, return False.
        :return:
        """
        board = [
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            ["\u25cb"] * 6,
            [" "] * 6,
            [" "] * 6
        ]
        valid = self.game.check_move(board, 4)
        self.assertFalse(valid)

    def test_check_move_with_barely_valid(self):
        """
        Given an invalid column, return False.
        :return:
        """
        board = [
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            ["\u25cb"] * 5 + [" "],
            [" "] * 6,
            [" "] * 6
        ]
        valid = self.game.check_move(board, 4)
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()
