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
        self.board = [[" " for _ in range(6)] for _ in range(7)]
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
        """
        Adds the proper token to the board in the column passed in
        by index (the value passed in is human input, and needs
        to be decremented by 1 first).
        :param index: the column to add a piece to (counting at 1)
        :return: Returns the row the piece finished at
        """
        column = self.board[index]
        token = self.players[self.turn % 2].token
        for i, slot in enumerate(column):
            if slot == ' ':
                self.board[index][i] = token
                #return the row where the piece finished
                return i


    def get_current_player(self):
        return self.players[self.turn % 2]

    def update_player(self):
        self.turn += 1

    def get_board(self):
        """
        passes board to Controller
        :return: the board as a list of lists of strings
        """
        return self.board