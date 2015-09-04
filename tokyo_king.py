""" An attempt at King of Tokyo. """
from random import randint, shuffle


class TokyoKing(object):
   """The main class for a game of Tokyo King"""
   def __init__(self):
      super(TokyoKing, self).__init__()
      # A List of Monsters
      self.monsters = self.create_monsters()
      self.board = Board(len(self.monsters), self.monsters)
      self.dice = [Die() for i in range(6)]
      self.still_playing = self.monsters[:]
      self.winner = None

      self.play_game()
      

   def create_monsters(self):
      """A function to prompt the players for num players,
      then create the Monsters based on that number,
      prompting for names as you go."""
      num_players = eval(input("How many Monsters are playing? >>> "))
      monsters = []
      for player in range(num_players):
         name = input("Player {}, what is your Monster name? >>> ".format(player+1))
         print("Thank you,", name)
         monsters.append(Monster(name))

      return monsters


   def play_game(self):
      """Starts the game by randomly shuffling the player list
      and prompting the first player to roll the dice."""

      shuffle(self.still_playing)
      
      while len(self.still_playing) > 1:
         for each_monster in self.still_playing:
            print("----------------------------------------------------------")
            print("**********************************************************")
            print("----------------------------------------------------------")
            print("{}, it's your turn.".format(each_monster.name))
            if each_monster.in_tokyo():
               print("You're in Tokyo and earn a point!")
               each_monster.victory_points += 1
            print("You have {} Points and {} Health!".
               format(each_monster.victory_points, each_monster.health))
            roll = 1
            dice_kept = []

            # while rolls < 3 and there are dice to roll
            while roll < 4 and len(dice_kept) < 6:
               # Roll the dice until they get what they want
               self.roll_the_dice(dice_kept, roll)
               
               # Increment the roll counter
               roll += 1

            # Evaluate roll and reset dice
            dice_values = []
            for die in dice_kept:
               dice_values.append(die.value)
               die.keep = False
            self.evaluate_turn(dice_values, each_monster)
            del dice_kept[:]

            # See if anyone has won.
            self.check_winner()
            if self.winner:
               break

            print()

         if self.winner:
            break

      # Congratulate the winner (or announce a tie)
      self.congrats(self.winner)
      # See if they want to play again
      self.play_again()

   def play_again(self):
      """Prompt the users to see if they want to play again.
      If so, reset the Monsters and Board and play again.
      """
      again = " "

      while again:
         again = input("Would you like to play again with the same players? (y/n) >>> ")

         if again.lower() == "y":
            for each_monster in self.monsters:
               each_monster.reset()
            self.board.reset(self.monsters)
            break
         elif again.lower() == "n":
            print("Until next time!")
            exit()
         else:
            print("I didn't quite get that...")

      self.play_game()


   def evaluate_turn(self, dice, monster):
      """Resolves the Monster's turn based on what
      they kept.

      Arguments:
         dice – a list of dice kept
         monster – the Monster whose turn it is
      """
      # Determine if they're in Tokyo or not
      in_tokyo = monster.in_tokyo()

      # If they have a set of 3 numbers,
      # gain that number of points
      for num in [1,2,3]:
         tote_num = dice.count(num)
         if tote_num >= 3:
            extra = (tote_num - 3) * 1
            monster.score(num + extra)

      # If they have H's and are outside Tokyo, 
      # heal that amount
      num_h = dice.count("H")
      if num_h and not in_tokyo:
         monster.heal(num_h)

      # If they have any C's, attack the correct location
      # with that amount of C's
      num_c = dice.count("C")
      if num_c:
         if in_tokyo:
            print()
            self.board.attack_outside(num_c)
         else:
            print()
            self.board.attack_tokyo(num_c, monster)


   def check_winner(self):
      """Checks to see if a winner can be announced.
         If there is a winner, assigns it to self.winner
      """
      # First, see if a player has status of "WINNING"
      for each_monster in self.monsters:
         status = each_monster.status
         if status == "WINNING":
            self.winner = each_monster
            break
         elif status == "K.O.'d":
            print(each_monster.name, " was K.O'd?")
            self.still_playing.remove(each_monster)

         if len(self.still_playing) == 1:
            self.winner = self.still_playing.pop()
            break

   def congrats(self, monster):
      """Prints out the winner or tie condition message."""
      if monster:
         print("--------------------------------------------")
         print("CONGRATULATIONS {}, YOU ARE THE TOKYO KING!!".format(monster.name))
         print("--------------------------------------------")
      else:
         print("----------------------------------------------------------")
         print("ALL THE MONSTERS HAVE BEEN K.O.'d. THERE IS NO KING TODAY.")
         print("----------------------------------------------------------")

   def roll_the_dice(self, dice_kept, roll):
      """Keep prompting the user for their roll and hold
      selections until they've held all the dice, or
      rolled a total of 3 times.

      Arguments:
         dice_kept – list of the dice they've kept
         roll – int representing how many rolls they've taken
      """
      print()
      print("\nRoll {} for you is:".format(roll))
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print()
      # Roll remaining
      self.roll(self.dice)
      
      # Prompt which should be kept
      keep = " "
      while keep != None and len(dice_kept) < 6:
         # Print dice to keep
         self.print_dice(self.dice)

         keep = input("Enter the number of a die you'd like to keep.\n If you've kept all the ones you want, return. >>> ")
         if keep != "" and int(keep) < len(self.dice) :
            keep = int(keep)
            die = self.dice[keep]
            die.keep = not die.keep
            # Keep any they want
            dice_kept.append(die) if die.keep else dice_kept.remove(die)
         elif keep != "":
            print("You've entered a invalid number. Try again.")
         else:
            keep = None

   def roll(self, dice):
      """Helper method to roll all the dice."""
      for die in dice:
         die.roll() 

   def print_dice(self, dice):
      """A helper method that prints out the dice
      all pretty like, with numbers below them.

      Arguments:
         dice – a list of dice to print
      """
      keeping = "Keeping: "
      dice_roll = "         "
      num_roll = "         "
      underline = "         "
      for i,die in enumerate(dice):
         keeping += "  {}   ".format("X" if die.keep else " ")
         dice_roll += "[ {} ] ".format(die.value)
         underline += "------"
         num_roll += " #{}   ".format(i)

      print(keeping)
      print(dice_roll)
      print(underline)
      print(num_roll)



