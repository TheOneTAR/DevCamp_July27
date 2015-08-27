__author__ = 'TheOneTAR'

from angry_dice import AngryDie

class AngryModel:

    def __init__(self):
        self.stage = 1
        self.die_a = AngryDie()
        self.die_b = AngryDie()
        self.cheating = False

    def change_stage(self, new_stage):
        if new_stage > 0 or new_stage < 5:
            self.stage = new_stage

    def get_stage(self):
        return self.stage