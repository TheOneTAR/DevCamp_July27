__author__ = 'joecken'


class View:
    """STWINGS"""

    def get_player_name(self):
        name = input("Who you be?")
        if len(name) > 20:
            name = name.split()[0]
            if len(name) > 20:
                name = name[0:20]
            print("Wow, that's an impressive name. "
                  "How about we call you {}? Hi, {}!"
                  .format(name, name))
        return name