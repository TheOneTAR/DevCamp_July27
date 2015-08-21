__author__ = 'TheOneTAR'

from connect4_view import View
from connect4_game import Game

class Connect4:

    def __init__(self):
        self.view = View()
        self.model = Game()


    def create_player(self, token):
        """
        Create a player by prompting for their name,
        and then storing that in the model Game.
        :param token: color this player's pieces will be
        :return:
        """
        name = self.view.get_player_name()
        self.model.add_player(name, token)

