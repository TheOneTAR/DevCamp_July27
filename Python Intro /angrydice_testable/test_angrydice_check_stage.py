__author__ = 'TheOneTAR'

import unittest
from angry_dice import AngryDiceGame


class AngryDiceStageCheckTest(unittest.TestCase):

    def setUp(self):
        self.angry_game = AngryDiceGame()

    def tearDown(self):
        del self.angry_game

    def test_stage_one_to_stage_two_valid_inputs(self):
        self.angry_game.die_a.setDieFaceValue("1")
        self.angry_game.die_b.setDieFaceValue("2")
        self.angry_game.cheating = False

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    def test_stage_one_to_stage_two_invalid_inputs(self):
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("2")
        self.angry_game.cheating = False

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 1)

    def test_stage_one_to_stage_two_valid_cheating(self):
        self.angry_game.die_a.setDieFaceValue("1")
        self.angry_game.die_b.setDieFaceValue("2")
        self.angry_game.cheating = True

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 1)

    def test_stage_one_to_stage_two_cheating(self):
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("3")
        self.angry_game.cheating = True

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 1)

    def test_stage_two_to_stage_three_valid_inputs(self):
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("4")
        self.angry_game.cheating = False

        self.angry_game.current_stage = 2
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

    def test_stage_two_to_stage_three_invalid_inputs(self):
        self.angry_game.die_a.setDieFaceValue("5")
        self.angry_game.die_b.setDieFaceValue("4")
        self.angry_game.cheating = False

        self.angry_game.current_stage = 2
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    def test_stage_two_to_stage_three_valid_cheating(self):
        self.angry_game.die_a.setDieFaceValue("ANGRY")
        self.angry_game.die_b.setDieFaceValue("4")
        self.angry_game.cheating = True

        self.angry_game.current_stage = 2
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    def test_stage_two_to_stage_three_cheating(self):
        self.angry_game.die_a.setDieFaceValue("1")
        self.angry_game.die_b.setDieFaceValue("4")
        self.angry_game.cheating = True

        self.angry_game.current_stage = 2
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    def test_stage_three_to_stage_four_valid_inputs(self):
        self.angry_game.die_a.setDieFaceValue("5")
        self.angry_game.die_b.setDieFaceValue("6")
        self.angry_game.cheating = False

        self.angry_game.current_stage = 3
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 4)

    def test_stage_three_to_stage_four_invalid_inputs(self):
        self.angry_game.die_a.setDieFaceValue("1")
        self.angry_game.die_b.setDieFaceValue("3")
        self.angry_game.cheating = False

        self.angry_game.current_stage = 3
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

    def test_stage_three_to_stage_four_valid_cheating(self):
        self.angry_game.die_a.setDieFaceValue("5")
        self.angry_game.die_b.setDieFaceValue("6")
        self.angry_game.cheating = True

        self.angry_game.current_stage = 3
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

    def test_stage_three_to_stage_four_cheating(self):
        self.angry_game.die_a.setDieFaceValue("1")
        self.angry_game.die_b.setDieFaceValue("4")
        self.angry_game.cheating = True

        self.angry_game.current_stage = 3
        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

if __name__ == '__main__':
    unittest.main()
