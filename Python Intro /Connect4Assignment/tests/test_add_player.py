__author__ = 'joecken'

import unittest

from connect4_game import Player, Game


class Connect4AddPlayerTest(unittest.TestCase):
    """Tests the add_player method of the Game"""

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        del self.game

    def test_with_first_player(self):
        """
        Ensure that the Game correctly adds Players to its list.
        :return: Returns None
        """
        self.game.add_player("Peele", "red")
        self.assertEqual(
            len(self.game.players),
            1,
            "Failed to add Player to players"
        )
        self.assertEqual(
            self.game.players[0],
            Player("Peele", "red"),
            "Failed to instantiate Player correctly"
        )

    def test_with_second_player(self):
        """
        Ensure that the Game correctly adds the second Player
        :return: Returns None
        """
        self.game.add_player("Peele", "red")
        self.game.add_player("Tennille", "yellow")
        self.assertEqual(
            len(self.game.players),
            2,
            "Failed to add second Player to players"
        )
        self.assertEqual(
            self.game.players[1],
            Player("Tennille", "yellow"),
            "Failed to instantiate Player correctly"
        )


if __name__ == '__main__':
    unittest.main()
