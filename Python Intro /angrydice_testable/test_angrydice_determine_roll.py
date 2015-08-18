__author__ = 'TheOneTAR'

import unittest
from angry_dice import AngryDiceGame
from unittest.mock import patch


class AngryDiceDetermineRollTest(unittest.TestCase):

    def setUp(self):
        self.angry_game = AngryDiceGame()

    def tearDown(self):
        del self.angry_game

    @patch('builtins.input', return_value='ab')
    def test_input_a_and_b(self, inputted_value):
        dice_to_roll = self.angry_game.determine_roll()

        self.assertIn(self.angry_game.die_a, dice_to_roll)
        self.assertIn(self.angry_game.die_b, dice_to_roll)


    @patch('builtins.input', return_value='b')
    def test_input_just_b(self, inputted_value):
        dice_to_roll = self.angry_game.determine_roll()

        self.assertNotIn(self.angry_game.die_a, dice_to_roll)
        self.assertIn(self.angry_game.die_b, dice_to_roll)


    @patch('builtins.input', return_value='a')
    def test_input_just_a(self, inputted_value):
        dice_to_roll = self.angry_game.determine_roll()

        self.assertNotIn(self.angry_game.die_b, dice_to_roll)
        self.assertIn(self.angry_game.die_a, dice_to_roll)

    @patch('builtins.input', return_value='')
    def test_input_just_a(self, inputted_value):
        dice_to_roll = self.angry_game.determine_roll()

        self.assertNotIn(self.angry_game.die_b, dice_to_roll)
        self.assertNotIn(self.angry_game.die_a, dice_to_roll)

if __name__ == '__main__':
    unittest.main()
