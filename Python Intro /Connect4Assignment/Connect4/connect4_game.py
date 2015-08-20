__author__ = 'joecken'


class Player:
    """Simple object to hold player details"""

    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __eq__(self, other):
        return self.name == other.name and self.token == other.token


class Game:
    """Communicates with the Players and Robot for the Controller"""

    def __init__(self):
        self.players = []
        self.board = [[" " for x in range(6)] for y in range(7)]
        self.turn = 0

    def add_player(self, name, token):
        """
        Adds Player with requested name to the players list.
        :param name: Player's name
        :param token: unicode character of Player's tokens
        :return: Returns None
        """
        self.players.append(Player(name, token))

    def update_board(self, index):
        column = self.board[index - 1]
        token = self.players[self.turn % 2].token
        for i, slot in enumerate(column):
            if slot == ' ':
                self.board[index - 1][i] = token
                break


    def get_current_player(self):
        pass

    def update_player(self):
        pass

    def get_board(self):
        pass