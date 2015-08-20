__author__ = 'joecken'

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
        :return: None
        """
        awesome = "Woo! Who's awesome? {}'s AWESOME, cause {} won!!"\
                  .format(player_name, player_name)

        print(awesome)