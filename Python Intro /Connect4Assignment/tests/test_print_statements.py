__author__ = 'TheOneTAR'

import unittest
from connect4_view import View
from unittest.mock import patch
from io import StringIO


class StaticPrintStatements(unittest.TestCase):
    """Test that the needed static strings are printed correctly."""

    def setUp(self):
        self.view = View()

    def tearDown(self):
        del self.view

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_instructions(self, output):
        """
        Prints the instructions for how to play the game.
        :return: Returns None
        """

        self.view.show_instructions()

        instructions = "Let's play Connect 4! The first player to connect 4" \
                       "tokens of their color vertically, horizontally, " \
                       "or diagonally, wins. Players will alternate turns " \
                       "dropping checkers into the board, trying their " \
                       "best to win.\n\nOn a player's turn, they will be " \
                       "prompted to enter the column they want their piece " \
                       "dropped into.\n"

        self.assertEqual(instructions, output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_declare_sadness(self, output):
        """
        Prints a very sad message that the players have tied.
        :return: Returns None
        """
        self.view.declare_sadness()
        sadness = "Well, you both should be filled with an immense sadness," \
                  " as there is no winner. You have tied.\n"

        self.assertEqual(sadness, output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_declare_awesome(self, output):
        """
        Prints that someone is AWESOME, because they won the game.
        :return: Returns None
        """
        self.view.declare_awesome("Vlaad")

        awesome = "Woo! Who's awesome? Vlaad's AWESOME, cause Vlaad won!!\n"

        self.assertEqual(output.getvalue(), awesome)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_board(self, output):
        board = [['X', 'O', 'X', ' ', ' ', ' '],
                 ['O', 'X', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'X', ' ', ' ', ' '],
                 ['O', 'X', 'O', 'X', ' ', ' '],
                 ['X', 'O', 'X', ' ', ' ', ' '],
                 ['X', 'O', 'X', ' ', ' ', ' '],
                 ['O', 'X', ' ', ' ', ' ', ' ']]

        self.view.print_board(board)

        board_output = "\rConnect 4 Game:\n\n" \
                       "   | | | | | | | |\n"\
                       "   | | | | | | | |\n"\
                       "   | | | |X| | | |\n"\
                       "   |X|O|X|O|X|X| |\n"\
                       "   |O|X|O|X|O|O|X|\n"\
                       "   |X|O|X|O|X|X|O|\n"\
                       "   |-------------|\n"\
                       "   -             -\n"

        self.assertEqual(board_output, output.getvalue())



if __name__ == '__main__':
    unittest.main()
