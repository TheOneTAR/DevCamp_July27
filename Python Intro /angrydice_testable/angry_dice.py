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
      """ Overrides Die.roll() so that in addition to
      rolling the dice, it sets the die's value based on
      the currentValue.
      """
      self.currentValue = choice(self.possibleValues)
      self.value = AngryDie.ANGRY_VALUES[self.currentValue]
      return self.currentValue

   def setDieFaceValue(self, faceValue):
      """ A helper method that, given a valid faceValue,
       will update the die's currentValue and value to match
       the passed faceValue.
       """
      if faceValue in AngryDie.ANGRY_VALUES:
         self.currentValue = faceValue
         self.value = AngryDie.ANGRY_VALUES[faceValue]


class AngryDiceGame:
   """An Angry Dice Game that allows a single player to play Angry Dice."""

   def __init__(self):
      self.die_a = AngryDie()
      self.die_b = AngryDie()
      self.cheating = False
      self.current_stage = 1

   def main(self):
      """ Drive the Angry Dice game for the user.
      Welcomes them to the game and prints the instructions,
      then prompts them with the die values and what they want to roll
      until they advance through all the stages and win."""

      text = "Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n" \
             "Stage 1 you need to roll 1 & 2\n" \
             "Stage 2 you need to roll ANGRY & 4\n" \
             "Stage 3 you need to roll 5 & 6\n" \
             "You can lock a die needed for your current stage \n" \
             "and just roll the other one, but beware!\n" \
             "If you ever get 2 ANGRY's at once, you have to restart to Stage 1!\n" \
             "Also, you can never lock a 6! That's cheating!\n\n" \
             "To roll the dice, simply input the name of the die you want to roll.\n" \
             "Their names are a and b.\n"
      print(text)
      input("Press ENTER to start!")

      # Check to see if we advance in stage
      self.check_stage()

      #Show inital state of the game
      self.print_dice()

      while self.current_stage != 4:
         # Prompt user what to reroll
         dice = self.determine_roll()

         # Check for cheating
         self.check_cheating(dice)

         # Roll the dice
         self.roll_the_dice(dice)

         # Check for ANGRY
         self.check_angry()

         # Check to see if we advance in stage
         self.check_stage()

         # Print the dice
         self.print_dice()


      # Congratulate them on winning
      print("You've won! Calm down!")

   def roll_the_dice(self, dice):
      """ Roll the dice passed in the list."""
      if type(dice) == list:
         for die in dice:
            die.roll()

   def print_dice(self):
      """ Print both die values, as well as the current stage."""

      stage_to_print = 3 if self.current_stage == 4 else self.current_stage
      print("You rolled:\n   a = [  {}  ]\n   b = [  {}  ]\n\nYou are in Stage {}"
         .format(self.die_a, self.die_b, stage_to_print))

   def determine_roll(self):
      """Prompt the user for input, and return the dice they want to roll."""
      dice_to_roll = []
      to_roll = input("Roll dice: ")
      if 'a' in to_roll:
         dice_to_roll.append(self.die_a)

      if 'b' in to_roll:
         dice_to_roll.append(self.die_b)

      return dice_to_roll

   def check_stage(self):
      """ Check the state of the game and if conditions are met to
      advance the player to the next stage.
      """

      #Initalize target and goal_stage to stage1 values
      target = 3
      goal_stage = 2

      # Set target and goal_stage if current stage is not 1
      if self.current_stage == 2:
         target = 7
         goal_stage = 3
      elif self.current_stage == 3:
         target = 11
         goal_stage = 4

      # Check the stage goals
      if self.die_a.value + self.die_b.value == target and not self.cheating:
         self.current_stage = goal_stage

   def check_angry(self):
      """Checks to see if both dice are Angry, if so, sets current_stage to 1"""
      if self.die_a.value == 3 and self.die_b.value == 3:
         print("WOW, you're ANGRY!\nTime to go back to Stage 1!")
         self.current_stage = 1


   def check_cheating(self, dice=[]):
      """" In Stage 3, they can only hold a 5 valued die.
      If they hold a 6, they'll be found cheating and thus,
      cannot win, or advance to the next stage.
      """

      #Assume they're not cheating until proven guilty
      self.cheating = False

      if self.current_stage == 3:
         if self.die_a not in dice and (self.die_a.value == 6):
            print("You're cheating! You cannot lock a 6! You cannot win "
                  "until you reroll it!")
            self.cheating = True
         elif self.die_b not in dice and (self.die_b.value == 6):
            print("You're cheating! You cannot lock a 6! You cannot win "
                  "until you reroll it!")
            self.cheating = True




if __name__ == '__main__':
   game = AngryDiceGame()
   game.main()