class Board(object):
   """An object representing the Board of King of Tokyo.
   The size of Tokyo is determined by the number of players.

   Arguments:
      num_players – number of players playing
   """
   def __init__(self, num_players, monsters):
      super(Board, self).__init__()
      # A list of the monsters currently in Tokyo
      self.tokyo = self.build_tokyo(num_players)

      # A list of the monsters outside of Tokyo
      self.outside_tokyo = monsters[:]

   def reset(self, monsters):
      self.outside_tokyo = monsters[:]
      self.tokyo = self.build_tokyo(len(monsters))

   def build_tokyo(self, num_players):
      """Build the Tokyo list, determined
      by the number of players.

      Arguments:
         num_players – number of players
      """
      if num_players < 5:
         return [None]
      else:
         return [None, None]

   def attack_tokyo(self, hp, attacker):
      """Attack all the Monsters currently in Tokyo
      for the passed hp amount. Check their status
      and remove any from Tokyo that are K.O.'d.

      Any Monster hit in Tokyo has the option of fleeing,
      forcing the attacker into Tokyo.

      Arguments:
         hp – amount of health to attack with
         attacker – the Monster that is attacking
      """

      # Loop through and hit each Monster in Tokyo
      for i,each_monster in enumerate(self.tokyo):
         if each_monster:
            remaining_health = each_monster.attack(hp)       

            # Check to see if the Monster wants to Flee Tokyo
            if each_monster.flee():
               self.leave_tokyo(each_monster, i)

            # If a monster's remaining health is less than 0, 
            # remove them from Tokyo
            if remaining_health <= 0:
               self.tokyo[i] = None

      # Once all Monsters have been attacked, see if there's
      # a spot in Tokyo. If there is, put the Attacker there.
      for i,spot in enumerate(self.tokyo):
         if spot == None:
            self.enter_tokyo(attacker, i)
            break

   def attack_outside(self, hp):
      """Attack all the Monsters currently outside Tokyo
      for the passed hp amount. Check their status
      and remove any from outside Tokyo that are K.O.'d.

      Arguments:
         hp – amount of health to attack with
      """
      # Loop through and hit each Monster in Tokyo
      for i,each_monster in enumerate(self.outside_tokyo):
         remaining_health = each_monster.attack(hp)       

         # If a monster's remaining health is less than 0, 
         # remove them from Tokyo
         if remaining_health <= 0:
            self.outside_tokyo[i] = None

   def enter_tokyo(self, monster, spot=0):
      """Enter Tokyo with the passed Monster.
      That Monster recieves 2 points for entering Tokyo.

      Arguments:
         monster – the Monster entering Tokyo
         spot – the spot in Tokyo the Monster is entering
      """
      # Remove the Monster from outside_tokyo
      self.outside_tokyo.remove(monster)
      # Put the Monster into Tokyo
      self.tokyo[spot] = monster
      monster.status = "In Tokyo"
      print("{}, you enter Tokyo! You earn 2 points.".format(monster.name))
      #Adjust their score accordingly
      monster.victory_points += 2

   def leave_tokyo(self, monster, spot=0):
      """Enter Tokyo with the passed Monster.
      That Monster recieves 2 points for entering Tokyo.

      Arguments:
         monster – the Monster entering Tokyo
         spot – the spot in Tokyo the Monster is leaving
      """
      self.outside_tokyo.append(monster)
      monster.status = "Out of Tokyo"
      self.tokyo[spot] = None
      print("{}, you leave Tokyo!".format(monster.name))


