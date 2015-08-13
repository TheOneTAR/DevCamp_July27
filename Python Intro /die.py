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

   def roll_a_bunch(self, max, numOfDice=4):
      rolls = []
      for i in range(numOfDice):
         rolls.append(roll(max))

      return rolls


   def roll_distro(self, max, numOfDice=4):
      #Roll a bunch of dice
      rolls = roll_a_bunch(max, numOfDice)

      distribution = {}

      # count what's rolled
      for each in rolls:
         currentCount = distribution.get(each, 0)
         print("Current count of", each, ":",currentCount)
         currentCount += 1
         distribution[each] = currentCount

      output = ""
      for roll in distribution:
         output += "Number " + str(roll) + " was rolled " + str(distribution[roll]) + " times\n"

      print(output)



