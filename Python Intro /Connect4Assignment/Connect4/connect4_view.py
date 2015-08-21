__author__ = 'joecken'

import os
import sys
import time
from random import choice


class View:
    """Communicates with the user as a proxy for the Controller"""

    def get_player_name(self):
        """
        Asks user for name, shortening if necessary.
        :return: A string of between 1 and 20 characters
        """
        name = input("Who you be?")
        if len(name) > 20 or not name:
            if len(name) > 20:
                name = name.split()[0][0:20]
                print("Wow, that's an impressive name.")
            else:
                with open('bin/names.txt') as f:
                    names = [line.rstrip() for line in f]
                name = choice(names)
                print("You don't care at all?")
            print("How about we call you {}? Hi, {}!"
                  .format(name, name))
        return name

    def get_player_move(self, msg=""):
        """
        Asks user for move, checks if intelligible and asks again
        if necessary.
        :param msg: Message to the user about last failure, if necessary
        :return: An integer representing the column in which to play
        """
        if msg != "":
            print(msg)
        move = ""
        while move == "":
            move = input("Where would you like to play?")
            try:
                move = int(move)
            except ValueError:
                move = 8
            if move not in range(1, 8):
                print("Please type only an integer from 1 to 7.")
                move = ""
        return move

    def show_instructions(self):
        """
        Print the instructions of how to play onto the screen.
        """
        instructions = "Let's play Connect 4! The first player to connect 4" \
                       "tokens of their color vertically, horizontally, " \
                       "or diagonally, wins. Players will alternate turns " \
                       "dropping checkers into the board, trying their " \
                       "best to win.\n\nOn a player's turn, they will be " \
                       "prompted to enter the column they want their piece " \
                       "dropped into."

        print(instructions)

    def declare_sadness(self):
        """
        Called when there's a tie to inform the players of how
        sad they should be.
        """
        sadness = "Well, you both should be filled with an immense sadness," \
                  " as there is no winner. You have tied."
        print(sadness)

    def declare_awesome(self, player_name):
        """
        Called when there is a winner to declare how
        awesome that player is.
        :param player_name: name of the winning player
        :return: Returns None
        """
        awesome = "Woo! Who's awesome? {}'s AWESOME, cause {} won!!"\
                  .format(player_name, player_name)

        print(awesome)

    def print_board(self, board):
        """
        Given a board, print the lists of lists.
        :param board: a list of lists that represents the game board
        :return: Returns None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.write("\r")
        for i in range(5, 0, -1):
            print('|', "|".join(column[i] for column in board), end='|\n', sep="")
        print("|-------------|")
        print("-             -")

        sys.stdout.flush()

    def add_token_to_board(self, target, token, board):
        """
        Adds a token to the board, via a cute animation.
        Due to the animation, this function is untestable.
        :param target: (column,row) tuple for where the piece is going.
        :return:
        """
        self._drop_piece(target, (target[0], -1), None, token, board)

    def _drop_piece(self, target, current, old, token, board):
        """
        Recursive function that animates a piece being added to the board.
        :param target: goal location
        :param current: where the token currently is
        :param old: where the token was
        :param token: the token being dropped
        :param board: the board itself
        :return:
        """
        if target != old:
            time.sleep(0.2)
            # Then 'drop' it down through the rows
            # Tuples is (column,row)
            if old is not None:
                board[old[0]][old[1]] = ' '
            board[current[0]][current[1]] = token
            new_current = (current[0], current[1]-1)
            self.print_board(board)

            # Recursive!
            self._drop_piece(target, new_current, current, token, board)