class Monster(object):
   """The Monster class for King of Tokyo.

   Arguments:
      Name – the name you want for your monster"""
   def __init__(self, name):
      super(Monster, self).__init__()
      self.name = name
      self.reset()

   def reset(self):
      """Reset the Monster to initial values."""
      self.status = "Out of Tokyo"
      self.health = 10
      self.victory_points = 0

   def in_tokyo(self):
      """Helper method that returns True if Monster is in Tokyo"""
      return True if self.status == "In Tokyo" else False

   def flee(self):
      """Prompt the Monster to see if they want to 
      flee Tokyo. This is called after the mosnter has
      been hit while in Tokyo.

      Return:
         True if they wish to flee, False otherwise
      """
      flee_tokyo = input("{}, you've been hit! You have {} HP left. Do you want to flee Tokyo? (y/n) >>> "
         .format(self.name, self.health))

      if (flee_tokyo.lower() == "y"):
         print("You flee Tokyo!")
         return True
      else:
         print("You dare to remain in Tokyo!")
         return False

   def heal(self, hp):
      """Heal the monster by a passed amount of hp.
      The monster's health cannot exceed 10hp.

      Arguments:
         hp – amount to be added to health
      """

      if (hp + self.health < 10):
         self.health += hp
      else:
         self.health = 10

      print("You heal {}, for a total of {}, {}!"
         .format(hp, self.health, self.name))

   def attack(self, hp):
      """Attack the monster for a passed amount of hp.
      If the monster's health drops below 0, they are
      out of the game and their status is updated.

      Arguments:
         hp – amount to be removed from health

      Return:
         Remaining health of the monster
      """
      self.health -= hp

      print("{}, you were attacked for {}! Your health is now {}!"
         .format(self.name, hp, self.health))

      if (self.health <= 0):
         print("Oh no! You were K.O.'d!!")
         self.status = "K.O.'d"

      return self.health

   def score(self, points):
      """Update the monster's score with whatever points
      are passed. If the monster hits 20 points, they win.

      Arguments:
         points – points to be added to victory_points

      Return:
         Total points of the monster
      """
      self.victory_points += points

      if (self.victory_points >= 20):
         self.status = "WINNING"

      print("Woohoo! You scored {} points, bringing your total to {}, {}."
         .format(points, self.victory_points, self.name))

      return self.victory_points


class Die(object):
   """A basic Tokyo King Dice"""
   # The possible values of the die
   DIE_VALUES = [1, 2, 3, "H", 1, "C"]

   def __init__(self):
      super(Die, self).__init__()
      self.value = 1
      self.keep = False

   def roll(self):
      if not self.keep:
         self.value = self.DIE_VALUES[randint(0,5)]
      return self.value

   def __str__(self):
      return self.value

   def __repr__(self):
      return self.value



if __name__ == '__main__':
  game = TokyoKing()
