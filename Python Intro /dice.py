from random import randint

class Die(object):

   """A class for making dice of different sizes 
   and rolling them."""

   diceRolls = []

   def __init__(self, numSides):
      self.numSides = numSides
      self.currentValue = 1
      self.color = "white"

   def roll(self):
      self.currentValue = randint(1, self.numSides)
      if self.currentValue == 1:
         self.shame()
      if self.currentValue == self.numSides:
         print("WINNING")
      Die.diceRolls.append(self.currentValue)
      return self.currentValue

   def cheat(self, value):
      if value <= self.numSides and value > 0:
         self.currentValue = value
      return self.currentValue

   def change_color(self, color):
      self.color = color

   def shame(self):
      print("You have shamed us on this day. I will never forgive you.")

