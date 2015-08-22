__author__ = 'TheOneTAR'

from connect4_view import View
from connect4_game import Game
from itertools import product


class Connect4:
    """The Controller for the Connect 4 game."""

    def __init__(self):
        self.view = View()
        self.model = Game()

    def main(self):

        # Clear the console, and print the instructions.
        self.view.show_instructions()

        # Create the two players
        self.create_player('\u25cf')
        self.create_player('\u25cb')

        while not self.update_player():
            move = -1
            msg = ""
            while move < 0:
                self.view.print_board(self.model.get_board())
                move = self.get_move(self.model.get_current_player().name, msg)
                if self.check_move(self.model.get_board(), move):
                    row = self.model.update_board(move)
                    self.model.get_board()[move][row] = ' '
                    self.view.animate_turn(move,
                                           row,
                                           self.model.get_current_player().token,
                                           self.model.get_board())
                else:
                    msg = "That move is not legal; the column is full."
                    move = -1
            is_won = self.winner_check(
                self.model.get_board(),
                self.model.get_current_player().token
            )
            if is_won:
                self.view.declare_awesome(
                    self.model.get_current_player().name
                )
                break
        else:
            self.view.declare_sadness()


    def create_player(self, token):
        """
        Create a player by prompting for their name,
        and then storing that in the model Game.
        :param token: color this player's pieces will be
        :return: Returns None
        """
        name = self.view.get_player_name()
        self.model.add_player(name, token)

    def get_move(self, name, msg=""):
        """
        Gets a move from the user to pass to the game.
        :return: the column of Player's choice (int)
        """
        return self.view.get_player_move(name, msg) - 1

    def check_move(self, board, column):
        """
        Verifies that a chosen move is legal.
        :param board: current state of the game board
        :param column: which column the player wants
        :return: whether the move is legal (bool)
        """
        # Check to make sure the column is not full.
        if board[column][5] == ' ':
            return True

        return False

    def winner_check(self, board, token):
        """
        Looks to see if the player that just moved won.
        :param board: current state of the game board
        :return: whether the move is legal (bool)
        """

        # Vertical
        # for each column, make it a string, look for substring of four in a row
        for col in board:
            if (token * 4) in ''.join(col):
                return True

        # Horizontal
        for i in range(6):
            if (token * 4) in ''.join(column[i] for column in board):
                return True

        # Diagonal Right

        for i,j in product(range(4),range(3)):
            if (token * 4) in ''.join(board[i+k][j+k] for k in range(4)):
                return True

        # Diagonal Left
        for i,j in product(range(4),range(3,6)):
            if (token * 4) in ''.join(board[i+k][j-k] for k in range(4)):
                return True

        # No solution found, so return False
        return False

    def update_player(self):
        """
        Asks the game to update the turn and whether the
        game has ended in a tie.
        :return: whether the game ended in a tie (bool)
        """
        self.model.update_player()

        if self.model.turn == 42:
            return True

        return False

if __name__ == '__main__':
    controller = Connect4()
    controller.main()