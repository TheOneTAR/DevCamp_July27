# This is a dice faking module
from random import choice, randint


class Die():

   def __init__(self, possibleValues):
      self.possibleValues = possibleValues
      self.currentValue = choice(self.possibleValues)

   def roll(self):
      num = randint(len(self.possibleValues))
      self.currentValue = self.possibleValues[num]
      return self.currentValue

   def __repr__(self):
      return self.currentValue


