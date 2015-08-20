__author__ = 'joecken'


class Player:
    """Simple object to hold player details"""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color


class Game:
    """Communicates with the Players and Robot for the Controller"""

    def __init__(self):
        self.players = []
        self.board = [["" for x in range(6)] for y in range(7)]
        self.turn = 0

    def add_player(self, name, color):
        """
        Adds Player with requested name to the players list.
        :param name: Player's name
        :param color: color of Player's tokens
        :return: Returns None
        """
        self.players.append(Player(name, color))

    def update_board(self, column):
        pass

    def get_current_player(self):
        pass

    def update_player(self):
        pass

    def get_board(self):
        pass