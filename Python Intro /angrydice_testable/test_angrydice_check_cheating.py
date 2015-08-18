__author__ = 'TheOneTAR'

import unittest
from angry_dice import AngryDiceGame
from unittest.mock import patch
from io import StringIO

class AngryDiceCheckCheatingTest(unittest.TestCase):

    def setUp(self):
        self.angry_game = AngryDiceGame()

    def tearDown(self):
        del self.angry_game

    @patch('sys.stdout', new_callable=StringIO)
    def test_stage_three_holding_six(self, mock_stdout):
        """Hold a 6 in Stage 3 and confirm user is found cheating."""
        self.angry_game.die_a.setDieFaceValue("5")
        self.angry_game.die_b.setDieFaceValue("6")
        self.angry_game.current_stage = 3

        self.angry_game.check_cheating([self.angry_game.die_a])

        self.assertEqual(mock_stdout.getvalue(),"You're cheating! You cannot "
                                                "lock a 6! You cannot win "
                                                "until you reroll it!\n")

        self.assertTrue(self.angry_game.cheating)

    @patch('sys.stdout', new_callable=StringIO)
    def test_stage_three_holding_five(self, mock_stdout):
        """Hold a 5 in Stage 3 and confirm user is not found cheating."""
        self.angry_game.die_a.setDieFaceValue("6")
        self.angry_game.die_b.setDieFaceValue("5")
        self.angry_game.current_stage = 3

        self.angry_game.check_cheating([self.angry_game.die_a])

        self.assertEqual(mock_stdout.getvalue(),"")

        self.assertFalse(self.angry_game.cheating)

    @patch('sys.stdout', new_callable=StringIO)
    def test_stage_three_not_holding_anything(self, mock_stdout):
        """Roll both dice in Stage 3 and confirm user is not found cheating."""
        self.angry_game.die_a.setDieFaceValue("6")
        self.angry_game.die_b.setDieFaceValue("5")
        self.angry_game.current_stage = 3

        self.angry_game.check_cheating([self.angry_game.die_a,
                                        self.angry_game.die_b])

        self.assertEqual(mock_stdout.getvalue(),"")

        self.assertFalse(self.angry_game.cheating)

    @patch('sys.stdout', new_callable=StringIO)
    def test_stage_three_holding_six_and_five(self, mock_stdout):
        """Hold a 6 & 5 in Stage 3 and confirm user is found cheating."""
        self.angry_game.die_a.setDieFaceValue("6")
        self.angry_game.die_b.setDieFaceValue("5")
        self.angry_game.current_stage = 3

        self.angry_game.check_cheating([])

        self.assertEqual(mock_stdout.getvalue(),"You're cheating! You cannot "
                                                "lock a 6! You cannot win "
                                                "until you reroll it!\n")

        self.assertTrue(self.angry_game.cheating)

if __name__ == '__main__':
    unittest.main()
