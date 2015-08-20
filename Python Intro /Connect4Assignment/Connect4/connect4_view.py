__author__ = 'joecken'

from random import choice


class View:
    """STWINGS"""

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