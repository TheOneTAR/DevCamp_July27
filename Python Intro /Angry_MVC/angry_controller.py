__author__ = 'TheOneTAR'

from angry_view import AngryView
from angry_view_mobile import AngryMobileView
from angry_model import AngryModel

class AngryController():

    def __init__(self, screen_size):
        self.model = AngryModel()

        if screen_size == "small":
            self.view = AngryMobileView()
        else:
            self.view = AngryView()

    def start_game(self):
        self.view.show_instructions()

    def check_game_state(self):
        if self.model.die_a_value() == 1 and self.model.die_b_value() == 2:
            self.model.change_stage(2)


if __name__ == '__main__':
    angry = AngryController("large")
    angry.start_game()