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
        """Roll one die using the roll_the_dice function."""
        angry_game = AngryDiceGame()

        single_die = Die([1,2,3,"Dog"])
        single_die.currentValue = 7
        angry_game.roll_the_dice([single_die])

        self.assertNotEqual(single_die.currentValue, 7, "Die was not rolled")

    def test_roll_five_dice(self):
        """Roll five dice using the roll_the_dice function."""
        angry_game = AngryDiceGame()
        dice = []

        for i in range(5):
            dice.append(Die([1,2,3,"Dog"]))
            dice[i].currentValue = 7

        angry_game.roll_the_dice(dice)

        for die in dice:
            self.assertNotEqual(die.currentValue, 7,
                                "Die {} of 5 was not rolled"
                                .format(i+1))


if __name__ == '__main__':
    unittest.main()
