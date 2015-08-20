__author__ = 'TheOneTAR'

import unittest
from angry_dice import AngryDiceGame
from unittest.mock import patch
from io import StringIO


class AngryDiceCheckAngryTest(unittest.TestCase):

    def setUp(self):
        self.angry_game = AngryDiceGame()

    def tearDown(self):
        del self.angry_game

    @patch('sys.stdout', new_callable=StringIO)
    def test_both_die_angry(self, mock_stdout):
        """Set both dice to ANGRY and check that the game resets their game."""
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("ANGRY")

        angry_text = "WOW, you're ANGRY!\nTime to go back to Stage 1!\n"

        self.angry_game.check_angry()

        self.assertEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.angry_game.current_stage, 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_die_a_angry(self, mock_stdout):
        """Set both dice to ANGRY and check that the game resets their game."""
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("5")

        angry_text = "WOW, you're ANGRY!\nTime to go back to Stage 1!\n"
        self.angry_game.current_stage = 2
        self.angry_game.check_angry()

        self.assertNotEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.angry_game.current_stage, 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_die_b_angry(self, mock_stdout):
        """Set both dice to ANGRY and check that the game resets their game."""
        self.angry_game.die_b.setDieFaceValue("ANGRY")
        self.angry_game.die_a.setDieFaceValue("5")

        angry_text = "WOW, you're ANGRY!\nTime to go back to Stage 1!\n"
        self.angry_game.current_stage = 2
        self.angry_game.check_angry()

        self.assertNotEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.angry_game.current_stage, 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_neither_die_angry(self, mock_stdout):
        """Set both dice to ANGRY and check that the game resets their game."""
        self.angry_game.die_b.setDieFaceValue("2")
        self.angry_game.die_a.setDieFaceValue("5")

        angry_text = "WOW, you're ANGRY!\nTime to go back to Stage 1!\n"
        self.angry_game.current_stage = 2
        self.angry_game.check_angry()

        self.assertNotEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.angry_game.current_stage, 2)

if __name__ == '__main__':
    unittest.main()
