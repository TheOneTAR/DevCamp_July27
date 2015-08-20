__author__ = 'joecken'


class View:
    """STWINGS"""

    def get_player_name(self):
        """
        Asks user for name, shortening if necessary.
        :return: A string of between 1 and 20 characters
        """
        name = input("Who you be?")
        if len(name) > 20:
            name = name.split()[0]
            if len(name) > 20:
                name = name[0:20]
            print("Wow, that's an impressive name. "
                  "How about we call you {}? Hi, {}!"
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