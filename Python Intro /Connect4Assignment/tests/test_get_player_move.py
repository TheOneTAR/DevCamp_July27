__author__ = 'kielejocain'

import unittest
from unittest.mock import patch
from io import StringIO

from connect4_view import View


class Connect4GetPlayerMoveTest(unittest.TestCase):
    """
    Testing the View's get_player_move function.
    """

    def setUp(self):
        self.view = View()

    def tearDown(self):
        del self.view

    @patch('builtins.input', side_effect=["", "4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_with_no_message(self, inputted_value, output):
        return_value = self.view.get_player_move()
        self.assertEqual(
            output.getvalue(),
            "That is not a valid move.\n",
            "Empty string warning is incorrect"
        )
        self.assertEqual(return_value, 4, "get_player_move should return 4")

if __name__ == '__main__':
    unittest.main()
