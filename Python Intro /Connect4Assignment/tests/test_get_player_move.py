__author__ = 'kielejocain'

import unittest
from unittest.mock import patch
from io import StringIO

from connect4_view import View


class Connect4GetPlayerMoveTest(unittest.TestCase):
    """Test the Get Player Move method from the View"""

    def setUp(self):
        self.view = View()

    def tearDown(self):
        del self.view

    @patch('builtins.input', return_value="1")
    def test_with_no_message(self, inputted_value):
        """
        Ensures that the view correctly handles a standard move input.
        :param inputted_value: string passed in by mock.patch
        :return: NoneType
        """
        return_value = self.view.get_player_move()
        self.assertEqual(return_value, 1, "get_player_move should return 1")

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=StringIO)
    def test_with_message(self, output, inputted_value):
        """
        Ensures that the view correctly handles a passed in message.
        :param inputted_value: string passed in by mock.patch
        :param output: string printed to stdout by the function
        :return: NoneType
        """
        return_value = self.view.get_player_move(msg="Not so much.")
        self.assertEqual(
            output.getvalue(),
            "Not so much.\n",
            "Message is not printing correctly"
        )
        self.assertEqual(return_value, 3, "get_player_move should return 3")

    @patch('builtins.input', side_effect=["", "4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_with_no_response(self, output, inputted_value):
        """
        Ensures that the view will reject an empty string as a move
        and press for a new answer.
        :param inputted_value: strings passed in by mock.patch
        :param output: strings printed to stdout by the function
        :return: NoneType
        """
        return_value = self.view.get_player_move()
        self.assertEqual(
            output.getvalue(),
            "That is not a valid move.\n",
            "Empty string warning is incorrect"
        )
        self.assertEqual(return_value, 4, "get_player_move should return 4")

    @patch('builtins.input', side_effect=["10", "-3", "2"])
    def test_with_invalid_int(self, inputted_value):
        """
        Ensures that the view properly rejects invalid integers.
        :param inputted_value:
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
