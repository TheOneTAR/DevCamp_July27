class Monster:

   def __init__(self, name, hp):
      self.name = name
      self.hit_points = hp
      self.moves = []

   def attack(self):
      