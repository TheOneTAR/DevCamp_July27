__author__ = 'TheOneTAR'

import unittest
from angry_dice import AngryDiceGame
from unittest.mock import patch
from io import StringIO


class AngryDicePrintDiceTest(unittest.TestCase):

    def setUp(self):
        self.angry_game = AngryDiceGame()

    def tearDown(self):
        del self.angry_game

    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_die_values(self, mock_stdout):
        """Set both dice to ANGRY and check that the game resets their game."""
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("4")

        printed_die_string = "You rolled:\n   a = [  {}  ]\n   b = [  {}  ]" \
                             "\n\nYou are in Stage {}\n".format("ANGRY", "4", 1)

        self.angry_game.print_dice()

        self.assertEqual(mock_stdout.getvalue(), printed_die_string)


if __name__ == '__main__':
    unittest.main()
