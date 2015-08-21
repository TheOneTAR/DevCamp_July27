__author__ = 'joecken'

import unittest

from connect4_game import Game


class Connect4UpdateBoardTest(unittest.TestCase):
    """Tests the Game.update_board method."""

    def setUp(self):
        self.game = Game()
        self.game.add_player("Tiffany", "\u25cb")
        self.game.add_player("Kyle", "\u25cf")

    def tearDown(self):
        del self.game

    def test_with_token_one(self):
        self.game.update_board(5)

        board = [
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            ["\u25cb"] + [" "] * 5,
            [" "] * 6,
            [" "] * 6
        ]

        self.assertEqual(
            self.game.board,
            board,
            "Fails to update first in column correctly"
        )

    def test_with_token_two(self):
        self.game.update_board(5)
        self.game.turn += 1
        self.game.update_board(5)

        board = [
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            [" "] * 6,
            ["\u25cb"] + ["\u25cf"] + [" "] * 4,
            [" "] * 6,
            [" "] * 6
        ]

        self.assertEqual(
            self.game.board,
            board,
            "Fails to update first in column correctly"
        )


if __name__ == '__main__':
    unittest.main()
