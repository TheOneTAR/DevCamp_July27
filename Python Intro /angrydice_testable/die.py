# This is a dice faking module
from random import choice


class Die():

   def __init__(self, possibleValues):
      self.possibleValues = possibleValues
      self.currentValue = choice(self.possibleValues)

   def roll(self):
      self.currentValue = choice(self.possibleValues)
      return self.currentValue

   def __repr__(self):
      return self.currentValue


