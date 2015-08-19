__author__ = 'TheOneTAR'

import unittest
from unittest.mock import patch
from angry_dice import AngryDiceGame


class AngryDiceMainTest(unittest.TestCase):

    @patch('builtins.input', return_value='')
    @patch.object(AngryDiceGame, 'check_cheating', autospec=True)
    def test_main_run(self, input_mock, mock_game_cheating):
        game = AngryDiceGame()
        game.current_stage = 3
        game.die_b.setDieFaceValue("5")
        game.die_a.setDieFaceValue("6")
        game.main()

        mock_game_cheating.assert_called_with(["Die B"])
if __name__ == '__main__':
    unittest.main()
