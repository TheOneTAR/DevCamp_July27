__author__ = 'TheOneTAR'

from connect4_view import View
from connect4_game import Game


class Connect4:
    """The Controller for the Connect 4 game."""
    def main(self):
        pass

    def __init__(self):
        self.view = View()
        self.model = Game()

    def create_player(self, token):
        """
        Create a player by prompting for their name,
        and then storing that in the model Game.
        :param token: color this player's pieces will be
        :return: Returns None
        """
        name = self.view.get_player_name()
        self.model.add_player(name, token)

    def get_move(self):
        """
        Gets a move from the user to pass to the game.
        :return: the column of Player's choice (int)
        """
        pass

    def check_move(self, board, column):
        """
        Verifies that a chosen move is legal.
        :param board: current state of the game board
        :param column: which column the player wants
        :return: whether the move is legal (bool)
        """
        pass

    def winner_check(self, board):
        """
        Looks to see if the player that just moved won.
        :param board: current state of the game board
        :return: whether the move is legal (bool)
        """
        pass

    def update_player(self):
        """
        Asks the game to update the turn and whether the
        game has ended in a tie.
        :return: whether the game ended in a tie (bool)
        """
        pass