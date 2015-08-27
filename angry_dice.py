#An Angry Game
from die import Die
from random import choice


class AngryDie(Die):
   """Implement a new type of Die, called AngryDie"""

   ANGRY_VALUES = {"1":1, "2":2, "ANGRY":3, "4":4, "5":5, "6":6}
         

   def __init__(self):
      self.keys = list(AngryDie.ANGRY_VALUES.keys())
      super(AngryDie, self).__init__(self.keys)
      self.value = AngryDie.ANGRY_VALUES[self.currentValue]

   def roll(self):
      self.currentValue = choice(self.possibleValues)
      self.value = AngryDie.ANGRY_VALUES[self.currentValue]
      return self.currentValue


class AngryDiceGame:
   """An Angry Dice Game that allows a single player to play Angry Dice."""

   def __init__(self):
      self.die_a = AngryDie()
      self.die_b = AngryDie()
      self.stages = [self.stage1,self.stage2,self.stage3]
      self.cheating = False
      self.current_stage = 0

      self.angry_start()

   def angry_start(self):
      text = "Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n"
      text += "Stage 1 you need to roll 1 & 2\n"
      text += "Stage 2 you need to roll ANGRY & 4\n"
      text += "Stage 3 you need to roll 5 & 6\n"
      text += "You can lock a die needed for your current stage \n"
      text += "and just roll the other one, but beware!\n"
      text += "If you ever get 2 ANGRY's at once, you have to restart to Stage 1!\n"
      text += "Also, you can never lock a 6! That's cheating!\n\n"
      text += "To roll the dice, simply input the name of the die you want to roll.\n"
      text += "Their names are a and b.\n"
      print(text)
      input("Press ENTER to start!")

      while self.current_stage != 3:
         print(self.current_stage)
         self.stages[self.current_stage]()

      print("You've won! Calm down!")

   def roll_the_dice(self, dice):
      for die in dice:
         die.roll()

   def print_dice(self):
      print("You rolled:\n   a = [  {}  ]\n   b = [  {}  ]\n\nYou are in Stage {}"
         .format(self.die_a, self.die_b, self.current_stage))

   def what_to_roll(self):
      return input("Hold on a minute")

   def do_things(self, dice):
      # Roll the dice
      self.roll_the_dice(dice)
      self.print_dice()

      print(self.current_stage)
      # Check for ANGRY
      if self.check_angry():
         self.current_stage = -1
         return False
      # Prompt user what to reroll
      dice = self.what_to_roll()

      # Check for cheating
      self.check_cheating(dice)
      return True

   def stage1(self):
      dice = [self.die_a, self.die_b]
      # Do what needs to be done to get us to... STAGE 2
      while self.die_a.value + self.die_b.value != 3 and not self.cheating:
         if not self.do_things(dice):
            break

      self.current_stage += 1

   def stage2(self):

      dice = [self.die_a, self.die_b]
      # Do what needs to be done to get us to... STAGE 3
      while self.die_a.value + self.die_b.value != 7 and not self.cheating:
         if not self.do_things(dice):
            break
      self.current_stage += 1

   def stage3(self):

      dice = [self.die_a, self.die_b]
      # Do what needs to be done to get us to... VICTORY
      while self.die_a.value + self.die_b.value != 11 and not self.cheating:
         if not self.do_things(dice):
            break
      self.current_stage += 1

      
   def check_angry(self):
      if self.die_a.value == 3 and self.die_b.value == 3:
         print("WOW, you're ANGRY!\nTime to go back to Stage 1!")
         return True
      return False

   def check_cheating(self, dice):
      #Stage 1, they can only hold a 1 or 2
      if self.current_stage == 0:
         if self.die_a not in dice and (die_a.value != 1 or die_a != 2):
            self.cheating = True
         elif self.die_b not in dice and (die_b.value != 1 or die_b != 2):
            self.cheating = True
         else:
            self.cheating = False
      #stage 2, they can only hold a 4 or 3
      if self.current_stage == 1:
         if self.die_a not in dice and (die_a.value != 3 or die_a != 4):
            self.cheating = True
         elif self.die_b not in dice and (die_b.value != 3 or die_b != 4):
            self.cheating = True
         else:
            self.cheating = False
      #Stage 3, they can only hold a 5
      if self.current_stage == 2:
         if self.die_a not in dice and (die_a.value != 5):
            self.cheating = True
         elif self.die_b not in dice and (die_b.value != 5):
            self.cheating = True
         else:
            self.cheating = False


if __name__ == '__main__':
  game = AngryDiceGame()
