__author__ = 'TheOneTAR'

import unittest
from die import Die

class TestDieRoll(unittest.TestCase):

    def setUp(self):
        """Setup to run Die roll tests, by making a die."""
        self.test_values = ["1","2","TEST","4","DOG"]
        self.test_die = Die(self.test_values)

        print("TestDie: Test Begin")

        print(self.shortDescription())

    def test_single_roll(self):
        """Roll the Test Die and determine if the outcome is in test_values."""
        self.assertIn(self.test_die.roll(),self.test_values)

    def test_multiple_rolls(self):
        """Roll the die 10 times and ensure that it changes at least once."""
        previous_roll = self.test_die.roll()
        for i in range(10):
            if self.test_die.roll() != previous_roll:
                return True

        return False



    def tearDown(self):
        print("TestDie: Test End")

if __name__ == '__main__':
    unittest.main()