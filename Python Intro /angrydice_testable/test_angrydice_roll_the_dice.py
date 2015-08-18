__author__ = 'TheOneTAR'

import unittest
from angry_dice import AngryDiceGame
from die import Die


class AngryDiceRollDiceTest(unittest.TestCase):

    def test_roll_empty_list(self):
        angry_game = AngryDiceGame()
        exception = False

        try:
            angry_game.roll_the_dice([])
        except:
            exception = True

        self.assertFalse(exception)

    def test_roll_invalid_input(self):
        angry_game = AngryDiceGame()

        try:
            angry_game.roll_the_dice(2)
        except TypeError:
            self.assertTrue(False, "Invalid type passed and not handled.")

    def test_roll_one_die(self):
        angry_game = AngryDiceGame()

        single_die = Die([1,2,3,"Dog"])
        single_die.currentValue = 7
        single_die_list = angry_game.roll_the_dice([single_die])

        self.assertNotEqual(single_die_list[0], 7)

if __name__ == '__main__':
    unittest.main()
